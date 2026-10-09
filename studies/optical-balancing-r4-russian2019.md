# Round 4 — Russian 2019 retrieval: Al Akkad & Gazimzyanov, "Automated system for evaluating 2D-image compositional characteristics: configuring the mathematical model"

**Date:** 2026-10-09
**Worker:** Round 4 retrieval subagent
**Target paper:** Аль Аккад М. Айман, Газимзянов Ф. Ф. «Автоматизированная система оценки композиционных характеристик 2D-изображения: настройка математической модели» // Интеллектуальные системы в производстве. 2019. Т. 17, № 1. С. 26–33. DOI: 10.22213/2410-9304-2019-1-26-33

## 1. Bottom line

**Coefficients retrieved: NO.** The PDF body is unobtainable from this environment. The exact reason is documented in §2. Everything below is what *was* verifiably recovered: full bibliographic record, the complete abstract (article is CC-BY 4.0), the full 9-item reference list (mined from the PDF by OpenAIRE), the single citing paper, and precise handoff instructions so a live-browser session can fetch the file in one step.

## 2. Retrieval log (what was tried, what worked/failed)

| # | Attempt | Result |
|---|---------|--------|
| 1 | DOI resolution via `https://doi.org/10.22213/2410-9304-2019-1-26-33` | **Failed** — fetch service returned HTTP 500, empty body, 3 attempts |
| 2 | OJS article landing page `http://izdat.istu.ru/index.php/ISM/article/view/4317` | **Failed** — `izdat.istu.ru` does not resolve in the fetch worker ("requires a resolvable public HTTP(S) URL"). Same for the `https://` variant and the `/issue/archive` page |
| 3 | Direct PDF `http://izdat.istu.ru/index.php/ISM/article/download/4317/2772` (URL confirmed verbatim by Crossref deposit, OpenAlex, Semantic Scholar, OpenAIRE/Unpaywall) | **Failed** — same DNS-resolution failure. Sibling article `…/download/4323/2778` from the same issue *is* indexed by search engines, so the OJS platform is live; the failure is local to this worker's network path |
| 4 | Crossref API (`api.crossref.org/works/…`) | **Worked** — full metadata, PDF link, license CC-BY 4.0, abstract |
| 5 | OpenAlex API | **Worked** — metadata, OA status "diamond", pdf_url identical, `cited_by_count: 0`, author ORCID for Al Akkad (0000-0002-0558-8726) |
| 6 | Semantic Scholar API | **Worked** — `citationCount: 1`, openAccessPdf = same OJS URL, status GOLD, license CCBY |
| 7 | OpenAIRE API | **Worked** — full abstract, subject classification, and the **complete 9-item reference list** (mined from the actual PDF by OpenAIRE's IIS pipeline — proof the PDF exists and was machine-readable) |
| 8 | Wayback availability API for PDF URL and article URL (http and https) | **Worked, negative** — `archived_snapshots: {}` — no capture exists |
| 9 | Wayback CDX / timemap APIs | **Failed** — fetch service 500s |
| 10 | Fatcat (`api.fatcat.wiki`) release lookup | **Failed** — fetch service 500 |
| 11 | Search-engine full-text probing (exact-title, distinctive abstract phrases, "Jenetics", "переиспользованием кода", download IDs `4317/2772`) | **Negative** — the *2017* paper's full text is indexed (`…/download/3884/2434`), the *2019* paper's body text is not indexed anywhere |
| 12 | CyberLeninka (`site:cyberleninka.ru`) | **Negative** — not present |
| 13 | eLibrary.ru / RSCI via search | **Negative** — no entry surfaced |
| 14 | ResearchGate author/publication search | **Negative** — no upload found |
| 15 | ORCID record of Al Akkad | **Worked, negative for this work** — lists only Scopus-indexed items; no link to the 2019 paper |
| 16 | Gazimzyanov master's thesis hunt (dissercat, IzhGTU, general search) | **Negative** — nothing found |
| 17 | Follow-up conference paper IEET-2019 (the one citation) via `ieet.istu.ru/papers.php/?p=22` | **Failed** — same `*.istu.ru` DNS failure as #2 |

**Exact reason the PDF is unobtainable here:** the publisher host `*.istu.ru` (both `izdat.istu.ru` and `ieet.istu.ru`) does not resolve from this worker's fetch network, while the DOI resolver and archive APIs also fail from here. The file itself verifiably exists (Crossref deposited the PDF link on 2019-04-11; OpenAIRE mined its references from the PDF). **A live browser on a normal network should fetch it in one step** — see §8 handoff.

## 3. Verified bibliographic record

- **Authors:** M. A. Al Akkad (IzhGTU / Kalashnikov Izhevsk State Technical University; ORCID 0000-0002-0558-8726), F. F. Gazimzyanov (same affiliation; in 2017 listed as master's student / магистрант)
- **Journal:** Интеллектуальные системы в производстве (Intellekt. Sist. Proizv.), ISSN 1813-7911 (print) / 2410-9304 (electronic)
- **Issue:** Vol. 17, No. 1 (2019), pp. 26–33; published online 2019-04-11
- **DOI:** 10.22213/2410-9304-2019-1-26-33
- **Publisher:** Kalashnikov Izhevsk State Technical University
- **License:** CC-BY 4.0 (diamond/gold OA; confirmed by Crossref, OpenAlex, Semantic Scholar, OpenAIRE)
- **Language:** Russian
- **Canonical PDF:** `http://izdat.istu.ru/index.php/ISM/article/download/4317/2772` (OJS article ID 4317, file ID 2772)
- **Article landing page:** `http://izdat.istu.ru/index.php/ISM/article/view/4317`

## 4. Full abstract (CC-BY 4.0 — from Crossref/OpenAIRE record)

> Статья посвящена разработке автоматизированной системы оценки композиционных характеристик 2D-изображения. Представлен специальный генетический алгоритм, разработанный для настройки математической модели, описанной в предыдущей статье авторов «Автоматизированная система оценки композиционных характеристик 2D-изображения: математическая модель». Вся система основывается на исследованиях Р. Арнхейма, описании общей концепции посвящена первая статья цикла «Автоматизированная система оценки композиционных характеристик 2D-изображения: концепция». Проводится обзор методов, потенциально пригодных для решения поставленной задачи, обосновывается выбранный метод, приводится адаптация выбранного метода к особенностям конкретной задачи. Приведена математическая модель, адаптированная для работы с существующей математической моделью при помощи нового метода. Описывается структура обучающей выборки, особенности сбора данных. Анализ данных и сортировка производится при помощи разработанного генетического алгоритма с переиспользованием кода, выбор метода обосновывается. Анализируются полученные результаты, представлена визуализация композиционных параметров простых сцен, для разных групп опрашиваемых, выявленных при сортировке и анализе данных. Демонстрируется схожесть с результатами, полученными и продемонстрированными Р. Арнхеймом в своей книге без использования информационных и автоматизированных методов. Представляются результаты исследования.

**What the abstract structurally tells us (no body needed):**
- GA setup: a *special-purpose* genetic algorithm built for this fitting task, implemented **with code reuse** ("с переиспользованием кода") — consistent with the mission brief's Jenetics note, i.e. they reused an existing GA library's code rather than writing operators from scratch; the paper reviews candidate methods, justifies the choice, and adapts it to the task. No population size / operators / fitness function in the abstract — those are body-only.
- Model: the paper presents the 2017 model **adapted** for fitting ("математическая модель, адаптированная для работы с существующей математической моделью при помощи нового метода").
- Stimulus set / raters: a **training sample** ("обучающая выборка") whose structure and data-collection specifics are described; data came from **surveying respondents** ("анкетирование" per the 2017 paper's conclusion; here "групп опрашиваемых" — respondent groups discovered via sorting/analysis of the data, i.e. respondents were clustered into groups); results are **visualizations of compositional parameters of simple scenes**, per respondent group; claimed agreement with Arnheim's published results.
- **The "76 compositions" figure from the mission brief is NOT verified** — it appears nowhere in the abstract or any metadata I could reach. Treat as unconfirmed until the PDF body is read.

## 5. Coefficient tables — exact status

**Not retrieved.** No coefficient values (kpF or per-factor weights), no fitted numbers of any kind appear in any reachable source: not in the abstract, not in metadata, not in the reference list, not in the citing paper's metadata, and the body text is not indexed by any search engine. The fitted numbers exist only inside the PDF.

## 6. Reference list of the 2019 paper (9 items, via OpenAIRE full-text mining)

1. Аль Аккад М. Айман, Газимзянов Ф. Ф. Автоматизированная система оценки композиционных характеристик 2D-изображения: концепция // Вестник ИжГТУ имени М. Т. Калашникова. 2017. Т. 20, № 2. С. 160–162. DOI: 10.22213/2413-1172-2017-2-160-162.
2. Аль Аккад М. Айман, Газимзянов Ф. Ф. Автоматизированная система оценки композиционных характеристик 2D-изображения: математическая модель // Интеллектуальные системы в производстве. 2017. Т. 15, № 2. С. 105–108. DOI: 10.22213/2410-9304-2017-2-105-108.
3. Арнхейм Р. Искусство и визуальное восприятие. Благовещенск: БГК им. И. А. Бодуэна де Куртене, 2000. 392 с.
4. Линник Ю. В. Метод наименьших квадратов и основы математико-статистической теории обработки наблюдений. 2-е изд., испр. и доп. М.: Физматгиз, 1962. 349 с.
5. Акулич И. Л. Математическое программирование в примерах и задачах. М.: Высш. шк., 1986. С. 298–311.
6. Коробейников А. В. Программирование нейронных сетей. Ижевск: Ижевский государственный технический университет, 2012. 14 с.
7. Li C. and Chen T. Aesthetic Visual Quality Assessment of Paintings. IEEE … (truncated in mining output)
8–9. (mining output truncated; at least 9 references total per OpenAIRE)

Note: refs 4–5 (least squares, mathematical programming) are the optimization-methods survey the abstract mentions.

## 7. Citation sweep — third-party citations of the 2017/2019 papers

- **2019 paper:** Semantic Scholar `citationCount = 1`; OpenAlex `cited_by_count = 0`. The single citing item is **the authors' own follow-up conference paper** (self-citation, not third-party):
  - Gazimzyanov F. F., Al Akkad M. A. "Solving the problem of automated 2D images compositional characteristics evaluation." Proc. V Int. Forum "Instrumentation Engineering, Electronics and Telecommunications — 2019" (IEET-2019), pp. 33–39. DOI: **10.22213/2658-3658-2019-33-39**. Published online 2019-12-03. Landing page `http://ieet.istu.ru/papers.php/?p=22` (unreachable from here — same `*.istu.ru` issue). This paper likely restates the fitted model — **highest-value second target** for a live-browser fetch.
- **2017 papers:** no citation data surfaced in any reachable index for DOI 10.22213/2410-9304-2017-2-105-108 or 10.22213/2413-1172-2017-2-160-162.
- **Verdict: zero independent third-party citations found anywhere.** The work has had no measurable uptake outside its own authors.

## 8. Handoff for a live-browser session (parent agent)

The PDF is one fetch away on a normal network. In order:
1. `http://izdat.istu.ru/index.php/ISM/article/download/4317/2772` — direct OA PDF (CC-BY 4.0). If that fails, the article page `http://izdat.istu.ru/index.php/ISM/article/view/4317` (check "supplementary files" tab — OJS pages list them there).
2. If the host is down entirely: Wayback has no snapshot, so try the IEET-2019 follow-up at `http://ieet.istu.ru/papers.php/?p=22` (same host risk) or its proceedings volume.
3. eLibrary.ru item search for the title as fallback (RSCI usually carries the PDF behind login).

Things to extract once the PDF is in hand (in priority order): the fitted/adapted model formulas and notation; the coefficient table (kpF / per-factor weights); GA config (population, operators, fitness, Jenetics usage); training-sample structure and respondent-group counts; whether the 76-composition figure is real; any supplementary dataset/code attachments.

## 9. Context note — 2017 model notation (from the search-indexed 2017 full text)

For orientation when the 2019 PDF is read: the 2017 paper defines a scene object as `O = {vW, vD, oC}` (visual weight, visual direction, center-of-mass coordinates) and the additive decomposition `vW = vW_sS + vW_c + vW_S`, where `vW_sS` = weight from the structural plan, `vW_c` = from color, `vW_S` = from size. The 2017 paper's conclusion states the polynomial-with-coefficients form can be tuned by least squares and that tuning requires surveying ("проведя анкетирование") — which is exactly what the 2019 paper does with the GA. Round 3's correction stands: in 2017 only the structural-plan (position) term was specified; the 2019 paper is where color/size terms were meant to be fitted.

## 10. Full citation list

- Аль Аккад М. А., Газимзянов Ф. Ф. (2019). Автоматизированная система оценки композиционных характеристик 2D-изображения: настройка математической модели. *Интеллектуальные системы в производстве*, 17(1), 26–33. https://doi.org/10.22213/2410-9304-2019-1-26-33 — **target paper, body unobtainable from here; canonical PDF** `http://izdat.istu.ru/index.php/ISM/article/download/4317/2772`
- Аль Аккад М. А., Газимзянов Ф. Ф. (2017). Автоматизированная система оценки композиционных характеристик 2D-изображения: математическая модель. *Интеллектуальные системы в производстве*, 15(2), 105–108. https://doi.org/10.22213/2410-9304-2017-2-105-108 — full text indexed at `https://izdat.istu.ru/index.php/ISM/article/download/3884/2434`
- Аль Аккад М. А., Газимзянов Ф. Ф. (2017). Автоматизированная система оценки композиционных характеристик 2D-изображения: концепция. *Вестник ИжГТУ имени М. Т. Калашникова*, 20(2), 160–162. https://doi.org/10.22213/2413-1172-2017-2-160-162
- Gazimzyanov F. F., Al Akkad M. A. (2019). Solving the problem of automated 2D images compositional characteristics evaluation. *Proc. V Int. Forum "Instrumentation Engineering, Electronics and Telecommunications — 2019" (IEET-2019)*, 33–39. https://doi.org/10.22213/2658-3658-2019-33-39 — sole citing paper (self-citation); body unreachable from here
- Metadata sources: Crossref, OpenAlex (W2939115957), Semantic Scholar (CorpusId 189426640), OpenAIRE (doi_dedup___::6ca364c31213185892c74afab3ee7c6b)
