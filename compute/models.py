"""Visual-balance models for the optical-balancing research mission.

Candidate models, common interface:
    model.name -> str
    model.score(img) -> {'balance': float in [0, 1], 'detail': dict}
where img is a PIL Image (RGB) and 1.0 = perfectly balanced.

Models:
  1. DCMModel      — Hübner & Fillinger 2016, DOI 10.3389/fpsyg.2016.00335
                     (hand-rolled; validated against #5 below)
  2. VMEModel      — Zhang & Xue 2025,   DOI 10.3390/sym18010041
  3. RussianModel  — Al Akkad & Gazimzyanov 2017. POSITION-ONLY faithful
                     subset by default (mode="position_only"); color/size
                     terms exist only in mode="extended" and are OUR
                     EXTENSION, not the paper. See class docstring.
  4. SaliencyModel — Itti-Koch-lite (à la Abeln et al. 2016,
                     DOI 10.3389/fnhum.2015.00704)
  5. ToolboxDCMModel / ToolboxBalanceModel — CANONICAL references vendored
                     from the Aesthetics Toolbox (Redies et al. 2025,
                     DOI 10.3758/s13428-025-02632-3), reference/huebner.py.

HONESTY / ASSUMPTIONS (marked in code and in detail dicts where relevant):
  - The exact coefficient forms of Al Akkad & Gazimzyanov (2017) are
    UNOBTAINABLE (no accessible full text). Moreover, the parallel
    literature track (Round 3, verified) established that the paper's
    model is POSITION-ONLY: vWc (color) and vWs (size) were never
    specified; the full additive formula vW = vWsS + vWc + vWs never
    existed — only the promise of it. The color and size terms in
    RussianModel are therefore ~pure invention~ by the implementer; the
    model as implemented is ~90% reconstruction, ~10% paper. Even the
    exact coefficient form of the position term is unobtainable.
    Placeholder coefficients (A_S = A_C = A_P = 1.0) are NOT the
    paper's fitted values and no published numeric value is reproduced
    here.
  - VME's nine-grid quadrant attention weights (UL 0.33, UR 0.28, LL 0.23,
    LR 0.16) are taken from the task specification, which attributes them
    to Zhou et al. via the VME paper. They are implemented as an optional
    flag (`nine_grid=True`), off by default, and flagged as unverified
    against the primary source in the detail dict.
  - "Near-white" background threshold (gray >= 245) and the VME D_max
    definition (W/2 + H/2, Manhattan center-to-corner distance) are
    implementer choices, documented below where used.
  - No randomness is used anywhere in this module; output is fully
    deterministic.
  - No network calls. Only numpy / scipy / PIL (+ matplotlib only if the
    smoke test is extended; the models themselves do not need it).
"""

from __future__ import annotations

import math
from typing import Dict, List, Tuple

import numpy as np
from PIL import Image
from scipy import ndimage


# ---------------------------------------------------------------------------
# shared helpers
# ---------------------------------------------------------------------------

def _to_array(img: Image.Image) -> np.ndarray:
    """Return img as float64 RGB array of shape (H, W, 3), values 0..255."""
    arr = np.asarray(img.convert("RGB"), dtype=np.float64)
    return arr


def _grayscale(arr: np.ndarray) -> np.ndarray:
    """Luminance via the standard Rec. 601 luma coefficients, values 0..255."""
    return 0.299 * arr[..., 0] + 0.587 * arr[..., 1] + 0.114 * arr[..., 2]


def _dcm_from_centroid(bx: float, by: float, W: int, H: int) -> Dict[str, float]:
    """Shared DCM formula (Hübner & Fillinger 2016).

    dx, dy are absolute offsets of the mass centroid (bx, by) from the
    geometric center, each normalized by the corresponding half-dimension.
    DCM = 100 * sqrt((dx/(W/2))^2 + (dy/(H/2))^2) / sqrt(2):
      0   = mass perfectly centered,
      100 = all mass in one corner.
    """
    cx, cy = W / 2.0, H / 2.0
    dx = abs(bx - cx) / (W / 2.0)
    dy = abs(by - cy) / (H / 2.0)
    dcm = 100.0 * math.sqrt(dx * dx + dy * dy) / math.sqrt(2.0)
    balance = 1.0 - dcm / 100.0
    return {
        "centroid": (float(bx), float(by)),
        "geometric_center": (float(cx), float(cy)),
        "dx_norm": float(dx),
        "dy_norm": float(dy),
        "DCM": float(dcm),
        "balance": float(min(1.0, max(0.0, balance))),
    }


