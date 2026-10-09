# Optical Balancing — Round 2: The Missing Experiment & Unverified Items

**Worker A, Round 2 (2026-10-09).** Built on the Round 1 master study (`optical-balancing-study.md`); does not duplicate its findings. Two tasks: (1) hunt for any experiment that ever fit native visual-weight values for multiple factors simultaneously; (2) resolve or kill the four unverified items from Round 1.

**Headline verdicts:**
- **Task 1:** The missing experiment still does not exist. No study has ever fit saturation × hue × lightness × area × position × contrast jointly. But the hunt turned up something Round 1 missed entirely: a whole **quantitative "spatial balance of color pairs" tradition** (Munsell → Moon & Spencer 1944 → Granger 1953 → Morriss & Dunlap 1982/87/88) that *did* fit area × chroma and area × value and chroma × hue — the missing experiment's direct ancestors at n = 2 factors. This is the ready-made experimental paradigm for running the real thing.
- **Task 2:** Three of four items RESOLVED (all Tier 1). One (Corwin preprint) confirmed still-unreviewed — remains below Tier 1, but now with verified status rather than an open question.

---

## Task 1 — The missing experiment: hunt report

### The question
Round 1's gap #1: no validated weight function w(saturation, hue, lightness, area, position, contrast), because no experiment ever fit the native values of all factors at once — via conjoint measurement, factorial design, multiple regression of balance ratings, or multivariate ML on balance itself. Searched across vision science, empirical aesthetics, HCI, computational aesthetics, and color science.

### Search trail (documented)
Queries run: `conjoint measurement visual weight pictorial balance experiment` · `"conjoint analysis" visual aesthetics preference color size complexity experiment` · `"pictorial balance" "multiple regression" luminance chroma size predictors ratings` · `predicting pictorial balance from image features machine learning regression coefficients luminance color` · `factorial experiment "visual weight" balance saturation size hue judgment aesthetics` · `Thurstone scaling visual weight balance color size paired comparison experiment fitted` · `thesis visual balance experiment fitting weights saturation hue size position conjoint` · targeted follow-ups on every lead (Morriss/Dunlap, Moon & Spencer, Granger, Pieters, Linnett, Bauerly & Liu, Altaboli & Lin, Ke et al., Dhar et al., Corwin).

### Verdict: the experiment does not exist — but its ancestors do

**Nobody has fit all six factors at once.** That stands. But the hunt was not empty. Ranked by closeness to the missing experiment:

**1. The spatial-balance-of-color-pairs tradition — the direct ancestors (n = 2 factors fitted).**
- **Morriss, R. H., & Dunlap, W. P. (1988). "Joint Effects of Chroma and Value on Spatial Balance of Color Pairs." *Empirical Studies of the Arts*, 6(2), 117–126. DOI 10.2190/46M2-30KP-CA57-ARQV.** This is the single closest published thing to the missing experiment: value (lightness) and chroma (saturation) varied jointly — in equal Munsell steps (Exp. 1) and in approximately equal perceptual units (Exp. 2) — with subjects adjusting areas to balance. Both factors affected balance roughly as when varied alone; in Exp. 2 chroma alone carried the effect. Munsell's theory fit better than Moon & Spencer's, but neither captured how value behaves on a gray ground. Two native weight factors, one paradigm, simultaneous manipulation. The ceiling of the literature.
- **Morriss, R. H., & Dunlap, W. P. (1988). "Influence of chroma and hue on spatial balance of color pairs." *Color Research and Application*, 13, 385–388.** Same program, second two-factor combination: chroma × hue.
- **Morriss, R. H., Dunlap, W. P., & Hammond, E. H. (1982). "Influence of chroma on spatial balance of complementary hues." *American Journal of Psychology*, 95, 323–332. DOI 10.2307/1422474.** Single factor (chroma) via the area-adjustment method; tested Munsell's inverse-ratio law directly: within-subject correlations between actual settings and theoretical predictions were predominantly high and positive, especially for subjects with formal color training.
- **Morriss, R. H., & Dunlap, W. P. (1987). "Influence of value on spatial balance of color pairs." *Journal of General Psychology*, 114, 353–361.** The lightness leg: when two colors differed in value, subjects avoided equal areas; on black or white backgrounds they preferred larger areas of the color whose value was nearer the background's; on gray, a narrow band of either light or dark. Neither Munsell nor Moon–Spencer survived this one — value effects are background-contingent.
- **Granger, G. W. (1953). "Area Balance in Color Harmony: An Experimental Study." *Science*, 117, 59–61. DOI 10.1126/science.117.3029.59.** The first empirical shoot-out of the two quantitative balance formulas: subjects adjusted patch areas for most pleasing balance; observed ratios were correlated against the Munsell and Moon–Spencer predictions (inter-subject agreement .672 and .732 — remarkably high objectivity for an aesthetic judgment). The methodological template the whole tradition inherited.
- **Moon, P., & Spencer, D. E. (1944). "Area in Color Harmony." *JOSA*, 34, 93–103. DOI 10.1364/JOSA.34.000093; and "Aesthetic Measure Applied to Color Harmony." *JOSA*, 34, 234 (1944).** The formulas themselves: color weight as a moment arm in Munsell space — chroma as the arm, value-distance from the adaptation point entering too — areas balanced inversely to the weights. The earliest explicit w(pixel group) in the literature, and the reason the missing experiment's paradigm is the method of adjustment, not rating scales.

