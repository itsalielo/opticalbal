# Optical Balancing — Round 4: New-Model Citation Check

**Date:** 2026-10-09
**Worker:** Round 4 (citation/replication watch)
**Scope:** Zhang & Xue VME (Symmetry 2025/26), Lu/Tang/Wu 2024 E_II (Symmetry 16), new 2025–2026 balance formulas, replication updates for DCM/APB/VME. Every paper verified by exact-title/DOI lookup (OpenAlex + web). Tier 1 = peer-reviewed; Tier 2 separated.

---

## 1. Zhang & Xue, "Visual Moment Equilibrium" — citation verdict

**Paper:** Visual Moment Equilibrium: A Computational Cognitive Model for Assessing Visual Balance in Interface Layout Aesthetics. *Symmetry* 18(1):41, DOI 10.3390/sym18010041. Published online **2025-12-24** (journal issue dated 2026 — so "Zhang & Xue (2025)" and "Symmetry 2026" are the same paper).

**Citation count (OpenAlex, 2026-10-09): 1.** The single citing work:

- Yuan, H., Wang, Y., & Zhong, J. (2026). Research on Optimal Design of Visual Elements of CNC Press Display Interface Based on Visual Cognition. *Applied System Innovation* 9(6), 121. DOI 10.3390/asi9060121. — An applied industrial-HMI study (CNC press interfaces): field studies, KANO-model prioritization, eye-tracking comparison of layout groups, usability validation. Relevance to VME: background-level — VME is cited as part of the visual-cognition/interface-aesthetics literature framing, not as a tested model. No replication, extension, or refutation. *(Caveat: the MDPI article page refused a text fetch (403), so the depth of the VME citation inside Yuan et al. could not be confirmed from the full text; classification as background rests on the abstract and study design.)*

**Verdict: nothing substantive.** No replication, no independent validation, no challenge, no applied extension of VME's equations exists in the indexed literature ~10 months after publication. This is normal for a paper this young, but it means VME's r = 0.942 (regular interfaces, n = 15) remains a single-study number.

---

## 2. Lu, Tang & Wu (2024), improved equilibrium formula E_II — citation verdict

**Paper:** Product Form Design and Evaluation Method Based on Improved Form Aesthetic Formula. *Symmetry* 16(7), 883, DOI 10.3390/sym16070883. Published 2024-07-11. (This is the E_II paper with the r = 0.986 vs. expert rankings on five bladeless-fan alternatives.)

**Citation count (OpenAlex, 2026-10-09): 6.** None validates, replicates, or challenges E_II. In brief:

