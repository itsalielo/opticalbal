# Optical Balancing — Round 5: Design-Research Venues

**Date:** 2026-10-09. **Worker brief:** the design discipline's own literature on composing/balancing layouts — design-methods papers on composition, practice-based accounts of how designers balance work, design-research quantification attempts, typography/layout research, and the designerly-ways-of-knowing literature insofar as it touches compositional judgment. Kept tight; no general design-theory survey.

**Venues swept:** *She Ji* (diamond OA), *Artifact* (diamond OA), *Visible Language* (OA), *Design Studies*, *International Journal of Design* (OA to read), *Design Issues*, *CoDesign*, *The Design Journal* — plus *ulm* (HfG Ulm journal) for one design-native quantification that belongs nowhere else.

**Dedup vs Rounds 1–4:** none of the 35 Tier 1 items below appears in the logged corpus (verified by grep over all `optical-balancing-*.md` files). One item — Beier (2016) — was previously logged as Tier 2; it is reclassified to Tier 1 here (it is a peer-reviewed *Visible Language* article) and counted once, flagged as an upgrade. Every item verified by exact-title search with DOI or stable URL.

**Headline result:** the design discipline has produced exactly ONE genuine quantification attempt at a compositional measure — Bonsiepe (1968), and it measures order/complexity, not visual weight. Everything else the venues offer is either (a) experimental work on typographic layout variables, (b) protocol evidence that designers judge compositions perceptually and tacitly, or (c) theory explaining *why* the judgment stays tacit. The design literature thus independently confirms the mission's hard limit: the field never produced w(pixel group) because its own epistemology treats compositional judgment as non-verbalizable.

---

## 1. The design discipline's own quantification attempts — (c)

Thin by design, not by accident. Two genuine formula-shaped contributions in sixty years, both about order/complexity or line measure — never about visual weight.

**Bonsiepe, G. (1968).** "Eine Methode, Ordnung in der typographischen Gestaltung zu quantifizieren / A method of quantifying order in typographic design." *ulm* 21, 24–31. **This is the single most important find of the round (see §7).** Working at the HfG Ulm, Bonsiepe proposed that order in typographic design can be measured rather than only felt. He distinguishes two kinds of order: *system order* (objects sharing common widths and common heights) and *distribution order* (objects sharing common distances from the top and left of the page — explicitly built on the Western top-to-bottom, left-to-right reading pattern). The technique: draw contour lines around each typographic object, classify the objects, and compute the layout's complexity C from the class proportions using a Shannon-derived formula, C = −Σ p_i log₂ p_i. High alignment across few classes = low C = high order. This is the design field's own first computable compositional measure — information aesthetics applied to the page, eight years before the design-methods movement's peak. It quantifies *order*, not *weight*: it says nothing about how heavy a red square feels versus a gray one, which is exactly the mission's gap. Venue caveat: *ulm* was the HfG Ulm's edited school journal, not a modern double-blind journal — Tier 1 with that note. Citation verified via the Monoskop Bonsiepe bibliography (exact title, venue, year, pages); no DOI exists for 1968 *ulm*.

**Comber, T., & Maltby, J. R. (1997).** "Layout complexity: does it measure usability?" In S. Howard, J. Hammond & G. Lindgaard (eds.), *Human–computer interaction: Interact '97* (pp. 623–626). Chapman & Hall, London. Peer-reviewed conference paper; the documented second life of Bonsiepe's metric. They port the technique to GUI screens — classifying screen objects by common dimensions and positions — and test whether the resulting complexity score predicts usability. Pilot finding: users preferred screens midway between simple and complex, not the simplest ones the guidelines recommended. For the mission: the only empirical test of a design-native compositional formula, and it immediately found that *minimal complexity is not the optimum* — a warning for any balance formula that treats "more ordered" as "better."

**Peña, E. (2016).** "Calculating line length: An arithmetic approach." *Visible Language*, 50(1), 112–125. Stable URL: https://journals.uc.edu/index.php/vl/article/download/5917/4781/7594. An actual arithmetic formula for a typographic layout decision, published in a design journal: line length = LCA′ × Cρ × S, where LCA′ is the length of the lowercase alphabet plus a space character, Cρ the desired character density, and S a constant (≈0.0345). A short-range study across common serif text faces held error under 5%. Narrow domain — line measure, not balance — but it is proof that the design venues *do* publish closed-form layout formulas when the problem is constrained enough. The contrast with the total absence of any weight formula is the point.

