# Optical Balancing — Online Method-of-Adjustment Prototype

**Honesty statement (read first).** This is a **prototype research instrument**,
not a validated one. It has no ethics approval — the consent text in the app is
an explicitly marked **PLACEHOLDER** — and **no human data has ever been
collected with it**. It is the *secondary* instrument for the optical-balancing
mission (the lab study is primary): a fallback / extension tool for collecting
human balance judgments remotely. Do not treat any data it produces as
scientific findings without validation, ethics review, and calibration.

## What it implements

The method-of-adjustment paradigm of the spatial-balance-of-color-pairs
tradition (Moon & Spencer 1944; Granger 1953; Morriss & Dunlap 1982, 1987,
1988): the observer **adjusts the AREA of a patch until balance is achieved**,
and the adjusted area is the dependent variable.

**Our instantiation** (implementer extension — see "Design decisions" below):
each trial shows **two side-by-side compositions**. Each composition has two
elements on a gray ground: a fixed dark-gray anchor disk A (r = 40 at x = 120)
and a test disk B (nominally x = 280). The left/right assignment of the
*reference* composition (A + fixed B) vs the *test* composition (A + B with
manipulated factors and **adjustable area**) is randomized per trial. The
participant drags a slider (or uses ← → / + − keys) to change the test patch's
radius until the two compositions *feel equally balanced*, then confirms.

### Trial design (main loop: 24 trials)

Reference: B = red (h 0°, s 0.80, v 0.70), r 40; ground gray v 0.78.
Slider range r ∈ [14, 66] (area ratio ≈ 0.12–2.72 vs reference).

| Block | n | Factor varied (test B; rest at reference) |
|---|---|---|
| saturation | 4 | s ∈ {0.20, 0.45, 0.65, 1.00} |
| hue | 4 | h ∈ {60°, 120°, 240°, 300°} |
| lightness | 3 | v ∈ {0.35, 0.50, 1.00} |
| position | 3 | x ∈ {250, 295, 325} |
| contrast | 3 | ground v ∈ {0.45, 0.60, 0.92} (element HSV fixed — contrast varies against the ground, per §3) |
| null | 1 | exact-null calibration (test ≡ reference) |
| interaction | 4 | 2×2: s ∈ {0.35, 0.95} × x ∈ {250, 310} |
| attention | 2 | near-invisible patch (expect slider → max); dark saturated red (expect slider → min) |

Plus 3 fixed practice trials (easy: small hue / saturation / lightness shifts;
start r = 40, adjustable panel always right).

**Randomization** (seeded RNG, mulberry32, **seed = 20261009**, documented in
code and in every export): trial order shuffled; attention checks spliced into
positions 8 and 16; slider start r ∼ uniform[18, 62] (counters anchoring bias —
cheap substitute for ascending/descending series); adjustable side randomized
(counters reading-direction position-weight asymmetries, cf. the sign-flip
break in the computational track). **The seed is fixed, so every participant
currently gets the identical protocol** — a deliberate prototype simplification.

**Attention checks:** expected-end thresholds are r ≥ 56 (expect-max) and
r ≤ 22 (expect-min). Results are *flagged* in the data file only — the
participant is never judged or lectured.

## How to run

No build step, no backend, no external dependencies. Either:

- Open `index.html` directly in a browser (`file://` works), or
- Serve statically: `python3 -m http.server` in this directory, then open
  `http://localhost:8000/`.

Tested logic headless with Node (color math, trial generation, determinism);
the interactive flow requires a browser. Laptop/desktop widths recommended —
a non-blocking advisory appears below 760 px; mobile is explicitly out of scope.

**Keyboard:** ← → (or ↑ ↓) adjust when the slider is focused; + / − adjust
anywhere during a trial (Shift = ×10 step); Enter confirms.

## Screens (in order)

1. **Consent** — placeholder text, clearly badged PLACEHOLDER; "I consent"
   gates entry.
2. **Instructions** — plain-language task description + static worked example
   (canvas diagram; not interactive).
3. **Practice** — 3 trials; confirm shows "Recorded" (mechanics confirmation,
   never correctness feedback — there is no right answer).
4. **Main loop** — 24 trials with counter ("Trial 7 of 24") and progress bar.
5. **Debrief + export** — neutral completion summary; download JSON, download
   CSV, copy JSON to clipboard. Data never leaves the browser otherwise.

