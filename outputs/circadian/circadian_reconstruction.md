# The Eye Clock: Jack Kruse's Circadian Theory Reconstructed

*Built from the 737-post blog archive (`input/kruse_blog_glix/markdown`, June 2011 – January 2026).*

---

## What this document is

Kruse has written about circadian biology in 404 of his 737 posts. It is his single most load-bearing topic — the hinge on which the light-over-food thesis, the mitochondrial theory of disease, and the entire clinical protocol all turn. But it is scattered across fifteen years, four distinct blog series, and at least three substantially different versions of the mechanism.

This reconstruction does three things:

1. **States the theory as a coherent whole** — what he actually argues, in his own logical order rather than his publication order.
2. **Tracks how it changed** from 2011 to 2025. The change is large, and he never announces it. Reading a 2011 post and a 2023 post as if they describe the same model produces nonsense.
3. **Labels the epistemic status of each layer.** Throughout, claims are marked:
   - **[Established]** — mainstream, well-replicated science that Kruse is reporting accurately.
   - **[Contested]** — published and real, but a minority position, weakly replicated, or from a fringe-adjacent group.
   - **[Extrapolation]** — Kruse's own inference. May be reasonable, may not be, but it is not something you will find in a chronobiology textbook.
   - **[Error]** — factually wrong on a checkable point.

The labeling is not an attempt to score points. The framework's most interesting feature is precisely that its foundation is often textbook-correct and the extrapolation is layered on top with no visible seam. Separating the layers is the whole exercise.

**Method note.** All 737 posts were scored on a weighted circadian vocabulary (SCN, melanopsin, clock genes, zeitgeber, entrainment, melatonin, chronodisruption, etc.); 463 posts registered a hit, 62 scored ≥100. The reconstruction draws on a 23-post spine covering the top-scoring posts and the dedicated series — *Time* #1–25 (2015–16), *Ubiquitination* #2/3/16/17 (2015), *Quantum Engineering* #1/18/23/44 (2021–23), the *Decentralized Medicine* applications (2025), and the 2011–13 leptin/sleep foundations. Ranking script: `scripts/rank_circadian.py`; full scores in `outputs/circadian/raw/circadian_rank.json`.

---

## 1. The thesis in one sentence

> **The eye is a clock before it is a camera; that clock is the top of a strict hierarchy that controls every cell in the body; and modern light — blue-heavy, UV-deficient, present at night — breaks the clock, which is the upstream cause of essentially all chronic disease.**

Everything else is machinery attached to that sentence. Note what it *doesn't* say: it makes no claim about calories, macronutrients, or food quality. That absence is deliberate and is the framework's central polemic. His compressed version, from the 2023 year-end review: *"light trumps food."*

---

## 2. The inherited substrate: what he gets right

Before the extrapolations, it is worth being clear about how much correct chronobiology is in these posts. In *Ubiquitination 16* (2015) he lays out the canonical transcription–translation feedback loop with no errors at all:

> CLOCK and BMAL1 heterodimerize, translocate to the nucleus, bind circadian E-box promoter elements (core sequence CACGTG), and enhance transcription of PERIOD 1/2 and CRYPTOCHROME 1/2. PER and CRY proteins feed back to inhibit CLOCK/BMAL1-mediated transactivation. A second loop runs through REV-ERBα and RORα competing at RRE elements in the *Bmal1* promoter. Outputs are clock-controlled genes (CCGs), including *aanat*, the penultimate enzyme in melatonin synthesis.

**[Established]** — this is the standard model, correctly stated, down to the E-box consensus sequence.

His 2025 opening paragraph in *Decentralized Medicine #67* is equally clean: light → ipRGCs → retinohypothalamic tract → SCN → pineal melatonin, with relays to locus coeruleus and raphe nuclei modulating arousal. Again textbook.

He also correctly reports several genuinely important findings that are underappreciated outside the field:

- **The NAD⁺/SIRT1/clock loop.** NAMPT (rate-limiting enzyme of NAD⁺ salvage) is itself a clock-controlled gene; NAD⁺ levels oscillate; SIRT1 deacetylates BMAL1 and PER2, feeding back on the core loop. **[Established]** — Nakahata, Ramsey, Bass, Sassone-Corsi *et al.*, 2008–09. Kruse cites this accurately and builds heavily on it.
- **Extrapineal melatonin.** Melatonin is synthesized far beyond the pineal — gut, retina, immune cells, gonads, and within mitochondria themselves; pinealectomy does not zero plasma melatonin. **[Established]** — Reiter, Tan, Acuña-Castroviejo. This is real and still poorly known among clinicians. Kruse has been on it since well before it was fashionable.
- **Neuropsin (OPN5) photoentrainment.** Local circadian oscillators in mammalian retina and cornea are photoentrained by UV-A/violet light via OPN5, independent of melanopsin. **[Established]** — Buhr *et al.*, *PNAS* 2015, cited correctly.
- **Circadian misalignment causes metabolic harm independent of diet.** **[Established]** — Scheer *et al.* (*PNAS* 2009) and the forced-desynchrony literature; shift work is IARC Group 2A. His directional claim here is not fringe.

So the substrate is sound. The question throughout is what gets built on it.

---

## 3. The arc: four eras

The single most important thing a reader needs, and the thing no individual post supplies, is that **the mechanism changed three times while the conclusions stayed fixed**. The protocol advice from 2012 and 2025 is nearly identical; the stated reason for it is almost unrecognizably different.

### Era 1 (2011–2012): the neuroendocrine model

In *Why Do We Sleep* and *Why Sleep and Leptin Are Yoked* (both June 2011), there is essentially **no light-centrism at all**. The mechanism is conventional neuroendocrinology: hypocretin/orexin neurons in the lateral hypothalamus (~50,000 of them) as the junction box coupling arousal, appetite, and reward; leptin resistance driving hypercortisolism, which ablates hypocretin function; narcolepsy-cataplexy as the natural experiment. Sleep is discussed in terms of REM/NREM staging, PER2 and the cell cycle, and myelination.

Light appears once, in passing. Food and leptin are the controllers.

One idea from this era does survive intact to 2023: **sleep is the primordial state and wakefulness is the derived, evolved condition.** He states it in 2011 as a speculation ("did we evolve sleep? Or did we evolve wakefulness?") and is still asserting it in *Quantum Engineering #44* twelve years later.

### Era 2 (2013–2014): the electromagnetic turn

*Energy and Epigenetics 9: Quantum Sleep* (Nov 2013) is the pivot post, and it is a genuine discontinuity. The controller is no longer hormonal — it is electromagnetic.

The mechanism he proposes:

- Robert O. Becker's mid-century work on a **DC electrical current** running in the perineural tissue below myelin, which reverses polarity between wakefulness and sleep. **[Contested]** — Becker's experiments are real and published; the "current of injury" and its role in amphibian regeneration are documented. The generalization to a global sleep/wake control current is Becker's own speculation and has not been taken up.
- Becker's induction of anesthesia in salamanders with a 2,000–3,000 gauss magnetic field, reversible on removal. **[Contested]** — reported by Becker; not replicated in the modern literature.
- **[Extrapolation]** Kruse's own addition: an **electromagnetic vortex in the cerebrospinal fluid of the third ventricle**, generated by the pineal gland acting as a laser-like coherence device ("optical magnetic resonance"). The vortex spins counterclockwise in light and clockwise in darkness, and this reversal drives the polarity flip of Becker's DC current via SQUID-like behavior in the ependymal cell layer.

This is the most physically speculative machinery anywhere in the corpus. There is no evidence for a CSF vortex, for ependymal SQUIDs, or for biological superconductivity at physiological temperature. It also contains the framework's most florid physics claim: that vortex velocities exceed *c*, making vortices "capable of breaking through dimensional boundaries."

**Worth noting: this entire apparatus is quietly abandoned.** It does not appear in the 2021–25 posts. The conclusions it was built to support — light controls sleep, artificial light at night causes disease, melatonin and cooling matter — all survive, re-derived from different premises.

### Era 3 (2015–2016): the eye-clock era — the systematic core

The *Ubiquitination* and *Time* series are the framework's mature statement and the best material in the archive. If you read only one era, read this one.

The organizing claim is **hierarchical control**, which he emphasizes to the point of typographic shouting in *Ubiquitination 17*:

> "Melanopsin controls the SCN's eye clock exclusively. That is called hierarchical control folks. That means nothing is more important to a living thing. I'VE NOW SAID IT TWICE IN THIS BLOG."

The chain, as he builds it:

1. **Melanopsin ipRGCs** in the inner retina are the sole photic input to the SCN, functionally independent of the rod/cone "camera" system in the outer retina. **[Established]**, with one qualification: rods and cones do contribute to entrainment, but they route their signal *through* ipRGCs, so the ipRGC really is the final common path. He gives melanopsin's peak as 435–465 nm (elsewhere 460–500 nm); the accepted human value is **~480 nm**. **[Error, minor]** — consistently shifted toward blue, which conveniently strengthens the blue-light-hazard argument.