---

## 2. Protocol studies: what designers actually do when they compose — (b)

The *Design Studies* protocol-analysis tradition is the closest the design discipline comes to documenting compositional judgment in the act. Its consistent finding: designers inspect their own marks, perceive relations they did not intend, and judge the result perceptually — "seeing" is the instrument, and it resists verbalization.

**Suwa, M., & Tversky, B. (1997).** "What do architects and students perceive in their design sketches? A protocol analysis." *Design Studies*, 18(4), 385–403. https://doi.org/10.1016/S0142-694X(97)00008-2. Architects designed a museum on video, then narrated every pen stroke retrospectively. The coding scheme's "spatial relations" and "emergent properties" categories are the paper's record of compositional perception: designers report seeing things like "too sharp a corner," symmetries, axes, and configurations — perceptual judgments about the arrangement itself, distinct from functional inferences. Experts differed from students mainly in making *functional* inferences from sketches; the perceptual seeing was shared. Full text archived at the authors' Columbia page (PII S0142-694X(97)00008-2).

**Suwa, M., Purcell, T., & Gero, J. S. (1998).** "Macroscopic analysis of design processes based on a scheme for coding designers' cognitive actions." *Design Studies*, 19(4), 455–483. https://doi.org/10.1016/S0142-694X(98)00016-7. The coding scheme that made the above legible: designers' actions sorted into physical, perceptual, functional, and conceptual levels, with dependencies and triggering relations coded between levels. For the mission it matters as method: it gives "perceptual action" a formal slot in design protocols — the category under which every optical-balancing judgment a designer ever made would fall — without ever being able to say what the judgment's content was.

**Purcell, A. T., & Gero, J. S. (1998).** "Drawings and the design process: A review of protocol studies in design and other disciplines and related research in cognitive psychology." *Design Studies*, 19(4), 389–430. https://doi.org/10.1016/S0142-694X(98)00015-5. The review that consolidates the protocol literature. Useful here as the methodological anchor: it establishes that think-aloud and retrospective protocols are the design field's validated instrument for studying judgment-in-action — the instrument any future study of designers making balancing decisions would use.

**Kavakli, M., & Gero, J. S. (2001).** "Sketching as mental imagery processing." *Design Studies*, 22(4), 347–364. https://doi.org/10.1016/S0142-694X(01)00002-3 — plus the companion **Kavakli, M., & Gero, J. S. (2002).** "The structure of concurrent cognitive actions: A case study on novice and expert designers." *Design Studies*, 23(1), 25–40. https://doi.org/10.1016/S0142-694X(01)00021-7. Protocol evidence that concurrent perceptual and conceptual actions structure designing differently in novices versus experts. Relevant as the expertise gradient behind "the designer's eye": the perceptual judgments that constitute optical balancing are part of what expertise *is* in this literature.

**Oxman, R. (2002).** "The thinking eye: visual re-cognition in design emergence." *Design Studies*, 23(2), 135–164. https://doi.org/10.1016/S0142-694X(01)00026-6. Argues that designers literally see new visual structures in their own emerging drawings — re-cognition — and that this visual emergence drives the design forward. The paper's model of designing is a loop of drawing, seeing, and re-seeing; compositional decisions (what goes where, what dominates) are made inside that loop, by the eye, not by rule.

**Goldschmidt, G. (1994).** "On visual design thinking: the vis kids of architecture." *Design Studies*, 15(2), 158–174. https://doi.org/10.1016/0142-694X(94)90022-1. The "seeing as / seeing that" dialectic: designers oscillate between seeing a sketch *as* something (interpretation) and seeing *that* something is the case about it (factual visual pickup — proportions, alignments, emphases). The "seeing that" modality is where optical-balancing judgments live, and Goldschmidt's framework is the design literature's most precise description of their phenomenology.