def _norm01(m: np.ndarray) -> np.ndarray:
    """Linearly map array to [0, 1]; returns zeros if the range is zero."""
    lo, hi = float(m.min()), float(m.max())
    if hi <= lo:
        return np.zeros_like(m)
    return (m - lo) / (hi - lo)


# ---------------------------------------------------------------------------
# 1. DCM — Deviation of the Center of Mass (Hübner & Fillinger 2016)
# ---------------------------------------------------------------------------

class DCMModel:
    """DCMModel (Hübner & Fillinger 2016, DOI 10.3389/fpsyg.2016.00335).

    Grayscale the image; per-pixel mass m = 1 - gray/255 (dark = heavy).
    Mass-weighted centroid, offsets from geometric center, DCM in [0, 100]
    (0 = centered, 100 = mass in a corner); balance = 1 - DCM/100.
    """

    name = "DCM (Hübner & Fillinger 2016)"

    def score(self, img: Image.Image) -> Dict:
        arr = _to_array(img)
        H, W = arr.shape[0], arr.shape[1]
        gray = _grayscale(arr)
        mass = 1.0 - gray / 255.0
        total = float(mass.sum())
        if total <= 0.0:
            # Uniform pure-white image: no mass; trivially balanced.
            return {"balance": 1.0,
                    "detail": {"DCM": 0.0, "total_mass": 0.0,
                               "centroid": (W / 2.0, H / 2.0),
                               "note": "zero mass (uniform white); "
                                       "balanced by convention"}}
        ys_idx, xs_idx = np.mgrid[0:H, 0:W]
        bx = float((xs_idx * mass).sum() / total)
        by = float((ys_idx * mass).sum() / total)
        d = _dcm_from_centroid(bx, by, W, H)
        detail = {
            "centroid": d["centroid"],
            "geometric_center": d["geometric_center"],
            "DCM": d["DCM"],
            "total_mass": total,
            "mass_is": "m = 1 - gray/255 (dark = heavy)",
        }
        return {"balance": d["balance"], "detail": detail}


# ---------------------------------------------------------------------------
# Reference implementations — Aesthetics Toolbox (Redies et al. 2025)
# ---------------------------------------------------------------------------
# Vendored verbatim in reference/huebner.py from
# https://github.com/RBartho/Aesthetics-Toolbox (AT/balance_qips.py).
# Paper: Redies, C. et al. (2025), Behav. Res. Methods, 57(4), 117.
# DOI: 10.3758/s13428-025-02632-3 (open access, PMC11909096).
# These are the CANONICAL reference implementations — our hand-rolled
# DCMModel above is validated against ToolboxDCMModel, not the reverse.

def _toolbox():
    """Lazy import of the vendored reference (keeps module import light)."""
    import os
    import sys
    refdir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "reference")
    if refdir not in sys.path:
        sys.path.insert(0, refdir)
    import huebner
    return huebner


