# Optical Balancing — Round 4: Japanese Thesis & Experimental Territory

**Date:** 2026-10-09
**Worker:** Round 4 subagent
**Mission context:** Ali's hypothesis of an exact formula w(saturation, hue, lightness, area, position, contrast) for visual weight. Rounds 1–3 mapped ~200 papers; Round 3 dead-ended on CiNii Dissertations (text client returned empty). Known Japanese items already logged (not re-reported here): Fukada 1983/84/85 (Doshisha bulletin, print-only — skipped per brief), Peng/Inoue/Hara 2020, Sato/Urakawa 2003.

## Method

Text searches only (browser.search + browser.open of J-STAGE pages). Japanese keywords: 視覚的均衡, 画面構成, 色彩重量, 視覚重量, 構図 バランス, 色の重さ, 色彩の重量感, 視覚的重量感, 色彩の空間的構造. Routes attempted: J-STAGE article pages (English + Japanese char versions), KAKEN grant records, CORE/ IR thesis records, exact-title verification searches. Every item below was verified against a retrievable record (J-STAGE page, KAKEN record, CORE record, or publisher metadata). Paraphrase-only summaries; no quoted text over 50 words from any single work.

## Tier 1 — Peer-reviewed papers

### 1. Hayashi, Mikio (1969) — the crown find of this round
- **Citation:** 林 美樹雄 (Hayashi, Mikio). 「画面の力動的均衝に関する一研究: 美的観照に関する研究-第II報告」[A study of dynamic balance of pictures: Studies on aesthetic observation, Report II]. *教育心理学研究 (Japanese Journal of Educational Psychology)*, 3(1), 11–17.
- **DOI / link:** https://doi.org/10.5926/jjep1953.3.1_11 — https://www.jstage.jst.go.jp/article/jjep1953/3/1/3_11/_article/-char/ja (journal-free; PDF downloadable, 1,267K)
- **Why it matters:** This is a direct experimental study of *dynamic* pictorial balance from Japanese experimental psychology, and it appears nowhere in Rounds 1–3. With 587 participants (adults and middle-schoolers) and 18 figures shown in three compositions each (center, left/right deviation, up/down deviation), it produced hard numbers: the geometrically balanced center composition was preferred about 50% of the time (~80% when the figure itself was symmetric); figures carrying directional tension were preferred in compositions deviated *against* their tension direction; downward deviation beat upward deviation 29:19; sex differences were significant; correlation with an intelligence test was r = .318. The paper explicitly frames composition as a problem of element *weight and directionality* and closes by proposing continuous-deviation methods to locate a picture's equilibrium point — essentially the six-factor program's position/direction arm, 55 years early.

### 2. Sunaga, Park & Spence (2016) — lightness → visual heaviness, position interaction
- **Citation:** Sunaga, T., Park, J., & Spence, C. (2016). Effects of lightness–location congruency on consumers' purchase decision-making. *Psychology & Marketing*, 33(11), 934–950.
- **DOI / link:** https://doi.org/10.1002/mar.20929
- **Why it matters:** Japanese-led experiment (Tsutomu Sunaga first author) establishing that darker packaging colors are perceived as visually heavier, and that light colors "belong" in upper shelf positions while dark colors "belong" lower — a lightness × vertical-position interaction on perceived weight, with purchase-choice consequences. This is the only modern Japanese-authored experiment that jointly manipulates two of Ali's six factors (lightness and position) against perceived weight, and it was cited as the foundation for the 2022 Japanese follow-up below. It confirms the weight–position axis independently of the Russian tradition.

