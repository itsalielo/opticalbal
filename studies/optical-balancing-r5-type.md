# ROUND 5 — TYPE-DESIGN COMPENSATION: THE CRAFT NUMERIC VEIN

Mission context: the reader's problematic is the exact mathematical formula for visual weight.
Type design is the craft where optical compensation is most quantified. This file extracts every
hard number the craft has published — plus new measurements made for this round directly from
shipped font binaries (method documented, reproducible with fontTools).

Tier key: **T1** = peer-reviewed; **T2** = informed practitioner / engineering documentation;
**M** = author-measured from published font binaries (primary data, method below).
Already logged in earlier rounds (not repeated): Karow 3% (O)/5% (A), Hoefler ~1% square squeeze,
horizontals ~85–90% of verticals, TypeDrawers Helvetica/Arial/Geneva/Verdana EM-100 overshoot
stats, Ahrens & Mugikura size-specific adjustments, Adobe optical kerning/margin alignment,
Spiekermann diagonal rule, Frere-Jones eye-over-ruler, Carter Bell Centennial, Sitka/Role,
Cheng, Noordzij. Seredkina NOT reopened.

---

## 1. THE NUMERIC VEIN — MASTER TABLE

### 1a. Optical-size (opsz) axis: measured deltas, 4 variable fonts [M]

Method: each font instantiated at opsz min/max (all other axes at default) with
fontTools.varLib.instancer; glyph bounds via BoundsPen, ink area via AreaPen, stem widths via
flattened-outline scanlines (quadratic subdivision, 24 steps). Sources: google/fonts repo
(OFL binaries, Oct 2026). Regular/default weight.

| Font (UPM) | opsz | x-height (% em) | O overshoot (% cap) | adv H (u) | adv n (u) | n LSB (u) | n-stem (u) | H-stem (u) | o contrast side/bottom | ink area H (u²) |
|---|---|---|---|---|---|---|---|---|---|---|
| Fraunces (2000) | 9 | 48.20 | 2.86 | 1805 | 1373 | 54 | 424 | 464 | 3.27 | 1,584,434 |
| Fraunces (2000) | 144 | 44.80 | 1.43 | 1606 | 1124 | 26 | 362 | 428 | 24.32 | 1,242,068 |
| Inter (2048) | 14 | 54.59 | 1.34 | 1522 | 1210 | 158 | 180 | 190 | 0.93 | 697,576 |
| Inter (2048) | 32 | 51.56 | 1.61 | 1450 | 1120 | 126 | 170 | 180 | 1.09 | 663,440 |
| Newsreader (2000) | 6 | 51.20 | 1.41 | 1803 | 1397 | 80 | 198 | 218 | 1.18 | 974,928 |
| Newsreader (2000) | 72 | 51.20 | 1.40 | 1649 | 1192 | 46 | 184 | 206 | 3.92 | 719,442 |
| Roboto Flex (2048) | 8 | 53.17 | 2.06 | 1528 | 1212 | 148 | 198 | 205 | 1.26 | 730,776 |
| Roboto Flex (2048) | 144 | 44.63 | 1.37 | 1170 | 908 | 118 | 107 | 110 | 1.16 | 387,940 |

