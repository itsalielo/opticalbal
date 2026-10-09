# Optical Balancing — Round 5: Frontier Sweep (newest 2026 literature)

**Sweep date:** 2026-10-09. **Worker brief:** newest 2026 papers (published after ~August 2026, or missed by earlier rounds) on visual/compositional balance measurement, interface aesthetic evaluation, composition assessment, visual weight computation.

**Venues swept:** OpenAlex/Semantic Scholar-indexed results via web search, MDPI Symmetry vols 17–18 (through 18(10)), i-Perception, Behavior Research Methods, Journal of Vision, CVPR 2026 proceedings, WACV 2026 collections, arXiv cs.CV 2026, PLOS ONE, Color Research & Application, JASE.

**Dedup vs logged corpus:** None of the items below duplicates Round 1–4 holdings (Lu/Tang/Wu 2024; Zhang & Xue VME; Yang 2025; Wang/Liu/Huang 2026 18(8):1402; Redies 2025 toolbox; Thömmes/Hübner/Hayn-Leichsenring 2025; Ruan & Li 2026 18(5):811; Lin et al. 2024 EEG; FGAesQ CVPR 2026 oral). Verified by exact-title search before reporting; DOI or stable URL given for each.

---

## TIER 1 — peer-reviewed

### 1.1 He, J. & Liu, C. (2026). Research on Composition Optimization Methods for Visual Graphic Design Styles Based on Diffusion Models. *Proceedings of the 3rd International Conference on Machine Intelligence and Digital Applications* (published 04 Sept 2026). https://doi.org/10.1145/3801438.3803130
**Authors:** Junjie He, Chen Liu — Shanghai Zhongqiao Vocational and Technical University, Shanghai.

**What it adds:** The only new closed-form composition equation found this round. They define a differentiable, learnable composition evaluator

J_comp = αB + βR + γS + δH + εD + ζN + ηA − θC

where **B = visual balance computed from the second moment of saliency maps**; R = rule-of-thirds/golden-ratio alignment; S = semantic saliency coverage (text/subject); H = CIELAB chromatic harmony consistency; D = hierarchical/perspective depth; N = normalized white-space ratio; A = CLIP-encoder aesthetic prior; C = edge crowding/clutter (subtracted). The weights α…θ are learned via channel attention/scale gating, and the evaluator is anchored to humans by paired ranking calibration on expert preference pairs: L_rank = −log σ(J_comp(x⁺) − J_comp(x⁻)). It is then injected as gradient guidance into the diffusion sampling path (ControlNet + classifier-free guidance). Validation: 500 designer-composed samples across 9 layout styles; reported +11.5% compositional aesthetic score over DDPM, +10.3% over StyleGAN.

**Verdict for the formula question:** This is the round's sharpest find. It treats visual weight *implicitly through saliency moments* (not decomposed into the six native factors — hue/saturation/lightness/area/position/contrast as separate terms), and it demonstrates exactly the "weights identifiable only up to expert-preference calibration" pattern the compute track predicted: the additive form is fixed, but the coefficients are learned, not derived. A human-anchored additive balance term — the closest thing in 2026 to a deployed descendant of the decomposition program — with the decomposition itself still refused (balance enters only as B, the second moment of a saliency map). **Tier 1 core.**

**Visual-weight treatment:** learned (saliency-moment-based, not factor-decomposed).

### 1.2 Hsiao (2026). A Methodology for Matching Colors in Product Design Using Gradient Colors and a New Aesthetic Measurement Method. *Color Research & Application* (first published 03 Feb 2026). https://doi.org/10.1002/col.70050
**What it adds:** Proposes a new aesthetic measurement formula for gradient color schemes (RGB/Pantone/Munsell integrated strips built by arithmetic progression), with eye-tracking-identified visual hotspots feeding a tricolor aesthetic measurement; validated against public perception via aesthetic questionnaire with Pearson correlation. Running shoes as the design case.

**Verdict:** A 2026 formula, but a *color-harmony* formula, not a balance one — adjacent to the problematic, useful only as evidence that the field still ships closed-form aesthetic measures when the domain is narrowed (here: tricolor gradient strips). Validated against humans (questionnaire + eye tracking), which is more than most. **Tier 1 adjacent (color).**

**Visual-weight treatment:** n/a (color measurement).