### 3. Unnamed Japanese author team (2022, J-STAGE) — price–lightness congruency experiment
- **Citation (provisional):** "The effect of congruence between the price and background color lightness on the price list." *Journal of the Japan Society of Marketing & Distribution Review (jsmdreview)*, 7(1). (Author block did not render in text extraction — see open paths.)
- **Link:** https://www.jstage.jst.go.jp/article/jsmdreview/7/1/7_1/_html/-char/en
- **Why it matters:** A 2022 Japanese experiment (n = 299, online) manipulating background-color lightness (HSV lightness 30 / 50 / 70, hue 200, saturation 100 fixed) against price levels on a price list. Price–lightness congruency (high price × low lightness) raised both list evaluation (F(1,244) = 12.873, p < .001) and choice satisfaction (F(1,244) = 5.090, p = .025), fully mediated by "feeling right." Crucially, the authors explicitly tested and *failed to find* a position–lightness (heaviness) interaction effect here — a documented boundary condition: lightness-driven weight effects activate for tangible goods (Sunaga's detergent packages) but not for intangible services. Its reference list also names two further leads: Alexander & Shansky (1976) and a Japanese 2007 paper by Shinohara, Kinoshita & Ichikawa on lightness evoking heaviness (not yet retrieved — open path).

### 4. Yoto, Katsuura, Iwanaga & Shimomura (2007) — color heaviness ratings + EEG
- **Citation:** Yoto, A., Katsuura, T., Iwanaga, K., & Shimomura, Y. (2007). Effects of object color stimuli on human brain activities in perception and attention referred to EEG alpha band response. *Journal of Physiological Anthropology*, 26(3), 373–379.
- **DOI / link:** https://doi.org/10.2114/jpa2.26.373 — https://www.jstage.jst.go.jp/article/jpa2/26/3/26_3_373/_article/-char/ja/
- **Why it matters:** Peripheral to balance but squarely in the Japanese 色の重量感 tradition with real numbers: subjective "heavy" ratings of colored paper differed significantly between red and blue, alongside EEG alpha/theta-band differences. Useful as a physiological anchor that hue carries weight-relevant signal independent of luminance — the exact claim the computational track's "nobody sees hue as hue" result is testing against.

### 5. Nakauchi et al. (2022) — experimental aesthetics of painting chromatic composition (KAKEN-funded)
- **Citation:** Nakauchi, S., Kondo, T., Kinzuka, Y., Taniyama, Y., Tamura, H., Higashi, H., Hine, K., Minami, T., Linhares, J. M. M., & Nascimento, S. M. C. (2022). Universality and superiority in preference for chromatic composition of art paintings. *Scientific Reports*, 12, 4294.
- **DOI / link:** https://doi.org/10.1038/s41598-022-08365-z — funded by KAKENHI JP19H01119
- **Why it matters:** Toyohashi University of Technology team measured the chromatic statistics of actual paintings (including Japanese paintings) and showed experimentally that viewers prefer the original chromatic compositions over shuffled versions, across cultures and art-training levels. Not a balance study, but it is the closest funded Japanese experimental line on *pictorial color composition*, and its dataset approach (real paintings, measured color statistics) is a template the optical-balancing lab experiment could borrow for stimulus construction.

### 6. Anonymous (1934) — two-color combinations × areal proportion, paired comparisons
- **Citation (provisional):** 「色彩の空間的構造と感情價値 (第二報)」[The spatial structure of color and its affective value, Report II]. *心理学研究 (The Japanese Journal of Psychology)*, 9(3), p. 489–. (Author name did not render in text extraction — open path.)
- **Link:** https://www.jstage.jst.go.jp/article/jjpsy1926/9/3/9_489/_article/-char/ja
- **Why it matters:** A prewar Japanese paired-comparison experiment on color combinations where the *areal proportion* of the two components was systematically varied (1:9 through 9:1, both vertical and horizontal arrangements). Finding: a combination judged unpleasant at 5:5 could become pleasant at 3:7 — i.e., the affective value of a two-color composition is not a linear sum of single-color values but depends on the *area ratio itself*. This is an early area × hue interaction result, directly relevant to the area factor's non-additivity that the computational track just documented (area × saturation interaction). Four observers only — weak by modern standards, but historically the earliest Japanese area-proportion experiment found.

## Tier 2 — Theses and reports

### 7. Sato, Yui (2018) — master's thesis on visual heaviness (視覚的重量感)
- **Citation:** 佐藤 由依 (Sato, Yui). 「パッケージの色の明度による視覚的重量感の差と重要性知覚の関連について」[On the relationship between differences in visual heaviness due to packaging color lightness and perceived importance]. Master's thesis (Psychology), Tokyo Metropolitan University (首都大学東京), 2018-03-25.
- **Record:** OAI identifier oai:tokyo-metro-u.repo.nii.ac.jp:00006914 — CORE record: https://core.ac.uk/outputs/235010988/
- **Why it matters:** The only located Japanese thesis using the exact term 視覚的重量感 ("visual heaviness"). It extends the Sunaga 2016 lightness–heaviness paradigm to *perceived importance* judgments of packages. The abstract page did not expose its numerical results in this round — the full text sits in the TMU institutional repository (open retrieval path), and its experimental design may include the lightness-step heaviness ratings the formula needs.

## Dead ends (one line each)

- **CiNii Books alternate route:** generic web search surfaced no retrievable ci.nii.ac.jp book records for 視覚的均衡 / 視覚重量 / 画面構成 — keyword hits only; a live CiNii Books session or API key is needed.
- **CiNii Dissertations:** dead end inherited from Round 3 (empty response to the text client); not re-attempted.
- **KAKEN "visual weight / pictorial balance" (English):** no dedicated funded project found; adjacent aesthetics projects (Yoshida 26370119, aesthetics of illusion; Miura 18K00120, definition of art) are not balance-focused.
- **Doshisha / Kyoto / Tsukuba / Kyushu IR keyword searches:** no retrievable balance/composition theses surfaced this round beyond the TMU record above.
- **Fukada 1983/84/85:** skipped per brief (print-only, dead end already established).
- **Shinohara, Kinoshita & Ichikawa (2007):** cited in the 2022 jsmdreview paper as a Japanese source for lightness-evoked heaviness, but no retrievable record located this round — author spellings and venue unverified.

## Full citation list

1. Hayashi, M. (1969). 画面の力動的均衝に関する一研究: 美的観照に関する研究-第II報告. 教育心理学研究, 3(1), 11–17. https://doi.org/10.5926/jjep1953.3.1_11
2. Sunaga, T., Park, J., & Spence, C. (2016). Effects of lightness–location congruency on consumers' purchase decision-making. Psychology & Marketing, 33(11), 934–950. https://doi.org/10.1002/mar.20929
3. [Author pending]. (2022). The effect of congruence between the price and background color lightness on the price list. jsmdreview, 7(1). https://www.jstage.jst.go.jp/article/jsmdreview/7/1/7_1/_html/-char/en
4. Yoto, A., Katsuura, T., Iwanaga, K., & Shimomura, Y. (2007). Effects of object color stimuli on human brain activities in perception and attention referred to EEG alpha band response. Journal of Physiological Anthropology, 26(3), 373–379. https://doi.org/10.2114/jpa2.26.373
5. Nakauchi, S., Kondo, T., Kinzuka, Y., Taniyama, Y., Tamura, H., Higashi, H., Hine, K., Minami, T., Linhares, J. M. M., & Nascimento, S. M. C. (2022). Universality and superiority in preference for chromatic composition of art paintings. Scientific Reports, 12, 4294. https://doi.org/10.1038/s41598-022-08365-z
6. [Author pending]. (1934). 色彩の空間的構造と感情價値 (第二報). 心理学研究, 9(3), 489–. https://www.jstage.jst.go.jp/article/jjpsy1926/9/3/9_489/_article/-char/ja
7. Sato, Y. (2018). パッケージの色の明度による視覚的重量感の差と重要性知覚の関連について. Master's thesis, Tokyo Metropolitan University. oai:tokyo-metro-u.repo.nii.ac.jp:00006914 — https://core.ac.uk/outputs/235010988/

## Still-open retrieval paths

1. **Hayashi 1969 full PDF** (free on J-STAGE): digitize the 18-figure × 3-composition preference tables — the direction-tension × deviation data is the earliest real dataset for the position/direction arm of the formula.
2. **Hayashi Report I** (美的観照に関する研究-第I報告): presumed to exist; search CiNii once live access is available.
3. **Sato (2018) TMU thesis full text** via the TMU IR record oai:tokyo-metro-u.repo.nii.ac.jp:00006914 — likely downloadable PDF with the lightness-step heaviness numbers.
4. **jsmdreview 2022 article authorship + DOI**, and through its reference list, **Shinohara, Kinoshita & Ichikawa (2007)** — the Japanese lightness→heaviness root experiment.
5. **1934 心理学研究 paper**: author name and full page range (J-STAGE browse page for jjpsy1926 vol 9 no 3).
6. **CiNii Books / NDL**: live session or API access would reopen the thesis avenue that the text client could not reach.