**2. Conjoint measurement applied to color aesthetics — the method, pointed at the wrong DV.**
- **Pieters, J. M. (1979). "A conjoint measurement approach to color harmony." *Perception & Psychophysics*, 26, 281–286. DOI 10.3758/BF03199881.** Real conjoint measurement in empirical aesthetics — the method the missing experiment would use — but applied to color *harmony*, not visual weight. Proves the psychometric machinery existed by 1979; nobody ever aimed it at balance.
- Conjoint analysis in aesthetics today lives in marketing (packaging studies) and one recent visualization paper ("What Catches the Eye?", arXiv, infographic preferences) — never on visual weight. Negative result, documented.

**3. Factorial designs at the composite-measure level (multivariate, but wrong factors).**
- **Altaboli, A., & Lin, Y. (2011). "Investigating Effects of Screen Layout Elements on Interface and Screen Design Aesthetics." *Advances in Human-Computer Interaction*, 2011. DOI 10.1155/2011/659758.** Controlled factorial experiment on Ngo et al.'s composite measures (balance × unity × sequence), significant effects and interactions on perceived interface aesthetics. Multivariate design, but the factors are whole layout metrics, not native visual-weight factors.
- **Bauerly, M., & Liu, Y. (2006). "Computational modeling and experimental investigation of effects of compositional elements on interface and design aesthetics." *IJHCI*.** Systematically varied symmetry, balance, and element quantity in geometric images and web pages; ratio-scale magnitude estimation against a benchmark. Same level-of-analysis limitation as Altaboli & Lin.

**4. Multivariate ML — many predictors, never the right DV.**
- PLOS ONE 10.1371/journal.pone.0291647 (dynamic generative artwork): regression with horizontal/vertical balance, symmetry, hue-average among six predictors of aesthetic ratings — the closest ML architecture, but DV is liking, not balance.
- Datta, Joshi, Li & Wang (2006, ECCV); Dhar, Ordonez & Berg (2011, CVPR); Ke, Tang & Jing (2006, CVPR): 56-feature SVMs, attribute classifiers, high-level photo-quality features — multivariate models of aesthetic quality, never of balance weight; coefficients are classifier weights, not interpretable visual weights.
- Thesis repositories (NDLTD, EThOS) were not exhaustively searchable from here; the missing experiment, if it exists anywhere unpublished, would most plausibly be a PhD thesis. Flagged as the one remaining unsearched territory.

**5. A killed lead (honesty requires it).** A ResearchGate record attributed a chroma-adjustment balance paper to "Linnett, Morriss, Dunlap & Fritchie." Cross-checking Dunlap's full publication list shows no such paper; the record is a merge artifact tangled with Schloss & Palmer (2011). **Killed — do not cite.**

