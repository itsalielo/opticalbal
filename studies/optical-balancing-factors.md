# OPTICAL BALANCING — Factor Decomposition (Worker E)

**Angle:** decompose pixel-group visual weight into calculable factors; test the "native values" hypothesis (each visual factor carries an intrinsic, quantifiable contribution to visual weight; perceived balance should be computable from these).
**Date:** 2026-10-09 · **Worker:** E (factor decomposition) · **Status:** literature survey, all citations verified by exact-title search.

## 0. How this was sourced

- **Tier 1** = peer-reviewed journal papers, peer-reviewed conference proceedings, and peer-reviewed book chapters. Each was verified by searching its exact title; the bibliography gives DOI and/or a direct link plus an access-status note.
- **Tier 2** = preprints (not peer-reviewed), books, practitioner writing, curated reference files, and secondary summaries. Clearly marked; never used as a substitute for Tier 1.
- **UNVERIFIED** = a claim or citation I could not confirm in this pass. Flagged, never presented as established literature.
- Summaries are in my own words throughout; no extended quotation.

## 1. The hypothesis under test

The reader's sharpened hypothesis has three testable components:

1. **Native values:** each visual factor (saturation, hue, lightness, area, position, contrast, …) carries an intrinsic, quantifiable weight contribution — a coefficient or rank that holds across contexts.
2. **Composition rule:** perceived balance = some function (additive, weighted, multiplicative…) of these native values × their spatial arrangement.
3. **Computability:** given the pixel groups, balance is in principle calculable.

The literature contains both the strongest support for this idea and its most direct refutations. Both are reported below.

## 2. The theoretical starting point: Arnheim's factor inventory

Rudolf Arnheim's *Art and Visual Perception* (1974, rev. ed.; Tier 2, book) is the origin of almost every factor list in the field. His inventory of what generates visual weight:

- **Location (the lever):** weight increases with distance from the center — explicitly opposed to physics, where attraction falls with distance squared.
- **Depth:** the further an area of the visual field reaches in depth, the greater its weight.
- **Size:** larger = heavier, other things equal.
- **Color:** red is "heavier" than blue; **bright** colors are "heavier" than dark ones (he attributes the latter partly to irradiation — bright surfaces look relatively larger).
- **Intrinsic interest:** formal complexity, intricacy, or peculiarity adds weight.
- **Isolation:** an isolated element (the moon in an empty sky) gains weight.
- **Shape:** simpler/more regular shapes (circles, squares) are heavier; compactness (mass concentrated around its center) adds weight.
- **Orientation:** vertically oriented forms seem heavier than oblique ones.
- **Anisotropy:** objects are heavier at the **top** of the image and on the **right** of the image (as tested by McManus et al., 2011, Tier 1).
- **Knowledge:** the viewer's knowledge of the depicted subject has little or no influence on weight.

Note what Arnheim did **not** provide: a single number for any factor, or a combination rule. Every quantified coefficient in the sections below comes from later experimental work — and, as §5 shows, later work frequently contradicts both Arnheim and itself.

## 3. Factor-by-factor quantification

### 3.1 Area / size

**Quantification status: STRONGEST of all factors — but always relational, never absolute.**

- Size is the one factor with no serious challenger: every model treats weight as proportional to area (pixel count). In the DCM/APB family (Wilson & Chatterjee, 2005; Hübner & Fillinger, 2016 — Tier 1), total weight is the sum over pixels, so area enters multiplicatively with per-pixel weight.
- **Munsell's law of inverse ratios of areas** (Munsell, 1905, Tier 2 book): a large area of dull, unsaturated color is balanced by a small area of highly saturated color. The law is relational (area₁ × strength₁ = area₂ × strength₂), i.e., area has no native value — its contribution is defined against the strength of what fills it.
- **Locher, Overbeeke & Stappers (2005, Tier 1)** tested this directly with Mondrian compositions: they permuted red/yellow/blue across three areas and had participants rate each area's apparent weight and locate the composition's balance center. Finding: the perceived weight of a color — especially red and yellow — varied as a function of the area it occupied (an **interaction**, not an additive constant), and balance centers shifted accordingly. Only design-trained participants detected the subtler shifts — expertise moderates the factor (see §5).
- **Ngo, Teo & Byrne (2003, Tier 1)** operationalize element weight from bounding-box area in their balance/equilibrium formulas for screen aesthetics (Information Sciences, 152, 25–46).

**Native-value verdict for area:** area behaves like *mass* in the mechanical analogy — the most stable factor — but always as a multiplier on other factors' strengths. No standalone "weight per unit area" exists independent of what fills the area.

### 3.2 Lightness / value

**Quantification status: MOST MEASURED — and the most internally contradictory.**

Two competing native-value assignments dominate:

**(a) Dark = heavy.** Wilson & Chatterjee's APB (2005, Tier 1) assumes each pixel's perceptual weight is *inversely* related to its gray level — dark pixels heavier than bright ones. Hübner & Fillinger (2016, Tier 1) formalized this as the DCM: black pixel = mass 1, white pixel = mass 0, center of perceptual mass computed like a physical center of gravity. Results on simple black-and-white geometric patterns: DCM scores explained **up to 68% of variance in balance ratings and up to 86% in liking ratings** (averaged across pictures). This is the closest the literature comes to a working native value for lightness.

**(b) Bright = heavy.** Arnheim (1974, Tier 2) claims bright colors are heavier than dark ones (irradiation argument). The brightness–weight illusion literature (Walker, Francis & Walker, 2010, Tier 1) complicates it further: *seen* dark objects are judged heavier, but *lifted* dark objects feel *lighter* than bright ones — a ~6% felt-weight reversal (a 129 g white ball felt ~8 g heavier than an identical black ball when hefted). Expectation and perception run in opposite directions.

