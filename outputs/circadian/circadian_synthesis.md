# The Biology of Circadian Rhythm and Its Disruption

*A synthesis: established chronobiology as the spine, with Kruse's defensible contributions integrated and dated.*

---

## What this document is, and how to read it

The two companion documents in this folder reconstruct what Jack Kruse argues about circadian biology (`circadian_reconstruction.md` for the graded overview, `circadian_kruse.md` for the full exposition). This one asks a different question: **what is actually true?**

The spine is mainstream chronobiology. Kruse's claims appear where they add something defensible, marked like this:

> **[JK 2015]** — a claim he was making in that year, which survives scrutiny.

Where he is wrong, the claim is noted and rejected rather than silently omitted, because knowing *which* parts fail is part of the value.

**A note on why the dates matter.** Kruse rebuilt his mechanism three times between 2011 and 2025 while keeping the same conclusions. His retrospective accounts of when he figured things out are not reliable — in November 2013 he claimed to have been arguing light-over-food "for three years," when the post he cites as evidence is from September 2012 and his blog began in June 2011. The dates here come from the posts themselves, not from his account of them.

**The reliability heuristic that emerged from reading all 737 posts:** when Kruse reports other people's published biology, he is usually accurate and occasionally ahead of clinical awareness. When he constructs his own physics, the argument nearly always fails on checkable grounds. Almost everything credited to him below falls in the first category.

---



# Part I — What a circadian clock is



## 1.1 The defining properties

A circadian rhythm is not simply "a daily pattern." A daily pattern driven by the environment is a *diurnal* rhythm; it disappears when the environment is held constant. A true circadian clock has three properties, formalised by Colin Pittendrigh:

1. **Self-sustained oscillation.** It persists in constant conditions — constant darkness, constant temperature, no time cues — with a period *close to* but not exactly 24 hours. This "free-running period" is called **τ (tau)**. In humans, τ averages about **24.2 hours** (Czeisler *et al.*, 1999, using forced desynchrony to strip out masking effects).
2. **Temperature compensation.** Unlike almost every other biochemical process, the period barely changes across physiological temperatures. A clock that ran faster when you had a fever would be useless. This is one of the strongest arguments that the clock is not a simple chemical reaction cascade.
3. **Entrainability.** It can be reset by environmental cues (**zeitgebers**, "time-givers"), and the direction and size of the shift depend on *when* the cue arrives. This relationship is the **phase response curve (PRC)** — and it is the single most practically important concept in the field.



## 1.2 The phase response curve

For light in humans, roughly:


| Timing of light exposure                                              | Effect                                      |
| --------------------------------------------------------------------- | ------------------------------------------- |
| Early biological night (evening, before core temperature minimum)     | **Phase delay** — pushes the clock later    |
| Late biological night (after temperature minimum, i.e. early morning) | **Phase advance** — pulls the clock earlier |
| Mid-day                                                               | Little phase effect; increases amplitude    |


Core body temperature minimum typically falls **1–3 hours before habitual wake time**. This is the pivot. Light before it delays you; light after it advances you.

This single curve explains almost all practical circadian advice, and it explains why the *same* intervention can help or harm depending on timing. Melatonin has a PRC roughly inverted relative to light's.

> **[JK 2012]** — Kruse's protocol (morning sun immediately on waking; darkness after sunset) is a correct application of the light PRC, arrived at before he had any mechanism to justify it. Note that he never actually invokes the PRC by name; he reaches the right prescription by a different and much weaker route.

---



# Part II — The molecular clock



## 2.1 The transcription–translation feedback loop (TTFL)

The core mechanism, conserved in outline from flies to mammals. The 2017 Nobel Prize in Physiology or Medicine went to Hall, Rosbash, and Young for working it out in *Drosophila*.

**The positive arm.** Two bHLH-PAS transcription factors, **CLOCK** and **BMAL1**, heterodimerise, enter the nucleus, and bind **E-box** elements (core sequence CACGTG) in target promoters, driving transcription.

