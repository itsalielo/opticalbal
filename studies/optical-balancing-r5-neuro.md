# Optical Balancing — Round 5 vein: NEUROAESTHETICS (EEG/fMRI on compositional balance)

**Date:** 2026-10-09
**Scope:** exact-title searches + keyword sweeps across EEG/ERP and fMRI literature on compositional/pictorial balance, visual heaviness, compositional preference, and factor-decomposed neural correlates of aesthetic value. Conference proceedings (Graz BCI 2024), preprints (Preprints.org, ResearchGate, arXiv), dissertations (KU Leuven LIRIAS, generic), and Japanese sources (KAKEN, J-STAGE) checked. Window: through 2026-10-09.
**Already-logged items NOT re-reported:** Peng et al. 2022 (saturation-contrast → heaviness, ERP N2/P3); Yoto et al. 2007 (hue–heaviness + EEG); Lin et al. 2024 (Symmetry 16(9):1191 — EEG, balance as IV); Round 3's "no fMRI with balance as IV through 2026"; Round 2's "no fMRI 2024–2026".

## HEADLINE VERDICT

**Still no fMRI study that manipulates compositional balance as an independent variable exists through late 2026.** The only study anywhere with balance-as-IV and neural data remains Lin et al. 2024 (EEG, logged). Round 3's absence finding is confirmed, not overturned.

The genuinely new development is **Iigaya et al. 2023** — the first neuroimaging study to fit per-feature *weights* for an aesthetic quantity in the brain. It is the neural analogue of the additive-decomposition program: the brain itself runs a weighted linear integration over visual features. It stops short of visual *weight*, but it proves the method is not a category error.

---

## TIER 1 — peer-reviewed (5 new + 1 background anchor)

### 1. Iigaya, K., Yi, S., Wahle, I. A., Tanwisuth, S., Cross, L., & O'Doherty, J. P. (2023). Neural mechanisms underlying the hierarchical construction of perceived aesthetic value. *Nature Communications*, *14*, 127. https://doi.org/10.1038/s41467-022-35654-y

**The most important find of this vein.** Caltech/O'Doherty lab. Participants rated ~1000 paintings over 4 days in fMRI (ratings 0–3). The model (LFS) shows aesthetic value is computed hierarchically as a *weighted integration* over low-level visual features (mean hue, mean contrast) plus high-level ones (concreteness, dynamics). Neural dissociation: feature representations in early/late visual cortex extend into parietal and lateral prefrontal cortex; the overall value is read out in medial prefrontal cortex — the same reward-valuation region that lights up for faces, music, and mathematical beauty across studies.

Why it matters for the formula: this is an existence proof that factor-decomposable, *additive* weights for an aesthetic quantity live in the brain and can be measured — the fitted weights are exactly the kind of per-factor numbers the mission seeks. Sharp limits: the fitted quantity is liking/value, not visual weight; and compositional geometry (position, area arrangement) was not among the features. Nobody has run the balance version of this experiment.

### 2. Taniyama, Y., Nihei, Y., Minami, T., & Nakauchi, S. (2025). Natural color composition induces oddball P3 asymmetry associated with processing fluency. *Scientific Reports*, *15*, 4878. https://doi.org/10.1038/s41598-025-88815-6

Toyohashi University of Technology (Nakauchi lab — same lab as the 2022 color-statistics composition work). EEG oddball paradigm: original paintings vs hue-rotated versions (90°/180°/270°) swapped as standard/deviant. P3 amplitude asymmetry — the marker of processing fluency — appeared only for the original-vs-180° pairing: the original color composition is processed more fluently than any rotation. The paper itself opens by taking balanced composition as the paramount criterion for paintings' aesthetic value, then isolates the hue-composition factor neurally.

Why it matters: an ERP correlate of a *compositional* property decomposed at the factor level (hue relationships), complementing Peng 2022's saturation→heaviness N2/P3 signatures. Fluency, not preference, is the measured mechanism — the neural route by which color composition lands as "right."

### 3. Liang, X. et al. (2026). Latent neural architecture organising shared aesthetic evaluations of visual artworks. *Nature Communications*. https://doi.org/10.1038/s41467-026-73153-6

The newest neuroaesthetics paper in the vein (September 2026). 34 volunteers viewed 96 traditional Chinese watercolor paintings in a **7T** MRI scanner. Ratings were decomposed by collaborative-filtering (the Netflix/Spotify recommender machinery) into two latent dimensions — visual content (figure↔landscape) and hedonic value (disliked↔liked). MVPA shows the brain keeps them neurally separate: content is decoded along the visual pathways, hedonic value in the deeper reward/pleasure circuits; visual-arts expertise strengthens the encoding, showing up in the default mode network.

Why it matters: compositional balance is not manipulated as an IV (natural variation only), so this is adjacent, not decisive. But it tells the formula where to plug in: balance would live in the perceptual/content stream, dissociated from reward — two systems combine into every judgment. The 7T resolution plus latent-factor decomposition is the methodological template a balance-IV fMRI study would copy.

### 4. Lin, F., Xu, W., Li, Y., & Song, W. (2024). Exploring the influence of object, subject, and context on aesthetic evaluation through computational aesthetics and neuroaesthetics. *Applied Sciences*, *14*(16), 7384. https://doi.org/10.3390/app14167384

Companion paper from the same Huaqiao/Fuzhou lab as the logged Symmetry 2024 balance study. EEG on abstract artworks whose composition, tone, and texture were quantified computationally (blank space, gray histogram, GLCM, LBP, Gabor filters); genuine-vs-fake context as moderator. Key temporal decomposition: composition classes evoked parietal positivities at 50–120 ms; tone classes evoked occipital responses at 200–300 ms; texture features drove later parieto-occipital and prefrontal components. Context (genuine vs fake) modulated prefrontal negativity across 200–1000 ms.