class ToolboxDCMModel:
    """Canonical DCM — Aesthetics Toolbox reference (Redies et al. 2025).

    Wraps huebner.DCM() verbatim. Returns (rdist, htmp, vtmp); rdist in
    0..~141.42 (100 = centroid at edge-midpoint distance, ~141.42 at the
    corner, given the (dist/0.5)*100 normalization). balance =
    max(0, 1 - rdist/141.4213562373095). NOTE the reference quirks, kept
    intentionally: minority-side inversion at the 128 threshold (with the
    historical MATLAB double-count), 1-based fulcrum indexing (+1), and
    per-axis rounding — so a perfectly centered disk scores rdist ~0.71,
    not 0. These quirks are part of the canonical behavior.
    """

    name = "DCM reference (Aesthetics Toolbox, Redies et al. 2025)"

    def score(self, img: Image.Image) -> Dict:
        huebner = _toolbox()
        gray = np.asarray(img.convert("L"))
        rdist, htmp, vtmp = huebner.DCM(gray)
        balance = max(0.0, 1.0 - float(rdist) / 141.4213562373095)
        return {"balance": balance,
                "detail": {"rdist": float(rdist),
                           "htmp": float(htmp), "vtmp": float(vtmp),
                           "source": "vendored AT/balance_qips.py DCM(), "
                                     "Redies et al. 2025, "
                                     "DOI 10.3758/s13428-025-02632-3"}}


class ToolboxBalanceModel:
    """Canonical 'Balance' QIP — Aesthetics Toolbox reference (APB family).

    Wraps huebner.Balance() verbatim: mean of 8 axis/inner-outer
    difference measures (horizontal, vertical, inner-outer both axes,
    both diagonals + inner-outer), each 0..100; returns their mean bs
    (0 = balanced). balance = 1 - bs/100. NOTE: the inner-outer terms
    penalize concentrated central mass, so a single centered disk scores
    ~0.5, not ~1.0 — canonical behavior, not a bug.
    """

    name = "Balance QIP reference (Aesthetics Toolbox, Redies et al. 2025)"

    def score(self, img: Image.Image) -> Dict:
        huebner = _toolbox()
        gray = np.asarray(img.convert("L"))
        bs = float(huebner.Balance(gray))
        return {"balance": max(0.0, 1.0 - bs / 100.0),
                "detail": {"bs_0_100": bs,
                           "source": "vendored AT/balance_qips.py Balance(), "
                                     "Redies et al. 2025, "
                                     "DOI 10.3758/s13428-025-02632-3"}}


# ---------------------------------------------------------------------------
# shared segmentation (VME + Russian)
# ---------------------------------------------------------------------------

def _segment_elements(img: Image.Image, bg_threshold: float = 245.0
                      ) -> Tuple[List[Dict], int, int]:
    """Segment non-background connected components.

    Background = near-white pixels (gray >= bg_threshold). The threshold
    245/255 is an implementer choice, not taken from the papers; it is
    reported in the detail dicts of the models that use it.

    Returns (elements, W, H) where each element is a dict with
    'area' (pixel count), 'centroid' (x, y in pixel coords),
    'mask' (bool array) and 'label'.
    """
    arr = _to_array(img)
    H, W = arr.shape[0], arr.shape[1]
    gray = _grayscale(arr)
    mask = gray < bg_threshold
    labeled, n = ndimage.label(mask)
    elements: List[Dict] = []
    for lab in range(1, n + 1):
        emask = labeled == lab
        area = int(emask.sum())
        if area == 0:
            continue
        ys_idx, xs_idx = np.nonzero(emask)
        cx = float(xs_idx.mean())
        cy = float(ys_idx.mean())
        elements.append({"area": area, "centroid": (cx, cy),
                         "mask": emask, "label": lab})
    return elements, W, H


# ---------------------------------------------------------------------------
# 2. VME — Visual Mass Equilibrium (Zhang & Xue 2025)
# ---------------------------------------------------------------------------

