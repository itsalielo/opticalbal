# Optical Balancing — Round 3: Dissertations & Theses

Date: 2026-10-09. Hunt across thesis repositories for the exact-formula question (visual weight as a decomposable function of pixel-group factors: saturation, hue, lightness, area, position, contrast). Most relevant first. Discovery layer: OpenAlex (dissertation filter) + grafiati + repository pages; repository quirks and dead ends listed at the end.

---

## 1. Martin Georg Fillinger — *Effects of perceptual balance on aesthetic appreciation* (2020, University of Konstanz)
- **University:** University of Konstanz, Germany — **Advisor:** Ronald Hübner
- **URL:** http://nbn-resolving.de/urn:nbn:de:bsz:352-2-1ewj19tdkfvvp9 (KOPS)
- **Access:** Open (CC-BY per OpenAlex). I could not fetch the landing page with my text client — record harvested from KOPS via OpenAlex OAI-PMH; existence corroborated by the indexed dissertation summary on ResearchGate and citations.
- **Why it matters (most relevant find):** This is the dissertation *behind* the DCM model (Hübner & Fillinger 2016) — the comparison of objective balance measures that Round 2 ranked as a key anchor. It is a four-paper thesis testing whether balance, computed as a mechanical equilibrium from assumed element weights, predicts subjective balance and liking. Its working assumption is stated plainly: each element in a picture has a perceptual weight depending on its low-level features such as color, size and form. Key results: the mechanical-balance metaphor holds for simple stimuli but breaks for complex pictures (calligraphies, textured artworks); balance is read as mechanical for single-element pictures and as gravitational stability for multi-element/dynamic ones; instability is liked when it implies movement. This is the closest any thesis comes to confronting the additive weight-function hypothesis head-on — and to falsifying it where it fails.

## 2. Mohammad Ali Mokarian — *Visual balance in engineering design for aesthetic value* (2007, University of Saskatchewan)
- **University:** University of Saskatchewan, Canada — Dept. of Mechanical Engineering — **Degree:** M.Sc. thesis
- **Handle:** http://hdl.handle.net/10388/etd-05112007-140335 — **Open PDF (Library and Archives Canada):** https://www.collectionscanada.gc.ca/obj/thesescanada/vol2/SSU/TC-SSU-05112007140335.pdf
- **Access:** Open PDF via LAC. (The USask handle page itself timed out for my text client.)
- **Why it matters:** The abstract explicitly claims a "more general formula" relating visual balance to both geometric and color variables, derived after statistical experiments with cell-phone designs testing two hypotheses about classifying design variables. This is the forgotten-formula-attempt archetype this round was hunting: a quantitative balance function fitted to experiments, now essentially uncited except by Koenderink et al. (2017, "Compositorial 'Weight' & 'Luminance'"). Worth retrieving the formula chapter and comparing its factor set (geometry, color) against the hypothesized native factors.

## 3. Michael P. Bauerly — *Mathematical modeling and experimental study of interface aesthetics* (2007, University of Michigan)
- **University:** University of Michigan — **Degree:** PhD (ProQuest diss. 3276095)
- **URL:** https://hdl.handle.net/2027.42/126625 (Deep Blue — landing page verified live)
- **Access:** Metadata + abstract open; full text via ProQuest, no open PDF linked.
- **Why it matters:** Sets out to develop and validate quantitative metrics for common compositional attributes, symmetry and balance among them, and to relate the attribute quantities to appraisals of aesthetic appeal via subject ratings. The abstract reports subjects prefer symmetry and fewer compositional elements. It is a direct attempt at an operational formula for balance/symmetry measures with human validation — a template for how the field tried to formalize balance before the deep-learning era. The final section uses an interactive genetic algorithm to optimize designs from user feedback, which is the inverse use of the same measures.

## 4. Aliaksei Miniukovich — *Computational Aesthetics in HCI: Towards a Predictive Model of Graphical User Interface Aesthetics* (2016, Università degli studi di Trento)
- **University:** University of Trento, Italy — **Degree:** Doctoral thesis
- **Handle:** https://hdl.handle.net/11572/368110 — **Open PDF:** http://eprints-phd.biblio.unitn.it/1773/1/aesthetics_thesis_v1.2.12_final_1.pdf
- **Access:** Open PDF.
- **Why it matters:** Builds a predictive model of GUI aesthetics grounded in processing-fluency theory: it defines several theory-backed visual dimensions of interface designs, automatically evaluates each, and combines them into an estimate of the average population impression. This is a multi-factor composition function of exactly the additive/combinatorial kind the project is after, with the combination weights derived from theory plus validation — a useful foil to the Russian additive model (Al Akkad & Gazimzyanov 2017) for the question of how factors get combined (additive vs. fitted).

