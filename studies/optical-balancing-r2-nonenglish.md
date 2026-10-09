# Optical Balancing — Round 2: Non-English Literature

**Project:** OPTICAL BALANCING — does an exact mathematical formula for perceived visual balance exist? (Each pixel group carrying a weight decomposable into saturation, hue, lightness, area, position, contrast.)
**Round 2 brief:** cover what Round 1 (English-centric) missed — academic literature in German, French, Japanese, Russian, searched natively (queries in the target language, native terminology).
**Method:** native-language queries via OpenAlex (title/abstract search + topic filter), HAL API (French), CiNii records, CyberLeninka-indexed sources, DOI/Springer verification pages. Every item below was verified to exist by exact-title search and/or a resolving DOI/landing page. Full texts were read where openly available (German *Visuelle Statik* I+II; the three Al Akkad & Gazimzyanov papers).

**Two-tier discipline (same as Round 1):** Tier 1 = peer-reviewed papers (DOI/link verified). Doctoral dissertations are academic but examined, not journal peer-reviewed — they are listed inside Tier 1 with an explicit label, never silently. University-repository manuscripts that were never peer-reviewed are labeled as grey literature. Tier 2 = informed non-academic (books, craft classics), clearly marked, never standing in for papers. Adjacent literature (color theory, saliency, golden section, general aesthetics) is in a separate section. Summaries are in my own words; direct quotes kept far under 50 words per work.

---

## Headline verdict

The non-English literature **strengthens the Round 1 verdict while adding the single closest formula ever proposed**:

1. **The closest formula in any language is Russian.** Al Akkad & Gazimzyanov (2017) published an explicit additive decomposition of visual weight — vW = vWsS + vWc + vWs (structural-plan/position + color + size) — with a balance function over scene objects and coefficients explicitly meant to be fitted to human ratings; a 2019 follow-up fits them with a genetic algorithm. It is the reader's hypothesized program in miniature, and it hits the same walls Round 1 identified (simple geometric stimuli only; fitted constants; no saturation/hue/lightness/contrast decomposition).
2. **The reader's exact research program was independently stated in German in 1997.** Piesbergen & Müller (*Visuelle Statik I*) wrote that the effect-strength of each phenomenal-weight criterion must be determined "je einzeln und in Kombination" — singly and in combination — and ran the first experiments (Part II).
3. **A 1963 German paper proposed brightness as the single currency of balance.** Wolff (*Psychological Research*) argued balance is the even spatial distribution of brightness-equivalents across the picture plane — a quantitative, testable hypothesis about w(pixel group) with lightness as the weight carrier.
4. **No language community has fit all native factors simultaneously.** The gap Round 1 identified ("no study has ever fit native values for all factors at once") survives the non-English sweep.

---

## German (Deutsch)

### Tier 1 — peer-reviewed

**Wolff, F. (1963). Über die gemeinsame Ursache der Harmonie und des Gleichgewichts zwischen farbigen Flächen im Bild. *Psychological Research* (*Psychologische Forschung*). https://doi.org/10.1007/bf00424857**
Argues that *brightness impressions* (Helligkeitseindrücke) are the common cause of both harmony and balance between colored areas in a picture. Harmony occurs when the quantities of mutually related brightness-equivalents in the colored areas are equal; balance is observed when those brightness-equivalents are evenly distributed over the whole picture plane. He published the thesis before running the verification and proposed the experiment: observers judge whether the left/right halves of color plates are "equally heavy," then the plates are rotated 180° and 90° and judged again (rotation exposes uneven brightness distribution). Relation to the formula question: this is a quantitative hypothesis that reduces visual weight to a single measurable carrier — lightness — and defines balance as its spatial evenness. It is the strongest historical statement of the "lightness-as-weight" position, and it directly contradicts Arnheim's bright-heavy claim while agreeing with the DCM dark-heavy family only if "brightness-equivalent" is read as luminance contrast against ground. Verified via Springer page (abstract/thesis text read).

