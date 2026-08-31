# Kruse's Circadian Theory: A Period-by-Period Exposition

*Companion to `circadian_reconstruction.md`. Where that document gives the graded overview, this one explains each period in full — the mechanisms, the named molecules, the arguments, and the sources.*

*Built from the 737-post archive in `input/kruse_blog_glix/markdown` (June 2011 – January 2026).*

---

## How to use this document

The overview document states Kruse's circadian theory as a single coherent position and grades it. That's useful for judging the framework, but it flattens something important: **the theory was rebuilt from the ground up at least three times**, and the versions are not compatible with each other. A mechanism that carries the entire explanatory load in 2013 is silently absent by 2022.

This document therefore runs chronologically. Each period gets:

- **The question he was trying to answer** in that period
- **The full mechanism** as he states it, with the actual molecules and pathways named
- **The key posts**, so claims can be traced
- **What carried forward** and **what was abandoned**

Claims carry the same labels as the overview:

- **[Established]** — mainstream, well-replicated; he's reporting it accurately
- **[Contested]** — real and published, but minority, weakly replicated, or from a fringe-adjacent source
- **[Extrapolation]** — his own inference, not textbook chronobiology
- **[Error]** — wrong on a checkable point

### Two corrections to the overview document

Reading deeply changed two things I previously wrote, and both matter:

1. **The light turn is 2013 — the overview was right.** I initially wrote here that it begins in 2012, on the strength of *Cold Thermogenesis 7* (March 2012) and *Brain Gut 11* (September 2012). That was a selection-bias error: those posts were chosen *because* they scored highest on circadian vocabulary, and they run ~5.5x their own half-year average, so they are outliers rather than a trend. Measured across the whole corpus, light:food vocabulary is **flat through 2012** (ratio 0.28 -> 0.35 -> 0.28) and crosses over only in **2013 H1** (0.97), with light decisively dominant from 2013 H2 (1.48). What 2012 actually contains is two remarkable posts sitting inside a corpus still overwhelmingly about food, leptin, and cold: he wrote the thesis before he committed to it. See §1.7 and the note on backdating below.

2. **There are five periods, not four.** The overview folds 2017–2020 into the surrounding eras. It deserves its own treatment, because it contains the framework's single most important structural move: the **unification of the 2011 leptin work with the 2015 eye-clock work into one mechanism**. Without that period, the jump from Period 3 to Period 5 looks unmotivated.

### Method

All 737 posts were scored on weighted circadian vocabulary (`scripts/rank_circadian.py`; scores in `raw/circadian_rank.json`). 463 posts registered a hit. This exposition draws on roughly 35 posts read in full or near-full, selected as the highest-density post in each period plus the posts that introduce a named mechanism.

---

## The five periods at a glance

| Period | Years | The controller is… | Signature mechanism | Key posts |
|---|---|---|---|---|
| **1. Neuroendocrine** | 2011–2012 | Hormones — food, cold, leptin | Leptin → hypocretin → prolactin/GH autophagy window | *Why Do We Sleep*, *CT-7*, *Brain Gut 11* |
| **2. Electromagnetic** | 2013–2014 | DC current and field geometry | CSF vortex reversing Becker's DC current | *EE 9: Quantum Sleep*, *QB 12*, *EMF 2* |
| **3. Eye clock** | 2015–2016 | Melanopsin → SCN, gated by DHA | Ubiquitin economy tuned by NAD⁺/SIRT1 | *Ubiquitination 2/4/16/17*, *Time 2/9/17* |
| **4. Unification** | 2017–2020 | Melanopsin, with leptin as its output | Retinal release from melanopsin's Schiff base | *QT 22*, *CPC 27*, *food vs light* |
| **5. Mitochondrial** | 2021–2026 | Mitochondrial melatonin + melanin | Melanin electrochemical time-stamping; SCN as time crystal | *QE 18/44/55/65*, *DM 67* |

The through-line: **the conclusion never changes, only the mechanism.** Get morning sun, avoid light at night, and your metabolism follows. He has argued this from hormones, from field physics, from membrane biophysics, from photochemistry, and from condensed-matter physics, in that order.

---

# Period 1 (2011–2012): The Neuroendocrine Clock

## 1.1 The question

*Why does sleep control metabolism?* In 2011 Kruse is a spine surgeon writing about obesity. He is not yet a light theorist. The problem he's solving is why leptin-resistant patients cannot lose weight regardless of diet.

**What this period actually consists of.** This matters, because the two posts that get the most space below are not typical of it. Across **121 posts** in 2011–2012, titles break down roughly as: food/diet/paleo (21), *Brain Gut* series (18), *Cold Thermogenesis* series (15), leptin (14), hormones/cortisol/thyroid (6) — and **light, sun, circadian, or sleep: 4**. Corpus-wide, light vocabulary sits at a light:food ratio of ~0.3 and does not move across the two years.

So Period 1 is a **food, cold, and hormone** period. Circadian timing is present throughout as a *framework* for when hormones act, but light is not yet the causal agent — it is the thing that sets the clock, in the ordinary textbook sense that any chronobiologist would accept. §1.4 and §1.7 cover two posts that break this pattern sharply; they are treated at length because of what they *anticipate*, not because they represent the period.

## 1.2 The starting position: sleep is primordial

The first substantive circadian claim in the corpus, from *Why Do We Sleep* (22 June 2011), is an evolutionary inversion:

> "Did we evolve sleep? Or did we evolve wakefulness? I think sleep is the primordial condition."

His reasoning: evolution selects for exploiting an environmental niche, and exploration requires wakefulness. Sleep is therefore the default state, and wakefulness the derived, expensive adaptation layered on top.

**[Extrapolation]** — and a durable one. He is still asserting it twelve years later in *QE #44* (2023), where he reframes it thermodynamically: sleep is when the entropy debt incurred by wakefulness is repaid.

The same post already contains the **circadian–cell cycle yoke** that will anchor everything downstream: PER1/PER2 link the clock to mitosis; mPER2-knockout mice show increased tumor development and decreased apoptosis; the affected downstream genes are Cyclin D1, Cyclin A, Mdm-2, Gadd45α, and c-myc via E-box-mediated reactions. **[Established]** — accurately reported.

