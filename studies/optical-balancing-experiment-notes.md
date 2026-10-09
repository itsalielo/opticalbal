# Optical balancing — experiment track: build notes

**Status:** protocol + prototype built 2026-10-09. NOT validated — no human data collected with either.
**Lab-first decision:** binding from the reader; online prototype is the fallback/extension.

## What got built

1. `~/workspace/design-sense/optical-balancing-experiment-protocol.md` (569 lines, 11 sections) — the lab-primary protocol: hypotheses H1–H4 with falsification criteria; D-optimal 64-trial fractional factorial over six factors + preregistered area×saturation and hue×lightness factorial blocks; method of adjustment with area as DV (Morriss & Dunlap 1988 extended 2→6); colors authored in CIELAB; hierarchical Bayesian conjoint-style analysis with the three computational break modes as mandatory prespecified checks; lab N = 48 (24 L2R / 24 R2L); full apparatus spec (D65, 120 cd/m², ΔE*ab < 3, 60 cm chin-rest, ≤64 lux) tied to CIE 15:2018 / ISO 3664 / ITU-R BT.500 with 22 flagged judgment calls; word-for-word experimenter script; ethics/IRB checklist; preregistration outline; lab-partner vs we-bring table; online-fallback what-changes section.

2. `~/workspace/opticalbal-experiment/` (index.html, experiment.js, styles.css, README.md) — working self-contained prototype: consent (PLACEHOLDER badge) → instructions with static diagram → 3 practice trials → 24 main trials (factorial-structured + interaction block + 2 attention checks) → debrief with JSON/CSV/clipboard export. Vanilla JS, seeded RNG, canvas rendering, full event logging. Verified headless via Node (syntax, trial counts, color math, id wiring, no edge-clipping); NOT click-tested in a live browser — a smoke run is still advisable.

## What was simplified

- Protocol: several thresholds are pilot-dependent judgment calls (trial count 64, exclusion cutoffs, cond(J) > 100 flag) — frozen post-pilot per the protocol itself; evaluation-block stimulus construction deferred to pilot medians.
- Prototype: no backend, placeholder consent, no display calibration, unlinearized sRGB math, fixed seed for all participants, desktop widths only. The prototype implements a reduced 24-trial version of the paradigm, NOT the full 64-trial lab protocol.

## What real deployment still needs

1. **Lab partner** — the parent's lab-scout track (top candidates: Redies/Jena, Leder/Vienna, Wagemans/KU Leuven); the protocol's partner-vs-we-bring table is the negotiation document.
2. **Ethics** — IRB submission at the partner institution using the protocol's checklist; consent text must be replaced with approved wording.
3. **Pilot** — n = 12 simulation-backed pilot to freeze thresholds, validate apparatus numbers, and check the 90-minute session estimate.
4. **Preregistration** — filed before any confirmatory data collection.
5. **Online fallback** — only if lab stalls: hosting, recruitment pipeline, browser calibration self-test, larger N.
6. **Stimuli generator code** — the CIELAB-authored 64-trial set must be rendered by code we supply (listed as we-bring; not yet written — the prototype's generator is a starting point, not the lab renderer).

## Key design decisions

- CIELAB (not HSL) for stimulus authoring — the hue/lightness confound warning is structural.
- Area as DV, not rating scales — the Morriss & Dunlap tradition is the only paradigm that ever produced weight coefficients.
- Factorial blocks are preregistered interaction diagnostics — the compute track proved OFAT designs are interaction-blind by construction.
- Scale anchor β_area ≡ 1 stated explicitly — no absolute-weight claims, ever.
- Reading-direction split (24/24) is structural — the position sign-flip collapse is a prespecified check, not a post-hoc excuse.
