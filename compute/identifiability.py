"""Task 2: six-factor identifiability experiment.

Two-element compositions. Element A = fixed reference (mid-gray disk,
r=40, at (120,200)). Element B varies ONE factor at a time (OFAT):
saturation, hue, lightness, area, horizontal position, contrast-against-ground
(contrast measured from rendered pixels; it varies via luminance even when
HSV value is fixed).

SYNTHETIC GROUND TRUTH (implementer choice, documented):
    w_true(i) = c1*area + c2*sat*area + c3*hue_w*area + c4*(1-val)*area
                + c5*area*pos + c6*contrast*area
    hue_w(h)  = 0.5*(1+cos(2*pi*h/360))   # peaks at red, implementer choice
    pos       = |x_c - 200| / 200          # normalized horizontal eccentricity
    contrast  = |mean_gray_elem - mean_gray_bg| / 255  (luminance-based)
    y         = 1 - |x_w - 200| / 200      # synthetic "balance rating"
with TRUE c = [1.0, 0.5, 0.3, 0.7, 0.4, 0.2].

The fitter sees ONLY rendered pixels: it segments the two elements,
measures the six features from pixels, and fits c2..c6 (c1 = 1.0 fixed as
the scale anchor -- balance ratings are homogeneous of degree 0 in c, so
absolute scale is unidentifiable; only ratios c_k/c_1 are identified).

Breaks:
  (a) truth gains c7*sat*area*(area/A_ref) interaction (c7=0.6); a 3x3
      area-x-sat factorial block is added; purely additive model is fit.
  (b) hue sweep confounded: value ramps with hue (the real-world confound).
  (c) two synthetic observers; observer 2 has c5 sign-flipped
      (reading-direction effect); a single c5 is fit to both.
"""
import colorsys
import json
import math
import os
import sys

import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage
from scipy.optimize import least_squares

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from models import DCMModel, VMEModel, RussianModel, SaliencyModel

SIZE = 400
CX = SIZE / 2.0
A_POS = (120.0, 200.0)
A_R = 40
A_GRAY = 128  # mid-gray reference

TRUE_C = np.array([1.0, 0.5, 0.3, 0.7, 0.4, 0.2])  # c1..c6
FACTOR_NAMES = ["area", "sat", "hue", "dark", "pos", "con"]


def hue_weight(h_deg):
    return 0.5 * (1.0 + math.cos(2.0 * math.pi * h_deg / 360.0))


def rgb_of(h_deg, s, v):
    r, g, b = colorsys.hsv_to_rgb(h_deg / 360.0, s, v)
    return (int(round(r * 255)), int(round(g * 255)), int(round(b * 255)))


def gray_of(rgb):
    return 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]


def render_trial(b_spec):
    """b_spec = dict(h, s, v, r, x). Returns PIL image."""
    img = Image.new("RGB", (SIZE, SIZE), "white")
    d = ImageDraw.Draw(img)
    d.ellipse([A_POS[0] - A_R, A_POS[1] - A_R,
               A_POS[0] + A_R, A_POS[1] + A_R], fill=(A_GRAY,) * 3)
    rgb = rgb_of(b_spec["h"], b_spec["s"], b_spec["v"])
    r, x = b_spec["r"], b_spec["x"]
    d.ellipse([x - r, 200 - r, x + r, 200 + r], fill=rgb)
    return img


def analytic_features(spec, x, r):
    """Ground-truth-side features from generating parameters."""
    area = math.pi * r * r
    return {
        "area": area,
        "sat": spec["s"] * area,
        "hue": hue_weight(spec["h"]) * area,
        "dark": (1.0 - spec["v"]) * area,
        "pos": area * abs(x - CX) / (SIZE / 2.0),
        "con": abs(gray_of(rgb_of(spec["h"], spec["s"], spec["v"])) - 255.0)
               / 255.0 * area,
        "x": x,
    }


def weight_of(feats, c):
    f = np.array([feats["area"], feats["sat"], feats["hue"],
                  feats["dark"], feats["pos"], feats["con"]])
    return float(f @ c)