### 1.3 Ji, K., Gao, Y., Sun, L., Zheng, Y., Chen, Z., Zhang, J., Zhu, X., Tian, Y., Zhang, Z., & Zhai, G. (2026). A³: Towards Advertising Aesthetic Assessment. *CVPR 2026*. arXiv:2603.24037. PDF: https://openaccess.thecvf.com/content/CVPR2026/papers/Ji_A3_Towards_Advertising_Aesthetic_Assessment_CVPR_2026_paper.pdf
**What it adds:** A theory-driven paradigm (A³-Law) with three stages — Perceptual Attention (does it grab the eye), Formal Interest (formal composition of color and spatial layout), Desire Impact (persuasive force) — plus a 30K-image/120K-instruction-response-pair dataset with chain-of-thought rationales and a CoT-guided MLLM (A³-Align) plus benchmark (A³-Bench). Composition is evaluated as formal spatial layout inside "Formal Interest"; the 5-point rubric in the supplement scores composition alongside visual appeal, artistry, clarity.

**Verdict:** Largest 2026 human-annotated composition-assessment resource adjacent to the problematic. No equation for balance — judgments are learned by the MLLM from CoT-annotated pairs. Relevant as a *methodological* precedent (paired/ranked human aesthetic judgment at scale), not as a formula. **Tier 1 adjacent.**

**Visual-weight treatment:** learned (MLLM).

### 1.4 Cao, S., Ma, N., Li, J., Li, X., Shao, L., Zhu, K., Zhou, Y., Pu, Y., Wu, J., Wang, J., Qu, B., Wang, W., Qiao, Y., Yao, D., & Liu, Y. (2026). ArtiMuse: Fine-Grained Image Aesthetics Assessment with Joint Scoring and Expert-Level Understanding. *CVPR 2026*, pp. 15313–15322.
**What it adds:** ArtiMuse-10K dataset with expert annotations; joint scoring across 8 aesthetic attributes with explicit attribute weights (Composition & Design 0.07; Visual Elements & Structure 0.07; Technical Execution 0.08; Originality & Creativity 0.15; Theme & Communication 0.15; Emotion & Viewer Response 0.10; Overall Gestalt 0.38; plus a comprehensive evaluation), combined with MLLM-generated expert-level textual assessments. A noted positivity bias in raw MLLM evaluations was corrected with professional human annotation.

**Verdict:** Fine-grained learned assessment; composition is one weighted attribute, not decomposed and not balance-measured. Useful to the mission only as a data point on *how the field now operationalizes "composition" without measuring balance* (attribute weight 0.07, dominated by Overall Gestalt 0.38). **Tier 1 adjacent.**

**Visual-weight treatment:** learned (attribute-weighted).

### 1.5 Fang, H., Li, B., Zhou, Z., Li, M., Lai, H., Zheng, Y., Hu, B., & Chen, W. (2026). Exploring the aesthetic cognition and artistic acceptance of AIGC-generated urban sculptures: A structural equation modeling and visual content analysis approach. *PLoS ONE* 21(3): e0344501. https://doi.org/10.1371/journal.pone.0344501
**What it adds:** SEM + expert visual-content analysis of AI-generated public-sculpture imagery; among the rated dimensions, symmetry & balance drew the highest mean score (M = 4.11), marking it the dominant perceptual anchor in the set. Data public on Figshare (10.6084/m9.figshare.31260229).

**Verdict:** No equation; human ratings only. Notable for the mission as fresh 2026 evidence that when experts rate generated compositions, balance dominates the perceptual structure — a behavioral datum consistent with the lab-track hypotheses, not a formula. **Tier 1 adjacent.**

**Visual-weight treatment:** human-rated only.

### 1.6 MDAF-ViT (2026). Quantitative Aesthetic Evaluation of Visual Artworks Using Vision Transformer with Multi-Dimensional Artistic Feature Fusion. *Journal of Applied Science and Engineering (Tamkang)*. https://doi.org/10.6180/jase.202609_32.043 (received 08 Apr 2026; accepted 01 May 2026).
**Authors unconfirmed in this pass** — the journal landing page was unreachable at sweep time; only the corresponding contact email was recoverable from the PDF. Title, DOI, venue, and dates verified by exact-title search.
**What it adds:** Hierarchical ViT backbone with a Dynamic Multi-Dimensional Attention Fusion module combining handcrafted feature branches — low-level visual attributes, mid-level compositional rules (incl. composition balance), high-level semantic style — evaluated on BAID, APDDv2, JenAesthetics against CNN and ViT baselines (PLCC/SRCC/MSE).