**Tausch, R. (1954). Optische Täuschungen als artifizielle Effekte der Gestaltungsprozesse von Größen- und Formenkonstanz in der natürlichen Raumwahrnehmung. *Psychologische Forschung, 24*, 299–348. https://doi.org/10.1007/BF00422032**
Theoretical paper (Univ. Marburg) arguing that geometric-optical illusions are artificial byproducts of the size- and shape-constancy mechanisms operating in natural space perception. Relation to the formula question: it supplies the *mechanism* behind optical correction — the distortions designers compensate for (overshoot, optical centering) arise from constancy processes, which is why geometric regularity fails perceptually. No formula, but the best German theoretical account of *why* the formula is needed. Verified via Springer.

**Fechner, G. T. (1871). Zur experimentalen Aesthetik. https://doi.org/10.34726/dig.17689716**
The founding paper of experimental aesthetics — the first programmatic statement that aesthetic response can be measured experimentally (the golden-section preference experiments followed in *Vorschule der Ästhetik*, 1876). Relation to the formula question: origin of the entire quantitative program; also the origin of its first failure (golden-section preference did not replicate cleanly). Historical Tier 1. Verified via OpenAlex/digitization record.

**Gottschaldt, K. (1926). Über den Einfluß der Erfahrung auf die Wahrnehmung von Figuren. *Psychologische Forschung*. https://doi.org/10.1007/bf02411523**
Gestalt-psychology classic: prior experience reshapes figure perception. Relation to the formula question: supports the theory-ladenness side — perceived weight is not a pure stimulus function, which is a standing objection to fixed native values. Adjacent-core. Verified via Springer DOI.

### Tier 1 (labeled) — doctoral dissertations (examined, not journal peer-reviewed)

**Schwabe, K. (2019). Über die Wahrnehmung von Bildkomposition in abstrakten Kunstwerken. Doctoral dissertation (Thuringia, db-thueringen.de). https://doi.org/10.22032/dbt.39426**
Experimental aesthetics: whether isolated perceptual processing of artistic composition yields stable aesthetic judgments, or whether cognitive/affective processes are prerequisites. Findings: stable judgments of composition are possible from 50 ms exposure onward and stay constant at longer exposures even when cognitive/affective processing is minimized — but only for structural terms (harmonisch, interessant, geordnet); the subjective "gefällt" was unstable. Known correlations between term pairs and dependencies on statistical image properties were already constant at very short exposures. Relation to the formula question: evidence that compositional judgments (the output side of any balance formula) are computed fast and pre-cognitively — consistent with Gershoni & Hochstein (2011) in Round 1 — but the *subjective* component resists stabilization, which is a problem for any formula predicting "pleasing balance." Verified via OpenAlex + repository abstract.

**Oberhummer-Rambossek, S. (2012). Mondrian oder die Relativität des Gleichgewichts. Doctoral dissertation, University of Vienna. https://doi.org/10.25365/thesis.26490**
Art-historical: balance as *relative* — Mondrian's neoplastic compositions as the case. Relation to the formula question: argues against absolute balance metrics from the art-theory side; adjacent. Verified via OpenAlex.

### Academic grey literature (university repository manuscripts — read in full, not peer-reviewed)

**Piesbergen, C., & Müller, K. (1997). VISUELLE STATIK – I: Phänomenologische Betrachtungen zur Wahrnehmung von Gewicht und Last. LMU München, epub.ub.uni-muenchen.de/11116.**
Phenomenology of visual weight ("anschauliche Schwere"). Core claims: (a) an object is seen as heavy only inside a structural context — the duality of *Last* (load, that which bears down) and *Belastetes*/Träger (bearer, that which is loaded); a lone object has no phenomenal weight; (b) visual criteria of heaviness: relative size/mass, spatial proportioning (stocky "gedrungen" reads heavier than slender), brightness (dark Romanesque = heavy, light Gothic = light), and saturation (saturated surface colors convey massive heaviness; unsaturated look lighter); (c) the explicit research program — the task is to determine the factors causing phenomenal weight, and "die Wirkungsstärke der verschiedenen Schwerekriterien je einzeln und in Kombination mit den anderen experimentell zu bestimmen" (the effect-strength of each weight criterion, singly and in combination, must be determined experimentally). The authors note this exceeds a single study and restrict Part I to size/mass. Relation to the formula question: this is the reader's hypothesized decomposition program, stated independently in 1997, in the Gestalt-phenomenological tradition — and the honest admission that the combined experiment had never been run. Full text read (9 pp.).