**Goldschmidt, G. (2003).** "The backtalk of self-generated sketches." *Design Issues*, 19(1), 72–88. https://doi.org/10.1162/074793603762667728. Extends the dialectic: sketches "talk back" — they present the designer with unintended visual information (a heaviness here, an imbalance there) that the designer then answers. This is the design-venue description of the exact moment optical balancing happens: the artifact returns perceptual information the maker did not put there deliberately, and the maker adjusts.

**Goldschmidt, G. (2007).** "To see eye to eye: The role of visual representations in building shared mental models in design teams." *CoDesign*, 3(1), 43–50. https://doi.org/10.1080/15710880601170826. The one on-point *CoDesign* item: visual representations coordinate team members' mental models precisely because they carry visual information — configuration, emphasis, arrangement — that survives translation into words poorly. Indirect support for the non-verbalizability thesis.

**Stones, C., & Cassidy, T. (2007).** "Comparing synthesis strategies of novice graphic designers using digital and traditional design tools." *Design Studies*, 28(1), 59–72. https://doi.org/10.1016/j.destud.2006.09.001. The rare *graphic-design*-specific empirical study in the corpus: novice graphic designers given synthesis (composition) tasks on paper versus computer. Paper supported more solutions and better reinterpretation; the authors note that working with symbolic systems like fonts during synthesis can restrict the scope of ideas. For the mission: composing with finished, specified elements (typefaces) constrains exploration relative to sketching — a small caution about studying balancing decisions only in high-fidelity tools.

## 3. Designerly ways of knowing: why the judgment stays tacit — (e)

Kept to the papers that touch compositional judgment directly. The through-line, from Cross (1982) through Schön & Wiggins (1992) to Gentes & Marcocchia (2023): designers make reliable qualitative visual judgments they cannot state as rules — which is both the explanation for the practitioner's silence on numbers (Round 4's finding) and the epistemological obstacle to the exact formula.

**Cross, N. (1982).** "Designerly ways of knowing." *Design Studies*, 3(4), 221–227. https://doi.org/10.1016/0142-694X(82)90040-0. The founding claim: design is a "third area" of education alongside sciences and humanities, with its own ways of knowing — modelling, pattern-formation, synthesis — whose values are practicality, ingenuity, and appropriateness rather than truth or justice. Compositional judgment is the unexplicated core of that claim: the paper asserts the faculty without decomposing it.

**Cross, N. (2001).** "Designerly ways of knowing: Design discipline versus design science." *Design Issues*, 17(3), 49–55. https://doi.org/10.1162/074793601750357196. The sequel: warns against absorbing design into design science, defending the designerly mode as irreducible to scientific method. Read against the mission: the exact formula is a design-science ambition; this paper is the clearest statement of why the design discipline resists it.

**Schön, D. A., & Wiggins, G. (1992).** "Kinds of seeing and their functions in designing." *Design Studies*, 13(2), 135–156. https://doi.org/10.1016/0142-694X(92)90268-F. The theoretical keystone for (e). Designing proceeds as seeing–moving–seeing; designers appreciate spatial Gestalts and recognize qualities of configurations that they cannot describe as rules — the paper quotes Christopher Alexander's observation that the ability to recognize qualities of a spatial configuration does not depend on being able to state the rules of recognition, and notes that even when designers make qualitative judgments tacitly, they cannot necessarily make the criteria explicit. That is the whole optical-balancing problem in one paragraph: the eye knows, the mouth cannot say, so no formula gets written down.

**Cross, N. (2004).** "Expertise in design: an overview." *Design Studies*, 25(5), 427–441. https://doi.org/10.1016/j.destud.2004.06.002. Review of design-expertise research: expert designers differ from novices in solution-focused strategy, and design expertise has aspects significantly different from expertise in other fields. The compositional eye is part of that difference, though the review never isolates it.

**Stolterman, E. (2008).** "The nature of design practice and implications for interaction design research." *International Journal of Design*, 2(1), 55–65. Stable URL: https://ijdesign.org/index.php/IJDesign/article/viewFile/240./139. Argues that design complexity is not scientific complexity and that research aimed at supporting practice must be grounded in the nature of practice itself. The paper's account of practice centers on judgment under conditions practitioners cannot fully articulate — the same tacit-judgment structure, stated as a programmatic claim about what design research may and may not formalize.

