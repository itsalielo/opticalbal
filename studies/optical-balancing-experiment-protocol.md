# Optical Balancing — Experiment Protocol (Lab Variant, Primary)

**Status: DRAFT PROTOCOL — NOT A VALIDATED INSTRUMENT.**
This document is a design for an experiment that has never been run. Every number in it is either (a) inherited from the published spatial-balance tradition, or (b) flagged **JUDGMENT CALL** where no literature source exists. The protocol's job is to be precise enough that a lab collaborator can render the stimuli, run the sessions, and fit the model — not to claim the instrument is proven. Pilot data should precede the full run.

**Problematic under test (reader's hypothesis):** each pixel group carries a visual weight decomposable into native factor values —
w(saturation, hue, lightness, area, position, contrast).
The literature ceiling is two factors fitted jointly (Morriss & Dunlap 1988); no study has ever fit all six (see `optical-balancing-study.md` §10, `optical-balancing-r2-gaps.md`). The computational track (`optical-balancing-compute.md`) showed the design must survive three break modes: scale non-identifiability, silent interaction absorption, and reading-direction sign-flip collapse. This protocol is built around those.

**Binding decision:** LAB is the primary variant. Online is the fallback/extension (§11).

---

## 1. Hypotheses

**H1 (primary). Six-factor additive decomposition.**
The null-point of balance is explained by a per-factor weight decomposition
w(group) = A · (1 + Σ βₖ·xₖ), k ∈ {saturation, hue, lightness, position, contrast},
with area as the scale anchor (β_area ≡ 1; the computational track proved absolute
scale is unidentifiable from balance data alone — ratios only).
Per-observer random effects on all βₖ; group-level βₖ estimated with uncertainty.
*Source: the reader's hypothesis; formal ancestor Al Akkad & Gazimzyanov 2017
(additive promise, position-only — §12 of master study); method ancestor
Morriss & Dunlap 1988 (DOI 10.2190/46M2-30KP-CA57-ARQV), area-as-DV.*

**Falsification (preregistered, any one suffices):**
- (a) The additive model loses to a non-additive alternative on the factorial
  blocks (§6): ΔAIC > 10 in favor of an interaction model, or a max-rule model
  (Koenderink et al. 2018, *Vision Research* 151, 88–98) fits better.
- (b) Split-half (odd/even trials) reliability of any group-level ratio
  βₖ/β_area falls below r = .70 → the factor's "native value" is not stable
  enough to claim.

**H2 (secondary). Task-frame moderation.**
Following Hübner (2025, *i-Perception*): balance preference flips between
production and evaluation tasks. Weights fitted from the adjustment task
(production) will differ in sign or magnitude from weights fitted from an
evaluation (rating) task on the same stimulus set — specifically the position
coefficient.
*Falsification: all between-task differences |Δβₖ| < 2 SE for every factor →
no task-frame effect detected; report as failed replication of Hübner 2025.*

**H3 (secondary). Reading-direction sign flip on the position weight.**
Following Chokron & De Agostini (2000): horizontal weight preferences reverse
with reading direction. The horizontal position coefficient β_P fitted
separately for L2R-habitual vs R2L-habitual readers will differ (sign flip or
significant magnitude change); a single pooled coefficient will collapse toward
zero and leave signed structured residuals — exactly the computational track's
break (c).
*Falsification: the direction-split model does not beat the pooled model
(ΔAIC < 2) → H3 rejected; pooled estimate reported.*

**H4 (secondary). Ground-assignment contingency.**
Following Morriss & Dunlap (1987, *J. General Psychology* 114, 353–361):
lightness/value effects are background-contingent; and Parada-Castellano (2016):
weight as contrast-force-against-a-ground. The lightness weight function
β_L differs across ground conditions (gray / white / black blocks).
*Falsification: the ground-invariant model wins (ΔAIC) → value effects are
not ground-contingent in this paradigm; H4 rejected.*

---

## 2. Stimuli

### 2.1 Composition
Two filled disks on a uniform ground, centered horizontally, both on the
canvas vertical midline. Element A: fixed (position, area, color all set by
the trial). Element B: adjustable — the observer changes B's radius until the
composition feels balanced. Mirrored variants: on half the trials A is on the
right and B on the left (adjustable element alternates side, so the position
weight is not confounded with "which element is adjustable").
*Source: two-element compositions keep the null-point interpretable;
Morriss & Dunlap used color pairs; disks avoid corner/edge artifacts that
Koenderink et al. (2017) show carry their own weight.*

### 2.2 Factors and levels
All colors specified in **CIELAB (D65)**. Do NOT author in HSL/HSV:
the compute track's break (b) showed hue and lightness confound at
corr ≈ .64 when authored in HSV; independent variation must be built in
at the design stage. **JUDGMENT CALL:** saturation = C\*ab chroma,
lightness = L\*, hue = h_ab as a 4-level categorical (red ≈ 30°,
yellow ≈ 95°, green ≈ 145°, blue ≈ 265° — the replicated heaviest→lightest
ordinal, Locher et al. 2005). A circular cos/sin encoding may be tested
as a secondary model; primary is categorical.

| Factor | Levels | Notes |
|---|---|---|
| Saturation (C\*) | 20 / 45 / 70 | within-gamut at all L\* levels — generator must gamut-check; out-of-gamut level combinations are dropped from the candidate set |
| Hue (h_ab) | 30° / 95° / 145° / 265° | red, yellow, green, blue |
| Lightness (L\*) | 30 / 50 / 70 | — |
| Area (fixed element A, radius) | 32 / 48 / 64 px | B's adjusted radius is the DV, continuous 16–96 px |
| Position (eccentricity of each element) | 0.25 / 0.50 / 0.75 of canvas half-width | both elements on vertical midline; A fixed at 0.50 on its side per trial, B's eccentricity varies |
| Contrast vs ground | ΔL\* = \|L\*_element − L\*_ground\| | DERIVED, not independently set; independent variation comes from crossing L\* levels with ground blocks (gray L\*=50 / white L\*=95 / black L\*=10). This redundancy is what saved identifiability in break (b). |

### 2.3 Design logic — why not OFAT
One-factor-at-a-time stimulus sets are **blind by construction** to
interactions: the computational track showed an area×saturation
interaction is silently absorbed into the nearest additive coefficient
(+115% error on ĉ_sat) and is invisible without factorial variation.
The design therefore has three parts:
- **Core: D-optimal fractional factorial** — candidate set = full
  factorial over the 6 factors × mirror (A-left/A-right) minus
  out-of-gamut cells; select 64 trials maximizing D-efficiency for the
  additive model with all two-way interactions in the candidate model.
  **JUDGMENT CALL** on 64 (pilot-tunable 48–80).
- **Factorial block 1: area×saturation, fully crossed 3×3** (other
  factors held at mid levels, both mirrors) — the interaction-absorption
  diagnostic (break a).
- **Factorial block 2: hue×lightness, fully crossed 4×3** (both mirrors) —
  the confound diagnostic (break b).
- **Anchors (8):** symmetric trials (A ≡ B mirrored) where the correct
  null is equal areas — serve as catch/attention trials and bias checks.
- **Reliability repeats:** 20 trials repeated (2nd presentation) →
  test–retest of the adjustment DV.

Trial count per observer (Phase A, gray ground): 64 + 18 + 24 + 8 = 114
unique, +20 repeats = **134 adjustments**. At 25–35 s each ≈ 50–65 min
of task time. If pilot mean exceeds 35 s/trial, split into two sessions.
(**JUDGMENT CALL** — the session-length bound, to be set by pilot.)

### 2.4 Rendering specification
- **Canvas:** 1024 × 768 px logical, centered on display, on the ground
  color filling the full screen outside the canvas region.
- **Ground blocks:** Phase A = gray (L\*=50). Phase B (optional extension,
  §7 note) = white (L\*=95), black (L\*=10) — tests H4.
- **Anti-aliasing:** on; disk edges gamma-correct.
- **Color pipeline:** author CIELAB → convert via display ICC profile
  (built from colorimeter measurement, §4) → 8-bit RGB. Verify with
  spot measurements on at least the 4 hue × 3 L\* anchor colors;
  accept ΔE\*ab < 3, else re-profile. **JUDGMENT CALL** (tolerance).
- **Stimulus generator code** is brought by us (§10); the lab renders
  from it, never re-authors.
## 3. Procedure

### 3.1 Session flow (Phase A)
| Step | Duration | Content |
|---|---|---|
| 1. Welcome + consent | ~10 min | Experimenter script §5; written consent signed |
| 2. Vision screening | ~5 min | Ishihara plates (color vision); near acuity; exclusion on fail (§6.5) |
| 3. Setup + adaptation | ~7 min | Seating, chin rest, 5 min adaptation to display + room light |
| 4. Task instruction | ~5 min | Script §5.3; observer repeats the task back in own words (comprehension check) |
| 5. Practice | ~5 min | 5 practice trials, experimenter present, no feedback on "correctness" — only on how the controls work |
| 6. Block 1: production (adjustment) | ~30 min | ~67 trials; self-paced |
| 7. Break | 10 min | Script §5.5; observer leaves the chair |
| 8. Block 2: evaluation (ratings) | ~12 min | 24 rendered stimuli, "how balanced is this composition?" 1–7; counterbalanced order with Block 1 between subjects |
| 9. Debrief | ~5 min | Script §5.6; reading-direction + color-training questionnaire |
| **Total** | **~90 min** | Hard cap 100 min incl. breaks (eye-strain mitigation, §8) |

*Order counterbalancing tests H2. Block 1/Block 2 assignment randomized per
observer. The 24 evaluation stimuli: fixed subset spanning the design,
rendered with B at the radius the Phase-A pilot's group-median null predicts
± offsets — **JUDGMENT CALL** on construction; finalize from pilot.*

### 3.2 Trial structure (adjustment block)
1. Stimulus appears; B starts at a **randomized radius** (uniform 20–92 px)
   — randomized start defeats anchoring on the default size.
2. Observer adjusts B's radius: ←/→ keys = ±1 px (fine), Shift+←/→ = ±8 px
   (coarse). Radius constrained to [16, 96] px.
3. Observer presses **Space** to confirm. No time limit; trial auto-flags
   if >90 s (exclusion review, not auto-exclude).
4. 500 ms blank (ground color) between trials.
5. No feedback is ever given about the setting.

### 3.3 Practice trials
5 trials spanning easy (A ≡ B mirrored anchor) to typical. Experimenter
script §5.4. Purpose is control fluency, not training a criterion —
the instruction is deliberately criterion-free ("go by your immediate
visual impression").

### 3.4 Attention / catch trials
- **8 symmetric anchors** interleaved: A and B identical except mirrored.
  A calibrated observer sets equal areas; systematic deviation = bias or
  inattention.
- **20 repeats** of earlier trials: test–retest reliability of the DV.
- **No trick questions** — the task has no "right" answer except on
  anchors, and observers are told this.

### 3.5 Pacing and breaks
- Self-paced; recommended cadence communicated as "take the time you
  need, most people need about half a minute."
- Mandatory 10-min break at the midpoint (step 7); observer may request
  additional pauses — the experimenter offers one explicitly at the
  script point (§5.5) rather than waiting to be asked.
- Session aborted on observer request or visible fatigue; partial data
  retained and flagged.

---

## 4. Lab apparatus specification (PRIMARY)

Everything here is specified so the lab can either confirm they meet it
or quote the deviation. Where a number has no literature source it is
flagged **JUDGMENT CALL**.

### 4.1 Display and calibration
- Panel: ≥24″, ≥1920×1080, IPS or equivalent (stable off-axis color);
  matte or glare-controlled.
- **Calibration procedure** (per session day, before first observer):
  1. Warm up display ≥30 min.
  2. Colorimeter (e.g. X-Rite i1Display Pro / Calibrite ColorChecker —
     **JUDGMENT CALL** on model; any NIST-traceable colorimeter acceptable)
     builds an ICC profile: D65 white point, 120 cd/m² peak white,
     gamma 2.2 (sRGB EOTF), black point ≤ 0.5 cd/m².
  3. Validate: measure the 4 hue × 3 L\* anchor colors; accept
     ΔE\*ab < 3 mean, < 5 max — else re-profile. Log the validation
     report with the session data.
- *Source for the practice: CIE 15:2018 (colorimetry — the CIELAB
  definitions this protocol's color spec rests on); ISO 3664:2009
  (viewing conditions for graphic technology — nearest standard to
  display-based psychophysics; the specific numbers above are a
  **JUDGMENT CALL** adapting print-viewing practice to a
  self-luminous display).*

### 4.2 Viewing geometry
- Viewing distance: **60 cm, fixed by chin rest** (observer's nasion at
  the rest; chair height adjusted).
- Canvas 1024×768 px on a 24″ 1080p panel (0.277 mm pitch) ⇒ canvas
  ≈ 28.4 × 21.3 cm ⇒ **subtends ≈ 26.6° × 20.1°** at 60 cm.
  (**JUDGMENT CALL** — chosen so the whole composition falls well
  inside the useful field while elements stay foveally resolvable;
  ITU-R BT.500-14's 3–4 picture-heights guidance for subjective
  assessment is the nearest published anchor.)
- Screen center at observer eye height.

### 4.3 Ambient light
- Dim neutral surround: **≤64 lux** at the observer position, no direct
  light on the screen, no visible reflections; walls/hood neutral gray
  if available. Monitor is the dominant light source.
- *Nearest source: ISO 3664 ambient limits for critical monitor
  comparison; the 64-lux ceiling is a **JUDGMENT CALL**.*
- **Dropped in the online variant** (§11) — replaced by instruction +
  self-report.

### 4.4 Observer positioning and response device
- Chin rest + fixed chair (fore-aft locked after setup). **JUDGMENT CALL:**
  free head movement adds unmeasured position variance; the chin rest is
  cheap control. If the lab's ethics setup forbids chin rests, fix the
  chair and mark the floor position — record the deviation.
- Response: standard keyboard, arrow keys as in §3.2. No mouse
  (avoids Fitts-law variance in a radius-setting task — **JUDGMENT CALL**).
- 5-minute adaptation to display + room before Block 1.

---

## 5. Experimenter script

Read verbatim. Bracketed text is action, not speech. The script is
written to keep the balance criterion unled: the words *size, color,
position, weight-as-criterion* must not appear in the task instruction
(the observer necessarily adjusts size — the instrument does that;
the experimenter must not name any factor as the thing to judge by).

### 5.1 Welcome
> "Thank you for coming in. I'm [NAME], and I'll be running today's
> session. This is a study about how people see visual balance in simple
> compositions — there are no right or wrong answers, we're measuring
> your perception, not testing your ability."

### 5.2 Consent walkthrough
> "Before we start, let me walk you through the consent form.
> The session takes about 90 minutes with a break in the middle.
> You'll look at simple colored shapes on a screen and make judgments
> about them. The risks are minimal — the most likely discomfort is mild
> eye tiredness, which is why we build in breaks. You can stop at any
> time, for any reason, without penalty, and you can ask for your data
> to be deleted up to [RETENTION WINDOW — lab fills in]. Your data is
> stored under a participant code, never your name. Do you have any
> questions? [Answer.] Please read and sign if you're willing to take part."

### 5.3 Task explanation (adjustment block)
> "In this part you'll see two colored disks on a gray background.
> One of them you can resize using the arrow keys — left and right
> arrows change it a little, holding Shift changes it a lot.
> Your task: **adjust the changeable disk until the whole picture feels
> balanced to you — as if neither side pulls more than the other.**
> Go by your immediate visual impression. Don't think about it too
> long, and don't try to measure anything — there is nothing to get
> right. When it feels balanced, press the Space bar and the next
> picture appears. Sometimes the changeable disk will be on the left,
> sometimes on the right. Any questions?"
>
> [Comprehension check:] "Just to make sure I explained it clearly —
> can you tell me in your own words what you'll be doing?"

*Neutrality note for the experimenter: if the observer asks "should I
match the sizes?" or "should I go by color?", answer: "There's no rule
— set it wherever the picture feels balanced to you." Do not name any
factor as a criterion. Log any such exchange.*

### 5.4 Practice-trial script
> "Let's do five practice rounds so the keys feel natural. Remember,
> I'm not checking your answers — only that the controls make sense.
> [Run 5 trials.] How did that feel? Ready to start the real ones?"

### 5.5 Break script
> "That's the first half done. Let's take ten minutes — please stand
> up, look away from the screen, walk around if you like. I'll come
> get you. There's water [LOCATION]."
> [After break:] "Welcome back. The second part is a little different:
> you'll see finished pictures and rate how balanced each one feels,
> from 1 — not at all balanced — to 7 — perfectly balanced. Again,
> your impression, no right answers."

### 5.6 Debrief
> "That's everything — thank you. A quick explanation of what this was
> about: we're trying to find out whether the feeling of visual balance
> can be broken down into separate contributions — how much comes from
> an element's size, its color, its position, and so on. That's why you
> were adjusting one disk while everything else changed. Before you go,
> three quick questions: [1] What is your habitual reading direction —
> do you mostly read left-to-right, right-to-left, or both equally?
> [2] Have you had any formal training in color theory, graphic design,
> or visual art? [3] Did any strategy occur to you while you were doing
> the task? [Record verbatim.] Thank you — your participant code is
> [CODE]; contact [EMAIL] if you want your data withdrawn."
## 6. Analysis plan

### 6.1 Model (preregistered primary)
Conjoint-style decomposition via a hierarchical Bayesian nonlinear
mixed-effects model (Stan/brms — analysis code brought by us, §10).
Balance condition at the observer's null point: w(A) = w(B), with

    w(group) = A · ( 1 + Σₖ βₖ · xₖ ),   k ∈ {S, H, L, P, C}

xₖ = normalized factor encodings (0–1; hue as 3 dummy variables vs red
reference). Taking logs of the null condition:

    log(A_B/A_A) = log(1 + Σₖ βₖ·x_A,k) − log(1 + Σₖ βₖ·x_B,k)

DV = log null area ratio; A_A known; βₖ with observer-level random
effects; group-level posteriors are the fitted "native values."
*Method precedent: Pieters (1979) brought conjoint measurement into
aesthetics (DV was harmony); Locher, Gray & Nodine (1996) had
participants assign weights to pictorial features — this model aims
the same machinery at balance itself.*

### 6.2 Identifiability diagnostics (reported for every fit)
- **Scale anchor (stated, not estimated):** β_area ≡ 1 by convention.
  Balance data identify weights only up to a global positive scale
  (compute track, break statement §5). All reported coefficients are
  ratios βₖ/β_area. No absolute-weight claims, ever.
- **Condition of the Jacobian** at the posterior mode / least-squares
  optimum: report cond(J). Clean synthetic reference: cond(J) ≈ 16.
  Flag cond(J) > 100 as near-non-identified (**JUDGMENT CALL** threshold).
- **SEs / posterior SDs on all ratios**; R-hat < 1.01 for Bayesian fits.
- **Split-half reliability** (odd/even trials) per ratio: r ≥ .70
  required for a "native value" claim (H1 falsification criterion b).

### 6.3 Explicit checks for the three computational break modes
1. **Interaction absorption (break a).** Fit the additive model, then
   test residuals inside the two factorial blocks for structure:
   Tukey's one-df test for nonadditivity + model comparison
   additive vs additive+interaction (area×saturation, hue×lightness).
   ΔAIC > 10 for the interaction model = H1 falsified via criterion (a).
   *This check is the reason the factorial blocks exist — an OFAT-only
   fit cannot run it.*
2. **Sign-flip collapse (break c).** Fit the horizontal position
   coefficient pooled vs split by reading-direction group (L2R / R2L /
   both). Compare ΔAIC. Report the pooled fit's residual pattern by
   group: the synthetic signature of the collapse is a fitted ≈ 0
   coefficient with signed split residuals (+/− by group). If the
   split model wins → H3 supported; if not → H3 rejected per §1.
3. **Confound / rank loss (break b).** Report the design-matrix
   correlation between every factor pair as actually rendered
   (target: max |r| < .7 — **JUDGMENT CALL**). If any pair exceeds .9,
   coefficients for that pair are declared non-identified and dropped
   to a combined term; the failure is reported, not hidden.

### 6.4 Secondary analyses
- **H2:** same model fitted to evaluation-block ratings (ordinal
  regression DV, same factor encodings); compare β vectors
  production vs evaluation.
- **H4 (Phase B):** lightness-coefficient comparison across ground
  blocks; ground-invariant vs ground-varying model comparison.
- **Robustness:** max-rule alternative (Koenderink et al. 2018) fitted
  and compared — prespecified as the leading non-additive rival.

### 6.5 Preregistered exclusion criteria
1. Fails Ishihara or acuity screening.
2. >2 of 8 symmetric anchors set with |log area ratio| > 0.5
   (inattention/bias — **JUDGMENT CALL** threshold, pilot-tunable).
3. Test–retest correlation on the 20 repeats < .50 (**JUDGMENT CALL**).
4. Session incomplete (< 80% of trials) or aborted.
5. Mean trial time > 90 s with no recorded cause (flag for review;
   exclusion only if paired with criterion 2 or 3).
6. Self-reported strategy of deliberate measurement ("I tried to make
   the areas match mathematically") — debrief Q3; excluded from
   primary, retained for a strategy-sensitivity analysis.
7. Under 18; uncorrected vision below screening; color-vision
   deficiency of any type.
- Color/art/design training is RECORDED as a covariate (Morriss et al.
  1982 found training predicts theory fit), not an exclusion.

---

## 7. Power and sample size

- **The n ≥ 100 note:** Fukada's follow-up force-balance experiments
  (read end to end, Round 3) conclude n ≥ 100 observers are needed for
  stable estimates in a between-subject placement paradigm. That number
  applies to *low-control, few-trials-per-observer* designs.
- **Lab N (primary): 48** — 24 L2R-habitual + 24 R2L-habitual readers
  (H3 needs the split powered). Justification for the smaller N:
  1. **Repeated measures:** ~134 adjustments per observer ⇒ ~6,400
     observations total; H1 is fundamentally within-subject
     (per-observer null points), and group-level ratios are estimated
     hierarchically, borrowing strength across observers.
  2. **The DV is high-objectivity:** the method-of-adjustment tradition
     reports inter-subject agreement of .672–.732 on area-balance
     settings (Granger 1953, *Science* 117, 59–61) — unusually high for
     an aesthetic judgment, which is why this paradigm (not rating
     scales) is the right ancestor.
  3. **High control** (calibrated display, chin rest, adaptation)
     removes the display/ambient/viewing-distance variance that forces
     large online Ns.
- **Target is a JUDGMENT CALL** — no closed-form power formula exists
  for a hierarchical nonlinear conjoint model; the honest procedure is
  a simulation-based power check from the pilot data (preregistered:
  pilot n = 12, used to simulate power for the full N and to finalize
  the D-optimal trial count). If the pilot suggests N = 48 is thin for
  H3's between-group comparison, extend to 72 before Phase B.
- **Online fallback N: ≥ 200** (§11) — larger N compensates uncontrolled
  variance; same Fukada logic that motivated n ≥ 100.

---

## 8. Ethics / IRB checklist

Minimal-risk perception experiment with healthy adults. For the IRB
application, prepare:

1. **Protocol** — this document (plus the lab's local formatting).
2. **Informed consent form** — purpose, 90-min duration, voluntary
   participation, right to withdraw at any time without penalty,
   data-withdrawal window, anonymization (participant codes),
   contact for questions. Walkthrough script in §5.2.
3. **Recruitment text** — neutral; no mention of hypotheses; states
   duration, compensation, eligibility (18+, normal/corrected vision).
   Compensation: lab's standard rate; must not be coercive.
   **JUDGMENT CALL** left to the lab's norms.
4. **Risk assessment** — risks: mild eye tiredness / strain from
   ~65 min of screen judgments. Mitigations: mandatory 10-min break,
   self-paced trials, 100-min hard cap, observer may stop anytime,
   room lighting per §4.3 (no flicker sources). No deception, no
   sensitive topics, no physical contact beyond the chin rest
   (disclose it in consent; offer the no-chin-rest variant, §4.4).
5. **Data anonymization** — participant codes; no names in data files;
   debrief questionnaire stored separately from consent forms;
   reading-direction/training answers are non-identifying.
6. **Data retention** — raw data retained [lab's policy, e.g. 10 years];
   anonymized dataset + analysis code published open (OSF) on
   publication — state this in consent.
7. **Vulnerable populations** — excluded: under-18s, anyone unable to
   give informed consent. No targeting of clinical groups.
8. **Debrief** — full purpose disclosure after the session (§5.6),
   including the decomposition hypothesis; opportunity to withdraw
   data post-debrief.
9. **Adverse events** — none expected; procedure: stop session, record,
   report to IRB per local rules.
## 9. Preregistration outline

Aimed at the standards of **She Ji** (diamond OA, design
theory/methodology — the single most useful venue for this problematic)
and **i-Perception** (natural home for an experimental balance study).
Register on OSF (or AsPredicted) before the first full-run observer;
pilot (n = 12) is explicitly exploratory and registered separately as
such. Contents:

1. **Hypotheses** — H1–H4 verbatim from §1, each with its falsification
   criterion. State the directional predictions: hue ordinal
   red > blue > green > yellow (Bullough 1907 → Locher et al. 2005);
   saturation amplifies (Morriss et al. 1982); position-weight sign
   differs by reading direction (H3); lightness weight is
   ground-contingent (H4).
2. **Design** — §2 in full: factors, levels, D-optimal core (publish the
   selected trial list), factorial blocks, anchors, repeats, mirror
   variants, ground blocks (Phase A gray; Phase B white/black).
3. **Sampling** — lab N = 48 (24 L2R / 24 R2L), recruitment pool,
   eligibility, compensation; pilot n = 12 for the simulation-based
   power check and trial-count finalization.
4. **Variables** — IVs: the six factors (+ mirror, + ground block,
   + task block). DV (primary): log null area ratio from method of
   adjustment. DV (secondary): 1–7 balance ratings. Covariates:
   reading direction, color/design training, trial order, session.
5. **Analysis** — the §6 model as primary; identifiability diagnostics
   (§6.2) as mandatory reporting; the three break-mode checks (§6.3)
   as prespecified; max-rule as the prespecified rival; H2/H4
   comparisons as specified.
6. **Exclusion rules** — §6.5 verbatim, including the pilot-tunable
   thresholds and the rule that thresholds are frozen after the pilot.
7. **What counts as a "native value" claim** — a group-level ratio
   βₖ/β_area with split-half r ≥ .70, SE small enough to exclude zero
   (or to sign it), replicated across the pilot→full-run boundary.
   Anything weaker is reported as an estimate, not a value.

---

## 10. Lab-partner provides vs we bring

| | Lab provides | We bring |
|---|---|---|
| Stimuli | — | **Generator code** (renders the full trial set from the CIELAB spec; gamut-checks; emits the D-optimal list) |
| Protocol | Local IRB formatting; translation of materials if needed | **This protocol**, versioned |
| Apparatus | Calibrated display(s) per §4.1, testing room per §4.3, chin rest / seating | Calibration acceptance criteria (§4.1); validation logging template |
| Participants | Recruitment, scheduling, compensation, pool access (incl. R2L readers — the lab's location determines feasibility of H3) | Eligibility criteria (§6.5, §8) |
| Ethics | IRB submission infrastructure, consent-form templates, data-retention policy | Risk assessment text (§8), debrief script (§5.6) |
| Running | RA time: sessions, screening, calibration logs | Experimenter script (§5), training call on the neutrality rules (§5.3 note) |
| Analysis | — | **Analysis code** (Stan/brms hierarchical model, identifiability diagnostics, break-mode checks); preregistration draft (§9) |
| Software | Machine to run it on | Experiment software (PsychoPy / jsPsych build — **JUDGMENT CALL** on framework, lab's preference wins if they maintain one) |

**First-conversation talking points (authorship / data):**
- Authorship: lab PI + RA as co-authors (target She Ji or i-Perception);
  author order and corresponding author agreed in writing before data
  collection. Our contribution: hypothesis, design, stimuli, analysis.
- Data ownership: raw data stays with the lab under its retention
  policy; anonymized dataset + analysis code published open (OSF/CC-BY)
  on publication — agreed upfront, stated in consent.
- IP: the fitted weight functions are scientific results, published
  openly; no commercial encumbrance either way. (The reader's interest
  is the public formula, not a proprietary one.)
- Pilot-first: n = 12 pilot with a go/no-go on trial count, timing,
  and the identifiability diagnostics before the full run — protects
  both sides' time.
- Preregistration before the full run; deviations logged publicly.

---

## 11. Online fallback — what changes

If no lab partner is secured, the same design runs online. What changes,
honestly stated:

- **Apparatus (§4) — dropped, replaced by instruction + self-report.**
  No colorimeter, no chin rest, no ambient control. Mitigations:
  browser-based display check (gamma self-test card + "is this room
  dim?" self-report + fullscreen enforcement); viewing distance set by
  instruction ("about an arm's length") with a calibration card
  (credit-card-on-screen scaling — **JUDGMENT CALL**); record
  screen size, OS, and browser. Color spec degrades from CIELAB-verified
  to sRGB-authored — the hue/lightness confound risk (break b) rises;
  compensate by widening the design's independent variation, not by
  hoping.
- **N rises to ≥ 200** (Fukada's n ≥ 100 logic, plus uncontrolled
  variance). Reading-direction groups recruited deliberately
  (targeted panels), not by convenience.
- **Attention checks strengthen:** anchors stay; add 4 instructional
  manipulation checks ("press the left arrow three times"); exclude on
  any failed IMC + the §6.5 criteria. Trial-time flags tighten
  (>60 s or <3 s median — **JUDGMENT CALL**).
- **Session splits:** 134 trials is too long unsupervised → two
  ~35-min sessions, 48 h apart max; order counterbalanced.
- **What the online data CAN claim:** the same decomposition estimates,
  with wider uncertainty; H2/H3 tests still valid (task frame and
  reading direction are within-design).
- **What it CANNOT claim vs lab:** colorimetric precision of the
  per-factor functions (no verified color pipeline — report sRGB
  values with the caveat); the position-weight geometry (uncontrolled
  viewing distance ⇒ visual-angle uncertainty); H4's ground
  contingency at full strength (ambient light contaminates ground
  appearance). Frame online as the *replication/extension*, lab as
  the *measurement*.

---

*Document history: drafted 2026-10-09 from `optical-balancing-study.md`
(§10–§12), `optical-balancing-r2-gaps.md` (Morriss & Dunlap design
sketch), and `optical-balancing-compute.md` (identifiability breaks).
Next steps: pilot the D-optimal trial count, finalize the evaluation-block
stimulus construction from pilot medians, then preregister.*
