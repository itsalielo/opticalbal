# OPTICAL BALANCING — The Perception Science
*Worker A deliverable · perception science angle · 2026-10-09*

This file covers the academic literature on **perceived visual balance**: what the Gestalt tradition claims, what Rudolf Arnheim's model actually says, and what later empirical psychology found when it tried to test those claims. It ends with a synthesis of the visual-weight factors the literature identifies — the candidate terms for any "exact formula" — and a verdict on whether such a formula exists.

Sourcing rule applied: every Tier 1 item below was verified to exist by web search (title, authors, journal, DOI/PMID). Anything unverified is flagged `UNVERIFIED`.

---

## 1. Definitions (get the vocabulary straight)

The literature uses several distinct concepts that are often conflated. Hübner & Fillinger (2019) showed empirically that people actually mean different things by "balance" depending on the picture type:

- **Mechanical balance** — the seesaw metaphor: visual "weights" distributed around a center, as if the composition were a physical system in static equilibrium. This is the Denman Ross formulation: unequal attractions balance at distances inversely proportional to them. Applies most when people judge single-element or simple abstract compositions.
- **Gravitational stability** — the "will it fall over?" reading: a composition feels balanced when its mass distribution suggests it could stand upright under gravity (more weight low = more stable). This is how people tended to rate balance for multi-element and dynamic-pattern pictures (Hübner & Fillinger, 2019). Pierce (1894, cited in Hübner & Fillinger, 2019) already observed that horizontal arrangements invoke *balance* while vertical arrangements invoke *stability*, and that pictures were preferred with more weight in the lower half.
- **Symmetry / reflection** — a special, limiting case of balance (perfect mirroring around an axis). Treated in the literature as a distinct, neurally privileged cue (Bertamini et al., 2018).
- **Equilibrium / center of mass (CoM)** — the computational operationalization used in modern tests: treat each pixel or element as a mass and compute the composition's center of mass, then measure its deviation from the frame center or from Arnheim's symmetry axes. Two formal measures appear in the literature:
  - **APB (Assessment of Preference for Balance)** — a formula based on Arnheim's symmetry-axes framework (element size and position relative to the horizontal, vertical, and diagonal axes of the frame), introduced in the Gershoni & Hochstein (2011) line of work.
  - **DCM (deviation of the center of mass)** — the distance of the computed center of mass from the frame center/axes; a straightforward physicalist measure. *(Gloss: the exact DCM computation is standard center-of-mass physics; what Hübner & Fillinger (2019) report is that DCM scores explained up to ~68% of variance in balance ratings for simple stimuli.)*
- **Perceptual balance vs. photometric balance** — Koenderink et al. (2017) demonstrate that compositional "weight" is not the same thing as luminance or any other physical quantity: balancing a white patch against a black patch on a gray ground depends on background tone, edge quality, and shape in ways that photometry cannot predict.

Bottom line for the formula question: the literature agrees there is no single agreed *thing* called "balance" — there are at least two readings (mechanical vs. gravitational-stability), and subjects switch between them by picture type.

---

## 2. The Gestalt foundations: Wertheimer, Köhler, Koffka (Tier 2)

An important honest finding first: **the classical Gestalt founders did not theorize compositional balance as such.** Balance of a layout is Arnheim's development. What the founders supplied is the principle behind it — *Prägnanz* (the tendency of perception toward "good form") — plus the field-and-force metaphor Arnheim borrowed from Köhler.

- **Max Wertheimer (1923), "Untersuchungen zur Lehre von der Gestalt, II"** (*Psychologische Forschung*, 4, 301–350). The law of Prägnanz: the psychological organization of the visual field always tends toward the *best* (most regular, symmetrical, simple) form that conditions allow. Perceptual organization is dynamic — it settles into equilibrium states rather than merely recording stimuli. Symmetry and simplicity are preferred not by taste but by the nature of the process. (Tier 2: primary source text, pre-peer-review era.)
- **Wolfgang Köhler (1929), *Gestalt Psychology* (Liveright; rev. 1947); (1938), *The Place of Value in a World of Facts* (Liveright).** Köhler's core claim: brain processes are physical-chemical systems that distribute themselves dynamically toward states of minimal energy — a physical *equilibrium* — and perceived form corresponds to ("is isomorphic with") these states. This is the source of the perceptual-force language Arnheim later took literally: perceptual "forces" are, in Köhler's scheme, real tendencies of the underlying process toward equilibrium. (Tier 2.) Modern neuroscience rejects the isomorphism claim as a historical curiosity (McManus et al., 2011, note this explicitly), but the descriptive principles — preference for regularity, symmetry, simplicity — survive as empirical generalizations.
- **Kurt Koffka (1935), *Principles of Gestalt Psychology* (Harcourt, Brace).** The systematic textbook statement of Prägnanz: organization tends toward the most stable, simple, unified, symmetrical configuration available; "goodness" of a Gestalt includes simplicity, unity, regularity, and symmetry. Koffka's treatment of equilibrium states in perception is the bridge between Wertheimer's principle and Arnheim's applied compositional theory. (Tier 2.)