**Piesbergen, C., Müller, K., & Tunner, W. (1997). VISUELLE STATIK – II: Empirische Studien zum Problem von Last und Stütze. LMU München. https://doi.org/10.5282/ubm/epub.11118**
The experiments: (1) N=48 judgment study (balanced? yes/no) on load/support patterns; binomial tests (α=5%) classified 28 patterns (balanced/unbalanced/contested); balanced patterns clustered upper-middle of the matrix; (2) N=40 *active construction* study — participants built supports for given loads: chosen supports were *significantly wider than the load heights* in every case (ratios falling from 3.8 to 1.25 as load height grew), with 3 patterns landing near the golden section; small homogeneous sample noted as a limitation. Relation to the formula question: the only located experiment that directly measures a phenomenal-weight proportioning function (support width as a function of load) — a partial w(·) for one factor pair. Full text read (11 pp.).

### Tier 2 — informed non-academic (clearly marked)

- **Bense, M. (1998). Einführung in die informationstheoretische Ästhetik.** In Metzler eBook. https://doi.org/10.1007/978-3-476-03716-9_3 — The German information-theoretic aesthetics program (Birkhoff lineage: aesthetic measure from order/complexity). Tried to mathematize aesthetics; relevant as the historical formula attempt in the German tradition. Book chapter.
- **Metzger, W. Gesetze des Sehens** (1936; re-edited 2008) — the German Gestalt laws of seeing (Prägnanz etc.); the perceptual vocabulary Arnheim built on. Book.
- **Itten, J. Kunst der Farbe** (1961) — craft doctrine of color weight/balance (e.g., quantitative color contrasts). Practitioner book; adjacent.
- Arnheim's *Kunst und Sehen* (German translation of *Art and Visual Perception*) is the German carrier of the visual-weight vocabulary — covered via Round 1's Arnheim.

---

## French (Français)

The French literature on this exact question is thinner and more philosophical than experimental — a finding in itself. No French peer-reviewed paper proposing or fitting a balance formula was located.

### Tier 1 — peer-reviewed

**Gentaz, É., & Ballaz, C. (2000). La perception visuelle des orientations et « l'effet de l'oblique ». *L'Année psychologique*. https://doi.org/10.3406/psy.2000.28671**
Review of the oblique effect: vertical/horizontal orientations are perceived systematically more precisely than obliques; the functional basis remains debated. Relation to the formula question: orientation anisotropy is a position-independent factor any weight function must absorb (diagonals carry different perceptual status than cardinals) — adjacent, but a verified French perceptual mechanism relevant to composition. Verified via OpenAlex abstract.

**Cordeau, H. (1953). Le nombre d'or dans le dessin enfantin. *Enfance*. https://doi.org/10.3406/enfan.1953.1259**
Golden section in children's drawings. Historical/adjacent — the French developmental-psychology angle on proportion preference. Verified via DOI.

### Tier 1 (labeled) — doctoral dissertation (examined, not journal peer-reviewed)

**Bigoin-Gagnan, A. (2020). The Influence of symmetry on visual attention, evaluations and purchase intention: an application to packaging. Doctoral dissertation, Université Rennes 1. http://www.theses.fr/2020REN1G037/document**
Two eye-tracking experiments (n=150 consumers) manipulating symmetry level of food-packaging facings; measures: visual attention, perceived visual complexity, perceptual fluency, aesthetic evaluation, purchase intention. Related English journal paper: Lacoste-Badie, Bigoin Gagnan & Droulers (2019), *Journal of Retailing and Consumer Services*. Relation to the formula question: adjacent — empirical French work on symmetry perception with aesthetic-evaluation measures, but applied to packaging, not compositional balance. Verified via theses.fr/OpenAlex abstract.

### Tier 2 — informed non-academic (clearly marked)