def measured_features(img):
    """Fitter side: measure the six features of A and B from pixels only."""
    arr = np.asarray(img.convert("RGB"), dtype=np.float64)
    gray = 0.299 * arr[..., 0] + 0.587 * arr[..., 1] + 0.114 * arr[..., 2]
    bg = gray >= 245.0
    bg_gray = float(gray[bg].mean())
    labeled, n = ndimage.label(~bg)
    comps = []
    for lab in range(1, n + 1):
        m = labeled == lab
        ys, xs = np.nonzero(m)
        comps.append({"mask": m, "area": int(m.sum()),
                      "x": float(xs.mean()), "y": float(ys.mean())})
    assert len(comps) == 2, f"expected 2 components, got {len(comps)}"
    # A = component nearest the fixed reference position.
    comps.sort(key=lambda c: abs(c["x"] - A_POS[0]) + abs(c["y"] - A_POS[1]))
    hsv = np.asarray(img.convert("HSV"), dtype=np.float64)
    sat = hsv[..., 1] / 255.0
    val = hsv[..., 2] / 255.0
    hue = hsv[..., 0] / 255.0 * 360.0
    out = []
    for c in comps:
        m = c["mask"]
        area = float(c["area"])
        ms, mv = float(sat[m].mean()), float(val[m].mean())
        mh = float(hue[m].mean())
        mg = float(gray[m].mean())
        out.append({
            "area": area,
            "sat": ms * area,
            "hue": hue_weight(mh) * area,
            "dark": (1.0 - mv) * area,
            "pos": area * abs(c["x"] - CX) / (SIZE / 2.0),
            "con": abs(mg - bg_gray) / 255.0 * area,
            "x": c["x"],
        })
    return out[0], out[1]  # A, B


def balance_from_weights(wA, xA, wB, xB):
    xw = (wA * xA + wB * xB) / (wA + wB)
    return 1.0 - abs(xw - CX) / (SIZE / 2.0), xw


# ---------------------------------------------------------------- sweeps
def b_ref():
    return {"h": 0.0, "s": 0.0, "v": A_GRAY / 255.0, "r": A_R, "x": 280.0}


def build_sweeps(confound_hue_lightness=False):
    """Returns list of (factor, level_label, b_spec)."""
    trials = []
    ref = b_ref()
    # saturation (red hue, mid value)
    for s in [0.0, 0.25, 0.5, 0.75, 1.0]:
        b = dict(ref); b.update(h=0.0, s=s, v=0.5)
        trials.append(("sat", f"s={s}", b))
    # hue (sat .8, mid value) -- or confounded with value
    for i, h in enumerate([0, 60, 120, 180, 240]):
        b = dict(ref); b.update(h=float(h), s=0.8, v=0.5)
        if confound_hue_lightness:
            b["v"] = 0.25 + 0.6 * (h / 240.0)
        trials.append(("hue", f"h={h}" + ("+v_ramp" if confound_hue_lightness else ""), b))
    # lightness (achromatic)
    for v in [0.15, 0.35, 0.55, 0.75, 0.95]:
        b = dict(ref); b.update(h=0.0, s=0.0, v=v)
        trials.append(("dark", f"v={v}", b))
    # area (achromatic mid-gray)
    for r in [24, 32, 40, 48, 56]:
        b = dict(ref); b.update(r=r)
        trials.append(("area", f"r={r}", b))
    # horizontal position (achromatic mid-gray)
    for x in [205, 245, 285, 325, 355]:
        b = dict(ref); b.update(x=float(x))
        trials.append(("pos", f"x={x}", b))
    return trials


def build_factorial():
    """3x3 area x saturation block (for the interaction break)."""
    trials = []
    for r in [28, 40, 52]:
        for s in [0.2, 0.6, 1.0]:
            b = b_ref(); b.update(h=0.0, s=s, v=0.5, r=r)
            trials.append(("areaXsat", f"r={r},s={s}", b))
    return trials


A_SPEC = {"h": 0.0, "s": 0.0, "v": A_GRAY / 255.0}
A_R_ANALYTIC = A_R


def ground_truth_y(trials, c, c7=0.0, flip_pos_sign=False):
    """Synthetic ratings from TRUE generating parameters (fitter never sees)."""
    ys = []
    A_ref_area = math.pi * A_R_ANALYTIC ** 2
    for _, _, b in trials:
        fA = analytic_features(A_SPEC, A_POS[0], A_R_ANALYTIC)
        fB = analytic_features(b, b["x"], b["r"])
        cc = c.copy()
        if flip_pos_sign:
            cc[4] = -cc[4]
        wA = weight_of(fA, cc)
        wB = weight_of(fB, cc)
        if c7:
            wB += c7 * b["s"] * fB["area"] * (fB["area"] / A_ref_area)
        y, _ = balance_from_weights(wA, A_POS[0], wB, b["x"])
        ys.append(y)
    return np.array(ys)


def fit_model(trial_feats, ys, x0, c1_fixed=1.0):
    """Fit c2..c6 (c1 anchored) to ratings; features measured from pixels."""
    def resid(p):
        c = np.array([c1_fixed, *p])
        r = []
        for (fA, fB), y in zip(trial_feats, ys):
            wA = weight_of(fA, c)
            wB = weight_of(fB, c)
            yh, _ = balance_from_weights(wA, fA["x"], wB, fB["x"])
            r.append(yh - y)
        return np.array(r)

    sol = least_squares(resid, np.array(x0), method="lm",
                        xtol=1e-12, ftol=1e-12, gtol=1e-12,
                        max_nfev=20000)
    r = resid(sol.x)
    sse = float(r @ r)
    n, p = len(ys), len(sol.x)
    J = sol.jac
    JTJ = J.T @ J
    cov = np.linalg.inv(JTJ) * (sse / max(n - p, 1))
    se = np.sqrt(np.diag(cov))
    condJ = float(np.linalg.cond(J))
    return {"c": np.array([c1_fixed, *sol.x]), "se": se, "sse": sse,
            "resid": r, "condJ": condJ, "success": sol.success,
            "x": sol.x}


