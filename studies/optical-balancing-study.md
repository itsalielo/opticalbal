# Optical Balancing — Research Study

**Problematic (briefed 2026-10-09):** geometric/grid alignment does not guarantee perceived visual balance; images need human perceptual assessment. The reader's hypothesis: an EXACT mathematical formula exists — each pixel group carries weight decomposable into native factor values (saturation, hue, lightness, area, position, contrast).

**Scope of this study:** six research veins (perception science, typography, logo case studies, computational models, factor decomposition, academic landscape), all citations verified to exist. Full vein notes: `optical-balancing-perception.md`, `optical-balancing-typography.md`, `optical-balancing-logos.md`, `optical-balancing-formulas.md`, `optical-balancing-factors.md`, `optical-balancing-sources.md`.

**Sourcing discipline:** two-tier bibliography throughout. Tier 1 = peer-reviewed papers (DOI/link, verified by exact-title search). Tier 2 = informed non-academic sources (clearly marked). Unverifiable items flagged UNVERIFIED, never presented as literature.

---

## 1. The concept, defined

Optical balancing (optical correction, optical compensation) is the practice of deliberately deviating from geometric/mathematical regularity so that a composition *looks* right to human perception. The mechanism: the visual system does not measure — it weighs. A circle and a square of identical height do not look the same size; a geometrically centered element does not look centered; a perfectly symmetrical mark can read as lifeless. The designer's eye, not the ruler, is the final instrument.

The classical statement of the ambition and its limit comes from Denman Ross (1907): unequal visual attractions balance at distances inversely proportional to them — but "calculations become difficult if not impossible" once qualitative factors enter. The entire research program since is an attempt to close that gap.

---

## 2. The formula question — verdict

**No exact general formula for optical balancing exists.** What exists:

**Closest verified models:**
- **Center-of-mass / DCM family** (Hübner & Fillinger 2016, *Frontiers in Psychology* — Tier 1, open access, DOI 10.3389/fpsyg.2016.00335; canonical implementation Redies et al. 2025, *Behavior Research Methods*). Explains up to 68% of variance in balance ratings and 86% in liking ratings — but only for simple homogeneous geometric patterns. Fails on Japanese calligraphy; weakens on photographs.
- **Visual Moment Equilibrium** (Zhang & Xue 2025, *Symmetry* 18(1):41, DOI 10.3390/sym18010041): B_m = 1 − D_centroid/D_max, sharpened by B_m′ = e^(5·B_m−1), with nine-grid visual weights and a shape-sparsity term; validated at r = 0.942 (R² = 0.888) on 15 interfaces — tiny sample, fitted constants, area-only weights.
- **APB index** (Wilson & Chatterjee 2005, *Empirical Studies of the Arts*): balance score from pixel distributions across vertical, horizontal and diagonal axes plus inner/outer regions, built on Arnheim's structural skeleton. The most on-point precedent for a quantitative balance formula.

**The precise gap:** every model needs w(pixel group) — a validated weight function combining saturation, hue, lightness, area, position, and contrast. The literature has no such function. The reader's hypothesized decomposition is exactly the right program; every term is unidentified. Beyond that: reference points and anisotropies are fitted constants, not derived; models fail across picture types; and there may be a theoretical ceiling — Reber et al. (2004) ground beauty in the perceiver's processing experience, and McManus et al. (2010) show strong stable *individual* preferences with weak population ones, so a purely stimulus-side exact formula may be impossible in principle.

**Refutations on record:** Birkhoff's M=O/C (1933) failed empirically (Eysenck 1968: r=.13, n.s.); its successors inverted it. Zen & Vanderdonckt (2016) showed a plausible balance formula can correlate *zero* with human judgment until structurally fixed. McManus, Stöver & Kim (2011, *i-Perception*, PMC3485801) tried to turn Arnheim–Ross into a computable formula — the strong controlled tests failed.

---

## 3. Factor decomposition — the native-values hypothesis tested

