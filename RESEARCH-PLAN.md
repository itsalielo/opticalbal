# Optical Balancing — Research Plan

**Goal:** derive, validate, and publish the weight function w(saturation, hue, lightness, area, position, contrast) — the exact mathematical formula for visual weight in graphic design. Or prove precisely why it can't exist.

---

## Phase 0 — Consolidation (done / in hand)

- [x] Literature survey: ~180 Tier 1 papers, two-tier bibliography, 30 non-English items
- [x] Formula verdict: no exact general formula; closest models documented with limits
- [x] Factor analysis: what each factor contributes, where the hypothesis breaks
- [x] Case studies verified; lore refused
- [x] Academic source landscape mapped (journals, repositories, databases)
- [x] Formal starting point identified: Al Akkad & Gazimzyanov additive model

## Phase 1 — Close the literature gaps

1. **Thesis repositories** — the one unsearched territory (NDLTD, EThOS, theses.fr, DiVA). Dissertations are where failed formula attempts go to be forgotten.
2. **Retrieve Fukada (1984/1985)** — Japanese experimental color-balance studies, CiNii-verified, not digitized. Interlibrary loan via a university library.
3. **Resolve the Russian follow-ups** — Al Akkad & Gazimzyanov 2019 coefficients; Seredkina et al. compositional formula (venue unconfirmed).
4. **Replicate-or-extend scan** — check for direct replications/refutations of DCM, APB, VME (none found through 2026; keep watching).

## Phase 2 — The missing experiment (the core)

**Design sketch exists** (see studies/optical-balancing-r2-gaps.md). The experiment that has never been run:

- **Paradigm:** method of adjustment — observers adjust one factor until two compositions feel equally balanced.
- **DV:** area (adjust area to balance chroma/value/hue differences), following Morriss & Dunlap 1988.
- **Design:** fractional-factorial over six factors (saturation, hue, lightness, area, position, contrast) — the 2→6 jump.
- **Controls:** task frame (production vs evaluation — Hübner 2025), reading direction (Chokron & De Agostini 2000), ground assignment (Parada-Castellano 2016).
- **Analysis:** conjoint-style decomposition → the first fitted w(pixel group).
- **Honest risk:** Teixeira 2026 suggests factors may not separate ecologically — build the lab/field comparison into the design from the start.

**Decision point for Ali:** lab study needs participants and a lab (university collaboration), or run it as a large-N online experiment (lower control, higher power). This is the fork in the road.

## Phase 3 — Formal model

1. Start from the Russian additive model (vW = position + color + size) as the null formalization.
2. Extend with the fitted coefficients from Phase 2; test additive vs interactive combination rules (Koenderink et al. 2018: nonlinear max-rule beats linear combination in high-level tasks).
3. Benchmark against DCM/APB/VME on the same stimulus set — beat 68% variance on simple patterns *and* survive real images, or document exactly where it fails.
4. If the strong form fails: fall back to the defensible formalization (weight-as-contrast-force-against-a-ground) and publish the boundary conditions — a negative result with precise limits is still a contribution.

## Phase 4 — Publish

- **Primary target:** *She Ji: The Journal of Design, Economics, and Innovation* — diamond open access (free to read and publish), explicitly welcomes design theory/methodology/philosophy.
- **Empirical fallback:** *i-Perception* (open access, natural home for the experimental study).
- **Preprint:** publish the literature review + formula verdict early (it stands alone as a contribution).

## Open questions (for Ali)

1. Lab collaboration vs large-N online for the missing experiment?
2. Scope: chase the universal formula, or bound it to a domain first (e.g. logo/identity marks — the symbol–wordmark weight-matching task practitioners already do by eye)?
3. Timeline ambition: is this a years-long program or a focused 12-month push to the first publication?

---

*This plan is a living document. Update it as findings land.*