Deltas, small→large opsz (the designer's encoded compensation function):
- **Fraunces** (Undercase Type, serif, opsz 9–144): x-height −3.40 pp (−7.1% relative);
  O overshoot **halved**, 2.86%→1.43% of cap; advance H −11.0%; ink area H −21.6%;
  contrast ratio 3.27→**24.32** (hairline bottom of 'o' thins to 14u at display size).
- **Inter** (Rasmus Andersson, sans, opsz 14–32): x-height −3.03 pp; advance H −4.7%;
  ink area −4.9%; overshoot 1.34%→**1.61%** — rises with size, against the usual rule.
- **Newsreader** (Production Type, serif, opsz 6–72, default 18): x-height 51.2% (6pt)
  → 42.6% (default 18) → 51.2% (72pt) — non-monotonic; contrast 1.18→3.92;
  advance H −8.5% min→max.
- **Roboto Flex** (Font Bureau for Google, sans, opsz 8–144): x-height −8.54 pp
  (−16% relative, the largest swing); advance H **−23.4%**; ink area H **−46.9%**;
  stems −46%; overshoot 2.06%→1.37%.

Reading: across all four, small-size masters buy legibility with +3 to +8.5 pp x-height,
+5 to +23% advance width, +5 to +47% ink area, and looser sidebearings (n LSB +22 to +28u);
display masters spend it on contrast (up to 24:1 in Fraunces) and tighter spacing.

### 1b. Roboto Flex parametric axes — Font Bureau's published compensation parameters [M]

Read from the shipped fvar table (UPM 2048). These are the designer's own numeric
optical-correction controls; YTLC/YTUC are literally "lowercase/uppercase height" knobs:

| Axis | Meaning | Min | Default | Max |
|---|---|---|---|---|
| opsz | optical size (pt) | 8 | 14 | 144 |
| YTLC | lowercase height (u) | 416 (20.3% em) | 514 (25.1%) | 570 (27.8%) |
| YTUC | uppercase height (u) | 528 (25.8% em) | 712 (34.8%) | 760 (37.1%) |
| YTAS | ascender height (u) | 649 | 750 | 854 |
| YTDE | descender depth (u) | −305 | −203 | −98 |
| YTFI | figure height (u) | 560 | 738 | 788 |
| XOPQ | counter width, x (u) | 27 | 96 | 175 |
| YOPQ | counter width, y (u) | 25 | 79 | 135 |
| XTRA | counter/space param (u) | 323 | 468 | 603 |
| GRAD | grade | −200 | 0 | 150 |
| wdth | width (%) | 25 | 100 | 151 |
| slnt | slant (°) | −10 | 0 | 0 |

### 1c. Psychophysics: the thickness illusion, lab-measured [T1]

de Waard, J.M., Van der Burg, E. & Olivers, C.N.L. (2019). "A Thickness Illusion:
Horizontal Is Perceived as Thicker than Vertical." *Vision*, 3(1), 1.
https://doi.org/10.3390/vision3010001 — https://www.mdpi.com/2411-5150/3/1/1
The first experimental test of the illusion behind horizontal/vertical stroke compensation.
- Exp 1 (n=28): mean PSE −0.05° (−2.71 px); **the vertical line must be 5.4% thicker
  than the horizontal for perceptual equality**; bias present in 27/28 observers;
  t(27) = −9.44, p < .001, BF = 4.6×10⁶.
- Exp 2 (n=29, replication + frames): thickness effect **2.6%**; vertical–horizontal
  length illusion 3.9%; frame-orientation ratio (horizontal:vertical frame) 1:2.3
  thickness, 1:3.3 length; individual-difference correlation r = −0.321, p = .045
  (shared mechanism with the vertical–horizontal illusion).
- Authors measured the actual vertical/horizontal stroke ratios in **Futura (13%)**
  and **Avenir (20%)** — 2.4× to 7.7× larger than the lab illusion (5.4% / 2.6%).
  Craft lore (85–90% horizontals = 11–18% thicker verticals) sits between the two.
  The paper flags the gap as unexplained: typographic context, size, and acuity may
  amplify the illusion beyond the abstract-line lab value.
- Explicitly notes Arabic reverses the pattern: Arabic typefaces are "commonly thicker
  in horizontally oriented segments, even when the intended result is to appear
  constant in thickness," citing TypeDrawers discussion #2034.

### 1d. Microsoft font-engineering documentation [T2]

From the OpenType spec / TrueType fundamentals / VTT docs (learn.microsoft.com):
- Sample Control Value Table (font units): UC round base **−39**, LC round base **−35**,
  figure round base **−33** (i.e. overshoots encoded as negative CVT entries);
  x-height flat 1082 / round 1114 (Δ32); cap flat 1493 / round 1522 (Δ29);
  figures flat 1463 / round top 1491 (Δ28); ascender flat 1493 / round 1514 (Δ21);
  x stem weight **157** / y stem weight **127** — vertical stems **24% thicker**
  than horizontals in the reference font.
- VTT worked example ("MyFont"): UC flat 1465, UC round 1490 → overshoot **25u**;
  the prep program keeps round/flat heights unified "until there is enough pixels
  to display a round overshoot."
- DELTA exceptions: delta_base default **9 ppem**; DELTAP1/C1 cover 9–24 ppem;
  DELTAP2 +16 ppem, DELTAP3 +32 ppem above that.
- VTT delta/move resolution: **1/8 px** default; Alt refines to 1/16, 1/32, 1/64 px;
  Ctrl coarsens to 1/4, 1/2, 1/1 px.
- Rasterization rationale: a round stroke "just over 1½ pixels rounds up to 2 pixels"
  while a straight stroke "just under 1½ pixels rounds down to 1" — the CVT exists to
  force both to the same pixel count at small sizes.
- Character design standards: Tahoma small caps **78.5% vertical × 82% horizontal**
  of cap height; Palatino Linotype small caps **65% × 66%**; L-slash bar ≈30°
  (Palatino regular **29.8°**, italic **28.03°**); Eth bar "slightly north of the
  mathematical center"; round characters must overshoot the baseline "the same amount
  as the top overshoots"; S and C "often need to be a bit smaller than the
  fully-enclosed O" (Matthew Carter, quoted in the standard).

### 1e. Arabic optical compensation [T2 + M]

- TypeDrawers #2034, "Optical Correction in Arabic Monoline"
  (https://typedrawers.com/discussion/2034/optical-correction-in-arabic-monoline/p1):
  consensus that Arabic monolines thin the **verticals** (reverse of Latin); one
  practitioner proposes verticals at **76** against horizontals at 100 for the
  sample weight; Tahoma Arabic cited as a shipping example. Thread notes the
  Maghribi styles of Spain/North Africa are the most uniform, contrast "limited to
  the terminals of strokes in bowls and arcs," rarely stressing verticals.
- Measured in Amiri Regular (UPM 1000, OFL, Khaled Hosny) [M]: alef vertical stem
  **49–63u** (~5.6% em); beh base horizontal stroke **83–98u** (~9.1% em) →
  **horizontals ≈1.6× verticals**, the Latin contrast ratio inverted, quantified.
- No Arabic-specific lab measurement of the compensation function found; the de
  Waard paper's Arabic remark is observational, not experimental.

### 1f. Other craft numbers gathered [T2]

- TypeDrawers "Your most valuable Tips & Tricks in Type Design" — hairline weight via
  stroking a skeletal path to **20 units / 1000 em**.
- Christian Schwartz, "Typography Spacing Techniques" (MICA, Fall 2007): SANS —
  space between flat characters "just under **half of the counterform width**";
  SERIF — "slightly less than the **counterform width**."
  (https://www.scribd.com/document/400385006/Christian-Schwartz-Spacing-Typography)
- Inter lab (Rasmus Andersson, rsms.me/inter/lab): body text below 18pt needs no
  tracking; display above 32pt takes **−0.02 em** tracking.
- *Designing Type* (2nd ed.) excerpt: thick diagonal **+5–10%** in light weights,
  **85–95%** in heavy weights (to avoid dark V); thin diagonals drawn heavier than
  the horizontal thin stroke, citing Waard 2019; O-vs-A overshoot ordering is
  design-dependent (both directions attested).
- Named designers (Carter, Highsmith, Berlow, Spiekermann, Schwartz, Sowersby,
  Edmondson): no additional published numeric overshoot/weight values surfaced
  beyond the above. Berlow's numbers live in the Roboto Flex parametric axes (§1b);
  Carter's in the Microsoft standard quote (§1d); Schwartz's in his spacing notes
  (this section). Highsmith, Sowersby, Edmondson, Spiekermann publish process
  writing but no hard compensation numbers found.

---

## 2. ABSENCES (checked, still empty)

- **(d) No lab study measures legibility or aesthetic effects of specific overshoot
  amounts.** The de Waard paper (§1c) is the closest psychophysics in existence and
  it covers thickness, not overshoot. The "psychophysical overshoot function"
  remains unmeasured.
- **(c) TrueType-side:** per-font CVT/delta values are the compensation layer, but
  no Microsoft/Google publication tabulates recommended overshoot or stroke-ratio
  values beyond the sample CVT in §1d.
- **(e) Arabic:** quantified only at craft level (TypeDrawers #2034, Amiri
  measurement); no psychophysical or foundry-published numeric tables found.

## 3. WHAT THIS ADDS UP TO (for the formula hunt)

1. The opsz axis is the craft's largest published multi-factor compensation dataset:
   x-height, width, spacing, weight, contrast, and overshoot all move together, and
   the four fonts disagree on direction for overshoot (Fraunces halves it, Inter
   raises it) — overshoot is not a fixed % of cap height but a per-design variable.
2. The lab value for the thickness illusion (2.6–5.4%) is far below craft practice
   (13–20% in Futura/Avenir; 24% in Microsoft's reference CVT) — either context
   amplifies the illusion ~3×, or craft overcompensates. This is a directly testable
   gap for the planned experiment (Phase 2): replicate de Waard with letterforms.
3. Arabic inverts the Latin contrast sign with a measured ~1.6:1 horizontal:vertical
   ratio — any "exact formula" for visual weight must be script-aware or it fails
   on the reader's own script.

## 4. SOURCES (all verified retrievable)

- https://www.mdpi.com/2411-5150/3/1/1 (T1)
- https://typedrawers.com/discussion/2034/optical-correction-in-arabic-monoline/p1 (T2)
- https://learn.microsoft.com/en-us/typography/opentype/otspec140/ttch01 (T2, sample CVT)
- https://learn.microsoft.com/en-us/typography/truetype/from-typeface-to-font-file (T2, VTT overshoot example)
- https://learn.microsoft.com/en-us/typography/tools/vtt/vtt-42-release-notes (T2, delta resolution)
- https://learn.microsoft.com/lv-lv/typography/truetype/fixing-rasterization-issues (T2, 1½-px rounding)
- https://learn.microsoft.com/de-de/typography/develop/character-design-standards/uppercase (T2)
- https://typedrawers.com/discussion/3993/ (T2, tips & tricks incl. 20u hairline)
- https://www.scribd.com/document/400385006/Christian-Schwartz-Spacing-Typography (T2)
- https://res.mdpi.com/vision/vision-03-00001/article_deploy/vision-03-00001.pdf (T1 PDF)
- Shipped binaries measured: google/fonts repo — ofl/fraunces, ofl/inter,
  ofl/newsreader, ofl/robotoflex, ofl/amiri (OFL; measurement scripts in /tmp/opsz —
  ephemeral, method described in §1a)