### What the missing experiment would actually look like (design sketch, for the project)
The Morriss/Dunlap paradigm generalizes directly: method of adjustment with **area as the dependent variable** (the observer adjusts a patch's area — or chroma, or lightness — until two regions look balanced), factors **saturation × hue × lightness × area(base) × position × contrast** in a fractional-factorial or adaptive design, fitted with a mixed-effects model or hierarchical Bayesian model yielding per-factor weight functions w_i(factor). The DV is behavioral (null-point of balance), not a rating — which is why this tradition succeeded where rating-based balance studies (Hübner & Fillinger's paradigm) never produced coefficients. The honest obstacles, per the literature: value effects are background-contingent (Morriss & Dunlap 1987), chroma×area reverses sign when chroma rather than area is the adjusted variable (the Linnett-artifact record, consistent with simultaneous-contrast explanations), and Koenderink's equipollence/max-rule findings ("Color weight photometry," VR 2018 — see bibliography) warn that the combination rule may be a nonlinear max, not a linear sum.

### Net for the project
Round 1's "no study has ever fit native values for all factors simultaneously" is confirmed and now precisely bounded: the literature reached **two factors** (Morriss & Dunlap 1988, twice), with a validated two-factor experimental paradigm ready to scale. The gap between 2 and 6 factors is the project's open frontier — and the method-of-adjustment color-balance tradition, not the rating-scale aesthetics tradition, is where the missing experiment belongs.

---

## Task 2 — Unverified items: resolved or killed

| Item | Verdict | Evidence |
|---|---|---|
| **Ngo, Teo & Byrne (2003) aesthetic measures** | **RESOLVED → Tier 1** | "Modelling interface aesthetics." *Information Sciences*, 152, 25–46. DOI **10.1016/S0020-0255(02)00404-8**. Confirmed via MMU institutional repository record (shdl.mmu.edu.my/2562) and convergent citation in multiple independent sources (ACM DL, arXiv UI-Bench bibliography). The 14-measure model (balance, symmetry, equilibrium, unity, sequence, density, …) is real and heavily cited. |
| **Reinecke et al. (2013) CHI website aesthetics** | **RESOLVED → Tier 1** | "Predicting users' first impressions of website aesthetics with a quantification of perceived visual complexity and colorfulness." Proc. CHI '13, pp. 2049–2058. DOI **10.1145/2470654.2481281**. Full author list: Reinecke, Yeh, Miratrix, Mardiko, Zhao, Liu, Gajos. Key result: colorfulness + visual complexity + demographics explain 48% of variance in appeal ratings after 500 ms; complexity dominates. PDF freely available from the author's Harvard page. |
| **Corwin bioRxiv preprint (10.1101/2020.05.26.104687)** | **Confirmed still unreviewed — stays below Tier 1, but status now verified** | As of Oct 2026: still a preprint, now at **v22** (latest revision ~Dec 2024). No journal publication found after exhaustive search; the bioRxiv page carries no "published in" notice. Also posted on ResearchSquare (Aug 2022, DOI 10.21203/rs.3.rs-1981907/v1). The single quantified claim remains the 1.07 ± ~0.03 upper-half darkness factor for "perfectly balanced" quadrant luminance. Retrievable, citable as preprint — but it cannot stand in for peer-reviewed literature, and the n=45/39 observer counts plus the all-painter subject pool are as thin as Round 1 said. |
| **Fillinger & Hübner 2018 DOI** | **RESOLVED → Tier 1** | Fillinger, M. G., & Hübner, R. "Relations Between Balance, Prototypicality, and Aesthetic Appreciation for Japanese Calligraphy." *Empirical Studies of the Arts*, 38(2), 172–190. DOI **10.1177/0276237418805656**. (Published online 2018; assigned to the 2020 issue — this is why it was hard to find under "2018".) Content, as cited in Hübner & Fillinger 2019: replicated Gershoni & Hochstein's APB failure on Japanese calligraphy, same negative result for DCM, balance ratings unrelated to liking — but prototypicality explained liking, and discounting it restored a DCM–liking link for less prototypical calligraphies. |

Minor flag for the parent: secondary sources disagree on the third author's initial in Morriss, Dunlap & Hammond (1982) — "E. H." (Springer/Academia reference lists) vs "S. E." (Giessen reading list). Title, venue, year, pages, and DOI are consistent everywhere; the initial is the only wobble.

---

## Two-tier bibliography — everything new in Round 2

### Tier 1 — peer-reviewed (all verified by exact-title search)

