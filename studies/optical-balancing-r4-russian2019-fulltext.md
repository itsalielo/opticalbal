# Optical Balancing — Round 4 addendum: Russian 2019 full text retrieved

**Date:** 2026-10-09
**Method:** live browser retrieval via Wayback Machine (izdat.istu.ru DNS-dead; eLibrary.ru IP-blocked). Both ISM papers CC-BY 4.0.
**Working copies:**
- 2019: https://web.archive.org/web/20220317231034id_/http://izdat.istu.ru/index.php/ISM/article/viewFile/4317/2772
- 2017: https://web.archive.org/web/20220319011420id_/http://izdat.istu.ru/index.php/ISM/article/viewFile/3884/2434
- IEET-2019 (English): https://web.archive.org/web/20240705095408id_/http://ieet.istu.ru/proceedings/IEET-2019/IEET-2019-04.pdf

## Title correction

The 2019 paper is NOT "Mathematical model of visual weight". Exact: Al Akkad M. A., Gazimzyanov F. F., "AUTOMATED SYSTEM FOR EVALUATING 2D-IMAGE COMPOSITIONAL CHARACTERISTICS: CONFIGURING THE MATHEMATICAL MODEL", ISM 17(1), 26–33, DOI 10.22213/2410-9304-2019-1-26-33. It is the THIRD paper of a cycle. The additive vW model lives in the SECOND: "...: математическая модель", ISM 15(2) (2017), 105–108, DOI 10.22213/2410-9304-2017-2-105-108.

## Exact model specification (2017, formulas 1–3)

- vW_oS^attract = 1 / (pF · k_pF), where pF = perceptual force, k_pF = influence coefficient of the force factor.
- pF = f(oCD), oCD = distance from the object's center of mass to a given element of the structural plan (Arnheim's structural skeleton). pF is interpolated by Akima spline from experimental control points.
- vW = vWsS + vWc + vWs: vWsS = visual weight from the structural plan (position term); vWc = from color; vWs = from size. Each source of the structural plan carries its own influence coefficient. **vWc and vWs are named with the same treatment promised but never specified — confirming Round 3's position-only verdict.**

## 2019 genetic-algorithm fitting (formulas 1–8)

- Drops the 2017 division (avoids inverse proportionality vs human ratings); uses pF directly in a piecewise evaluation combining segment sources (pF_segs) and dot sources (pF_dots), with error threshold e below which dot-source influence is null.
- gene = Akima control-point values x; chromosome/genotype/phenotype standard; fitness = Σ |pF_scene^gene − hE_scene| (absolute deviation from human scene ratings). Implemented in Java with the Jenetics library.

## THE COEFFICIENT MYSTERY — SOLVED

**The 2019 paper publishes NO numeric coefficient table.** The fitted "coefficients" are the genes = Akima spline control-point values; their numbers are never printed — results appear only as pF maps (figures 4–7: all-ratings mode, negative/neutral/positive trend modes). The 2017 paper introduces k_pF as fittable parameters with no numeric values. No population size or generation count reported. **The coefficients were never published — there is nothing more to retrieve.**

## Procedure (2019)

- **76 compositions CONFIRMED** ("Всего в бланках было представлено 76 композиций"), printed on A4 (identical perception; screens vary in size); simple "metric" objects as in Arnheim's *Art and Visual Perception* ch. 1.
- Human ratings: paper questionnaires, 1 (irritating) to 5 (pleasant to look at); sex, age, artistic skills recorded; data in Google Sheets. Means judged uninformative (very large SD); analysis via response spectrum and MODES.
- Second GA use: clustering respondents by trend — negative-trend group (mostly teenage girl artists), positive-trend group (no clear pattern), middle-aged men without artistic skills = reserved average scores. Respondent count not given ("small number of surveys" noted).

## Validation

Qualitative only — no numeric correlation, error, or comparison reported. pF maps agree with Arnheim's experiments: most stable zones = right part of the square and lower structural-plan sources; lower-right corner most stable; right/down preponderance around the vertical symmetry line; admissible visual center shifted down-right. Presented as confirmation the math correctly implements Arnheim's method. Modes beat means; future multivariate analysis suggested for "taste" identification and system personalization.

## IEET-2019 (English conference version)

Gazimzyanov & Al Akkad, "Solving the problem of automated 2D images compositional characteristics evaluation", IEET-2019, 33–39, DOI 10.22213/2658-3658-2019-33-39. Same formulas, same 76 compositions, same respondent groups, same pF maps. Own contributions: expanded literature review (aesthetic image-quality evaluation: neural nets, GAs), funding note (Kalashnikov Izhevsk State Technical University grant 27.06.01/18ВСВ), explicit conclusion (GA suits coefficient fitting and data sorting; modes beat means; system ready for deeper analysis). No additional numeric coefficients.

## Net effect

- The Russian line is now FULLY read (2017 + 2019 + IEET-2019). Nothing further to retrieve on it.
- The "additive formula" verdict stands corrected and deepened: the additive *structure* exists (vW = vWsS + vWc + vWs) but only the position term is specified; the fitted parameters were never published as numbers.
- Methodological gift: the mode-over-mean finding and the second-GA respondent-clustering are directly reusable in our experiment protocol's analysis plan.