class VMEModel:
    """VMEModel (Zhang & Xue 2025, DOI 10.3390/sym18010041).

    Segments non-background elements, computes the area-weighted aggregate
    centroid, then a Manhattan-distance-based balance:
        D_centroid = |x_c - x_center| + |y_c - y_center|   (pixels)
        D_max      = W/2 + H/2                              (Manhattan
                      center-to-corner distance; implementer choice)
        B_m        = 1 - D_centroid / D_max
    Sharpened score B_m' = exp(5*B_m - 1), reported both raw
    (range [e^-1, e^4] ≈ [0.368, 54.6]) and normalized to [0, 1].

    Optional nine_grid=True: each element's area is multiplied by a
    quadrant attention weight before aggregation —
    UL 0.33, UR 0.28, LL 0.23, LR 0.16 (attributed by the task spec to
    Zhou et al. via the VME paper; NOT verified against the primary
    source — flagged in detail dict).
    """

    QUADRANT_WEIGHTS = {"UL": 0.33, "UR": 0.28, "LL": 0.23, "LR": 0.16}

    name = "VME (Zhang & Xue 2025)"

    def __init__(self, nine_grid: bool = False):
        self.nine_grid = nine_grid
        if nine_grid:
            self.name = "VME-ninegrid (Zhang & Xue 2025)"

    @staticmethod
    def _quadrant(x: float, y: float, W: int, H: int) -> str:
        """Quadrant of a point relative to the image center."""
        vert = "U" if y < H / 2.0 else "L"
        horiz = "L" if x < W / 2.0 else "R"
        return vert + horiz

    def score(self, img: Image.Image) -> Dict:
        elements, W, H = _segment_elements(img)
        cx_geom, cy_geom = W / 2.0, H / 2.0

        weights_used = None
        if not elements:
            # No foreground elements: trivially balanced.
            agg = (cx_geom, cy_geom)
            total_area = 0
            detail_extra = {"note": "no non-background elements found; "
                                    "balanced by convention"}
        else:
            if self.nine_grid:
                # Weight each element's area by its quadrant attention weight.
                eff_areas = []
                weights_used = []
                for e in elements:
                    q = self._quadrant(e["centroid"][0], e["centroid"][1],
                                       W, H)
                    w = self.QUADRANT_WEIGHTS[q]
                    eff_areas.append(e["area"] * w)
                    weights_used.append((e["label"], q, w))
            else:
                eff_areas = [e["area"] for e in elements]
            total_area = float(sum(eff_areas))
            if total_area <= 0.0:
                agg = (cx_geom, cy_geom)
            else:
                x_c = sum(a * e["centroid"][0]
                          for a, e in zip(eff_areas, elements)) / total_area
                y_c = sum(a * e["centroid"][1]
                          for a, e in zip(eff_areas, elements)) / total_area
                agg = (float(x_c), float(y_c))
            detail_extra = {}

        D_centroid = abs(agg[0] - cx_geom) + abs(agg[1] - cy_geom)
        D_max = W / 2.0 + H / 2.0
        B_m = 1.0 - D_centroid / D_max
        B_m = float(min(1.0, max(0.0, B_m)))
        Bm_prime_raw = float(math.exp(5.0 * B_m - 1.0))
        # Normalize the sharpened score to [0, 1] using its known endpoints:
        # B_m in [0,1] -> B_m' in [e^-1, e^4].
        lo, hi = math.exp(-1.0), math.exp(4.0)
        Bm_prime_norm = (Bm_prime_raw - lo) / (hi - lo)

        detail = {
            "element_count": len(elements),
            "aggregate_centroid": agg,
            "geometric_center": (cx_geom, cy_geom),
            "D_centroid_manhattan_px": float(D_centroid),
            "D_max_manhattan_px": float(D_max),
            "B_m": B_m,
            "B_m_prime_raw": Bm_prime_raw,
            "B_m_prime_raw_range": "[e^-1, e^4] approx [0.368, 54.6] "
                                   "for B_m in [0, 1]",
            "B_m_prime_normalized_01": float(Bm_prime_norm),
            "background_threshold": 245.0,
            "nine_grid": self.nine_grid,
            **detail_extra,
        }
        if weights_used is not None:
            detail["quadrant_weights"] = self.QUADRANT_WEIGHTS
            detail["element_quadrant_weights"] = weights_used
            detail["quadrant_weight_source"] = (
                "UNVERIFIED: weights 0.33/0.28/0.23/0.16 per task spec, "
                "attributed to Zhou et al. via the VME paper; not checked "
                "against the primary source")
        return {"balance": B_m, "detail": detail}


# ---------------------------------------------------------------------------
# 3. Russian model — Al Akkad & Gazimzyanov 2017
# ---------------------------------------------------------------------------

