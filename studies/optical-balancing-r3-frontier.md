# Optical Balancing — Round 3: Frontier Watch (2025–2026)

**Scope.** Round 2 (file: `optical-balancing-r2-frontier.md`) covered: Lu/Tang/Wu 2024 (E_II, r=0.986), Hübner 2025 (task-frame flip), Kandemir et al. 2017 (decomposition), the DeepGaze lineage (II/IIE/III/UNISAL/MSDB 2025), Tu 2020 + Cheng 2022 (learned aesthetic score maps), Zhang 2021 SAMP-Net, Peng et al. 2022 (saturation→heaviness ERP), Liu & Yang 2025 (hue contrast→size), Teixeira et al. 2026 (chromatic attention), Guo et al. 2025 (CGA-GNN), Lin et al. 2024 (EEG balance), Iosa et al. 2025, Lucia et al. 2024, Miller/Hübner/Zhang 2025. None of these are repeated below. Round 3 is what came after or was missed: 13 new Tier 1 papers + 2 informed Tier 2 preprints, every one verified by exact-title search. Windows checked: *i-Perception*, *Symmetry*, *Frontiers in Psychology/Neuroscience*, *Journal of Vision*, *Empirical Studies of the Arts*, *Topics in Cognitive Science*, CVPR 2025/2026, and general web search (Semantic Scholar's API rate-limited this session and was dropped; ACM MM 2025 aesthetics workshops yielded nothing citable).

---

## 1. The crown find: a standardized toolbox for every balance formula

### 1.1 Redies, Bartho, Koßmann, Spehar, Hübner, Wagemans & Hayn-Leichsenring (2025) — the Aesthetics Toolbox

Redies, C., Bartho, R., Koßmann, L., Spehar, B., Hübner, R., Wagemans, J. & Hayn-Leichsenring, G. U. (2025). A toolbox for calculating quantitative image properties in aesthetics research. *Behavior Research Methods, 57*(4), 117. https://doi.org/10.3758/s13428-025-02632-3 — **DIRECT**

The author list alone signals importance: Redies (Jena), Hübner (Konstanz), Wagemans (Leuven), Spehar (UNSW) — the four leading European labs in quantitative aesthetics — co-authoring one open-source Python toolbox (github.com/RBartho/Aesthetics-Toolbox). It implements 43 quantitative image properties, and the balance-relevant section is explicit: it standardizes the Assessment of Preference for Balance (APB; Wilson & Chatterjee 2005), the DCM center-of-mass deviation (Hübner & Fillinger 2016; McManus et al. 2011), and mirror-symmetry measures, alongside RGB/L*a*b*/HSV channel means and SDs, color entropy, RMS contrast, lightness entropy, and edge density. Validated on AVA, JenAesthetics, and random-phase images. For this project the implication is structural: APB and DCM — the two classical balance formulas Round 1 tracked — are now canonical, versioned reference implementations rather than one-off lab code. Anyone who ever runs the missing experiment (fitting all native factors simultaneously) will almost certainly compute baseline balance terms with this toolbox, which makes it the single most infrastructure-relevant publication since Kandemir et al. (2017).

---

## 2. New computational composition measurements (DIRECT-adjacent)

### 2.1 Wang, Liu & Huang (2026) — traceable formal measurement of centroid balance

Wang, X., Liu, W. & Huang, L. (2026). Traceable Symmetry-Aware Image Processing for Two-Dimensional Morphological Diagnostics in Product Concept Design: A Four-Alternative Smart-Speaker Study. *Symmetry, 18*(8), 1402. https://doi.org/10.3390/sym18081402 — **DIRECT**

This paper attacks a known weakness of the engineered-formula lineage (including Lu et al. 2024): aggregate balance scores hide which image layer produced them and how sensitive they are to rasterization choices. The authors define seven dimensionless descriptors — including silhouette reflection, **centroid balance**, light-band closure, aperture regularity, and contour compactness — computed on separate body/light-band/aperture masks of four smart-speaker alternatives, with perturbation audits (resolution resampling, one-pixel morphology, parameter perturbation). Its own literature table positions Lin et al. 2024 (balance metrics + EEG) and Lu et al. 2024 (equilibrium metric) as relatives. It does not fit color-factor weights, and it has no independent perceptual validation — but it is the first paper in this literature to demand *provenance* for formal balance measures, which is a methodological upgrade the reader's eventual formula will need.

### 2.2 Thömmes, Hübner & Hayn-Leichsenring (2025) — Center of Mass balance in a real-world arrangement task

Thömmes, K., Hübner, R. & Hayn-Leichsenring, G. U. (2025). Is There a Timeless Truth for Good Arrangement of Paintings in Art Galleries and Museums? An Experimental Investigation of the Barnes Collection. *Empirical Studies of the Arts, 43*(1), 424–450. https://doi.org/10.1177/02762374241252108 — **DIRECT**

Participants recreated Albert Barnes's gallery-wall hangings in an online production task; the authors measured visual balance as the **Center of Mass (CoM) of the wall image and its distance to the physical midline** — a DCM-family measure applied to a real-world composition problem rather than abstract dot arrays. Experiment 1 found participants spontaneously reproduced Barnes's motifs: a central focal piece, paired arrangements, and globally midline-balanced compositions; experts reproduced them better than naïfs. This is rare ecological support for the center-of-mass family: when people arrange real compositions freely, their productions land near the CoM-balanced arrangement. It bears on the formula question by validating the *position* term's form (distance of perceptual mass from the midline) in a production task — the same task frame Hübner 2025 showed otherwise distorts rule preferences, which makes the convergence with expert hanging practice all the more telling.

### 2.3 Ruan & Li (2026) — composition features (visual center + symmetry) in a fused computational framework

Ruan, Y. & Li, X. (2026). Symmetry Analysis of Aesthetic Features for Computational Support in Assessment of Art Learning Outcomes. *Symmetry, 18*(5), 811. https://doi.org/10.3390/sym18050811 — **DIRECT-adjacent**

Built on WikiArt paintings, this framework fuses three feature families: HSV color histograms plus dominant-color vectors, **compositional features** (visual-center coordinates from a graph-based saliency algorithm, salient-region area proportion, dispersion of the salient region, and SSIM-based structural symmetry), and VGG-19 Gram-matrix style features. The compositional block is notable: it operationalizes "where the visual weight sits and how spread it is" in exactly the terms the reader's hypothesis uses (position, area, plus color channels available in the same feature vector) — but the weights that fuse these features are learned for a style-discrimination task, not fitted to human balance judgments, so it remains an architecture without a formula. Relevance: this is the current closest thing to a native-factor feature set (position × area × color channels) sitting in one computational pipeline; it shows the feature-extraction half of the decomposition problem is effectively solved, while the weight-fitting half is untouched.

---

## 3. The learned-aesthetics wave, 2025–2026 (all ADJACENT, all still no decomposition)

### 3.1 FGAesQ: Yang et al. (2026, CVPR oral) — discriminative scores from relative ranks

Yang, Z., Wang, J., Zhang, Z., Xie, P., Sheng, X., Chen, P. & Li, L. (2026). Fine-grained Image Aesthetic Assessment: Learning Discriminative Scores from Relative Ranks. *Proc. IEEE/CVF CVPR 2026* (oral). arXiv:2603.03907. https://arxiv.org/abs/2603.03907 — **ADJACENT**

The authors' central claim is methodological: coarse-grained IAA models (NIMA, MUSIQ, VILA, Charm) fail on fine-grained ranking of subtly different images, and the fix is annotation by **pairwise comparisons within series** plus rank-aware training (FGAesthetics: 32,217 images in 10,028 series; FGAesQ with DiffToken, CTAlign, RankReg). Fine-tuning SOTA models with ranking loss improved fine-grained discrimination but degraded coarse-grained performance — a tradeoff the authors read as evidence that absolute-scale scores and relative judgments are different learning targets. For the missing experiment this is a directly usable prescription: if Ali ever fits native factor weights, comparative judgments (the Law of Comparative Judgment) are the annotation protocol the field's newest work converges on — ratings alone likely cannot resolve the small weight differences between factor values.

### 3.2 ArtiMuse: Cao et al. (2026, CVPR) — expert 8-attribute decomposition

Cao, S., Ma, N., Li, J., Li, X., Shao, L., Zhu, K., Zhou, Y., Pu, Y., Wu, J., Wang, J., Qu, B., Wang, W., Qiao, Y., Yao, D. & Liu, Y. (2026). ArtiMuse: Fine-Grained Image Aesthetics Assessment with Joint Scoring and Expert-Level Understanding. *Proc. IEEE/CVF CVPR 2026*. arXiv:2507.14533. https://arxiv.org/abs/2507.14533 — **ADJACENT**

ArtiMuse-10K annotates 10,000 images (design, AIGC, photography…) with eight expert-defined aesthetic attributes plus an overall score; attribute 1 is **Composition & Design** — explicitly "balance, contrast, layout aesthetics, and rhythm… dynamic focal points, unity, and harmony" — and attribute 2 is Visual Elements & Structure (color, geometry, spatial organization, illumination). This is the closest non-formal analogue of a weight decomposition the literature now contains: experts decomposing aesthetic judgment into named, scored factors with balance as its own dimension. It still yields no formula — the attributes are MLLM-produced judgments, not fitted coefficients — but it demonstrates that the field's best practice is moving *toward* explicit multi-factor structure and *away* from single holistic scores, which is exactly the direction of the reader's hypothesis.

### 3.3 Charm: Behrad, Tuytelaars & Wagemans (2025, CVPR) — composition-preserving tokenization

Behrad, F., Tuytelaars, T. & Wagemans, J. (2025). Charm: The Missing Piece in ViT fine-tuning for Image Aesthetic Assessment. *Proc. IEEE/CVF CVPR 2025*. arXiv:2504.02522. https://arxiv.org/abs/2504.02522 — **ADJACENT**

Charm is a ViT tokenization scheme that preserves **Composition**, High-resolution, Aspect ratio, and Multi-scale information (the acronym) instead of cropping/resizing; it improves aesthetic prediction up to ~8% by refusing to destroy the compositional information standard preprocessing discards. The connection to this project is indirect but instructive: the SOTA aesthetics models only work when composition survives preprocessing — composition is load-bearing information, not decoration — yet the models still cannot say *what* about the composition matters (no factor decomposition). Also noteworthy: Wagemans (Leuven aesthetics) co-authors a CVPR paper, further evidence the perception and ML communities are converging on the same problem from opposite sides.

### 3.4 JoPPO: Qiao et al. (2026, CVPR) — compositional constraints in aesthetic ranking

Qiao, Y. et al. (2026). JoPPO: Hierarchical Photography Assessment via Contrastive Joint Conditional Probabilistic Reinforcement Learning. *Proc. IEEE/CVF CVPR 2026*. http://openaccess.thecvf.com/content/CVPR2026/papers/Yang_JoPPO_Hierarchical_Photography_Assessment_via_Contrastive_Joint_Conditional_Probabilistic_Reinforcement_CVPR_2026_paper.pdf — **ADJACENT**

JoPPO trains a VLM-as-a-judge for image aesthetics with explicit compositional assessment constraints: supervised fine-tuning on a synthetic composition dataset instills compositional priors, then a contrastive probabilistic-RL stage learns joint dimension-level and overall ranking. Evaluated on aesthetics — "a task requiring nuanced understanding of multiple attributes including composition, lighting, color and geometry" — it improves ranking consistency with zero-shot generalization. Same verdict as the rest of this section: the architecture learns to *use* compositional attributes, and the attribute weights are interpretable in name only (they are RL-optimized policy parameters, not perceptual coefficients).

### 3.5 Yu (2026) — visual saliency + composition-edge fusion for design aesthetics

Yu, X. (2026). Forms and innovative applications of fine arts factors in the design of literary and artistic products. *International Journal of Engineering Systems Modelling and Simulation*. https://doi.org/10.1504/ijesms.2026.154396 — **ADJACENT**

This is the saliency-and-composition paper Round 2's framework predicts would keep appearing: an EfficientNet-based system fusing visual-saliency features with composition-edge information (structure/balance of lines, shapes, background) under weakly supervised attention, tested on two standard aesthetics datasets where it beats established deep models. The conceptual move is the same one the whole literature keeps making — saliency as the weight map, composition as the structural prior, a learned fusion between them — and the same limitation applies: the fusion weights are fitted, uninterpretable, and dataset-bound. Included as the 2026 data point confirming that the "saliency + composition" learned-aesthetics program is still expanding without producing factor decompositions.

---

## 4. Behavioral and neural evidence (FACTOR and ADJACENT)

### 4.1 Straffon, Perea-García, den Blaauwen & Kret (2026) — perceived balance as a human signature

Straffon, L. M., Perea-García, J. O., den Blaauwen, T. & Kret, M. E. (2026). Traces of Intentionality: Balance, Complexity, and Organization in Artworks by Humans and Apes. *Topics in Cognitive Science, 18*(2). https://doi.org/10.1111/tops.70022 (first published online Sept 2025) — **ADJACENT**

Participants rated abstract paintings by untrained humans vs. chimpanzees on intentionality, organization, balance, and complexity. Human-made works were rated significantly more balanced (p < .001) and more organized; a "composition" principal component (explaining 74.7% of the variance in balance, organization, and complexity) predicted preference, mediated by perceived intentionality. Two things matter for the project: (a) balance is perceptible and preference-relevant even in abstract works where semantic content is near zero — this counters the Kandemir-derived worry that *all* balance perception is semantic; (b) balance, organization, and complexity collapse into one compositional PC in human judgment, which suggests the native factors may not be as separable in the mind as the hypothesis's factor list implies.

### 4.2 Taniyama, Nihei, Minami & Nakauchi (2025) — color composition and processing fluency (P3)

Taniyama, Y., Nihei, Y., Minami, T. & Nakauchi, S. (2025). Natural color composition induces oddball P3 asymmetry associated with processing fluency. *Scientific Reports, 15*(1), 4878. https://doi.org/10.1038/s41598-025-88815-6 — **ADJACENT**

Using oddball tasks with original vs. hue-rotated paintings, the authors show P3 asymmetry — taken as a neural index of perceptual fluency — occurs only for original color compositions, meaning familiar/natural color compositions are processed more fluently. This extends the fluency mechanism (Reber et al. 2004; Liu & Yang 2025) into the neurophysiology of *color composition specifically*: the weight a color arrangement carries in aesthetic judgment runs through how fluently it is processed, and fluency here is a property of the whole composition's color statistics (cf. their earlier Sci. Rep. 2022 paper on color-statistic regularities), not of any single pixel's hue or saturation. Another vote for relational over native weights.

### 4.3 Fairbanks, Viengkham, Andersson, Baldwin, Mureika & Taylor (2025) — balance via lacunarity/fractal analysis

Fairbanks, M. S., Viengkham, C., Andersson, A., Baldwin, D., Mureika, J. R. & Taylor, R. P. (2025). A question of Jackson Pollock's balance: using lacunarity and fractal analysis to distinguish poured paintings by adults and children. *Frontiers in Physics, 13*. https://doi.org/10.3389/fphy.2025.1673780 — **ADJACENT**

Poured paintings by adults vs. children are distinguished using lacunarity and fractal analysis — "balance" operationalized as a statistical property of spatial patterning rather than a center-of-mass computation. This is a genuinely different computational formalization of pictorial balance from the CoM/APB family: balance as the *statistical homogeneity of mark distribution across scales*. For the formula question it opens a second formal lineage — one in which balance is not Σ(wᵢ·positionᵢ) = 0 but a measure of distributional evenness — and it connects naturally to the Ruan & Li finding that balanced compositions show concentrated, low-dispersion saliency.

---

## 5. Infrastructure: a dataset that makes factor studies possible

### 5.1 Lin, Op de Beeck & Wagemans (2025) — LOAD: the orthogonalized art dataset

Lin, Y., Op de Beeck, H. & Wagemans, J. (2025). Leuven Orthogonalized Art Data Set (LOAD): A multidimensional art image set for aesthetic appreciation research. *Psychology of Aesthetics, Creativity, and the Arts*. Advance online publication. https://doi.org/10.1037/aca0000791 (stimuli on OSF: https://osf.io/cufnj/) — **ADJACENT**

LOAD contains 343 Western paintings selected to fit an orthogonally balanced design across style, content (human/nonhuman), emotional valence, and liking/beauty, each annotated by 50 participants (n=301 total) on pleasure, fluency, interest, liking, emotional valence, and familiarity. Its explicit purpose is to let researchers *disentangle* dimensions that normally co-vary — the same non-separability problem Teixeira et al. 2026 identified for hue/saturation/luminance and Round 2 flagged as the likely blocker of the missing experiment. LOAD does not itself fit factor weights, and its stimuli are paintings rather than parametrically controlled compositions, but it is the first stimulus infrastructure built for exactly the kind of multi-factor decomposition the reader wants; any future weight-fitting study would be well advised to build its stimulus set on the orthogonalization principle LOAD demonstrates.

---

## Tier 1 bibliography (Round 3 additions)

1. Behrad, F., Tuytelaars, T. & Wagemans, J. (2025). Charm: The Missing Piece in ViT fine-tuning for Image Aesthetic Assessment. *Proc. IEEE/CVF CVPR 2025*. arXiv:2504.02522. https://arxiv.org/abs/2504.02522
2. Cao, S., Ma, N., Li, J., Li, X., Shao, L., Zhu, K., Zhou, Y., Pu, Y., Wu, J., Wang, J., Qu, B., Wang, W., Qiao, Y., Yao, D. & Liu, Y. (2026). ArtiMuse: Fine-Grained Image Aesthetics Assessment with Joint Scoring and Expert-Level Understanding. *Proc. IEEE/CVF CVPR 2026*. arXiv:2507.14533. https://arxiv.org/abs/2507.14533
3. Fairbanks, M. S., Viengkham, C., Andersson, A., Baldwin, D., Mureika, J. R. & Taylor, R. P. (2025). A question of Jackson Pollock's balance: using lacunarity and fractal analysis to distinguish poured paintings by adults and children. *Frontiers in Physics, 13*. https://doi.org/10.3389/fphy.2025.1673780
4. Lin, Y., Op de Beeck, H. & Wagemans, J. (2025). Leuven Orthogonalized Art Data Set (LOAD): A multidimensional art image set for aesthetic appreciation research. *Psychology of Aesthetics, Creativity, and the Arts*. Advance online publication. https://doi.org/10.1037/aca0000791
5. Qiao, Y. et al. (2026). JoPPO: Hierarchical Photography Assessment via Contrastive Joint Conditional Probabilistic Reinforcement Learning. *Proc. IEEE/CVF CVPR 2026*. http://openaccess.thecvf.com/content/CVPR2026/papers/Yang_JoPPO_Hierarchical_Photography_Assessment_via_Contrastive_Joint_Conditional_Probabilistic_Reinforcement_CVPR_2026_paper.pdf
6. Redies, C., Bartho, R., Koßmann, L., Spehar, B., Hübner, R., Wagemans, J. & Hayn-Leichsenring, G. U. (2025). A toolbox for calculating quantitative image properties in aesthetics research. *Behavior Research Methods, 57*(4), 117. https://doi.org/10.3758/s13428-025-02632-3
7. Ruan, Y. & Li, X. (2026). Symmetry Analysis of Aesthetic Features for Computational Support in Assessment of Art Learning Outcomes. *Symmetry, 18*(5), 811. https://doi.org/10.3390/sym18050811
8. Straffon, L. M., Perea-García, J. O., den Blaauwen, T. & Kret, M. E. (2026). Traces of Intentionality: Balance, Complexity, and Organization in Artworks by Humans and Apes. *Topics in Cognitive Science, 18*(2). https://doi.org/10.1111/tops.70022
9. Taniyama, Y., Nihei, Y., Minami, T. & Nakauchi, S. (2025). Natural color composition induces oddball P3 asymmetry associated with processing fluency. *Scientific Reports, 15*(1), 4878. https://doi.org/10.1038/s41598-025-88815-6
10. Thömmes, K., Hübner, R. & Hayn-Leichsenring, G. U. (2025). Is There a Timeless Truth for Good Arrangement of Paintings in Art Galleries and Museums? An Experimental Investigation of the Barnes Collection. *Empirical Studies of the Arts, 43*(1), 424–450. https://doi.org/10.1177/02762374241252108
11. Wang, X., Liu, W. & Huang, L. (2026). Traceable Symmetry-Aware Image Processing for Two-Dimensional Morphological Diagnostics in Product Concept Design: A Four-Alternative Smart-Speaker Study. *Symmetry, 18*(8), 1402. https://doi.org/10.3390/sym18081402
12. Yang, Z., Wang, J., Zhang, Z., Xie, P., Sheng, X., Chen, P. & Li, L. (2026). Fine-grained Image Aesthetic Assessment: Learning Discriminative Scores from Relative Ranks. *Proc. IEEE/CVF CVPR 2026* (oral). arXiv:2603.03907. https://arxiv.org/abs/2603.03907
13. Yu, X. (2026). Forms and innovative applications of fine arts factors in the design of literary and artistic products. *International Journal of Engineering Systems Modelling and Simulation*. https://doi.org/10.1504/ijesms.2026.154396

## Tier 2 bibliography (informed non-academic: arXiv preprints, clearly marked)

- Bethi, M. R., Jhade, S. R., Yaganti, P., Khan, M. M. & Yu, Z. (2026). Modeling Art Evaluations from Comparative Judgments: A Deep Learning Approach to Predicting Aesthetic Preferences. arXiv:2602.00394 [cs.CV]. *(Preprint, not peer-reviewed.)* Directly compares the classic handcrafted baseline — linear regression on hue, saturation, brightness, entropy, edge density, symmetry — against deep CNN features for predicting beauty/liking of paintings, and tests pairwise comparative learning (Law of Comparative Judgment) against direct rating regression. The handcrafted-factor baseline is the reader's hypothesis in miniature: if he wants to know what the old factor list can explain, this is the current benchmark of that exact comparison.
- Braun, H. C., Mukherjee, K., Gorelik, S. R. & Schloss, K. B. (2025). Affective Color Scales for Colormap Data Visualizations. arXiv:2511.14009. *(Preprint, not peer-reviewed; Schloss lab.)* Shows colormaps can keep strong lightness contrast for spatial legibility while carrying affective connotation, and finds affective connotation depends on *how often* colors appear in the image (data-dependence hypothesis). FACTOR-relevant: another demonstration that a color factor's weight is not a fixed native value but depends on its deployment statistics — the "weight" lives in the composition, not the pixel.

---

## What Round 3 changes (net assessment vs. the Round 2 verdict)

1. **The most important infrastructure event since Kandemir (2017).** The Redies et al. (2025) Aesthetics Toolbox standardizes APB, DCM, and mirror-symmetry implementations in one open package maintained by the four leading labs. The classical balance formulas are no longer lab folklore — they are reference code. Any future weight-fitting experiment starts here.
2. **The field is converging on multi-factor structure without formulas.** ArtiMuse's expert 8-attribute system (with Composition & Design = balance as its own scored dimension), FGAesQ's rank-aware training, JoPPO's compositional priors — the newest CVPR work keeps rediscovering that aesthetics must be decomposed into named factors, but none of the decompositions produce coefficients. The appetite for the reader's hypothesis is growing; the mathematics still isn't there.
3. **The missing experiment got a methodological prescription.** FGAesQ (2026) and Bethi et al. (2026) independently converge on pairwise comparative judgments over absolute ratings — the Law of Comparative Judgment — as the annotation protocol sensitive enough to resolve fine-grained differences. If the all-factors-simultaneously experiment is ever run, it should be a comparison experiment, not a rating experiment. This refines, rather than contradicts, Round 2's gap statement.
4. **Ecological support for the CoM family.** Thömmes et al. (2025) shows free gallery-wall arrangements converge on CoM-midline balance; Straffon et al. (2026) shows perceived balance survives near-zero semantic content (abstract human-vs-ape paintings). Together they blunt the two strongest anti-formula objections from Round 2 (task-dependence, semantic dominance) — partially. The Hübner task-frame problem stands; it is just no longer the whole story.
5. **Relational weights keep winning.** Taniyama et al. (2025) routes color composition through fluency at the neural level; Braun et al. (2025) makes color weight data-dependent; Straffon et al. (2026) collapses balance/organization/complexity into one principal component. Every new data point pushes the weights out of the pixel and into the composition.

**Net:** nothing in Round 3 refutes the Round 2 verdict — no paper fits native factor weights simultaneously, and the engineered-formula lineage produced no new validation number to challenge Lu et al.'s r = 0.986. What Round 3 adds is *infrastructure* (the toolbox, LOAD, the comparative-judgment prescription) and *convergence* (the field moving toward explicit factor structure). The program is better equipped than it was a year ago, and still equally unproven.

## Gaps and non-findings (worth recording)

- No new *i-Perception* 2026 paper on balance/composition was found; no *Journal of Vision* 2025–2026 paper directly on pictorial balance formulas; no citable ACM MM 2025 aesthetics-workshop paper on composition or balance surfaced. The perception journals are quiet on the formula question right now — the action is in CVPR proceedings and the quantitative-aesthetics labs' own venues.
- DeepGaze MSDB (ICCV 2025) remains the newest static-saliency milestone; no 2026 static saliency model with balance relevance was found — the saliency frontier has moved to video and foundation models (e.g., Attend to Anything, ICML 2026), which are outside this project's scope.
- No 2025–2026 replication or refutation of DCM, APB, or VME was found — the replication gap Round 2 identified is still open.

## Most important find

**Redies, Bartho, Koßmann, Spehar, Hübner, Wagemans & Hayn-Leichsenring (2025), "A toolbox for calculating quantitative image properties in aesthetics research"** (*Behavior Research Methods*). It canonicalizes the implementations of APB and DCM — the two formulas at the heart of this project — in open code from the four leading labs, and bundles the color/contrast/entropy measures the native-factor hypothesis needs as covariates. It is the single paper most likely to be cited by the eventual experiment that fits all factors at once.