Summary: the founders' contribution to the balance question is the claim that perception is an **equilibrium-seeking dynamic system with a built-in preference for regular, symmetrical, simple organization**. Arnheim converts this into a compositional mechanics.

---

## 3. Arnheim's model of balance (Tier 2, foundational)

**Rudolf Arnheim, *Art and Visual Perception: A Psychology of the Creative Eye* (1954; revised ed. 1974, University of California Press), Chapter 1, "Balance"; continued in *The Power of the Center* (1982, University of California Press).**

Chapter 1 opens with the famous reductionist exercise: a single black disk on a white square. An off-center disk looks "restless" — its position is perceived as a play of attraction and repulsion relative to the frame's edges. The claims, in my own words:

1. **Balance is dynamic equilibrium of perceptual forces.** A composition is balanced when its visual forces mutually counterbalance — the way physical forces do. Arnheim means this in a strong, near-literal sense, not as metaphor: he writes that perceptual forces are "assumed to be real in both realms of existence — that is, as both psychological and physical forces" (1974, p. 16).
2. **The structural skeleton of the frame.** Every framed composition contains a hidden network of visual forces: the frame's center, its horizontal and vertical midlines, its diagonals, and its edges. Even an empty square is "empty and not empty at the same time" — its center belongs to a complex hidden structure, explorable the way iron filings explore a magnetic field. Positions lying on the skeleton (the center, the axes) are comparatively "restful"; off-axis positions carry tension and pull. Arnheim's figure of the square's skeleton (center + cross + diagonals) is the single most cited diagram in compositional-balance literature — the APB measure is literally a formalization of it.
3. **The optical center sits slightly above the geometric center.** The perceived center of gravity of a composition — the point around which balance is actually felt — lies just above the true geometric middle of the frame. (This is the canonical "optical center" claim carried from this chapter into design practice: centering by coordinates reads as low.)
4. **Balance is achieved two ways: symmetry, or asymmetric equilibrium.** Symmetry is the simple case. The interesting case — and the heart of optical balancing — is the asymmetric composition whose unequal weights counterbalance each other. Arnheim follows Denman Ross here: unequal attractions balance at distances inversely proportional to them (a small weight far from center can counterweight a large one near it) — the lever principle applied to the visual field, with the balance point being "the center of the frame coinciding with the weight center of the pattern."
5. **Visual weight: the factors.** Arnheim's chapter enumerates what makes an element "heavier" (i.e., exert a stronger pull):
   - **Size** — larger areas weigh more.
   - **Color** — warm, advancing colors weigh more than cool, receding ones; high-chroma, luminous colors weigh more than dull ones.
   - **Value (darkness) relative to background** — darker elements weigh more on a light ground (the reverse holds on dark grounds); contrast against the surround matters more than absolute tone.
   - **Position: top vs. bottom** — the upper half of the picture is heavier: a dark area placed high appears heavier than the same area placed low. (This is why Arnheim-derived lore says the optical center sits *above* the geometric one.)
   - **Position: left vs. right** — the right side of the field is held to weigh more heavily than the left (a standard attribution in design textbooks summarizing Arnheim).
   - **Position on the structural skeleton** — a weight on a main axis or at the center behaves differently from one off-axis; the lever distance from the balance point multiplies the weight.
   - **Shape regularity** — compact, regular shapes weigh more than irregular ones.
   - **Orientation** — vertical orientation weighs more than horizontal; diagonal is the heaviest (inherited by design lore from this chapter).
   - **Intrinsic interest / detail / complexity** — an area rich in articulation or meaning attracts more and therefore weighs more.
   - **Isolation** — empty space around an object increases its weight; a figure surrounded by void pulls harder than the same figure crowded by neighbors.