**Verdict:** Another learned fusion system; compositional rules enter as handcrafted features fused by attention — the fusion weights are the closest thing to "factor weights," but they are learned, opaque, and never reported as numbers. **Tier 1 adjacent.**

**Visual-weight treatment:** learned (attention-fused).

---

## TIER 2 — informed non-academic / preprints (clearly separated)

### 2.1 Deng, Z., Li, L., Ji, J., Lyu, S., Xu, Z., Chen, Z., Fang, R., Bai, S., Hu, X., & Wei, J. (2026). AUV-Bench: Aesthetic Understanding and Generation Evaluation for User Interfaces. arXiv:2609.34854 (submitted 28 Sept 2026). https://arxiv.org/abs/2609.34854
HKUST (Guangzhou) + Alibaba. Eight UI aesthetic dimensions (Color, Typography, Graphics & Imagery, **Layout**, Component Consistency, Visual Style Consistency, Copy Quality, Image–Text Fit); dimension-specific calibration functions mapping model ratings to human-anchored scores; frozen-judge evaluation of generated UIs plus a pairwise win-rate complement. Preprint, not peer-reviewed. **Adjacent** — UI layout judged as one dimension among eight; no balance equation.

### 2.2 Dong, Z., Li, C., Yu, J., & Chen, H. (2026). CROP: Expert-Aligned Image Cropping via Compositional Reasoning and Optimizing Preference. arXiv:2605.12545. https://arxiv.org/abs/2605.12545
Reformulates aesthetic cropping as VLM multimodal reasoning ("analysis–proposal–decision"), explicitly reasoning over ten compositional elements (rule of thirds, center, golden ratio, horizontal, symmetric, diagonal…), with an expert-preference alignment module (SFT + DPO). 1,500 collected human votes confirm preference alignment. Preprint. **Adjacent** — compositional reasoning, no weight decomposition.

### 2.3 francismvom (2026). A Mathematical Model for the Automated Evaluation of Graphical User Interfaces. *Medium*, 18 Sept 2026. https://medium.com/@francismvom/a-mathematical-model-for-the-automated-evaluation-of-graphical-user-interfaces-a607649734e6
An 8-criterion normalized scoring model (color, contrast, typography, **balance**, proportion, consistency, alignment, spacing; each 0–1, weighted into a 100-point score). Its balance section states the most explicit decomposed visual-weight formula found anywhere this round:

visualWeightᵢ = normalizedAreaᵢ · contrastFactorᵢ · saturationFactorᵢ · salienceFactorᵢ

with the interface's visual center of mass as Σ(wᵢ·xᵢᶜ)/Σwᵢ and balanceScore = 1 − min(1, balanceDeviation), deviation normalized by the frame diagonal. Worked numerical example included. Non-academic essay; no human validation is shown (empirical calibration is mentioned only for the color criterion). **Directly on-topic for the problematic** — area × contrast × saturation × salience is a four-factor decomposition of exactly the kind the mission hypothesizes — but Tier 2: unpublished, unvalidated, and the multiplicative form is asserted, not derived.

---

## Adjacent literature (saliency models, generic aesthetic scoring) — marked section

All Tier 1 adjacent items above (§1.2–1.6) and Tier 2 §2.1–2.2 belong here. Common pattern across the 2026 crop: **composition assessment has moved to learned attribute weights and MLLM judges; nobody ships per-factor visual-weight numbers.** The ArtiMuse attribute weights (Composition & Design 0.07 vs Overall Gestalt 0.38) and AUV-Bench's 8-dimension layout scoring are the clearest 2026 instances. The diffusion paper (§1.1) is the exception that proves the rule: it keeps a closed additive form but only because a balance term defined via saliency moments was hand-specified, and even there the coefficients are learned.

## Exclusions and dead ends

- **Seredkina:** KILLED per standing order — not reopened.
- **Fukada full text:** still a dead end (print-only); one confirming line, no effort expended, per instructions.

## Gaps remaining

- MDAF-ViT author list unconfirmed (journal page unreachable during sweep; DOI + title + dates verified).
- The Medium essay's claimed "empirical calibration" covers color harmony only; its balance weights are asserted. No human-subject data anywhere in Tier 2.
- No new peer-reviewed human experiment jointly fitting ≥3 visual-weight factors appeared after August 2026 — the Morriss & Dunlap 1988 ceiling (2 factors) still stands unchallenged in the 2026 literature found.
