# Optical balancing — computational track notes

**Status:** model-vs-model experiments, 2026-10-09.
**Honesty header:** Everything below is SYNTHETIC. No human judgments were
collected; no human data appears anywhere. These are candidate models scored
on rendered geometric stimuli — a consistency and identifiability probe of
the *formalisms*, not evidence about human perception. Nothing here replaces
the missing human experiment (RESEARCH-PLAN.md Phase 2).

**Evaluation framing (field fault line):** all models below are scored on
BALANCE prediction only. No claim is extended to preference/liking
prediction — that is a separate, harder claim the literature shows keeps
failing (balance ≠ liking; Hübner 2025 shows the task frame flips balance
preference). Keep the two claims apart.

Code: `~/workspace/opticalbal-compute/` — `models.py`, `corpus.py`,
`headtohead.py`, `identifiability.py`, `reference/huebner.py` (vendored
Aesthetics Toolbox), outputs `headtohead.json`, `identifiability.json`.
Corpus: 17 images, 400×400, white ground, `corpus/` + `metadata.json`.

---

## 1. What was implemented (one line per model)

- **DCM** (hand-rolled, Hübner & Fillinger 2016): per-pixel mass
  m = 1 − gray/255, mass-weighted centroid, DCM in [0,100], balance =
  1 − DCM/100. *Validated against the canonical toolbox DCM: max|diff| =
  0.0058, mean 0.0036 over the corpus; corr = 1.000. Our DCM is confirmed
  against the reference, not the reverse.*
- **ToolboxDCM** (canonical reference, Redies et al. 2025, DOI
  10.3758/s13428-025-02632-3, vendored verbatim from
  `reference/huebner.py`): balance = 1 − rdist/141.42. Reference quirks
  kept intentionally: minority-side inversion at the 128 threshold,
  1-based fulcrum indexing, per-axis rounding → centered disk scores
  0.995, not 1.0.
- **ToolboxBalance** (canonical APB-family QIP, same source): mean of 8
  axis/inner-outer difference measures, balance = 1 − bs/100. The
  inner-outer terms penalize concentrated central mass → centered disk
  scores **0.496** (canonical behavior, not a bug). Different construct
  from the others; compressed range on this corpus (0.43–0.76).
- **VME** (Zhang & Xue 2025): area-weighted aggregate centroid of
  segmented elements, Manhattan distance to center. Area-only weights.
- **VME-ninegrid**: VME with quadrant attention weights UL 0.33 / UR 0.28
  / LL 0.23 / LR 0.16 (per task spec, attributed to Zhou et al. via the
  VME paper — **unverified against the primary source**).
- **Russian position-only** (DEFAULT; Al Akkad & Gazimzyanov 2017,
  faithful subset): element weight = normalized distance of centroid
  from image center. Concept-faithful; exact functional form UNVERIFIED
  (no accessible full text).
- **Russian extended** (OUR EXTENSION, explicitly NOT the paper): adds
  size term A_S·(area/img_area) and color term A_C·sat·(1−val); all
  coefficients PLACEHOLDER (1.0).
- **Saliency** (Itti-Koch-lite, à la Abeln et al. 2016): center-surround
  pyramids over intensity, R−G, B−Y, orientation; DCM on the saliency
  map. Parameters are implementer choices.

**Russian-model correction (Round 3, verified — do not soften):** the
2017 paper's model is POSITION-ONLY. vWc (color) and vWs (size) were
never specified — named only as future work. The full additive formula
vW = vWsS + vWc + vWs never existed; only the promise of it. The
color/size terms in `mode="extended"` are ~pure invention. The model as
implemented is ~90% reconstruction, ~10% paper. Even the position term's
exact coefficient form is unobtainable.

---

## 2. Head-to-head on the 17-image corpus (balance scores)

