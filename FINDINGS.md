# Optical Balancing — Draft Findings

**Research project:** toward an exact mathematical formula for visual weight in graphic design.
**Status:** draft v0.1 — two research rounds complete (2026-10-09). ~180 verified Tier 1 papers, 17 Tier 2 practitioner sources, 30 non-English items.
**Full evidence:** `studies/` (master study + 10 vein files).

---

## 1. The problematic

Geometric/grid alignment does not guarantee perceived visual balance. The visual system does not measure — it weighs. Optical balancing is the deliberate deviation from geometric regularity so a composition *looks* right. The open question: **can the designer's eye be replaced — or at least formalized — by an exact mathematical formula?**

## 2. The formula verdict

**No exact general formula exists.** The literature's best attempts:

| Model | Result | Limit |
|---|---|---|
| Center-of-mass / DCM (Hübner & Fillinger 2016) | ~68% of balance-rating variance | Simple homogeneous patterns only; fails on calligraphy, weakens on photos |
| Visual Moment Equilibrium (Zhang & Xue 2025) | r = 0.942 | n = 15, fitted constants, area-only weights |
| Lu, Tang & Wu (2024) equilibrium formula | r = 0.986 vs expert ratings | Narrow domain, fitted terms |
| APB index (Wilson & Chatterjee 2005) | Pixel-distribution balance score | Fails completely on real art |
| Birkhoff's M=O/C (1933) | — | Failed empirically (Eysenck 1968: r = .13, n.s.) |

**The precise gap:** every model needs **w(pixel group)** — a validated weight function combining saturation, hue, lightness, area, position, and contrast. No such function exists. The decomposition hypothesis (each factor carries a native, quantifiable value) is exactly the right program — and every term is unidentified.

## 3. What the evidence says about each factor

- **Area** — the universal multiplier. Undisputed: weight ∝ area.
- **Saturation** — amplifies weight (small/high-chroma balances large/low-chroma; Morriss, Dunlap & Hammond 1982), but *reduces* apparent heaviness in other paradigms (Monroe 1925). No stable coefficient.
- **Hue** — ordinal trend red (heaviest) → yellow (lightest), replicated across a century (Bullough 1907 → Locher et al. 2005: red ≈7.95 vs yellow ≈7.18).
- **Lightness** — sign-flips between paradigms: dark-heavy (DCM) vs bright-heavy (Arnheim) vs luminance-irrelevant (Koenderink et al. 2017).
- **Position** — weight shifts with distance from center/edges; reading direction reverses horizontal preferences (Chokron & De Agostini 2000).
- **The killer fact:** no study has ever fit all factors simultaneously. The two-factor ceiling (Morriss & Dunlap 1988, area × chroma / area × value) is the methodological ancestor. The gap is **2 → 6**.

## 4. The formal starting point exists

**Al Akkad & Gazimzyanov (2017)** — the only explicit additive factor-decomposition of visual weight in any language:

> vW = vWsS + vWc + vWs (position + color + size)

Coefficients fitted in the 2019 follow-up via genetic algorithm on 76 compositions. It hits the known walls (toy stimuli, no saturation/hue/lightness/contrast split) — but it is the program in formal dress, and the place to start building.

Two more testable hypotheses on record: **Wolff (1963)** — balance = even distribution of brightness-equivalents; **Piesbergen & Müller, *Visuelle Statik* (1997)** — independently stated this exact research program and measured a phenomenal-weight proportioning function.

## 5. The honest cautions

- ~~Teixeira et al. (2026)~~ — RETRACTED 2026-10-09 (Round 5): could not be retrieved after repeated exact-title/DOI searches; the claim is unverified and no longer cited. The separability question now rests on verified work: Alexander & Shansky (1976) jointly fit hue×value×chroma on perceived heaviness (heaviness rises with chroma, falls with value, hue ~nil — never replicated), Ou et al. (2004) found separability is construct-dependent, and Devinck & Knoblauch (2025) ran a three-way conjoint where chroma dropped out.
- **Hübner (2025):** balance preference flips between production and evaluation tasks — any formula needs a task-frame parameter.
- **Reber et al. (2004) / McManus et al. (2010):** beauty may live in the perceiver's processing experience with strong *individual* preferences — a purely stimulus-side exact formula may be impossible in principle.
- **Koenderink et al. (2017):** compositional weight is not photometric — background tone, edge quality, shape, position dominate.
- Most defensible formalization found: **Parada-Castellano (2016)** — weight-as-contrast-force-against-a-ground. Keeps the math, abandons intrinsicality.

## 6. Case-study verdicts

- **Nintendo Switch logo — partially verified.** Geometry checks out (right Joy-Con drawn narrower, compensating the outline's weight) but Nintendo never confirmed intent. Cite as analyst-attributed.
- **Google "G" (2015)** — best-documented case, maker-confirmed ("optically refined to prevent a visual 'overbite'").
- **NBC peacock (2022)** — cleanest maker-attributed case since Google's G (feather spacing "balanced" to the mark's "visual weight").
- **Refused lore:** Apple golden ratio (debunked), Spotify pause (Reddit only), Pepsi document (authenticity questioned).
- **Tier 1 gap:** zero peer-reviewed papers on optical correction in a commercial logo. Practitioners almost never publish measurements.

## 7. Where the project stands

The question moved from "does a formula exist?" (no) to "what is the exact shape of the missing piece?" — the weight function w(saturation, hue, lightness, area, position, contrast), with the 2→6 experimental gap, a formal starting point (Russian additive model), a methodological ancestor (joint-fit paradigm), and an experiment design sketch. The next move is empirical, not literary.