**Gentes, A., & Marcocchia, G. (2023).** "The forgotten legacy of Schön: From materials to 'mediums' in the design activity." *Design Issues*, 39(2), 3–13. https://doi.org/10.1162/desi_a_00713. Re-reads Schön for contemporary design: designing is a reflective conversation with materials, and the concepts that matter — tacit knowledge, reflection-in-action — describe judgment that operates below explicit articulation. Included as the current *Design Issues* statement of the tacit-judgment position.

**Goldschmidt, G. (2017).** "Design thinking: A method or a gateway into design cognition?" *She Ji*, 3(2), 107–112. https://doi.org/10.1016/j.sheji.2017.10.009. Distinguishes design thinking as a portable method from design cognition as the underlying mental reality; argues the latter is what needs studying. For the mission: a *She Ji* voice saying the method-talk misses the cognition — and compositional judgment belongs to the cognition side.

**Lindgaard, K., & Wesselius, H. (2017).** "Once more, with feeling: Design thinking and embodied cognition." *She Ji*, 3(2), 83–92. https://doi.org/10.1016/j.sheji.2017.05.004. Argues design cognition is embodied — feeling and bodily response are part of judgment, not noise around it. If compositional judgments are partly affective/bodily, a purely stimulus-side formula faces one more principled obstacle. Included for that implication, stated briefly.

---

## 4. Typography and layout: the Visible Language / Design Journal record — (d)

*Visible Language* is the richest design venue for this problematic: it publishes both craft knowledge and experiments on the typographic variables, and it is where the field has come closest to saying "here is what we can and cannot quantify."

**Friedman, D. (1973).** "A view: Introductory education in typography." *Visible Language*, 7(2), 129–144. Issue ToC: https://journals.uc.edu/index.php/vl/issue/download/323/87. A 1973 call — filed as "A View," i.e., a position piece — for typography teaching grounded in the "generically perceptual or purely syntactic characteristics of arranging type on the page" rather than in outdated mechanics. His exercise program varies position, weight, size, slant, spacing, and clustering within square (neutral) compositions and asks students to observe the perceptual effects. The earliest design-venue statement found of the program the mission inherits: composition taught as perceptual experiment, with the variables named but their interactions unquantified.

**Lonsdale, M. D. S. (2014).** "Typographic features of text. Outcomes from research and practice." *Visible Language*, 48(3), 29–67. PDF: https://eprints.whiterose.ac.uk/id/eprint/82895/11/VisibleLanguage-48-3_28-67-Lonsdale-TypeFeatures.pdf. A systematic review mapping what research and practice each say about typographic features — including the nearest thing the literature offers to quantified spacing judgments: for 10–12 pt text, "too wide" letter spacing ≈ above a thick space (⅓ em), "too close" ≈ below a thin space (⅕–⅛ em), with the explicit admission that "research and practice are yet to give us quantifiable definitions for 'too wide' and 'too close.'" Also documents the interaction the mission keeps hitting: features must be judged as groups, not in isolation (size × spacing × configuration trade off).

**Moys, J.-L. (2014).** "Investigating readers' impressions of typographic differentiation using repertory grids." *Visible Language*, 47(3), 91–118. Using Kelly's repertory-grid technique on magazine layouts, Moys derives three patterns of typographic differentiation (high, moderate, low) — high: irregular, tight, overlapping elements; moderate: orderly columns, rules, even space distribution; low: generous white space, symmetrical or strikingly balanced. This is a *descriptive taxonomy of composed layouts* built from readers' own constructs — the design venue's empirical answer to "what do composed pages look like," though it measures impressions, not the weights that produce them.

**Moys, J.-L. (2014).** "Typographic layout and first impressions – testing how changes in text layout influence readers' judgments of documents." *Visible Language*, 48(1), 46–72. https://centaur.reading.ac.uk/39859/ (refereed). Paired-comparison experiment: six controlled documents varying only in the layout attributes of the three differentiation patterns. Finding: the layout-attribute clusters shift readers' rhetorical judgments even with content and stylistic range controlled — and, crucially, the author stresses that *inter-relationships between clusters of attributes* matter more than isolated variables. That non-additivity verdict, from inside the design literature, rhymes with the compute track's identifiability result.

