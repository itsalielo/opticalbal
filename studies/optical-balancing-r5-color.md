# OPTICAL BALANCING — Round 5: Color-Science Deep Dive (the separability question)

**Angle:** can the effects of hue, lightness, and saturation on perceived weight/heaviness be disentangled — i.e., do the three color factors separate, or do they only exist as interactions?
**Date:** 2026-10-09 · **Worker:** R5-color · **Status:** literature survey, every item verified by exact-title search (DOI, PMID, or stable URL).

## 0. How this was sourced

- **Tier 1** = peer-reviewed journal papers, theses excluded. Each verified by searching its exact title; bibliography gives DOI/PMID/stable URL.
- **Tier 2** = books (incl. public-domain), theses, technical reports. Clearly marked.
- **Not verified** = cited-by-others items I could not independently retrieve. Flagged in §9, never presented as established.
- Summaries in my own words; quotes kept under 50 words per work. Equations are reproduced as factual formulae.
- Items from the mission's already-logged list are referenced, not re-reported. **Fukada:** full text remains a dead end (his later follow-up with real numbers — black>gray>white kick, blue<green<yellow<red resistance — was already recovered in Round 3).

## 1. The crux, first: Teixeira et al. 2026 (Symmetry)

**I could not retrieve this paper.** Repeated exact and variant searches (title fragments, author + journal, DOI-prefix search `10.3390/sym18` + Teixeira, MDPI Symmetry 2026 volume scan) returned no such article — only an unrelated 2026 Symmetry eye-tracking paper on background color and reading (DOI 10.3390/sym18010076, no Teixeira author). Possibilities: the citation is slightly off (year, journal, or spelling), or the paper is too new to be indexed. **The claim "hue and saturation don't separate ecologically" therefore rests on a parent-supplied citation I could not independently verify.** Everything below is what the retrievable literature actually says about separability — and the short version is: the non-separability thesis is well supported even without Teixeira.

## 2. The headline answer: the 2-factor ceiling is broken — for heaviness, not for balance

The mission's logged "2 → 6 gap" (Morriss & Dunlap 1988 as the joint-factorial ceiling) needs a scope correction. **For spatial-balance area-ratio tasks, M&D 1988 remains the ceiling. For perceived heaviness of colors, three factors were jointly manipulated decades earlier** — and the results directly answer the separability question.

### 2.1 Alexander & Shansky (1976) — the single most important find of this round

**Alexander, K. R., & Shansky, M. S. (1976). Influence of hue, value, and chroma on the perceived heaviness of colors. *Perception & Psychophysics*, 19(1), 72–74.** (Tier 1; pre-DOI era, no DOI exists. Verified via citations in Nature Communications 2020, Woods et al. crossmodal review, and a PLOS ONE reference list.)

Using **magnitude estimation** on Munsell-specified colors — hue, value, and chroma jointly varied — they found:

- **Apparent heaviness is an increasing function of chroma/saturation.**
- **Apparent heaviness is a decreasing function of value/lightness** (darker = heavier).
- **Hue has little influence on apparent weight.**

This is the cleanest separability result in the entire literature: three factors in, two survive, one drops out. It also directly contradicts Monroe (1925), where increasing saturation made colors weigh *less* — the sign flip Worker E flagged now has a second witness on the opposite side, and the method differs (Monroe: fulcrum balancing; A&S: magnitude estimation), which is the honest account of the contradiction.

### 2.2 Wright (1962) — the other three-factor study

**Wright, B. (1962). The influence of hue, lightness, and saturation on apparent warmth and weight. *The American Journal of Psychology*, 75(2), 232–241.** PMID 14008416. (Tier 1; verified via JOSA A 2025, NTT Technical Review, and Hogrefe reference lists.)

Joint manipulation of all three factors against two response dimensions (warmth *and* weight) — the earliest study to put the full triple on weight. Warmth and weight were both measured, which matters: it lets you see whether the factor structure of "weight" and "warmth" judgments dissociate. (Full-text findings not re-verified in this pass beyond the design; the paper is the structural precedent for every later three-factor design.)

### 2.3 The pre-history: weight, size, and color were never separate constructs