## Color math (as implemented)

- Stimuli specified in **HSV** (h degrees, s/v in [0,1]); "lightness" in the
  six-factor framing = HSV value V (documented simplification, not CIELAB L*).
- **HSV→RGB**: standard sector algorithm (Foley & van Dam / CSS Color 4 form).
- **Luminance**: Rec. 709 luma on gamma-encoded 8-bit sRGB, **not linearized**
  (documented simplification — values are display-referred, not photometric).
- **Contrast** = |L_element − L_ground| ∈ [0,1] (per §3; achromatic ground ⇒
  L_ground = V_ground). Hue-as-hue is encoded nowhere — consistent with the
  computational finding that no model sees hue as hue (only via luminance).
- Stimuli rendered on `<canvas>` with `devicePixelRatio` backing-store scaling;
  flat fills only (no shadows/gradients — they'd add luminance confounds).

## Data format

Per trial (JSON full record; CSV flattened, trajectory JSON-only):

- `trial_number` (restarts per phase), `trial_type` (`practice`/`main`/`attention`),
  `block`, `adjustable_side`
- Stimulus parameters: saturation, hue, lightness (v), base area (r = 40 ref),
  position (x, y), contrast (luminance-based), background (`ground_v`) —
  recorded for **both** reference and test patches, plus per-element luminance
  and contrast values so analysts need not recompute them
- `r_start`, `r_final`, `area_final`, `area_ratio_vs_ref`
- `trajectory`: `[[elapsed_ms, radius], …]` for every slider movement (timestamps
  from `performance.now()`)
- `rt_ms` (stimulus onset → confirm), `n_inputs`
- `attention_expected` / `attention_pass` (null on non-attention trials)
- Session metadata: seed, session id, ISO start time, user agent, viewport, DPR
- `events`: every screen show, trial start/confirm, export — all with
  `performance.now()` timestamps

## Simplified vs a real deployment (deployment gaps)

- **No backend**: data lives in the browser until the participant downloads it.
  No participant management, no resume, no server-side validation.
- **No ethics**: consent text is a placeholder; no IRB process, no debriefing
  standards, no data-protection compliance work.
- **No display calibration**: no gamma measurement, no ambient-light control,
  no physical-size normalization (stimuli are in CSS px, not degrees of visual
  angle), sRGB math is unlinearized (see above).
- **Fixed seed**: identical trial order for all participants (a real deployment
  would draw and record a fresh seed per participant).
- **Self-administered**: no experimenter script, no controlled viewing distance,
  no exclusion-criteria enforcement.
- **Timing**: `performance.now()` granularity only; no photodiode / frame-count
  verification of stimulus onset.
- **Single session**, no practice-to-main performance gating, no break handling.
- **Desktop widths only**; not validated on touch devices.

## Design decisions made without a literature source

Stated plainly so a future validator knows what was invented here:

1. **Two-panel match-to-reference.** Morriss & Dunlap adjusted area *within*
   one composition; matching two compositions' balance against each other is
   our extension to make the task self-explanatory online.
2. **Slider range r ∈ [14, 66], step 0.5** — implementer choice; wide enough
   for large weight ratios, narrow enough to avoid edge clipping at x = 325.
3. **Attention thresholds** (r ≥ 56 / r ≤ 22) — implementer choice.
4. **Practice fixed** (start r = 40, right side) — training simplification.
5. **No numeric readout** on the slider — avoids anchoring on numbers.
6. **Contrast operationalized as ground variation** — follows §3's definition,
   but the specific ground levels {0.45, 0.60, 0.92} are implementer choices.
7. **Fixed seed across participants** — prototype simplification (see above).
8. **Random slider starts as the anti-anchoring device** — a cheap substitute
   for the classical method-of-adjustment ascending/descending series.

## Files

- `index.html` — all screens, no build step
- `styles.css` — monochrome instrument chrome (stimuli carry the color)
- `experiment.js` — vanilla JS; seeded RNG, color math, trial generation,
  canvas rendering, logging, export
- `README.md` — this file

Motion: one quiet 250 ms cross-fade between screens, disabled entirely under
`prefers-reduced-motion`. The progress bar updates discretely. Nothing else
moves.
