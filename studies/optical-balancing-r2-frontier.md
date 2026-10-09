# Optical Balancing — Round 2: The Three Frontiers

**Scope.** Round 1 (`optical-balancing-study.md`) landed the master verdict: no exact general formula exists; the closest models are the center-of-mass/DCM family, Wilson & Chatterjee's APB, and Zhang & Xue's Visual Moment Equilibrium (2025); the precise gap is a validated weight function w(saturation, hue, lightness, area, position, contrast). Round 2 does not re-cover Round 1's veins (Hübner & Fillinger 2016/2019, McManus et al. 2011, Koenderink et al. 2017, Wilson & Chatterjee 2005 APB, Zhang & Xue 2025 VME, Itti-Koch-Niebur 1998, Reber et al. 2004, Palmer & Schloss 2010, Pelli et al. 2006, Leder et al. 2004). It pushes three frontiers: (1) the newest 2024–2026 literature, (2) deep saliency models as candidate weight-decomposition machinery, (3) neuroaesthetics of balance and color-science weighting studies. Every paper verified by exact-title search; DOI or stable link given for each. Sourcing discipline: Tier 1 = peer-reviewed, Tier 2 = informed non-academic (clearly marked), adjacent literature in its own section.

---

## Frontier 1 — Latest 2024–2026 papers

### 1.1 A new validated equilibrium formula: Lu, Tang & Wu (2024)

The single most formula-relevant paper of the round. Lu, Tang & Wu (2024), *Symmetry* 16(7), 883, propose an **improved equilibrium measurement formula (E_II)** for product form design. Starting from an existing equilibrium formula (E_I, which produced non-referential negative values), they add the **number of form elements** as a new parameter. Tested on five design alternatives for a bladeless fan against expert perceptual questionnaires (E_III), the improved formula's rankings correlated with expert rankings at **r = 0.986 (p < 0.01)** — the highest validation number found anywhere in this literature (Zhang & Xue's VME reached r = 0.942). Honest caveats: tiny stimulus set (5 alternatives), expert rather than lay raters, 3D product forms rather than 2D compositions, and the weight term is a fitted constant — it does not decompose weight into saturation/hue/lightness factors. But it is the first post-VME entry in the "engineered balance equation" lineage, and it validates cleanly.

### 1.2 The Hübner lab, 2025: balance preference depends on the task

- **Hübner (2025), *i-Perception* 16(6), 1–20.** Two experiments on symmetry vs. balance vs. proximity preferences. When participants *rated* precomposed pictures, they preferred positional symmetry over balance and balance over proximity; when they *produced* arrangements with movable elements, proximity dominated. The combined result: the preferred composition rule depends on the assessment method — production prompts a local perspective, evaluation a global one. For the formula question this is a further strike against any fixed stimulus-side formula: the weights people apply change with the task frame, consistent with the method-effects Round 1 already documented (Puffer 1903; McManus et al. 2010 on individual vs. population preferences).
- **Miller, Hübner & Zhang (2025), *Humanities and Social Sciences Communications* 12(1), 685.** A Chinese–German cross-cultural study of aesthetic preference universality and inference. Relevant as the newest data point on the culture-relativity of compositional weights (cf. Round 1: Chokron & De Agostini 2000; Maass et al. 2009). Full treatment belongs to a cross-cultural annex; flagged here as adjacent.

### 1.3 Lin, Song, Li & Xu (2024): EEG + SVM on balance and aesthetic judgment

*Symmetry* 16(9), 1191. Stimuli classified by symmetry, center-of-gravity, and negative-space indices; 18 participants gave dichotomous balance and aesthetic judgments with EEG recorded. Key neural findings: from **300–500 ms** post-stimulus, the aesthetic task showed stronger activation, with unbeautiful/imbalanced stimuli eliciting larger frontal negative waves and occipital positive waves; from **600–1000 ms**, beautiful stimuli produced smaller negative waves at Pz. Behaviorally, participants largely used balanced composition as their aesthetic criterion. An SVM combining compositional indices with subject data reached **99% accuracy** vs. 71% for compositional parameters alone — a direct demonstration that human-side factors dominate any stimulus-only formula. (Bridges Frontiers 1 and 3; neural details in §3.)

### 1.4 Guo, Fu & Zhu (2025): composition-aware graph neural networks

