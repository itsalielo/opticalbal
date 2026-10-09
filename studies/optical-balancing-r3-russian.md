# Round 3 — Russian follow-up hunt: Al Akkad & Gazimzyanov 2019, Seredkina et al., citation sweep

**Date:** 2026-10-09. **Method:** Russian-language exact-title/DOI queries via web search (CyberLeninka-indexed sources, elibrary signals, Google Scholar-style queries, the journal's own OJS platform izdat.istu.ru), plus full-text read of the 2017 model paper via its open-access PDF. This agent (subagent, no live browser) could fetch pages only through search-result references; literal-URL page fetches failed in this environment. Every paper below was verified by exact-title search and/or resolving DOI.

---

## 1. The 2019 follow-up — full citation and access status

**Аль Аккад, М. А., & Газимзянов, Ф. Ф. (2019). Автоматизированная система оценки композиционных характеристик 2D-изображения: настройка математической модели.** *Интеллектуальные системы в производстве, 17*(1), 26–33. https://doi.org/10.22213/2410-9304-2019-1-26-33 — Russian, peer-reviewed (regional Russian journal, ISSN 1813-7911 / e-ISSN 2410-9304).

**Existence verified.** Exact-title and exact-DOI searches confirm the record; the journal's OJS platform (izdat.istu.ru) carries it in issue 17(1), 2019. The issue's other articles are openly downloadable there (download IDs cluster ~4320–4333 for that issue), and Round 2 read this paper's full text (8 pp.).

### What Round 2 recovered from the full text (2019)
- The 2017 model was fitted with a specially built genetic algorithm; analysis was done in **Google Sheets + the Jenetics library**.
- Survey: respondents rated **76 simple geometric compositions** (objects inside a square) on a 1–5 scale.
- Means are uninformative (very large standard deviations, bimodal 2-vs-5 splits); **modes** capture the tendencies.
- Visualized pF maps agree with Arnheim: right side and bottom more "stable"; lower-right corner most stable; the pF tolerance zone of the visual center is shifted to lower-right.
- Rater subgroups emerged (teenage girl artists tended negative; middle-aged men without art training tended moderate).
- Conclusion: the model correctly implements Arnheim, but averaging across observers destroys the structure — taste groups would need separate tuning.

### ⚠️ The coefficient values — NOT obtainable, reason documented
The **actual numeric coefficient values (the fitted kpF per structural-plan source, or any per-factor weights) could not be retrieved**. Precise reason — **not a paywall**: the journal is open access and the PDF is freely downloadable from the journal's OJS platform. The barrier is twofold:

1. This subagent has no live-browser access; literal-URL fetches failed in this environment, and the search index does not carry the 2019 paper's body text (its PDF is not surfaced by exact-title/DOI/content queries — only the 2017 papers and other 17(1) articles are indexed).
2. Round 2's full-text read (8 pp.) recorded **no numeric coefficient table** — only the fitting procedure and its conclusions. That is consistent with how the 2017 paper frames the coefficients (see §3): they are per-source multipliers of hand-drawn/Akima-interpolated pF curves, so the "fitted values" may exist only as curve parameters inside the authors' Jenetics run, not as a published table.

**Exact access path for retrieval (recommended: live-browser delegation):** journal platform izdat.istu.ru → journal ISM (*Интеллектуальные системы в производстве*) → issue 17(1), 2019 → article pp. 26–33; or resolve the DOI (10.22213/2410-9304-2019-1-26-33). The article download endpoint follows the OJS pattern `index.php/ISM/article/download/<id>/<file>` (sibling articles in the issue use IDs 4320–4333). A live-browser pass should also check the article's OJS page for supplementary files (the Jenetics code or the 76-composition dataset may be attached, which would yield the coefficients directly).

### What the 76 compositions were — partially known
Round 2: 76 simple geometric compositions — arrangements of simple geometric objects (the model paper's running example is a dark disk inside the structural-plan square) rated 1–5 by questionnaire respondents. The exact stimulus set (images) was not recovered; it would be in the paper's figures or an appendix.

---

## 2. Full model specification (from the 2017 papers — full text read this round)

Both 2017 papers were re-verified and the model paper read in full via its open-access PDF (https://izdat.istu.ru/index.php/ISM/article/download/3884/2434). This is the exhaustive specification, notation as in the paper:

- **Concept paper:** Аль Аккад & Газимзянов (2017). *Вестник ИжГТУ имени М. Т. Калашникова, 20*(2), 160–162. https://doi.org/10.22213/2413-1172-2017-2-160-162 — proposes the program, reviews Li & Chen 2009 as the one existing computer-aesthetics work, reports pilot experiments.
- **Model paper:** Аль Аккад & Газимзянов (2017). *Интеллектуальные системы в производстве, 15*(2), 105–108. https://doi.org/10.22213/2410-9304-2017-2-105-108 — the formula.

**Definitions.** Scene object: O = {vW, vD, oC} — visual weight, visual direction, center-of-mass coordinates. Scene balance is a function f(O₁, O₂, …, Oₙ); the closer its value to zero, the better balanced the scene.

**Formula (1) — weight from one structural-plan source:** vWsSsource = 1 / (pF · kpF), where pF is the perceptual force of that source and kpF the influence coefficient of the force factor.

**Formula (2) — perceptual force:** pF = f(oCD), a function of the distance from the object's center of mass to the structural-plan element. The curve shape comes from Akima-spline interpolation of hand-drawn reference graphs (chosen to avoid oscillations at extrema and abrupt value changes). Distinct curve families for edges vs. internal structural lines: internal lines show **no** pF drop near oCD = 0, because the viewer cannot apply the "standing on a surface" perceptual experience to invisible lines; the edge curve has its maximum at oCD = oRad (the disk "standing" on the edge — perceived as the stable position).

**The additive decomposition:** vW = vWsS + vWc + vWs — structural-plan component + color component + size component (paper also says "цвета и яркости" — color and brightness). And: vWsS = Σ over sources vWsSsourceN — each structural-plan source has its own influence coefficient on the overall estimate.

**Calibration doctrine (the paper's own words, paraphrased):** the coefficients (kpF and per-factor weights) are *not derivable from Arnheim* — "it is impossible, based only on Arnheim's book and personal experience, to tune such a complex system consisting of a huge number of different parameters." They must be fitted to human data; "the influence of different factors with coefficients, written as a polynomial, can be tuned by least squares." Planned method: questionnaires (анкетирование) — respondents rate compositions of objects inside a square on a 1–5 scale.

**Critical nuance for the project:** vWc (color) and vWs (size) are **never actually specified** — the paper only says the same approach could compute color/size influence ("Точно так же можно вычислить влияние цвета или размера объекта на его визуальный вес"). So the 2017 "exact formula" is really: **vW(position) = Σᵢ 1/(pFᵢ(oCDᵢ)·kpFᵢ)** over structural-plan sources, with **+ vWc + vWs left as aspirations**. No saturation/hue/lightness split, no contrast term anywhere in the three papers.

---

## 3. Seredkina et al. — venue status

**Середкина, Н. Н., Ермаков, Т. К., & Гомонов, И. С. (2026). The Compositional Formula as a Concept of the Theory of Visual Thinking (R. Arnheim and V. I. Zhukovsky).** SibFU Digital Repository: https://elib.sfu-kras.ru/handle/2311/160105

**Venue: still unconfirmed.** The repository page was unreachable from this environment (same limitation Round 2 hit); general web search finds no journal record for this title. The authors are Siberian Federal University humanities scholars whose usual outlet is the *Journal of Siberian Federal University. Humanities & Social Sciences* (e.g., Seredkina & Ermakov 2026, 19(2): 248–258, on a different topic — confirmed indexed), but the compositional-formula paper is **not** confirmed there. Cite via the repository handle.

**Content note:** it is a *theoretical* paper — whether a "compositional formula" is thinkable, linking Arnheim's perceptual force-lines with V. I. Zhukovsky's "compositional formula" (композиционная формула: the carrier of a work's general rational meaning, dissolved in the picture surface). **There is no mathematical formula to retrieve** and no experiment. Relevance to the project: philosophical framing only, not a candidate model.

---

## 4. Citation search — anyone citing or extending the 2017/2019 model?

**No third-party citing or extending work found.** Sweeps run: Russian queries for citing authors ("Аль Аккад" "Газимзянов" + цитирует/ссылка), the model vocabulary ("визуальный вес" "Газимзянов"), Gazimzyanov's master's thesis (the likely source document behind the 2019 paper — not located in open repositories), ResearchGate/Semantic Scholar author profiles, CyberLeninka article records. Result: the only known citations are **self-citations within the chain** (2019 cites the two 2017 papers; the concept paper precedes the model paper). The work appears entirely uncited by others in open indexes — consistent with a regional journal, a 2019 date, and a niche (computational aesthetics) that the mainstream balance literature never picked up.

---

## 5. What remains unobtainable and why (honest accounting)

| Item | Status | Why unobtainable / path |
|---|---|---|
| 2019: fitted numeric kpF values | ❌ Not retrieved | Not a paywall — OA journal. This agent lacks live-browser page fetching; the search index doesn't carry the 2019 body text; R2's full-text read recorded no coefficient table. **Live-browser retrieval of the OJS article page + PDF is the fix** (see §1 access path). |
| 2019: GA setup details (population, operators, fitness function, Jenetics config) | ⚠️ Partial (from R2): Jenetics + Google Sheets, modes not means | Full parameters need the paper's methods section — same live-browser retrieval. |
| 2019: the 76 compositions (stimulus set) | ⚠️ Partial: 76 simple geometric compositions, 1–5 ratings | Exact stimuli are figures/appendix in the PDF — same retrieval. |
| Seredkina et al. venue | ❌ Unconfirmed | Repository page unreachable from here; no journal record indexed. Needs live browser on the elib.sfu-kras.ru handle. |
| Seredkina et al. formula | ➖ N/A | No formula exists — theoretical paper. Nothing to retrieve. |
| Third-party extensions of the model | ❌ None found | Appears genuinely uncited outside the author chain (open indexes). |
| Gazimzyanov's master's thesis | ❌ Not located | Not in open repositories found via search; may exist only in the IzhGTU internal archive. |

## 6. Single most important retrieval of this round

**The 2017 model paper's full text** (open-access PDF, read end-to-end), because it corrects and hardens the project's crown find in two ways: (1) it gives the *exact* published specification — vWsSsource = 1/(pF·kpF), pF = f(oCD) via Akima-spline interpolation of hand-drawn curves, per-source influence coefficients, balance as f(O₁…Oₙ)→0 — which the computational track can now implement directly (~/workspace/opticalbal-compute/); (2) it exposes the model's real boundary: **color and size were never specified, only named** — vWc and vWs are placeholders, so the "only additive factor-decomposition in any language" is, strictly, a *position-only* formula with an additive *promise*. That is precisely where the project's six-factor program must begin: the Russian model never got past position.

## Full citation list (this round)

1. Аль Аккад, М. А., & Газимзянов, Ф. Ф. (2017). Автоматизированная система оценки композиционных характеристик 2D-изображения: концепция. *Вестник ИжГТУ имени М. Т. Калашникова, 20*(2), 160–162. https://doi.org/10.22213/2413-1172-2017-2-160-162
2. Аль Аккад, М. А., & Газимзянов, Ф. Ф. (2017). Автоматизированная система оценки композиционных характеристик 2D-изображения: математическая модель. *Интеллектуальные системы в производстве, 15*(2), 105–108. https://doi.org/10.22213/2410-9304-2017-2-105-108 — full text read (PDF: https://izdat.istu.ru/index.php/ISM/article/download/3884/2434)
3. Аль Аккад, М. А., & Газимзянов, Ф. Ф. (2019). Автоматизированная система оценки композиционных характеристик 2D-изображения: настройка математической модели. *Интеллектуальные системы в производстве, 17*(1), 26–33. https://doi.org/10.22213/2410-9304-2019-1-26-33 — exists, OA; full text not re-retrieved this round (see §1)
4. Середкина, Н. Н., Ермаков, Т. К., & Гомонов, И. С. (2026). The Compositional Formula as a Concept of the Theory of Visual Thinking (R. Arnheim and V. I. Zhukovsky). SibFU Digital Repository. https://elib.sfu-kras.ru/handle/2311/160105 — venue unconfirmed; theoretical, no formula