| image | manip | DCM | VME | VME-9g | Rus-pos | Rus-ext | Saliency | Tbx-DCM | Tbx-Bal |
|---|---|---|---|---|---|---|---|---|---|
| disk_centered | baseline | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.995 | 0.496 |
| disk_left | position | 0.646 | 0.750 | 0.750 | 0.646 | 0.646 | 0.646 | 0.650 | 0.431 |
| disk_right | position | 0.646 | 0.750 | 0.750 | 0.646 | 0.646 | 0.646 | 0.643 | 0.435 |
| disk_top | position | 0.646 | 0.750 | 0.750 | 0.646 | 0.646 | 0.646 | 0.650 | 0.431 |
| disk_bottom | position | 0.646 | 0.750 | 0.750 | 0.646 | 0.646 | 0.646 | 0.643 | 0.435 |
| two_inverse_ratio | area×lightness | 0.975 | 0.866 | 0.842 | 1.000 | 0.962 | 0.873 | 0.971 | 0.687 |
| dark_vs_light | lightness | 0.777 | 1.000 | 0.960 | 1.000 | 1.000 | 0.777 | 0.781 | 0.482 |
| big_vs_small | area | 0.810 | 0.866 | 0.842 | 1.000 | 0.962 | 0.894 | 0.813 | 0.558 |
| red_vs_blue | hue | 0.988 | 1.000 | 0.960 | 1.000 | 1.000 | 0.986 | 0.985 | 0.733 |
| sat_high_vs_low | saturation | 0.941 | 1.000 | 0.960 | 1.000 | 0.992 | 0.875 | 0.943 | 0.677 |
| quadrants_heavy_UL | pos×light | 0.692 | 0.823 | 0.742 | 0.867 | 0.874 | 0.766 | 0.697 | 0.485 |
| three_triangle | position | 0.859 | 0.900 | 0.917 | 0.798 | 0.804 | 0.859 | 0.855 | 0.757 |
| bar_left_heavy | lightness | 0.886 | 1.000 | 1.000 | 1.000 | 1.000 | 0.875 | 0.890 | 0.495 |
| mark_symmetric | baseline | 1.000 | 1.000 | 0.976 | 1.000 | 1.000 | 1.000 | 0.995 | 0.605 |
| mark_switch_structure | structure | 0.930 | 0.951 | 0.973 | 1.000 | 0.982 | 0.951 | 0.926 | 0.518 |
| mark_switch_narrow_right | struct+area | 0.963 | 0.974 | 0.996 | 0.975 | 0.991 | 0.939 | 0.961 | 0.545 |
| mark_g_style | structure | 0.966 | 0.976 | 0.976 | 0.966 | 0.966 | 0.990 | 0.968 | 0.445 |

Corpus means: DCM 0.845, VME 0.903, VME-9g 0.891, Rus-pos 0.894,
Rus-ext 0.889, Saliency 0.845, Tbx-DCM 0.845, Tbx-Bal 0.542.
Pairwise correlations: DCM–Tbx-DCM 1.000, DCM–Saliency 0.954,
Rus-pos–Rus-ext 0.996, VME–VME-9g 0.967; Tbx-Bal agrees with nothing
above 0.594 (different construct).

### Confirmed artifacts (all reproduced on this run)
- **VME = 1.000 on `dark_vs_light` and `bar_left_heavy`**: area-only
  weights are blind to lightness — the documented VME limit, confirmed.
- **Rus-pos = 1.000 on every equidistant pair** (`big_vs_light`… i.e.
  `big_vs_small`, `dark_vs_light`, `bar_left_heavy`, `red_vs_blue`,
  `sat_high_vs_low`, `two_inverse_ratio`, `mark_switch_structure`):
  both elements get identical weights (0.3182 each on `big_vs_small`) →
  centroid at center. The honest degeneracy of the position-only model:
  it cannot see size, lightness, or color at all.
- **Rus-pos on `disk_centered`**: total visual weight = 0.000000 (centered
  element has zero weight) → 1.0 by convention, flagged in the detail
  dict. A centered composition is *unscorable* under the position-only
  model — that degeneracy is a finding, not a bug.
- **Rus-ext = 1.000 on `dark_vs_light`, `bar_left_heavy`** (achromatic →
  color term sat·(1−val) = 0) and on **`red_vs_blue`** (color term has no
  hue encoding: sat·(1−val) is identical for red and blue). Both are
  reconstruction artifacts of OUR extension — not paper claims.
  On `big_vs_small` Rus-ext = 0.962 vs DCM 0.810: the placeholder
  position term swamps the size term.
- **VME-9g breaks mirror symmetry**: `mark_symmetric` → 0.976 vs 1.000
  for plain VME (left bar falls in UL/LL: 0.33/0.23; right bar in
  UR/LR: 0.28/0.16). Bonus fragility: on `dark_vs_light` VME-9g = 0.960
  because the two disks' centroids straddle the exact center line and
  get assigned different quadrants by a pixel-boundary flake.