2. **DHA is the transducer.** The retina holds more DHA than the brain; photoreceptor outer segments and synapses are the most DHA-rich membranes in the body; DHA has not been substituted in 600 million years of eukaryotic evolution despite DPA being thermodynamically cheaper to make and less peroxidation-prone. **[Established]** — this is Michael Crawford's argument and it is a real and striking conservation result. Kruse reports the membrane biophysics (SN-2 esterification, supraenoic species, NPD1, phosphatidylserine recruitment, G-protein coupling) accurately.

   **[Extrapolation]** The leap: because DHA supports G-protein-coupled photoreception, and because melanopsin is a G-protein-coupled photopigment, DHA level *sets the gain of the entire circadian system* — and blue light photo-oxidatively destroys DHA, degrading the clock. Retinal photo-oxidation of DHA is real *in vitro*; that ambient screen light meaningfully depletes systemic DHA is not established.

3. **NAD⁺ and SIRT1 are "the gears."** Falling NAD⁺ collapses the redox ratio, releases SIRT1 control of BMAL1/PER2, and raises the rate of ubiquitin-marked protein turnover — which, since protein synthesis is the cell's largest energy expenditure, is metabolically catastrophic. **[Established]** for the loop; **[Extrapolation]** for making ubiquitination rate the master read-out of circadian health.

4. **Diseases are staged by where the clock breaks first.** Cataracts and glaucoma as early sentinels; autoimmunity next; cancer as the terminal outcome ("extinction of both sides of the coupled system").

This era also contains the framework's most aggressive physics claim, in *Ubiquitination 2*: that **gravitational time dilation across the ~6 feet between your feet and your SCN** is biologically significant, requiring the SCN to "run faster" than peripheral clocks the way GPS satellite clocks must run faster than ground clocks.

**[Error]** This one is worth doing the arithmetic on, because he explicitly invites it. Fractional time dilation over height *h* is *gh/c²* = (9.8 × 1.83) / (9 × 10¹⁶) ≈ **2 × 10⁻¹⁶**. Integrated over an 80-year lifespan that is roughly **half a microsecond**. Circadian period differences that actually matter to physiology are on the order of *minutes*. The effect is real — NIST measured it across 33 cm in 2010 — and it is about thirteen orders of magnitude too small to have any biological consequence. The GPS analogy inverts the lesson: GPS needs the correction precisely *because* satellite clocks are fast, high, and read to nanosecond precision, none of which describes the SCN.

The same post contains two clean physics slips: *"light has a universal speed limit at 186,000 miles an hour"* (that is per **second**), and *"blue light has a higher frequency, longer wavelength and higher photon energies"* — blue light has a **shorter** wavelength, and the sentence contradicts itself. He also states cataracts "form in the cornea"; they form in the **lens**.

### Era 4 (2021–2025): mitochondrial melatonin and the time crystal

The modern era drops the CSF vortex entirely and rebuilds on published literature — much of it genuinely good.