**Beier, S., & Dyson, M. C. (2014).** "The influence of serifs on 'h' and 'i': Useful knowledge from design-led scientific research." *Visible Language*, 47(3), 74–95. https://journals.uc.edu/index.php/vl/article/view/5875. A model of what Beier (2016) prescribes: design-led experiments on letterforms, with test materials built from design knowledge. Included as the working example of the collaboration the field says it needs.

**Lonsdale, M. D. S. (2016).** "Typographic features of text and their contribution to the legibility of academic reading materials: an empirical study." *Visible Language*, 50(1), 79–111. Experimental follow-up: layouts conforming to legibility guidelines improved search-reading performance with and without time pressure, and were rated easiest and most attractive. The paper's theoretical model locates layout effects at the *perceptual* level of reading — the closest the VL line comes to granting layout a perceptual (rather than merely cognitive) mechanism.

**Beier, S. (2016).** "Letterform research: An academic orphan." *Visible Language*, 50(2), 64–79. https://journals.uc.edu/index.php/vl/article/view/5923. **Reclassified Tier 2 → Tier 1** (it is a peer-reviewed journal article; previously logged from the typography round as a practitioner essay). The diagnosis the mission needs from inside the discipline: letterform research never found an academic home, so its questions were set by other disciplines' interests; progress requires experiments built on design knowledge, reading-research results, and no more hunting for universal answers. Replace "letterform" with "visual weight" and this is the mission's own situation report.

**Dyson, M. C. (2013).** "Where theory meets practice: A critical comparison of research into identifying letters and craft knowledge of type design." *The Design Journal*, 16(3), 271–294. https://doi.org/10.2752/175630613X13660502571741. Directly compares what reading research knows about letter identification with what type designers know from craft — and finds the two bodies of knowledge misaligned in scope and grain. The paper is the *Design Journal* version of the Beier diagnosis: craft knowledge (the eye) and research knowledge (the lab) are not yet commensurable, which is why no formula crosses the gap.

**Thiessen, M., Beier, S., & Keage, H. (2020).** "A review of the cognitive effects of disfluent typography on functional reading." *The Design Journal*, 23(5), 797–815. https://doi.org/10.1080/14606925.2020.1810434. Review of how typographic disfluency affects reading — included briefly as evidence that *The Design Journal* now carries perception-grounded typography research; adjacent rather than central (reading, not balance).

**Peña, E. (2025).** "About visual acuity and type design: A protocol." *Design Issues*, 41(2), 71–. https://direct.mit.edu/desi/article-abstract/41/2/71/128593/About-Visual-Acuity-and-Type-Design-A-Protocol. Newest item in the round: derives a protocol from optometric visual-acuity principles to calculate the *relative acuity of typographic signs* and guide type design decisions. This is the design venue's 2025 attempt to ground a typographic judgment in vision science with numbers — the closest living relative of the mission's program on the type side. Worth tracking for follow-up work.

---

## 5. Graphic design theory in Design Issues and She Ji — (a)

**Frascara, J. (1988).** "Graphic design: Fine art or social science?" *Design Issues*, 5(1), 18–29. https://doi.org/10.2307/1511556. The founding theory paper for graphic design as a discipline. Two points touch the problematic directly: (1) Gestalt psychology "replaced intuitive rules for what was called composition" in visual-fundamentals teaching — i.e., the field *already* underwent one rationalization of composition, from rules-of-thumb to perceptual theory, and it stopped at theory, never reaching formula; (2) Frascara argues visual decisions should be based "not only on compositional concerns, but also, and chiefly, on the study of human communication" — the receiver-centered move that pulls the field away from stimulus-side formalization.

**Frascara, J. (2022).** "Revisiting 'Graphic design: Fine art or social science?' — The question of quality in communication design." *She Ji*, 8(2), 270–288. https://doi.org/10.1016/j.sheji.2022.05.002. Thirty-four years later, in *She Ji*: returns to the quality question, arguing for explicable decision processes in graphic design. The arc 1988→2022 is the field's own record of *wanting* explicability and still not having a compositional calculus.

**Moszkowicz, J. (2011).** "Gestalt and graphic design: An exploration of the humanistic and therapeutic effects of visual organization." *Design Issues*, 27(4), 56–67. https://doi.org/10.1162/DESI_a_00105. Applies Gestalt principles to graphic design practice; included as the *Design Issues* instance of the Gestalt-composition lineage the mission already knows from Arnheim — showing the design venue treats it as design theory, not as a measurement program.