def render_and_measure(trials):
    imgs = [render_trial(b) for _, _, b in trials]
    feats = [measured_features(im) for im in imgs]
    return imgs, feats


def main():
    out = {}
    x0 = [0.25, 0.15, 0.35, 0.2, 0.1]

    # ---- clean OFAT fit ----
    trials = build_sweeps()
    imgs, feats = render_and_measure(trials)
    ys = ground_truth_y(trials, TRUE_C)
    fit = fit_model(feats, ys, x0)
    ratio_true = TRUE_C / TRUE_C[0]
    ratio_fit = fit["c"] / fit["c"][0]
    rel_err = np.abs(ratio_fit - ratio_true) / np.abs(ratio_true)
    out["clean"] = {
        "n_trials": len(trials),
        "true_c": TRUE_C.tolist(),
        "fit_c": fit["c"].tolist(),
        "fit_ratios_ck_over_c1": ratio_fit.tolist(),
        "true_ratios": ratio_true.tolist(),
        "rel_err_ratios": rel_err.tolist(),
        "se": fit["se"].tolist(),
        "sse": fit["sse"],
        "condJ": fit["condJ"],
        "max_abs_resid": float(np.abs(fit["resid"]).max()),
    }
    print("== CLEAN FIT (c1=1 anchored; ratios ck/c1) ==")
    for k, name in enumerate(FACTOR_NAMES):
        print(f"  {name:5s} true_ratio={ratio_true[k]:.3f} fit={ratio_fit[k]:.4f} "
              f"rel_err={rel_err[k]:.2%} se={fit['se'][k-1] if k>0 else 0:.4f}")
    print(f"  SSE={fit['sse']:.3e} max|resid|={np.abs(fit['resid']).max():.2e} "
          f"cond(J)={fit['condJ']:.1f}")

    # ---- break (a): area x saturation interaction in truth ----
    trials_a = trials + build_factorial()
    _, feats_a = render_and_measure(trials_a)
    ys_a = ground_truth_y(trials_a, TRUE_C, c7=0.6)
    fit_a = fit_model(feats_a, ys_a, x0)
    ratio_fit_a = fit_a["c"] / fit_a["c"][0]
    rel_err_a = np.abs(ratio_fit_a - ratio_true) / np.abs(ratio_true)
    # residuals on the factorial block vs OFAT block
    r_ofat = np.abs(fit_a["resid"][:len(trials)])
    r_fact = np.abs(fit_a["resid"][len(trials):])
    out["break_a"] = {
        "interaction": "c7*sat*area*(area/A_ref), c7=0.6, in truth only",
        "n_trials": len(trials_a),
        "fit_ratios": ratio_fit_a.tolist(),
        "rel_err_ratios": rel_err_a.tolist(),
        "sse": fit_a["sse"],
        "max_abs_resid_ofat": float(r_ofat.max()),
        "max_abs_resid_factorial": float(r_fact.max()),
        "mean_abs_resid_factorial": float(r_fact.mean()),
        "sse_clean_for_reference": fit["sse"],
        "condJ": fit_a["condJ"],
    }
    print("\n== BREAK (a): area x saturation interaction c7=0.6 in truth ==")
    for k, name in enumerate(FACTOR_NAMES):
        print(f"  {name:5s} true_ratio={ratio_true[k]:.3f} fit={ratio_fit_a[k]:.4f} "
              f"rel_err={rel_err_a[k]:.2%}")
    print(f"  SSE={fit_a['sse']:.3e} (clean SSE={fit['sse']:.3e})")
    print(f"  max|resid| OFAT block={r_ofat.max():.4f}, factorial block={r_fact.max():.4f} "
          f"(mean={r_fact.mean():.4f})")

    # ---- break (b): hue/lightness confound ----
    trials_b = build_sweeps(confound_hue_lightness=True)
    _, feats_b = render_and_measure(trials_b)
    ys_b = ground_truth_y(trials_b, TRUE_C)
    fit_b = fit_model(feats_b, ys_b, x0)
    ratio_fit_b = fit_b["c"] / fit_b["c"][0]
    rel_err_b = np.abs(ratio_fit_b - ratio_true) / np.abs(ratio_true)
    # column correlation between hue and dark features (B elements)
    FB = np.array([[f[1]["hue"], f[1]["dark"]] for f in feats_b])
    corr_hd = float(np.corrcoef(FB[:, 0], FB[:, 1])[0, 1])
    out["break_b"] = {
        "confound": "hue sweep value ramps 0.25->0.85 with hue 0->240",
        "corr_hue_dark_features": corr_hd,
        "fit_ratios": ratio_fit_b.tolist(),
        "rel_err_ratios": rel_err_b.tolist(),
        "se": fit_b["se"].tolist(),
        "se_clean": fit["se"].tolist(),
        "sse": fit_b["sse"],
        "condJ": fit_b["condJ"],
        "condJ_clean": fit["condJ"],
    }
    print("\n== BREAK (b): hue/lightness confound ==")
    print(f"  corr(hue_feat, dark_feat) = {corr_hd:.3f}")
    names = FACTOR_NAMES[1:]
    for k, name in enumerate(names):
        print(f"  {name:5s} true={ratio_true[k+1]:.3f} fit={ratio_fit_b[k+1]:.4f} "
              f"rel_err={rel_err_b[k+1]:.2%} se={fit_b['se'][k]:.4f} "
              f"(clean se={fit['se'][k]:.4f})")
    print(f"  SSE={fit_b['sse']:.3e} cond(J)={fit_b['condJ']:.1f} "
          f"(clean cond={fit['condJ']:.1f})")

    # ---- break (c): reading-direction sign flip, two observers ----
    ys_c1 = ground_truth_y(trials, TRUE_C, flip_pos_sign=False)
    ys_c2 = ground_truth_y(trials, TRUE_C, flip_pos_sign=True)
    ys_c = np.concatenate([ys_c1, ys_c2])
    feats_c = feats + feats
    fit_c = fit_model(feats_c, ys_c, x0)
    ratio_fit_c = fit_c["c"] / fit_c["c"][0]
    r1 = fit_c["resid"][:len(trials)]
    r2 = fit_c["resid"][len(trials):]
    # residual split on the position sweep (trials 20..24)
    pos_idx = [i for i, (f, _, _) in enumerate(trials) if f == "pos"]
    out["break_c"] = {
        "design": "2 synthetic observers x 30 trials; observer 2 has c5 sign-flipped",
        "fit_c5_ratio": float(ratio_fit_c[4]),
        "true_c5_ratio": float(ratio_true[4]),
        "fit_ratios": ratio_fit_c.tolist(),
        "sse": fit_c["sse"],
        "sse_clean_60trials_reference": float(2 * fit["sse"]),
        "mean_resid_obs1_pos_sweep": float(r1[pos_idx].mean()),
        "mean_resid_obs2_pos_sweep": float(r2[pos_idx].mean()),
        "max_abs_resid": float(np.abs(fit_c["resid"]).max()),
    }
    print("\n== BREAK (c): position-sign flip for half the observers ==")
    print(f"  fitted c5/c1 = {ratio_fit_c[4]:+.4f}  (true +0.400 / -0.400)")
    print(f"  SSE={fit_c['sse']:.3e}")
    print(f"  mean resid on position sweep: observer1={r1[pos_idx].mean():+.4f}, "
          f"observer2={r2[pos_idx].mean():+.4f}")
    print(f"  max|resid|={np.abs(fit_c['resid']).max():.4f}")

    # ---- model sensitivity probes (task 1 add-on) ----
    from models import (DCMModel, VMEModel, RussianModel, SaliencyModel,
                        ToolboxDCMModel, ToolboxBalanceModel)
    models = [("DCM", DCMModel()), ("VME", VMEModel()),
              ("VME-9g", VMEModel(nine_grid=True)),
              ("Rus-pos", RussianModel(mode="position_only")),
              ("Rus-ext", RussianModel(mode="extended")),
              ("Saliency", SaliencyModel()),
              ("Tbx-DCM", ToolboxDCMModel()),
              ("Tbx-Bal", ToolboxBalanceModel())]
    sens = {}
    for factor in ["sat", "hue", "dark", "area", "pos"]:
        simgs = [im for (f, _, _), im in zip(trials, imgs) if f == factor]
        row = {}
        for mname, m in models:
            sc = [m.score(im)["balance"] for im in simgs]
            row[mname] = {"min": min(sc), "max": max(sc),
                          "range": max(sc) - min(sc)}
        sens[factor] = row
    out["sensitivity"] = sens
    print("\n== MODEL SENSITIVITY (score range across each OFAT sweep) ==")
    for factor, row in sens.items():
        ranked = sorted(row.items(), key=lambda kv: kv[1]["range"],
                        reverse=True)
        print(f"  {factor:5s}: " + ", ".join(
            f"{k}={v['range']:.3f}" for k, v in ranked))

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "identifiability.json"), "w") as f:
        json.dump(out, f, indent=2)
    print("\nsaved identifiability.json")


if __name__ == "__main__":
    main()