**The negative arm.** Among their targets are their own repressors: **PER1, PER2, PER3** and **CRY1, CRY2**. PER and CRY proteins accumulate in the cytoplasm, complex with casein kinase 1δ/ε, translocate back into the nucleus, and inhibit CLOCK/BMAL1 — shutting off their own transcription. As they degrade, repression lifts, and the cycle restarts.

**The stabilising loop.** CLOCK/BMAL1 also drive **REV-ERBα/β** and **RORα/β/γ**, which compete for ROR response elements in the *Bmal1* promoter — REV-ERB repressing, ROR activating. This produces the antiphase *Bmal1* rhythm and confers robustness.

> **[JK 2015]** — Kruse's statement of this loop in *Ubiquitination 16* is textbook-accurate, including the E-box consensus sequence and the REV-ERB/ROR secondary loop. Whatever else is true of him, he did his reading here.



## 2.2 Where the ~24 hours actually comes from

This is the part most summaries skip, and it matters. A transcription-translation loop does not automatically take 24 hours — left to itself it would oscillate far faster. **The period is set by imposed delays, and most of them are post-translational:**

- **Phosphorylation.** CK1δ/ε phosphorylate PER proteins, controlling both their stability and their nuclear entry timing. The human **FASP** (familial advanced sleep phase) syndrome is caused by a PER2 mutation (S662G) that removes a CK1 phosphorylation site — carriers run ~4 hours early. A CK1δ mutation produces the same phenotype.
- **Ubiquitination and degradation.** **β-TrCP** targets phosphorylated PER; **FBXL3** targets CRY. Mutations in FBXL3 lengthen period substantially.
- Also SUMOylation, acetylation, and O-GlcNAcylation.

So the clock's period is largely a **protein degradation-rate problem**, not a transcription problem.

> **[JK 2015]** — This is the legitimate core of Kruse's "ubiquitin economy." He was right that ubiquitin-mediated protein turnover is central to circadian timekeeping. Where he overreaches is in making *whole-organism ubiquitination rate* the master readout of health, and in claiming eukaryotes spend 80% of their energy budget on protein synthesis — a figure at the extreme end of plausible for differentiated tissue.



## 2.3 What the clock controls

Clock-controlled genes (CCGs) are the output. The scale is larger than most clinicians appreciate: surveying 12 mouse organs, **roughly 43% of all protein-coding genes are rhythmically expressed in at least one tissue** (Zhang *et al.*, 2014). Rhythmic genes are heavily enriched for rate-limiting enzymes and for drug targets — which is the entire basis of chronopharmacology.

The tissue-specificity matters: most rhythmic genes cycle in only one or two organs. There is no single "circadian program"; there are hundreds of tissue-specific ones sharing a timing signal.

---



# Part III — Clocks without transcription

The TTFL is not the whole story, and this is one of the genuinely surprising findings of the last two decades.

**The cyanobacterial KaiABC oscillator.** Three purified proteins — KaiA, KaiB, KaiC — plus ATP, in a test tube, sustain a temperature-compensated ~24-hour phosphorylation rhythm for days with no transcription whatsoever (Nakajima *et al.*, 2005). A clock reduced to protein biochemistry.

**Peroxiredoxin oxidation cycles.** In 2011, two *Nature* papers showed:

- **Human red blood cells** — which have no nucleus and cannot transcribe anything — sustain a ~24-hour rhythm in peroxiredoxin oxidation state (O'Neill & Reddy).
- ***Ostreococcus tauri***, a picoalga held in constant darkness, shows no detectable transcription, yet on return to light resumes its rhythm *at the phase a running clock would predict* — not from a reset zero (O'Neill *et al.*).

Follow-up work found peroxiredoxin rhythms conserved across all three domains of life (Edgar *et al.*, 2012), making them arguably the most ancient circadian marker known.

**What this means.** Circadian timekeeping is not fundamentally a genetic phenomenon. There is a redox-based oscillator underneath the transcriptional one, and the TTFL appears to be a later, more controllable layer built on top.

> **[JK 2013]** — *Quantum Biology 12* is built entirely on these two papers and is his single best piece of argumentation. He grasped the implication early: if the clock predates and outlives transcription, then genes are not the timekeeper. His inference from there — that light acting on "coherent water" is the true transducer, via Fröhlich coherence — is unsupported. But the observation he built on is real and important, and he was reading it within months of publication.

---



# Part IV — The central pacemaker



## 4.1 The suprachiasmatic nucleus

The **SCN** is a paired nucleus of roughly **20,000 neurons** in humans, sitting immediately above the optic chiasm at the base of the hypothalamus.

Evidence that it is the master clock:

- **Lesion** it and behavioural rhythms disappear.
- **Transplant** an SCN from a mutant hamster with a short period into an arrhythmic host, and the host adopts the *donor's* period (Ralph *et al.*, 1990) — the decisive experiment.
- Isolated SCN tissue continues oscillating in culture for weeks.



## 4.2 Why the network matters more than the neuron

Individually, SCN neurons are mediocre oscillators — noisy, with scattered periods. The precision is a **network property**, produced by coupling.

- The **core** (ventrolateral) region is retinorecipient and expresses **VIP** and GRP.
- The **shell** (dorsomedial) expresses **AVP**.
- **VIP signalling through the VPAC2 receptor is essential for synchrony.** Knock out VIP or VPAC2 and the SCN becomes behaviourally arrhythmic — not because individual cells stop oscillating, but because they stop agreeing.

This coupling is also why the SCN is stubborn. It resists rapid phase shifts, which is precisely why jet lag takes days to resolve.

> **[JK 2012]** — Kruse's account of VIP/VPAC2 in *Cold Thermogenesis 7* is accurate and well-sourced, including the 9–24% expression figure and VPAC2-ablation arrhythmia. His extension — that VIP governs a *summer* clock while eNOS, NPY, and α-MSH govern a separate *winter* clock — is his own and is not supported. He dropped it after 2012.

---



# Part V — Light input: the non-image-forming pathway



## 5.1 A third photoreceptor

Until the late 1990s, rods and cones were assumed to be the eye's only photoreceptors. Then:

- Mice lacking all rods and cones still entrained to light.
- **Melanopsin (OPN4)** was identified (Provencio *et al.*, 1998–2000).
- **Intrinsically photosensitive retinal ganglion cells (ipRGCs)** were shown to depolarise to light directly, in isolation, with rods and cones pharmacologically blocked (Berson, Dunn & Takao, 2002).

ipRGCs make up only about **1–2% of retinal ganglion cells**. They are:

- **Peak sensitive at ~480 nm** — blue, but *not* the same as the blue-cone peak
- **Slow, sustained, and high-threshold** — irradiance detectors, not image detectors. They report "how much light is there, overall, right now," integrated over minutes.
- Projecting via the **retinohypothalamic tract (RHT)** to the SCN, and also to the olivary pretectal nucleus (pupillary reflex), the intergeniculate leaflet, the habenula (mood), and the ventrolateral preoptic nucleus (sleep).

Phototransduction runs through Gq/11 → PLCβ4 → TRPC6/7 — an invertebrate-like cascade, unlike the rod/cone system.

**Rods and cones are not irrelevant.** They feed into ipRGCs and contribute to entrainment, especially at low light levels. Abolishing entrainment entirely requires a triple knockout (Hattar *et al.*, 2003). The ipRGC is the *final common path*, not the sole input.

**Clinically decisive observation:** blind people with intact ipRGCs entrain normally despite having no visual perception. Those without light perception at all — enucleated, or with total retinal loss — develop **non-24-hour sleep-wake disorder**, free-running with a τ slightly over 24 hours, drifting in and out of phase with the world every few weeks.

> **[JK 2015]** — The "your eye is a clock before it is a camera" framing is a genuinely good piece of science communication and is correct. Two caveats on his version: he gives melanopsin's peak as 435–465 nm, consistently blue-shifted from the accepted ~480 nm; and he insists melanopsin controls entrainment "exclusively," which overstates a system where rods and cones demonstrably contribute.



## 5.2 Other opsins

**OPN5 (neuropsin)** is UV/violet-sensitive and photoentrains local oscillators in the retina and cornea independently of melanopsin (Buhr *et al.*, 2015).

Opsins are also expressed well outside the eye — **OPN4 and OPN3 in skin**, and **OPN3 in adipocytes**, where light exposure has been shown to modulate lipolysis (2020).

> **[JK 2012 → confirmed 2015–2020]** — This is Kruse's best genuine prediction, and it deserves credit. He argued from his cold-thermogenesis protocol that a melanopsin-like photoreceptor *had to* exist in skin, and later that opsins would be found in subcutaneous fat. Both came in. Whether extra-ocular opsins contribute meaningfully to *systemic entrainment* in humans remains unresolved — but the existence claim was his, and it was right.



## 5.3 What actually counts as bright

A practical point often lost:


| Environment                                    | Illuminance                                     |
| ---------------------------------------------- | ----------------------------------------------- |
| Overcast daylight, outdoors                    | 1,000–10,000 lux                                |
| Direct sunlight                                | 30,000–100,000 lux                              |
| Well-lit office                                | 300–500 lux                                     |
| Living room, evening                           | 50–200 lux                                      |
| Threshold for meaningful melatonin suppression | ~30–100 lux (varies widely between individuals) |


Indoor daytime light is roughly **1–2 orders of magnitude too dim** to entrain robustly, and evening indoor light is easily bright enough to suppress melatonin. This — not any exotic mechanism — is the core of the modern circadian problem: **days too dim, nights too bright.**

> **[JK 2019]** — Kruse's point that ordinary window glass blocks essentially all UVB, most UVA, and a substantial fraction of IR-A is correct, and his conclusion that "indoors" is a spectrally amputated environment follows. The illuminance argument above is stronger and simpler than the spectral one he prefers, and he rarely makes it.

---



# Part VI — Peripheral clocks and internal synchrony



## 6.1 Clocks are everywhere

Essentially every nucleated cell has a functioning TTFL. Liver, gut, pancreas, adipose, muscle, kidney, skin, immune cells — all oscillate autonomously in culture.

The SCN does not *impose* rhythmicity on them. It **synchronises** oscillators that would otherwise run at their own periods and drift apart. Its signals are:

- **Neural** — autonomic outflow
- **Humoral** — notably **glucocorticoids**, a powerful peripheral sync signal
- **Body temperature** — the SCN-driven ~1°C daily temperature rhythm is itself a zeitgeber for peripheral clocks (Buhr, Yoo & Takahashi, 2010). Elegantly, peripheral clocks are resettable by temperature while the SCN itself is not — so the master clock doesn't reset itself with its own output.
- **Feeding-related signals**



## 6.2 Feeding can override the SCN — locally

This is the most important qualification to any simple hierarchy story. **Restricted feeding at an abnormal time uncouples the liver clock from the SCN entirely** (Damiola *et al.*, 2000; Stokkan *et al.*, 2001). The liver phase-shifts to match food availability within days, while the SCN, entrained by light, stays put.

The result is **internal desynchrony**: a correctly-timed brain and an incorrectly-timed liver.

**This matters for evaluating the "light trumps food" claim.** Light is the dominant zeitgeber *for the SCN*. Food is the dominant zeitgeber *for much of the periphery*. Neither trumps the other in general — they entrain different clocks, and health depends on the two agreeing.

> **[JK 2012, and maintained through 2025]** — This is where Kruse's central slogan is genuinely wrong, not merely overstated. The strong form — that food is downstream of light and "you can eat shit on a shingle if your light environment is optimized" (2019) — is contradicted by the restricted-feeding literature, which predates his claim by a decade. Meal timing entrains peripheral clocks independently of light. His *practical* advice (eat in the daytime, don't eat late) is well supported; his stated reason for it is not.



## 6.3 The retinal exception

The retina is the one peripheral tissue that entrains directly to light on its own, maintaining rhythms independently while supplying the SCN with its signal.

> **[JK 2016]** — Correctly stated in *Time 9*, including the detail that human SCN τ runs slightly over 24 hours while nocturnal rodents run slightly under.

---



# Part VII — Outputs



## 7.1 Melatonin

Synthesised in the pineal via a multi-synaptic pathway: SCN → paraventricular nucleus → intermediolateral cell column → superior cervical ganglion → pineal. Rate-limiting enzyme **AANAT**.

Key properties:

- Secreted **only in darkness**; acutely suppressed by light
- **Dim light melatonin onset (DLMO)** is the gold-standard marker of circadian phase
- It is a *signal of darkness*, not a sleep-inducer per se — hence its modest hypnotic effect and its strong phase-shifting effect at the right time
- Exogenous melatonin has a PRC roughly inverted from light's: evening doses advance, morning doses delay
- Low doses (0.3–0.5 mg) are generally as effective as high for phase-shifting, with fewer next-day effects

**Extrapineal melatonin.** Melatonin is synthesised far beyond the pineal — gut (in far greater total quantity than the pineal), retina, skin, bone marrow, lymphocytes, and within mitochondria. Extrapineal melatonin is largely **non-rhythmic and locally acting**, functioning as an antioxidant rather than a timing signal. Pinealectomy abolishes the circulating rhythm but not tissue melatonin.

> **[JK 2022]** — Kruse's re-centering of melatonin on its mitochondrial and antioxidant roles is well-founded and reflects a real literature (Reiter, Tan, Acuña-Castroviejo) that remains underappreciated clinically. **Important qualification he elides:** extrapineal melatonin is not a circadian signal. Conflating the two lets him imply that boosting tissue melatonin through sun exposure improves *timing*, which does not follow.

> **[JK 2016]** — His claim that melatonin and insulin are opposed signals is correct and was prescient. **MT1/MT2 receptors are present on pancreatic beta cells, and melatonin inhibits insulin secretion.** The **MTNR1B** locus (melatonin receptor 1B) is among the most robustly replicated type 2 diabetes risk variants in human genetics (2009). Eating at a time of high circulating melatonin — i.e. late at night — produces measurably worse glucose tolerance, and this effect is modified by MTNR1B genotype. His conclusion that "insulin resistance is a light-at-night problem" overstates a real and well-evidenced mechanism.



## 7.2 Cortisol

Peaks ~30–45 minutes after waking (the **cortisol awakening response**), falls across the day, nadir around midnight. Driven by the SCN via the HPA axis, and a major sync signal to peripheral clocks.

## 7.3 Core body temperature

~1°C amplitude, minimum 1–3 hours before habitual wake. The most reliable non-invasive phase marker after DLMO, and — as above — a zeitgeber in its own right.

## 7.4 Sleep–wake: the two-process model

Borbély's framework remains the standard:

- **Process S** — homeostatic sleep pressure, accumulating with time awake (adenosine is the leading candidate substrate), dissipating during sleep
- **Process C** — circadian alertness signal, independent of prior sleep

Sleep timing and quality emerge from the *interaction*. The circadian system actively promotes wakefulness in the evening ("wake maintenance zone") just as sleep pressure peaks, and promotes sleep in the early morning as pressure falls. Misalignment between S and C — not either alone — produces most insomnia phenotypes.

> **[JK 2012]** — Kruse's adenosine account is broadly correct. His specific claim that leptin entry into the brain at midnight triggers a prolactin surge that gates GH release and autophagy is his own construction and is not supported as a serial dependency, though each component is individually real. He reversed himself on the GH element in 2023, asserting that GH release in slow-wave sleep "is simply not true" — on the mainstream evidence he was closer to right in 2012.



## 7.5 Metabolism and redox

The clock and metabolism are bidirectionally coupled, and this is among the best-established mechanistic links in the field:

- **NAD⁺ levels oscillate**, driven by **NAMPT**, the rate-limiting salvage enzyme, which is itself a clock-controlled gene.
- **SIRT1**, an NAD⁺-dependent deacetylase, deacetylates **BMAL1 and PER2**, feeding back onto the core loop.
- So the clock drives NAD⁺, and NAD⁺ availability drives the clock (Nakahata *et al.*, Asher *et al.*, 2008; Ramsey *et al.*, 2009).

Peroxiredoxin redox cycles (Part III) sit underneath this as an even more primitive layer.

> **[JK 2015]** — Kruse identified this loop early and made it central. It remains the strongest mechanistic anchor in his framework across all five periods, and he reports it accurately.



## 7.6 Immunity, cell cycle, and DNA repair

- **TLR9** expression and responsiveness are rhythmic; sepsis severity and vaccine response both vary with time of administration (2012).
- The circadian clock gates the **cell cycle**, partly through PER2's effects on Cyclin D1, c-Myc, and Wee1. *Per2*-mutant mice show increased tumour incidence.
- **DNA repair** capacity, including nucleotide excision repair, is rhythmic.

> **[JK 2011]** — The circadian/cell-cycle yoke and its cancer implication was in his very first sleep post, accurately reported, including the *Per2* mouse data. This predates his light work entirely.

---



# Part VIII — Disruption



## 8.1 Five distinct failure modes

Lumping these together causes most of the confusion in popular writing:


| Mode                          | What it is                                                        | Typical cause                    |
| ----------------------------- | ----------------------------------------------------------------- | -------------------------------- |
| **Phase shift**               | Clock correctly aligned internally, wrong relative to environment | Jet lag                          |
| **Chronic misalignment**      | Behaviour repeatedly opposed to internal time                     | Shift work                       |
| **Internal desynchrony**      | Central and peripheral clocks disagree                            | Late eating, shift work          |
| **Amplitude reduction**       | Rhythm intact but flattened                                       | Dim days, ageing, constant light |
| **Intrinsic phase disorders** | Clock itself abnormal                                             | DSPD, ASPD/FASP, non-24          |


**Amplitude reduction is the most common and the least discussed.** Most people in modern indoor environments do not have a *shifted* clock so much as a *weak* one — insufficient light contrast between day and night to drive a robust oscillation.

## 8.2 What the evidence actually shows

**Controlled human misalignment.** Scheer *et al.* (2009) put subjects on a 28-hour day, forcing behaviour out of phase with internal time. Within ten days: leptin fell, glucose and insulin rose, mean arterial pressure rose, and **three of eight subjects met criteria for a prediabetic state**. Diet and sleep duration were controlled. This is the cleanest demonstration that misalignment alone produces metabolic harm.

**Sleep restriction combined with disruption.** Buxton *et al.* (2012) found reduced insulin secretion and elevated postprandial glucose under combined sleep restriction and circadian disruption.

**Shift work and cancer.** IARC classified shift work involving circadian disruption as **Group 2A, "probably carcinogenic to humans"** (2007, reviewed 2019). The evidence is strongest for breast cancer, though heterogeneous, and confounding by sleep loss and light exposure is difficult to fully separate.

**Meal timing.** Delaying meals by five hours delays peripheral clock gene rhythms in adipose tissue without shifting central markers (Wehrens *et al.*, 2017) — direct human evidence for induced internal desynchrony.

**Light at night.** Epidemiological work associates bedroom light at night with obesity, metabolic syndrome, and depressive symptoms. These are observational and confounded, but consistent.

## 8.3 Why misalignment causes harm

Four mechanisms, in rough order of evidential strength:

1. **Loss of temporal segregation.** Circadian organisation exists partly to keep incompatible processes apart — DNA replication from repair, anabolism from catabolism, inflammation from regeneration. Desynchrony lets them overlap.
2. **Signalling at the wrong time.** Eating during the melatonin window impairs glucose handling; cortisol at the wrong phase disrupts peripheral clocks.
3. **Amplitude collapse.** Reduced amplitude weakens every downstream rhythm, including the NAD⁺/SIRT1 cycle.
4. **Loss of anticipation.** The clock's evolutionary function is to prepare *before* events. A disrupted clock is always reacting.

> **[JK 2019]** — Kruse's most testable claim belongs here: that the metabolic benefit of fasting is *gated* by circadian alignment — "it won't work in fake light when ALAN is present." This is a genuine, falsifiable hypothesis. It is broadly consistent with the time-restricted eating literature, where **early** TRE outperforms late TRE, but the specific claim that light environment gates fasting benefit has not been directly tested. It remains the most interesting untested idea in his corpus.

---



# Part IX — What actually helps

Ranked by evidential strength:

**Strong evidence:**

1. **Bright light in the morning.** Outdoors if possible — even overcast daylight is 10–20× a lit office. This advances and strengthens the rhythm.
2. **Darkness at night.** Dim, warm light after sunset; dark bedroom. Targets both melatonin suppression and phase delay.
3. **Regular sleep and wake times**, including weekends. Social jet lag is real and measurable.
4. **Appropriately timed melatonin** for phase shifting — low dose, hours before target sleep onset. Not a hypnotic.
5. **Light therapy** for seasonal affective disorder and delayed sleep phase disorder — well established.
6. **Tasimelteon** for non-24 in blind patients — a genuine mechanism-derived therapy.

**Moderate evidence:**
7. **Earlier eating window.** Early TRE outperforms late TRE for glucose control; benefit appears to come from timing more than from the fast itself.
8. **Avoiding food in the 3 hours before bed** — melatonin/insulin antagonism gives this a clear mechanism.
9. **Daytime light exposure at work** — increasing daytime illuminance, not just cutting evening light.

**Weak or contested:**
10. **Blue-blocking glasses.** Mechanistically sensible, but trial results are mixed and effect sizes modest. Reducing overall illuminance likely matters as much as spectrum.
11. **Deliberate UV exposure.** Kruse's position, and the sharpest divergence from dermatological consensus. Vitamin D, nitric oxide release, and mood effects are real; skin cancer risk is also real. This is a genuine risk–benefit question, not a settled one either way.

> **[JK 2012–2025]** — Items 1, 2, 3, and 8 are all in Kruse's protocol from 2012 onward and are well supported. Item 11 is his and is contested. The striking thing is how little his *advice* has changed while his *explanations* were rebuilt three times — which suggests the protocol was arrived at first and the mechanisms retrofitted.

---



# Part X — The Kruse ledger, by year

Every substantive claim, dated to first appearance, with a verdict.


| Year | Claim                                                                                           | Verdict                                                                                                                             |
| ---- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| 2011 | Circadian and cell cycles are yoked via PER1/2; clock disruption is a cancer mechanism          | **Correct**                                                                                                                         |
| 2011 | Sleep and metabolism fail together because they share hypothalamic control                      | **Directionally right**; his specific chain has leptin and glucose *exciting* orexin neurons, which is backwards — both inhibit     |
| 2011 | Sleep is the primordial state, wakefulness derived                                              | **Speculative**, unresolved, not unreasonable                                                                                       |
| 2012 | Hour-by-hour hormonal day (cortisol, BP, temperature, leptin, GH)                               | **Broadly correct in outline**; stated with more precision than the evidence supports                                               |
| 2012 | Don't eat within 3–4 h of sleep                                                                 | **Correct**, later vindicated by chrononutrition                                                                                    |
| 2012 | Light > food ("48% of brain is light-wired vs 10% leptin outflow")                              | **Conclusion partly right, argument invalid.** Cortical area ≠ control authority; also contradicted by restricted-feeding data      |
| 2012 | Extra-ocular photoreceptors must exist in skin                                                  | **Correct — his best prediction**                                                                                                   |
| 2012 | VIP/VPAC2 essential to SCN function                                                             | **Correct**                                                                                                                         |
| 2012 | Separate summer (VIP) and winter (eNOS/NPY/α-MSH) clocks                                        | **Unsupported**; he abandoned it                                                                                                    |
| 2013 | Transcription-independent clocks (peroxiredoxin) are foundational                               | **Correct and early — his best argument**                                                                                           |
| 2013 | CSF vortex, pineal-as-laser, ependymal SQUIDs drive sleep                                       | **Reject.** No supporting evidence; silently abandoned by ~2020                                                                     |
| 2015 | The eye is a clock before it is a camera; melanopsin ipRGCs are the entrainment path            | **Correct** (peak given as 435–465 nm; true value ~480 nm)                                                                          |
| 2015 | DHA is required for photoreceptor membrane function                                             | **Correct biology**, overextended to whole-body circadian gain                                                                      |
| 2015 | Ubiquitin-mediated turnover is central to clock timing                                          | **Correct** in mechanism; "80% of energy budget" overstated                                                                         |
| 2015 | NAD⁺/SIRT1/NAMPT couples clock to metabolism                                                    | **Correct — his strongest anchor**                                                                                                  |
| 2015 | Gravitational time dilation requires the SCN to run fast                                        | **Reject.** Off by ~~13 orders of magnitude (~~0.5 μs over a lifetime)                                                              |
| 2015 | Metals precipitating in tissue speed organ clocks; explains copper IUDs                         | **Reject.** Copper IUDs act via copper ions and endometrial inflammation                                                            |
| 2016 | Melatonin and insulin are opposed; light at night drives insulin resistance                     | **Substantially correct** — MT1/MT2 on beta cells, MTNR1B is a replicated T2D locus                                                 |
| 2016 | Warburg metabolism is the cell braking its clock in a bad light environment                     | **Speculative**, but an interesting reframing                                                                                       |
| 2017 | Skin is a circadian organ; CLOCK/PER2 modulate psoriasis                                        | **Correct**                                                                                                                         |
| 2018 | Melanopsin's retinal Schiff base is unusually unstable in humans                                | **Correct** — real published finding                                                                                                |
| 2018 | Leptin resistance *is* melanopsin dysfunction; leptin is an optical chromophore                 | **Reject the strong form.** No support for leptin as a light-sensing molecule                                                       |
| 2019 | Window glass blocks UVB/most UVA                                                                | **Correct**                                                                                                                         |
| 2019 | Fasting's benefit is gated by light environment                                                 | **Testable, untested — the most interesting open claim**                                                                            |
| 2022 | Melatonin is made throughout the body, including mitochondria; primarily an antioxidant         | **Correct**, but conflates non-rhythmic tissue melatonin with the circadian signal                                                  |
| 2022 | Morning UV drives tryptophan → serotonin, loading evening melatonin synthesis                   | **Plausible, partly supported**; each link real, the chain is his                                                                   |
| 2023 | The SCN is a time crystal                                                                       | **Reject.** Misattributed to Feynman (it was Wilczek, 2012); time crystals require periodic driving and do not evade the second law |
| 2023 | Schumann resonance (7.83 Hz) entrains thalamic alpha                                            | **Reject.** Numerical coincidence, no mechanism                                                                                     |
| 2023 | Melanin electrochemically time-stamps cells                                                     | **Speculative.** The melanin electrochemistry is real; the circadian role is invented                                               |
| 2024 | Missing sunrise makes TCA-cycle fat oxidation "impossible"; chemiosmosis supplies only ⅓ of ATP | **Reject.** Contradicts well-established bioenergetics                                                                              |
| 2025 | Thanatotranscriptomic genes mediate a nightly "diurnal death" via ultraweak photon emission     | **Speculative.** The post-mortem gene expression is real; the interpretation is his                                                 |




**Tally:** of 31 dated claims — **14** correct or substantially correct, **5** partly right or overextended, **4** speculative, **7** rejected, and **1** testable-but-untested.

**The distribution is the finding.** Every rejected claim is one where he constructed physics. Almost every correct claim is one where he reported biology. The proportion of rejections also rises sharply after 2022.

---



## Bottom line

A defensible circadian framework does not require anything unique to Kruse. The mechanism is: **a redox oscillator overlaid by a transcription-translation loop, coordinated by an SCN that reads irradiance through melanopsin ipRGCs, distributed to peripheral clocks that are also entrained by feeding, with metabolism coupled in through NAD⁺/SIRT1.** Disruption is best understood as five distinct failure modes, of which amplitude collapse is the most prevalent.

What Kruse contributes, at his best, is **emphasis and early attention**: he was reading the peroxiredoxin papers in 2013, insisting on non-visual photoreception in 2015, predicting extra-ocular opsins in 2012, and taking mitochondrial melatonin seriously well before it was fashionable. Those are real merits.

What he contributes at his worst is a physics overlay that fails every time it can be checked, and a central slogan — light trumps food — whose strong form was already contradicted by the restricted-feeding literature before he first stated it.

---



## Related documents

- `circadian_reconstruction.md` — graded overview of Kruse's position
- `circadian_kruse.md` — full exposition of the circadian framework, with sources
- `circadian_primer.md`, `circadian_theory.md`, `circadian_protocol.md` — the earlier mainstream-first chapter set (Feb 2026)
- `../evolution/semiconductor_theory.md` — the solid-state substrate underlying his Periods 3–5