**Lomas, J. D., & Xue, H. (2022).** "Harmony in design: A synthesis of literature from classical philosophy, the sciences, economics, and design." *She Ji*, 8(1), 5–64. https://doi.org/10.1016/j.sheji.2022.01.001. A 60-page *She Ji* synthesis whose conclusion — harmony is the integration of diversity into a greater whole, not sameness — is the design discipline's contemporary philosophical statement of what compositions are *for*. No formula, deliberately: it is the anti-reductionist pole of the literature. Included to mark the boundary of what the venues will claim.

---

## 6. Two-tier bibliography

### Tier 1 — peer-reviewed (35 items; 34 new + 1 reclassified)

*Design Studies*
- Cross, N. (1982). Designerly ways of knowing. *Design Studies*, 3(4), 221–227. https://doi.org/10.1016/0142-694X(82)90040-0
- Schön, D. A., & Wiggins, G. (1992). Kinds of seeing and their functions in designing. *Design Studies*, 13(2), 135–156. https://doi.org/10.1016/0142-694X(92)90268-F
- Goldschmidt, G. (1994). On visual design thinking: the vis kids of architecture. *Design Studies*, 15(2), 158–174. https://doi.org/10.1016/0142-694X(94)90022-1
- Suwa, M., & Tversky, B. (1997). What do architects and students perceive in their design sketches? A protocol analysis. *Design Studies*, 18(4), 385–403. https://doi.org/10.1016/S0142-694X(97)00008-2
- Purcell, A. T., & Gero, J. S. (1998). Drawings and the design process: A review of protocol studies in design and other disciplines and related research in cognitive psychology. *Design Studies*, 19(4), 389–430. https://doi.org/10.1016/S0142-694X(98)00015-5
- Suwa, M., Purcell, T., & Gero, J. S. (1998). Macroscopic analysis of design processes based on a scheme for coding designers' cognitive actions. *Design Studies*, 19(4), 455–483. https://doi.org/10.1016/S0142-694X(98)00016-7
- Kavakli, M., & Gero, J. S. (2001). Sketching as mental imagery processing. *Design Studies*, 22(4), 347–364. https://doi.org/10.1016/S0142-694X(01)00002-3
- Kavakli, M., & Gero, J. S. (2002). The structure of concurrent cognitive actions: A case study on novice and expert designers. *Design Studies*, 23(1), 25–40. https://doi.org/10.1016/S0142-694X(01)00021-7
- Oxman, R. (2002). The thinking eye: visual re-cognition in design emergence. *Design Studies*, 23(2), 135–164. https://doi.org/10.1016/S0142-694X(01)00026-6
- Cross, N. (2004). Expertise in design: an overview. *Design Studies*, 25(5), 427–441. https://doi.org/10.1016/j.destud.2004.06.002
- Stones, C., & Cassidy, T. (2007). Comparing synthesis strategies of novice graphic designers using digital and traditional design tools. *Design Studies*, 28(1), 59–72. https://doi.org/10.1016/j.destud.2006.09.001

*Design Issues*
- Frascara, J. (1988). Graphic design: Fine art or social science? *Design Issues*, 5(1), 18–29. https://doi.org/10.2307/1511556
- Cross, N. (2001). Designerly ways of knowing: Design discipline versus design science. *Design Issues*, 17(3), 49–55. https://doi.org/10.1162/074793601750357196
- Goldschmidt, G. (2003). The backtalk of self-generated sketches. *Design Issues*, 19(1), 72–88. https://doi.org/10.1162/074793603762667728
- Moszkowicz, J. (2011). Gestalt and graphic design: An exploration of the humanistic and therapeutic effects of visual organization. *Design Issues*, 27(4), 56–67. https://doi.org/10.1162/DESI_a_00105
- Gentes, A., & Marcocchia, G. (2023). The forgotten legacy of Schön: From materials to "mediums" in the design activity. *Design Issues*, 39(2), 3–13. https://doi.org/10.1162/desi_a_00713
- Peña, E. (2025). About visual acuity and type design: A protocol. *Design Issues*, 41(2), 71–. https://direct.mit.edu/desi/article-abstract/41/2/71/128593/About-Visual-Acuity-and-Type-Design-A-Protocol