**The melatonin re-centering** (*Quantum Engineering #18*, 2022) is the strongest single move in the late corpus. The argument:

- Melatonin is made throughout the body wherever mitochondria are, not just the pineal. **[Established]**
- It is a potent antioxidant, arguably evolution's first, predating its signaling role. **[Established]** — Tan & Hardeland's evolutionary argument.
- Near-infrared light penetrates tissue and stimulates local mitochondrial melatonin production; sunlight exposure during exercise produces plasma/sweat melatonin ramp rates >30× the dim-light onset rate. **[Contested]** — real published observation (Zimmerman & Reiter), small literature, not independently replicated at scale.
- Morning UV energizes tryptophan → serotonin, and OPN5 sets the rhythm, loading the substrate for the evening serotonin → melatonin conversion. **[Established]** in each link; **[Extrapolation]** as an integrated causal chain.
- Therefore poor sleep is a **proxy for mitochondrial damage**, not merely a cause of it. **[Extrapolation]**, but a genuinely interesting inversion.

Note the slip in the same post: *"most melatonin in mammals is not made in the pituitary gland."* He means **pineal**. The substantive point is right.

**The time crystal** (*Quantum Engineering #44*, 2023) is where the late era goes furthest. He proposes the SCN is literally a time crystal — an out-of-equilibrium phase of matter that oscillates perpetually. The supporting claims are mostly wrong:

- **[Error]** He attributes the time-crystal proposal to *"Feynman's 1982 paper."* Feynman's 1982 paper is *Simulating Physics with Computers* and says nothing about time crystals. Time crystals were proposed by **Frank Wilczek in 2012** — which Kruse *also* states two paragraphs later, without noticing the contradiction.
- **[Error]** *"You appear to evade the second law of thermodynamics."* Discrete time crystals do not evade the second law. They require a **periodic external drive** (a Floquet system) and are perfectly consistent with thermodynamics; the interesting property is breaking discrete time-translation symmetry, not free perpetual motion.
- **[Error]** He describes time crystals as simultaneously *"settled into the state with the lowest energy... properties don't change with time"* and *"dissipative far from equilibrium structures."* These are contradictory; the passage reads as two incompatible summaries stitched together.
- **[Error]** *"The retina wires directly to the SCN with no synapsing in between... almost every tract in the eye synapses before it gets into the brain. This one does not."* There is a real and interesting fact underneath: the ipRGC is unusual in being **both** photoreceptor and projection neuron, so unlike the rod → bipolar → ganglion chain there is no *intraretinal* synapse. But the ipRGC axon certainly synapses in the SCN — that is what the retinohypothalamic tract terminates in.
- **[Contested]** The geomagnetic/HRV synchronization study (10 subjects, 31 days, separate locations, ~2.5-day period) is a real publication but comes from HeartMath, and the result is weak.
- **[Extrapolation]** The Schumann resonance fundamental (7.83 Hz) as the entrainer of thalamic alpha rhythm. The numerical near-coincidence with the alpha band (8–12 Hz) is frequently noted; no causal mechanism is established.

**The 2025 endpoint** (*Decentralized Medicine #67*) pushes into the **thanatotranscriptome** — the ~1,000+ genes that upregulate for hours to days *after* death, documented in zebrafish and mice. **[Established]** as a phenomenon (Pozhitkov & Noble). **[Extrapolation]**, and self-labeled as hypothesis, is his reading: that we undergo a partial "diurnal death" nightly, that these genes regulate ultraweak photon emission during it, and that melatonin drives the sleep respiratory-quotient shift from ~1.0 to ~0.7 by inhibiting Complex I via cardiolipin. The RQ shift itself is **[Established]**; the melatonin/Complex I mechanism is his own and is flagged as such.

---

## 4. The mature model, assembled

Stripping the era-specific machinery, here is what the framework actually asserts, in dependency order:

| # | Claim | Status |
|---|---|---|
| 1 | Non-visual photoreception via melanopsin ipRGCs entrains the SCN; this is a separate system from image-forming vision | **Established** |
| 2 | The SCN sits atop a hierarchy; peripheral tissue clocks follow it | **Established** (with real caveats — feeding time entrains liver clocks largely independently of the SCN, which the framework underweights) |
| 3 | Therefore the light environment, not the food environment, is the primary controller of physiology | **Extrapolation** — the strong form ("food is downstream") does not follow from (2); the weak form (light is a large and neglected controller) is well supported |
| 4 | DHA sets the gain of the transducer; blue light photo-oxidizes it | **Established** substrate, **Extrapolation** at system scale |
| 5 | Morning UV/IR-A loads the tryptophan → serotonin → melatonin pathway; evening darkness converts it | **Established** links, **Extrapolation** as a chain |
| 6 | Melatonin is made in mitochondria bodywide and is primarily an antioxidant | **Established** |
| 7 | Clock ↔ NAD⁺/SIRT1 coupling makes circadian state and metabolic state the same variable | **Established** |
| 8 | Artificial light at night + UV deficiency = the upstream lesion in most chronic disease | **Extrapolation** — plausible direction, far stronger than the evidence supports as a monocausal claim |
| 9 | The physical substrate is solid-state: EZ water, semiconduction, coherent domains, time crystals | **Extrapolation**, mostly unsupported |
| 10 | Non-native EMF independently degrades the same machinery | **Contested**, and outside this document's scope |

**The critical structural observation:** claims 1, 2, 4, 5, 6, and 7 are real science and do a great deal of work. Claim 8 — the entire clinical payload — rests on them but does not follow from them. And claim 9, the layer Kruse himself treats as the deepest, is the one carrying the least evidential weight. **The framework is load-bearing in the middle and speculative at both ends.**

---

## 5. The operational core

What the theory actually asks you to do is short, cheap, and — this is the awkward part for critics — mostly defensible on mainstream grounds alone:

1. **View unfiltered sunrise light.** Outdoors, no glasses, contacts, or windows. 3–5 minutes minimum, longer preferred. His memorable framing: "act like the Sphinx at sunrise" — face east, get light on the eyes, limbs grounded.
2. **Get UV exposure once UV index ≥ 1** — i.e. not at first light, but during the morning as UV becomes available. Roughly 7 AM to noon.
3. **Eliminate blue light after sunset.** Amber lighting, blue-blocking lenses, red-shifted screens.
4. **Sleep in complete darkness**, 7–9 hours.
5. **Anchor circadian phase before anchoring diet.** Fasting and cold exposure are framed as circadian tools, not caloric ones — and explicitly as *ineffective under artificial light*: "It won't work in fake light when ALAN is present."
6. **Match light exposure to latitude and season**; treat mismatch (travel, shift work, indoor life) as the primary exposure.

Points 1, 3, and 4 are standard sleep-medicine advice. Point 5 is the genuinely distinctive one, and it is a real, testable claim: *that the metabolic benefit of fasting is conditional on circadian alignment.* Point 2 is the contentious one — deliberate UV exposure sits against dermatological consensus, which is where most of the clinical objection to Kruse actually lives.

---

## 6. Predictions and how they've fared

Unusually for this genre, he makes datable, checkable predictions. Some have landed:

- **Opsins outside the eye.** He predicted from the cold-thermogenesis protocol that a melanopsin-like photoreceptor had to exist in skin, and later that more opsins would be found in subcutaneous fat. **Both have substantial support** — OPN4 and OPN3 are expressed in human skin, and OPN3 in adipocytes has been shown to be light-responsive and to regulate lipolysis (Nayak *et al.*, 2020). This was a real prediction, made early, and it came in.
- **UV-driven photoentrainment beyond melanopsin.** He argued for UV's circadian role before OPN5's photoentrainment function was published (Buhr 2015). Directionally correct.
- **Circadian disruption as a driver of metabolic disease independent of calories.** The last decade of chrononutrition and misalignment work has moved substantially toward him.

Others have not, or are unfalsifiable as stated:

- The CSF vortex, ependymal SQUIDs, and biological superconduction: no supporting evidence in the twelve years since, and quietly dropped from his own writing.
- Gravitational effects on SCN timing: arithmetically excluded.
- The SCN as a literal time crystal: not a testable biological claim as posed.

**What would falsify the core?** The framework's testable heart is claim 5 in §5 — that circadian alignment gates metabolic interventions. A well-controlled trial in which time-restricted feeding or fasting produced equivalent metabolic benefit under circadian-disrupted versus aligned light conditions would directly contradict it. Conversely, the strong "light trumps food" thesis would be supported by demonstrating that light-environment correction outperforms dietary correction head-to-head on hard metabolic endpoints. Neither experiment appears to have been run.

---

## 7. How to read him

Three practical rules from doing this reconstruction:

1. **Date every claim.** A mechanism from 2013 may have been silently retired by 2022. He does not issue corrections; he changes the substrate and keeps the conclusion.
2. **The physics analogies are rhetorical, not quantitative.** Where he invokes relativity, time crystals, or superconduction, the analogy is doing persuasive work, and the numbers — where they can be checked — generally do not survive checking. Where he invokes *biology* (melanopsin, DHA, NAD⁺/SIRT1, extrapineal melatonin), he is usually accurate and often ahead of the field.
3. **Separate the protocol from the justification.** The advice is largely low-risk and partly mainstream. The stated mechanism is where the framework's weight-bearing problems are. The two can be evaluated independently, and should be.

---

## 8. Relation to existing work in this repo

- `outputs/circadian/circadian_*.md` (Feb 2026) approaches the same territory **mainstream-first** — chronobiology and circadian oncology as the spine, with Kruse as a bounded section (§9 of `circadian.md`). It was built from the UV/melanin source docs, not the blog archive.
- **This document is the mirror image**: Kruse-first, reconstructed from his own 737-post corpus, with mainstream science as the reference frame against which his claims are graded.
- `outputs/evolution/semiconductor_theory.md` covers the solid-state/semiconductor substrate — claim 9 in §4 above — in far more depth. The two documents share that layer; this one treats it as a dependency rather than the subject.
- Open follow-on: a **claim ledger** (structured extraction of each discrete assertion with source post, mechanism, and falsifiability rating) would make the graded claims here machine-queryable across the whole archive rather than the 23-post spine.