## 5. Chien-Yin Lai (賴建穎) — *An Intelligent Composition System for Text-overlaid Images based on Computational Aesthetics* (2009, National Chi Nan University, Taiwan)
- **University:** National Chi Nan University, Taiwan — Dept. of Computer Science and Information Engineering — **Degree:** PhD
- **NDLTD Taiwan handle:** http://ndltd.ncl.edu.tw/handle/31375054678738849202 — **CORE record (abstract + metadata):** https://core.ac.uk/outputs/70630938/
- **Access:** Abstract and metadata open (CORE / NCNU IR); full-text availability unconfirmed.
- **Why it matters:** Proposes quantitative models of balance and symmetry explicitly "based on principles of visual weights and image segmentation techniques," with two experiments establishing a proportional relation between computed balance and aesthetic appeal. A later pilot study estimates the visual weight of each object from saliency maps and finds the saliency-based balance tracks appeal the same way as the segmentation approach. This is one of the few theses that treats visual weight as an explicit, computed quantity and swaps its estimator (segmentation vs. saliency) — directly relevant to whether weight should be a bottom-up pixel measure or a semantic-object measure. Follow-up thesis in the same lab: Mien-Tsung Tsai (2014), *Low Intrusive In-image Text Overlay Based on Saliency Cut and Computational Aesthetics* (http://ndltd.ncl.edu.tw/handle/33219226581006567627, metadata only).

## 6. Pierre Lelièvre — *Pictorial composition: modeling, perception & creation* (2022, Université Paris Sciences et Lettres)
- **University:** Université PSL, France — **Degree:** Doctoral dissertation — **DOI:** 10.70675/cc153babzed95z4048z9594z3b1b65403dbe
- **URL:** https://doi.org/10.70675/cc153babzed95z4048z9594z3b1b65403dbe (resolves to theses.fr record — verified live)
- **Access:** theses.fr metadata verified; open PDF not confirmed from the record page.
- **Why it matters:** A research-creation thesis that models compositional regularities as a continuous, vector, probabilistic latent space built from hierarchical RNN-VAEs trained on 5,000+ personal abstract compositions vectorized as Bézier curves. Perceptual structure of the latent space is validated with MLDS triplets and captured via Fisher information. It rejects pixel-based deep models for the sequential, non-stationary composition process — a strong counter-proposal to the pixel-group factor hypothesis: it models the *generative process* of composition rather than decomposing weight per pixel group. The contrast is exactly what the project needs to sharpen its own claim.

## 7. Weng Khuan Hoh — *Effect of Encoded Theories of Visual Perception in Computational Aesthetics* (2022, Victoria University of Wellington)
- **University:** Victoria University of Wellington, New Zealand — **Degree:** PhD — **DOI:** 10.26686/wgtn.20337570
- **Open PDF:** https://openaccess.wgtn.ac.nz/articles/thesis/Effect_of_Encoded_Theories_of_Visual_Perception_in_Computational_Aesthetics/20337570/1/files/36350304.pdf
- **Access:** Open PDF.
- **Why it matters:** Encodes classical theories of visual perception into computational aesthetics — i.e., it tests whether the inherited theoretical vocabulary (Gestalt/Arnheim lineage) survives when implemented as algorithms. Useful as a check on which theoretical primitives (potentially including balance/weight) are computable at all.

## 8. Christel Chamaret — *Color harmony: experimental and computational modeling* (2016, Université Rennes 1 / IRISA)
- **University:** Université Rennes 1, France — **Degree:** PhD — **NNT:** 2016REN1S015
- **TEL:** https://theses.hal.science/tel-01382750 — **Open PDF:** https://theses.hal.science/tel-01382750v1/file/CHAMARET_Christel.pdf (13.24 MB, verified live)
- **Access:** Open PDF.
- **Why it matters:** Two-pronged (eye-tracking experiment + computational models) treatment of the color side of the weight question. It builds ground truth for color harmony judgments and proposes two computational models plus a quality metric combining visual masking and color harmony to predict which areas read as harmonious given their neighborhood. Relevant for the hue/saturation/lightness factor values of the hypothesized formula — and for whether color effects decompose additively or interact with spatial context (masking).

## 9. Xiaoyang Yang — *Visual balance — the tightrope of computer generated layout* (1995, MIT)
- **University:** MIT — Program in Media Arts & Sciences — **Degree:** M.S. thesis — **Advisor:** William J. Mitchell
- **Handle:** http://hdl.handle.net/1721.1/63208 (DSpace@MIT — landing page verified live)
- **Access:** Open PDF (6.93 MB).
- **Why it matters:** An early (1995) attempt to make visual balance computable for computer-generated layout — historical baseline for how the formula question was first posed in HCI/design computing, before saliency, before DCM. Likely thin on experiment, but useful as the earliest thesis-shaped attempt.

## 10. Vasiliki Kitsopoulou — *Analysing formal visual elements of corporate logotypes using computational aesthetics* (2018, University of East Anglia)
- **University:** University of East Anglia, UK — Norwich Business School — **Degree:** PhD
- **URL:** https://ueaeprints.uea.ac.uk/69186/ (repository page verified live)
- **Access:** Metadata open; full text requires repository login (a direct PDF URL is indexed by OpenAlex: https://ueaeprints.uea.ac.uk/id/eprint/69186/1/Vasiliki_Kitsopoulou_PhD_thesis_-_6524036.pdf).
- **Why it matters:** Applies 107 computational aesthetic measures — including, for the first time in this literature, hue, saturation and colorfulness metrics — to 215 professionally designed logotypes, and shows via regression and RBF neural nets that the measures predict expert ratings. It is effectively a catalog of candidate factor-measures with their empirical distributions and a factor analysis of how they group (elaborateness/naturalness/harmony). Good source for which factors are measurable and which collapse together.

## 11. Bin Jin — *Computational Aesthetics and Image Enhancements using Deep Neural Networks* (2018, EPFL)
- **University:** EPFL, Switzerland — **Degree:** Doctoral thesis — **DOI:** 10.5075/epfl-thesis-8420
- **URL:** https://infoscience.epfl.ch/handle/20.500.14299/146179 (Infoscience)
- **Access:** Open access per OpenAlex; landing page not fetched, PDF likely available via Infoscience.
- **Why it matters:** Deep-learning approach to aesthetic assessment and enhancement. Less formula-oriented, but documents the learned-feature alternative to explicit factor decomposition — the approach the project is arguing against.

## 12. Li Ji — *Image composition in computer rendering* (2016, University of Victoria)
- **University:** University of Victoria, Canada — **Handle:** http://hdl.handle.net/1828/7574
- **Access:** Metadata via grafiati; full text presumed open at UVic handle (landing page not fetched).
- **Why it matters:** Studies image composition in computer rendering — how composition can be computed and why it is hard with conventional renderers. Adjacent to the composition-modeling question rather than the weight formula.

## 13. Qianqian Gu — *Computational aesthetics learning of traditional Chinese painting* (University of Manchester)
- **University:** University of Manchester, UK — **Degree:** PhD
- **URL:** https://research.manchester.ac.uk/en/studentTheses/8f0d62be-cee0-483d-be2c-b4cbb7569f1f
- **Access:** Record exists (Manchester Pure); full text not open via that record.
- **Why it matters:** Machine-learning approach to computational aesthetics on traditional Chinese painting. Included as a data point that the learned-aesthetics strand dominates recent theses — the formula attempts are mostly pre-2010 (Mokarian, Yang, Lai, Bauerly) or psychology-anchored (Fillinger).

---

## Repository notes and quirks (this round)

- **EThOS**: confirmed relaunched (new Hyku platform at ethos.bl.uk) as a metadata-only discovery service with 650k+ UK thesis records; download buttons now redirect to the holding university's repository. Full-text access depends on each university.
- **NDLTD Global ETD Search** (search.ndltd.org): interface is JavaScript-only — not queryable with a text client. Covered instead via OpenAlex (which harvests the same repositories' OAI-PMH feeds) plus direct NDLTD-Taiwan handles found via grafiati/CORE.
- **DART-Europe**: per brief, closed Feb 2025; not used — NDLTD/OpenAlex covered the European records.
- **theses.fr / TEL**: theses.fr website works (Lelièvre record opened live); the standalone API endpoints I tried returned 404/unresolvable — query theses.fr via the web UI or HAL/TEL pages instead. TEL full texts open (Chamaret PDF verified).
- **DiVA portal**: smash search page refused my text client (403); DiVA records were reached via OpenAlex OAI harvest instead.
- **DissOnline (Germany)**: no relevant German-language dissertations surfaced on visual balance/weight or Bildästhetik relevant to the formula question this round — territory likely thin; the Konstanz (Fillinger) record is the German contribution.
- **CiNii Dissertations (Japan)**: search endpoint returned an empty response to my text client — dead end for direct querying; Japanese theses unsearched this round.
- **PQDT Open**: checked via OpenAlex/grafiati; no directly relevant records beyond those covered here.

## Dead ends / gaps

- Mokarian's USask handle page timed out; the LAC-hosted PDF covers it.
- Fillinger's KOPS landing page could not be fetched; record confirmed via OpenAlex harvest + indexed dissertation summary.
- No dissertations were found that propose an *exact closed-form* visual-weight function with fitted per-factor coefficients beyond the Al Akkad & Gazimzyanov model already in Round 2 — Mokarian (2007) comes closest to a forgotten formula attempt and its PDF is open.
- French-language theses on "équilibre visuel" did not surface; the one relevant French thesis found (Chamaret) is on color harmony.