## 1.3 The leptin–hypocretin architecture

*Why Sleep and Leptin Are Yoked* (24 June 2011) supplies the neuroanatomy:

- **VLPO neurons** (GABAergic, inhibitory) fire on subcortical arousal centers to produce cortical synchronization — sleep onset.
- **Hypocretin/orexin neurons** in the ventrolateral hypothalamus — only ~50,000 of them in an organ of ~10¹¹ cells — are the junction box. They project widely and control the *stability* of wakefulness.
- These neurons are excited by leptin, glucose, ghrelin, NPY, and CRF.
- **The causal chain:** chronic leptin resistance → hypercortisolism → cortisol knocks out hypocretin neurons → arousal and appetite decouple.
- **The natural experiment:** narcolepsy-cataplexy, where hypocretin neurons are lost (HLA-associated, T-cell receptor alpha locus, likely autoimmune). Narcoleptics are strikingly resistant to drug addiction but *prone to obesity* — which he reads as proof that the hypocretin system governs energy expenditure rather than appetite per se.

**[Established]** — the hypocretin/narcolepsy biology is correct and well-sourced (de Lecea, Koob's operant-conditioning work). This is competent, conventional neuroendocrinology.

## 1.4 *Cold Thermogenesis 7* — the hour-by-hour day

*CT-7* (21 March 2012) is the most detailed single circadian document in the entire corpus — and an outlier within its own period, running about 5.5x the half-year average for light vocabulary. It sits inside the *Cold Thermogenesis* series, whose subject is cold adaptation, not light. He walks a full 24 hours, hour by hour. Reconstructed:

| Time | Event |
|---|---|
| ~4:00 AM | Lowest body temperature; signals hypothalamus that sleep is ending |
| 6:00 AM | Cortisol surge wakes the cortex via the reticular activating system. **VIP** peaks. Ghrelin peaks |
| 6:45 AM | Sharpest blood-pressure rise of the day — why cardiac deaths cluster here |
| Daybreak | Sunlight on retina shuts off pineal melatonin. AM sun is IR-dominant; UV arrives later |
| 7:30 AM | Melatonin fully suppressed (about an hour after first light) |
| 8:30 AM | Gastrocolic reflex; peristalsis. Cortisol, aldosterone, ghrelin all elevated |
| 9–10 AM | Peak sex-steroid secretion; peak alertness ~10 AM |
| 2:30 PM | Best muscle coordination; fastest reaction times ~3:30 PM |
| 5:00 PM | Peak cardiovascular efficiency and peak protein synthesis — his prescribed exercise window |
| 6:30 PM | Highest blood pressure (ANF/ADH, renin–aldosterone) |
| 7:00 PM | Body temperature rises as leptin and IL-6 release from fat stores |
| 7–10 PM | Leptin rises, insulin falls, adiponectin falls; adenosine accumulates |
| 10:00 PM | Adenosine peaks. Melatonin permitted after 3–4 hours of true darkness |
| 11:30 PM | GI tract shuts down; vagus quiet |
| **Midnight** | **Leptin enters the hypothalamus, binds its receptor, triggers the prolactin surge** |
| 12–3 AM | **The autophagy window.** GH released; protein recycling at maximum |

**[Established]** in outline — the cortisol awakening response, the BP morning surge, evening leptin rise, adenosine accumulation, and nocturnal GH release are all real. **[Extrapolation]** in the precision: the clock times are stated far more exactly than the literature supports, and the causal ordering (leptin entry *causes* the prolactin surge *causes* GH) is his own.

## 1.5 The prolactin gate — the linchpin

He says explicitly: *"I base every bio-hack I do on this step in circadian biology because it is the most important."*

The claim: the midnight prolactin surge, which follows leptin's entry into the brain, is the permission signal for the anabolic/autophagic phase of sleep and the large nocturnal GH pulse. It is abolished by:

- **Artificial light after sunset** (he cites Jessa Gamble's talk)
- **Eating within 3–4 hours of bed** — any insulin spike blocks leptin from binding
- Leptin resistance, sleep apnea, post-menopause

Downstream consequences: low DHEA, high IL-6, reduced lean mass, impaired cardiac function, and — because autophagy never completes — cells starting the next day with unrepaired components.

**[Contested]** — prolactin is genuinely sleep-associated and light-suppressed, and GH is genuinely tied to slow-wave sleep. But the specific dependency (leptin entry → prolactin → GH → autophagy) as a serial gate is his construction. Note that by 2023 he *reverses* the GH claim outright, saying in the year-end review that "growth hormone is released during slow wave sleep... is simply not true. POMC controls it."

## 1.6 Seasonal switching: two different clocks

A distinctive Period 1 idea that mostly disappears later. He argues warm-adapted and cold-adapted mammals **do not share the same circadian biology**:

- **Long-light/summer:** **VIP** dominates SCN entrainment. VIP is a real SCN neurotransmitter, expressed in 9–24% of SCN neurons, retino-recipient, acting through the **VPAC2** receptor; VPAC2 ablation renders the clock arrhythmic. **[Established]** — this is correct and well-sourced.
- **Cold/short-light:** photic entrainment is displaced. **eNOS** rises and "blocks photic input to SCN"; **NPY** (from the geniculohypothalamic tract) suppresses SCN firing; **α-MSH** potentiates the seasonal switch.

He adds a genuinely interesting coupling: **leptin induces VIP expression** through the VIP cytokine response element, so leptin sensitivity directly sets circadian entrainment gain. **[Contested]** — the leptin/VIP transcriptional link exists in the literature; the systemic claim built on it is his.

He also correctly reports the **TLR9 circadian immunity** finding — mice infected at the TLR9 nadir develop more severe sepsis; vaccination near the TLR9 peak produces stronger responses. **[Established]**

## 1.7 *Brain Gut 11* — where "light trumps food" is born

*Brain Gut 11: Is Technology an Achilles Heel?* (6 September 2012) contains the argument that the entire framework rests on — and then, tellingly, **he does not follow it up for another six months.** The light:food ratio in the half-year *after* this post (0.28) is lower than in the half-year before it (0.35). He states the thesis and returns to writing about the gut. He calls it a "third grade math question": **48% vs 10%**.

The argument:

- Humans have 8 lobes; the 2 occipital lobes are devoted to vision → 25% of the brain is light-wired.
- Light also projects into association cortex in the other six lobes → **45–48% of the brain is wired to light circuits.**
- The **hypothalamus is 1% of brain volume**, and leptin-receptor outflow tracts project to only **10% of neurons**.
- Therefore: *"the conventional wisdom that diet is the main controller of metabolism might be dead wrong. Maybe light is the master controller of how you account for calories."*

**[Error in inference]** — this is the framework's load-bearing argument, and it is a non-sequitur. Cortical area devoted to processing a signal is not a measure of that signal's control authority over metabolism. By the same arithmetic, the ~1% hypothalamus should be metabolically negligible, which no one believes — including Kruse, whose entire Period 1 rests on it. The premise also double-counts: association-cortex visual projections serve *image-forming* vision, which is precisely the pathway he elsewhere insists is irrelevant to the circadian clock (that's the melanopsin ipRGC system, a few thousand cells).

**A note on backdating.** Kruse consistently antedates his own light turn. In *Energy and Epigenetics 9* (November 2013) he writes: *"I have said for three years on this blog that light exposure was far more important than food."* Three years before November 2013 is November 2010 -- but the blog did not begin until June 2011, and the post he cites as evidence is *Brain Gut 11* (September 2012), fourteen months earlier. He claims roughly double the priority the record supports. This matters for reading him: his retrospective accounts of when he figured something out are not reliable, and the corpus itself is the better witness.

The same post makes a much better argument he doesn't emphasize: E-box regulation extends to **hTERT**, the telomerase catalytic subunit, tying circadian disruption to senescence and carcinogenesis. **[Contested]** — the link exists but the causal weight is his.

## 1.8 What Period 1 established

**Carried forward permanently:** sleep as primordial; circadian–cell-cycle yoke; the midnight leptin window; "no eating after sunset"; light > food as a slogan.

**Abandoned:** VIP/eNOS seasonal switching; hypocretin as the central junction; the prolactin→GH gate (later contradicted); the set-point critique.

**The gap that drove the next period:** nothing here explains *how* a photon becomes a hormonal signal. The mechanism is a black box, and Period 2 is the attempt to open it.

**How to read this period.** Two posts in it are extraordinary and the other 119 are not about light at all. The honest summary is that Kruse arrived at his central thesis in September 2012, left it sitting unused, and only rebuilt his framework around it in 2013 — which is why Period 2, not Period 1, is where the light turn belongs.

---

# Period 2 (2013–2014): The Electromagnetic Turn

## 2.1 The question

*What is the physical carrier of circadian information?* Having decided light controls metabolism, he needs a transduction mechanism. He goes looking in physics rather than biochemistry, and this is the period where his writing changes character permanently.

## 2.2 *Quantum Biology 12* — clocks without DNA

*Do We Need DNA to Tell Time?* (21 July 2013) is, on the evidence, the strongest argument in the entire corpus. He builds it on two 2011 *Nature* papers:

- **Human red blood cells** — anucleate, no transcription possible — sustain a ~24-hour rhythm.
- ***Ostreococcus tauri***, a picoalga, kept in constant darkness shows no detectable transcription or translation, yet on returning to light resumes its rhythm *at the phase predicted by a clock that had been running all along* — not from a reset "phase zero."
- The oscillating species in both is **peroxiredoxin**, cycling between oxidized and reduced states on a 24-hour period.

**[Established]** — this is real, important, and well-replicated (O'Neill & Reddy). Peroxiredoxin oxidation cycles are now recognized as a transcription-independent circadian marker conserved across all three domains of life.

His inference: *"something other than a biologic pathway or chemical has to control all circadian signaling."* If the clock predates and outlives DNA transcription, the primordial timekeeper must be physical, not genetic. He proposes light acting on **coherent water** in the cytoplasm as the transducer, invoking **Herbert Fröhlich's** prediction that hydrated proteins plus light suffice. **[Extrapolation]** — Fröhlich coherence remains unconfirmed in biological systems.

This post also introduces the **analog/digital dual clock**:

- **Analog** — SCN and pineal, responding in graded fashion to photon flux
- **Digital** — retina and optic nerve, all-or-none action potentials

**[Extrapolation]**, though a reasonable metaphor.

And the reframing of leptin: *"The leptin receptor... counts quanta of light, phonons, protons, and electrons from food. It is a quantum clock not a calorie clock."* This is the bridge that will become Period 4's unification.

He closes with the **fluctuation–dissipation theorem**, attributing it to Einstein's fourth 1905 paper: any fluctuation in timing produces energy loss, and biological change follows stochastic (square-root) rather than linear dynamics. **[Error, minor]** — Einstein's 1905 Brownian motion paper is foundational to it, but the fluctuation–dissipation theorem proper was formalized by Callen and Welton in 1951.

## 2.3 Becker's DC current

*Energy and Epigenetics 9: Quantum Sleep* (15 November 2013) is the pivot post. Its foundation is **Robert O. Becker's** mid-century work:

- Ralph Gerard showed steady DC potentials along cortical neurons — front-to-back polarization, frontal lobes negative relative to occipital.
- Becker demonstrated the current runs **outside the axon, below the myelin**, in the perineural/interfacial water layer, and is **semiconductive** — he showed a Hall effect in frozen nerve.
- Passing a small DC current front-to-back rendered salamanders unconscious; increasing it deepened delta-wave activity.
- **He could put animals to sleep and wake them by reversing current direction.**
- A 2,000-gauss field perpendicular to the brain induced diffuse delta; 3,000 gauss produced full anesthesia, reversed within seconds on removing the magnet with none of the side effects of chemical anesthetics.

**[Contested]** — Becker's experiments were published and his regeneration work is respected; the anesthesia results have not been replicated in modern literature and the global sleep-control interpretation was Becker's own speculation.

Kruse pairs this with Bukalo's NIH work showing dendritic back-propagation during rest and sleep, arguing modern neuroscience rediscovered in 2011 what Becker found in the 1960s. He also cites real work showing sleep upregulates oligodendrocyte myelination genes while sleep deprivation activates cell-stress and death genes. **[Established]**

## 2.4 The CSF vortex — the high-water mark of speculation

Then comes his own addition, and it is the most physically extravagant machinery anywhere in the corpus:

- The **pineal gland** acts as a coherence device — a biological laser — performing "optical magnetic resonance" (a term he attributes to Roy Glauber). It integrates three simultaneous inputs: photic signal from the RPE, the geomagnetic field, and gravity (via its calcium concretions).
- This generates an **electromagnetic vortex in the CSF of the third ventricle**.
- **Counterclockwise in light** — focuses electron flow, structures CSF water, produces the electron burst that wakes the cortex.
- **Clockwise in darkness** — disperses energy outward like a hurricane, permits melatonin release, drops CSF temperature ~2°C.
- The vortex direction sets the polarity of Becker's DC current, read out by **SQUID-like behavior in the ependymal cell layer**, with cilia beating coherently along the flow.
- Concussion and PTSD **reverse the vortex instantly**, which is why post-concussive syndrome involves circadian signaling at the wrong time.

**[Extrapolation]**, and unsupported at every step: there is no evidence for a CSF vortex, for ependymal SQUIDs, or for biological superconductivity at 37°C. The post also asserts that vortex velocities exceed *c*, making vortices "physically capable of breaking through dimensional boundaries" — **[Error]**.

Embedded in it, however, is a claim that survives everything: **"we are oxidized during sunlight hours by design; at night cells become chemically reduced."** The diurnal redox oscillation is real, and it becomes the spine of Periods 3–5.

## 2.5 What Period 2 established

**Carried forward:** the peroxiredoxin/transcription-independent-clock argument; diurnal redox oscillation; light as information not just energy; the leptin-receptor-as-photon-counter reframing; melatonin/cooling coupling.

**Abandoned entirely:** the CSF vortex, ependymal SQUIDs, pineal-as-laser, the concussion mechanism. None appear in Period 5.

This is worth stating plainly: **the machinery that this period's posts present as the fundamental discovery is gone from his own writing within a decade, without retraction.**

---

# Period 3 (2015–2016): The Eye Clock

## 3.1 The question

*Which tissue holds the clock, and what is the currency it controls?* This is the framework's systematic core — the *Ubiquitination* series (25 posts) and the *Time* series (25 posts), written across roughly eighteen months. If you read one period, read this one.

## 3.2 Hierarchical control

The organizing claim, stated in *Ubiquitination 17* with unusual emphasis:

> "Melanopsin controls the SCN's eye clock exclusively. That is called hierarchical control folks. That means nothing is more important to a living thing. I'VE NOW SAID IT TWICE IN THIS BLOG."

And in *Ubiquitination 16*, the reframing that names the period:

> "Medicine today treats the eye as a camera almost exclusively, when its most important physiologic role is as an optical clock."

The retina splits into two functionally independent systems: **outer retina** (rods/cones) = camera; **inner retina** (melanopsin ipRGCs) = clock. **[Established]** — and his statement of the canonical TTFL in the same post is textbook-accurate, down to the E-box consensus sequence CACGTG and the REV-ERBα/RORα secondary loop.

## 3.3 The transducer: melanopsin and DHA

**Melanopsin** forms a functional photopigment catalyzing G-protein activation in light-dependent fashion; ipRGCs project directly to the SCN and generate pineal melatonin rhythms. He gives its sensitivity as 435–465 nm (elsewhere 460–500 nm). **[Error, minor]** — human melanopsin peaks at **~480 nm**; his figures run consistently blue-shifted, which strengthens the blue-hazard argument.

**DHA** is the gain control. From *Ubiquitination 17*:

- The retina holds more DHA than the brain; photoreceptor outer segments and synapses are the most DHA-rich membranes in the body; DHA is ~50% of CNS PUFA.
- DHA has not been substituted once in **600 million years** of eukaryotic evolution, despite DPA (differing by one double bond) being thermodynamically cheaper and less peroxidation-prone. **[Established]** — Crawford's conservation argument, and genuinely striking.
- Mechanism: DHA is esterified at the SN-2 position; "supraenoic" species (ω-3 at both SN-1 and SN-2) constitute 52% of phosphatidylserine and 31% of phosphatidylcholine in photoreceptor discs; very-long-chain FAs at SN-1 "atomically curl" to restrict rhodopsin motion.
- **NPD1** (neuroprotectin D1), the DHA-derived docosanoid of the RPE, upregulates Bcl-2/Bcl-xL and downregulates Bax/Bad, producing a pro-survival transcriptome.
- DHA-rich phosphatidylserine recruits Raf-1 and PKC to modulate AKT1 signaling, suppressing apoptosis.

**[Established]** for the membrane biophysics — this is accurately reported lipid science. **[Extrapolation]** for the leap: that because melanopsin is a GPCR requiring a DHA-rich environment, **DHA level sets the gain of the entire circadian system**, and blue light photo-oxidatively destroys DHA to degrade the clock body-wide.

His mechanism for **cataracts is genuinely novel**: they form to **block blue light and protect retinal DHA stores** — a protective adaptation, not a disease. (He says they form "in the cornea"; they form in the **lens**. **[Error]**)

## 3.4 The ubiquitin economy

This is the period's most distinctive contribution and the reason the series is named *Ubiquitination*. The argument:

- Eukaryotes spend **80%** of their total energy budget on protein synthesis. Each peptide bond costs **5 ATP** — five times the cost of polymerizing nucleotides into DNA.
- Protein turnover is therefore the single largest line item in cellular economics, and it is governed by **ubiquitin marking rate**.
- The eye clock is hierarchically organized to control **the whole organism's ubiquitination rate**.
- Elevated ubiquitination → accelerated replacement → pushes the Hayflick limit → telomere shortening → disease.
- **Elevated blood glucose is a clinical sign of elevated ubiquitin rate**, not primarily a fuel-handling problem.

**[Contested]** on the 80% figure — protein synthesis is a major ATP sink and can approach this in rapidly growing cells, but 80% is at the extreme end for differentiated tissue. **[Extrapolation]** for ubiquitination rate as the master read-out of circadian health.

## 3.5 The gears: NAD⁺ and SIRT1

- **SIRT1** removes acetyl groups, inactivating ubiquitin marking in cells under "carbon stress."
- SIRT1 is coupled to **NAD⁺** at complex I, linking protein-synthetic machinery directly to the respiratory chain and making **NAD⁺/NADH the cell's master redox sensor**.
- SIRT1 regulates the amplitude and duration of circadian gene expression in the retina by deacetylating **BMAL1 and PER2**.
- **NAMPT**, rate-limiting for NAD⁺ salvage, is itself clock-controlled — a closed feedback loop.

**[Established]** — accurately reported, and this loop remains the framework's strongest mechanistic anchor across all later periods.

## 3.6 Melatonin as the sulfate ferry

From *Ubiquitination 2* and *4* — a mechanism largely borrowed from Stephanie Seneff:

- Sunlight drives **sulfation** of lipids: cholesterol sulfate in skin and gut, DHEA-sulfate in blood, melatonin sulfate in gut and brain.
- **Melatonin is a night-time ferry** carrying sulfate from the small bowel to the pineal, then distributing it through the CSF during sleep. This is why the pineal has no blood-brain barrier.
- Sulfates **reflect the solar frequencies we cannot use**, cooling tissue surfaces — he draws an extended analogy to volcanic sulfate aerosols cooling the stratosphere after Pinatubo.
- Cooling increases magnetic sensitivity and makes proton tunneling (via the Grotthuss mechanism) more favorable.

**[Contested]** — the sulfation hypothesis is published but marginal and not independently established.

He adds a mechanism for **pineal calcification**: **fluoride as a dielectric blocker.** The cell membrane acts as a capacitor with water (dielectric constant 78) as the dielectric; fluoride discharges the stored voltage, lessening water's battery capacity, and fluoride uptake rises with temperature. **[Extrapolation]** — pineal calcification and fluoride accumulation are real observations; the capacitor mechanism is his.

## 3.7 The relativity claim

From *Ubiquitination 2* — the framework's most aggressive physics claim, and one he explicitly invites checking:

> "The SCN circadian clock has to run faster than the organ body clocks because of the warping effects of gravity."

The analogy: GPS satellite clocks must run 38 μs/day faster or positions drift ~10 km/day. He argues the ~6 feet between your feet and your SCN produces a biologically meaningful equivalent.

**[Error]** — the arithmetic: fractional dilation is *gh/c²* = (9.8 × 1.83)/(9 × 10¹⁶) ≈ **2 × 10⁻¹⁶**. Over an 80-year lifespan that integrates to roughly **half a microsecond**. Circadian period differences that matter physiologically are on the order of *minutes*. The effect is real — NIST measured it across 33 cm in 2010 — and about thirteen orders of magnitude too small to matter. The GPS analogy inverts its own lesson: the correction is needed because satellite clocks are read to nanosecond precision, which the SCN is not.

Two clean slips in the same post: *"light has a universal speed limit at 186,000 miles an hour"* (per **second**), and *"blue light has a higher frequency, longer wavelength and higher photon energies"* — blue light has a **shorter** wavelength; the sentence contradicts itself.

He extends the idea in *Ubiquitination 4*: **metals precipitating in tissue speed up local organ clocks** relative to the SCN, destroying signaling — and claims this explains how **copper IUDs** work ("ovulation is impossible when the uterus clock is running faster than the ovarian one"). **[Error]** — copper IUDs act through spermicidal copper ions and a local inflammatory endometrial response.

## 3.8 Melatonin and insulin as opposed solar metronomes

*Time 17* (June 2016) supplies the metabolic coupling:

- **NADH is a fluorophore** absorbing maximally at **340 nm**, coupling electron entry at complex I photoelectrically to the solar spectrum. **[Established]** — NADH's 340 nm absorbance is real and is the basis of standard lab assays.
- **Tyrosine**, an aromatic UV-absorbing amino acid, is critical to insulin release and storage. **[Established]**
- **Melatonin receptors are present on pancreatic beta cells**, and melatonin activation *decreases* insulin secretion.
- Therefore insulin and melatonin are **antagonistic metronomes**: insulin encodes the high-energy summer electron signal; melatonin encodes darkness. Light at night collapses the opposition. *"Insulin resistance is not a food only problem, it is a light at night problem."*

**[Established]** — and this is one of his strongest points. Melatonin receptors (MT1/MT2) on beta cells are well documented, and the **MTNR1B** variant is among the most robustly replicated type 2 diabetes risk loci in human genetics. The direction of his argument has real support; the monocausal strength does not.

## 3.9 Warburg metabolism as the emergency brake

A striking inversion from *Ubiquitination 4*:

> "Glucose down regulates the circadian clock genes... this is why a Warburg metabolism is selected for in oncogenesis. It is the body trying to slow time down."

The cell, unable to lower ubiquitination rate because its light environment is wrong, uses glucose to brake clock-gene cycling. Warburg metabolism is thus a **last-ditch adaptive response to a bad light environment**, not a defect. Cancer is "an epigenetic disease of light" — oncology fails because "they are looking in the genes for a mechanism that is optically based."

**[Extrapolation]** — but a genuinely interesting reframing, and it connects directly to the atavism material in `../evolution/evolution_cancer_digest.md`.

## 3.10 Disease staging

The clinical payload: diseases appear in order of where the clock breaks first.

**Cataracts and glaucoma** (earliest sentinels — the clock organ itself) → **autoimmunity, Hashimoto's, melasma** → **neurodegeneration** → **cancer** ("extinction of both sides of the coupled system").

---

# Period 4 (2017–2020): Unification

## 4.1 The question

*Are leptin and melanopsin two things or one?* This period gets its own section because it resolves the framework's biggest internal tension. Period 1 made leptin the controller; Period 3 made melanopsin the controller. They sat unreconciled for years.

## 4.2 *QT #22* — "Leptin resistance IS melanopsin dysfunction"

The title of the November 2018 post is the thesis. The mechanism:

- Melanopsin binds its chromophore **retinal** via a **Schiff base** linkage.
- 2015 data show this Schiff base is **unusually susceptible to spontaneous cleavage in mammals, and "particularly unstable for human melanopsin."** **[Established]** — this is a real published finding.
- Blue light and nnEMF cleave the bond, liberating **free retinal**.
- Free retinal is an **aldehyde and a photosensitiser** that destroys chromophores across all photoreceptive proteins. His formulation: *"Vitamin A is the ONLY Vitamin on Earth that emits light."*
- **Leptin is itself a chromophore in subcutaneous fat.** Its job is to take optical data from skin and skin arterioles about day/night, combine it with energy-balance information, and deliver the package to the hypothalamus under cover of darkness.
- Free retinal at the wrong time of day damages leptin optically → leptin cannot signal → **leptin resistance is a photonic lesion, not a metabolic one.**

**[Established]** for melanopsin's unstable Schiff base and for retinal's phototoxicity — both real. **[Extrapolation]**, and a large one, for leptin as an optical signalling chromophore.

The structural significance is hard to overstate: this single move **retroactively converts all of Period 1 into a special case of Period 3.** The 2011 leptin work isn't superseded — it's absorbed. He also uses it autobiographically, explaining his own 360-lb obesity as light-induced leptin damage sustained in the operating room.

He adds the therapeutic counterweight: *"The antidote to blue light in nature is 42% of the red light in sun,"* augmented by UVA/UVB, which strengthen mitophagy and apoptosis.

## 4.3 Skin as a circadian organ

*Is the Skin Circadian Sensitive?* (2017) extends the clock outward:

- Skin cells divide and repair more at night; skin is more acidic, less hydrated, slightly warmer at night. Lower pH → smaller exclusion zone → lower DC current → impaired regeneration.
- **CLOCK-mutant mice have *less* severe psoriasis; PER2-mutant mice develop psoriasis** even without other autoimmune features. **[Established]** — real published mouse data.
- He reads CLOCK and PER2 as a "coupled thermodynamic gene pair" whose uncoupling causes extinction of both arms.
- Practical chronotherapy: topical medications absorb better in the evening.

## 4.4 The NAD⁺ chain, formalized

*The food versus light lesson* (July 2019) is the clearest statement of the mature light-over-food argument, written as a direct rebuttal to a former member arguing for micronutrients. He compresses the mechanism into a single chain:

> **SUN + fasting → NAD⁺ → SIRT1 → BMAL1/CLOCK → NAMPT → NAD⁺**

With supporting claims:

- **UVA releases nitric oxide** from arteries, improving microcirculation while inhibiting cytochrome c oxidase — slowing electron transport and *decreasing* the need for food substrate. **[Contested]** — UVA-induced NO release from cutaneous stores is real and published (Feelisch, Weller); the downstream inference is his.
- *"Sunlight is a calcium channel blocker"* altering voltage-gated channel firing rates.
- **Glass blocks all UVB, most UVA, and 30–50% of IR-A** — so indoor living is a spectral amputation regardless of diet. **[Established]** for ordinary window glass and UVB/UVA.
- Indoor air is less charged → pseudohypoxia → NAD⁺ drops → SIRT1 falls.

## 4.5 The one genuinely falsifiable claim

Stated here more explicitly than anywhere else:

> "Solar exposure and fasting work with light frequencies to slow ECT flow and this can increase the intracellular NAD/NADH ratio if the light environment is dominated by sunlight. **It won't do this with artificial light.** ... **It won't work in fake light when ALAN is present.**"

This is the framework's testable heart: **the metabolic benefit of fasting is conditional on circadian alignment.** A well-controlled trial showing equivalent benefit from time-restricted feeding under disrupted versus aligned light conditions would directly contradict it. The experiment appears not to have been run.

---

# Period 5 (2021–2026): Mitochondrial Melatonin, Melanin, and Time Crystals

## 5.1 The question

*Where is the clock actually located, physically?* The answer moves inward — from the eye to the mitochondrion, and from biochemistry to condensed-matter physics.

## 5.2 Melatonin re-centered

*QE #18* (November 2022) is the strongest post of the late period:

- Most melatonin is **not made in the pineal**. It is made wherever mitochondria are: eye (lens, retina, ciliary body), inner ear, thymus, immune cells (T cells have the highest concentration of any cell), gut (**400× the pineal's content**), microbiome, ovaries, testes. A 1958 experiment removing bovine pineal glands still found melatonin in blood. **[Established]** — Reiter, Tan, Acuña-Castroviejo. (He writes "not made in the pituitary gland"; he means **pineal**. **[Error, slip]**)
- Melatonin is evolution's original antioxidant, predating its signalling role — arising when the sun's increasing UV output drove oxygenation of Earth. **[Established]** — Tan & Hardeland's evolutionary argument.
- **Mitochondrial melatonin is produced under UV/IR-A control**; NIR penetrates tissue to stimulate it. Sunlight-plus-exercise produces plasma/sweat melatonin ramp rates >30× dim-light-onset rates. **[Contested]** — real (Zimmerman & Reiter) but a small literature.
- The COVID application: mortality tracked **latitude and obesity, not vaccination coverage**, because both limit NIR penetration and local melatonin production. **[Contested]** — the ecological correlation is real; the causal attribution is his and is confounded.

The morning pathway, stated concretely:

> **UV light energizes tryptophan → serotonin (OPN5/neuropsin sets the rhythm) → at night, pineal enzymes convert the accumulated serotonin to melatonin.**

*"Melatonin is 'made' in your eye in the morning via UV/IR-A light."* Hence the instruction to *"act like the Sphinx at sunrise"* — face east, unfiltered light on the eyes, limbs grounded.

The inversion worth noting: **poor sleep is a proxy for mitochondrial damage**, not merely a cause of it — supported by the observation that patients with diagnosed mitochondrial disease sleep badly.

## 5.3 Neuropsin and the regeneration cycle

Developed in *Time 9* and carried forward: **OPN5/neuropsin**, a UVA-sensitive opsin in cornea, skin, and retina, permits the retina to maintain a clock separable from other peripheral clocks. **[Established]** — Buhr *et al.*, *PNAS* 2015.

His extension: *"Time re-creation begins and ends with this neuropsin light meter in the cornea."* Neuropsin and melatonin together recycle mitochondria by lowering **heteroplasmy** — the proportion of mutant mtDNA in a cell, which he treats as the master aging variable. Hence the clinical injunctions: no sunglasses, no contacts, avoid UV-blocking implanted lenses.

His statement of clock architecture here is precise and correct: the human SCN free-runs slightly **longer** than 24 hours (mice shorter); nearly every tissue has a local clock; **all peripheral clocks except the retina must be synchronized by the SCN**, the retina being the one that maintains its own rhythm while supplying the master signal. **[Established]**

## 5.4 Melanin as the electrochemical time stamp

*QE #55* (2023) introduces the mechanism that distinguishes the late period:

> "THE TTFL USES MELANIN TO ELECTROCHEMICALLY TIME STAMP YOUR CELLS."

- Natural melanins contain indole-based tetramers arranged into **porphyrin-like domains**.
- **Sodium ions undergo occupancy-dependent stepwise insertion** into these tetramer cores at discrete electrochemical potentials — a real electrochemical fingerprinting result.
- These discrete potentials "time stamp the atomic lattice," giving cells an internal metric for entropy flow.
- The TTFL is a **limit cycle** — a closed loop returning to its trajectory after perturbation — *but only if the melanin structures are intact and continually renewed.*
- Therefore: chronic disease arises when electrochemical time-stamping degrades, **with no alteration to DNA or RNA whatsoever.**

**[Extrapolation]** — the melanin electrochemistry is real; its role as circadian time-stamp is entirely his.

He also introduces **CSP-1** as a morning-induced transcriptional repressor gating evening gene expression — *"If you do not get AM sun your evening genomic expression will be AWRY."* (CSP-1 is a *Neurospora* clock component; extending it to mammals is unsupported. **[Error]**)

## 5.5 The SCN as time crystal

*QE #44* (June 2023) is the most physics-forward post of the period, and the least reliable:

- The SCN is "an optical lattice clock... a true time crystal," receiving ipRGC input from the inferior nasal retina.
- Time crystals sustain periodic motion without expending energy, breaking time-translation symmetry.
- Therefore living things **must sleep**: sleep is when the entropy debt of maintaining a highly ordered time crystal is repaid — which he presents as vindication of his 2011 "sleep is primordial" claim.

The errors cluster densely:

- **[Error]** Attributes the time-crystal proposal to *"Feynman's 1982 paper."* That paper is *Simulating Physics with Computers* and says nothing about time crystals. Wilczek proposed them in **2012** — which Kruse states correctly two paragraphs later without noticing the contradiction.
- **[Error]** *"You appear to evade the second law of thermodynamics."* Discrete time crystals require a **periodic external drive** (Floquet systems) and are fully consistent with thermodynamics.
- **[Error]** Describes them as simultaneously in a lowest-energy state with time-invariant properties **and** as "dissipative far from equilibrium structures." These are incompatible.
- **[Error]** *"The retina wires directly to the SCN with no synapsing in between."* There is a real fact underneath — the ipRGC is both photoreceptor and projection neuron, so unlike the rod → bipolar → ganglion chain there's no *intraretinal* synapse — but the RHT axon certainly synapses in the SCN.
- **[Contested]** The HeartMath geomagnetic/HRV synchronization study (10 subjects, 31 days, ~2.5-day period).
- **[Extrapolation]** Schumann resonance (7.83 Hz) entraining thalamic alpha (8–12 Hz). The numerical proximity is often noted; no causal mechanism is established.

## 5.6 Water, vasopressin, and the sodium marker

*QE #23* (2023) adds a hydration axis:

- **Vasopressin (AVP)** is released before sleep in anticipation of nocturnal dehydration, and after every kind of brain injury.
- He classifies non-terrestrial light as **a form of traumatic brain injury** — *"Light injuries have become the most common non-military injury humans get."*
- AVP contains two aromatic amino acids and a disulfide bond — "two clues it is a circadian qubit."
- **Serum sodium > 142 mmol/L** associates with 39% increased chronic disease risk; > 144 with 21% elevated premature mortality. **[Established]** — real (Dmitrieva *et al.*, 2023). His inference that serum Na is *"a proxy for your light clock management at the SCN level"* is **[Extrapolation]**.
- MS patients respond to vasopressin antagonists, implicating chronic AVP release to light stress. **[Contested]**
- **REV-ERBα controls Cx43**, determining bladder capacity — hence nocturia in shift workers.

## 5.7 Sunrise and the TCA cycle

*QE #65* (February 2024) makes the most operationally specific claim in the corpus:

> "If you miss the sunrise, you cannot metabolize fat via the TCA cycle in your matrix. It becomes IMPOSSIBLE. This is why what you eat is superfluous if the light you do it in is not sunlight."

The mechanism: lipid rafts turn sunlight into DC current; that current stabilizes forward TCA cycling; the mitochondrial inner-membrane junctions "align perfectly every AM when you see the sunrise." He also rejects Mitchell's chemiosmotic theory as a "half-truth," citing Gilbert Ling: the ATPase can supply at most ⅓ of cellular ATP, with the remaining ⅔ coming from sunlight acting on water and melanin. **[Extrapolation]** — chemiosmosis is among the best-established results in bioenergetics; the ⅓ figure has no support.

The dietary rule that follows is the Leptin Rx restated as chronotherapy: *"Eat like a king 30 minutes after sunrise, like a prince at lunch, like a pauper at dinner."*

## 5.8 Diurnal death

*DM #67* (August 2025), the most recent major circadian post, reaches for **thanatotranscriptomic genes** — the ~1,000+ genes that upregulate for hours to days *after* death, documented in zebrafish and mice. **[Established]** as a phenomenon (Pozhitkov & Noble).

His reading, self-labeled as hypothesis: we undergo a partial **diurnal death** nightly; these genes regulate **ultraweak photon emission (UPE)** during it; melatonin drives the sleep respiratory-quotient shift from ~1.0 to ~0.7 by **inhibiting Complex I via cardiolipin**, promoting fat oxidation through FADH₂ and Complex II, and supporting mitochondrial photorepair. The RQ shift is **[Established]**; the melatonin/Complex I mechanism is his own and flagged as such.

---

# What runs through all five periods

Six claims survive every rebuild. These are the actual framework:

1. **Sleep is primordial; wakefulness is derived.** (2011 → 2023)
2. **Circadian and cell cycles are yoked** through PER1/PER2, making clock failure a cancer mechanism.
3. **Cells are oxidized by day and reduced by night** — the diurnal redox oscillation.
4. **The midnight window is when repair happens**, and food or light in the wrong place closes it.
5. **Light is the upstream controller; food is downstream.**
6. **The clock is hierarchical**, with the eye at the top.

Everything else — hypocretin, VIP/eNOS seasonal switching, the CSF vortex, ependymal SQUIDs, gravitational dilation, time crystals — is scaffolding that was erected and later removed.

# What changed, and when

| Mechanism | Introduced | Status now |
|---|---|---|
| Hypocretin as junction box | 2011 | Dropped after Period 1 |
| VIP/eNOS seasonal clock switching | 2012 (*CT-7*) | Dropped |
| Prolactin → GH autophagy gate | 2012 (*CT-7*) | **Explicitly contradicted** in 2023 ("GH released in slow wave sleep... is simply not true") |
| Peroxiredoxin / transcription-free clock | 2013 (*QB 12*) | Retained |
| Becker DC current | 2013 (*EE 9*) | Retained as background; mechanism no longer load-bearing |
| CSF vortex, pineal laser, ependymal SQUIDs | 2013 (*EE 9*) | **Silently abandoned** |
| Gravitational dilation at the SCN | 2015 (*Ubiq 2*) | Faded; no longer emphasized |
| Melanopsin hierarchical control | 2015 (*Ubiq 17*) | **Retained — core** |
| DHA as circadian gain control | 2015 (*Ubiq 17*) | Retained |
| Ubiquitin economy | 2015 (*Ubiq* series) | Retained, de-emphasized |
| NAD⁺/SIRT1/NAMPT loop | 2015 | **Retained — strongest anchor** |
| Leptin resistance = melanopsin dysfunction | 2018 (*QT 22*) | **Retained — the unification** |
| Mitochondrial melatonin | 2022 (*QE 18*) | **Retained — core of late period** |
| Melanin electrochemical time-stamping | 2023 (*QE 55*) | Current |
| SCN as time crystal | 2023 (*QE 44*) | Current |
| Thanatotranscriptome / diurnal death | 2025 (*DM 67*) | Current |

# The protocol, across time

Strikingly stable given three mechanism rewrites:

| Rule | First appears | Still current? |
|---|---|---|
| No food within 3–4 hrs of sleep | 2012 (*CT-7*) | Yes |
| Complete darkness for sleep | 2011 | Yes |
| Morning sun on the eyes, unfiltered | 2012 | Yes — now specified as UV index ≥ 1, 7 AM–noon, 3–5 min minimum |
| No sunglasses / contacts / windows | 2016 (*Time 9*) | Yes |
| Eat largest meal after sunrise | 2012 (Leptin Rx) | Yes (*QE 65*) |
| Blue-blockers after sunset | 2013 | Yes |
| Cold exposure as circadian tool | 2012 (*CT* series) | De-emphasized |
| Fasting only under natural light | 2019 (*food vs light*) | Yes — the key testable claim |

---

# Assessment

Reading all five periods in sequence produces a clearer verdict than any single period supports.

**The biology is frequently excellent.** His statements of the TTFL, the NAD⁺/SIRT1/NAMPT loop, DHA conservation and membrane biophysics, melanopsin ipRGC architecture, extrapineal melatonin, OPN5 photoentrainment, melatonin receptors on beta cells, and the peroxiredoxin transcription-independent clock are accurate, well-sourced, and in several cases were ahead of general clinical awareness by years. The extra-ocular opsin prediction genuinely came in (OPN3 in adipocytes, Nayak 2020).

**The physics is consistently unreliable.** Every time he reaches for relativity, thermodynamics, or condensed-matter physics, the argument fails on checkable grounds — the gravitational claim by thirteen orders of magnitude, the time crystal by misattribution and by misunderstanding what breaks in time-translation symmetry, the chemiosmosis rejection against overwhelming evidence. The pattern is specific enough to be a useful reading heuristic.

**The load-bearing argument is the weakest link.** "Light trumps food" rests, in its original 2012 form, on the 48%-vs-10% brain-wiring comparison, which does not support the conclusion. The claim may still be *partly* right for other reasons — circadian misalignment does produce metabolic harm independent of caloric intake — but the argument he actually gives for it is invalid.

**The most interesting thing he has done is Period 4.** The unification of leptin and melanopsin into a single photonic mechanism is a genuine intellectual move: it takes his weakest-supported early work and his strongest later work and makes them one claim, at the cost of a large extrapolation about leptin as an optical chromophore. Whether or not it survives, it is the hinge the whole framework turns on.

---

## Related documents in this repo

- `circadian_reconstruction.md` — the graded overview this expands on
- `circadian_primer.md` → `circadian_theory.md` → `circadian_protocol.md` — the mainstream-first chapter set (Feb 2026), useful as the reference frame
- `../evolution/semiconductor_theory.md` — the solid-state substrate underlying Periods 3–5 in depth
- `../evolution/evolution_cancer_digest.md` — the atavism/Warburg material that §3.9 connects to
- `../melanin/` — the melanin biology that Period 5 depends on

**Open follow-on:** a structured claim ledger — each discrete assertion with source post, date, mechanism invoked, and falsifiability rating — would make this queryable across all 463 circadian-relevant posts rather than the ~35 read here.