**(c) Luminance hardly matters.** Koenderink, van Doorn & Gegenfurtner (2017, Tier 1) tested whether luminance predicts "compositorial weight" — their term for the operational, design-relevant sense of weight. Their conclusion: luminance per se is **hardly important** except in deliberately constrained paradigms; observers *can* judge weight by luminance when forced to, but with **strong idiosyncratic differences**. They frame compositorial weight as closer to *salience* than to any photometric quantity, influenced by "raw photometric/colorimetric parameters, various kinds of psychophysical contrast, image geometry, even semantic properties."

**(d) Vertical lightness gradients carry weight.** Xu, Zhang, Zhu & Xia (2023, Tier 1): for six product forms, a monochrome gradient with a **darker bottom and lighter top** increased perceived weight and stability versus the reverse; weight perception mediated the stability effect; the effect was stronger for women than men.

**Native-value verdict for lightness:** the sign of the coefficient flips between research programs (dark-heavy in DCM/APB vs. bright-heavy in Arnheim), and Koenderink's program suggests lightness has no stable native value at all outside stripped-down paradigms. Lightness is the best-measured factor and the clearest case that "native value" is paradigm-relative.

### 3.3 Hue

**Quantification status: WEAK — ordinal hints, no stable coefficients; hopelessly confounded with lightness and saturation.**

- **Bullough (1907, Tier 1)** — "On the apparent heaviness of colours," *British Journal of Psychology*, 2, 111–152 — is the founding experiment: trained observers ranked colors by apparent heaviness and the rankings tracked luminosity, with introspective reports invoking landscape associations and preference.
- **Monroe (1925, Tier 1)** — "The apparent weight of color and correlated phenomena," *American Journal of Psychology*, 36(2), 192–206 — extended the work; secondary summaries report that increasing saturation made colors appear to weigh *less* (see §3.4 for the contradiction this creates).
- **Pinkerton & Humphrey (1974, Tier 1)** — "The apparent heaviness of colours," *Nature*, 250(5462), 164–165, DOI 10.1038/250164a0 — using a fulcrum-balancing method, found a stable ranking: **red heaviest, then blue, green, orange, yellow lightest**; darker colors heavier; no independent brightness effect (ranking detail as reported in secondary summaries — Tier 2).
- **Locher, Overbeeke & Stappers (2005, Tier 1)** provide the closest thing to native hue weights: in the Mondrian triads, red areas were rated heaviest, with red and yellow showing the strongest area-dependence (reported means on a 10-point scale: red ≈ 7.95, yellow ≈ 7.18, blue ≈ 7.76 for the largest area — figures reported in secondary write-ups of the study, Tier 2, treat as approximate).
- **Itten (1961, Tier 2 book)** proposed literal native values: harmonic area proportions **yellow : orange : red : violet : blue : green = 3 : 4 : 6 : 9 : 8 : 6**, derived from Goethe's "intensity" numbers (strong colors need less area). This is the purest historical statement of the native-values hypothesis — and it was never experimentally validated.
- **Disconfirmation — Payne (1958, Tier 1):** "Apparent weight as a function of color," *Am. J. Psychol.*, 71(4), 725–730 — the heaviness rankings of *colors* do not transfer to *objects*: red objects do not look heavier than otherwise identical yellow objects. Whatever hue-weight exists is about color patches, not about things.

**Native-value verdict for hue:** red-heavy / yellow-light is the most replicated ordinal pattern, but (i) it is confounded with lightness in every study, (ii) it does not generalize from patches to objects, and (iii) no interval-scale coefficient survives across paradigms. Itten's ratios remain unvalidated design lore.

### 3.4 Saturation / chroma

**Quantification status: MODERATE evidence for a real effect — with the SIGN disputed.**

- **Morriss, Dunlap & Hammond (1982, Tier 1)** — "Influence of chroma on spatial balance of complementary hues," *Am. J. Psychol.*, 95, 323–332: the relative chroma of color pairs predictably affects the relative areas judged as balanced — **small areas of high chroma balance large areas of low chroma**. The chroma effect was independent of background and relatively independent of the hues involved, and Munsell's inverse-ratio rule fit the data better than Moon & Spencer's (1944) contrast-with-background model. Follow-ups: Morriss & Dunlap (1987, Tier 1) on value; Morriss & Dunlap (1988, Tier 1) on joint chroma×value effects.
- **Hagtvedt & Brasel (2017, Tier 1)** — "Color Saturation Increases Perceived Product Size," *J. Consumer Research*, 44(2), 396–413, DOI 10.1093/jcr/ucx039: six experiments show higher saturation → larger perceived size, mediated by **attention capture**, itself driven by arousal. This gives saturation a causal *chain* into visual weight (saturation → attention → apparent size → weight) rather than a direct coefficient.
- **Against:** Monroe (1925, Tier 1), as summarized in secondary sources, found increasing saturation made colors appear to weigh *less* — the opposite sign. The contradiction is unresolved in the literature and is a direct strike against a stable native saturation value.

**Native-value verdict for saturation:** the balance-relevant evidence (Munsell → Morriss → Locher) treats saturation as a weight *amplifier* (weight ≈ area × f(saturation)), but the sign of the direct heaviness effect flips between paradigms. No numeric coefficient is published.

### 3.5 Position — distance from center/edges, the lever, top/bottom, left/right

**Quantification status: MODERATE for the vertical axis; the horizontal axis is CULTURALLY CONTINGENT.**