- **Tbx-Bal ≠ the others' scale**: `disk_centered` → 0.496; never trust
  a "1.0 = centered" reading of the Balance QIP.

### Sensitivity ranking (score range across single-factor sweeps)
| factor | most → least sensitive |
|---|---|
| position | Tbx-Bal 0.461 · **Rus-pos 0.247** · Rus-ext 0.239 · Tbx-DCM 0.127 · DCM 0.124 · Saliency 0.124 · VME-9g 0.103 · VME 0.088 |
| area | Tbx-Bal 0.203 · DCM 0.132 · Tbx-DCM 0.122 · VME-9g 0.119 · VME 0.093 · Saliency 0.071 · Rus-ext 0.013 · Rus-pos 0.000 |
| lightness | Tbx-Bal 0.290 · Saliency 0.216 · DCM 0.216 · Tbx-DCM 0.215 · VME/VME-9g/Rus-pos/Rus-ext 0.000 |
| saturation | Saliency 0.170 · Rus-ext 0.125 · Tbx-Bal 0.097 · DCM 0.074 · Tbx-DCM 0.073 · VME/VME-9g/Rus-pos 0.000 |
| hue | Tbx-Bal 0.081 · Saliency 0.079 · DCM 0.062 (luminance only) · Tbx-DCM 0.060 · VME/VME-9g/Rus-pos/Rus-ext 0.000 |

No model sees hue as hue — the best responders (Saliency, DCM) see it
only through luminance. Nobody is hue-sensitive in the perceptual sense.

### Per-model verdicts
- **Winner, all-round: DCM (hand).** Validated against the canonical
  reference within 0.0058; responds to all five factors; no catastrophic
  blindness. The reference implementation is the ground truth for the
  formalism — our copy is faithful.
- **ToolboxBalance:** canonical but a different construct (APB family);
  do not compare its absolute scores with the 1.0-centered models.
- **Saliency:** runner-up; most saturation-sensitive; tracks DCM at
  0.954. Itti-Koch-lite approximations documented in code.
- **VME:** clean on position/area, *structurally* blind to
  lightness/saturation/hue. Fails exactly where the literature says it
  does.
- **VME-ninegrid:** adds unverified quadrant weights that break mirror
  symmetry and introduce boundary flakes. Net negative on this corpus.
- **Rus-pos:** the faithful paper subset — and the subset is degenerate:
  blind to everything except eccentricity asymmetry, unscorable on
  centered compositions. This is what the paper actually gives us.
- **Rus-ext:** demonstrates what the paper's *program* would look like
  completed, but every number it produces beyond position is ours, with
  placeholder coefficients and a hue-blind color term. Useful as a
  scaffold, citable as nothing.

---

## 3. Six-factor identifiability experiment

**Protocol.** Two-element compositions, 400×400. Element A fixed:
mid-gray disk, r=40, at (120,200). Element B varies ONE factor at a
time, 5 levels each (30 trials): saturation (red, 0→1), hue
(0°→240°, sat 0.8), lightness (achromatic v 0.15→0.95), area (r 24→56),
horizontal position (x 205→355), contrast-against-ground (luminance-based,
varies even at fixed HSV value). Synthetic ground truth
(implementer choice, documented in `identifiability.py`):
`w = c1·area + c2·sat·area + c3·hue_w·area + c4·(1−val)·area +
c5·area·pos + c6·contrast·area`, `hue_w = 0.5·(1+cos(2πh/360))`
(peaks at red), `pos = |x−200|/200`,
`contrast = |gray_elem − gray_bg|/255`; rating
`y = 1 − |weighted_centroid_x − 200|/200`. TRUE
c = [1.0, 0.5, 0.3, 0.7, 0.4, 0.2]. The fitter sees rendered pixels
only: segments A/B, measures the six features from pixels, fits
c2..c6 by nonlinear least squares (`scipy.optimize.least_squares`).
**c1 = 1.0 is fixed as the scale anchor: balance ratings are
homogeneous of degree 0 in c, so absolute scale is unidentifiable —
only the ratios c_k/c_1 are estimable.** Design-matrix condition
reported as cond(J) of the least-squares Jacobian at the optimum.