**Strongest quantified support:**
- **Area** — the universal multiplier. No study disputes weight ∝ area.
- **Saturation as amplifier** — small/high-chroma balances large/low-chroma, independent of background and largely of hue (Morriss, Dunlap & Hammond 1982); mediated chain saturation→attention→perceived size (Hagtvedt & Brasel 2017).
- **Hue ordinal trend** — red heaviest → yellow lightest, replicated across Bullough 1907, Pinkerton & Humphrey 1974 (*Nature*), Locher et al. 2005 (red ≈7.95 vs yellow ≈7.18 on a 10-point weight scale).
- **Darkness-as-mass** — DCM/APB explain up to 68% of balance-rating variance, homogeneous black-and-white geometric patterns only (Hübner & Fillinger 2016).

**Where the hypothesis breaks hardest:**
- **Sign flips between paradigms** — lightness is dark-heavy (DCM) vs. bright-heavy (Arnheim) vs. luminance-irrelevant (Koenderink et al. 2017: "hardly important," strong idiosyncratic differences). Saturation *amplifies* weight (Morriss) but *reduces* apparent heaviness (Monroe 1925). No stable coefficient survives.
- **Flagship measures fail on real art** — APB fails completely on Japanese calligraphy; balance is computed at first fixation (≤100 ms) from "meaningful content before form" (Gershoni & Hochstein 2011).
- **Coefficients are culture-relative** — reading direction reverses horizontal weight preferences (Chokron & De Agostini 2000; Maass et al. 2009); holistic vs. analytic attention changes how much weight the *ground* carries (Masuda & Nisbett 2001).
- **No-transfer and no-computation** — color heaviness rankings don't transfer to objects (Payne 1958); observers can't reliably locate the center of perceptual mass (Friedenberg 2002/2008); **no study has ever fit native values for all factors simultaneously** — the key missing experiment.

**Net verdict:** the literature supports *contextual, relational* weights — real but parameterized by paradigm, picture type, ground assignment, culture, expertise, and task. The strong form (fixed native values + universal combination rule) is disconfirmed. Most defensible formalization found: Parada-Castellano (2016), weight-as-contrast-force-against-a-ground — keeps the math, abandons intrinsicality.

---

## 4. The science — perception

- Compositional balance is **Arnheim's invention**, not the Gestalt founders': Wertheimer, Köhler, Koffka supplied Prägnanz and the field-force metaphor but did not theorize compositional balance as such (Worker A correction).
- Arnheim's model: visual weight, the structural skeleton of the square, perceptual forces; the optical center sits slightly above the geometric center. The literature identifies ~17 visual-weight factors — but the ones resisting quantification are relational/configural/semantic (edge quality, "interest," meaning, background-dependence).
- "Balance" is two different judgments: mechanical balance vs. gravitational stability, switched by picture type (Hübner & Fillinger 2019, *i-Perception*, DOI 10.1177/2041669519856040) — formal measures predict simple stimuli (~68% variance) but collapse on real images (~10% of Instagram likes for photos).
- Koenderink, van Doorn, Pinna & Pont (2017, DOI 10.1163/22134913-00002067): compositional weight is *not* photometric — depends on background tone, edge quality, shape, position. Direct challenge to any pixel-group formula built from isolated group properties.

## 5. The craft — typography