Why it matters: the only EEG dataset that decomposes composition vs tone vs texture into *time windows* — a temporal decomposition of the factor set. Composition is processed early and globally (parietal, 50–120 ms), which constrains any neural account of visual weight: the position/composition term acts before detailed evaluation.

### 5. Qin, Q., Chai, J., & Zhong, W. (2026). Dual-pathway processing of AI-generated Chinese ink painting: evidence from eye-tracking, EEG, and artistic expertise. *Frontiers in Psychology*. https://doi.org/10.3389/fpsyg.2026.1966943

Published 28 September 2026 — the freshest EEG aesthetics dataset. 120 participants (60 artists, 60 non-artists) viewed AI-generated vs traditional vs digital Chinese ink paintings with eye-tracking + semantic differential + EEG. AI works produced greater scan-path entropy and beta-band suppression — broader attentional exploration, higher engagement — while experts and novices agreed on expressiveness but diverged on cultural authenticity. Compositional weight and compositional complexity appear in the theoretical framing and gaze analysis.

Why it matters: peripheral but legitimately in-vein — compositional factors are in play and measured neurally, though balance is not an IV and the question is authorship, not weight. Included because it is 2026-fresh and its scan-path/compositionality data will matter if the lab track ever compares human vs computed balance judgments.

### 6. Background anchor — Bertamini, M., & Makin, A. D. J. (2014). Brain activity in response to visual symmetry. *Symmetry*, *6*, 975–996. PDF: https://www.research.unipd.it/retrieve/12cf5a3d-ddab-4f0e-9c79-9929ce2c5721/BertaminiMakin2014.pdf

The canonical review of symmetry's neural correlates — and symmetry is balance's special case, so this is the established baseline any future balance-IV study builds on. The sustained posterior negativity (SPN) is the reliable ERP marker of symmetry processing; aesthetic judgment of the same patterns dissociates neurally from symmetry classification (Jacobsen, Schubotz, Höfel & von Cramon 2006 fMRI: aesthetic judgment → frontomedian cortex, bilateral prefrontal, posterior cingulate — a *mode of judgment*, not reducible to symmetry assessment). Included as Tier 1 background so the "what would a balance study look like" comparison has its anchor; likely overlaps with earlier adjacent-lit notes, flagged accordingly.

---

## TIER 2 — leads, preprints, conference (not peer-reviewed-grade evidence)

- **Welter, M. et al. (2024).** "EEG single-trial decoding of visual art preference." *Proceedings of the 9th Graz Brain-Computer Interface Conference 2024*. https://openlib.tugraz.at/download.php?id=670cfeea46d14&location=browse — FBCSP+LDA pipeline decodes like/dislike of 120 artworks from single EEG trials at ~0.80 accuracy (chance 0.61). The authors themselves note objective properties like symmetry and complexity could serve as a-priori priors for training-data selection — the first step toward an EEG model that *uses* compositional factors rather than just correlating with them. Conference paper; watch for the journal version.
- **Unverified preprint (ResearchGate):** "Pictorial balance is a bottom-up aesthetic property mediated by eye movements. A theoretical model of a primitive visual operating system could explain balance." — the only item found with "pictorial balance" in the title AND neural-method content (EEG electrode placement described). Peer-review status unconfirmed, authors not independently verified; lead only. If real, it would be the second neural study touching balance directly — worth one verification pass if a later round needs it.

---

## Dead ends

- **Seredkina:** KILLED — not reopened.
- **Fukada:** dead end (Round 3: full text unobtainable; the retrievable follow-up yielded real practitioner numbers — black>gray>white visual "kick," blue<green<yellow<red resistance — retained only as maker-side numbers, not neural evidence).

---

## Absence statement (the finding)

- **No fMRI study with compositional/pictorial balance as an IV through 2026-10-09.** Searched: exact-title, keyword sweeps ("pictorial balance," "compositional balance," "visual balance" × EEG/fMRI/ERP/neuroaesthetics), 2024–2026 windows, conference proceedings, preprints, dissertations. The Russian literature (Round 4) is psychophysical, not neural.
- **No neuroimaging study decomposes visual weight into factor-specific neural correlates** (no color-weight vs position-weight neural dissociation for balance). The nearest things are Iigaya 2023 (weights for *value*, not weight) and Taniyama 2025 (hue-composition fluency, ERP).
- **No dissertation on EEG compositional balance** surfaced (only adjacent: Gestalt/SSVEP theses such as Alp 2017, KU Leuven).

## Net effect for the mission

1. **Iigaya 2023 is the neural proof that the additive program is not a category error.** The brain literally computes aesthetic quantities by weighted linear integration over features, with measurable per-feature weights. It validates pursuing factor-decomposed weights — and tells us where each piece lives (feature maps in visual cortex → integration in PFC). The missing experiment is now precisely nameable: run the Iigaya paradigm with balance as the target quantity and position/color/size/contrast as the fitted features.
2. **Composition gets an early neural slot.** Lin 2024b puts compositional processing at 50–120 ms parietal — the position term of any formula acts in the first perceptual pass, not in deliberation. Taniyama 2025 adds that hue-composition arrives via processing fluency (P3 asymmetry), a different mechanism than the saturation→heaviness route of Peng 2022. The factors likely dissociate neurally by mechanism, not just by weight.
3. **The 2026 state of the art (Liang 2026)** gives the experiment track its design template: high-field fMRI, latent-factor decomposition of ratings, and the content-vs-reward dissociation — which is where a future balance formula would be validated neurally.
4. For the lab track: Redies (Jena, Aesthetics Toolbox) remains the natural home for this — his group's computational-aesthetic indices plus a neural validation arm would be the first balance-as-IV neuroimaging study ever run.