**Clean fit (30 trials).** Ratios recovered: sat 0.4998 (err 0.04%),
hue 0.3020 (0.66%), dark 0.6950 (0.71%), pos 0.4008 (0.19%), con
0.2076 (3.79%). SSE = 7.68e-06, max|resid| = 2.08e-03, cond(J) = 16.5.
SEs: sat 0.0119, hue 0.0086, dark 0.0302, pos 0.0113, con 0.0258.
An additive six-factor model *is* identifiable from this design — when
the world cooperates.

**Break (a): area×saturation interaction in the truth**
(`+ c7·sat·area·(area/A_ref)`, c7 = 0.6), plus a 3×3 area×sat
factorial block (39 trials), additive model fit. ĉ_sat/c1 = **1.0759
vs true 0.500 — 115% error**; other ratios nearly untouched (hue
4.8%, dark 0.7%, pos 1.1%, con 6.8%). SSE = 1.57e-03 (**205× the
clean SSE**); factorial-block max|resid| = 0.0218 vs OFAT 0.0021.
Note the OFAT-only portion fits *fine* — the interaction is invisible
without the factorial block. OFAT designs cannot detect interactions;
the misspecification is absorbed silently into the nearest additive
coefficient.

**Break (b): hue/lightness confound** (hue sweep value ramps
0.25→0.85 with hue). Feature correlation corr(hue, dark) = 0.644 —
and the fit **survived**: rel errors ≤ 2.8%, SEs comparable to clean
(hue SE 0.0081 vs 0.0086), cond(J) = 8.7 vs clean 16.5. Honest
reading: at 0.64 correlation the design's redundancy (each factor
also varied alone in its own sweep) rescues identifiability.
Non-identifiability is a matter of degree — it bites at
near-perfect collinearity, not at realistic 0.6-level confounds.
The danger case is a corpus where hue and lightness *never* vary
independently (then no design matrix, however clever, separates them).

**Break (c): reading-direction sign flip** (two synthetic observers;
observer 2 has c5 → −c5; single c5 fit to all 60 ratings).
Fitted ĉ5/c1 = **−0.0485** (truth ±0.400) — the single sign
collapses toward zero, representing neither observer. SSE =
2.19e-03; position-sweep mean residuals split +0.0113 / −0.0110 by
observer; max|resid| = 0.026. A single fitted sign does not average
two populations — it erases the effect and leaves a signed residual
pattern that looks like noise unless you split by observer.

**Precise mathematical statement of what breaks and why.**
(1) *Scale:* balance ratings identify visual weights only up to a
global positive scale (the centroid is a ratio); absolute coefficients
are unestimable without an independent anchor — c1 ≡ 1 is a choice,
not a measurement. (2) *Interactions:* an unmodeled multiplicative
term is absorbed into the nearest additive coefficient (+115% on
ĉ_sat) and is undetectable without factorial variation — OFAT
stimulus sets are blind to it by construction. (3) *Confounding:*
correlated factors are separable only insofar as the design contains
independent variation; at corr → 1 the Jacobian loses rank and the
coefficients become non-identified (standard errors → ∞). Real-world
stimuli (hue/lightness) live dangerously close to this. (4) *Sign
instability:* a position coefficient with observer-dependent sign
(left-to-right vs right-to-left reading) cannot be represented by one
parameter; the fit returns ≈ 0 and the true ±0.4 effect vanishes into
structured residuals.

---

## 4. Sanity-check note (DCM on trivial cases)

Centered disk → DCM(hand) 1.000, Tbx-DCM 0.995 (reference quirks:
minority-side inversion, 1-based fulcrum, per-axis rounding — hence
≠ 1.0 exactly). Offset disk (100 px) → 0.646 / 0.650. Corner-ward
mass drives the score toward 0 monotonically. Qualitative behavior
only — this is a formalism check, **not** a replication of any
published validity figure (e.g. the published DCM–rating
correspondences). No human data was used at any point.

## 5. What remains missing for the exact formula

The sharpest statement: **balance ratings identify visual weights
only up to a global scale and only through their ratios inside a
centroid — so without human-anchored weights the "exact" formula is
underdetermined by construction; and our breaks show an additive fit
silently absorbs an area×saturation interaction (+115% into ĉ_sat),
survives only moderate hue/lightness confounds by design redundancy,
and collapses a sign-flipped position weight to −0.05 instead of
failing loudly.** The missing piece is not a better equation — it is
the human experiment (factorial, both reading directions, anchored
scale) that would let any equation be identified at all.