- **Overshoot:** 1–3% of cap height for "O" (3% per Karow's *Digital Formats for Typefaces*, 5% for "A"); Hoefler: ~1% squeeze on squares. Craft conventions, never lab-optimized — **no psychophysical overshoot function exists (gap 1)**.
- **Weight:** horizontals drawn ~85–90% of verticals (craft lore); lab tolerance wide at fovea, collapse at extremes.
- **Optical center:** pure craft doctrine (E-bar above geometric midline); **no lab measurement found (gap 2)**.
- **Spacing:** default near-optimal (Chung 2002: 1.16× x-width); visual span mediates (Yu et al. 2007).
- **Optical sizing:** Bell Centennial (Carter, 1978) the textbook case; lab basis = size-dependent spatial-frequency channels (Majaj et al. 2002).
- Most useful craft source: Karen Cheng's *Designing Type* (Yale, 2006/2020) — the only practitioner book treating optical compensation systematically with measured diagrams; Carter's "I judge them purely by eye" as the philosophical keystone.
- Formula verdict from the craft side: none exists. Closest: Pelli et al. (2006) perimetric-complexity law. The designer's eye *is* the instrument.

## 6. Case studies — verified

- **Nintendo Switch logo — PARTIALLY VERIFIED.** The geometric fact verifies: the right (solid) Joy-Con is drawn slightly narrower than the left (outlined) one — documented by David Hellman (Jan 2017) with centerline overlays; an independent analysis measured the difference as roughly the outline's line width. The weight-compensation explanation is consistent with standard practice. **But no Nintendo or designer statement confirms intent — every claim of deliberate correction is analyst inference.** Cite as "analyst-attributed, unconfirmed by Nintendo."
- **Google "G" (2015)** — best-documented case. Google's own *Evolving the Google Identity* states the mark was "optically refined to prevent a visual 'overbite'" where circle meets crossbar. No numeric amount stated.
- **Google wordmark (2014)** — confirmed one-pixel nudge ("g" 1px right, "l" 1px down+right), acknowledged by a Google spokesperson on the record.
- **Starbucks Siren (Lippincott, 2011)** — designer-attributed: a few pixels of extra shadow on the right side of the nose; perfect symmetry read as uncannily inhuman. Different motive (perceptual warmth, not weight balance).
- **Twitter bird (2012)** — geometry-first counter-example (Bowman/Grasser: "a blend of mathematics and artistic intuition").
- **Refused lore:** Spotify pause button (Reddit speculation only); Apple golden-ratio construction (debunked — Janoff said "freehand"; measured ratios 1.53–1.73); Pepsi "BREATHTAKING" document (authenticity questioned).
- **Tier 1 gap:** no peer-reviewed paper documents an optical correction in a specific commercial logo.
- **Methodological finding:** practitioners almost never publish measurements — one confirmed hard number (Google's 1px nudge) plus amateur measurements and type-trade rules. That scarcity of quantification is itself a finding.

## 7. Academic source landscape — where to build the project

**Journals (open access first):** She Ji (diamond OA, Tongji — the single most useful venue for this problematic: welcomes design theory/methodology/philosophy); i-Perception (SAGE, OA — natural home for an experimental balance study); Artifact (diamond OA, practice-based design research); Visible Language (OA, visual communication); InfoDesign (OA, trilingual); International Journal of Design (OA to read); Journal of Vision (fully OA, vision mechanics); w/k (German/English OA); Sciences du Design (French, OA after 2-year wall); JSSD Bulletin via J-STAGE (Japanese, free). Subscription worth knowing: Design Studies, Design Issues, Perception, Vision Research.
**Thesis repositories:** NDLTD Global ETD Search (1M+ records — the DART-Europe successor; DART-Europe closed permanently 3 Feb 2025); EThOS (relaunched 2026 as metadata-plus-links after the 2023 British Library cyberattack); PQDT Open; theses.fr/TEL; DiVA; design-school repositories (UAL Research Online, MIT DSpace).
**Databases:** Google Scholar (citation chaining), Semantic Scholar, OpenAlex (free API), BASE (240M+ docs, OA ranked first), CORE, DOAJ (vet OA venues), Unpaywall, Internet Archive Scholar.
**Non-English infrastructure:** HAL + OpenEdition (French), J-STAGE + CiNii (Japanese), CyberLeninka (Russian OA), EZB Regensburg (German journals), OpenAIRE (EU).

## 8. Adjacent literature (separate section — core bibliography stays clean)

Mechanisms underneath optical balancing where the term never appears: Itti, Koch & Niebur (1998) saliency model (DOI 10.1109/34.730558) — the formalization of "what pops," decomposable by feature channel, direct ancestor of the factor-decomposition hypothesis; Henderson & Hayes (2017) meaning maps — the corrective (meaning guides fixations, no pixel formula absorbs semantics); Reber, Schwarz & Winkielman (2004) processing fluency — the serious alternative hypothesis (balance pleases because it processes easily); Leder et al. (2004) aesthetic appreciation model; Palmer, Schloss & Sammartino (2013) review; Palmer & Schloss (2010) ecological valence theory of color preference (PNAS, open); Wilms & Oberfeld (2018) disentangling hue/saturation/brightness; Locher, Gray & Nodine (1996) — participants *assigning weights to pictorial features*, the experimental ancestor of the decomposition hypothesis; Bauerly & Liu (2006) carrying balance metrics into real web pages.

---

## 9. Two-tier bibliography (essential entries; full bibliographies in the vein files)

### Tier 1 — peer-reviewed
- Hübner, R., & Fillinger, M. G. (2016). Comparison of objective measures for predicting perceptual balance and visual aesthetic preference. *Frontiers in Psychology, 7*, 335. https://doi.org/10.3389/fpsyg.2016.00335 — open access; the head-to-head of balance metrics.
- Hübner, R., & Fillinger, M. G. (2019). Perceptual Balance, Stability, and Aesthetic Appreciation. *i-Perception*. https://doi.org/10.1177/2041669519856040 — open; balance vs stability split.
- McManus, I. C., Stöver, K., & Kim, D. (2011). Arnheim's Gestalt theory of visual balance. *i-Perception*. PMC3485801 — open; the failed formula attempt.
- Koenderink, J., van Doorn, A., Pinna, B., & Pont, S. (2017). Compositorial "Weight" & "Luminance". https://doi.org/10.1163/22134913-00002067 — weight is not photometric.
- Wilson, A., & Chatterjee, A. (2005). The assessment of preference for balance. *Empirical Studies of the Arts, 23*, 165–180 — the APB index.
- Zhang & Xue (2025). Visual Moment Equilibrium. *Symmetry* 18(1):41. https://doi.org/10.3390/sym18010041 — most complete engineered equation.
- Locher, P., Gray, S., & Nodine, C. (1996). The structural framework of pictorial balance. *Perception, 25*(12), 1419–1436. https://doi.org/10.1068/p251419 — participants assigning weights to features.
- Itti, L., Koch, C., & Niebur, E. (1998). A model of saliency-based visual attention. *IEEE TPAMI, 20*(11), 1254–1259. https://doi.org/10.1109/34.730558
- Reber, R., Schwarz, N., & Winkielman, P. (2004). Processing fluency and aesthetic pleasure. *PSPR, 8*(4), 364–382. https://doi.org/10.1207/s15327957pspr0804_3
- Palmer, S. E., & Schloss, K. B. (2010). An ecological valence theory of human color preference. *PNAS, 107*(19), 8877–8882. https://doi.org/10.1073/pnas.0906172107 — open.
- Pinkerton, E., & Humphrey, N. K. (1974). *Nature* — hue weight ordinal replication.
- Chokron, S., & De Agostini, M. (2000) — reading direction reverses horizontal weight preferences.
- Gershoni, S., & Hochstein, S. (2011). Measuring pictorial balance perception at first glance using Japanese calligraphy. *i-Perception*. PMC3485800 — open.
- Leder, H., et al. (2004). A model of aesthetic appreciation and aesthetic judgments. *British Journal of Psychology, 95*, 489–508. https://doi.org/10.1348/0007126042369811
- Palmer, S. E., Schloss, K. B., & Sammartino, J. (2013). Visual aesthetics and human preference. *Annual Review of Psychology, 64*, 77–107. https://doi.org/10.1146/annurev-psych-120710-100504
- Pelli, D. G., et al. (2006) — perimetric complexity law; the closest thing to a formula on the craft side.

### Tier 2 — informed non-academic (clearly marked)
- Arnheim, R. (1974). *Art and Visual Perception* (new version). UC Press — the vocabulary of visual weight; foundational though a book.
- Cheng, K. (2006/2020). *Designing Type*. Yale — only practitioner book with systematic measured optical compensation.
- Noordzij, G. *The Stroke* — stroke-based letterform theory.
- Google, *Evolving the Google Identity* (2015) — the "G" optical refinement documented by the maker.
- Karow, P. *Digital Formats for Typefaces* — 3% O / 5% A overshoot figures.
- Beier, S. (2016). "Letterform research: An academic orphan" — why no formula exists on the craft side.

### UNVERIFIED — leads, not literature
- Ngo, Teo & Byrne (2003) aesthetic measures — seen only in secondary citation.
- Reinecke et al. (2013) CHI website aesthetics — seen only in secondary citation.
- Corwin's quadrant-luminance balance equation — unreviewed bioRxiv preprint; author admits limits.

---

## 10. What the project still needs (honest gaps)

1. **The weight function** w(saturation, hue, lightness, area, position, contrast) — no validated form; the experiment that fits all factors simultaneously has never been run.
2. **A psychophysical overshoot function** and a lab measurement of the optical center — craft numbers only.
3. **A Tier 1 paper on optical correction in a real commercial logo** — the academic gap is total.
4. **The Switch intent question** — geometry verified, intent unconfirmed; needs a primary source or must stay analyst-attributed.
5. **Cross-cultural coefficients** — reading-direction and attention-style effects are documented but unquantified for design use.

---

## 11. Round 2 (2026-10-09) — what was added

Four new vein files: `optical-balancing-r2-gaps.md` (missing experiment + unverified items), `optical-balancing-r2-nonenglish.md` (German/French/Japanese/Russian literature), `optical-balancing-r2-frontier.md` (2024–2026 papers, saliency, neuroaesthetics, color science), `optical-balancing-r2-practitioners.md` (Tier 2 craft sources). No duplication of Round 1.

### The missing experiment — verdict sharpened

Genuinely does not exist — but its ancestors were found. A quantitative **"spatial balance of color pairs" tradition** (Munsell → Moon & Spencer 1944 → Granger 1953 → Morriss & Dunlap 1982/87/88) fitted area × chroma, area × value, and chroma × hue jointly via the method of adjustment:
- **Moon & Spencer (1944), "Area in Color Harmony," *JOSA* 34, 93–103, DOI 10.1364/JOSA.34.000093** — the first explicit w(pixel group) formula.
- **Granger (1953), *Science* 117, 59–61, DOI 10.1126/science.117.3029.59** — first empirical test of the balance formulas.
- **Morriss & Dunlap (1988), "Joint Effects of Chroma and Value on Spatial Balance of Color Pairs," *Empirical Studies of the Arts* 6(2), 117–126, DOI 10.2190/46M2-30KP-CA57-ARQV** — the ceiling of the literature: two native factors varied jointly, area adjusted to balance. Reframes the gap from "nothing exists" to "the literature reached two factors with a validated paradigm; the gap is 2 → 6."
- **Pieters (1979), "A conjoint measurement approach to color harmony," *Perception & Psychophysics* 26, 281–286, DOI 10.3758/BF03199881** — real conjoint measurement in aesthetics since 1979, but the DV was harmony, never visual weight.
- **Koenderink et al. (2018), "Color weight photometry," *Vision Research* 151, 88–98** — nonlinear max-rule beats linear combination in high-level tasks; directly relevant to the combination-rule question.

Negative results documented: conjoint analysis exists only in marketing/packaging, never on visual weight; multivariate ML fits aesthetics, never balance itself. One killed lead: a ResearchGate record for a "Linnett, Morriss, Dunlap & Fritchie" chroma-adjustment paper is a record-merge artifact — no such publication exists. The vein file includes a design sketch for the actual missing experiment (method of adjustment, area as DV, fractional-factorial over six factors) and flags thesis repositories (NDLTD/EThOS) as the one unsearched territory.

### Unverified items — all resolved

- **Ngo, Teo & Byrne (2003) → Tier 1.** "Modelling interface aesthetics," *Information Sciences* 152, 25–46, DOI 10.1016/S0020-0255(02)00404-8 (verified via MMU repository + convergent citations).
- **Reinecke et al. (2013) → Tier 1.** CHI '13, 2049–2058, DOI 10.1145/2470654.2481281; 48% of appeal variance explained by colorfulness + complexity + demographics.
- **Corwin bioRxiv (DOI 10.1101/2020.05.26.104687) → confirmed still unreviewed** (v22, ~Dec 2024, no journal publication). Stays below Tier 1, now with verified status instead of an open question.
- **Fillinger & Hübner 2018 → Tier 1.** "Relations Between Balance, Prototypicality, and Aesthetic Appreciation for Japanese Calligraphy," *Empirical Studies of the Arts* 38(2), 172–190, DOI 10.1177/0276237418805656 (online 2018, issued 2020 — hence hard to find).

### Non-English literature — 30 verified items

- **German (11):** Wolff (1963, *Psychological Research* — brightness-equivalents as the currency of balance); Tausch (1954); Fechner (1871, founding paper of experimental aesthetics); Gottschaldt (1926); 2 dissertations (Schwabe 2019, composition perception at 50ms; Oberhummer-Rambossek 2012, Mondrian/balance); 2 grey manuscripts read in full — Piesbergen & Müller, *Visuelle Statik* I & II (1997, LMU): independently stated the reader's exact research program and measured a phenomenal-weight proportioning function. Tier 2: Bense, Metzger, Itten.
- **French (8):** Gentaz & Ballaz (2000, *L'Année psychologique* — oblique effect); Cordeau (1953 — golden section); 1 dissertation (Bigoin-Gagnan 2020, symmetry/eye-tracking); Tier 2: Moles, Ghyka, Bertin (*Sémiologie graphique* — the visual-variables factor decomposition), Groupe μ. Finding: no French experimental formula work exists — the tradition is philosophical.
- **Japanese (4):** Fukada (1984, 1985) experimental studies of color/form and color/size in pictorial balance (Doshisha bulletin, CiNii-verified; full text not digitized — retrieval flag); adjacent: Peng/Inoue/Hara 2020, Sato/Urakawa 2003.
- **Russian (7):** Al Akkad & Gazimzyanov 2017 (concept), 2017 ("Mathematical Model," *Intellektual'nye Sistemy v Proizvodstve*), 2019 (genetic-algorithm tuning); Seredkina et al. (compositional formula concept, venue unconfirmed — flagged); Tier 2: Arnheim Russian translation, Kandinsky, Vygotsky.

**Most important non-English find:** Al Akkad & Gazimzyanov (2017) — the only paper in any language with an explicit additive factor-decomposition of visual weight: vW = vWsS + vWc + vWs (position + color + size), coefficients fitted in the 2019 follow-up via genetic algorithm on 76 compositions. The reader's hypothesis in formal dress, hitting Round 1's walls (toy stimuli, no saturation/hue/lightness/contrast split).

### Frontier — 19 new Tier 1 papers (10 from 2024–2026)

- **Lu, Tang & Wu (2024, *Symmetry*)** — new improved equilibrium formula validated at r = 0.986 against expert ratings; strongest validation number in the literature, narrow domain.
- **Hübner (2025, *i-Perception*)** — balance preference flips between production and evaluation tasks; a task-frame parameter any formula would need.
- **Kandemir, Zhou, Li & Wang (2017, ACM MM workshops)** — the only paper operationalizing the decomposition hypothesis almost literally (per-feature-type centers of mass + regression weights); result: the architecture works, saliency alone fails, high-level semantic features are mandatory terms. (No DOI located; flagged as peer-reviewed workshop paper.)
- **Saliency lineage:** DeepGaze II/IIE/III, UNISAL (2020), MSDB (2025); Tu et al. (2020, AAAI) and Cheng et al. (2022, WACV) — learned pixel-wise aesthetic score maps, the closest thing to a learned w(pixel group); Zhang et al. (2021, BMVC) — SAMP-Net composition assessment.
- **Neuroaesthetics/color:** Peng et al. (2022, *Frontiers in Neuroscience*) — saturation-contrast → perceived heaviness with ERP N2/P3 signatures; Liu & Yang (2025, *Psychology & Marketing*) — product-background hue contrast → perceived size via fluency; Teixeira et al. (2026, *Symmetry*) — hue/saturation → attentional capture, with the honest admission the factors don't separate (cuts against fixed native values — and suggests the missing experiment may be un-runnable in ecological stimuli).
- Caveats: no direct replication/refutation of DCM, APB, or VME has appeared; no fMRI study of compositional balance in 2024–2026 (EEG only, via Lin et al. 2024).

### Practitioners — 17 Tier 2 sources, attribution-marked

- **TypeDrawers threads** — richest numeric vein: practitioner-measured overshoot statistics (Helvetica/Arial/Geneva/Verdana normalized to EM 100); rule-of-thumb ranges; in-thread designer values (Phinney participating).
- **Adobe InDesign docs** — Optical Kerning and Optical Margin Alignment as shipped algorithms.
- **Ahrens & Mugikura, *Size-specific Adjustments to Type Designs*** — directional formalization (small sizes: +width, +x-height, −contrast, looser spacing) + interview corpus (Slimbach, Berlow, Kobayashi, Schwartz) + the documentation-gap thesis explaining why numbers are scarce.
- **New maker-attributed logo cases:** NBC 2022 peacock redraw (on the record with NBC's SVP of Creative Design: feather spacing "balanced," logotype tuned to the mark's "visual weight" — cleanest maker-attributed case since Google's G); Airbnb Bélo refinement (Chesky walkthrough, secondhand-reported); Lufthansa 2018 crane (company-attributed); Lindon Leader's FedEx kerning account. 12 investigated-but-empty cases excluded rather than stretched.
- Recurring bounded task identified: **symbol–wordmark weight matching**, done entirely by eye — a concrete sub-problem of the weight function.

### Net effect on the verdict

Round 1's "no exact general formula" stands, sharpened. The project now has: (a) a concrete formal starting point — the Russian additive model; (b) the two-factor joint-fit paradigm (Morriss & Dunlap 1988) as methodological ancestor; (c) a design sketch for the missing experiment; (d) two new testable hypotheses — Wolff 1963 (balance = even distribution of brightness-equivalents) and Visuelle Statik load/support ratios. New cautions: Teixeira 2026 (factors don't separate ecologically); Hübner 2025 (task-frame parameter needed). Top validation number moved from VME's r = 0.942 to Lu et al.'s r = 0.986 (narrow domain, fitted terms).

### Round 2's single most important find

**Al Akkad & Gazimzyanov (2017)** — the only explicit additive factor-decomposition of visual weight in any language. It is the reader's hypothesized program in formal dress: vW = vWsS + vWc + vWs, with coefficients explicitly designated for fitting to human ratings.

---

## 12. Round 3 (2026-10-09) — Phase 1 literature gaps executed

Five new vein files: `optical-balancing-r3-theses.md` (thesis repositories), `optical-balancing-r3-fukada.md` (Fukada retrieval), `optical-balancing-r3-russian.md` (Russian coefficients + Seredkina), `optical-balancing-r3-replications.md` (replication scan + fMRI), `optical-balancing-r3-frontier.md` (2025–2026 frontier). No duplication of Rounds 1–2.

### Theses — the unsearched territory, searched

14 dissertation records. Most relevant: **Fillinger (2020, Konstanz, advisor Hübner)** — the dissertation *behind* the DCM model, explicitly testing that "each element in a picture has a certain perceptual weight that depends on its low-level features such as color, size and form"; finds the mechanical-balance metaphor holds for simple stimuli but collapses for complex pictures. Open (CC-BY) via KOPS. Runner-up: **Mokarian (2007, Saskatchewan)** — a forgotten formula attempt ("more general formula" combining geometry and color), cited once (Koenderink et al. 2017), then vanished. Repository notes: EThOS confirmed live on relaunched Hyku (metadata-only, 650k+ records); DART-Europe closed (use NDLTD/OpenAlex); NDLTD search JS-only; DiVA 403'd; theses.fr API failed; CiNii Dissertations dead-ended — Japanese theses remain unsearched.

### Fukada — holding identified, text unobtained; later paper read in full

The 1983–85 Doshisha bulletin papers (color/form and color/size in pictorial balance) are print-only: CiNii records, no PDF anywhere, zero citing literature, WorldCat zero hits. ILL path documented (NDL copy service most practical). Crown find: Fukada's own later follow-up paper (1993 experiments, Tsukamoto Gakuin funding) is **freely available and was read end to end** — a force-balance paradigm: subjects place a 3 cm colored square to achieve "good harmony," placement distance d measured; printed figure "kicks" ∝ its visual weight, color square "resists" ∝ its own. Results: black > gray > white kick strength; color resistance blue < green < yellow < red (red heaviest); larger figures kick farther; n ≥ 100 needed.

### Russian coefficients — unobtainable, and the model reframed

The 2019 paper exists and is open access (DOI 10.22213/2410-9304-2019-1-26-33), but no numeric coefficient table is retrievable — consistent with the 2017 framing where coefficients are per-source multipliers of hand-drawn/Akima-spline pF curves, possibly existing only inside the authors' Jenetics run. Exact live-access path documented for a future browser session. **Critical reframe from reading the 2017 full text end to end:** the "only additive decomposition in any language" is strictly a **position-only** formula — vWc (color) and vWs (size) were never specified, only named ("the same approach could compute color/size influence"). The additive promise was never fulfilled even for its own three terms. This is exactly where the six-factor program must begin. Seredkina et al.: venue still unconfirmed (SibFU handle 2311/160105), theoretical paper, no formula to retrieve.

### Replications — verdicts per model

- **DCM: EXTENDED** — 43 citing papers; originating lab published honest nulls (Hübner & Thömmes 2019; Hübner & Fillinger 2019); Chen & Lu (2023) independently decomposed visual weight three ways.
- **APB: REFUTED as a general index** — 107 citing papers, one genuine empirical re-test (Gershoni & Hochstein 2011, first-fixation balance of Japanese calligraphy): low correlation, boundary-condition failure, zero successful independent replications.
- **VME: UNREPLICATED** — one citing paper (background citation only).
- **Birkhoff: UNREPLICATED** (Eysenck 1941 refutation stands).
- **McManus/Stöver/Kim CoM: EXTENDED** — aesthetic-payoff claim twice weakened (Samuel & Kerzel 2013; Leyssen et al. 2012); computational extensions exist.
- **fMRI: none through 2026.** No study manipulates compositional balance as an IV. EEG/ERP only.
- **The live fault line:** balance *measures* keep working computationally while balance→*preference* effects keep coming back weak or null.

### Frontier — 15 new items, verdict extended not refuted

Biggest: **Redies et al. (2025, *Behavior Research Methods*)** — four leading European quantitative-aesthetics labs shipped one open-source Python toolbox canonicalizing APB and DCM into versioned reference code (+43 image properties). The strongest infrastructure event since Kandemir 2017. Also: Wang, Liu & Huang (2026) — seven dimensionless descriptors with perturbation audits, first paper demanding *provenance* for balance measures; Thömmes, Hübner & Hayn-Leichsenring (2025) — free gallery-wall arrangements converge on CoM midline (ecological support); Ruan & Li (2026) — saliency + symmetry + HSV in one pipeline. Missing-experiment methodology prescribed independently twice: **pairwise comparative judgments** (Law of Comparative Judgment) over ratings (FGAesQ CVPR 2026 oral; 2026 preprint).

### Net effect

Round 2's verdict stands, sharpened twice: (1) the formal starting point is narrower than believed — position-only, with color/size as unfilled promises; (2) the field's own replication record draws the fault line the formula must cross: computation works, preference doesn't follow. New assets: the Redies toolbox (reference implementations), the Fukada force-balance numbers, the pairwise-comparison prescription for the missing experiment, and 14 dissertations (Fillinger 2020 as the deepest).

### Round 3's single most important find

The 2017 Russian model is **position-only** — vWc and vWs were named but never specified. Round 2's crown is real but smaller than it looked: the additive *promise* exists, the additive *formula* does not. The six-factor program starts exactly there.