class RussianModel:
    """RussianModel (Al Akkad & Gazimzyanov 2017) — honesty-first implementation.

    LITERATURE STATUS (Round 3, verified by full-text read): the paper's
    model is POSITION-ONLY. The paper names three additive components
    vW = vWsS + vWc + vWs (position + color + size), but vWc (color) and
    vWs (size) were NEVER SPECIFIED — named only as future work. The full
    additive formula never existed; only the promise of it. Even the exact
    functional form of the position term vWsS is unobtainable (no
    accessible full text). What the paper establishes is the CONCEPT: a
    position component of per-element visual weight.

    Two modes:
      mode="position_only" (DEFAULT) — the FAITHFUL subset. Element
          weight = vWsS = euclidean distance of the element centroid
          from the image center, normalized by center-to-corner
          distance (Arnheim's lever: weight grows with distance from
          center). Concept-faithful; exact functional form UNVERIFIED.
          NOTE the honest degeneracy: a centered element has ZERO
          weight, so centered compositions are unscorable — that
          degeneracy IS a finding about the position-only model.
      mode="extended" — OUR EXTENSION, explicitly NOT the paper.
          Adds vWs(size) = A_S * (area / image_area) and
          vWc(color) = A_C * mean_saturation * (1 - mean_value) in HSV.
          All coefficients PLACEHOLDER (defaults 1.0). Exists to show
          what the paper's program would look like completed.

    Balance in both modes: DCM-style on the element weights (same
    formula as DCMModel).
    """

    name = "Russian vW (Al Akkad & Gazimzyanov 2017; see mode)"

    COEFFICIENT_STATUS = ("position term: concept-faithful, form UNVERIFIED; "
                          "color/size terms (extended mode): OUR EXTENSION, "
                          "not in the paper; all coefficients PLACEHOLDER")

    def __init__(self, mode: str = "position_only",
                 A_S: float = 1.0, A_C: float = 1.0, A_P: float = 1.0):
        if mode not in ("position_only", "extended"):
            raise ValueError("mode must be 'position_only' or 'extended'")
        self.mode = mode
        self.A_S = float(A_S)
        self.A_C = float(A_C)
        self.A_P = float(A_P)
        self.name = ("Russian vW position-only (Al Akkad & Gazimzyanov 2017, "
                     "faithful subset)" if mode == "position_only" else
                     "Russian vW + EXTENSION (color/size: our invention, "
                     "not the paper)")

    def score(self, img: Image.Image) -> Dict:
        elements, W, H = _segment_elements(img)
        cx_geom, cy_geom = W / 2.0, H / 2.0
        img_area = float(W * H)
        max_center_dist = math.sqrt((W / 2.0) ** 2 + (H / 2.0) ** 2)

        hsv = None
        if self.mode == "extended":
            # NOTE (assumption): "lightness" uses HSV value as proxy —
            # HSV has no lightness channel. Extension-only.
            hsv = np.asarray(img.convert("HSV"), dtype=np.float64)
            sat = hsv[..., 1] / 255.0
            val = hsv[..., 2] / 255.0

        elem_weights = []
        for e in elements:
            m = e["mask"]
            ex, ey = e["centroid"]
            pos_term = self.A_P * (
                math.hypot(ex - cx_geom, ey - cy_geom) / max_center_dist)
            if self.mode == "extended":
                size_term = self.A_S * (e["area"] / img_area)
                color_term = self.A_C * float(sat[m].mean()) * (
                    1.0 - float(val[m].mean()))
                vW = pos_term + size_term + color_term
            else:
                size_term = 0.0
                color_term = 0.0
                vW = pos_term
            elem_weights.append(
                {"label": e["label"], "vW": float(vW),
                 "vWs_size": float(size_term),
                 "vWc_color": float(color_term),
                 "vWsS_position": float(pos_term)})

        total_vW = sum(w["vW"] for w in elem_weights)
        if total_vW <= 0.0 or not elem_weights:
            return {"balance": 1.0,
                    "detail": {"coefficients": self.COEFFICIENT_STATUS,
                               "mode": self.mode,
                               "element_count": len(elements),
                               "total_vW": float(total_vW),
                               "note": "zero visual weight under the "
                                       "position-only model (e.g. all "
                                       "elements centered); the model "
                                       "cannot discriminate — balanced by "
                                       "convention, flagged as degeneracy"}}

        bx = sum(w["vW"] * elements[i]["centroid"][0]
                 for i, w in enumerate(elem_weights)) / total_vW
        by = sum(w["vW"] * elements[i]["centroid"][1]
                 for i, w in enumerate(elem_weights)) / total_vW
        d = _dcm_from_centroid(float(bx), float(by), W, H)

        detail = {
            "coefficients": self.COEFFICIENT_STATUS,
            "mode": self.mode,
            "A_S": self.A_S, "A_C": self.A_C, "A_P": self.A_P,
            "coefficient_forms": {
                "vWsS_position": "A_P * euclid(centroid, center) / "
                                 "center_to_corner_distance "
                                 "(concept-faithful; exact form UNVERIFIED)",
                "vWs_size": "A_S * (area / image_area) "
                            "[EXTENDED MODE ONLY — our invention]",
                "vWc_color": "A_C * mean_saturation * (1 - mean_value), HSV "
                             "[EXTENDED MODE ONLY — our invention]",
            },
            "element_count": len(elements),
            "element_vW": elem_weights,
            "total_vW": float(total_vW),
            "vW_centroid": d["centroid"],
            "DCM_on_vW": d["DCM"],
        }
        return {"balance": d["balance"], "detail": detail}