| Citing paper | Journal, date | Relationship to E_II |
|---|---|---|
| Wu, F., Lu, P., & Hsiao, S.-W. (2025). Generative Large Model-Driven Methodology for Color Matching and Shape Design in IP Products. *Entropy* 27(3), 319. DOI 10.3390/e27030319 | Tier 1 | **Same research group.** An AIGC/multimodal (GPT-4o + Midjourney) design methodology. No equilibrium formula is used or validated ("equilibrium" absent from abstract). Background/self-citation. |
| Liu, S. (2025). Hybrid Ant Colony Optimization and Convolutional Neural Network for Product Morphology Design Optimization. Proc. IC3IT 2025. DOI 10.1109/ic3it66137.2025.11340814 | Tier 1 (conference proceedings) | Product-morphology optimization; citation depth not verified — from venue/topic it is a background-level reference, not an E_II test. |
| Li, L., & Liu, X. (2026). Exploring Aesthetic Evaluation Through Color Matching in Mechanical Product Design. *Color Research & Application*. DOI 10.1002/col.70053 | Tier 1 | Uses an Aesthetic Measurement Model (AMM) + Markov decision on 125 color palettes — a *color*, not form, method. Cites the form-aesthetic lineage only for background. |
| Xia, P. (2026). Automated Aesthetic Evaluation of Digital Product Designs Using Patch-Based Convolutional Neural Networks. *Data & Metadata*. DOI 10.56294/dm2026790 | Tier 1 | Learned CNN aesthetic model (PCNN with Barber optimization) — deep-learning lineage, not the closed-form formula lineage. Background citation. |
| Wang, X., Liu, W., & Huang, L.-C. (2026). Traceable Symmetry-Aware Image Processing for Two-Dimensional Morphological Diagnostics in Product Concept Design: A Four-Alternative Smart-Speaker Study. *Symmetry* 18(8), 1402. DOI 10.3390/sym18081402 | Tier 1 | **Closest thing to a continuation.** Directly cites Lu et al. 2024 in the computational-aesthetics literature. Same engineered-formula product-form lineage (four smart-speaker alternatives, like Lu's five bladeless fans). Proposes a new traceable pipeline (SAGE-D framing) with seven dimensionless measures (silhouette reflection, centroid, light-band regularity gradient, component-scale retention, contour compactness) plus resolution-resampling, one-pixel-morphology, and parameter-perturbation sensitivity analysis. Does **not** independently validate E_II's r = 0.986 and reports no human-rating correlation for its new measures — but it is the first paper to extend the same design-science program. See §3. |
| Chen, Z. et al. (2026). Combining NMF and DFNN for Data-Driven Kansei Design of New Energy Vehicle Rear-End Styling. *Mathematics*. DOI 10.3390/math14173171 | Tier 1 | Data-driven Kansei (NMF + deep feedforward nets); background citation. |

**Verdict: r = 0.986 stands unchallenged and unreplicated.** No paper reproduces E_II on new stimuli, tests it against lay (non-expert) raters, or contests the number. The Wang et al. (2026) paper continues the lineage with new measures but no fresh human validation.

---

## 3. New balance-formula papers, 2025–2026

### Tier 1 (peer-reviewed)

1. **Yang, Y., Zhuo, Y., Liu, J., Meng, W., & Wu, Z. (2025).** A Hybrid Quantitative Method for Evaluating HMI Layout Design in Service Robots. *Symmetry* 17(12), 2102. DOI 10.3390/sym17122102. Published 2025-12-07. **Genuinely new to this mission (not covered in Rounds 1–3).**
   - New explicit balance formula for interface layouts: BM = 1 − (|BMv| + |BMh|), where BMv = (wL − wR)/max(|wL|,|wR|) (and BMh analogously), with wj = Σ aij·dij — visual weight = element area × distance from the frame boundary. This is a visual-moment-style formulation (weight × distance) but, like every prior formula, weight is not decomposed into native factors (saturation/hue/lightness) — area does the work.
   - Also proposes a Visual Perceptual Intensity (VPI) model based on retinal cone-cell distribution (fovea-to-periphery weighting) and fuses expert (AHP) and objective (entropy) weights inside an axiomatic-design decision framework.
   - Applied to five medical-service-robot HMI designs (N = 15 participants); eye-tracking correlations with fixation metrics (unity r = 0.682, color harmony r = 0.788) were moderate-to-large but non-significant at that sample size. Same tiny-N engineered-formula caveats as Lu et al. Mission-relevant: another data point that new formulas keep getting *more* domain-bound (service-robot HMI), not more general.
   - Cited by: Zuo et al.'s related interface-aesthetics work ("Aesthetic evaluation method for interactive interface layouts on the basis of visual cognitive multi-attribute fusion") — applied continuation within the same school.

2. **Wang, X., Liu, W., & Huang, L.-C. (2026).** Traceable Symmetry-Aware Image Processing for Two-Dimensional Morphological Diagnostics in Product Concept Design. *Symmetry* 18(8), 1402. DOI 10.3390/sym18081402. Published 2026-08-20.
   - New formula-family: seven dimensionless measures over separate body/light-band/aperture masks of product concept images, with explicit sensitivity testing (resolution resampling, one-pixel morphology, synthetic controls). This is the first paper in the lineage to take *metric fragility* seriously — directly relevant to the mission's identifiability concerns. Limitation: no human-judgment validation numbers reported in the abstract; it is a diagnostics paper, not a perception paper.

### Tier 2 (not peer-reviewed)

3. Anonymous practitioner essay (Medium, handle @francismvom, ~Sep 2026). "A Mathematical Model for the Automated Evaluation of Graphical User Interfaces." Proposes visualWeight = normalizedArea × contrast × saturation × salience and a center-of-mass balance score normalized by screen diagonal. Not literature, but worth one line: it is the only 2026 text found that explicitly decomposes visual weight into native perceptual factors (area, contrast, saturation, salience) — the exact decomposition the mission hypothesizes — even though it offers no data. https://medium.com/@francismvom/a-mathematical-model-for-the-automated-evaluation-of-graphical-user-interfaces-a607649734e6

---

## 4. Replication updates: DCM, APB, VME

- **DCM (Fillinger/Hübner deviation of center of mass):** No new replication or refutation since Round 3. Braun, Hofmann & Doerschner (2026, *i-Perception*, "Being K. Malevich" — already logged in Round 3) computes both APB and DCM on Suprematist originals and participant-made arrangements, and finds the geometrical indices do not correlate strongly with liking (individual differences dominate). No independent group has re-run DCM's core experiments; no refutation of the measure exists. Status: **unchanged — extended by originating lab, never independently replicated, never refuted.**
- **APB (Wilson & Chatterjee):** No new replication or challenge since Round 3. Status: **unchanged.**
- **VME (Zhang & Xue):** Published Dec 2025; one background citation; no replication yet. Status: **too young to have a replication record.**

---

## Net verdict

**Nothing new on the replication front, but two genuinely new formula-lineage entries:** (1) Yang et al. (2025, *Symmetry*) — a new explicit BM balance formula (area × distance weighting) for service-robot HMI, the first new closed-form balance equation since Lu et al.; (2) Wang et al. (2026, *Symmetry*) — a new traceable seven-measure family in the product-form lineage that cites Lu et al. 2024 but offers no fresh human validation. The two frontier numbers both stand single-sourced: E_II r = 0.986 (Lu et al., 6 citations, none substantive) and VME r = 0.942 (1 citation, background only). The pattern Round 2 identified continues: the engineered-formula lineage is alive but each new formula is *more* domain-bound, and nobody is replicating anybody.

### Full citation list

- Zhang, X., & Xue, C. (2026). Visual Moment Equilibrium: A Computational Cognitive Model for Assessing Visual Balance in Interface Layout Aesthetics. *Symmetry* 18(1), 41. https://doi.org/10.3390/sym18010041
- Lu, T., Tang, Y., & Wu, F. (2024). Product Form Design and Evaluation Method Based on Improved Form Aesthetic Formula. *Symmetry* 16(7), 883. https://doi.org/10.3390/sym16070883
- Yuan, H., Wang, Y., & Zhong, J. (2026). Research on Optimal Design of Visual Elements of CNC Press Display Interface Based on Visual Cognition. *Applied System Innovation* 9(6), 121. https://doi.org/10.3390/asi9060121
- Wu, F., Lu, P., & Hsiao, S.-W. (2025). Generative Large Model-Driven Methodology for Color Matching and Shape Design in IP Products. *Entropy* 27(3), 319. https://doi.org/10.3390/e27030319
- Liu, S. (2025). Hybrid Ant Colony Optimization and Convolutional Neural Network for Product Morphology Design Optimization. Proc. IC3IT 2025. https://doi.org/10.1109/ic3it66137.2025.11340814
- Li, L., & Liu, X. (2026). Exploring Aesthetic Evaluation Through Color Matching in Mechanical Product Design. *Color Research & Application*. https://doi.org/10.1002/col.70053
- Xia, P. (2026). Automated Aesthetic Evaluation of Digital Product Designs Using Patch-Based Convolutional Neural Networks. *Data & Metadata*. https://doi.org/10.56294/dm2026790
- Wang, X., Liu, W., & Huang, L.-C. (2026). Traceable Symmetry-Aware Image Processing for Two-Dimensional Morphological Diagnostics in Product Concept Design: A Four-Alternative Smart-Speaker Study. *Symmetry* 18(8), 1402. https://doi.org/10.3390/sym18081402
- Chen, Z. et al. (2026). Combining NMF and DFNN for Data-Driven Kansei Design of New Energy Vehicle Rear-End Styling. *Mathematics*. https://doi.org/10.3390/math14173171
- Yang, Y., Zhuo, Y., Liu, J., Meng, W., & Wu, Z. (2025). A Hybrid Quantitative Method for Evaluating HMI Layout Design in Service Robots. *Symmetry* 17(12), 2102. https://doi.org/10.3390/sym17122102
- Braun, D. I., Hofmann, M., & Doerschner, K. (2026). Being K. Malevich: A hands-on approach to compositional preference. *i-Perception*. https://doi.org/10.1177/20416695261421103