- **The lever itself:** Arnheim's claim (weight ∝ distance from center) is formalized in DCM/APB as the moment arm: each pixel's contribution is its weight × its coordinates. McManus, Stöver & Kim (2011, Tier 1) tested the full Arnheim–Ross axis theory across five studies and found that **the detailed predictions did not hold**: participants did not re-frame compositions to rebalance disks of different sizes/greys, and paired comparisons showed no preference for center-of-mass-on-axis images (one study even found a significant preference for *off*-axis images). Weak statistical residue: acclaimed art photographs sit nearer the axes than random ones, but this may be symmetry preference, not mass mechanics.
- **Vertical anisotropy:** Arnheim's "top is heavier" gets a number from an unlikely source — Corwin's bioRxiv preprint (Tier 2, **not peer-reviewed**): perfectly balanced pictures have bilateral quadrant luminance symmetry with the lower half lighter by a factor of **~1.07 ± ~0.03**, and his balance formula weights the upper quadrants' Y-coordinates by 1.07. Treat as an intriguing unreviewed estimate, not an established constant. Pierce (1894, Tier 1) found vertical arrangements are judged more as *stability* than *balance* — a task-dependence caveat (see §5).
- **Positional weighting schemes:** Ngo et al. (2003, Tier 1) assign explicit quadrant weights in their "sequence" measure — upper-left : upper-right : lower-left : lower-right = **4 : 3 : 2 : 1** (as summarized in secondary reviews, Tier 2) — i.e., a published, if unvalidated-outside-HCI, set of positional native values.
- **Center preference:** Rodway, Schepman & Lambert (2012, Tier 1) — "Preferring the one in the middle," *Applied Cognitive Psychology*, 26, 215–222, DOI 10.1002/acp.1812 — replicate the **centre-stage effect**: items in the middle of an array are preferred horizontally *and* vertically. Position carries preference weight independent of content.
- **Horizontal sign flips with culture:** Chokron & De Agostini (2000, Tier 1), *Cognitive Brain Research*, 10, 45–49, DOI 10.1016/S0926-6410(00)00021-5 — French (left-to-right) readers prefer rightward directionality; Israeli (right-to-left) readers prefer leftward. Maass, Suitner, Favaretto & Cignacchi (2009, Tier 1), *J. Exp. Soc. Psychol.*, 45, 496–504, DOI 10.1016/j.jesp.2009.01.004 — the **spatial agency bias**: Italians place agentic groups to the left, Arabic speakers to the right. Any "native" left/right weight coefficient is therefore culture-relative.

**Native-value verdict for position:** distance-from-center as a moment arm is the one structural assumption every model shares, but the axis-alignment theory built on it fails detailed tests; the vertical coefficient (~1.07) is unreviewed; the horizontal coefficient changes sign with reading direction. Position is structural, not intrinsic.

### 3.6 Contrast against ground

**Quantification status: MODERATE — mostly via the attention proxy.**