6. **Top-heaviness and direction.** Because the top is intrinsically heavier, compositions tend to read as "top-heavy" unless compensated; balance is therefore not just a matter of left–right seesaw but of the vertical axis, where gravitational stability (bottom-weightedness) enters — a point the later empirical work (Hübner & Fillinger, 2019; Pierce, 1894) confirms subjects are sensitive to.

Caveat: the factor list above is Arnheim's *introspective theory*, not an experimental result. Its status is exactly what the Tier 1 literature argues about.

---

## 4. The physicalist predecessor: Denman Ross (Tier 2)

**Denman W. Ross (1907), *A Theory of Pure Design* (Houghton, Mifflin).** Arnheim cites Ross (p. 19) and derives the quantitative backbone of his theory from him. Ross proposes that visual "attractions, tensions or pulls" behave like physical forces: equal attractions balance at equal distances from a center; unequal attractions balance at distances inversely proportional to them. Given a set of attractions, one finds the balance point by "weighing the attractions together in the field of vision and observing the position of the center." Ross explicitly sought "measurable quantities and qualities" of art — a scientific basis for design that could verify or correct visual feeling. He concedes the hard limit: when objects "vary in their tones, measures, and shapes, and where there are qualities as well as quantities to be considered," calculation becomes difficult if not impossible, and one must depend on "visual sensitiveness." **This is the original statement of the exact-formula ambition — and of its defeat.**

---

## 5. The empirical literature (Tier 1)

### 5.1 McManus, Stöver & Kim (2011) — the direct test of Arnheim–Ross
**"Arnheim's Gestalt theory of visual balance: Examining the compositional structure of art photographs and abstract images." *i-Perception*, 2, 615–647.**
- DOI: 10.1068/i0445aap · Open access (PMCID: PMC3485801, PMID: 23145250).
- What they did: formalized the Arnheim–Ross theory in its *physicalist* reading — compute the image's center of mass (CoM) and test whether it falls on the frame center or one of Arnheim's axes. Three data types: (a) a large representative collection of art photographs of recognized quality vs. controls; (b) expert and non-expert croppings; (c) Ross's own procedure of moving a frame around simple objects (e.g., Arnheim's two black disks).
- What they found: weak support in the correlational data — CoM of art photographs was closer to an axis (horizontal, vertical, or diagonal) than controls; same for photographic croppings. But **strong within-image paired comparisons found no support**: moving the CoM on/off an axis (the "gamma-ramp" study) or comparing adjacent croppings on/off an axis (the "spider-web" study) produced no preference; frame-around-disks studies of different size/greyness/background did not support the Gestalt theory either.
- Conclusion: the *detailed* physicalist theory is not supported, although several significant correlational results "clearly require explanation by any adequate theory of the aesthetics of visual composition."
- Relevance to the formula question: this is the cleanest existing attempt to turn Arnheim into a computable formula (center of mass vs. axes) — and it fails in controlled tests. Any formula claim must reckon with this paper.