*Visible Language*
- Friedman, D. (1973). A view: Introductory education in typography. *Visible Language*, 7(2), 129–144. Issue ToC: https://journals.uc.edu/index.php/vl/issue/download/323/87
- Moys, J.-L. (2014). Investigating readers' impressions of typographic differentiation using repertory grids. *Visible Language*, 47(3), 91–118.
- Beier, S., & Dyson, M. C. (2014). The influence of serifs on 'h' and 'i': Useful knowledge from design-led scientific research. *Visible Language*, 47(3), 74–95. https://journals.uc.edu/index.php/vl/article/view/5875
- Lonsdale, M. D. S. (2014). Typographic features of text. Outcomes from research and practice. *Visible Language*, 48(3), 29–67. PDF: https://eprints.whiterose.ac.uk/id/eprint/82895/11/VisibleLanguage-48-3_28-67-Lonsdale-TypeFeatures.pdf
- Moys, J.-L. (2014). Typographic layout and first impressions – testing how changes in text layout influence readers' judgments of documents. *Visible Language*, 48(1), 46–72. https://centaur.reading.ac.uk/39859/
- Peña, E. (2016). Calculating line length: An arithmetic approach. *Visible Language*, 50(1), 112–125. https://journals.uc.edu/index.php/vl/article/download/5917/4781/7594
- Lonsdale, M. D. S. (2016). Typographic features of text and their contribution to the legibility of academic reading materials: an empirical study. *Visible Language*, 50(1), 79–111.
- Beier, S. (2016). Letterform research: An academic orphan. *Visible Language*, 50(2), 64–79. https://journals.uc.edu/index.php/vl/article/view/5923 — **reclassified from Tier 2** (Round 1) to Tier 1.

*The Design Journal*
- Dyson, M. C. (2013). Where theory meets practice: A critical comparison of research into identifying letters and craft knowledge of type design. *The Design Journal*, 16(3), 271–294. https://doi.org/10.2752/175630613X13660502571741
- Thiessen, M., Beier, S., & Keage, H. (2020). A review of the cognitive effects of disfluent typography on functional reading. *The Design Journal*, 23(5), 797–815. https://doi.org/10.1080/14606925.2020.1810434

*She Ji*
- Goldschmidt, G. (2017). Design thinking: A method or a gateway into design cognition? *She Ji*, 3(2), 107–112. https://doi.org/10.1016/j.sheji.2017.10.009
- Lindgaard, K., & Wesselius, H. (2017). Once more, with feeling: Design thinking and embodied cognition. *She Ji*, 3(2), 83–92. https://doi.org/10.1016/j.sheji.2017.05.004
- Lomas, J. D., & Xue, H. (2022). Harmony in design: A synthesis of literature from classical philosophy, the sciences, economics, and design. *She Ji*, 8(1), 5–64. https://doi.org/10.1016/j.sheji.2022.01.001
- Frascara, J. (2022). Revisiting "Graphic design: Fine art or social science?" – The question of quality in communication design. *She Ji*, 8(2), 270–288. https://doi.org/10.1016/j.sheji.2022.05.002

*International Journal of Design*
- Stolterman, E. (2008). The nature of design practice and implications for interaction design research. *International Journal of Design*, 2(1), 55–65. https://ijdesign.org/index.php/IJDesign/article/viewFile/240./139

*CoDesign*
- Goldschmidt, G. (2007). To see eye to eye: The role of visual representations in building shared mental models in design teams. *CoDesign*, 3(1), 43–50. https://doi.org/10.1080/15710880601170826

*Design-native quantification lineage (outside the 8, kept for (c))*
- Bonsiepe, G. (1968). Eine Methode, Ordnung in der typographischen Gestaltung zu quantifizieren / A method of quantifying order in typographic design. *ulm*, 21, 24–31. No DOI (pre-DOI journal); citation verified via Monoskop Bonsiepe bibliography. Venue note: HfG Ulm's edited school journal.
- Comber, T., & Maltby, J. R. (1997). Layout complexity: does it measure usability? In S. Howard, J. Hammond & G. Lindgaard (eds.), *Human–computer interaction: Interact '97* (pp. 623–626). Chapman & Hall. Peer-reviewed proceedings; applies Bonsiepe's metric to GUIs.