**The spatial-balance tradition (Task 1's main yield):**
- Moon, P., & Spencer, D. E. (1944). Area in color harmony. *Journal of the Optical Society of America, 34*, 93–103. https://doi.org/10.1364/JOSA.34.000093 — the first explicit w(pixel group): weight as moment arm in Munsell space.
- Moon, P., & Spencer, D. E. (1944). Aesthetic measure applied to color harmony. *JOSA, 34*, 234. https://opg.optica.org/abstract.cfm?uri=josa-34-4-234 — the full aesthetic-measure formula.
- Granger, G. W. (1953). Area balance in color harmony: An experimental study. *Science, 117*, 59–61. https://doi.org/10.1126/science.117.3029.59 — first empirical test of the balance formulas; observed-vs-predicted area ratios, high inter-subject agreement.
- Morriss, R. H., Dunlap, W. P., & Hammond, E. H. (1982). Influence of chroma on spatial balance of complementary hues. *American Journal of Psychology, 95*, 323–332. https://doi.org/10.2307/1422474 — direct test of Munsell's inverse-ratio law via area adjustment.
- Morriss, R. H., & Dunlap, W. P. (1987). Influence of value on spatial balance of color pairs. *Journal of General Psychology, 114*, 353–361 — the lightness leg; background-contingent value effects; neither Munsell nor Moon–Spencer survived.
- Morriss, R. H., & Dunlap, W. P. (1988). Influence of chroma and hue on spatial balance of color pairs. *Color Research and Application, 13*, 385–388 — two-factor (chroma × hue).
- Morriss, R. H., & Dunlap, W. P. (1988). Joint effects of chroma and value on spatial balance of color pairs. *Empirical Studies of the Arts, 6*(2), 117–126. https://doi.org/10.2190/46M2-30KP-CA57-ARQV — two-factor (chroma × value); the ceiling of the literature.

**Conjoint/multivariate precedents:**
- Pieters, J. M. (1979). A conjoint measurement approach to color harmony. *Perception & Psychophysics, 26*, 281–286. https://doi.org/10.3758/BF03199881 — conjoint measurement in aesthetics (DV: harmony).
- Schloss, K. B., & Palmer, S. E. (2011). The role of spatial organization in preference for color pairs. *Perception, 40*(9), 1063–1080. https://doi.org/10.1068/p6992 — logistic-regression fits of preference with yellowness/blueness and lightness/darkness predictors; area as spatial factor (DV: preference).
- Altaboli, A., & Lin, Y. (2011). Investigating effects of screen layout elements on interface and screen design aesthetics. *Advances in Human-Computer Interaction*, 2011. https://doi.org/10.1155/2011/659758 — factorial (balance × unity × sequence) on interface aesthetics.
- Bauerly, M., & Liu, Y. (2006). Computational modeling and experimental investigation of effects of compositional elements on interface and design aesthetics. *International Journal of Human-Computer Interaction* — factorial (symmetry × balance × element quantity), ratio-scale magnitude estimation.
- Koenderink, J., van Doorn, A., & Gegenfurtner, K. (2018). Color weight photometry. *Vision Research, 151*, 88–98. https://doi.org/10.1016/j.visres.2017.06.006 — "color weight" fitted across paradigms; equipollence and a nonlinear max-rule beat the linear CIE functional in mid/high-level tasks. Directly relevant to the combination-rule question.

**Task 2 resolutions:**
- Ngo, D. C. L., Teo, L. S., & Byrne, J. G. (2003). Modelling interface aesthetics. *Information Sciences, 152*, 25–46. https://doi.org/10.1016/S0020-0255(02)00404-8
- Reinecke, K., Yeh, T., Miratrix, L., Mardiko, R., Zhao, Y., Liu, J., & Gajos, K. Z. (2013). Predicting users' first impressions of website aesthetics with a quantification of perceived visual complexity and colorfulness. Proc. CHI '13, 2049–2058. https://doi.org/10.1145/2470654.2481281
- Fillinger, M. G., & Hübner, R. (2018). Relations between balance, prototypicality, and aesthetic appreciation for Japanese calligraphy. *Empirical Studies of the Arts, 38*(2), 172–190. https://doi.org/10.1177/0276237418805656

### Tier 2 — informed non-academic (clearly marked; never standing in for papers)
- Corwin, D. (2020–2024). Pictorial balance… (bioRxiv preprint, v22). https://doi.org/10.1101/2020.05.26.104687 — retrievable, unreviewed; the 1.07 upper-darkness factor.
- ResearchSquare posting of the same work (Aug 2022). https://doi.org/10.21203/rs.3.rs-1981907/v1
- beautif
...[truncated 144 chars]