- **Parada-Castellano (2016, Tier 1)** — "Study of balance of images using visual weight," *Color Research & Application*, 41(2), 175–187, DOI 10.1002/col.21943 — the most explicit "native value" formula in the recent literature: visual weight is **the visual force due to contrast of light** among elements. He distinguishes *partial weight* (a figure's contrast against its local ground) from *integral weight* (each element's contrast against the image's average lightness), and defines balance as the resultant force landing on the geometric center. Weight here is irreducibly relational: no ground, no value.
- **Saliency bridge:** Itti, Koch & Niebur (1998, Tier 1), *IEEE Trans. Pattern Anal. Mach. Intell.*, 20(11), 1254–1259, DOI 10.1109/34.730558 — the standard computational saliency model builds "conspicuity" from **center–surround contrast** in color, intensity, and orientation channels. Abeln et al. (2015, Tier 1), *Front. Hum. Neurosci.*, 9, 704, DOI 10.3389/fnhum.2015.00704 — showed the DCM computed on *saliency* (not raw luminance) predicts which details people crop from photographs: contrast-based weight behaves like mass.
- **Figure–ground framing effects:** Corwin's preprint (Tier 2) reports that a white-bordered image on a black ground is seen as *one visual object* (image + frame), while a black-bordered image on white is not — the ground assignment changes what counts as the figure whose weight is computed.
- **Fluency:** Reber, Schwarz & Winkielman (2004, Tier 1), *Pers. Soc. Psychol. Rev.*, 8, 364–382, DOI 10.1207/S15327957PSPR0804_3 — trace aesthetic effects of figure–ground contrast to **processing fluency**: high contrast is liked because it is processed easily, not because contrast has an intrinsic weight.

**Native-value verdict for contrast:** the best-formalized modern "native value" (Parada-Castellano) is explicitly *relational* — weight is a contrast force, meaningless without the ground it is measured against. That is the opposite of an intrinsic pixel-group property.

### 3.7 Shape: complexity, regularity, compactness

**Quantification status: WEAK for weight per se; complexity is quantifiable but its aesthetic function is NONLINEAR.**

- Arnheim's claims — intrinsic interest adds weight; simpler/more regular shapes are heavier; compactness adds weight — have **no direct modern quantification as weight coefficients** (gap).
- **Complexity can be measured:** Forsythe, Nadal, Sheehy, Cela-Conde & Sawey (2011, Tier 1), *Br. J. Psychol.*, 102, 49–70, DOI 10.1348/000712610X498958 — perceived visual complexity in art is best predicted by automated measures, with **GIF compression** outperforming edge counts; fractal dimension accounts for more variance in beauty judgments than complexity alone. But the complexity–beauty function is contested: Berlyne's inverted-U vs. linear-vs-null findings across studies (Nadal et al., 2010; Silvia, 2005 — Tier 1, cited within these reviews). A factor whose contribution to liking changes sign with level cannot have a single native weight value.
- Removing color destroyed observers' ability to judge beauty at all (Forsythe et al.) — factors are not independently legible.
- Birkhoff (1933, Tier 2 book), *Aesthetic Measure*: M = O/C (order over complexity) — the earliest formula treating complexity as a weight-like denominator; "empirical studies almost immediately called it into question" (secondary summaries, Tier 2).

### 3.8 Orientation

**Quantification status: WEAK — preference effects established, weight coefficients not.**

- Latto, Brain & Kelly (2000, Tier 1), *Perception*, 29, 981–987, DOI 10.1068/p2352 — an **aesthetic oblique effect**: Mondrian compositions are preferred with horizontal/vertical component lines over oblique rotations; rotating the painting also changes its *lateral balance*, confounding orientation with weight.
- Plumhoff & Schirillo (2009, Tier 1), *Perception*, 38, 719–731, DOI 10.1068/p6160 — eye movements over Mondrian variants show the oblique effect in viewing behavior.
- Arnheim's "vertical heavier than oblique" has **no published weight coefficient** (gap); practitioner sources (Tier 2) variously claim diagonals are heaviest — i.e., the field cannot even agree on the ordinal ranking.

### 3.9 Depth cues and texture

**Status: LITERATURE GAP.** Arnheim lists depth (greater depicted depth = greater weight) and modern practitioners list texture as a weight factor (Tier 2 design writing), but I found **no Tier 1 study quantifying depth or texture as a visual-weight coefficient in balance judgments**. The nearest neighbor is Thömmes & Hübner (2018, Tier 1): balance predicted Instagram Likes in "3D-appearing" architectural photos but *reversed* in "2D" ones — depth appearance moderates the balance–liking link without being quantified as a weight.

### 3.10 Isolation / density

**Status: WEAK.** Arnheim's isolation claim (the moon in an empty sky) is unquantified experimentally. Ngo et al.'s (2003, Tier 1) *density* and *economy* measures formalize crowding, and attention research (Hagtvedt & Brasel, 2017, Tier 1) shows attention capture inflates apparent size — a plausible mechanism for isolation effects — but no coefficient exists.

## 4. How the literature says factors combine

| Model family | Combination rule | Source (Tier) |
|---|---|---|
| APB (Assessment of Preference for Balance) | **Additive**: sum of pixel weights (∝ darkness) differenced across 8 symmetric region pairs, averaged | Wilson & Chatterjee 2005 (1) |
| DCM (Deviation of Center of Mass) | **Additive moments**: Σ(massᵢ × positionᵢ)/Σmassᵢ; Euclidean distance of perceptual center of mass from geometric center, as % of max | Hübner & Fillinger 2016 (1); McManus et al. 2011 (1) |
| Interface aesthetics OM | **Weighted additive**: OM = Σ aᵢMᵢ over 14 normalized measures (balance, equilibrium, symmetry, sequence…) | Ngo, Teo & Byrne 2003 (1) |
| Visual-weight force model | **Vector resultant**: partial/integral contrast weights summed as forces; balance = resultant at geometric center | Parada-Castellano 2016 (1) |
| Color×area interaction | **Multiplicative/interactive**: perceived weight of a hue varies with the area it occupies; red/yellow most area-sensitive | Locher et al. 2005 (1) |
| Chroma×value joint effects | **Joint (non-additive)**: chroma and value interact in determining balanced area ratios | Morriss & Dunlap 1988 (1) |
| Saturation→attention→size chain | **Mediated causal chain**, not a coefficient | Hagtvedt & Brasel 2017 (1) |
| Learned nonlinear mapping | **Machine-learned** from large datasets of highly rated images; no closed form | Jahanian et al. 2015 (1, proceedings) |
| Multi-stage processing | **Stage model**: perceptual analysis → implicit memory → explicit classification → cognitive mastering → evaluation; balance is one input among many | Leder et al. 2004 (1) |
| Fluency | **Metacognitive**: liking = ease of processing; stimulus features matter only via processing dynamics | Reber et al. 2004 (1) |
| Top-weighted quadrant model | **Additive with fixed vertical anisotropy**: upper-quadrant Y × 1.07 | Corwin, bioRxiv (2, unreviewed) |

**The pattern:** the only models with real predictive success on controlled stimuli are *additive pixel-integration* models (APB, DCM) — and their success is confined to simple achromatic geometric patterns (see §5). Every attempt to handle real color compositions finds **interactions** (color×area, chroma×value) or retreats to mediation chains and learned mappings. No published model assigns simultaneous native values to all factors and combines them with a validated rule.

## 5. The native-values verdict

### 5.1 Where the hypothesis is CONFIRMED (narrowly)

1. **Darkness-as-mass works — for simple stimuli.** DCM/APB explain up to 68% of balance-rating variance and 86% of liking variance for homogeneous black-and-white geometric patterns (Hübner & Fillinger, 2016, Tier 1). This is the hypothesis's best empirical hour.
2. **The inverse-ratio law holds relationally.** Small/high-chroma balances large/low-chroma, independent of background and largely independent of hue (Morriss et al., 1982, Tier 1); Munsell's area law survives experimental comparison against Moon & Spencer's model.
3. **Hue shows a replicable ordinal pattern** (red heaviest, yellow lightest) across Bullough (1907), Pinkerton & Humphrey (1974), and Locher et al. (2005) — all Tier 1.
4. **Area is the universal multiplier.** No study disputes weight ∝ area.

### 5.2 Where the hypothesis BREAKS

**B1. Sign flips between paradigms (no stable coefficient).**
- Lightness: dark-heavy (DCM/APB) vs. bright-heavy (Arnheim) vs. luminance-irrelevant (Koenderink 2017).
- Saturation: amplifier of weight (Morriss; Munsell; Hagtvedt & Brasel) vs. *reducer* of apparent weight (Monroe 1925).
- A "native value" whose sign depends on the paradigm is not native.

**B2. The flagship measures fail on real artwork.**
- Gershoni & Hochstein (2011, Tier 1): APB **completely failed** to predict balance ratings for Japanese calligraphy; rotation changed perceived balance but cannot change APB at all; balance is computed at first fixation (≤100 ms) from **meaningful content before form** — an element's weight derives from its contextual meaning, not its formal attributes. DCM failed the same stimuli on replication (Fillinger & Hübner, 2018, as reported in Hübner & Fillinger, 2019, Tier 1).
- Hübner & Thömmes (2019, Tier 1), *Symmetry*, 11, 1468, DOI 10.3390/sym11121468: replicating Puffer (1903) with modern methods — **little to no evidence for balance** as a production principle; participants used *closeness* and *bilateral symmetry* instead of mechanical balance.
- McManus et al. (2011, Tier 1): the Arnheim–Ross axis theory fails its detailed predictions.

**B3. The balance–liking link is conditional, not lawful.**
- Hübner & Fillinger (2019, Tier 1), *i-Perception*, 10, DOI 10.1177/2041669519856040: the relations **depend on the picture type**. The 68%/86% figures come only from simple stimuli; for photographs the explained variance drops to ~6–14% (Thömmes & Hübner, 2018, Tier 1), and for calligraphy balance ratings were **entirely unrelated to liking** until prototypicality was discounted.
- Reber, Schwarz & Winkielman (2004, Tier 1): aesthetic pleasure is grounded in the perceiver's *processing experience*, explicitly "in contrast to theories that trace aesthetic pleasure to objective stimulus features per se" — a philosophical near-negation of the native-values program.

**B4. Figure–ground assignment precedes weight.** Weight is computed *after* the visual system decides what is figure and what is ground (Parada-Castellano's partial vs. integral weight; Corwin's frame/ground effect, Tier 2; Rubin's classic figure–ground organization). A figure–ground reversal reassigns every weight in the image — native values cannot survive a reversal they do not predict.

**B5. Culture changes the coefficients' signs.** Reading direction reverses horizontal weight/directionality preferences (Chokron & De Agostini, 2000; Maass et al., 2009 — Tier 1); holistic vs. analytic attention changes how much weight the ground carries at all (Masuda & Nisbett, 2001, Tier 1 — Americans focus on focal objects, Japanese on background context and object–field relations).

**B6. Individuals differ — systematically.** Jacobsen (2004, Tier 1) found stable individual *strategies* in aesthetic judgment; Vessel, Starr & Rubin (2012, Tier 1) showed aesthetic response is "highly individual," with a step-like default-mode response only for personally moving works; Nodine, Locher & Krupinski (1993, Tier 1) showed art training changes how compositions are perceived and judged (cf. Locher et al., 2005: only trained viewers detected color-driven balance shifts). Koenderink et al. (2017, Tier 1) found **strong idiosyncratic differences** even in the stripped-down luminance paradigm.

**B7. Task changes the construct.** Pierce (1894, Tier 1) already noted: *balance* is applied to horizontal arrangements, *stability* to vertical ones — observers prefer weight in the lower half (stability) while a mass model predicts indifference. Balance ratings, stability ratings, and liking ratings dissociate (Hübner & Fillinger, 2019).

**B8. Observers may not even compute what the models compute.** Friedenberg's work on perceiving the center of mass of multi-element displays (2002, Tier 1, DOI 10.3758/BF03194724; 2008, Tier 1, DOI 10.2174/1874230000802010013) and Liby's follow-ups show locating the center of mass is error-prone and biased by size ratio, symmetry, and elongation — if the visual system cannot reliably find the center of perceptual mass, a theory requiring it to do so is psychologically suspect.

**B9. No transfer from patches to objects.** Payne (1958, Tier 1): color heaviness rankings do not transfer to object weight perception. Native values measured on patches do not travel.

### 5.3 Bottom line for the hypothesis

| Component | Verdict |
|---|---|
| Native values exist for **area** | **Confirmed** — but only as a multiplier, never standalone |
| Native values exist for **lightness** | **Contested** — strongest numbers (DCM/APB) coexist with sign-flipped rivals and Koenderink's near-null |
| Native values exist for **saturation** | **Weak/contradictory** — amplifier in balance tasks, reducer in heaviness judgments |
| Native values exist for **hue** | **Weak** — replicable ordinal trend (red > … > yellow), no stable interval coefficient, confounded with lightness, no transfer to objects |
| Native values exist for **position** | **Structural, not intrinsic** — moment-arm math is shared, but horizontal sign is cultural and vertical coefficients are unreviewed |
| Native values exist for **contrast** | **Relational by definition** — the best formalization makes weight *depend* on the ground |
| Native values exist for **complexity/orientation/texture/depth** | **Unquantified or nonlinear** — measurable (compression, fractal dimension) but with non-monotonic aesthetic functions |
| **A valid combination rule** | **None published** — additive models work only on toy stimuli; real stimuli show interactions, mediation chains, and meaning-driven overrides |

**The honest summary:** the literature supports *contextual, relational* weights — each factor's contribution is real but parameterized by paradigm, picture type, ground assignment, culture, expertise, and task. The "exact mathematical formula" version of the hypothesis — fixed native values per factor, combined by a universal rule — is **disconfirmed in its strong form** and **unproven in every weak form** that has been tested beyond achromatic geometric patterns. The most defensible formalization today is Parada-Castellano's: weight as a *contrast force against a ground*, summed vectorially — which keeps the math but abandons intrinsicality.

## 6. Gaps worth flagging to the other workers

1. **Depth and texture** have no Tier 1 weight coefficients at all (§3.9).
2. **Orientation** has preference data but no weight coefficient (§3.8).
3. **Isolation** is unquantified (§3.10).
4. **No study assigns native values to all factors simultaneously** — the joint-estimation experiment the hypothesis needs has never been run.
5. **The first-fixation finding** (Gershoni & Hochstein, 2011) suggests weight is computed pre-attentively from meaning — a worker on perception science should chase the timing literature.

## 7. Bibliography

### Tier 1 — peer-reviewed

1. Abeln, J., Fresz, L., Amirshahi, S. A., McManus, I. C., Koch, M., Kreysa, H., & Redies, C. (2015). Preference for well-balanced saliency in details cropped from photographs. *Frontiers in Human Neuroscience*, 9, 704. DOI: 10.3389/fnhum.2015.00704 — access: open access via Frontiers.
2. Bullough, E. (1907). On the apparent heaviness of colours. *British Journal of Psychology*, 2(2), 111–152. — access: pre-DOI era; public domain; verify via journal archives.
3. Chokron, S., & De Agostini, M. (2000). Reading habits influence aesthetic preference. *Cognitive Brain Research*, 10(1–2), 45–49. DOI: 10.1016/S0926-6410(00)00021-5 — access: ScienceDirect (subscription).
4. Corwin, D. M. — see Tier 2 (preprint, unreviewed).
5. Forsythe, A., Nadal, M., Sheehy, N., Cela-Conde, C. J., & Sawey, M. (2011). Predicting beauty: Fractal dimension and visual complexity in art. *British Journal of Psychology*, 102(1), 49–70. DOI: 10.1348/000712610X498958 — access: https://pubmed.ncbi.nlm.nih.gov/21241285/ (PubMed record; full text via publisher).
6. Friedenberg, J. D. (2002). Perception of two-body center of mass. *Attention, Perception, & Psychophysics*, 64, 531–… DOI: 10.3758/BF03194724 — access: Springer (subscription).
7. Friedenberg, J. D. (2008). Perceiving the center of three-body displays: The role of size-ratio, symmetry, elongation, and gravity. *The Open Behavioral Science Journal*, 2, 13–… DOI: 10.2174/1874230000802010013 — access: open access via publisher.
8. Gershoni, S., & Hochstein, S. (2011). Measuring pictorial balance perception at first glance using Japanese calligraphy. *i-Perception*, 2(6), 508–527. DOI: 10.1068/i0472 — access: open access, https://pmc.ncbi.nlm.nih.gov/articles/PMC3485800/
9. Hagtvedt, H., & Brasel, S. A. (2017). Color saturation increases perceived product size. *Journal of Consumer Research*, 44(2), 396–413. DOI: 10.1093/jcr/ucx039 — access: https://EconPapers.repec.org/article/oupjconrs/v_3a44_3ay_3a2017_3ai_3a2_3ap_3a396-413..htm (metadata; full text via OUP).
10. Hübner, R., & Fillinger, M. G. (2016). Comparison of objective measures for predicting perceptual balance and visual aesthetic preference. *Frontiers in Psychology*, 7, 335. DOI: 10.3389/fpsyg.2016.00335 — access: open access, https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2016.00335
11. Hübner, R., & Fillinger, M. G. (2019). Perceptual balance, stability, and aesthetic appreciation: Their relations depend on the picture type. *i-Perception*, 10, 1–17. DOI: 10.1177/2041669519856040 — access: https://journals.sagepub.com/doi/10.1177/2041669519856040 (Sage; check open access).
12. Hübner, R., & Thömmes, K. (2019). Symmetry and balance as factors of aesthetic appreciation: Ethel Puffer's (1903) "Studies in Symmetry" revised. *Symmetry*, 11(12), 1468. DOI: 10.3390/sym11121468 — access: open access, https://www.mdpi.com/2073-8994/11/12/1468
13. Itti, L., Koch, C., & Niebur, E. (1998). A model of saliency-based visual attention for rapid scene analysis. *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 20(11), 1254–1259. DOI: 10.1109/34.730558 — access: IEEE Xplore (verify; subscription).
14. Jacobsen, T. (2004). Individual and group modelling of aesthetic judgment strategies. *British Journal of Psychology*, 95, 41–56. DOI: 10.1348/000712604322779451 — access: publisher (subscription).
15. Jahanian, A., Vishwanathan, S. V. N., & Allebach, J. P. (2015). Learning visual balance from large-scale datasets of aesthetically highly rated images. *Proceedings of SPIE 9394, Human Vision and Electronic Imaging XX*. DOI: 10.1117/12.2084548 — access: SPIE Digital Library (peer-reviewed proceedings).
16. Koenderink, J., van Doorn, A., & Gegenfurtner, K. (2017). Compositorial 'Weight' & 'Luminance'. *Art & Perception*, 5(3), 299–311. DOI: 10.1163/22134913-00002067 — access: full text via Utrecht repository, https://dspace.library.uu.nl/bitstream/handle/1874/357747/22134913_005_03_s003_text.pdf?sequence=1
17. Koenderink, J., van Doorn, A., & Gegenfurtner, K. (2018). Compositorial colour weight. *i-Perception*, 9(5), 1–46. DOI: 10.1177/2041669518788582 — access: Sage/i-Perception (check open access).
18. Koenderink, J., van Doorn, A., & Gegenfurtner, K. (2018). Color weight photometry. *Vision Research*, 151, 88–98. DOI: 10.1016/j.visres.2017.06.006 — access: ScienceDirect (subscription).
19. Latto, R., Brain, D., & Kelly, B. (2000). An oblique effect in aesthetics: homage to Mondrian (1872–1944). *Perception*, 29(8), 981–987. DOI: 10.1068/p2352 — access: https://pubmed.ncbi.nlm.nih.gov/11145089/ (PubMed record).
20. Leder, H., Belke, B., Oeberst, A., & Augustin, D. (2004). A model of aesthetic appreciation and aesthetic judgments. *British Journal of Psychology*, 95(4), 489–508. DOI: 10.1348/0007126042369811 — access: publisher (subscription).
21. Locher, P. J. (2006). Experimental scrutiny of the role of balance in the visual arts. In P. Locher, C. Martindale, & L. Dorfman (Eds.), *New Directions in Aesthetics, Creativity and the Arts* (pp. 19–32). Baywood. — access: book chapter (peer-reviewed volume).
22. Locher, P., Gray, S., & Nodine, C. (1996). The structural framework of pictorial balance. *Perception*, 25, 1419–1436. DOI: 10.1068/p251419 — access: publisher (subscription).
23. Locher, P., Overbeeke, K., & Stappers, P. J. (2005). Spatial balance of color triads in the abstract art of Piet Mondrian. *Perception*, 34(2), 169–189. DOI: 10.1068/p5033 — access: https://www.researchgate.net/publication/7903741_Spatial_Balance_of_Color_Triads_in_the_Abstract_Art_of_Piet_Mondrian (ResearchGate page; full text via publisher/PubMed PMID 15832568).
24. Locher, P. J., Stappers, P. J., & Overbeeke, K. (1998). The role of balance as an organizing design principle underlying adults' compositional strategies for creating visual displays. *Acta Psychologica*, 99, 141–161. DOI: 10.1016/S0001-6918(98)00008-0 — access: ScienceDirect (subscription).
25. Maass, A., Suitner, C., Favaretto, X., & Cignacchi, M. (2009). Groups in space: Stereotypes and the spatial agency bias. *Journal of Experimental Social Psychology*, 45(3), 496–504. DOI: 10.1016/j.jesp.2009.01.004 — access: postprint at https://www.ssoar.info/ssoar/handle/document/28344
26. Masuda, T., & Nisbett, R. E. (2001). Attending holistically versus analytically: Comparing the context sensitivity of Japanese and Americans. *Journal of Personality and Social Psychology*, 81(5), 922–934. — access: APA PsycNet (subscription); DOI not independently verified in this pass.
27. McManus, I. C., Edmondson, D., & Rodger, J. (1985). Balance in pictures. *British Journal of Psychology*, 76, 311–324. DOI: 10.1111/j.2044-8295.1985.tb01955.x — access: publisher (subscription).
28. McManus, I. C., Stöver, K., & Kim, D. (2011). Arnheim's Gestalt theory of visual balance: Examining the compositional structure of art photographs and abstract images. *i-Perception*, 2(6), 615–647. DOI: 10.1068/i0445aap — access: open access, https://pmc.ncbi.nlm.nih.gov/articles/PMC3485801/
29. Monroe, M. (1925). The apparent weight of color and correlated phenomena. *The American Journal of Psychology*, 36(2), 192–206. — access: pre-DOI; JSTOR/PsycINFO.
30. Morriss, R. H., Dunlap, W. P., & Hammond, E. H. (1982). Influence of chroma on spatial balance of complementary hues. *American Journal of Psychology*, 95, 323–332. — access: pre-DOI; JSTOR/PsycINFO.
31. Morriss, R. H., & Dunlap, W. P. (1987). Influence of value on spatial balance of color pairs. *Journal of General Psychology*, 114, 353–361. — access: publisher (subscription).
32. Morriss, R. H., & Dunlap, W. P. (1988). Joint effects of chroma and value on spatial balance of color pairs. *Empirical Studies of the Arts*. DOI: 10.2190/46M2-30KP-CA57-ARQV — access: Sage/Baywood (subscription; journal details per publisher page).
33. Ngo, D. C. L., Teo, L. S., & Byrne, J. G. (2003). Modelling interface aesthetics. *Information Sciences*, 152, 25–46. — access: ScienceDirect (subscription); DOI not located in this pass.
34. Nodine, C. F., Locher, P. J., & Krupinski, E. A. (1993). The role of formal art training on perception and aesthetic judgment of art compositions. *Leonardo*, 26, 219–227. DOI: 10.2307/1575815 — access: JSTOR/MIT Press.
35. Palmer, S. E., Schloss, K. B., & Sammartino, J. (2013). Visual aesthetics and human preference. *Annual Review of Psychology*, 64, 77–107. DOI: 10.1146/annurev-psych-120710-100504 — access: https://pubmed.ncbi.nlm.nih.gov/23020642/ (PubMed record; full text via Annual Reviews).
36. Parada-Castellano, R. (2016). Study of balance of images using visual weight. *Color Research & Application*, 41(2), 175–187. DOI: 10.1002/col.21943 — access: publisher (subscription).
37. Payne, M. C., Jr. (1958). Apparent weight as a function of color. *The American Journal of Psychology*, 71(4), 725–730. — access: pre-DOI; JSTOR/PsycINFO.
38. Pierce, E. (1894). Studies from the Harvard Psychological Laboratory (II): The aesthetics of simple forms. I. Symmetry. *Psychological Review*, 1, 483–495. DOI: 10.1037/h0073983 — access: APA archives.
39. Pinkerton, E., & Humphrey, N. K. (1974). The apparent heaviness of colours. *Nature*, 250(5462), 164–165. DOI: 10.1038/250164a0 — access: Nature (subscription).
40. Plumhoff, J., & Schirillo, J. (2009). Mondrian, eye movements and the oblique effect. *Perception*, 38, 719–731. DOI: 10.1068/p6160 — access: publisher (subscription).
41. Puffer, E. D. (1903). Studies in symmetry. *Psychological Review Monograph Supplements*, 4 (Harvard Psychological Studies, 1), 467–539. — access: pre-DOI; APA archives.
42. Reber, R., Schwarz, N., & Winkielman, P. (2004). Processing fluency and aesthetic pleasure: Is beauty in the perceiver's processing experience? *Personality and Social Psychology Review*, 8(4), 364–382. DOI: 10.1207/S15327957PSPR0804_3 — access: https://pubmed.ncbi.nlm.nih.gov/15582859/ (PubMed record).
43. Redies, C., Bartho, R., Koßmann, L., Spehar, B., Hübner, R., Wagemans, J., & Hayn-Leichsenring, G. U. (2025). A toolbox for calculating quantitative image properties in aesthetics research. *Behavior Research Methods*, 57(4), 117. DOI: 10.3758/s13428-025-02632-3 — access: open access, https://pubmed.ncbi.nlm.nih.gov/40087197/
44. Rodway, P., Schepman, A., & Lambert, J. (2012). Preferring the one in the middle: Further evidence for the centre-stage effect. *Applied Cognitive Psychology*, 26(2), 215–222. DOI: 10.1002/acp.1812 — access: publisher (subscription).
45. Thömmes, K., & Hübner, R. (2018). Instagram likes for architectural photos can be predicted by quantitative balance measures and curvature. *Frontiers in Psychology*, 9, 1050. DOI: 10.3389/fpsyg.2018.01050 — access: open access, https://www.frontiersin.org/articles/10.3389/fpsyg.2018.01050/pdf
46. Vessel, E. A., Starr, G. G., & Rubin, N. (2012). The brain on art: Intense aesthetic experience activates the default mode network. *Frontiers in Human Neuroscience*, 6, 66. DOI: 10.3389/fnhum.2012.00066 — access: open access, https://pubmed.ncbi.nlm.nih.gov/22529785/
47. Walker, P., Francis, B. J., & Walker, L. (2010). The brightness-weight illusion: Darker objects look heavier but feel lighter. *Experimental Psychology*, 57(6), 462–469. PMID 20382626 — access: PubMed record via https://reference.medscape.com/medline/abstract/20382626; DOI not independently verified in this pass.
48. Wilson, A., & Chatterjee, A. (2005). The assessment of preference for balance: Introducing a new test. *Empirical Studies of the Arts*, 23, 165–180. DOI: 10.2190/B1LR-MVF3-F36X-XR64 — access: publisher (subscription).
49. Xu, X., Zhang, J., Zhu, Q., & Xia, T. (2023). The influences of gradient color on the weight perception and stability perception: A preliminary study. *i-Perception*, 14(4). DOI: 10.1177/20416695231197797 — access: Sage/i-Perception (check open access).
50. Fillinger, M. G., & Hübner, R. (2018). The relations between balance, prototypicality, and aesthetic appreciation for Japanese calligraphy. *Empirical Studies of the Arts*. — access: findings reported and discussed in Hübner & Fillinger (2019); standalone DOI not located in this pass — **flag for verification before citing independently**.

### Tier 2 — books, preprints, practitioner and secondary sources

- Arnheim, R. (1974). *Art and Visual Perception: A Psychology of the Creative Eye* (rev. ed.). University of California Press. — book; factor inventory (§2) via secondary chapter notes.
- Birkhoff, G. D. (1933). *Aesthetic Measure*. Harvard University Press. — book; M = O/C.
- Corwin, D. M. (2020–2022). Pictorial balance is a bottom-up aesthetic property mediated by eye movements. *bioRxiv* preprint, DOI 10.1101/2020.05.26.104687 — **not peer-reviewed**; 1.07 top-weighting factor and frame/ground findings are unreviewed estimates. https://www.biorxiv.org/content/10.1101/2020.05.26.104687v12.full
- Itten, J. (1961). *Kunst der Farbe / The Art of Color*. — book; harmonic area ratios 3:4:6:9:8:6 (yellow:orange:red:violet:blue:green), unvalidated. Tutorial summary: http://gitta.info/LayoutDesign/en/html/ColorDesign_learningObject5.html
- Munsell, A. H. (1905). *A Color Notation*. — book; law of inverse ratios of areas.
- Moon, P., & Spencer, D. E. (1944). Aesthetic measure applied to color harmony / Area in color harmony. *Journal of the Optical Society of America*, 34. — historical model (chroma + value + background contrast); described and tested against Munsell in Morriss et al. (1982).
- Ross, D. W. (1907). *A Theory of Pure Design*. Houghton Mifflin. — book (public domain); origin of the mechanical-balance/frame method.
- "Does red weigh more than blue?" — secondary synthesis of Bullough/Monroe/Pinkerton & Humphrey/Payne with reported rankings: https://scienceblogs.com/mixingmemory/2006/12/02/does-red-weigh-more-than-blue-1
- Visual-weight practitioner summary (size, color, saturation, position, texture, form, orientation, density): https://medium.com/design-bootcamp/visual-weight-and-visual-direction-visual-compensation-799ad8355a09
- Curated color-perception evidence file (warns against encoding absolute hue-weight rankings): https://github.com/doiiarx/claude-skills/blob/HEAD/scientific-color-maps/references/evidence-and-tools.md

---

*Worker E notes for the orchestrator: the single most load-bearing disconfirmations for the main study are (1) Koenderink et al. 2017 — luminance "hardly important," strong idiosyncratic differences; (2) Gershoni & Hochstein 2011 — APB fails completely on calligraphy, "meaningful content before form"; (3) Hübner & Thömmes 2019 — Puffer replication finds little/no evidence for balance; (4) the sign-flip catalog in §5.2-B1. The strongest confirmations are DCM/APB on simple stimuli, the Munsell/Morriss inverse-ratio law, and area-as-multiplier. Recommended follow-up experiment: the joint-estimation study (§6.4) — fit per-factor coefficients simultaneously on one stimulus set and test whether any coefficient survives picture-type, culture, and task changes.*