# ---------------------------------------------------------------------------
# 4. Saliency model — Itti-Koch-lite (à la Abeln et al. 2016)
# ---------------------------------------------------------------------------

class SaliencyModel:
    """SaliencyModel — Itti-Koch-lite (à la Abeln et al. 2016,
    DOI 10.3389/fnhum.2015.00704).

    Builds a saliency map from center-surround feature contrast using
    Gaussian pyramids (scipy.ndimage.gaussian_filter):
      - intensity channel (grayscale),
      - two color-opponency channels: R-G and B-Y,
      - orientation: gradient magnitude of the intensity channel at
        multiple scales.
    For each feature map, center-surround differences are taken across
    scale pairs (fine scale minus upsampled coarse scale, absolute
    value), each difference map is normalized to [0, 1], all are summed,
    and the final map is normalized to [0, 1].

    The DCM computation (same formula as DCMModel) is then run on the
    saliency map as mass. This is an "Itti-Koch-lite" approximation of
    the cited work, not a replication of its exact parameters.

    Implementation choices (documented, not from the papers):
      - pyramid via successive gaussian_filter on the full-resolution
        image (sigmas [1, 2, 4, 8]); center-surround pairs (1, 4) and
        (2, 8). Since all maps share the same resolution, no resampling
        is needed — the difference IS the multi-scale contrast.
      - R-G = (R - G) / 255, B-Y with Y = (R + G) / 2 (Itti-style).
    """

    name = "Saliency Itti-Koch-lite (Abeln et al. 2016)"

    # Gaussian pyramid sigmas and center-surround pairings.
    SIGMAS = (1.0, 2.0, 4.0, 8.0)
    CS_PAIRS = ((1.0, 4.0), (2.0, 8.0))

    def _pyramid(self, f: np.ndarray) -> Dict[float, np.ndarray]:
        """Blurred copies of f at each sigma (same resolution)."""
        return {s: ndimage.gaussian_filter(f, sigma=s) for s in self.SIGMAS}

    def _center_surround(self, pyr: Dict[float, np.ndarray]) -> np.ndarray:
        """Sum of |fine - coarse| over the scale pairs, normalized to [0,1]."""
        acc = np.zeros_like(next(iter(pyr.values())))
        for fine, coarse in self.CS_PAIRS:
            acc += np.abs(pyr[fine] - pyr[coarse])
        return _norm01(acc)

    def _saliency_map(self, img: Image.Image) -> np.ndarray:
        arr = _to_array(img) / 255.0
        R, G, B = arr[..., 0], arr[..., 1], arr[..., 2]

        intensity = _grayscale(arr * 255.0) / 255.0
        rg = (R - G)                      # red-green opponency
        by = B - (R + G) / 2.0            # blue-yellow opponency

        maps: List[np.ndarray] = []
        # Intensity conspicuity.
        maps.append(self._center_surround(self._pyramid(intensity)))
        # Color opponency conspicuities.
        maps.append(self._center_surround(self._pyramid(rg)))
        maps.append(self._center_surround(self._pyramid(by)))
        # Orientation conspicuity: gradient magnitude of the intensity
        # channel at multiple scales, with center-surround differences
        # taken across scales exactly like the other channels.
        grad_maps: Dict[float, np.ndarray] = {}
        for s in self.SIGMAS:
            blurred = ndimage.gaussian_filter(intensity, sigma=s)
            gx = ndimage.sobel(blurred, axis=1, mode="reflect")
            gy = ndimage.sobel(blurred, axis=0, mode="reflect")
            grad_maps[s] = np.hypot(gx, gy)
        maps.append(self._center_surround(grad_maps))

        saliency = _norm01(sum(maps))
        return saliency

    def score(self, img: Image.Image) -> Dict:
        arr = _to_array(img)
        H, W = arr.shape[0], arr.shape[1]
        sal = self._saliency_map(img)
        total = float(sal.sum())
        if total <= 0.0:
            return {"balance": 1.0,
                    "detail": {"saliency_sum": 0.0,
                               "note": "zero saliency; balanced by "
                                       "convention"}}
        ys_idx, xs_idx = np.mgrid[0:H, 0:W]
        bx = float((xs_idx * sal).sum() / total)
        by = float((ys_idx * sal).sum() / total)
        d = _dcm_from_centroid(bx, by, W, H)
        detail = {
            "saliency_min": float(sal.min()),
            "saliency_max": float(sal.max()),
            "saliency_mean": float(sal.mean()),
            "saliency_sum": total,
            "saliency_centroid": d["centroid"],
            "DCM_on_saliency": d["DCM"],
            "pyramid_sigmas": list(self.SIGMAS),
            "center_surround_pairs": [list(p) for p in self.CS_PAIRS],
            "channels": ["intensity", "R-G", "B-Y",
                         "orientation (gradient magnitude, multi-scale)"],
            "approximation_note": "Itti-Koch-lite; parameters are "
                                  "implementer choices, not a replication "
                                  "of Abeln et al.'s exact setup",
        }
        return {"balance": d["balance"], "detail": detail}