### Tier 2 — informed non-academic (4 items, canonical practitioner texts)

- Müller-Brockmann, J. (1981). *Grid systems in graphic design: A visual communication manual for graphic designers, typographers and three dimensional designers*. Niggli. — The grid bible: the geometric-composition pole against which "optical judgment" defines itself. No quantification of perceived balance; the grid is treated as a construction discipline, with optical correction left to the eye.
- Elam, K. (2001). *Geometry of design: Studies in proportion and composition for graphic designers and illustrators*. Princeton Architectural Press. — Reverse-engineers proportions (golden section, root rectangles) in designed artifacts from nature to Neville Brody. Analytical, not experimental; shows what the practitioner literature means by "compositional analysis" — post-hoc geometric description, never a predictive weight function.
- Bringhurst, R. (2004). *The elements of typographic style* (3rd ed.). Hartley & Marks. — The craft reference behind Peña's (2016) line-length work (Bringhurst's character-density table); the standard statement of typographic proportion as practiced knowledge.
- Lupton, E. (2004). *Thinking with type: A critical guide for designers, writers, editors, & students*. Princeton Architectural Press. — The design-pedagogy statement of typographic hierarchy and layout; cited in Lonsdale (2014) as the practice pole of the research–practice comparison.

---

## 7. Dead ends, exclusions, and venue notes

- ***Artifact* (diamond OA, practice-based):** swept for composition/balance/process papers — nothing on-point surfaced. The closest graphic-design item, Bichler & Beier (2016), "Graphic design for the real world? Visual communication's potential in design activism and design for social change" (*Artifact*, 3(4), DOI 10.14434/artifact.v3i4.12974), is about activism, not composition — excluded as off-brief. The venue's practice-based work runs toward social and material practice, not perceptual formalisms.
- ***CoDesign*:** participatory-design focus; only Goldschmidt (2007) touches visual representation per se. Thin venue for this problematic — one item, kept.
- ***International Journal of Design*:** only Stolterman (2008) on-brief; the journal's aesthetics-adjacent papers (packaging symbolism, interaction aesthetics) mention balance only in passing — excluded to keep the brief tight.
- **Gluth on "Roxane," *Visible Language* 33(3)** (a typeface-design case study foregrounding negative space): exact article title could not be verified — dropped, not listed.
- **Stiff's spine-typography piece, *Visible Language* 34(3/4):** exact title unverifiable from reachable sources — dropped, not listed.
- **Peña's "Font Remix (A Metadesign)"** (*Design Issues*): verified as published, but a metadesign piece, not compositional — excluded.

---

## 8. Net effect on the mission

Round 5's design-venues sweep sharpens the verdict from an unexpected direction. The psychophysics rounds established that no validated w(saturation, hue, lightness, area, position, contrast) exists; this round establishes that **the design discipline never even attempted one** — its single quantification (Bonsiepe 1968) measured order, and its epistemology (Cross → Schön → Stolterman → Gentes) actively defends the non-verbalizability of the judgment. The practitioner's silence on numbers (Round 4) is therefore not an oversight but a disciplinary position: the eye is the instrument, and the literature theorizes *why* it must stay so. Two constructive handholds survive: (1) Bonsiepe's class-proportion method as the design-native template for turning a composition into numbers — the mission's formula would be its weight-carrying successor; (2) the protocol-analysis tradition (Suwa/Tversky/Gero) as the validated method for studying balancing decisions empirically, and Peña (2025) as proof the design journals will still publish vision-grounded quantitative protocols.

### Round 5's single most important find

**Bonsiepe, G. (1968). "Eine Methode, Ordnung in der typographischen Gestaltung zu quantifizieren / A method of quantifying order in typographic design." *ulm* 21, 24–31** (no DOI; citation verified via the Monoskop Gui Bonsiepe bibliography). It is the only genuine quantification attempt the design discipline ever produced for a compositional property of layouts — system order and distribution order from object classifications, complexity C = −Σ p_i log₂ p_i over class proportions — and therefore the true design-native ancestor of the mission's formula program. Its limit is exactly the mission's starting point: it quantifies order, never weight.