*Scientific Reports* 15(1), 36046. A Composition-Aware GNN (CGA-GNN) for packaging aesthetics: image regions become graph nodes (features from U²-Net saliency detection), edges weighted by a fused symmetry/spatial-distance/directional-alignment rule with tunable coefficients. On 1,200 annotated packaging images it beat CNN and GAT baselines (Spearman's ρ = 0.714). This is the newest representative of the learned-aesthetics line — and note the architecture's implicit admission: even the neural net needs hand-coded compositional priors (symmetry, distance, alignment) as edge weights. No weight decomposition into color factors; the learned coefficients are fitted, not derived.

### 1.5 Net assessment for the formula question

The 2024–2026 window produced **one new engineered formula (Lu et al., validated at r = 0.986 on a narrow task), one new method-effect on balance preference (Hübner 2025), one EEG+computational study (Lin et al. 2024), and one composition-aware GNN (Guo et al. 2025)**. No paper replicates or refutes DCM, APB, or VME directly — that replication work has not happened. No paper fits native factor weights simultaneously. The direction of travel is *away* from closed-form formulas and toward hybrid human-in-the-loop models.

---

## Frontier 2 — Computational saliency models as weight decomposition

Round 1 covered Itti, Koch & Niebur (1998): feature channels (color, intensity, orientation) combined into a saliency map — the formal ancestor of the reader's decomposition hypothesis. This frontier asks whether modern deep saliency models output anything usable as w(pixel group).

### 2.1 The DeepGaze lineage (state of the art, still active)

- **DeepGaze II** — Kümmerer, Wallis, Gatys & Bethge (2017), *Proc. IEEE ICCV*, pp. 4789–4798. VGG-19 features trained on object recognition, passed through a learned readout network to predict fixations; introduced the information-gain metric that separates model, map, and metric (cf. Kümmerer et al. 2015/2018).
- **DeepGaze IIE** — Linardos, Kümmerer, Press & Bethge (2021), *Proc. IEEE/CVF ICCV*, pp. 12919–12928. Swaps VGG-19 for ResNet-50 backbones and combines several backbones in a principled way to fix overconfidence; the explicit lesson is **calibration**: raw deep-feature weights overpredict, and the fix is ensembling, not a better factor theory.
- **DeepGaze III** — Kümmerer, Bethge & Wallis (2022), *Journal of Vision* 22(5), 7. Moves from static maps to **scanpath** prediction: where the eyes go next, conditioned on fixation history. The model adds oculomotor biases and task history — the architecture drifts *away* from pure pixel-weighting toward behavioral state.
- **DeepGaze MSDB** — Kümmerer, Khanuja & Bethge (2025), *Proc. IEEE/CVF ICCV 2025*. Models **saliency dataset bias** itself. The frontier of the field is now about the measurement instrument, not the visual factors — telling for anyone hoping deep saliency will deliver clean factor weights.
- **UNISAL** — Droste, Jiao & Noble (2020), *Proc. ECCV*. Unified image-and-video saliency in one lightweight model. Listed here as the representative efficient architecture; same verdict applies.

**What these architectures actually learn.** Every one of them is a backbone (object-recognition features) + readout network (learned per-channel combination) + explicit **center-bias prior** added by hand. The readout weights are real numbers multiplying deep feature channels — formally the same *shape* as a weight decomposition — but the channels are uninterpretable (they are ImageNet filters, not hue/saturation/lightness), the weights are fit to gaze data, and the center-bias term is a fitted prior, not a derived one. DeepGaze II's own analysis ("understanding low- and high-level contributions") showed high-level object features dominate low-level contrast — the network rediscovers what Kandemir et al. found behaviorally (below).

### 2.2 The bridge: papers that connect saliency to balance or visual weight

- **Kandemir, Zhou, Li & Wang (2017), *Proc. Thematic Workshops of ACM Multimedia 2017*, pp. 26–34 — the most important saliency paper for this project.** It is the only work found that *literally implements the reader's hypothesis in computational form*: collect human-marked visual centers for photos (symmetric, dynamically balanced, imbalanced); compute the center-of-mass of each visual-feature type (saliency map, human detections, dominant vanishing points, …); then fit a **linear regression** predicting the human visual center from the per-feature-type centers. Result: high-level cues (humans, vanishing points) add statistically significant predictive power *on top of* saliency maps. This is w(pixel group) decomposed by feature type with empirically fit coefficients — the closest any literature comes to the hypothesized formula, and its message is double-edged: the decomposition works, but saliency alone is insufficient and the semantic terms are doing heavy lifting.
- **Tu et al. (2020), *Proc. AAAI* 34(7). "Image Cropping with Composition and Saliency Aware Aesthetic Score Map."** Learns a pixel-wise *aesthetic score map* shared across candidate crops: the same region gets different scores at different relative positions, and salient regions get more position-sensitive scores. This is the closest thing in the literature to a learned w(pixel group) that is explicitly position- and saliency-aware — but it is trained for crop ranking, not balance, and its weights are uninterpretable network parameters.
- **Cheng, Lin & Allebach (2022), *Proc. IEEE/CVF WACV*, pp. 1–9. "Re-Compose the Image by Evaluating the Crop on More Than Just a Score."** Extends the idea with an explainable 10-layer aesthetic score map: each layer shows how saliency position relative to the crop contributes to the score. Same verdict: learned pixel weights exist, interpretable factor decomposition does not.
- **Zhang, Niu & Zhang (2021), *Proc. BMVC*. "Image Composition Assessment with Saliency-augmented Multi-pattern Pooling" (SAMP-Net; arXiv:2104.03133).** First composition-assessment dataset (CADB, professional rater scores) plus a network that pools features over composition patterns (rule-of-thirds grids, diagonals, symmetry partitions) augmented with saliency maps, and predicts per-pattern importance weights. The per-pattern weights are the nearest neighbor of "balance coefficients" in deep learning — but they are pattern-level, not pixel-group-level, and again uninterpretable as color factors.

### 2.3 Verdict on saliency-as-w

Modern saliency models **do** output pixel-group weight maps (fixation probability densities, aesthetic score maps) — so the *form* w(pixel group) exists and is computable. What none of them provides is the *decomposition* into native factor values: no model factors its map into saturation × hue × lightness × area × position × contrast with validated coefficients. The learned weights live in deep-feature space, are fit to gaze or rating data, and every architecture carries hand-inserted priors (center bias) that do exactly what fitted constants did in the classical formulas. Kandemir et al. (2017) remains the cleanest empirical decomposition — and it says high-level semantic features are mandatory terms in the equation.

---

## Frontier 3 — Neuroaesthetics of balance + color-science weighting

### 3.1 Neural correlates of perceived balance

- **Lin et al. (2024)** (see §1.3): the only recent study recording brain activity *during balance judgments* on the same stimuli as aesthetic judgments. The 300–500 ms frontal-negativity/occipital-positivity signature for imbalanced+unbeautiful stimuli and the shared early processing stage for both tasks suggest balance evaluation is an early, pre-semantic pass — consistent with Gershoni & Hochstein (2011, Round 1: balance computed at first glance). The 600–1000 ms Pz effect for beauty suggests the aesthetic verdict is a later, separate integration.
- **Iosa, Lucia & Salera (2025), *European Journal of Neuroscience* 61(8), e70119.** Perspective review applying Gibson's ecological approach to neuroaesthetics: symmetry and the golden ratio as internalized environmental invariants (gravity, bilateral bodies). Proposes that balance/symmetry preferences are kinetic-ecological rather than purely visual — i.e., the "weight" metaphor may be grounded in the body's experience of gravity. A theoretical reframe worth the reader's attention: it relocates the formula question from pixel space to embodied space.
- **Lucia, Salera, Zivi, Iosa & Pecchinenda (2024), *Symmetry* 16(9), 1168.** Eye-tracking on symmetry and golden ratio in abstract art — gaze behavior as the physiological trace of balance processing. Adjacent to the neural question; included as Tier 1 eye-tracking evidence.

Net: no fMRI study of compositional balance itself was found in 2024–2026; the neural evidence is EEG (Lin et al.) and theoretical (Iosa et al.). The neural record so far supports **early, fast, preattentive balance computation** — which is compatible with a formula, but also with a hardwired heuristic that no closed form will capture cleanly.

### 3.2 Color science: hue/saturation/lightness contributions to weight, heaviness, size, attention

- **Peng, Tong, Xu, Jiang & Huang (2022), *Frontiers in Neuroscience* 16.** Simultaneous *saturation* contrast and perceived heaviness: a color patch on a desaturated background is judged visually heavier than the same patch on a saturated background — **persisting across all six hues tested** (red, orange, yellow, green, blue, purple). ERP data: the matched (pale-background/heaviness-positive) condition showed smaller N2 (less perceptual conflict) and larger P3 (more decision confidence). Two findings matter for the decomposition: (a) saturation acts *relationally* (figure vs. ground), not as an intrinsic pixel value — a direct hit on the strong form of the native-values hypothesis; (b) the heaviness effect has a neural signature at 200–400 ms (N2), i.e., early perceptual, not late cognitive.
- **Liu & Yang (2025), *Psychology & Marketing* 43, 692–705.** Product–background *hue* contrast and perceived size: across five studies plus two supplementary experiments, higher product-background color contrast consistently increased perceived size, via boundary clarity → processing fluency. Extends the Hagtvedt & Brasel (2017) saturation→size chain from Round 1 into the figure-ground domain. For the formula: position/contrast terms interact with color terms — they are not separable multiplicative factors.
- **Teixeira, Martins, Brito-Costa & Abbasi (2026), *Symmetry* 18(1), 76.** Eye-tracking (n=30, 120 Hz): warm highly-saturated colors (yellow fastest at 0.65 s) accelerate initial attentional capture; black backgrounds slowest (1.75 s) — but the pattern *reverses* for sustained processing, where high luminance contrast (white-on-black) wins. The authors stress hue, saturation, and luminance were naturally confounded and cannot be causally separated in their design. This is the honest state of the art on the attention side: the three color dimensions co-vary in every ecologically valid stimulus, which is precisely why no study has fit them simultaneously (Round 1, gap 1).

### 3.3 What this adds to the factor decomposition

Three sharpenings: (1) saturation's contribution to weight is **relational** (Peng et al. 2022) — figure-vs-ground, not a pixel property; (2) color effects on size/weight run through **processing fluency** (Liu & Yang 2025), the Reber et al. (2004) mechanism from Round 1, not through a fixed weight coefficient; (3) hue/saturation/luminance **cannot be cleanly separated** in attention studies (Teixeira et al. 2026) — the non-separability is empirical, not just a failure of experimental design. All three cut against fixed native values and for contextual, relational weights.

---

## Two-tier bibliography (Round 2 additions)

### Tier 1 — peer-reviewed (all verified by exact-title search)

1. Cheng, Y., Lin, Q. & Allebach, J. P. (2022). Re-Compose the Image by Evaluating the Crop on More Than Just a Score. *Proc. IEEE/CVF Winter Conf. on Applications of Computer Vision (WACV)*, pp. 1–9. https://openaccess.thecvf.com/content/WACV2022/html/Cheng_Re-Compose_the_Image_by_Evaluating_the_Crop_on_More_Than_WACV_2022_paper.html
2. Droste, R., Jiao, J. & Noble, J. A. (2020). Unified Image and Video Saliency Modeling (UNISAL). *Proc. European Conf. on Computer Vision (ECCV)*. (Listed on MIT/Tübingen Saliency Benchmark.) http://saliency.tuebingen.ai/results.html
3. Guo, X., Fu, S. & Zhu, D. (2025). Aesthetic quality evaluation of packaging design with graph neural networks and composition features. *Scientific Reports, 15*(1), 36046. https://doi.org/10.1038/s41598-025-20046-1
4. Hübner, R. (2025). Preference for symmetry, balance, or proximity in picture aesthetics depends on the method of evaluation. *i-Perception, 16*(6), 1–20. https://doi.org/10.1177/20416695251381548
5. Iosa, M., Lucia, M. P. & Salera, C. (2025). A Kinetic Ecological Approach to Beauty Perception: A Perspective Review on the Case of Symmetry and the Golden Ratio. *European Journal of Neuroscience, 61*(8), e70119. https://doi.org/10.1111/ejn.70119
6. Kandemir, B., Zhou, Z., Li, J. & Wang, J. Z. (2017). Beyond Saliency: Assessing Visual Balance with High-level Cues. *Proc. Thematic Workshops of ACM Multimedia 2017*, pp. 26–34. (Peer-reviewed workshop paper; no DOI located — verify via ACM DL.) http://InfoLab.Stanford.EDU/~wangz/project/imsearch/Aesthetics/ACMMMW17A/
7. Kümmerer, M., Bethge, M. & Wallis, T. S. A. (2022). DeepGaze III: Modeling free-viewing human scanpaths with deep learning. *Journal of Vision, 22*(5), 7. https://doi.org/10.1167/jov.22.5.7
8. Kümmerer, M., Khanuja, H. & Bethge, M. (2025). Modeling Saliency Dataset Bias (DeepGaze MSDB). *Proc. IEEE/CVF Int. Conf. on Computer Vision (ICCV)*. https://openaccess.thecvf.com/content/ICCV2025/html/Kummerer_Modeling_Saliency_Dataset_Bias_ICCV_2025_paper.html
9. Kümmerer, M., Wallis, T. S. A., Gatys, L. A. & Bethge, M. (2017). Understanding Low- and High-Level Contributions to Fixation Prediction (DeepGaze II). *Proc. IEEE Int. Conf. on Computer Vision (ICCV)*, pp. 4789–4798. https://openaccess.thecvf.com/content_iccv_2017/html/Kummerer_Understanding_Low-_and_ICCV_2017_paper.html
10. Lin, F., Song, W., Li, Y. & Xu, W. (2024). Investigating the Relationship between Balanced Composition and Aesthetic Judgment through Computational Aesthetics and Neuroaesthetic Approaches. *Symmetry, 16*(9), 1191. https://doi.org/10.3390/sym16091191
11. Linardos, A., Kümmerer, M., Press, O. & Bethge, M. (2021). DeepGaze IIE: Calibrated prediction in and out-of-domain for state-of-the-art saliency modeling. *Proc. IEEE/CVF Int. Conf. on Computer Vision (ICCV)*, pp. 12919–12928. http://openaccess.thecvf.com/content/ICCV2021/html/Linardos_DeepGaze_IIE_Calibrated_Prediction_in_and_Out-of-Domain_for_State-of-the-Art_Saliency_ICCV_2021_paper.html
12. Liu, Y. & Yang, C. (2025). Seeing Bigger: How Product-Background Color Contrast Shapes Perception of Product Size. *Psychology & Marketing, 43*, 692–705. https://doi.org/10.1002/mar.70082
13. Lu, P., Tang, J. & Wu, F. (2024). Product Form Design and Evaluation Method Based on Improved Form Aesthetic Formula. *Symmetry, 16*(7), 883. https://www.mdpi.com/2073-8994/16/7/883
14. Lucia, M. P., Salera, C., Zivi, P., Iosa, M. & Pecchinenda, A. (2024). An eye tracking study on symmetry and golden ratio in abstract art. *Symmetry, 16*(9), 1168. https://doi.org/10.3390/sym16091168
15. Miller, C. A., Hübner, R. & Zhang, K. (2025). On the universality of aesthetic preference and inference: A cross-cultural (Chinese–German) study. *Humanities and Social Sciences Communications, 12*(1), 685. https://doi.org/10.1057/s41599-025-04806-y
16. Peng, M., Tong, Y., Xu, Z., Jiang, L. & Huang, H. (2022). How does the use of simultaneous contrast illusion on product-background color combination nudge consumer behavior? A behavioral and event-related potential study. *Frontiers in Neuroscience, 16*. https://doi.org/10.3389/fnins.2022.942901
17. Teixeira, A., Martins, P., Brito-Costa, S. & Abbasi, M. (2026). Chromatic Asymmetry in Visual Attention: Dissociable Effects of Background Color on Capture and Processing During Reading — An Eye-Tracking Study. *Symmetry, 18*(1), 76. https://doi.org/10.3390/sym18010076
18. Tu, Y., Niu, L., Zhao, W., Cheng, D. & Zhang, L. (2020). Image Cropping with Composition and Saliency Aware Aesthetic Score Map. *Proc. AAAI Conf. on Artificial Intelligence, 34*(7). https://doi.org/10.1609/aaai.v34i07.6889
19. Zhang, B., Niu, L. & Zhang, L. (2021). Image Composition Assessment with Saliency-augmented Multi-pattern Pooling (SAMP-Net). *Proc. British Machine Vision Conf. (BMVC)*. arXiv:2104.03133. https://arxiv.org/abs/2104.03133

### Tier 2 — informed non-academic (clearly marked, never standing in for papers)

- MIT/Tübingen Saliency Benchmark (Kümmerer lab) — the live leaderboard for deep saliency models, with code and metrics (IG, AUC, sAUC, NSS, CC). http://saliency.tuebingen.ai/results.html
- DeepGaze reference implementation (matthias-k/deepgaze, GitHub) — canonical code and citation list for the DeepGaze family. https://github.com/matthias-k/deepgaze
- Research Design Connections blog summary of Liu & Yang (2025) — secondary write-up of the Tier 1 paper. https://researchdesignconnections.com/blog?page=5

---

## Adjacent literature (separate section — core bibliography stays clean)

- **Hübner, R. & Thömmes, K. (2019).** Symmetry and Balance as Factors of Aesthetic Appreciation: Ethel Puffer's (1903) "Studies in Symmetry" Revised. *Symmetry, 11*(12), 1468. https://doi.org/10.3390/sym11121468 — modern replication of Puffer's production method: little to no evidence for balance, participants use closeness and bilateral symmetry instead. (Pre-2024, but the direct ancestor of Hübner 2025.)
- **Pombo, M., Aleem, H. & Grzywacz, N. M. (2023).** Multiple Axes of Visual Symmetry: Detection and Aesthetic Preference. *Symmetry, 15*(8), 1568. https://doi.org/10.3390/sym15081568 — psychophysics + computational model of multi-axis symmetry detection and its (non-universal) aesthetic valence. Relevant to the neural machinery underlying balance.
- **Hu, L. et al. (2024).** A study on color visual perception of museum exhibition space based on eye movement experiments. *Frontiers in Psychology, 15*, 1431161. https://doi.org/10.3389/fpsyg.2024.1431161 — hue/saturation attractiveness mapping via eye-tracking; saturation 69–77% and red hue maximized attractiveness.

---

## Implications for the formula question (what Round 2 changes)

1. **The strongest validation number in the literature moved.** Zhang & Xue's VME (r = 0.942, n = 15) is no longer the top: Lu, Tang & Wu's E_II correlates at r = 0.986 with expert rankings. Both are narrow-domain engineered formulas with fitted terms — the lineage is alive, but each new formula is *more* domain-bound, not more general.
2. **The task-frame problem deepened.** Hübner (2025) shows composition-rule preferences flip between production and evaluation. A formula with fixed weights cannot be right for both tasks; any future w must be parameterized by task — another term the reader's decomposition would need.
3. **Saliency gave us the form but not the factors.** Deep saliency outputs genuine pixel-group weight maps, and aesthetic score maps (Tu et al. 2020; Cheng et al. 2022) are learned w(pixel group) in all but name. But the weights are uninterpretable deep features + hand-set center-bias priors. The one honest decomposition (Kandemir et al. 2017) proves semantic features are mandatory — which is exactly where a clean pixel formula dies.
4. **Color factors are relational, not native.** Peng et al. (2022) shows saturation weight depends on figure-vs-ground contrast and survives across hues; Liu & Yang (2025) routes color effects through fluency; Teixeira et al. (2026) cannot separate hue/saturation/luminance even in a purpose-built design. The strong form of the native-values hypothesis (fixed per-factor values, universal combination) takes three more hits.
5. **The neural timeline is early.** Lin et al. (2024) puts balance-relevant ERP signatures at 300–500 ms with shared early processing for balance and aesthetic tasks — balance is computed fast and pre-semantically, then integrated later. Compatible with a formula, but equally compatible with a hardwired heuristic.

**Net:** Round 2 confirms Round 1's verdict and sharpens it. The formula program is not dead — Lu et al. (2024) and Kandemir et al. (2017) are existence proofs that *local, domain-bound* weight equations can validate strongly. What remains disconfirmed is the *universal* form: fixed native values plus a universal combination rule. The missing experiment (fitting all factors simultaneously) is still missing, and Teixeira et al. (2026) suggests it may be un-runnable in ecologically valid stimuli because the factors do not separate.

## Most important find

**Kandemir, Zhou, Li & Wang (2017), "Beyond Saliency: Assessing Visual Balance with High-level Cues."** It is the only paper in the entire literature — Round 1 included — that operationalizes the reader's hypothesis almost literally: human-marked visual centers predicted by a linear combination of per-feature-type centers of mass, with fitted coefficients per feature type. It validates the *architecture* of his idea (decomposition works; regression finds real weights) while delivering its hardest empirical lesson (saliency alone fails; high-level semantic cues are statistically mandatory terms). If he ever runs the missing experiment, this is the methodological template.