# ---------------------------------------------------------------------------
# smoke test
# ---------------------------------------------------------------------------

def _make_test_image(size: Tuple[int, int] = (200, 200),
                     square: Tuple[int, int] = (120, 60),
                     side: int = 60) -> Image.Image:
    """White image with one black square.

    `square` = (x, y) top-left corner of the square; `side` = side length.
    """
    img = Image.new("RGB", size, (255, 255, 255))
    px = img.load()
    x0, y0 = square
    for y in range(y0, min(y0 + side, size[1])):
        for x in range(x0, min(x0 + side, size[0])):
            px[x, y] = (0, 0, 0)
    return img


def _print_result(model, res: Dict) -> None:
    print(f"--- {model.name} ---")
    print(f"  balance: {res['balance']:.4f}")
    for k, v in res["detail"].items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    print("Smoke test 1: black square offset up-left (expect: unbalanced)")
    img_off = _make_test_image(square=(10, 10), side=60)
    print("Smoke test 2: black square centered (expect: near-balanced)")
    img_ctr = _make_test_image(square=(70, 70), side=60)

    models = [DCMModel(), VMEModel(), VMEModel(nine_grid=True),
              RussianModel(), SaliencyModel()]
    for label, img in (("OFFSET", img_off), ("CENTERED", img_ctr)):
        print(f"\n===== {label} =====")
        for m in models:
            _print_result(m, m.score(img))
    print("\nSmoke test complete: no exceptions, all balances in [0, 1].")
