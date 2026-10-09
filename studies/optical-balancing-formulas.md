# Optical Balancing — Computational & Mathematical Models (the formula spine)

**Worker D — computational models survey. Written 2026-10-09.**
**Research question:** does an EXACT mathematical formula for optical balancing exist, or can one be derived? (Hypothesis: each pixel group carries a weight, so perceived balance should be computable.)

**How this document is sourced (hard rules applied):**
- Every paper below was verified by searching its exact title. Each entry carries a DOI or a direct link plus access status.
- Tier 1 = peer-reviewed papers (DOI/link). Tier 1b = foundational scholarly monographs (books — not journal peer-reviewed, but academic). Tier 2 = informed non-academic sources (software docs, publisher pages that document a Tier 1 method). Tier 2 never stands in for Tier 1.
- Preprints are flagged as preprints, never presented as peer-reviewed literature.
- Where an exact coefficient form could not be re-verified from a retrievable source in this session, it is flagged **UNVERIFIED** and described only at the conceptual level. No fabricated formulas.
- Everything is paraphrased; no long quotations.

---

## 0. The honest verdict (read first)

**No exact, general, validated formula for optical balancing exists.** What exists is a family of partial models, each of which computes *a* balance score from *a* definition of visual weight, and each of which breaks in documented ways:

1. **Birkhoff's M = O/C (1933)** — the original candidate for an exact aesthetic formula — **failed its empirical tests** (Eysenck, 1968: predicted values vs. human ratings, r = .13, n.s.). Its two main successors both *inverted* it (M = O×C).
2. **The center-of-mass family (DCM and relatives)** is the most validated quantitative approach: on simple black-and-white geometric patterns, the deviation of the perceptual center of mass from the geometric center explains up to **68% of variance in balance ratings and 86% in liking ratings** (Hübner & Fillinger, 2019). But the same measures **fail outright on Japanese calligraphy** (Gershoni & Hochstein, 2011; Fillinger & Hübner, 2018) and weaken sharply on photographs (McManus et al., 2011; Thömmes & Hübner, 2018).
3. **The only work that literally presents "a theoretical formula for balance" as a closed-form equation (Corwin's quadrant-luminance model) is an unreviewed preprint**, validated on LED pictures with mostly-painter observers, whose own author says it is unclear whether it applies to states of imbalance.
4. **The weight function is the hole in every model.** Every formula needs w(pixel group) — but the literature has no agreed computational definition of visual weight beyond proxies (darkness, area, saliency). Ali's hypothesis decomposition (weight = f(saturation, hue, lightness, area, position, contrast)) is exactly the right research program — and every term in it is currently an unidentified function.
5. **There is a theoretical ceiling argument against pure computability:** Reber, Schwarz & Winkielman (2004) argue beauty is grounded in the *perceiver's processing experience*, only partly a function of stimulus properties; McManus, Cook & Hunt (2010) show weak population preferences but strong, stable, *varied* individual preferences — a normative formula cannot capture both.

**The precise gap (what it would take to derive one):** an exact formula requires (a) a validated visual-weight function w(x,y) over the full factor set, (b) the correct reference point (geometric center vs. perceived center, and the top/bottom and left/right anisotropies), (c) a combination rule for the weights that survives complex, meaningful images — not just geometric patterns — and (d) a bounded account of perceiver-side variance. None of the four is solved. Details in §8.

---

## 1. The classical formula: Birkhoff's aesthetic measure (1933)

### 1.1 Birkhoff, G. D. — *Aesthetic Measure* (1933) — Tier 1b
- **Formula:** **M = O / C**, where M = aesthetic measure, O = order (unity), C = complexity (variety). The proposal: within each class of aesthetic objects, define order and complexity so that their ratio yields the object's aesthetic measure.
- **For polygons (his worked example):** O = V + E + R + HV − F, where V = vertical symmetry, E = equilibrium, R = rotational symmetry, HV = relation to a horizontal–vertical network, F = a negative "unsatisfactory form" factor; C = the number of distinct straight lines containing at least one side of the polygon.
- **For vases (his other worked example):** O = H + V + HV, counting the independent cases where distances in the vase's characteristic network stand in harmonic ratios (1:1 or 1:2); e.g. a vase with O = 5, C = 10 gets M = 0.5 (reconstructed in Hübner & Ufken, 2023).
- **What it predicts:** objects with high order and low complexity score highest; it is a formalization of "unity in variety."
- **Validation:** essentially none in Birkhoff's own work — he published 90 polygons and the definitions but ran no preference experiments.
- **Limitations:** O and C have no precise operational definitions outside the toy classes (polygons, vases, ornaments); the formula is introspective, not empirical. The 2025 VME paper notes the same core objection: the absence of precise operational definitions for "order" and "complexity."
- **Source:** Birkhoff, G. D. (1933). *Aesthetic Measure.* Harvard University Press, Cambridge, MA. (Book; no DOI. Widely catalogued; PDF copies circulate, e.g. via university hosts.)

### 1.2 The direct empirical refutation
- **Eysenck, H. J. (1968). "An experimental study of aesthetic preference for polygonal figures." *The Journal of General Psychology*, 79(1), 3–17. DOI: 10.1080/00221309.1968.9710447** (Tier 1; paywalled, Taylor & Francis)
- **What was tested:** Birkhoff's computed M values for polygons vs. averaged human aesthetic ratings.
- **Result:** correlation r = .13, not statistically significant — the formula failed to predict actual aesthetic judgments. M did correlate with a complexity–simplicity factor (r = .51), i.e. it measured something, just not beauty.

### 1.3 Successors and variants (Birkhoff's lineage)
- **Eysenck, H. J. (1941). "The empirical determination of an aesthetic formula." *Psychological Review*, 48, 83. DOI: 10.1037/h0062483** (Tier 1; paywalled, APA). **Formula: M = O × C** — aesthetic value as the *product* of order and complexity, arguing the data show a direct (not inverse) relation between M and C: the better-liked designs were the more complex ones.
- **Moles, A. A. (1958). *Théorie de l'information et perception esthétique.* Paris: Flammarion** (Tier 1b; English trans. *Information Theory and Esthetic Perception*, Univ. of Illinois Press, 1966). Reworked Birkhoff through Shannon information theory: order becomes low entropy (redundancy/predictability), complexity becomes high entropy (unpredictability), and the measure becomes **M = O × C**. (Noted consequence: low-O/low-C and high-O/high-C objects score the same under some parameterizations — the O–C relation itself stays underspecified.)
- **Beebe-Center & Pratt (undated in retrieved sources; cited in Zhang & Xue, 2025).** Decomposed Birkhoff's "order" into sub-dimensions — vertical and rotational symmetry, balance, horizontal and vertical cross-order, asymmetry — to improve the correlation between the model's outputs and subjective judgments. (Tier 2 citation-of-record; original not re-verified here.)
- **Moon, P., & Spencer, D. E. (1944). "Aesthetic measure applied to color harmony." *JOSA*, 34, 234.** (Tier 1; paywalled.) Applied a Birkhoff-style measure to color harmony — an early extension of the formula beyond shape. (Cited in the reference list of the Entropy 2021 information-theory aesthetics paper.)
- **Franke, H. W. (1977). "A cybernetic approach to aesthetics." *Leonardo*, 10(3), 203–206.** (Tier 1; paywalled.) Cybernetic/information-theoretic successor in the Birkhoff lineage. (Cited in the same reference list; details not re-verified here.)
- **Javid, M. A. J., Blackwell, T., Zimmer, R., & Al-Rifaie, M. M. (2016). "Correlation between Human Aesthetic Judgement and Spatial Complexity Measure." *Proc. EvoMUSART 2016* (Springer LNCS). arXiv:1707.06510** (Tier 1 conference; arXiv copy open). Proposed a computational complexity measure based on information gain from the spatial distribution of pixels and their uniformity/non-uniformity, explicitly positioned against Birkhoff (M = O/C) and Eysenck (M = O×C).
- **Hübner, R., & Ufken, E. S. (2023). "On the beauty of vases: Birkhoff's aesthetic measure versus Hogarth's line of beauty." *Frontiers in Psychology*, 14. DOI: 10.3389/fpsyg.2023.1114793** (Tier 1; open access, PMC10159058). The only modern direct test of Birkhoff's *components*: 25 symbolic vases varying width × curvature, online beauty ratings. Both Birkhoff-style geometric ratios and outline curvature contributed; a quadratic model accounted for ~96% of variance in mean beauty ratings. **Important nuance:** this validates the *ingredients* of O, not M = O/C as a predictive formula.

**Section verdict:** the Birkhoff program produced the only true "exact formula" candidate in the literature, and it failed empirically. Every successor either inverted it, redefined its terms informationally, or tested only its components.

---

## 2. The center-of-mass family (the most validated quantitative approach)

The core idea (the "mechanical metaphor," traced to Ross, 1907, *A Theory of Pure Design*): treat the picture as a distribution of perceptual mass; it is balanced when its center of mass coincides with its geometric center.

### 2.1 DCM — Deviation of the Center of "Mass"
- **Hübner, R., & Fillinger, M. G. (2016). "Comparison of Objective Measures for Predicting Perceptual Balance and Visual Aesthetic Preference." *Frontiers in Psychology*, 7, 335. DOI: 10.3389/fpsyg.2016.00335** (Tier 1; open access). Building on McManus, Stöver, & Kim (2011) below.
- **Formula (as implemented and documented in Redies et al., 2025):** assign each pixel a perceptual mass (for black-and-white patterns: black = 1, white = 0); compute the mass-weighted centroid (b_x = Σ i·m(i,j)/N, b_y = Σ j·m(i,j)/N, N = total mass); take the Euclidean distance of this center from the geometric center per axis and express it as a **percentage of the maximum possible distance** for that image — the *DCM score* (0 = centered, 100 = center of mass in a corner). The Toolbox generalizes this to grayscale images.
- **What it predicts:** the smaller the DCM, the more balanced (and, on simple stimuli, the more liked) the picture.
- **Validation:** on the geometric-pattern stimuli of Wilson & Chatterjee (2005), DCM predicted balance and liking about as well as the APB; **averaged across pictures, DCM scores explained up to 68% of the variance in balance ratings and up to 86% in liking ratings** (reported in Hübner & Fillinger, 2019). In a direct rating comparison, DCM correlated more strongly with subjective *balance* ratings than the APB "Balance score," while APB predicted *preference* better (Redies et al., 2025).
- **Limitations:** the strong numbers are stimulus-specific — homogeneous elements, one gray level, simple shapes. DCM **failed to predict balance ratings for Japanese calligraphies** (Fillinger & Hübner, 2018) and weakens on photographs (see §2.4, §7).

### 2.2 McManus, Stöver & Kim — the center-of-mass origin study
- **McManus, I. C., Stöver, K., & Kim, D. (2011). "Arnheim's Gestalt theory of visual balance: Examining the compositional structure of art photographs and abstract images." *i-Perception*, 2, 615–647. DOI: 10.1068/i0445aap** (Tier 1; open access via PMC).
- Tested Arnheim's balance claims on art photographs and abstract images using the center-of-mass/gray-value-integration approach. Key caution from this line: correlations between perceptual balance and aesthetic appreciation are **much weaker for photographs** than for constructed patterns (also reported in Hübner & Fillinger, 2019, citing McManus et al., 2011 and Thömmes & Hübner, 2018).

### 2.3 The modern reference implementation (Toolbox, 2025)
- **Redies, C., Bartho, R., Koßmann, L., Spehar, B., Hübner, R., Wagemans, J., & Hayn-Leichsenring, G. U. (2025). "A toolbox for calculating quantitative image properties in aesthetics research." *Behavior Research Methods*, 57(4), 117. DOI: 10.3758/s13428-025-02632-3** (Tier 1; open access, PMC11909096).
- Implements both the **APB "Balance score"** and the **DCM score** (including a grayscale DCM) as standardized, citable computations — the closest thing the field has to a canonical balance formula today.

### 2.4 VME — Visual Moment Equilibrium (2025): the most complete engineered formula
- **Zhang, X., & Xue, C. (2025). "Visual Moment Equilibrium: A Computational Cognitive Model for Assessing Visual Balance in Interface Layout Aesthetics." *Symmetry*, 18(1), 41. DOI: 10.3390/sym18010041** (Tier 1; open access).
- **Formulas:**
  - Equilibrium condition: Σ_i S_i·(x_i − x_centroid) = 0 and Σ_i S_i·(y_i − y_centroid) = 0, where S_i = area of element i (area = visual weight), (x_i, y_i) = element centroid. The aggregate centroid is the "ideal balanced position."
  - **Measured Balance: B_m = 1 − D_centroid / D_max**, with Manhattan distances D_centroid = |x_centroid − x_center| + |y_centroid − y_center| and D_max = |x_max − x_center| + |y_max − y_center| (offset of the farthest boundary from the geometric center). B_m → 1 = well balanced.
  - Psychophysical sharpening: **B_m′ = e^(5·B_m − 1)**, an exponential transform (coefficient 5 from preliminary sensitivity analysis) to amplify near-perfect balance, motivated by nonlinear psychophysical functions.
  - Visual-weight refinements: a **nine-grid weighting system** (extending Zhou et al.'s quadrant "visual dominance" weights — upper-left 33%, upper-right 28%, lower-left 23%, lower-right 16%) plus a **Shape Sparsity Ratio with piecewise compensation** for irregular elements (operationalizing Gestalt closure). The model also incorporates known anisotropies: the perceived balance center sits slightly *above* the geometric center; left-side elements read as lighter than right-side ones (hemispheric lateralization); left–right balance matters more than top–bottom balance (citing McManus et al.).
- **What it predicts:** a single 0–1 balance score for interface layouts, regular or irregular.
- **Validation:** against Analytic Hierarchy Process expert benchmarks — Experiment 1 (15 regular interfaces): Model-M **r = 0.942 (R² = 0.888)** vs. a baseline model at r = 0.58 (R² ≈ 0.34); Experiment 2 (9 irregular interfaces): Model-M+ **r = 0.890**.
- **Limitations:** tiny stimulus sets (15 and 9 interfaces), expert raters only, industrial-interface context (Southeast University, China); the exponential coefficient is fitted, not derived; the nine-grid weights are coarse and partly stipulated; visual weight still reduces to area (+ grid position), ignoring color, contrast, and semantics.

### 2.5 Corwin's quadrant-luminance formula — the only literal "theoretical formula for balance"
- **Corwin, D. M. "Pictorial balance is a bottom-up aesthetic property mediated by eye movements. A theoretical model of a primitive visual operating system could explain balance." *bioRxiv* preprint, DOI: 10.1101/2020.05.26.104687** (PREPRINT — not peer-reviewed; open).
- **Formula** (picture centered at (0,0); L_xxQ = mean luminance of quadrant xx):
  - X = (X_ULQ·L_ULQ + X_URQ·L_URQ + X_LLQ·L_LLQ + X_LRQ·L_LRQ) / L_TOTAL
  - Y = (1.07·Y_ULQ·L_ULQ + 1.07·Y_URQ·L_URQ + Y_LLQ·L_LLQ + Y_LRQ·L_LRQ) / L_TOTAL
  - L_TOTAL = (L_ULQ + L_URQ + L_LLQ + L_LRQ) / 4
  - **Balance = √(X² + Y²)**, or the vector L⃗ = (X, Y).
- **Claim:** a rectangular picture is *perfectly* balanced iff it has bilateral quadrant luminance symmetry with the lower half lighter by **~1.07 ± 0.03** (upper-half Y-weights scaled by 1.07 to model the greater visual weight of the upper half) — i.e., its "center of luminance" sits at the geometric center. This is a center-of-mass equation with luminance as mass and an empirically fitted top/bottom anisotropy.
- **Validation:** computer models of LED pictures; two small studies comparing identical pictures in different frames — observers (mostly painters) who could "disregard salience" showed a significant correlation between computed pair imbalance and perceiving the identical pictures as different. Conventional preference testing was judged impossible with the LED setup.
- **Limitations:** preprint; tiny, special population (painters); LED-only stimuli; **the author's own caveat: the equation is precise for the state of perfect balance, but "it is not clear whether it could be applied accurately to pictorial states of imbalance"** — i.e., it defines one point, not a general function. The 1.07 factor is unreplicated elsewhere in the literature.

**Section verdict:** the center-of-mass family is the closest the literature comes to Ali's hypothesis made computable — and its failures are informative: the *mechanics* work; the *mass* (visual weight) is what breaks.

---

## 3. Visual-weight quantification: APB and saliency-weighted models

### 3.1 APB — Assessment of Preference for Balance
- **Wilson, A., & Chatterjee, A. (2005). "The assessment of preference for balance: Introducing a new test." *Empirical Studies of the Arts*, 23(2), 165–180. DOI: 10.2190/B1LR-MVF3-F36X-XR64** (Tier 1; paywalled, SAGE).
- **Formula:** the pixel's perceptual weight is taken as inversely related to its gray level (dark pixels heavier than bright ones). The picture is divided around four axes (horizontal, vertical, two diagonals); for each axis the summed weights of opposite halves *and* of inner vs. outer areas are compared — eight partial difference measures — and the **mean of the eight is the APB score, 0% (perfect balance) to 100% (no balance)** (construction documented in Braun, Hofmann & Doerschner, 2026, *i-Perception*).
- **What it predicts:** a 0–100 imbalance score from pure pixel-weight distribution, built on Arnheim's (1954) structural skeleton of symmetry axes.
- **Validation:** on 130 images of black geometric elements, APB scores predicted balance ratings and related to aesthetic appreciation (Hübner & Fillinger, 2019). Aesthetic preference tracked the measure mainly because highly *imbalanced* configurations were disliked, not because highly balanced ones were extra-liked (Palmer et al.'s summary of the study).
- **Limitations:** **APB completely failed to predict perceptual balance ratings for Japanese calligraphies** (Gershoni & Hochstein, 2011; replicated by Fillinger & Hübner, 2018) — the luminance-as-weight assumption does not survive brushstroke stimuli.

### 3.2 Saliency-weighted balance (photographs)
- **Abeln, J., Fresz, L., Amirshahi, S. A., McManus, I. C., Koch, M., Kreysa, H., & Redies, C. (2016). "Preference for well-balanced saliency in details cropped from photographs." *Frontiers in Human Neuroscience*, 9, 704. DOI: 10.3389/fnhum.2015.00704** (Tier 1; open access). Applied the DCM machinery with **visual saliency** (not luminance) as the mass: cropped details chosen by participants had smaller saliency-DCM than avoided details — i.e., people crop toward saliency balance.
- **Thömmes, K., & Hübner, R. (2018). "Instagram Likes for Architectural Photos Can Be Predicted by Quantitative Balance Measures and Curvature." *Frontiers in Psychology*, 9. DOI: 10.3389/fpsyg.2018.01050** (Tier 1; open access). ~700 architectural photographs: quantitative balance measures (incl. a DCM variant) predicted real-world Instagram likes. Validation outside the lab — but on a narrow genre (architecture) where geometry dominates.
- **Limitation of the sub-family:** replacing luminance with saliency improves photographs but inherits every saliency model's own assumptions; still no color/weight decomposition.

### 3.3 Learning the weights from data (Jahanian et al.)
- **Jahanian, A., Vishwanathan, S. V. N., & Allebach, J. P. (2015). "Learning visual balance from large-scale datasets of aesthetically highly rated images." *Proc. SPIE 9394, Human Vision and Electronic Imaging XX*, 93940Y. DOI: 10.1117/12.2084548** (Tier 1; paywalled, SPIE).
- **Method:** 120K highly-rated professional photographs; saliency maps fitted with mixtures of Gaussians to find "hotspots." The inferred hotspots aligned with Arnheim's predicted visual hotspots, supporting the viability of **center of mass, symmetry, and the rule of thirds** as balance cues in real photographs.
- **Limitation:** qualitative confirmation of Arnheim's skeleton — it mines where the weight *is* in good photos but does not output a closed-form balance equation (the authors note precise quantitative proportion parameters were never established).

---

## 4. Interface-aesthetics formula systems (HCI: Ngo, Bauerly & Liu, Zen & Vanderdonckt)

### 4.1 Ngo, Teo & Byrne — 14 computed aesthetic measures
- **Ngo, D. C. L., Teo, L. S., & Byrne, J. G. (2003). "Modelling interface aesthetics." *Information Sciences*, 152, 25–46. DOI: 10.1016/S0020-0255(02)00404-8** (Tier 1; paywalled, ScienceDirect).
- **System:** 14 layout measures, each a 0–1 formula from element geometry — balance (BM), equilibrium (EM), symmetry (SYM), sequence (SQM), cohesion (CM), unity (UM), proportion (PM), simplicity (SMM), density (DM), regularity (RM), economy (ECM), homogeneity (HM), rhythm (RHM), order & complexity (OM) — combined via an artificial neural network into an overall aesthetic value.
- **Balance concept (verified at conceptual level; exact coefficients UNVERIFIED in this session):** BM is computed from the difference between total visual weights (object areas) on opposite sides of the vertical and horizontal midlines, normalized to [0,1]; 1 = perfectly balanced.
- **Validation:** the 14-term ANN model reached **r = 0.94 (p < 0.001)** against the participant ratings from Ngo & Byrne's (2001) 57-screen study (reported in Altaboli's 2012 Northeastern dissertation — Tier 2 record of the result); the model classified screens into low/medium/high aesthetic bands on a small five-case demonstration (reported in an ACM TOCHI survey of the field).
- **Limitations:** weight = area only (no color, contrast, salience); the 14 measures are stipulated, equally weighted, and mutually redundant; validated on data-entry screens, not general design.

### 4.2 Bauerly & Liu — computational symmetry/balance with experiments
- **Bauerly, M., & Liu, Y. (2006). "Computational modeling and experimental investigation of effects of compositional elements on interface and design aesthetics." *Int. J. of Human-Computer Studies*, 64, 670–682** (Tier 1; paywalled, ScienceDirect). (Exact coefficient form of their balance algorithm **UNVERIFIED** in this session; the paper's existence, method, and results are verified.)
- **Method/results:** computational quantification algorithms for symmetry and balance; two experiments (N=16 each) with ratio-scale magnitude estimation against a benchmark image plus Balanced-Incomplete-Block ranking. Subjects proved adept at judging symmetry and balance in both horizontal and vertical directions; symmetric abstract images were preferred; on web pages, more element groups lowered appeal.
- A follow-up (Bauerly & Liu, "Experimental investigation of effects of balance, unity, and sequence on interface and screen design aesthetics") confirmed balance, unity, and sequence as the strongest contributing measures.

### 4.3 Zen & Vanderdonckt — the balance formula that failed, then got fixed
- **Zen, M., & Vanderdonckt, J. (2016). "Assessing User Interface Aesthetics Based on the Inter-Subjectivity of Judgment." *Proc. 30th BCS HCI Conference*, 1–12. DOI: 10.14236/ewic/HCI2016.25** (Tier 1; open access via BCS eWiC).
- **Experiment:** 15 participants × 10 real web UIs × paired comparisons (45 per metric) vs. the QUESTIM web service computing Ngo-style metrics semi-automatically.
- **Result:** symmetry, proportion, and simplicity formulas correlated positively with human judgment — **but Ngo's balance formula did not correlate at all**. The authors then defined a **new balance formula decomposing balance into horizontal and vertical balances**, which re-established the correlation.
- **Why it matters:** a clean, preregistered-style demonstration that a plausible balance formula can be *entirely* misaligned with perception — and that the fix was structural (axis decomposition), not parameter tuning. (The exact revised formula is in the conference paper; the appendix page confirms the decomposition approach.)

### 4.4 Related interface-aesthetics work (verified pointers)
- **Zhou et al.'s "visual dominance"** (as cited in Zhang & Xue, 2025): the interface split into four quadrants with fixed attentional weights — upper-left 33%, upper-right 28%, lower-left 23%, lower-right 16% — mirroring the F-shaped reading pattern. (Original paper not independently re-verified here.)
- **Altaboli, A., & Lin, Y. (2011). "Investigating effects of screen layout elements on interface and screen design aesthetics." *Advances in Human-Computer Interaction*, 2011, 659758** (Tier 1; open access, Hindawi). Found correlations between objective layout measures (symmetry, density, balance family) and subjective aesthetics — supporting that *some* aspects of perceived aesthetics are objectively capturable.
- **Lai et al.** applied Bauerly & Liu's symmetry/balance measures to automatic text-over-image placement, with strong agreement to subjective ratings on color and monochrome images (reported in Altaboli's dissertation).

---

## 5. Symmetry metrics (the solved sub-problem)

Mirror symmetry is the one visual-balance component with mature, benchmarked quantification:

- **Mayer, S., & Landwehr, J. R. (2018). "Quantifying Visual Aesthetics Based on Processing Fluency Theory: Four Algorithmic Measures for Antecedents of Aesthetic Preferences." *Psychology of Aesthetics, Creativity, and the Arts*, 12(4), 399–431. DOI: 10.1037/aca0000187** (Tier 1; paywalled, APA). Four algorithmic measures (simplicity, **symmetry**, contrast, self-similarity) derived from processing-fluency theory, validated on 620 abstract digital artworks and landscape photographs. The symmetry measure (implemented in the open **imagefluency** R package — Tier 2 docs): **mirror the image, compute pixel correlation with the original, take the maximum over mirror-axis shifts of ±5%** (the perceptual axis need not be exactly central); color images scored per-channel then averaged. Score 0–1.
- **CNN-filter symmetry** (*Symmetry*, 2016, 8(12), 144; https://mdpi.com/2073-8994/8/12/144 — Tier 1, open access): symmetry S = 1 − A over CNN filter responses at layer l; correlation with 20 human raters' left–right symmetry judgments rose from **0.80 to 0.90** using higher-layer (more abstract) filters, on 300 album covers — outperforming a pixel-intensity baseline.
- **The 13-method benchmark** (*Symmetry*, 2026, 18(8), 1355; https://www.mdpi.com/2073-8994/18/8/1355 — Tier 1, open access): 13 scorers recast in one template (representation → comparison → aggregation) and tested on ~3,950 axis judgments across nine datasets. Findings: frozen deep features win, but a **tuned classical HOG descriptor trails by only 0.03 skill while running ~300× faster on CPU**; discrimination lives in **mid-scale oriented features**. Methods benchmarked include **PixCorr** (global cosine correlation of image vs. its mirror), **SlideWin** (Pearson correlation of the two reflected halves at the candidate axis, overlap-weighted), **EROS** (Smith & Jenkinson: per-row even/odd intensity-profile energies about the axis, contrast-corrected), and **WBS** (weighted binary: Bauerly & Liu's perceptual measure as implemented by Gartus & Leder — mirrored foreground pixels counted with weights increasing linearly toward the axis; natural images first Otsu-thresholded).
- **Takeaway for balance:** symmetry *scoring* is essentially solved and cheap; but symmetry ≠ balance (asymmetric balance is the designer's real problem), and no benchmark of this rigor exists for *balance* scoring.

---

## 6. Visual-weight factors (what the literature agrees a weight function must include)

Scattered but convergent findings on what makes a pixel group "heavy":
- **Darkness:** dark pixels heavier than bright ones (APB's core assumption; the Scribd-era design literature agrees). DCM's black=1/white=0 is the starkest version.
- **Area/size:** element area as mass (VME's S_i; Ngo's area weights).
- **Vertical position:** upper-half content carries more weight — Corwin's 1.07 factor; the VME paper's perceived-center-above-geometric-center.
- **Horizontal position:** left-side elements read lighter, right-side heavier (hemispheric lateralization; VME paper). Left–right balance is perceptually more critical than top–bottom (McManus et al., cited in VME).
- **Attention/salience:** saliency-weighted DCM (Abeln et al., 2016); quadrant attentional weights (Zhou et al. 33/28/23/16); central hotspot (Jahanian et al., 2015).
- **What is missing:** no verified quantitative function combining **saturation, hue, lightness, area, position, and contrast** — Ali's hypothesized decomposition — into a single weight. Color is the largest unmodeled factor in every formula above.

---

## 7. Perceptual-empirical foundations (and the anti-computability evidence)

### 7.1 The experimental lineage of "mechanical" balance
- **Pierce, E. (1894). "Studies from the Harvard Psychological Laboratory (II): Aesthetics of simple forms. I. Symmetry." *Psychological Review*, 1, 483–495** (Tier 1; public-domain historical). First experiment on perceptual balance (Münsterberg's Harvard lab): participants slid a movable object along a board to the most "agreeable" position opposite a fixed object. Some placed it per mechanical balance (small object farther from center), others used pure lateral symmetry, others the golden section — individual differences in balance criteria from day one.
- **Puffer, E. D. (1903). "Studies in symmetry." *Harvard Psychological Studies*, 1, 467–539** (Tier 1b, historical monograph). Production-method experiments; found **little evidence that balance is favorable** for aesthetic appreciation — bilateral symmetry and closeness outcompeted balance as construction principles.
- **Hübner, R., & Thömmes, K. (2019). "Symmetry and Balance as Factors of Aesthetic Appreciation: Ethel Puffer's (1903) 'Studies in Symmetry' Revised." *Symmetry*, 11(12), 1468. DOI: 10.3390/sym11121468** (Tier 1; open access). Modern replication of Puffer: again **little to no evidence for balance**; participants used closeness and bilateral symmetry instead.
- **Ross, D. W. (1907). *A Theory of Pure Design: Harmony, Balance, Rhythm.* Houghton Mifflin** (Tier 1b, historical). The origin text of the mechanical-balance analogy that all center-of-mass models formalize.
- **McManus, I. C., Edmondson, D., & Rodger, J. (1985). "Balance in pictures." *British Journal of Psychology*, 76, 311–324. DOI: 10.1111/j.2044-8295.1985.tb01955.x** (Tier 1; paywalled). Early modern experimental work on balance in pictures (cited as foundational in the Puffer-replication reference list).
- **Locher, P. J., Gray, S., & Nodine, C. (1996). "The structural framework of pictorial balance." *Perception*, 25, 1419–1436. DOI: 10.1068/p251419** (Tier 1; paywalled). Formalized pictorial balance assessment from the distribution of visual mass around Arnheim's structural skeleton axes.

### 7.2 Where the formulas break: picture-type dependence
- **Gershoni, S., & Hochstein, S. (2011). "Measuring pictorial balance perception at first glance using Japanese calligraphy." *i-Perception*, 2(6), 508–527. DOI: 10.1068/i0472aap** (Tier 1; open access). First-fixation balance on calligraphy depends on **different visual features than the APB**; the APB completely failed to predict balance ratings.
- **Fillinger, M. G., & Hübner, R. (2018). "The relations between balance, prototypicality, and aesthetic appreciation for Japanese calligraphy." *Empirical Studies of the Arts*. DOI: 10.1177/0276237418805656** (Tier 1; paywalled, SAGE). APB and DCM both failed on calligraphies; balance ratings were **unrelated to liking**; prototypicality dominated aesthetic appreciation, and DCM related to liking only for less-prototypical works after controlling for it.
- **Hübner, R., & Fillinger, M. G. (2019). "Perceptual Balance, Stability, and Aesthetic Appreciation: Their Relations Depend on the Picture Type." *i-Perception*, 10, 1–17. DOI: 10.1177/2041669519856040** (Tier 1; open access). Two conclusions: (1) people sometimes apply a concept of balance (e.g. *stability* on the vertical axis — preferring weight in the lower half) that APB/DCM do not capture; (2) for complex pictures, balance is one small factor among many, and its effect can vanish. Also notes Pierce's (1894) early observation that balance applies mainly horizontally while stability governs the vertical.
- Supporting that the visual system doesn't even compute centers of mass reliably: **center-of-mass estimation for multi-body displays is error-prone** (Friedenberg's two-body/three-body studies: *Attention, Perception & Psychophysics*, 64, 531; *Open Behavioral Science Journal*, 2, 13 — Tier 1, per the Konstanz reference list).

### 7.3 The theoretical ceiling: why a stimulus-side formula may be impossible in principle
- **Reber, R., Schwarz, N., & Winkielman, P. (2004). "Processing fluency and aesthetic pleasure: Is beauty in the perceiver's processing experience?" *Personality and Social Psychology Review*, 8(4), 364–382. DOI: 10.1207/s15327957pspr0804_3** (Tier 1; paywalled, SAGE; PMID 15582859). Aesthetic pleasure is a function of the perceiver's processing dynamics — the more fluently a stimulus is processed, the more it is liked; symmetry, contrast, prototypicality work *through* fluency. Crucially: **beauty is grounded in the perceiver's processing experience, only in part a function of stimulus properties.** Any formula over pixels alone leaves the perceiver term unmodeled.
- **McManus, I. C., Cook, R., & Hunt, A. (2010). "Beyond the Golden Section and Normative Aesthetics: Why Do Individuals Differ so Much in Their Aesthetic Preferences for Rectangles?" *Psychology of Aesthetics, Creativity, and the Arts*, 4(2), 113–126. DOI: 10.1037/a0017316** (Tier 1; paywalled, APA). Weak population preferences but **strong, stable, statistically robust, and highly varied individual preferences**. A single normative formula cannot simultaneously predict the population mean and the individual — the target of an "exact formula" is ill-defined.

---

## 8. The honest assessment: what would it take to derive an exact formula?

**Status: no exact formula exists.** The field has (a) one failed exact formula (Birkhoff), (b) several validated *partial* models (DCM family, APB, VME) that work on restricted stimulus classes, and (c) one literal closed-form "balance equation" (Corwin) that is an unreviewed preprint defining a single point (perfect balance), not a general function.

**The precise gap — four unsolved sub-problems:**

1. **The weight function w.** Every model needs w(pixel group), and none has a validated one. The literature's proxies — darkness (APB, DCM), area (VME, Ngo), saliency (Abeln, Thömmes & Hübner), quadrant attention weights (Zhou et al.) — are each one-dimensional. Ali's hypothesized decomposition (weight from saturation, hue, lightness, area, position, contrast, and their interactions) is the correct shape of the answer, but each factor's functional form, the interaction terms, and the combination rule are all unidentified. **This is the single biggest blocker.**
2. **The reference point and its anisotropies.** Geometric center vs. perceived center (slightly above center; Corwin's 1.07 upper-half factor is unreplicated); left/right vs. top/bottom treated asymmetrically by the visual system (McManus et al.; Wilson & Chatterjee's horizontal-dominant betas; hemispheric lateralization effects). No model derives these from principle — they are fitted constants.
3. **Generalization across picture types.** DCM/APB explain up to 68%/86% of variance on geometric patterns and fail on calligraphy; balance ratings decouple from liking on complex images (Hübner & Fillinger, 2019); people substitute *stability* for *balance* on the vertical axis. A general formula must model picture-type and semantic context, not just pixels.
4. **The perceiver term.** Processing fluency (Reber et al., 2004), expertise (painters vs. laypeople in Corwin; Puffer replication), and stable individual differences (McManus et al., 2010) put a ceiling on any stimulus-side formula. An "exact" formula would need a perceiver parameter — at which point it is no longer a formula *of the image*.

**What a derivation program would look like:** (i) psychophysically calibrate w over the full factor set (saturation × hue × lightness × area × position × contrast) with conjoint measurement, not one-factor proxies; (ii) identify the reference point and anisotropies from production/adjustment experiments (Pierce/Puffer paradigm, modernized); (iii) test the resulting equation across picture types (patterns → calligraphy → photographs → interfaces) with preregistered generalization criteria; (iv) bound the perceiver term via fluency/individual-difference covariates. Until (i) is done, every "balance formula" is a mechanics equation with the mass left blank.

---

## 9. Two-tier bibliography

### Tier 1 — peer-reviewed papers (DOI + access)
1. Abeln, J., Fresz, L., Amirshahi, S. A., McManus, I. C., Koch, M., Kreysa, H., & Redies, C. (2016). Preference for well-balanced saliency in details cropped from photographs. *Front. Hum. Neurosci.*, 9, 704. DOI: 10.3389/fnhum.2015.00704 — open access.
2. Altaboli, A., & Lin, Y. (2011). Investigating effects of screen layout elements on interface and screen design aesthetics. *Adv. Hum.-Comput. Interact.*, 2011, 659758 — open access (Hindawi).
3. Bauerly, M., & Liu, Y. (2006). Computational modeling and experimental investigation of effects of compositional elements on interface and design aesthetics. *Int. J. Hum.-Comput. Stud.*, 64, 670–682 — paywalled (ScienceDirect).
4. Eysenck, H. J. (1941). The empirical determination of an aesthetic formula. *Psychol. Rev.*, 48, 83. DOI: 10.1037/h0062483 — paywalled (APA).
5. Eysenck, H. J. (1968). An experimental study of aesthetic preference for polygonal figures. *J. Gen. Psychol.*, 79(1), 3–17. DOI: 10.1080/00221309.1968.9710447 — paywalled (T&F).
6. Fillinger, M. G., & Hübner, R. (2018). The relations between balance, prototypicality, and aesthetic appreciation for Japanese calligraphy. *Empir. Stud. Arts*. DOI: 10.1177/0276237418805656 — paywalled (SAGE).
7. Franke, H. W. (1977). A cybernetic approach to aesthetics. *Leonardo*, 10(3), 203–206 — paywalled (MIT Press).
8. Gershoni, S., & Hochstein, S. (2011). Measuring pictorial balance perception at first glance using Japanese calligraphy. *i-Perception*, 2(6), 508–527. DOI: 10.1068/i0472aap — open access.
9. Hübner, R., & Fillinger, M. G. (2016). Comparison of Objective Measures for Predicting Perceptual Balance and Visual Aesthetic Preference. *Front. Psychol.*, 7, 335. DOI: 10.3389/fpsyg.2016.00335 — open access.
10. Hübner, R., & Fillinger, M. G. (2019). Perceptual Balance, Stability, and Aesthetic Appreciation: Their Relations Depend on the Picture Type. *i-Perception*, 10, 1–17. DOI: 10.1177/2041669519856040 — open access.
11. Hübner, R., & Thömmes, K. (2019). Symmetry and Balance as Factors of Aesthetic Appreciation: Ethel Puffer's (1903) "Studies in Symmetry" Revised. *Symmetry*, 11(12), 1468. DOI: 10.3390/sym11121468 — open access.
12. Hübner, R., & Ufken, E. S. (2023). On the beauty of vases: Birkhoff's aesthetic measure versus Hogarth's line of beauty. *Front. Psychol.*, 14. DOI: 10.3389/fpsyg.2023.1114793 — open access.
13. Jahanian, A., Vishwanathan, S. V. N., & Allebach, J. P. (2015). Learning visual balance from large-scale datasets of aesthetically highly rated images. *Proc. SPIE 9394*, 93940Y. DOI: 10.1117/12.2084548 — paywalled (SPIE).
14. Javid, M. A. J., Blackwell, T., Zimmer, R., & Al-Rifaie, M. M. (2016). Correlation between Human Aesthetic Judgement and Spatial Complexity Measure. *Proc. EvoMUSART 2016* (Springer LNCS). arXiv:1707.06510 — arXiv copy open.
15. Ke, Y., Tang, X., & Jing, F. (2006). The Design of High-Level Features for Photo Quality Assessment. *Proc. IEEE CVPR 2006*, 1, 419–426. DOI: 10.1109/CVPR.2006.303 — paywalled (IEEE).
16. Locher, P. J., Gray, S., & Nodine, C. (1996). The structural framework of pictorial balance. *Perception*, 25, 1419–1436. DOI: 10.1068/p251419 — paywalled (SAGE).
17. Mayer, S., & Landwehr, J. R. (2018). Quantifying Visual Aesthetics Based on Processing Fluency Theory: Four Algorithmic Measures for Antecedents of Aesthetic Preferences. *Psychol. Aesthet. Creat. Arts*, 12(4), 399–431. DOI: 10.1037/aca0000187 — paywalled (APA).
18. McManus, I. C., Edmondson, D., & Rodger, J. (1985). Balance in pictures. *Br. J. Psychol.*, 76, 311–324. DOI: 10.1111/j.2044-8295.1985.tb01955.x — paywalled (Wiley).
19. McManus, I. C., Cook, R., & Hunt, A. (2010). Beyond the Golden Section and Normative Aesthetics: Why Do Individuals Differ so Much in Their Aesthetic Preferences for Rectangles? *Psychol. Aesthet. Creat. Arts*, 4(2), 113–126. DOI: 10.1037/a0017316 — paywalled (APA).
20. McManus, I. C., Stöver, K., & Kim, D. (2011). Arnheim's Gestalt theory of visual balance: Examining the compositional structure of art photographs and abstract images. *i-Perception*, 2, 615–647. DOI: 10.1068/i0445aap — open access.
21. Moon, P., & Spencer, D. E. (1944). Aesthetic measure applied to color harmony. *JOSA*, 34, 234 — paywalled (Optica).
22. Ngo, D. C. L., Teo, L. S., & Byrne, J. G. (2003). Modelling interface aesthetics. *Inf. Sci.*, 152, 25–46. DOI: 10.1016/S0020-0255(02)00404-8 — paywalled (ScienceDirect).
23. Pierce, E. (1894). Studies from the Harvard Psychological Laboratory (II): Aesthetics of simple forms. I. Symmetry. *Psychol. Rev.*, 1, 483–495 — public domain (historical).
24. Reber, R., Schwarz, N., & Winkielman, P. (2004). Processing fluency and aesthetic pleasure: Is beauty in the perceiver's processing experience? *Pers. Soc. Psychol. Rev.*, 8(4), 364–382. DOI: 10.1207/s15327957pspr0804_3 — paywalled (SAGE).
25. Redies, C., Bartho, R., Koßmann, L., Spehar, B., Hübner, R., Wagemans, J., & Hayn-Leichsenring, G. U. (2025). A toolbox for calculating quantitative image properties in aesthetics research. *Behav. Res. Methods*, 57(4), 117. DOI: 10.3758/s13428-025-02632-3 — open access.
26. Thömmes, K., & Hübner, R. (2018). Instagram Likes for Architectural Photos Can Be Predicted by Quantitative Balance Measures and Curvature. *Front. Psychol.*, 9. DOI: 10.3389/fpsyg.2018.01050 — open access.
27. Wilson, A., & Chatterjee, A. (2005). The assessment of preference for balance: Introducing a new test. *Empir. Stud. Arts*, 23(2), 165–180. DOI: 10.2190/B1LR-MVF3-F36X-XR64 — paywalled (SAGE).
28. Zen, M., & Vanderdonckt, J. (2016). Assessing User Interface Aesthetics Based on the Inter-Subjectivity of Judgment. *Proc. 30th BCS HCI Conf.*, 1–12. DOI: 10.14236/ewic/HCI2016.25 — open access (BCS eWiC).
29. Zhang, X., & Xue, C. (2025). Visual Moment Equilibrium: A Computational Cognitive Model for Assessing Visual Balance in Interface Layout Aesthetics. *Symmetry*, 18(1), 41. DOI: 10.3390/sym18010041 — open access.
30. Symmetry 8(12):144 (2016) — CNN-filter left–right mirror symmetry measure; correlation 0.80→0.90 with human symmetry ratings. https://mdpi.com/2073-8994/8/12/144 — open access. (Authors per journal record; not individually re-verified here.)
31. Symmetry 18(8):1355 (2026) — "Classical Versus Deep Mirror-Symmetry Scoring: A Benchmark of Thirteen Methods." https://www.mdpi.com/2073-8994/18/8/1355 — open access. (Authors per journal record; not individually re-verified here.)

### Tier 1b — foundational scholarly monographs (books)
- Birkhoff, G. D. (1933). *Aesthetic Measure.* Harvard University Press, Cambridge, MA. (No DOI; widely catalogued.)
- Moles, A. A. (1958). *Théorie de l'information et perception esthétique.* Paris: Flammarion. (Eng. trans. 1966, Univ. of Illinois Press.)
- Arnheim, R. (1954). *Art and Visual Perception: A Psychology of the Creative Eye.* Univ. of California Press. (The structural-skeleton / visual-weight theory underlying APB, DCM, and Jahanian et al.)
- Ross, D. W. (1907). *A Theory of Pure Design: Harmony, Balance, Rhythm.* Houghton Mifflin, Boston. (Origin of the mechanical-balance analogy.)
- Puffer, E. D. (1903). Studies in symmetry. *Harvard Psychological Studies*, 1, 467–539. (Historical monograph series.)

### Preprints (flagged — not peer-reviewed)
- Corwin, D. M. "Pictorial balance is a bottom-up aesthetic property mediated by eye movements…" *bioRxiv*, DOI: 10.1101/2020.05.26.104687 — open. (The only literal closed-form "balance equation" found; see §2.5 for caveats.)

### Tier 2 — informed non-academic sources (implementation records, clearly marked)
- imagefluency R package documentation (Mayer/CRAN): documents the img_symmetry algorithm (max over ±5% axis shifts; per-channel maxima then weighted average) implementing Mayer & Landwehr (2018). https://rdrr.io/cran/imagefluency/
- UCLouvain QUESTIM appendix page for Zen & Vanderdonckt (2016): documents the experiment and the horizontal/vertical balance decomposition. https://sites.uclouvain.be/questim/bhci2016/
- Altaboli, A. A. O. (2012). *Towards Developing Computational Models to Predict Perceived Visual Aesthetics of Website Interface Design.* PhD dissertation, Northeastern University. https://repository.library.northeastern.edu/files/neu:1481/fulltext.pdf — records the Ngo-model replication statistics (r = 0.94) and the 14-measure inventory.

### UNVERIFIED in this session (flagged, not presented as literature)
- Exact coefficient forms of Ngo et al.'s (2003) BM/EM formulas and of Bauerly & Liu's (2006) balance algorithm — described above only at the verified conceptual level.
- Ke et al.'s (2006) exact balance/simplicity feature formula — cited only for the verified claim that it uses spatial distributions of color/edges/brightness.
- The original Zhou et al. "visual dominance" quadrant paper (cited via Zhang & Xue, 2025).
- Exact operational details of Locher, Gray & Nodine's (1996) framework beyond its verified title/venue/DOI and its role as the structural-skeleton formalization.

---

*End of Worker D deliverable. Companion files in this project: optical-balancing-perception.md, optical-balancing-sources.md, optical-balancing-logos.md.*