- **De Camp, J. E. (1917). The influence of color on apparent weight: A preliminary study. *Journal of Experimental Psychology*, 2, 347–370.** (Tier 1; verified via PLOS ONE reference list. Note: Hogrefe's reference list misprints the volume as "62" — it is vol. 2.) The founding experiment: colored cubes judged for apparent weight; weak, inconsistent brightness effects. Everything since is a footnote to De Camp's inconsistency.
- **Warden, C. J., & Flynn, E. L. (1926). The effect of color on apparent size and weight. *American Journal of Psychology*, 37, 398–401.** (Tier 1; verified via Hogrefe reference list.) Color × apparent size *and* weight in one design — the size confound that haunts all heaviness work was on the table from 1926.
- **Wallis, W. A. (1935). The influence of color on apparent size. *Journal of General Psychology*, 13, 193–199.** (Tier 1; verified via Walker et al. 2017 reference list.) Color → apparent size, the mediating path (cf. Hagtvedt & Brasel's saturation→attention→size chain, already logged).

## 3. The hue paradox: two clean results, opposite conclusions

- **Pinkerton & Humphrey (1974, *Nature*; DOI 10.1038/250164a0)** — with brightness carefully controlled (transilluminated stimuli, subjectively equated), hue differences in apparent weight *survive*: "Coloured circles, equal in subjective brightness, differ considerably in apparent weight, while achromatic stimuli which differ in brightness are not consistently different in weight." Separability: YES for hue.
- **Alexander & Shansky (1976)** — with hue, value, chroma jointly manipulated and magnitude estimation: hue has *little influence*. Separability: hue drops out.

Both are Tier 1, both controlled brightness, opposite verdicts on hue. The methods differ (fulcrum/adjustment vs. magnitude estimation; small hue sets vs. Munsell sampling). **This is the live contradiction at the center of the separability question, and no later paper resolves it.** Anyone fitting the six-factor model must decide which paradigm's hue coefficient to trust — or model the paradigm as a moderator.

## 4. The CIELAB era: actual numbers assigning weight to color coordinates

### 4.1 Ou, Luo, Woodcock & Wright (2004) — quantitative formulae, and they disagree with each other

**Part I: Ou, L.-C., Luo, M. R., Woodcock, A., & Wright, A. (2004). A study of colour emotion and colour preference. Part I: Colour emotions for single colours. *Color Research & Application*, 29(3), 232–240.** (Tier 1; formulae verified via secondary reproduction of the paper's equations.)

Fitted models mapping CIELAB to emotion scales (British + Chinese observers):

- **Heavy–light: HL = −2.1 + 0.05(100 − L\*), R² = 0.76** — hue and chroma *drop out entirely*. Lightness is the whole story.
- **Colour weight (the factor-analytic factor): CW = −1.8 + 0.04(100 − L\*) + 0.45·cos(h − 100°), R² = 0.73** — lightness *plus a hue term*, no chroma term.
- **Warm–cool: WC = −0.5 + 0.02(C\*)^1.07·cos(h − 50°), R² = 0.74** — a hue×chroma *interaction* (multiplicative), no lightness term.

So within one paper, "heavy–light" separates cleanly onto L\* while "colour weight" needs hue and "warm–cool" is irreducibly interactive. The separability answer is *construct-dependent*: ask about "heavy–light" and the factors separate; ask about "warm–cool" and they don't. This is the quantitative version of Teixeira's alleged claim, twelve years before the CIELAB-era replication attempts.

**Part II: Ou et al. (2004). Part II: Colour emotions for two-colour combinations. *Color Res. Appl.*, 29, 292–298. DOI 10.1002/col.20024.** (Tier 1.) An **additivity relationship**: pair emotion ≈ mean of the two single-color emotions — a genuine combination rule, though it fails for preference prediction.

### 4.2 Xin, Cheng, Taylor, Sato & Hansuebsai (2004) — lightness + chroma swamp hue

**Part I: Quantitative analysis. *Color Res. Appl.*, 29(6), 451–457. DOI 10.1002/col.20062.** (Tier 1; verified via ResearchGate record.) 218 color samples, 12 emotion pairs (incl. heavy–light), Hong Kong/Japan/Thailand observers. Finding: **"the influences of lightness and chroma were found to be much more important than that of the hue on the colour emotions studied"** — with the best cross-regional agreement on light–dark and heavy–light. Hue is the weakest of the three factors, cross-culturally. (Part II, qualitative analysis: DOI 10.1002/col.20063.)

**Gao, X. P., Xin, J. H., Sato, T., Hansuebsai, A., Scalzo, M., Kajiwara, K., Guan, S. S., Valldeperas, J., & Lis, M. J. (2007). Analysis of cross-cultural color emotion. *Color Res. Appl.*, 32(3), 223–229.** (Tier 1; verified via Kyoto Tech publication list.) Extends the separability finding across more cultures.

### 4.3 Koenderink, van Doorn & Gegenfurtner (2018) — "Color weight photometry": the max-rule

**Koenderink, J., van Doorn, A., & Gegenfurtner, K. (2018). Color weight photometry. *Vision Research*, 151, 88–98. DOI 10.1016/j.visres.2017.06.006.** (Tier 1; full text retrieved and read.)

Eight paradigms, 17 observers, pairwise "balancing" of the principal colors RYGCBM — the most direct modern attempt to assign weight values to color coordinates. Two findings that matter for the formula:

1. **Heterochromatic photometry paradigms → weights track the CIE luminance functional. Mid/high-level "compositorial" tasks → R, G, B channels become *equipollent* (1:1:1), and the nonlinear max-rule, weight ≈ max(r,g,b), fits better than any linear functional.**
2. Their conclusion: "there exists a clearcut dichotomy between the linear CIE functional and the equipollent max-rule… 'Color weight' and CIE 'luminance' are categorically distinct concepts."

For the mission: **any formula that computes color weight as a linear functional of luminance is wrong for the compositorial task** — the combination rule is nonlinear (max, not sum). This converges with the computational track's finding that nobody sees hue as hue, only luminance — and sharpens it: they don't see luminance either, they see something like max-channel.

**Koenderink, van Doorn & Gegenfurtner (2018). Compositorial colour weight. *i-Perception*, 9(5), 1–46. DOI 10.1177/2041669518788582.** (Tier 1; already in Worker E's bibliography — re-read here for the separability angle, not counted as new.) Companion piece; same program.

## 5. Modern three-factor separability tests (not weight, but the method the weight field never used)

- **Devinck, F., & Knoblauch, K. (2025). Warm/cool judgments as a function of hue, value, and chroma. *JOSA A*, 42(5), B68–B75. DOI 10.1364/JOSAA.545368.** (Tier 1; full text retrieved.) Three-way **maximum-likelihood conjoint measurement**: 20 hues × 2 values × 2 chromas (80 stimuli, 3,160 pairs), plus a two-way follow-up. Result: warm/cool judgments depended on hue for most observers, value contributed with individual variation, and there was **little evidence for an effect of chroma** — chroma dropped out of the model entirely. This is the methodologically strongest separability test in the corpus (conjoint measurement, model selection by information criterion), and its answer is: hue and value separate; chroma doesn't earn a coefficient. Note the contrast with Alexander & Shansky (chroma mattered for *heaviness*) — again, construct-dependent.
- **Wilms, L., & Oberfeld, D. (2018). Color and emotion: effects of hue, saturation, and brightness. *Psychological Research*, 82(5), 896–914. DOI 10.1007/s00426-017-0880-8.** (Tier 1.) All three dimensions *and their interactions* drive emotion — the interaction terms are significant, i.e., the factors do not fully separate for affect.
- **Dresp-Langley, B., & Reeves, A. (2014). Effects of saturation and contrast polarity on the figure-ground organization of color on gray. *Frontiers in Psychology*, 5, 1136. DOI 10.3389/fpsyg.2014.01136.** (Tier 1; verified via HAL.) **Hue as such does not significantly affect** relative background brightness or figure-ground organization; **saturation × contrast-polarity interaction is significant**. Hue drops out again; saturation survives only in interaction.
- **Koenderink, J., van Doorn, A., & Braun, D. (2024). "Warm," "Cool," and the colors. *Journal of Vision*, 24(7), 5.** (Tier 1; verified via Devinck & Knoblauch reference list.) Ordinal-judgment mapping of the warm/cool dimension.

## 6. Adjacent threads

**Advancing/receding (depth = weight, per Arnheim's depth factor):**
- **Bailey, R., Grimm, C., et al. (2007). The effect of object color on depth ordering. Tech. Report WUCSE-2007-18, Washington Univ.** (Tier 2; verified via OpenScholarship record.) Warm colors appear nearer; the cue strengthens against darker backgrounds — a **background × color interaction** on depth. Realistic shaded objects, not patches.
- Leads not independently verified (cited in a published reference list): Mount, Case, Sanderson & Brenner (1956, *J. Gen. Psychol.* — distance judgments of colored objects); Egusa (1977 — the color stereoscopic phenomenon / chromostereopsis).

**Cross-sensory correspondences (heaviness as an aligned dimension):**
- **Walker, P., Scallon, G., & Francis, B. (2017). Cross-sensory correspondences: Heaviness is dark and low-pitched. *Perception*, 46(7), 772–792. DOI 10.1177/0301006616684369.** (Tier 1.) Felt heaviness (size/mass dissociated) induces judgments of darkness — bidirectionality confirmed.
- **Walker, P., Scallon, G., & Francis, B. (2020). Heaviness-brightness correspondence and stimulus-response compatibility. *Atten. Percept. Psychophys.*, 82, 1949–1970.** (Tier 1.)
- **Walker, P., Walker, L., & Francis, B. J. (2015). The size-brightness correspondence. *Atten. Percept. Psychophys.*, 77, 2694–2710.** (Tier 1.)
- Scallon, G. (2018). PhD thesis, Lancaster, on heaviness in cross-sensory correspondences (Tier 2).

**Munsell-era (weight-adjacent, non-experimental):**
- **Pope, A. (1922). *Tone Relations in Painting*.** (Tier 2; public-domain book.) Pope's critique of Munsell is a separability claim in prose: Munsell equates chroma steps across hues, but "the relation between Intensity (or Chroma) contrasts and Value contrasts is not observed" — value contrast, Pope argues, "exerts a much greater attraction on the eye" than the highest chroma contrast. I.e., **value outranks chroma as an attentional weight**, stated 1922.
- Itten's harmonic area ratios (yellow:orange:red:violet:blue:green = 3:4:6:9:8:6) remain the only historical *quantitative* weight ranking — already covered by Worker E, unvalidated, not re-reported.

**Thesis with a null result worth keeping:**
- **Dolese, M. J. (2006). Perceived weight of color: Its effect on balance evinced by scanning strategies. MA thesis, Montclair State Univ. (chair: P. Locher).** https://digitalcommons.montclair.edu/etd/1146/ (Tier 2.) Recoloring the *largest* area of Mondrian compositions (red→blue/yellow) did **not** significantly shift the perceived balance center or fixation distribution — area dominated color in a real-composition balance task. The one clean "color vs. area" dissociation on record.

## 7. The separability verdict

| Factor | Separates? | Evidence |
|---|---|---|
| Lightness/value | **Yes — the load-bearing factor** | Survives in every paradigm: A&S 1976 (negative), Ou 2004 HL = f(L\*) only, Xin 2004 (dominant), Walker 2017 (heaviness↔darkness) |
| Saturation/chroma | **Sometimes — sign and survival are paradigm-relative** | Amplifier in A&S 1976; drops out in Devinck & Knoblauch 2025 (warm/cool) and Dresp-Langley 2014 (figure-ground); interacts with polarity (Dresp-Langley) and with hue (Ou 2004 WC); *reduces* heaviness in Monroe 1925 |
| Hue | **Weakest; drops out under joint manipulation** | Null in A&S 1976 (magnitude estimation), null in Xin 2004 (cross-cultural), null in Dresp-Langley 2014 — BUT survives brightness-matching in Pinkerton & Humphrey 1974. The contradiction is method-bound and unresolved. |
| Combination rule | **Not additive-linear** | Ou 2004: hue×chroma multiplicative for warm–cool; Koenderink 2018: max-rule beats linear functional for compositorial weight; Wilms & Oberfeld 2018: significant interaction terms |

**Bottom line for the mission:** the separability question does not have one answer because "weight" is not one construct. Perceived *heaviness of color patches* decomposes (lightness dominant, chroma secondary, hue negligible — A&S 1976). *Compositorial* weight follows a nonlinear max-rule over channels, not a linear luminance functional (Koenderink 2018). *Warm–cool* is irreducibly hue×chroma interactive (Ou 2004). Any "exact formula" must therefore be indexed to the task — and the six-factor fit the computational track is attempting will inherit all of these contradictions the moment it leaves synthetic stimuli. The honest prior for the lab protocol: fit lightness first (it will survive), expect chroma's coefficient to be paradigm-fragile, and pre-register hue as the factor most likely to wash out.

## 8. Gaps for the other workers

1. **No joint color×position or color×area factorial on *balance* judgments** — the M&D 1988 ceiling stands for the balance task specifically. Dolese 2006 is the nearest (null) result.
2. **The Pinkerton-vs-A&S hue contradiction** has no adjudicating study (fulcrum vs. magnitude estimation, never directly compared).
3. **No replication of Alexander & Shansky 1976** found — the most important separability result in the field appears never to have been re-run.
4. Koenderink's max-rule has not been tested against the Russian additive model or DCM on the same stimulus set.

## 9. Not verified / dead ends

- **Teixeira et al. 2026 (Symmetry)** — not found; see §1. Do not cite until retrieved.
- **Wise & Wise (1988)** — cited by Koenderink et al. (2017, 2018) in the weight literature; exact-title search returned nothing. Possibly a book/chapter citation error. Not verified.
- **Monroe (1926)** as cited by Koenderink — is a typo for **Monroe (1925)**, *Am. J. Psychol.*, 36, 192–206 (confirmed via 1926 *Psychological Bulletin* abstract). No separate 1926 paper.
- **Katra et al.** (NCS-chip warm/cool × hue/saturation/lightness ratings, cited in Devinck & Knoblauch 2025) — could not independently verify; lead only.
- **Fukada** — full text dead end (see §0).

## 10. Bibliography

### Tier 1 — peer-reviewed (18 new)

1. Alexander, K. R., & Shansky, M. S. (1976). Influence of hue, value, and chroma on the perceived heaviness of colors. *Perception & Psychophysics*, 19(1), 72–74. — pre-DOI era; verified via multiple citing sources.
2. De Camp, J. E. (1917). The influence of color on apparent weight: A preliminary study. *Journal of Experimental Psychology*, 2, 347–370. — pre-DOI; vol. 2 (not 62).
3. Devinck, F., & Knoblauch, K. (2025). Warm/cool judgments as a function of hue, value, and chroma. *Journal of the Optical Society of America A*, 42(5), B68–B75. DOI 10.1364/JOSAA.545368 — full text retrieved.
4. Dresp-Langley, B., & Reeves, A. (2014). Effects of saturation and contrast polarity on the figure-ground organization of color on gray. *Frontiers in Psychology*, 5, 1136. DOI 10.3389/fpsyg.2014.01136 — PMID 25339931.
5. Gao, X. P., Xin, J. H., Sato, T., Hansuebsai, A., Scalzo, M., Kajiwara, K., Guan, S. S., Valldeperas, J., & Lis, M. J. (2007). Analysis of cross-cultural color emotion. *Color Research & Application*, 32(3), 223–229. — verified via institutional publication list.
6. Koenderink, J., van Doorn, A., & Gegenfurtner, K. (2018). Color weight photometry. *Vision Research*, 151, 88–98. DOI 10.1016/j.visres.2017.06.006 — full text retrieved.
7. Koenderink, J., van Doorn, A., & Braun, D. (2024). "Warm," "Cool," and the colors. *Journal of Vision*, 24(7), 5. — verified via citing paper.
8. Ou, L.-C., Luo, M. R., Woodcock, A., & Wright, A. (2004). A study of colour emotion and colour preference. Part I: Colour emotions for single colours. *Color Research & Application*, 29(3), 232–240. — equations verified via secondary reproduction.
9. Ou, L.-C., Luo, M. R., Woodcock, A., & Wright, A. (2004). Part II: Colour emotions for two-colour combinations. *Color Research & Application*, 29, 292–298. DOI 10.1002/col.20024.
10. Walker, P., Scallon, G., & Francis, B. (2017). Cross-sensory correspondences: Heaviness is dark and low-pitched. *Perception*, 46(7), 772–792. DOI 10.1177/0301006616684369.
11. Walker, P., Scallon, G., & Francis, B. (2020). Heaviness-brightness correspondence and stimulus-response compatibility. *Attention, Perception, & Psychophysics*, 82, 1949–1970. — verified via Lancaster EPrints.
12. Walker, P., Walker, L., & Francis, B. J. (2015). The size-brightness correspondence: Evidence for crosstalk among aligned conceptual feature dimensions. *Attention, Perception & Psychophysics*, 77, 2694–2710. — verified via citing reference list.
13. Wallis, W. A. (1935). The influence of color on apparent size. *Journal of General Psychology*, 13, 193–199. — pre-DOI; verified via citing reference list.
14. Warden, C. J., & Flynn, E. L. (1926). The effect of color on apparent size and weight. *American Journal of Psychology*, 37, 398–401. — pre-DOI; verified via Hogrefe reference list.
15. Wilms, L., & Oberfeld, D. (2018). Color and emotion: effects of hue, saturation, and brightness. *Psychological Research*, 82(5), 896–914. DOI 10.1007/s00426-017-0880-8.
16. Wright, B. (1962). The influence of hue, lightness, and saturation on apparent warmth and weight. *American Journal of Psychology*, 75(2), 232–241. PMID 14008416.
17. Xin, J. H., Cheng, K. M., Taylor, G., Sato, T., & Hansuebsai, A. (2004). Cross-regional comparison of colour emotions Part I: Quantitative analysis. *Color Research & Application*, 29(6), 451–457. DOI 10.1002/col.20062.
18. Xin, J. H., Cheng, K. M., Taylor, G., Sato, T., & Hansuebsai, A. (2004). Part II: Qualitative analysis. *Color Research & Application*, 29, 458–466. DOI 10.1002/col.20063.

Re-read (already in Worker E's bibliography, new separability analysis here — not counted as new): Koenderink, van Doorn & Gegenfurtner (2018), Compositorial colour weight, *i-Perception*, 9(5), 1–46, DOI 10.1177/2041669518788582. Re-verified: Payne (1958), PMID 13627281.

### Tier 2 — books, theses, reports

- Pope, A. (1922). *Tone Relations in Painting*. — public-domain book; value-vs-chroma attraction argument (§6).
- Bailey, R., Grimm, C., et al. (2007). The effect of object color on depth ordering. Tech. Report WUCSE-2007-18, Washington University. https://openscholarship.wustl.edu/cse_research/122/
- Dolese, M. J. (2006). Perceived weight of color: Its effect on balance evinced by scanning strategies. MA thesis, Montclair State University. https://digitalcommons.montclair.edu/etd/1146/
- Scallon, G. (2018). Cross-sensory correspondences: cross-activation of connotative feature dimensions through the felt heaviness of lifted objects. PhD thesis, Lancaster University. — via Lancaster EPrints.

---

*Worker notes for orchestrator: (1) 18 new Tier 1 items. (2) YES — joint-factorial color×weight studies exist beyond Morriss & Dunlap 1988: Alexander & Shansky 1976 (hue×value×chroma, magnitude estimation) and Wright 1962 (hue×lightness×saturation, warmth+weight); the "2-factor ceiling" holds only for spatial-balance area-ratio tasks. (3) Most important find: Alexander & Shansky (1976) — heaviness = +chroma, −value, hue ≈ null; pre-DOI, no DOI exists (Percept. Psychophys. 19(1), 72–74). Closest DOI-bearing equivalent: Devinck & Knoblauch (2025), DOI 10.1364/JOSAA.545368. (4) Teixeira 2026 could not be retrieved — flag before citing.*