### 5.2 Gershoni & Hochstein (2011) — balance at first glance
**"Measuring pictorial balance perception at first glance using Japanese calligraphy." *i-Perception*, 2(6), 508–527.**
- DOI: 10.1068/i0472 · Freely available (Pion-era; free PDF copies in circulation).
- What they did: compared the APB formula (formalized from Arnheim's symmetry-axes framework) against human balance ratings for Japanese calligraphy — first at first fixation, then with unlimited viewing, then across five rotations, with artist and novice groups.
- What they found: APB matched ratings for simple geometrical shapes with unlimited viewing time, but **failed to predict balance ratings for calligraphy**. High between-task correlation among humans, low correlation with the formula. Rotation had no effect on the APB computation but dramatically changed human balance ratings — especially for art experts.
- Their account: first-fixation balance derives from **global processes** — grouping of lines and shapes, object recognition, preference for horizontal and vertical elements (the "aesthetic oblique effect": Mondrian-type works are preferred with horizontal/vertical over rotated-oblique elements, cf. Latto & Russel-Duff; Plumhoff & Schirillo), closure, completion — "enhanced by vertical symmetry" — rather than from element size/position relative to symmetry axes. They list the attributes that can carry weight: size (citing Berlyne; Pierce 1894; Puffer 1903), color (citing Arnheim 1974; Bullough 1907; Pinkerton & Humphrey 1974), coarse texture, contrast, and *interest*. And they note an ecological factor: because natural scenes are more crowded at the bottom, weight at the top is perceived as "heavier" (citing Arnheim).
- Relevance: a formula that works for dots fails for real stimuli; balance perception at first glance is configural and semantic, not a weighted sum of size × position.

### 5.3 Hübner & Fillinger (2019) — "balance" is not one thing
**"Perceptual Balance, Stability, and Aesthetic Appreciation: Their Relations Depend on the Picture Type." *i-Perception*, 10(3).**
- DOI: 10.1177/2041669519856040 · Open access.
- What they did: rated pictures from the Visual Aesthetic Sensitivity Test (VAST) for balance and liking, plus objective measures (DCM, APB). Stimuli sorted — and the sorting was empirically validated by a categorization task — into single-element, multiple-element, and dynamic-pattern pictures.
- What they found: balance ratings did not differ across the three picture types, but liking did. Crucially, "balance" was **interpreted differently by stimulus type**: mechanical balance for single-element pictures, gravitational *stability* for multiple-element and dynamic-pattern pictures. **Only for multiple-element stimuli was there a positive relation between balance/stability and liking.** For single-element pictures, liking was independent of balance.
- On formulas: for specifically constructed simple pictures with homogeneous elements (citing Hübner & Fillinger 2016 and Wilson & Chatterjee 2005), DCM scores explained up to ~68% of the variance in balance ratings and ~86% in liking. For complex pictures the relation collapses: the APB "completely failed to predict perceptual balance ratings" for Japanese calligraphy (Gershoni & Hochstein, 2011; replicated by Fillinger & Hübner, 2018 — `UNVERIFIED`: exact title/venue not pinned down in this research pass), and for architectural photographs the formal scores explained only ~10% of Instagram Likes (Thömmes & Hübner, 2018). Their lesson: for complex artwork, balance is one small factor among many; discounting known factors (e.g., prototypicality) can restore some predictive power.
- Relevance: the strongest modern statement of *where formulas work and where they die*. Formulas work in the restricted domain of simple homogeneous stimuli; they do not generalize.

### 5.4 Hübner & Thömmes (2019) — replicating Puffer (1903)
**"Symmetry and Balance as Factors of Aesthetic Appreciation: Ethel Puffer's (1903) 'Studies in Symmetry' Revised." *Symmetry*, 11(12), 1468.**
- DOI: 10.3390/sym11121468 · Open access.
- What they did: repeated, with modern methods, one of the first experimental studies of balance — **Ethel Puffer (1903), "Studies in Symmetry," *Psychological Review Monograph Supplement*, 4 (Harvard Psychological Studies 1), 467–539** (Tier 1, historic). Puffer used a *production* method: participants arranged elements into pleasing compositions.
- What they found: then and now, **little to no evidence that mechanical balance guides construction**. Participants instead used *closeness* and *bilateral (lateral) symmetry* as organizing principles — even at the expense of mechanical balance.
- Relevance: when people *make* compositions rather than rate them, balance-as-physics loses to symmetry and grouping. The Gestalt grouping principles outrank the seesaw.

### 5.5 Thömmes & Hübner (2018) — balance in the wild
**"Instagram Likes for Architectural Photos Can Be Predicted by Quantitative Balance Measures and Curvature." *Frontiers in Psychology*, 9.**
- Open access. (Verified via the author's publication list; full citation details per exaly listing: *Frontiers in Psychology*, 2018, 9.)
- What they did: computed quantitative balance measures (DCM, APB) for ~700 architectural photographs posted on Instagram by different photographers and tested prediction of Instagram Likes.
- What they found: the scores correlated significantly with Likes — **for photographs of three-dimensional scenes** — but explained only ~10% of variance.
- Relevance: even with massive real-world data, computed balance is a real but *small* signal. This sets a quantitative ceiling on what any balance formula can explain for real images.

### 5.6 Locher and colleagues — balance in production and at first glance
**Locher, Stappers & Overbeeke (1998), "The role of balance as an organizing design principle underlying adults' compositional strategies for creating visual displays." *Acta Psychologica*, 99, 141–161.**
- DOI: 10.1016/S0001-6918(98)00008-0 · Paywalled.
- Production method: participants built "interesting and pleasant" designs from nine identical shapes of different sizes in a square frame; the resulting compositions' centers of gravity fell close to the frame's geometric center. Mechanical balance *is* used as a construction principle when elements can be freely placed — a counterweight to the Hübner & Thömmes result, suggesting the answer depends on the task and materials. (Hübner & Thömmes, 2019, synthesize: with multiple freely placeable elements, the geometric center functions as an "anchor"; with two fixed elements on a horizontal line, closeness and symmetry win.)
- Related: Locher, Stappers et al. (1999), "An empirical evaluation of the visual rightness theory of pictorial composition," *Acta Psychologica*, 103, 261–280 (verified via Stappers's publication list); Locher, Cornelis et al. (2001), "An empirical investigation of the role of balance in the creation of visual designs by adults," *Empirical Studies of the Arts*, 19(2), 213–227.
- Also: Locher's "at first glance" program — experiments in which balanced paintings and reconstructed less-balanced versions (color and B/W) were rated for balance after 100 ms (single fixation) vs. 5 s: both trained and untrained observers discriminated balance with a single glance, and longer viewing did not change the assessment. (As summarized in Locher, 2015, "The aesthetic experience with visual art 'at first glance'" — `UNVERIFIED` on the original paper's exact identity; the finding is reported in the 2015 chapter.)
- Relevance: balance detection is fast, spontaneous, and bottom-up — consistent with the biorxiv preprint's framing of balance as a "bottom-up aesthetic property mediated by eye movements" (preprint, 2020.05.26.104687 — `UNVERIFIED` on authorship; cited here as a pointer, not a source).

### 5.7 Samuel & Kerzel (2013) — equilibrium ≠ aesthetics
**"Judging Whether it is Aesthetic: Does Equilibrium Compensate for the Lack of Symmetry?" *i-Perception*, 4(1), 57–77.**
- DOI: 10.1068/i0557 · Open access (PMCID: PMC3690416, PMID: 23799188).
- What they did: two experiments with two- or three-rectangle compositions; asked whether "equilibrated" compositions (center of mass at the composition's center) are liked as much as symmetric ones, and whether aesthetics, balance, and weight ratings dissociate.
- What they found: CoM position influenced *weight* ratings strongly but *aesthetics* ratings only slightly; the overall shape of the rectangles influenced aesthetics more than weight. Balance ratings sat between the two — but when area ratios varied, balance ratings became independent of both. **Equilibrium does not compensate for lack of symmetry.**
- Relevance: even when the physics is right (CoM centered), people don't call it beautiful. The formula's output and the aesthetic judgment are different things.

### 5.8 Koenderink, van Doorn, Pinna & Pont (2017) — weight is not photometry
**"Compositorial 'Weight' & 'Luminance'." *Art & Perception*, 5(3), 299–311.**
- DOI: 10.1163/22134913-00002067 · Free PDF via Utrecht University repository.
- What they did: the extreme case — balancing a white patch against a black patch on a common mid-gray ground. If weight were luminance, this would be trivially solvable.
- What they found: it isn't. Balance judgments were affected by size, edge quality, shape, position in the frame, and — critically — the *background tone*: changing the ground flips which side the composition "veers" toward. "Compositorial 'weight' may derive from very different qualities than the mere photometric or colorimetric ones." They cite the design literature's factor list (Dondis, 1973; Graves, 1951; Taylor, 1964; Wong, 1993): size, edge quality, shape, position.
- Relevance: **the most direct evidence against an exact pixel-based formula.** Weight is relational (figure–ground), not a property of pixel groups alone. Any formula built on saturation/hue/lightness/area/position *of the pixel group in isolation* misses the background-dependence and edge-quality-dependence the data show.

### 5.9 Symmetry preference (adjacent Tier 1)
- **Enquist & Arak (1994), "Symmetry, beauty and evolution." *Nature*, 372, 169–172.** DOI: 10.1038/372169a0 · Paywalled. The classic evolutionary account: preference for symmetry arises as a by-product of sensory biases in mate/recognition systems — symmetry preference is a deep, pre-aesthetic bias, which explains why bilateral symmetry keeps beating mechanical balance in composition tasks.
- **Bertamini, Silvanto, Norcia, Makin & Wagemans (2018), "The neural basis of visual symmetry and its role in mid- and high-level visual processing." *Annals of the New York Academy of Sciences*, 1426(1), 111–126.** DOI: 10.1111/nyas.13667 · Paywalled (open copy at the University of Liverpool repository). Review of the neuroscience: symmetry evokes an automatic response in extrastriate cortex (starting in V3, through LOC and VO1), independent of task — a neural reason symmetry is the strongest single compositional cue.
- **Palmer, Schloss & Sammartino (2013), "Visual aesthetics and human preference." *Annual Review of Psychology*, 64, 77–107.** DOI: 10.1146/annurev-psych-120710-100504 · Paywalled. The field's standard review: aesthetic response decomposes into many components (color, spatial structure, shape properties, composition within a frame, individual differences); theoretical accounts include fluency, ecological valence, prototypes. Sets the frame: balance is one component of a multi-component system — no single formula can carry aesthetic judgment alone.

---

## 6. Visual-weight factors the literature identifies (feeding the formula question)

Consolidated across Tier 1 and Tier 2, with the strongest source for each:

| Factor (heavier →) | Sources |
|---|---|
| Larger size / area | Arnheim (ch. 1); Berlyne; Pierce (1894); Puffer (1903); Locher et al. (1998) |
| Greater distance from the balance point (lever arm) | Ross (1907); Arnheim (ch. 1) |
| Higher position in the frame | Arnheim (ch. 1); Gershoni & Hochstein (2011, ecological account) |
| Right-side placement (vs. left) | Arnheim tradition (design-textbook attribution) |
| On-axis / central placement on the structural skeleton | Arnheim (ch. 1); APB formalization |
| Darker value relative to background (figure–ground contrast, not absolute luminance) | Arnheim (ch. 1); Koenderink et al. (2017) |
| Background tone itself (flips the direction of imbalance) | Koenderink et al. (2017) |
| Warm / advancing hue; high chroma | Arnheim (ch. 1); Bullough (1907); Pinkerton & Humphrey (1974) via Gershoni & Hochstein |
| Shape regularity / compactness | Arnheim (ch. 1); design literature (Dondis; Graves; Taylor; Wong via Koenderink) |
| Vertical over horizontal orientation; diagonal heaviest | Arnheim tradition |
| Sharp / high-quality edges over soft ones | Koenderink et al. (2017) |
| Texture / density | Gershoni & Hochstein (2011) factor list; design lore |
| Detail, complexity, intrinsic interest ("interest" as weight) | Arnheim (ch. 1); Gershoni & Hochstein (2011) |
| Isolation (empty surround amplifies weight) | Arnheim tradition |
| Grouping / proximity (grouped elements act as one mass) | Gestalt grouping; Hübner & Thömmes (2019) |
| Horizontal/vertical over oblique (aesthetic oblique effect) | Gershoni & Hochstein (2011); Latto & Russel-Duff; Plumhoff & Schirillo |
| Vertical symmetry (global configural factor) | Gershoni & Hochstein (2011) |
| Meaning / salience (faces, text, recognizable objects) | McManus et al. (2011) note salient features break geometric balance; eye-movement literature (Locher & Nodine) |
| Low placement → perceived *stability* rather than weight | Pierce (1894); Hübner & Fillinger (2019) |

Note what resists quantification: edge quality, "interest," meaning, background-relational effects, and the balance-vs.-stability interpretation switch. These are exactly the terms a pixel-group formula would have to absorb.

---

## 7. Verdict from perception science on the "exact formula" question

1. **Ross (1907) already stated the ambition and the limit**: unequal attractions balance at distances inversely proportional to them — but once tones, measures, shapes, and *qualities* enter, "calculations and reasoning becomes difficult if not impossible."
2. **Formulas exist for restricted domains.** DCM (center-of-mass deviation) and APB (Arnheim's axes formalized) are exact, computable formulas, and they predict human balance ratings well (up to ~68% of variance) — but only for simple, homogeneous, abstract stimuli.
3. **The formulas break on real images.** They fail on Japanese calligraphy (Gershoni & Hochstein, 2011; Fillinger & Hübner, 2018), explain only ~10% of real-world liking for photographs (Thömmes & Hübner, 2018), and the literal physicalist reading of Arnheim fails controlled paired comparisons (McManus et al., 2011).
4. **Weight is not a pixel property.** Koenderink et al. (2017) show compositorial weight depends on figure–ground relations and edge quality in ways photometry cannot capture — a direct problem for any formula built from per-pixel-group factors (saturation, hue, lightness, area) alone.
5. **"Balance" is two things.** Mechanical balance and gravitational stability are different judgments, applied to different picture types (Hübner & Fillinger, 2019). A single formula cannot output both.
6. **Balance ≠ beauty.** Even perfect equilibrium doesn't buy aesthetic preference (Samuel & Kerzel, 2013); symmetry and closeness outrank balance in production tasks (Hübner & Thömmes, 2019); balance is one component among many (Palmer et al., 2013).

Net: perception science says **no exact, general formula exists**, and the evidence suggests the missing terms are relational, configural, and semantic — the hardest things to formalize. A formula is achievable *within* narrowly constrained stimulus classes (geometric abstractions), which is itself a useful, honest result for the research project.

---

## 8. Bibliography

### Tier 1 — peer-reviewed (all verified to exist)

1. McManus, I. C., Stöver, K., & Kim, D. (2011). Arnheim's Gestalt theory of visual balance: Examining the compositional structure of art photographs and abstract images. *i-Perception*, *2*, 615–647. https://doi.org/10.1068/i0445aap — **Open** (https://pmc.ncbi.nlm.nih.gov/articles/PMC3485801/)
2. Gershoni, S., & Hochstein, S. (2011). Measuring pictorial balance perception at first glance using Japanese calligraphy. *i-Perception*, *2*(6), 508–527. https://doi.org/10.1068/i0472 — **Free** (PDF copies in circulation; e.g., author-shared copies)
3. Hübner, R., & Fillinger, M. G. (2019). Perceptual balance, stability, and aesthetic appreciation: Their relations depend on the picture type. *i-Perception*, *10*(3), 2041669519856040. https://doi.org/10.1177/2041669519856040 — **Open**
4. Hübner, R., & Thömmes, K. (2019). Symmetry and balance as factors of aesthetic appreciation: Ethel Puffer's (1903) "Studies in Symmetry" revised. *Symmetry*, *11*(12), 1468. https://doi.org/10.3390/sym11121468 — **Open** (https://www.mdpi.com/2073-8994/11/12/1468)
5. Thömmes, K., & Hübner, R. (2018). Instagram Likes for architectural photos can be predicted by quantitative balance measures and curvature. *Frontiers in Psychology*, *9*. — **Open**
6. Samuel, F., & Kerzel, D. (2013). Judging whether it is aesthetic: Does equilibrium compensate for the lack of symmetry? *i-Perception*, *4*(1), 57–77. https://doi.org/10.1068/i0557 — **Open** (https://pmc.ncbi.nlm.nih.gov/articles/PMC3690416/)
7. Koenderink, J. J., van Doorn, A. J., Pinna, B., & Pont, S. C. (2017). Compositorial 'weight' & 'luminance'. *Art & Perception*, *5*(3), 299–311. https://doi.org/10.1163/22134913-00002067 — **Free PDF** (https://dspace.library.uu.nl/bitstream/handle/1874/357747/22134913_005_03_s003_text.pdf?sequence=1)
8. Locher, P. J., Stappers, P. J., & Overbeeke, C. J. (1998). The role of balance as an organizing design principle underlying adults' compositional strategies for creating visual displays. *Acta Psychologica*, *99*, 141–161. https://doi.org/10.1016/S0001-6918(98)00008-0 — **Paywalled**
9. Enquist, M., & Arak, A. (1994). Symmetry, beauty and evolution. *Nature*, *372*, 169–172. https://doi.org/10.1038/372169a0 — **Paywalled**
10. Bertamini, M., Silvanto, J., Norcia, A. M., Makin, A. D. J., & Wagemans, J. (2018). The neural basis of visual symmetry and its role in mid- and high-level visual processing. *Annals of the New York Academy of Sciences*, *1426*(1), 111–126. https://doi.org/10.1111/nyas.13667 — **Paywalled** (open copy at https://livrepository.liverpool.ac.uk/3020920/)
11. Palmer, S. E., Schloss, K. B., & Sammartino, J. (2013). Visual aesthetics and human preference. *Annual Review of Psychology*, *64*, 77–107. https://doi.org/10.1146/annurev-psych-120710-100504 — **Paywalled**
12. Puffer, E. D. (1903). Studies in symmetry. *Psychological Review Monograph Supplements*, *4* (Harvard Psychological Studies, 1), 467–539. — **Historic; scanned copies via archives** (Tier 1 as an empirical study in a peer-reviewed monograph series)
13. Locher, P. J., Cornelis, E., Wagemans, J., & Stappers, P. J. (2001). An empirical investigation of the role of balance in the creation of visual designs by adults. *Empirical Studies of the Arts*, *19*(2), 213–227. — **Paywalled** (verified via Stappers's publication list)
14. Locher, P. J., Stappers, P. J., Overbeeke, C. J., & Stappers, P. J. (1999). An empirical evaluation of the visual rightness theory of pictorial composition. *Acta Psychologica*, *103*, 261–280. — **Paywalled** (verified via Stappers's publication list)

### Tier 2 — books, chapters, essays (foundational or informed, clearly marked)

15. Arnheim, R. (1954/1974). *Art and Visual Perception: A Psychology of the Creative Eye*. Berkeley: University of California Press. — Ch. 1, "Balance": the structural skeleton of the frame, optical center above geometric center, visual-weight factors, dynamic equilibrium. *Foundational; the entire modern literature is a commentary on this chapter.*
16. Arnheim, R. (1982). *The Power of the Center: A Study of Composition in the Visual Arts*. Berkeley: University of California Press. — Extension of the balance/center theory.
17. Ross, D. W. (1907). *A Theory of Pure Design*. Boston: Houghton, Mifflin. — The physicalist formula Arnheim built on ("unequal attractions balance at distances inversely proportional to them").
18. Wertheimer, M. (1923). Untersuchungen zur Lehre von der Gestalt, II. *Psychologische Forschung*, *4*, 301–350. — The law of Prägnanz; preference for regular/symmetrical/simple organization.
19. Köhler, W. (1929/1947). *Gestalt Psychology*. New York: Liveright. — Equilibrium-seeking dynamics of perceptual processes; the force/field metaphor.
20. Köhler, W. (1938). *The Place of Value in a World of Facts*. New York: Liveright. — Perceptual "goodness" as physical equilibrium.
21. Koffka, K. (1935). *Principles of Gestalt Psychology*. New York: Harcourt, Brace. — Systematic statement of Prägnanz: simplicity, unity, regularity, symmetry.
22. Locher, P. (2015). The aesthetic experience with visual art "at first glance." In P. Bundgaard & F. Stjernfeld (Eds.), *Investigations into the Phenomenology and the Ontology of the Work of Art* (pp. 75–88). Springer Open. — Summarizes the first-glance balance-detection experiments (100 ms vs. 5 s viewing).

### UNVERIFIED — mentioned in the literature but not individually confirmed in this pass
- Fillinger, M. G., & Hübner, R. (2018). Reported in Hübner & Fillinger (2019) as replicating the Gershoni & Hochstein calligraphy failure for APB and DCM; exact title/venue not pinned down — do not cite without checking.
- Wilson & Chatterjee (2005). Reported in Hübner & Fillinger (2019) as a simple-stimuli study where DCM predicted liking; exact reference not pinned down — do not cite without checking.
- Pierce, E. (1894). Cited in Hübner & Fillinger (2019) for the balance-vs.-stability distinction (horizontal = balance, vertical = stability; preference for lower-weighted pictures); exact reference not pinned down — do not cite without checking.
- Leder, H., Tinio, P. P. L., Brieber, D., Kröner, T., Jacobsen, T., & Rosenberg, R. (2019). "Symmetry is not a universal law of beauty." *Empirical Studies of the Arts*, *37*, 104–114. — Cited in Hübner & Thömmes (2019); DOI not individually verified.
- Biorxiv preprint 2020.05.26.104687, "Pictorial balance is a bottom-up aesthetic property mediated by eye movements" — authorship not verified in this pass; cited as a pointer only.

---
*End of Worker A deliverable.*