- **Moles, A. (1958). Théorie de l'information et perception esthétique. Denoël/Gonthier.** — The French information-theoretic aesthetics: attempted a quantitative measure of aesthetic information. The French counterpart to Bense; the formula attempt in the French tradition. Book.
- **Ghyka, M. C. (1927). Esthétique des proportions dans la nature et dans les arts.** — Golden-section aesthetics across nature and art; the proportion-formula tradition in French. Book.
- **Bertin, J. (1967). Sémiologie graphique.** — Defines the retinal visual variables (position, size, value, texture/grain, color, orientation, shape) — the canonical *factor decomposition* of visual encoding, and the closest French academic precedent for the reader's native-factors hypothesis, developed for thematic maps rather than aesthetics. Book.
- **Groupe μ (1992). Traité du signe visuel. Seuil.** — Plastic semiotics (color, form, texture as signifiers). Book.
- **Guillaume, P. (1937). La psychologie de la forme. Flammarion.** — The French introduction to Gestalt psychology. Book.

---

## Japanese (日本語)

### Tier 1 — peer-reviewed (university bulletin papers; internally reviewed)

**深田尚彦 [Fukada, T.] (1984). 絵画の実験的研究-2-バランスに於ける色彩と形態 (Experimental study of painting, 2: Color and form in balance). 同志社女子大學學術研究年報 [Annual Report of Doshisha Women's College], 35(3), 308–316. CiNii NAID 110000278985.**
**深田尚彦 [Fukada, T.] (1985). 絵画の実験的研究III：バランスに於ける色彩とサイズ 2 (Experimental study of painting, III: Color and size in balance, 2). 同志社女子大學學術研究年報, 36(2), 85–91. CiNii NAID 110000278993.**
A series of experimental studies directly on pictorial balance: Part 2 manipulates color and form, Part 3 color and size, to study their roles in perceived balance of paintings. (Part 1 was not located in indexed metadata.) Fukada, a Doshisha Women's College psychologist, worked in the psychology-of-drawing tradition; these are the only located Japanese experimental papers with "balance" as the dependent variable and color/form/size as factors. Relation to the formula question: the factor-manipulation design is exactly right, but full texts were not accessible (bulletin not digitized in reachable repositories) — findings could not be verified beyond the program. Verified via OpenAlex bibliographic records + CiNii NAIDs. Note: OpenAlex misattributes the journal for some records as "Medical Entomology and Zoology"; the correct venue is the Doshisha bulletin.

### Japanese-lab work published in English (flagged for the English corpus, not claimed here)

- **Nakauchi, S., Kondo, T., Kinzuka, Y., et al. (2022). Universality and superiority in preference for chromatic composition of art paintings. *Scientific Reports, 12*, 4294. https://doi.org/10.1038/s41598-022-08365-z** — ~70% of Japanese and Portuguese observers prefer the original color composition of unseen paintings (hue-rotated fakes dispreferred); follow-up (2023, *Sci Rep*, s41598-023-29380-8) uses multiple regression to link preference to color statistics (skewness of a*, a*–b* correlation, L*–b* correlation). A quantified factor model of *color-composition preference* from a Japanese lab — adjacent to balance (preference, not balance judgments), English-language, included here only as a pointer.

### Adjacent (Japanese)

- **Peng, R., Inoue, K., & Hara, K. (2020). 目の部分の対称性とバランスに関する研究 (Research on symmetry and balance of the eye region).** Kyushu University repository, hdl.handle.net/2324/4113203 — facial eye-region symmetry/balance; adjacent (face aesthetics, not composition).
- **佐藤隆二・浦川直紀 [Sato & Urakawa] (2003). 立体物の見え方評価法に関する基礎的研究：その2 立方体のバランス評価と各部位の物理量との関係.** 照明学会全国大会講演論文集 — relates perceived balance of cubes to physical quantities of their parts; adjacent (3D/lighting context).

---

## Russian (Русский)

### Tier 1 — peer-reviewed — ★ the round's most important find

**Аль Аккад, М. А., & Газимзянов, Ф. Ф. [Al Akkad, M. A., & Gazimzyanov, F. F.] (2017). Автоматизированная система оценки композиционных характеристик 2D-изображения: концепция (Automated system for evaluating 2D-image compositional characteristics: Concept). *Вестник ИжГТУ имени М. Т. Калашникова, 20*(2), 160–162. https://doi.org/10.22213/2413-1172-2017-2-160-162**
Proposes building a computer system that evaluates the compositional characteristics of 2D images on Arnheim's methodology; reviews the one existing computer-aesthetics work (Li & Chen 2009, *IEEE JSTSP*) and its shortcomings; reports pilot experiments as evidence the methodology reflects perceptual mechanisms. Kalashnikov Izhevsk State Technical University. Full text read.

**Аль Аккад, М. А., & Газимзянов, Ф. Ф. (2017). Автоматизированная система оценки композиционных характеристик 2D-изображения: математическая модель (…: Mathematical Model). *Интеллектуальные системы в производстве, 15*(2), 105–108. https://doi.org/10.22213/2410-9304-2017-2-105-108**
The formula paper. Repeats Arnheim's structural-plan-of-the-square / dark-disk experiment in mathematical form. Definitions and equations (notation as in the paper):
- Object: O = {vW, vD, oC} (visual weight, visual direction, center-of-mass coordinates).
- Scene balance: a function f(O₁, O₂, …, Oₙ); the closer to zero, the better balanced.
- Weight contributed by one structural-plan source: **vWsSsource = 1 / (pF · kpF)** (1), where pF is perceptual force and kpF the influence coefficient of that force factor.
- **pF = f(oCD)** (2): perceptual force as a function of the distance from the object's center of mass to the structural-plan element; the curve shape is obtained by Akima-spline interpolation of hand-drawn reference graphs (chosen to avoid oscillations at extrema), with distinct curve families for edges vs. internal structural lines (internal lines show no drop near zero because the viewer cannot apply the "standing on a surface" experience to invisible lines).
- **Total visual weight: vW = vWsS + vWc + vWs**, where vWsS = Σ vWsSsourceN (sum over structural-plan sources), vWc = color component, vWs = size component. "Точно так же можно вычислить влияние цвета или размера объекта на его визуальный вес" — the same approach extends to other characteristics.
- The coefficients (kpF and per-factor weights) are explicitly *not derivable from Arnheim*: they must be fitted to human data — planned via questionnaires (1–5 ratings of compositions) and least squares.
Relation to the formula question: this is the only located paper in any language that writes down an additive factor-decomposition of visual weight with fittable coefficients — the reader's hypothesis in formal dress. Its limits are exactly Round 1's: only position (structural plan), color, and size appear — no saturation/hue/lightness split, no contrast term; stimuli are simple geometric compositions in a square. Full text read (4 pp.).

**Аль Аккад, М. А., & Газимзянов, Ф. Ф. (2019). Автоматизированная система оценки композиционных характеристик 2D-изображения: настройка математической модели (…: Configuring the Mathematical Model). *Интеллектуальные системы в производстве, 17*(1), 26–33. https://doi.org/10.22213/2410-9304-2019-1-26-33**
Fits the 2017 model with a specially built genetic algorithm on survey data: respondents rated 76 simple geometric compositions; analysis (Google Sheets + Jenetics) showed means are uninformative (very large SDs, bimodal 2-vs-5 splits) while *modes* capture the tendencies; visualized pF maps agree with Arnheim (right side and bottom more "stable"; lower-right corner most stable; pF tolerance zone for the visual center shifted to lower-right). Rater subgroups emerged (teenage girl artists tended negative; middle-aged men without art training tended moderate). Conclusion: the model correctly implements Arnheim, and averaging across observers destroys the structure — taste groups would need separate tuning. Relation to the formula question: the only located *empirical fit* of a balance formula's coefficients — and it reproduces Round 1's McManus finding (stable individual preferences, weak population ones) as a fitting problem. Full text read (8 pp.).

**Середкина, Н. Н., Ермаков, Т. К., & Гомонов, И. С. [Seredkina, Ermakov & Gomonov] (2026). The Compositional Formula as a Concept of the Theory of Visual Thinking (R. Arnheim and V. I. Zhukovsky). SibFU Digital Repository. https://elib.sfu-kras.ru/handle/2311/160105**
Conceptual paper analyzing the notion of "compositional formula" across Arnheim's and V. I. Zhukovsky's theories of visual thinking — linking Arnheim's perceptual concepts and force lines with Zhukovsky's "visible essence," on the shared premise that the image is structured by internal compositional laws. Relation to the formula question: theoretical discussion of *whether* a compositional formula is thinkable, not a formula; no experiment. Note: journal venue could not be confirmed from accessible metadata (repository page unreachable at time of check); cite via the repository handle. Verified via OpenAlex record + abstract.

### Tier 2 — informed non-academic (clearly marked)

- **Арнхейм, Р. Искусство и визуальное восприятие** (Russian translation, Blagoveshchensk, 2000, 392 pp.) — the edition the Al Akkad papers formalize; the Russian carrier of the visual-weight vocabulary. Book.
- **Кандинский, В. Точка и линия на плоскости** (1926; Russian editions) — assigns "weight" and "tension" to point/line/plane configurations; the Russian-formalist precursor of visual-force thinking. Book.
- **Выготский, Л. С. Психология искусства** (1925/1965) — Russian classic psychology of art. Book; historical.

---

## Adjacent literature (separate section — not core bibliography)

Mechanisms and neighboring traditions where "visual balance formula" never appears as such:
- **Nakauchi lab (Japan, English-language):** chromatic-composition preference ~70% for originals across cultures (2022, *Sci Rep* 12:4294); multiple-regression model of preference from color statistics — skewness a*, a*–b* correlation, L*–b* correlation (2023, *Sci Rep*). Quantified factor model of color-composition *preference*; English-language, flagged for the English corpus.
- **Tausch (1954)** (listed Tier 1 above, German): constancy mechanisms as the source of optical illusions — the mechanism behind optical correction.
- **Gentaz & Ballaz (2000)** (listed Tier 1 above, French): the oblique effect — orientation anisotropy.
- **Golden-section traditions:** Ghyka (French, 1927), Fechner (German, 1871/1876), Cordeau (French, 1953), Russian applied papers (e.g., golden section in interface design — practice, not perception).
- **Sato & Urakawa (2003)** (Japanese): perceived balance of 3D cubes vs. physical quantities of parts.
- **Peng, Inoue & Hara (2020)** (Japanese): symmetry/balance of the eye region in faces.
- **Bigoin-Gagnan (2020)** (French): symmetry → attention/fluency/aesthetic evaluation in packaging.

---

## Consolidated two-tier bibliography

### Tier 1 — peer-reviewed papers (verified)
1. Al Akkad, M. A., & Gazimzyanov, F. F. (2017). Automated system for evaluating 2D-image compositional characteristics: Concept. *Vestnik IzhGTU, 20*(2), 160–162. https://doi.org/10.22213/2413-1172-2017-2-160-162 — Russian.
2. Al Akkad, M. A., & Gazimzyanov, F. F. (2017). …: Mathematical Model. *Intellektual'nye Sistemy v Proizvodstve, 15*(2), 105–108. https://doi.org/10.22213/2410-9304-2017-2-105-108 — Russian. ★ the formula.
3. Al Akkad, M. A., & Gazimzyanov, F. F. (2019). …: Configuring the Mathematical Model. *Intellektual'nye Sistemy v Proizvodstve, 17*(1), 26–33. https://doi.org/10.22213/2410-9304-2019-1-26-33 — Russian. ★ the fit.
4. Wolff, F. (1963). Über die gemeinsame Ursache der Harmonie und des Gleichgewichts zwischen farbigen Flächen im Bild. *Psychological Research*. https://doi.org/10.1007/bf00424857 — German. ★ brightness as weight currency.
5. Tausch, R. (1954). Optische Täuschungen als artifizielle Effekte der Gestaltungsprozesse von Größen- und Formenkonstanz. *Psychol. Forsch., 24*, 299–348. https://doi.org/10.1007/BF00422032 — German.
6. Fechner, G. T. (1871). Zur experimentalen Aesthetik. https://doi.org/10.34726/dig.17689716 — German (historical).
7. Gottschaldt, K. (1926). Über den Einfluß der Erfahrung auf die Wahrnehmung von Figuren. *Psychologische Forschung*. https://doi.org/10.1007/bf02411523 — German (historical).
8. Gentaz, É., & Ballaz, C. (2000). La perception visuelle des orientations et « l'effet de l'oblique ». *L'Année psychologique*. https://doi.org/10.3406/psy.2000.28671 — French.
9. Cordeau, H. (1953). Le nombre d'or dans le dessin enfantin. *Enfance*. https://doi.org/10.3406/enfan.1953.1259 — French (historical).
10. Fukada, T. [深田尚彦] (1984). 絵画の実験的研究-2-バランスに於ける色彩と形態. *同志社女子大學學術研究年報, 35*(3), 308–316. CiNii NAID 110000278985 — Japanese.
11. Fukada, T. [深田尚彦] (1985). 絵画の実験的研究III：バランスに於ける色彩とサイズ 2. *同志社女子大學學術研究年報, 36*(2), 85–91. CiNii NAID 110000278993 — Japanese.
12. Seredkina, N. N., Ermakov, T. K., & Gomonov, I. S. (2026). The Compositional Formula as a Concept of the Theory of Visual Thinking (R. Arnheim and V. I. Zhukovsky). SibFU Digital Repository. https://elib.sfu-kras.ru/handle/2311/160105 — Russian (journal venue unconfirmed; cite via repository).

### Tier 1 (labeled) — doctoral dissertations
13. Schwabe, K. (2019). Über die Wahrnehmung von Bildkomposition in abstrakten Kunstwerken. Doctoral dissertation (Thuringia). https://doi.org/10.22032/dbt.39426 — German.
14. Bigoin-Gagnan, A. (2020). The Influence of symmetry on visual attention, evaluations and purchase intention: an application to packaging. Doctoral dissertation, Univ. Rennes 1. http://www.theses.fr/2020REN1G037/document — French.
15. Oberhummer-Rambossek, S. (2012). Mondrian oder die Relativität des Gleichgewichts. Doctoral dissertation, Univ. Vienna. https://doi.org/10.25365/thesis.26490 — German.

### Academic grey (read in full; not peer-reviewed — never cited as papers)
16. Piesbergen, C., & Müller, K. (1997). VISUELLE STATIK – I: Phänomenologische Betrachtungen zur Wahrnehmung von Gewicht und Last. LMU. https://epub.ub.uni-muenchen.de/11116/ — German.
17. Piesbergen, C., Müller, K., & Tunner, W. (1997). VISUELLE STATIK – II: Empirische Studien zum Problem von Last und Stütze. LMU. https://doi.org/10.5282/ubm/epub.11118 — German.

### Tier 2 — informed non-academic
- Bense, M. (1998). Einführung in die informationstheoretische Ästhetik. Metzler. (German)
- Metzger, W. Gesetze des Sehens. (German)
- Itten, J. Kunst der Farbe. (German)
- Moles, A. (1958). Théorie de l'information et perception esthétique. Denoël/Gonthier. (French)
- Ghyka, M. C. (1927). Esthétique des proportions dans la nature et dans les arts. (French)
- Bertin, J. (1967). Sémiologie graphique. (French)
- Groupe μ (1992). Traité du signe visuel. Seuil. (French)
- Guillaume, P. (1937). La psychologie de la forme. Flammarion. (French)
- Арнхейм, Р. (2000). Искусство и визуальное восприятие. Blagoveshchensk. (Russian)
- Кандинский, В. (1926). Точка и линия на плоскости. (Russian)
- Выготский, Л. С. (1925/1965). Психология искусства. (Russian)

---

## What this changes for the project

1. **The formula exists in draft form — in Russian.** Al Akkad & Gazimzyanov (2017/2019) is the empirical program the reader hypothesized: additive weight decomposition + fitted coefficients + balance function. Any continuation of the project should start by replicating or extending their model (their coefficients were never published as universal values; the tuning was demonstrative).
2. **The German phenomenologists named the missing experiment.** Piesbergen & Müller (1997) stated the single-and-combined factor program and measured one factor pair (load/support proportioning). Their Part II data (support/height ratios 3.8→1.25) is a usable prior.
3. **Wolff (1963) gives the project its sharpest testable hypothesis:** balance = even spatial distribution of brightness-equivalents. This is directly testable against the DCM family and the saturation findings.
4. **French output confirms a structural hole:** no French experimental formula work located — the tradition is philosophical (Moles, Bertin, Groupe μ). Bertin's visual variables remain the best French factor-decomposition precedent.
5. **Japanese experimental work exists but is thinly digitized:** Fukada's 1984/85 balance series needs a CiNii/NDL full-text retrieval pass before its findings can be used.
6. **Honest limits:** Al Akkad's journals are regional Russian peer-reviewed venues, not top-tier; stimuli are toy compositions; no saturation/hue/lightness/contrast decomposition anywhere; the Seredkina venue is unconfirmed.
