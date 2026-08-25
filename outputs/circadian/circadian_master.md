# Circadian Organization

## Foundations and Health

---

# PART I — BIOLOGICAL FOUNDATIONS

---

## 1. Scope and definitions

**Chronobiology** — the study of endogenous biological timing systems and their interaction with environmental cycles.

**Circadian rhythm** — an endogenously generated oscillation with a period of approximately 24 hours, distinguished from a merely daily (*diurnal*) pattern by three properties: it persists in constant conditions, its period is temperature-compensated, and it is entrainable by environmental cues.

**Zeitgeber** — an environmental cue capable of entraining a circadian oscillator. The dominant zeitgeber for the central pacemaker is the light–dark cycle. Feeding time, temperature, physical activity, and social cues act as zeitgebers for peripheral oscillators.

**Entrainment** — the process by which an endogenous oscillator is brought into stable phase relationship with an external cycle.

**Phase** — the position of an oscillator within its cycle, referenced to a marker such as dim light melatonin onset (DLMO) or core body temperature minimum.

**τ (tau)** — the free-running period expressed in the absence of time cues. In humans τ averages approximately 24.2 hours (Czeisler et al., 1999).

**Amplitude** — the magnitude of oscillation. Amplitude and phase are independent properties; a rhythm can be correctly timed yet weak.

**Circadian misalignment** — a stable but incorrect phase relationship between internal time and either the external environment or other internal oscillators.

> **Central thesis** — Circadian organisation is a global constraint system on cellular behaviour. Temporal order limits the degrees of freedom available to cells and tissues. Disease of timing follows when that constraint weakens: processes that should be sequential run concurrently, and the error rate of every one of them rises.

---

## 2. The oscillator

### 2.1 Defining properties

Self-sustained oscillation persists under constant darkness, constant temperature, and the absence of social cues. Isolated tissue, and isolated single cells, continue to oscillate for weeks in culture.

Temperature compensation holds the period nearly constant across the physiological temperature range. Reaction rates in the underlying biochemistry vary with temperature in the ordinary way; the network is arranged so that these variations cancel.

Entrainment is phase-dependent. The magnitude and direction of the shift produced by a stimulus depend on the phase at which it arrives, described by the **phase response curve (PRC)**.

### 2.2 The light phase response curve

For light in humans:

| Timing relative to core temperature minimum | Effect |
|---|---|
| Several hours before (biological evening and early night) | Phase delay |
| Immediately after (biological late night and early morning) | Phase advance |
| Mid-subjective day | Minimal phase shift; amplitude reinforcement |

Core body temperature minimum falls approximately 1–3 hours before habitual wake time. Light received before this point delays the clock; light received after it advances the clock. Magnitude scales with irradiance, duration, and spectral composition, and saturates at high intensity.

Exogenous melatonin exhibits an approximately inverted PRC: administration in the biological evening advances phase, administration in the biological morning delays it.

The PRC is the formal basis for all timing-dependent intervention. The same exposure is corrective or harmful according to when it is received.

### 2.3 The transcription–translation feedback loop

The core molecular oscillator in mammals is a delayed negative feedback loop operating on a period of approximately 24 hours.

**Positive arm.** The basic helix-loop-helix PAS-domain transcription factors **CLOCK** and **BMAL1** heterodimerise, translocate to the nucleus, and bind **E-box** elements (consensus CACGTG) in target promoters, activating transcription.

**Negative arm.** Among the genes activated are **PER1**, **PER2**, **PER3**, **CRY1**, and **CRY2**. Their protein products accumulate in the cytoplasm, form complexes with casein kinase 1δ/ε, re-enter the nucleus, and inhibit CLOCK/BMAL1-mediated transactivation, suppressing their own transcription. Progressive degradation of the repressor complex relieves inhibition and the cycle restarts.

**Stabilising arm.** CLOCK/BMAL1 additionally drive **REV-ERBα/β** and **RORα/β/γ**, which compete for ROR response elements in the *Bmal1* promoter, REV-ERB repressing and ROR activating. This generates the antiphase *Bmal1* rhythm and confers robustness against perturbation.

The output of this loop is the set of **clock-controlled genes**. Across twelve mouse organs, approximately 43% of protein-coding genes are rhythmically expressed in at least one tissue (Zhang et al., 2014), with rhythmic transcripts enriched for rate-limiting enzymes and pharmacological targets. Most rhythmic genes cycle in only one or two tissues; there is no single circadian program, but many tissue-specific programs sharing a timing reference.

### 2.4 Determination of period

The approximately 24-hour period is not intrinsic to transcription and translation, which alone would oscillate considerably faster. Period is set principally by imposed delays at the post-translational level.

**Phosphorylation.** CK1δ/ε phosphorylate PER proteins at multiple sites, governing both stability and the timing of nuclear entry. In familial advanced sleep phase syndrome, a PER2 mutation (S662G) abolishes a CK1 phosphorylation site and advances phase by approximately four hours; mutation of CK1δ produces the same phenotype.

**Ubiquitination and proteasomal degradation.** β-TrCP targets phosphorylated PER; FBXL3 targets CRY. Loss-of-function in FBXL3 substantially lengthens period.

**Additional modifications.** SUMOylation, acetylation, and O-GlcNAcylation further modulate stability and activity.

Period is therefore largely determined by protein turnover kinetics.

Kruse (2015) develops this observation into a general principle of cellular economics. Protein synthesis is the dominant energetic expenditure of eukaryotic cells, each peptide bond costing approximately five ATP — several times the cost of nucleotide polymerisation. Because ubiquitin marking governs the rate of that expenditure, and because clock proteins are themselves regulated by ubiquitin-mediated degradation, Kruse treats organism-wide ubiquitination rate as the principal quantity that circadian organisation exists to control. In this framing, chronic elevation of protein turnover — driven by signalling errors originating in the light environment — constitutes the common pathway from environmental mismatch to accelerated cellular ageing, replicative exhaustion, and telomere attrition. Kruse (2018) extends the same logic to interpret elevated fasting glucose as a marker of raised ubiquitination rate rather than solely of impaired fuel handling.

### 2.5 Non-transcriptional oscillators

Circadian timekeeping does not require transcription.

A self-sustained oscillator requires three elements: negative feedback, a delay long enough to prevent the system settling into a steady state, and a nonlinearity that converts smooth feedback into a cycle. The transcription–translation loop supplies the delay through transcription, translation, nuclear import, and phosphorylation. Non-transcriptional oscillators supply the same delay through slow chemistry performed on proteins that are already present, and they therefore continue to run in cells that cannot transcribe at all.

**The KaiABC phosphorylation cycle.** In cyanobacteria, the three purified proteins KaiA, KaiB, and KaiC, combined with ATP, sustain a temperature-compensated circadian phosphorylation rhythm in vitro for several days in the complete absence of transcription (Nakajima et al., 2005). The mechanism is fully reconstituted and is the clearest available account of how a protein keeps time.

KaiC assembles as a hexamer of two stacked ring domains, CI and CII, each with ATPase activity. Two residues in the CII ring, Thr432 and Ser431, are phosphorylated and dephosphorylated by KaiC itself. The reactions are not independent: they proceed through an obligatory ordered sequence, unphosphorylated → Thr432 alone → both residues → Ser431 alone → unphosphorylated, with each state reachable only from the one preceding it (Nishiwaki et al., 2004; Rust et al., 2007). A complete circuit must therefore traverse four states in fixed order, and the cycle cannot short-circuit back to its starting point.

KaiA binds exposed loops on the CII ring and stimulates autophosphorylation, driving the sequence forward. Phosphorylation of Ser431 propagates a conformational change through the hexamer to the CI ring, exposing a binding site that is otherwise cryptic. KaiB then binds that site, undergoing a rare fold switch from its ground-state conformation into a thioredoxin-like fold in order to do so (Chang et al., 2015). Bound KaiB captures KaiA and sequesters it, withdrawing the phosphorylation stimulus. KaiC then autodephosphorylates by running the phosphotransfer in reverse, returning phosphate to ADP and regenerating ATP. When Ser431 is finally dephosphorylated the CI site closes, KaiB and KaiA are released, and the cycle restarts. Negative feedback is therefore delivered not by a protein suppressing its own synthesis but by a protein progressively converting itself into the conformation that shuts off its own activator.

Period is set by the CI ATPase, which is extraordinarily slow: approximately ten to fifteen ATP hydrolysed per KaiC monomer per day. Across a panel of period mutants the ATPase rate is inversely proportional to the period of the resulting oscillation (Terauchi et al., 2007). Temperature compensation is a property of that same rate-limiting step. Because individual hexamers would otherwise drift apart in phase, coherence across the population is maintained by monomer exchange: hexamers continuously swap subunits, which pulls fast and slow molecules back toward a common phase and prevents the ensemble rhythm from damping out (Kageyama et al., 2006).

The timekeeping element is thus a queue of covalent modifications advancing through a fixed sequence at a rate limited by a slow, temperature-compensated ATPase — not a loop of changing concentrations. The quantity that cycles is the phosphorylation state of a single protein.

The Kai oscillator is not itself a redox cycle, but redox is how it reads the environment. The plastoquinone pool of the photosynthetic electron transport chain becomes oxidised when light fails at dusk, and oxidised quinones bind KaiA directly and destabilise it, delivering the phase signal to the oscillator (Wood et al., 2010; Kim et al., 2012). Light reaches the cyanobacterial clock as a change in the oxidation state of an electron carrier rather than through a photoreceptor.

**What redox state is.** A cell holds its electrons in a small number of shared carrier pools: NAD⁺/NADH, NADP⁺/NADPH, oxidised and reduced glutathione, and oxidised and reduced thioredoxin. Each pool is finite, and every reaction that consumes electrons draws from the same pool that every reaction producing them fills. The ratio of reduced to oxidised carrier is therefore a single intensive quantity — comparable to a voltage — that couples all metabolism in the cell simultaneously. That ratio is what is meant by redox state. The two major couples are functionally divided: NAD⁺/NADH carries the flux of fuel oxidation, and NADP⁺/NADPH supplies biosynthesis and antioxidant defence. Both are regenerated from the same incoming carbon, and glucose entering the cell is committed either to glycolysis, which yields NADH and ATP, or to the pentose phosphate pathway, which yields NADPH. The two branches compete for one substrate.

Thiol cysteines are the sensing elements that read this quantity. A cysteine thiol is oxidised reversibly, switches over a narrow range rather than gradually, and sits in the active site of enzymes throughout glycolysis, the pentose phosphate pathway, and the electron transport chain, as well as in transcription factors. Redox is consequently both the substrate of cellular energetics and its signalling medium.

**The peroxiredoxin cycle.** In eukaryotes, **peroxiredoxin oxidation state** oscillates with a circadian period in human erythrocytes, which are anucleate and incapable of transcription. In *Ostreococcus tauri* held in constant darkness, transcription and translation are undetectable, yet on restoration of light the transcriptional rhythm resumes at the phase predicted by a continuously running oscillator rather than from a reset origin (O'Neill and Reddy, 2011; O'Neill et al., 2011). Peroxiredoxin rhythms are subsequently found across all three domains of life (Edgar et al., 2012).

Peroxiredoxin is the reporter of that rhythm rather than its mechanism. Typical 2-Cys peroxiredoxins function as head-to-tail dimers and reduce hydrogen peroxide. The peroxidatic cysteine attacks H₂O₂ and is oxidised to a sulfenic acid, Cys-SOH, which condenses with the resolving cysteine on the partner subunit to form an intersubunit disulfide; thioredoxin, thioredoxin reductase, and NADPH then return the enzyme to its starting state. Complete turnover takes seconds. When peroxide flux is high, the sulfenic acid is oxidised a second time before it can condense, producing a catalytically inactive sulfinic acid, Cys-SO₂H (Wood et al., 2003). This form is retrieved only by sulfiredoxin, in an ATP-dependent reduction that takes hours. Because inactivation is fast and retrieval is slow, the sulfinylated fraction integrates the cell's oxidative history over a window of hours, which is why it can be assayed as a marker of a rhythm whose components turn over in seconds.

**What cycles.** The oscillating quantity is the redox poise of those shared carrier pools, and with it the flux of carbon between the oxidative and reductive branches of metabolism. The cycle closes because oxidation triggers its own reversal.

Fuel oxidation drives electrons through the respiratory chain, a fraction of which leak to oxygen and generate superoxide and hydrogen peroxide. Removing that peroxide consumes NADPH through the peroxiredoxin and glutathione systems. As NADPH is drawn down, removal capacity falls while production continues, and peroxide concentration rises. Rising peroxide and falling thiol reduction are themselves the signal that reroutes metabolism: oxidation of the active-site cysteine of GAPDH inhibits glycolysis and diverts glucose into the pentose phosphate pathway (Ralser et al., 2007), oxidation of pyruvate kinase M2 at Cys358 does the same at the downstream commitment step (Anastasiou et al., 2011), and oxidation of KEAP1 releases NRF2 to transcribe the antioxidant and pentose phosphate enzymes. Each of these responses generates NADPH. Peroxiredoxin's own inactivation contributes to the switch: with the fast arm disabled, peroxide is permitted to rise to concentrations at which it acts as a signal rather than being consumed as waste (Wood et al., 2003). Reductant supply is then restored, sulfiredoxin slowly retrieves the sulfinylated enzyme, peroxide removal capacity returns, and because the recovery response was induced in excess the pool overshoots into a reduced state, in which fuel oxidation resumes and the cycle begins again.

The three requirements of an oscillator are met by that circuit. Negative feedback: oxidation induces the machinery that reduces. Delay: sulfiredoxin retrieval takes hours, NRF2-driven transcription takes hours, and pentose phosphate flux must be rerouted before NADPH can recover. Nonlinearity: thiol switches and the hyperoxidation branch engage over narrow thresholds rather than proportionally. The oscillator is the metabolic network as a whole rather than any single protein within it, and no minimal component set for the eukaryotic version has been reconstituted in the way the Kai system has. Other quantities oscillate with the same period and are part of the same circuit: glycolytic and pentose phosphate flux, haemoglobin autoxidation in erythrocytes, transmembrane ion transport, and cytosolic magnesium, which gates the availability of ATP in its physiologically active Mg-ATP form and is conserved from algae to human cells (Feeney et al., 2016).

**Why redox carries the clock.** The daily cycle a cell must anticipate is itself an oxidative cycle. In a photosynthetic ancestor, dawn switches on the photosystems and floods the cell with electrons and with the reactive oxygen species that escape them, so peroxide production is intrinsically diurnal. An oscillator built from redox chemistry is therefore constructed out of the same perturbation it exists to track, and it schedules oxygen-sensitive chemistry away from peak photo-oxidative load — in cyanobacteria, confining nitrogen fixation, whose nitrogenase is destroyed by oxygen, to the dark phase, and in eukaryotes displacing DNA replication from the hours of maximum oxidative flux. Peroxiredoxins are among the most conserved proteins known, and their rhythm appears in bacteria, archaea, and eukaryotes alike, consistent with a timing system that dates to the rise of atmospheric oxygen (Edgar et al., 2012).

### 2.6 Coupling of the redox and transcriptional oscillators

The two systems are reciprocally connected rather than arranged as master and slave.

Redox state acts directly on the transcriptional loop at the level of DNA binding. The reduced cofactors NADH and NADPH enhance binding of CLOCK:BMAL1 and NPAS2:BMAL1 heterodimers to E-box elements, while the oxidised forms inhibit it (Rutter et al., 2001). The ratio of reduced to oxidised nicotinamide cofactors — a direct readout of metabolic flux — therefore gates transcriptional output with no intervening signalling cascade. NAD⁺ availability, set by the clock-controlled salvage enzyme NAMPT, drives SIRT1-mediated deacetylation of BMAL1 and PER2, closing a second metabolic feedback onto the loop (Nakahata et al., 2009; Ramsey et al., 2009).

The dependency runs in both directions. Peroxiredoxin and redox rhythms persist in cells lacking BMAL1 or both cryptochromes, but with reduced amplitude and reduced robustness; transcriptional rhythms in turn degrade when the redox environment is perturbed.

Circadian organisation is therefore layered: a redox-based oscillator of great evolutionary antiquity, running on the chemistry of fuel oxidation and requiring no genome, overlaid by a transcriptional loop that provides amplification, tissue-specific outputs, and the interface through which photic input entrains the whole system.

Kruse (2013) treats this architecture as foundational rather than peripheral. If timekeeping precedes and outlasts gene expression, then the genome cannot be the timekeeper; genes amplify and stabilise a timing signal that originates elsewhere. On this account circadian control is imposed by the physical environment on cellular redox state, and transcriptional machinery is downstream of, and subordinate to, that imposed rhythm. Kruse (2023) restates the principle in general form: environmental electromagnetic input determines gene expression rather than the reverse, and disorders arising from disrupted timing will therefore present without any alteration to DNA sequence.

### 2.7 The oscillating variable

No single quantity constitutes the clock. In a single cell the oscillator traverses a closed trajectory — a limit cycle — through a state space whose axes are the concentrations, modification states, and localisations of its components. What oscillates is that state vector. Phase is position along the trajectory, and every measurable marker is a projection of the trajectory onto one axis, which is why phase is always reported relative to a named reference such as dim light melatonin onset or the core body temperature minimum rather than in absolute terms.

The measurable variables differ by level of organisation.

**Within a cell**, the oscillating quantities are the abundance of *Per* and *Cry* transcripts, the cytoplasmic and nuclear concentrations of their protein products, the phosphorylation state of PER, the occupancy of CLOCK:BMAL1 at E-box elements, and the redox poise of the shared carrier pools. In cultured cells these are followed continuously as bioluminescence from a PER2::LUCIFERASE fusion, which reports one protein's abundance as a proxy for the whole trajectory.

**Within a tissue**, the oscillating quantity is the fraction of the transcriptome under rhythmic control, together with the rhythmic proteome and metabolome that follow from it. In any single organ roughly five to fifteen per cent of expressed transcripts cycle. Across twelve mouse organs, 43 per cent of all protein-coding genes are rhythmic in at least one tissue, but the rhythmic sets are largely non-overlapping between organs: apart from the core clock genes themselves, each tissue cycles a different set (Zhang et al., 2014). The same timing mechanism therefore controls almost entirely different output programs in liver, adipose, and muscle. Rhythms in protein and metabolite abundance are only partly predicted by transcript rhythms, a large fraction arising post-transcriptionally.

**Within an organism**, the oscillating quantities are plasma hormone concentrations, core body temperature, blood pressure, sleep propensity, cognitive throughput, and the rates of secretion, absorption, and excretion.

Rhythmic transcripts within an organ do not all peak together. They cluster into successive waves across the day, each wave corresponding to a coordinated block of the tissue's function.

---

## 3. The central pacemaker

### 3.1 The suprachiasmatic nucleus

The **suprachiasmatic nucleus (SCN)** is a paired hypothalamic structure of approximately 20,000 neurons situated immediately dorsal to the optic chiasm.

Its status as master pacemaker rests on three lines of evidence: ablation abolishes behavioural rhythmicity; transplantation of SCN tissue into an arrhythmic host restores rhythmicity with the *donor's* period (Ralph et al., 1990); and isolated SCN tissue sustains oscillation in culture indefinitely.

### 3.2 Network organisation

Individual SCN neurons are imprecise oscillators with dispersed periods. Precision is a property of the coupled network rather than of its elements.

The **core**, ventrolateral and retinorecipient, expresses vasoactive intestinal peptide (VIP) and gastrin-releasing peptide. The **shell**, dorsomedial, expresses arginine vasopressin (AVP).

VIP signalling through the **VPAC2** receptor is required for network synchrony. Deletion of VIP or VPAC2 renders the animal behaviourally arrhythmic, not by silencing individual oscillators but by desynchronising them.

Intercellular coupling confers resistance to perturbation. The SCN shifts slowly in response to abrupt changes in the light–dark cycle, which accounts for the multi-day time course of re-entrainment after transmeridian travel.

### 3.3 Output pathways

The SCN distributes timing information through autonomic outflow, through humoral signals — principally glucocorticoids — and through the daily body temperature rhythm. The multi-synaptic pathway to the pineal runs SCN → paraventricular nucleus → intermediolateral cell column → superior cervical ganglion → pineal.

---

## 4. Photic input

### 4.1 The non-image-forming pathway

Photic entrainment is mediated by a photoreceptive system anatomically and functionally distinct from the image-forming system.

**Intrinsically photosensitive retinal ganglion cells (ipRGCs)** constitute approximately 1–2% of retinal ganglion cells and express the photopigment **melanopsin (OPN4)**. They depolarise to light directly, in the absence of rod and cone input (Berson, Dunn and Takao, 2002).

Their properties are those of an irradiance detector rather than an image detector: peak spectral sensitivity near **480 nm**, slow kinetics, sustained response, high threshold, and integration over minutes. Phototransduction proceeds through Gq/11 → PLCβ4 → TRPC6/7.

ipRGC axons form the **retinohypothalamic tract**, projecting to the SCN and additionally to the olivary pretectal nucleus, intergeniculate leaflet, habenula, and ventrolateral preoptic nucleus.

Rods and cones contribute to entrainment through convergence onto ipRGCs, particularly at low irradiance; complete abolition of entrainment requires elimination of all three photoreceptor classes (Hattar et al., 2003). The ipRGC constitutes the final common path.

Clinically, individuals blind from outer retinal disease but retaining intact ipRGCs entrain normally despite absent visual perception. Individuals lacking all light perception free-run with τ slightly exceeding 24 hours, producing **non-24-hour sleep–wake disorder**, in which sleep timing drifts progressively later and cycles in and out of alignment over weeks.

### 4.2 The retina as a timing organ

Kruse (2015) makes the functional separation between the two retinal systems the organising principle of the entire framework: the eye is a clock before it is a camera, and its timing function is hierarchically superior to its imaging function. Under this framing the inner retina constitutes the top of a control hierarchy governing every downstream oscillator, and pathology of the eye — cataract formation, glaucoma, myopia — is read as early evidence of failure in the organism's central timing apparatus rather than as isolated ocular disease. Kruse (2015) accordingly treats ophthalmic findings as sentinel signs that precede systemic metabolic and neoplastic disease.

The clinical corollaries Kruse (2016) draws from this position govern much of the protocol: light must reach the retina unfiltered, since spectacles, contact lenses, sunglasses, windscreens, and window glass each remove portions of the spectrum that the non-image-forming system requires; and exposure must occur at the times when the required frequencies are present in terrestrial sunlight.

### 4.3 Chromophore stability

Melanopsin binds the chromophore **retinal** through a Schiff base linkage. This linkage is comparatively susceptible to spontaneous cleavage in mammals, and is particularly unstable in human melanopsin.

Kruse (2018) builds a mechanism of photoreceptor injury on this instability. Excess short-wavelength exposure, particularly in the absence of the balancing red and infrared frequencies present in natural light, liberates retinal from its protein. Free retinal is a reactive aldehyde and an efficient photosensitiser, and in the free state damages chromophores throughout the photoreceptive apparatus. Damaged chromophores no longer absorb light at their design frequencies, degrading the optical signalling on which timing depends. Kruse (2018) identifies this as the proximate lesion underlying the blue light hazard, and holds that the resulting loss of signal fidelity, not photothermal injury, is what makes chronic artificial light exposure pathogenic.

### 4.4 Additional opsins

**OPN5 (neuropsin)** is sensitive to ultraviolet and violet light and photoentrains local oscillators in the retina and cornea independently of melanopsin (Buhr et al., 2015).

Kruse (2016) assigns neuropsin a central role in tissue regeneration, proposing that UVA acting through corneal and cutaneous neuropsin initiates the melatonin-dependent programme by which mitochondrial populations are renewed and the proportion of defective mitochondrial genomes — **heteroplasmy** — is reduced. On this account the daily UVA signal is not merely a timing cue but the trigger for a repair cycle, and its chronic absence permits heteroplasmy to accumulate, which Kruse (2016) treats as the principal substrate of ageing and degenerative disease.

Opsins are expressed outside the eye. **OPN4** and **OPN3** are present in skin, and **OPN3** in adipocytes, where light exposure modulates lipolysis. Kruse (2012) predicted extra-ocular photoreception in skin and subsequently in subcutaneous adipose tissue on the grounds that the cold and light protocols produced systemic effects too rapid and too large to be mediated through the eye alone.

### 4.5 Membrane substrate

Docosahexaenoic acid (DHA) is concentrated in photoreceptor outer segments and synaptic membranes to a degree unmatched elsewhere in the body, and constitutes approximately half of central nervous system polyunsaturated fatty acid. Retinal DHA content exceeds that of brain. Despite the availability of docosapentaenoic acid, which differs by a single double bond and is both cheaper to synthesise and less susceptible to peroxidation, DHA has not been substituted at these positions across approximately 600 million years of eukaryotic evolution.

DHA-rich phospholipids provide the membrane environment permitting G-protein-coupled photoreceptive events. Photoreceptor discs contain phospholipids bearing ω-3 chains at both SN-1 and SN-2 positions; these species constitute approximately 52% of phosphatidylserine and 31% of phosphatidylcholine in the disc membrane. The DHA-derived docosanoid **neuroprotectin D1** upregulates Bcl-2 and Bcl-xL and downregulates Bax and Bad, generating a pro-survival transcriptional state in the retinal pigment epithelium.

Kruse (2015) treats DHA concentration as the gain control of the circadian system. Because melanopsin is a G-protein-coupled photopigment dependent on its lipid environment, and because DHA is subject to photo-oxidative destruction by short-wavelength light, tissue DHA status sets the fidelity with which light is transduced into a timing signal. Kruse (2015) accordingly holds that dietary DHA sufficiency is a prerequisite for circadian function rather than a general nutritional recommendation, and that DHA loss and light injury are mutually reinforcing.

### 4.6 Irradiance and spectral composition

The magnitude of the entraining signal depends on irradiance, spectral composition, duration, and timing.

| Environment | Approximate illuminance |
|---|---|
| Direct sunlight | 30,000–100,000 lux |
| Overcast daylight, outdoors | 1,000–10,000 lux |
| Well-lit interior | 300–500 lux |
| Domestic interior, evening | 50–200 lux |
| Threshold for melatonin suppression | approximately 30–100 lux |

Indoor daytime illuminance is one to two orders of magnitude below that required for robust entrainment, while evening indoor illuminance is sufficient to suppress melatonin. The modern light environment is therefore characterised by insufficient daytime signal and excessive nighttime signal, compressing the day–night contrast on which oscillator amplitude depends.

Spectral composition varies systematically through the solar day. At sunrise and sunset the solar disc is viewed through maximal atmospheric path length, and the spectrum reaching the eye is dominated by red and near-infrared frequencies with minimal ultraviolet. Ultraviolet A appears as solar elevation increases; ultraviolet B becomes available only above a solar elevation of approximately 30 degrees, and therefore only during the hours surrounding solar noon, and at higher latitudes only during part of the year.

Kruse (2016, 2022) organises the protocol around this sequence. The ordered daily progression from infrared and red, through ultraviolet A, to ultraviolet B constitutes the signal the system evolved to read, and the sequence carries information that no single component reproduces. Viewing the sunrise establishes the phase reference; subsequent exposure as ultraviolet becomes available supplies the frequencies required for the photochemical steps described in section 10. Kruse (2022) specifies exposure beginning at sunrise and continuing as ultraviolet becomes available, using ultraviolet index 1 as the practical threshold for UVA availability.

Ordinary window glass transmits visible light while removing essentially all ultraviolet B, the majority of ultraviolet A, and a substantial fraction of infrared A. Kruse (2019) treats indoor daytime occupancy as spectral truncation rather than merely reduced intensity: the light reaching the retina indoors is not a weaker version of sunlight but a different signal, retaining the short-wavelength component that suppresses melatonin while omitting the components that drive the compensating photochemistry.

---

## 5. Peripheral oscillators and internal synchrony

### 5.1 Distribution

Essentially every nucleated cell contains a functional transcription–translation feedback loop. Liver, gut, pancreas, adipose tissue, skeletal muscle, kidney, skin, and immune cells all oscillate autonomously in culture.

The SCN does not generate rhythmicity in these tissues; it synchronises oscillators that would otherwise drift apart at their individual periods.

```
                    ┌─────────────┐
                    │     SCN     │  ← receives light directly
                    │  (central)  │     most phase-stable oscillator
                    └──────┬──────┘
                           │  neural + endocrine output
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
     ┌──────────┐   ┌──────────┐   ┌──────────┐
     │  Liver   │   │   Gut    │   │  Muscle  │  ← peripheral: entrained by
     │  clock   │   │  clock   │   │  clock   │    SCN output + local cues
     └──────────┘   └──────────┘   └──────────┘
           │               │               │
           └───────────────┼───────────────┘
                           ▼
                 desynchronise when cues conflict
```

### 5.2 Peripheral zeitgebers

**Feeding time** is the dominant zeitgeber for hepatic and gastrointestinal oscillators. Restricted feeding at a phase opposed to the light–dark cycle uncouples the liver clock from the SCN entirely, shifting hepatic gene expression within days while the SCN, entrained by light, remains in place (Damiola et al., 2000; Stokkan et al., 2001). In humans, delaying meals by five hours delays adipose tissue clock gene rhythms without shifting central phase markers (Wehrens et al., 2017).

**Temperature.** The SCN-driven body temperature rhythm entrains peripheral oscillators. Peripheral clocks are resettable by temperature while the SCN itself is not, preventing the master oscillator from being reset by its own output (Buhr, Yoo and Takahashi, 2010).

**Glucocorticoids** act as a systemic synchronising signal to peripheral tissues.

**The retina** is exceptional among peripheral tissues in entraining directly to light and maintaining autonomous rhythmicity while supplying the central signal.

### 5.2a Hierarchy and override

```
    LIGHT (dominant zeitgeber)
         │
         ▼
    SCN (phase authority, not execution engine)
         │
         ├───────────────────┬────────────────────┐
         ▼                   ▼                    ▼
    Melatonin           Cortisol            Temperature
         │                   │                    │
         └───────────────────┴────────────────────┘
                             │
                             ▼
              Peripheral clocks (liver, gut, muscle, adipose)
                             ▲
         ┌───────────────────┼────────────────────┐
         │                   │                    │
     Feeding             Activity           Local signals
  (overrides liver)     (moderate)      (can oppose SCN)
```

**Override rules.** Light overrides melatonin. Feeding overrides the liver clock. No single signal overrides everything downstream of it. Chronic conflict between signals produces desynchrony rather than a winner.

> **Key.** When cues conflict chronically — bright light at night with daytime feeding — subsystems drift apart. The clocks still run. They disagree.

---

## 6. Determinants of individual response

**Chronotype.** The distribution of preferred timing is continuous and substantially heritable, with τ, PRC amplitude, and light sensitivity all varying between individuals.

**Genotype.** PER2 and CK1δ variants produce advanced phase; CRY1 variants produce delayed phase; MTNR1B genotype modifies the glucose response to eating during the melatonin window.

**Age.** Amplitude declines and phase advances with age. Lens yellowing reduces transmission of short wavelengths, diminishing the entraining signal reaching ipRGCs; this is one contributor to circadian fragmentation in older adults.

**Skin pigmentation and latitude.** Constitutive melanin density determines the ultraviolet dose required for equivalent cutaneous photochemistry, and therefore the exposure appropriate at a given latitude and season.

**Light history.** Sensitivity to evening light is modulated by preceding daytime exposure; individuals with high daytime light exposure show reduced melatonin suppression by a given evening stimulus.

Kruse (2015, 2022) treats latitude, season, and pigmentation as jointly determining the appropriate exposure, and holds that dietary composition should correspond to the photoperiod and latitude in which it is consumed, on the grounds that carbohydrate availability historically covaried with long photoperiod and that the two signals are read together.

---

## 7. Biophysical constraints

### 7.1 The clock is an integrator of photon flux

Rods and cones adapt within milliseconds and report contrast. Melanopsin-expressing ipRGCs depolarise slowly, sustain their response for the duration of the stimulus, and decay slowly after it ends. The cell integrates photon capture over minutes to tens of minutes, which makes it an irradiance detector rather than a contrast detector, and makes cumulative dose rather than peak brightness the quantity the clock receives.

Melanopsin is also photo-regenerating. The pigment interconverts between resting and signalling states under illumination, long wavelengths driving the signalling state back toward rest while short wavelengths drive it forward, so the pigment sustains its own chromophore supply independently of the retinal pigment epithelium (Emanuel and Do, 2015). The consequence for exposure design is that the ratio of short to long wavelengths determines the steady-state fraction of pigment available for signalling, and two spectra with identical melanopic weighting can therefore drive the pathway differently. A blue-enriched, red-depleted source and a broadband source of the same melanopic irradiance are not equivalent stimuli.

### 7.2 The irradiance–response relation is compressive

Phase shift magnitude and melatonin suppression follow a saturating function of the logarithm of irradiance. Half-maximal melatonin suppression occurs at illuminances on the order of a hundred lux, well below ordinary interior lighting, and the curve is steepest at the low end of its range.

The practical consequences run in both directions. At night, the first increment of light above darkness carries most of the biological effect, so the difference between complete darkness and dim light exceeds the difference between dim light and bright light. During the day, returns diminish above the saturating range, so additional illuminance beyond a threshold adds little.

Intensity and duration are not fully interchangeable. Sequences of brief bright pulses produce phase shifts approaching those of continuous exposure of the same total duration, because the pathway responds to the onset of illumination more strongly than to its maintenance (Gronfier et al., 2004).

### 7.3 Dynamic range is the operative quantity

The signal the circadian system extracts from the environment is the contrast between day and night rather than the absolute level of either. Outdoor illuminance spans approximately eight orders of magnitude across the natural day, from above 100,000 lux in direct sun to below 0.001 lux under an overcast moonless sky. A modern interior spans less than two, from a few hundred lux during the day to tens of lux in the evening.

Amplitude loss and phase instability follow from compression of that range, and the compression is bilateral: the daytime signal is reduced by three orders of magnitude while the night signal is raised by four. Either alone reduces the contrast; together they reduce it to a fraction of the natural value. Measurement and intervention are therefore directed at the ratio rather than at either level in isolation.

### 7.4 Precision is a property of the network, not the cell

Isolated SCN neurons keep time poorly, with period varying by hours between cells and drifting within cells. The intact nucleus keeps time to within minutes. The improvement arises from coupling: neurons synchronise through VIP and GABA signalling, and the ensemble averages the noise of its members.

Coupling strength governs a trade-off. A strongly coupled network is precise and resists perturbation, which is why the SCN shifts slowly after a change in the light schedule and why it is not reset by the temperature rhythm it generates. Weakly coupled peripheral networks shift quickly and are reset by temperature and feeding. The hierarchy between central and peripheral oscillators is a consequence of differing coupling strength rather than of any difference in the underlying molecular mechanism.

### 7.5 Amplitude and phase are coupled through the geometry of the limit cycle

An oscillator's state is a point moving on a closed orbit. A perturbation displaces that point by a fixed vector, and the resulting change in phase depends on the radius of the orbit: the same displacement applied to a small orbit rotates the state through a large angle, and applied to a large orbit rotates it through a small one.

Phase lability is therefore inversely related to amplitude. A flattened rhythm is not merely a weak one; it is one that any given zeitgeber, or any given disturbance, will displace further. This is the mechanism by which amplitude loss precedes and predisposes to phase instability, and it implies that amplitude must be restored before phase can be reliably corrected.

The limit is a stimulus strong enough, delivered near enough to the critical phase, to drive the state to the centre of the orbit, where amplitude is zero and phase is undefined. Bright light applied near the core temperature minimum reduces the amplitude of the subsequent melatonin rhythm rather than shifting it, and can suppress it to near zero (Jewett, Kronauer and Czeisler, 1991). Light at the wrong phase does not only mistime the oscillator; at sufficient intensity it degrades it.

### 7.6 Entrainment has a bounded range that widens with zeitgeber strength

An oscillator entrains to a driving cycle only when the mismatch between its intrinsic period and the driving period is small enough relative to the strength of the coupling. The set of period and strength combinations that permit entrainment forms a wedge that narrows to a point as coupling weakens.

Two consequences follow. The range of intrinsic periods that can be entrained contracts under a weak zeitgeber, so individuals with periods far from 24 hours fail to entrain under dim indoor conditions and entrain normally outdoors. And the phase angle at which entrainment settles is a function of both intrinsic period and zeitgeber strength: a long intrinsic period under a weak zeitgeber entrains at a delayed phase angle. Late chronotype under indoor conditions is the expected output of that relation rather than an independent trait, which is why a week of natural light exposure advances phase and compresses the spread between chronotypes (Wright et al., 2013).

### 7.7 Anticipation is the function that justifies the cost

Feedback control corrects an error after it occurs. Feedforward control acts before the disturbance arrives, and for a disturbance that is predictable it achieves lower error at lower cost. The daily light–dark cycle is the most predictable disturbance an organism experiences, and a clock converts the response to it from feedback to feedforward: enzymes are positioned before the substrate load arrives, and protective systems before the insult.

The advantage is measurable. Cyanobacterial strains whose intrinsic period matches the imposed light cycle outcompete strains whose period does not, and the advantage disappears in constant light (Ouyang et al., 1998). Plants whose clock period matches the environmental cycle accumulate more carbon and survive better (Dodd et al., 2005). Circadian organisation is maintained by selection because prediction is cheaper than reaction.

### 7.8 Tissue optics constrain where light can act

Absorption and scattering in tissue vary strongly with wavelength. Between approximately 650 and 1350 nm, haemoglobin absorption has fallen and water absorption has not yet risen, producing an optical window in which penetration is greatest. Blue light is attenuated within a fraction of a millimetre of the skin surface; red penetrates several millimetres; near infrared penetrates centimetres.

Extraocular photoreception is therefore constrained by wavelength. Short-wavelength effects are restricted to the eye and to superficial skin, where opsins are in fact expressed: OPN5 mediates local light entrainment of peripheral tissues, and OPN3 in adipocytes supports light-dependent regulation of lipolysis and thermogenesis (Buhr et al., 2015; Nayak et al., 2020). Long-wavelength effects can reach deep tissue, and the principal deep chromophore is cytochrome c oxidase, whose absorption bands near 660 and 810 nm underlie measurable increases in complex IV activity under red and near-infrared illumination.

Kruse (2012) states the prediction that photoreception is not confined to the eye and that skin and subcutaneous tissue respond directly to light; the opsin findings above establish the general claim, with the wavelength constraint above setting its limits.

### 7.9 Electron transfer, membrane potential, and the origin of the redox signal

Respiratory electron transfer proceeds by quantum tunnelling between redox centres, at rates that fall exponentially with distance and become negligible beyond approximately 14 Å. The spacing of centres within and between respiratory complexes is held below that limit, which makes the arrangement of the chain a physical constraint rather than a matter of convenience, and makes supercomplex organisation and cristae geometry determinants of transfer efficiency.

Superoxide production at complex I rises steeply with the mitochondrial membrane potential, particularly under reverse electron transport when the potential is high and the ubiquinone pool is reduced. Oxidant load is therefore a function of the thermodynamic state of the membrane rather than a fixed leak fraction, and the redox oscillation of section 2.5 is driven by a quantity that responds within minutes to substrate supply and demand.

Inner membrane lipid composition modulates both. Cardiolipin is required for supercomplex assembly and for the activity of several complexes, and the degree of unsaturation of membrane fatty acids alters proton permeability and the packing environment of the respiratory chain. Kruse (2015) builds on this in treating docosahexaenoic acid as a determinant of the gain of light-driven signalling, on the ground that the highly unsaturated membranes of retina and neural tissue are the ones in which photic signal transduction occurs.

### 7.10 Cryptochrome and the magnetic sense

Cryptochrome is both a core clock repressor and the leading candidate magnetoreceptor. On the radical pair mechanism, photoexcitation of the flavin cofactor generates a spin-correlated radical pair with a tryptophan residue, and the singlet–triplet interconversion of that pair is sensitive to magnetic fields far weaker than thermal energy, because the effect operates on spin coherence rather than on energy. Reaction yields therefore depend on the orientation and strength of the ambient field.

The mechanism is established for migratory orientation in birds and for magnetic responses in insects, where magnetic effects on circadian behaviour are cryptochrome-dependent. Comparable effects in humans are not established, and the field strengths at which the mechanism operates are geomagnetic and static, on the order of tens of microtesla, rather than the radiofrequency fields to which the mechanism is often extended.

---

## 8. Cancer


Circadian organisation separates incompatible processes in time. Cancer is, in part, a failure of that separation: when timing signals weaken or misalign, cells gain inappropriate freedom, and proliferation, metabolism, stress response, and immune evasion overlap in ways that favour malignant growth.

**Temporal segregation matrix.** These pairs are normally phase-separated. Disruption permits overlap, and overlap raises error rates.

| Process | Normally separated from | Consequence of overlap |
|---|---|---|
| DNA replication | DNA repair | Replication across unrepaired lesions |
| Anabolism | Catabolism | Futile cycling; wasted ATP |
| Proliferation | Inflammation | Growth amid damage signalling |
| Feeding | Insulin sensitivity nadir | Glycaemic load at the least tolerant phase |
| Replication | Oxidative stress peak | Mutation during synthesis |

**Permissiveness cascade.**

```
Circadian disruption
    │
    ├─→ Temporal overlap ......... incompatible processes run concurrently
    ├─→ Loss of repair windows ... DNA repair mistimed; autophagy and mitophagy reduced
    ├─→ Immune mis-timing ........ reduced nocturnal coordination; chronic inflammatory tone
    ├─→ Metabolic permissiveness . glycolytic bias; loss of metabolic gating
    └─→ Architecture instability . rhythmic adhesion expression lost
            │
            ▼
    Genomic instability + dysregulated metabolism + chronic inflammation
            │
            ▼
    Initiation, growth, invasion, metastasis
```
### 8.1 Circadian gating of the cell cycle

The circadian and cell division cycles are coupled, and the coupling is directional: the circadian oscillator gates progression through the cell cycle rather than the reverse.

CLOCK:BMAL1 drives transcription of *Wee1*, whose product inhibits the CDK1–cyclin B complex and controls the G2/M transition. In regenerating mouse liver, mitosis is confined to a restricted window each day, and the confinement is abolished by clock disruption (Matsuo et al., 2003). PER proteins act on Cyclin D1, c-MYC, and p21, coupling G1 progression to circadian phase.

*Per2*-mutant mice show elevated spontaneous tumour incidence and a markedly increased rate of lymphoma after ionising radiation, together with deficient p53-mediated apoptosis (Fu et al., 2002). *Per1* and *Per2* behave as tumour suppressors in this setting, and *Bmal1* deletion produces a comparable phenotype in several tissues.

The functional consequence is that proliferating tissue restricts DNA synthesis and mitosis to defined windows. When gating is lost, replication proceeds at phases when the supporting processes — nucleotide supply, chromatin state, and repair capacity — are not positioned for it.

### 8.2 Rhythmic DNA repair

Nucleotide excision repair, the pathway that removes ultraviolet photoproducts and platinum adducts, oscillates across the day. Its rate-limiting factor XPA is under circadian control at both transcript and protein level, and excision rates in mouse tissue vary several-fold between peak and trough.

Genotoxic exposure therefore carries a mutational cost that depends on the phase at which it arrives. The same dose delivered at the repair trough produces a larger residual lesion burden than at the peak, which supplies a direct mechanism connecting mistimed exposure to mutation rate without invoking any change in the exposure itself.

### 8.3 Melatonin and tumour growth

Melatonin has direct oncostatic activity independent of its role as a phase marker. Signalling through MT1 suppresses tumour uptake of linoleic acid and its conversion to the mitogenic metabolite 13-HODE, and melatonin at physiological nocturnal concentrations inhibits growth in human breast cancer xenografts.

The experiment that establishes the relevance of the light environment is a perfusion design: blood collected from women during the biological night, when melatonin is high, suppresses xenograft growth, while blood collected from the same women after exposure to light at night, with melatonin suppressed, stimulates it (Blask et al., 2005). The tumour-relevant variable is the melatonin content of circulating blood, and the light environment sets it.

### 8.4 Clock disruption in tumours and by external schedule

Clock gene expression is damped, phase-shifted, or lost in many human tumours, and the degree of loss correlates with grade and with prognosis in several tumour types.

Imposed disruption accelerates growth. Repeated phase advances of the light–dark cycle, a rodent model of chronic jet lag, accelerate the growth of transplanted and spontaneous tumours, and SCN ablation produces the same effect. The acceleration occurs without any change in carcinogen exposure.

### 8.5 Chronotherapy

Tolerance and efficacy of cytotoxic agents vary severalfold with the time of administration in animal models, tracking the rhythms of the cell cycle, drug-metabolising enzymes, and repair capacity in the target and host tissues. Chronomodulated delivery of fluorouracil and oxaliplatin in colorectal cancer reduces toxicity relative to constant-rate infusion, with efficacy benefit that is sex-dependent and has not replicated uniformly.

The clinical result is mixed; the underlying observation, that the same dose has different effects at different circadian phases, is not in doubt and is the sharpest available demonstration that biological time is a treatment variable.

### 8.6 Cancer as a timing disorder

Kruse (2011) identifies the coupling of circadian and cell cycles as the mechanism linking disrupted timing to oncogenesis, and Kruse (2016, 2018) develops this into the position that malignancy is primarily a disorder of cellular timing and energy handling rather than of mutation alone, with mutation accumulating as a consequence of replication and repair proceeding at the wrong phase. On this account the light environment is an upstream carcinogenic variable acting through melatonin amplitude, repair timing, and cell cycle gating rather than through direct genotoxicity.

The three mechanisms above — gating loss, repair at the wrong phase, and melatonin suppression — are each independently established, and each connects an environmental timing variable to a determinant of tumour initiation or growth.

---

## 9. Evidence

Stratified by study type. Established findings are distinguished from extrapolation. References link to [PubMed](https://pubmed.ncbi.nlm.nih.gov/).

### 9.1 Epidemiological

**Shift work.** Chronic circadian disruption from long-term night work, irregular sleep–wake timing, or nocturnal light exposure is associated with increased cancer incidence and worse prognosis. IARC classified shift work involving circadian disruption as **Group 2A, probably carcinogenic to humans**, in 2007, on limited human and sufficient experimental evidence [[Straif 2007](https://pubmed.ncbi.nlm.nih.gov/19271347/)], and reinforced the classification in the 2020 monograph. Large cohorts report elevated breast cancer risk in long-term night-shift nurses [[Stevens 2011](https://pubmed.ncbi.nlm.nih.gov/20953253/)].

The human cancer evidence is genuinely mixed: several large subsequent cohorts, including the Million Women Study, found no association. The discrepancy is unresolved, and the exposure metric is the likely reason — years of night work records schedule, not the degree of internal desynchrony achieved. Working group guidance emphasises measuring circadian impact rather than hours worked [[IARC Working Group](https://pubmed.ncbi.nlm.nih.gov/20962033/)].

Metabolic and cardiovascular associations are more consistent than the oncological ones: meta-analyses report elevated type 2 diabetes, obesity, metabolic syndrome, myocardial infarction, and ischaemic stroke, with risk rising by duration of exposure.

**Light at night.** Totally blind women have lower breast cancer incidence than sighted women, and the reduction follows a gradient with degree of light perception rather than with blindness as a category. This is the observation least susceptible to the confounding that affects shift work studies, since the exposure differs without the accompanying differences in schedule, sleep, and occupation. Satellite-measured outdoor light at night correlates with breast and prostate cancer incidence across regions, with the association concentrated in the short-wavelength fraction where individual spectral exposure is measured. Bedroom light at night is associated with obesity, metabolic syndrome, and depressive symptoms in cohorts of older adults.

**Rest–activity rhythm and mortality.** Blunted or irregular rest–activity rhythms predict reduced survival. In NHANES, low relative amplitude was associated with all-cause, cardiovascular, and cancer mortality, outperforming most traditional predictors [[Xu 2022](https://pubmed.ncbi.nlm.nih.gov/36450759/)]. In cancer patients, wearable-measured disruption — low amplitude, low mesor, high fragmentation — predicted all-cause, cancer-specific, and cardiovascular mortality and outperformed traditional risk factors [[2024](https://pubmed.ncbi.nlm.nih.gov/40930750/)].

Regularity of sleep timing predicts all-cause mortality more strongly than sleep duration (Windred et al., 2024). Low relative amplitude is associated with mood disorder, lower wellbeing, and impaired cognition independently of sleep duration (Lyall et al., 2018). These metrics correspond to stability and amplitude rather than phase, and carry predictive weight that timing measures alone do not.

**Chronotype, social jetlag, and eating time.** Evening chronotype is associated with elevated all-cause mortality and with metabolic and psychiatric morbidity, substantially mediated by the mismatch between endogenous phase and imposed schedule rather than by lateness itself — the epidemiological expression of the phase angle criterion. Social jetlag is associated with adiposity, adverse lipid and inflammatory markers, and depressive symptoms. In a weight loss intervention, participants eating the principal meal later lost less weight on matched energy intake, with no difference in reported intake or activity (Garaulet et al., 2013).

### 9.2 Controlled human disruption

Experimental misalignment of behavioural and circadian time induces cancer-relevant molecular changes within days.

Night-shift schedules cause circadian dysregulation of DNA repair genes and elevated DNA damage in blood [[Cheung 2021](https://pubmed.ncbi.nlm.nih.gov/33638890/)]. Simulated night work misaligns the peripheral blood mononuclear cell transcriptome, damping rhythmic expression across immune and signalling pathways including natural killer cell, Jun/AP-1, and STAT programs [[Kervezee 2018](https://pubmed.ncbi.nlm.nih.gov/29735673/)].

Under forced misalignment on a 28-hour day with diet and sleep duration controlled, subjects showed reduced leptin, elevated glucose and insulin, elevated mean arterial pressure, and in three of eight a postprandial glucose response in the prediabetic range (Scheer et al., 2009). Combined sleep restriction and circadian disruption reduces insulin secretion and raises postprandial glucose (Buxton et al., 2012). The circadian system affects glucose tolerance independently of behaviour, postprandial glucose being approximately 17 per cent higher in the biological evening (Morris et al., 2015).

These designs isolate circadian phase from behaviour within subjects, which is what the observational literature cannot do.

### 9.3 Natural experiments

Transitions into daylight saving time are followed by a transient increase in myocardial infarction and traffic accidents, with a corresponding decrease at the autumn transition. The exposure is a one-hour schedule shift applied to an entire population simultaneously, with no accompanying change in behaviour, occupation, or health status.

Position within a time zone separates solar time from clock time across an otherwise similar population. Residents at the western edge experience later solar time for a given clock hour, sleep less, and show elevated rates of several cancers relative to residents at the eastern edge.

A week of camping under natural light without electric light advances melatonin onset by approximately two hours and compresses the distribution of phase across chronotypes; the effect reproduces in winter (Wright et al., 2013). This is the intervention arm corresponding to the observational findings.

### 9.4 Chronotherapy

Administering therapy at circadian-preferred phases changes tolerability and efficacy.

**Chemotherapy.** A randomised trial of chronomodulated versus constant-rate oxaliplatin, fluorouracil, and folinic acid in metastatic colorectal cancer found five-fold reduced severe mucosal toxicity and increased objective response, 51 per cent versus 29 per cent [[Lévi 1997](https://pubmed.ncbi.nlm.nih.gov/9291901/)]. Meta-analysis confirms reduced haematological toxicity with inconsistent survival benefit [[meta-analysis](https://pubmed.ncbi.nlm.nih.gov/37090313/)]. Benefit varies by chronotype, rhythm stability, drug class, sex, and tumour biology.

**Immunotherapy.** The LungTIME-C01 phase 3 randomised trial in 210 treatment-naive NSCLC patients assigned anti-PD-1 immunochemotherapy to early (before 15:00) or late (after 15:00) administration for the first four cycles. Early administration improved progression-free survival, 11.3 versus 5.7 months (HR 0.40), and overall survival, 28.0 versus 16.8 months (HR 0.42). Morning circulating CD8+ T cells rose in the early group and fell in the late group, and the activated-to-exhausted CD8+ ratio was higher with early dosing [[Huang 2026](https://www.nature.com/articles/s41591-025-04181-w)].

The clinical result across agents is mixed; the underlying observation, that the same dose has different effects at different circadian phases, is not in doubt and is the sharpest available demonstration that biological time is a treatment variable.

### 9.5 Animal models

**Environmental disruption.** Light at night induces circadian disruption that accelerates ageing and promotes tumorigenesis in rats [[Blask 2012](https://pubmed.ncbi.nlm.nih.gov/23237593/)]. Circadian disruption promotes tumour growth through anabolic host metabolism [[2017](https://pubmed.ncbi.nlm.nih.gov/28874144/)]. Chronic jet lag, dim light at night, and rotating light–dark schedules produce comparable effects, and SCN ablation reproduces them. The acceleration occurs with no change in carcinogen exposure.

**Genetic disruption.** *Per2*-mutant mice show elevated spontaneous tumour incidence and markedly increased lymphoma after ionising radiation, with deficient p53-mediated apoptosis [[Fu 2009](https://pubmed.ncbi.nlm.nih.gov/19805073/)]. BMAL1 disruption promotes metastasis through PAI-1–TGF-β–dependent mechanisms [[BMAL1](https://pubmed.ncbi.nlm.nih.gov/37330661/)]. Disruption-induced tumours show increased stemness, immunosuppression, and metabolic deregulation.

### 9.6 Reversibility

**Light structure and melatonin.** Restoring light–dark cycles and preserving nocturnal melatonin suppresses tumour growth and enhances chemosensitivity in preclinical models. Melatonin's efficacy depends on preserved circadian amplitude, and it enhances tumour sensitivity to chemotherapy and radiotherapy while protecting normal tissue [[review](https://pubmed.ncbi.nlm.nih.gov/37916636/)].

**Feeding–fasting structure.** Time-restricted feeding aligned to the active phase attenuates mammary tumour growth, reduces metastasis, and normalises hyperinsulinaemia in obesity-enhanced models [[TRF breast](https://pubmed.ncbi.nlm.nih.gov/34894935/)], and attenuates high-fat-diet-enhanced metastasis of Lewis lung carcinoma [[TRF lung](https://pubmed.ncbi.nlm.nih.gov/30952713/)]. Mechanisms include restored diurnal gene expression in tumours and improved insulin sensitivity.

**Exercise and pharmacology.** Exercise during the biological active phase improves outcomes combined with therapy. Small molecules stabilising or shifting core clock components reduce proliferation and reprogram metabolic and immune pathways experimentally.

That disruption accelerates tumour growth and restoration slows it, in the same models, is the strongest preclinical argument that the relationship is causal rather than associative.

### 9.7 Causal inference

Confounding in the human literature is severe. Shift workers differ from day workers in socioeconomic position, smoking, diet, sleep duration, and healthcare access, and evening chronotypes differ in most of the same respects. No single observational association carries much weight.

Four independent lines converge.

- **Controlled misalignment** isolates circadian phase from behaviour within subjects over days.
- **Mendelian randomisation**, using genetic variants that determine chronotype and are unrelated to lifestyle, finds genetically predicted morning preference protective against breast cancer (Richmond et al., 2019).
- **Natural experiments** alter the exposure without altering the person.
- **Animal reversibility** shows the effect in both directions under controlled carcinogen exposure.

> **Inference.** The case rests on convergence across these lines together with the mechanisms of section 8 — not on cohort associations, which are the weakest element of the evidence base and the most frequently cited.

---

---

# PART II — CIRCADIAN HEALTH

---

## 10. Outputs

### 10.1 Melatonin

Pineal melatonin is synthesised from serotonin, with **AANAT** as rate-limiting enzyme, under SCN control through the pathway described in 3.3. Secretion occurs only in darkness and is acutely suppressed by light. **Dim light melatonin onset** is the reference marker of circadian phase.

Melatonin functions as a signal of darkness rather than as a hypnotic, which accounts for its modest sedative effect and substantial phase-shifting effect. Low doses in the range 0.3–0.5 mg are as effective as higher doses for phase shifting, with fewer residual next-day effects.

### 10.2 Extrapineal and mitochondrial melatonin

Melatonin is synthesised well beyond the pineal: in the gastrointestinal tract in far greater total quantity than in the pineal, and in retina, skin, bone marrow, lymphocytes, thymus, gonads, and within mitochondria. Pinealectomy abolishes the circulating rhythm without eliminating tissue melatonin. Extrapineal melatonin is largely non-rhythmic and acts locally, functioning principally as an antioxidant.

Kruse (2022) makes mitochondrial melatonin central. Melatonin is both lipid- and water-soluble, distributes across all subcellular compartments, and acts as a direct free radical scavenger and indirect antioxidant, stimulating superoxide dismutase, glutathione peroxidase, glutathione reductase, and catalase. Kruse (2022) holds that its production is driven locally by near-infrared and ultraviolet A penetrating tissue, and that consequently melatonin status is a function of daytime light exposure rather than solely of nighttime darkness. On this account melatonin is the principal agent limiting mitochondrial heteroplasmy, and sleep quality serves as an index of mitochondrial competence rather than only as its cause.

Kruse (2022) further proposes the daily photochemical sequence: morning ultraviolet exposure supplies the energy for conversion of tryptophan toward serotonin, with neuropsin setting the rhythm; the accumulated serotonin pool is converted to melatonin in darkness. Under this model the quantity of melatonin available at night is determined by the ultraviolet exposure received that morning, and darkness alone is insufficient if the daytime signal was absent.

### 10.3 Melatonin and glucose regulation

MT1 and MT2 melatonin receptors are expressed on pancreatic beta cells, where melatonin inhibits insulin secretion. The **MTNR1B** locus, encoding MT2, is among the most consistently replicated type 2 diabetes risk loci in human genetics. Food consumed during the period of elevated circulating melatonin produces measurably impaired glucose tolerance, an effect modified by MTNR1B genotype.

Kruse (2016) treats melatonin and insulin as opposed metronomes carrying complementary information: insulin encodes the high-energy signal associated with long photoperiod and carbohydrate availability, melatonin encodes darkness and the suspension of feeding. Where light at night is present, the opposition collapses, and insulin secretion proceeds at a phase where melatonin should be suppressing it. Kruse (2016) therefore treats insulin resistance as a disorder of light exposure expressed through carbohydrate handling rather than a disorder of carbohydrate intake as such, and prohibits food intake after dark on this basis.

### 10.4 Cortisol

Cortisol rises steeply in the period preceding waking and peaks approximately 30–45 minutes after waking, declining across the day to a nadir near midnight. The cortisol awakening response is SCN-driven through the hypothalamic–pituitary–adrenal axis and functions as a synchronising signal to peripheral oscillators.

Kruse (2012) treats the morning cortisol peak as the terminal step of a sequence initiated by photic input, and the flattened or inverted diurnal cortisol profile as the earliest measurable sign of circadian mismatch, preceding overt metabolic disease.

### 10.5 Body temperature

Core body temperature oscillates with an amplitude of approximately 1°C, reaching its minimum 1–3 hours before habitual wake time. It serves both as a phase marker and, as described in 5.2, as a zeitgeber for peripheral oscillators.

### 10.6 Sleep–wake regulation

Sleep timing is determined by the interaction of two processes (Borbély). **Process S** is homeostatic sleep pressure, accumulating with time awake and dissipating during sleep, with adenosine as the principal candidate substrate. **Process C** is the circadian alertness signal, independent of prior sleep.

The circadian system actively promotes wakefulness during the biological evening, opposing accumulated sleep pressure, and promotes sleep in the early morning as pressure declines. Misalignment between the two processes, rather than abnormality in either alone, underlies most disorders of sleep initiation and maintenance.

### 10.7 Metabolic coupling

The clock and cellular metabolism are reciprocally coupled through nicotinamide adenine dinucleotide.

**NAD⁺** concentration oscillates. **NAMPT**, the rate-limiting enzyme of the NAD⁺ salvage pathway, is a clock-controlled gene. **SIRT1**, an NAD⁺-dependent deacetylase, deacetylates BMAL1 and PER2, acting back on the core loop. The clock therefore drives NAD⁺ availability, and NAD⁺ availability drives the clock.

Kruse (2015, 2019) places this loop at the centre of the relationship between light and metabolism, expressing it as the sequence: sunlight and fasting raise the NAD⁺/NADH ratio, NAD⁺ activates SIRT1, SIRT1 modulates BMAL1 and CLOCK, which drive NAMPT, which regenerates NAD⁺. Kruse (2019) holds that the entry point of this cycle is the light environment, that artificial light lowers NAD⁺ at complex I, and that the cycle therefore cannot be driven by dietary intervention when the light environment is deficient.

### 10.8 Energy balance and adiposity signalling

**Leptin** is secreted by adipose tissue in proportion to fat mass and acts on hypothalamic receptors, activating POMC/CART neurons and inhibiting NPY/AgRP neurons. Its action is asymmetric: falling leptin produces a powerful signal of energy deficit, while elevated leptin produces a comparatively weak signal of sufficiency. In obesity, circulating leptin is elevated without corresponding central effect — leptin resistance — attributed to impaired transport across the blood–brain barrier, to upregulation of the negative regulators SOCS3 and PTP1B, and to hypothalamic inflammation.

Leptin secretion is rhythmic, rising through the evening and peaking during the night. Sleep restriction lowers leptin and raises ghrelin.

Kruse (2011) treats sleep and energy balance as a single system rather than two interacting ones, on the grounds that arousal and feeding are governed by an overlapping hypothalamic population, and that leptin resistance therefore necessarily presents with disordered sleep. Kruse (2018) resolves the relationship between adiposity signalling and photoreception by proposing that leptin carries optical as well as energetic information from the skin surface to the hypothalamus, and that free retinal liberated by inappropriate light exposure damages leptin in subcutaneous tissue. On this account leptin resistance is a consequence of photoreceptive failure, and is corrected by repair of the light environment rather than by dietary restriction.

### 10.9 Cell cycle, repair, and immunity

Circadian gating of the **cell cycle** operates partly through PER2, with downstream effects on Cyclin D1, c-Myc, and Wee1. *Per2*-mutant animals show elevated tumour incidence. **DNA repair** capacity, including nucleotide excision repair, is rhythmic. **Immune function** is rhythmic: TLR9 expression and responsiveness oscillate, and both sepsis severity and vaccine response vary with time of administration.

Kruse (2011) identifies the coupling of circadian and cell cycles as the mechanism linking disrupted timing to oncogenesis, and Kruse (2016, 2018) develops this into the position that malignancy is fundamentally a disorder of timing: sustained failure of temporal control removes the constraint separating proliferation from repair, and the resulting genomic changes are consequences rather than causes.

---

## 11. The internal phase map

Correct circadian organisation is not synchrony. A healthy system is defined by a specific, reproducible set of phase offsets between its oscillators, and coincident peaking of all variables would represent the loss of temporal organisation rather than its perfection.

The requirement is chemical. Opposed metabolic processes must be separated in time because running them simultaneously is futile: glycolysis against gluconeogenesis, lipogenesis against β-oxidation, protein synthesis against autophagy, proliferation against DNA repair. A synthetic pathway and its degradative counterpart operating at once consume ATP and yield no net product. Circadian organisation exists to place such processes in sequence, and the sequence is expressed as a set of fixed phase relationships.

The stable offset between an oscillator and its zeitgeber is the **phase angle of entrainment**. Health is defined by the correctness and stability of these angles, not by their absence and not by absolute clock time.

The approximate human phase map under conventional entrainment, for a person sleeping from 23:00 to 07:00:

| Variable | Approximate phase |
|---|---|
| Melatonin onset (DLMO) | 21:00, about 2 h before sleep onset |
| Melatonin peak | 03:00–04:00 |
| Melatonin offset | shortly after waking |
| Core body temperature minimum | 05:00, about 2 h before waking |
| Core body temperature maximum | 17:00–19:00 |
| Cortisol nadir | around sleep onset |
| Cortisol rise begins | 03:00, during sleep |
| Cortisol peak (awakening response) | 30–45 min after waking |
| Growth hormone principal pulse | first slow-wave sleep episode, shortly after sleep onset |
| Prolactin peak | mid to late night |
| TSH peak | late evening to early night |
| Aldosterone and renin peak | late night to early morning |
| Insulin sensitivity maximum | morning, declining across the day |
| Blood pressure | dips 10–20% during sleep, surges on waking |
| Platelet aggregability and PAI-1 peak | 06:00–09:00 |
| Airway calibre minimum | 04:00 |
| Bone resorption markers peak | night |
| Gastric acid secretion peak | late evening |
| Alertness and cognitive throughput | bimodal, with a post-prandial trough and an evening peak preceding the melatonin rise |
| Epithelial proliferation | DNA synthesis and mitosis gated to separate restricted windows |

These offsets encode an anticipatory program. Cortisol rises hours before waking so that fuel is mobilised before it is required. The temperature minimum precedes waking and anchors the phase response curve, light before it delaying and light after it advancing. Melatonin marks the biological night and simultaneously suppresses insulin secretion, so that the metabolic consequence of a meal depends on whether melatonin is present when it is eaten. The antiphase relationship between melatonin and cortisol is the most visible instance of a general rule rather than a special case.

Healthy variation moves the whole map while preserving its internal structure. Chronotype displaces every marker earlier or later by up to several hours without altering the offsets between them. Seasonal photoperiod changes the width of the melatonin window rather than its relationship to sleep. Within the pacemaker itself, day length is encoded by the degree of phase dispersion among SCN neurons — longer days producing a wider spread of individual neuronal phases — so that phase relationships within the network carry the seasonal signal directly.

Pathology is the alteration of the offsets themselves.

---

## 12. Disruption

### 12.1 Failure modes

| Mode | Description | Typical cause |
|---|---|---|
| Acute phase shift | Internally coherent, misaligned to environment | Transmeridian travel |
| Chronic misalignment | Behaviour repeatedly opposed to internal time | Shift work |
| Internal desynchrony | Central and peripheral oscillators in conflict | Late eating, night work |
| Amplitude reduction | Correct phase, diminished oscillation | Low daytime light, light at night, ageing |
| Intrinsic phase disorder | Abnormality of the oscillator itself | DSPD, ASPD, non-24 |

Amplitude reduction is the most prevalent mode in populations occupying indoor environments, and produces no subjective sense of misalignment.

```
ALIGNED          SCN ═══ Periphery ═══ Behaviour        (one phase)
SOCIAL JETLAG    SCN ═══ Periphery ═══   ╳   Weekend    (weekday vs free-day mismatch)
SHIFT WORK       SCN ═══   ╳   Forced schedule          (light at the wrong time)
INTERNAL DESYNC  SCN ══╳══ Liver ══╳══ Gut              (organs disagree: feeding vs light)
AMPLITUDE LOSS   scn ─── periphery ─── behaviour        (offsets correct, excursions shrunk)
```

### 12.2 Experimental evidence

Under forced misalignment on a 28-hour day, with diet and sleep duration controlled, subjects showed reduced leptin, elevated glucose and insulin, elevated mean arterial pressure, and in three of eight cases a prediabetic glucose profile within ten days (Scheer et al., 2009).

Combined sleep restriction and circadian disruption reduces insulin secretion and raises postprandial glucose (Buxton et al., 2012).

Shift work involving circadian disruption is classified by IARC as Group 2A, probably carcinogenic to humans, with the strongest evidence for breast cancer.

Light at night in the sleeping environment is associated in observational cohorts with obesity, metabolic syndrome, and depressive symptoms.

### 12.3 Mechanisms of harm

**Loss of temporal segregation.** Circadian organisation separates incompatible processes — DNA replication from repair, anabolism from catabolism, inflammation from regeneration. Desynchrony permits their overlap.

**Signalling at inappropriate phase.** Nutrient intake during the melatonin window impairs glucose handling; glucocorticoid elevation at the wrong phase disrupts peripheral entrainment.

**Amplitude collapse.** Reduced oscillator amplitude propagates to every downstream rhythm, including the NAD⁺/SIRT1 cycle and the rhythm of DNA repair.

**Loss of anticipation.** The adaptive function of a circadian clock is preparation in advance of predictable events. A disrupted clock responds rather than anticipates.

Kruse (2015, 2018) adds a fifth mechanism at the level of signal acquisition: chronic exposure to short-wavelength light without balancing red and infrared frequencies degrades the photoreceptive apparatus itself, through the chromophore mechanism of 4.3 and through photo-oxidative loss of membrane DHA. Under this account the system loses not only correct timing but the capacity to acquire timing information, and correction requires restoration of the input signal before any downstream intervention can take effect.

### 12.4 Internal desynchrony

Because central and peripheral oscillators respond to different zeitgebers, they can be driven into conflict. Light-entrained central timing combined with food-entrained peripheral timing at an opposed phase produces **internal desynchrony**: each oscillator is internally coherent, but the organism is not.

Decoupling is a measured relationship, not a metaphor. The phase of a peripheral oscillator is read as the time of peak clock-gene expression in that tissue, or as the peak of bioluminescence from an explant carrying a PER2::LUCIFERASE reporter. That phase is then expressed as an offset from a central phase marker, for which melatonin onset is used because it is a clean readout of SCN phase — not because melatonin drives the peripheral tissue. Decoupling means that this offset has changed: the liver now reaches its transcriptional peak at a different interval before or after DLMO than it previously did, while the SCN itself has not moved.

Restricted feeding at a phase opposed to the light–dark cycle inverts the phase of clock gene expression in liver, kidney, pancreas, and heart by approximately twelve hours within a few days, while the SCN remains locked to the light–dark cycle (Damiola et al., 2000; Stokkan et al., 2001). In humans, delaying meal times by five hours delays the plasma glucose rhythm by about five hours and delays *PER2* expression in adipose tissue, while melatonin and cortisol rhythms remain in place (Wehrens et al., 2017). The central marker holds, the peripheral tissue moves, and the offset between them is what has been damaged.

Amplitude reduction is distinct from this. It preserves the offsets while shrinking every excursion, so the phase map remains correct in shape and loses its depth. The two failures compound: a flattened rhythm is also more easily displaced, because a weak oscillator is more readily reset by a competing zeitgeber.

Internal desynchrony is the mechanism by which behaviour that is individually unremarkable — eating late, working at night, sleeping in daylight — produces physiological harm.

Kruse (2012, 2024) resolves the relationship between light and feeding by subordinating meal timing to the light cycle: food is to be consumed within the interval when light is present, with the largest meal taken shortly after sunrise and intake tapering across the day, and terminated some hours before sleep. Kruse (2019) proposes further that metabolic interventions dependent on circadian timing — fasting, time-restricted feeding, and cold exposure — are conditional on an intact light environment, and will fail to produce their expected effects when performed under artificial light or in the presence of light at night.

---

## 13. Defining circadian health

Circadian health is not a scalar. The system fails in at least five ways that are mechanistically distinct, independently caused, and independently reversible. A person may be correctly phased and flat; strongly rhythmic and misaligned; internally coherent on average and unstable across days. Any definition that collapses to one number will classify at least one of these states incorrectly.

The definition below therefore takes the form of a profile with five components. Each component has a stated failure mode, a marker that reports it, and a criterion for the healthy range.

A sixth quantity — the strength and timing of the environmental input — is not a component of health but its cause. It is measured separately because an intact output profile sustained under an inadequate input profile identifies a person with reserve who is being depleted, and that state requires intervention while every output marker still reads as normal.

The definition takes the form of a profile with five components. Each has a stated failure mode, a marker that reports it, and a criterion for the healthy range.

### 13.1 Entrainment

**Definition.** The oscillator runs with a period of exactly 24 hours and holds a fixed relationship to the solar day across weeks.

**Failure.** The intrinsic period is expressed rather than corrected, and phase drifts progressively. In sighted people this is rare; in the totally blind, non-24-hour sleep–wake disorder is common. Partial failure appears as a phase that wanders by more than an hour week to week.

**Why it is first.** Entrainment is a precondition. If phase is drifting, every other measurement describes a moving target, and single-session markers become uninterpretable.

### 13.2 Phase

**Definition.** Two separate quantities, both required.

*External phase* is the position of the internal clock relative to the solar day — where DLMO falls in local solar time.

Both quantities are joint outputs of intrinsic period and zeitgeber strength rather than fixed traits. An oscillator entrains only when the mismatch between its intrinsic period and 24 hours is small relative to the coupling strength, and the phase angle at which it settles is a function of both. A long intrinsic period under a weak zeitgeber entrains at a delayed phase angle, and may fail to entrain at all. Late phase measured under indoor conditions is therefore not by itself evidence of an intrinsic phase disorder, and the light input record is required to interpret it.

*Phase angle of entrainment* (ψ) is the interval between the internal clock and the person's own behaviour — conventionally DLMO to habitual sleep onset. This is the more clinically informative of the two.

**Failure.** External phase abnormality is advanced or delayed sleep phase. Phase angle abnormality is the condition in which the person's behaviour sits at the wrong point in their own biological night, which produces symptoms even when the absolute timing looks conventional. A person with a late but internally consistent schedule can have a normal phase angle; a person on a conventional schedule fighting a delayed clock has an abnormal one. Distinguishing these two determines whether the intervention is to shift the clock or to shift the behaviour.

### 13.3 Amplitude

**Definition.** The depth of oscillation — the excursion between peak and trough, in hormone concentration, temperature, activity, and gene expression.

**Failure.** Amplitude reduction preserves the shape of the phase map and drains it of depth. It is the most prevalent failure mode in indoor populations, it produces no subjective sense of misalignment, and it is not detectable from timing measurements alone.

It also compounds the other failures, for a reason that is geometric. The oscillator's state is a point on a closed orbit, and a perturbation displaces that point by a fixed vector. The resulting change in phase depends on the radius of the orbit: the same displacement rotates a small orbit through a large angle and a large orbit through a small one. Phase lability is therefore inversely related to amplitude, and a flattened rhythm is not merely a weak one but one that any disturbance will displace further. Amplitude must be restored before phase can be reliably corrected.

### 13.4 Internal alignment

**Definition.** The offsets between oscillators — central to peripheral, and peripheral to peripheral — hold their normal values. Health here is the correctness of a set of phase angles, not the coincidence of peaks.

**Failure.** Internal desynchrony. Each oscillator remains internally coherent while the intervals between them change: hepatic and adipose phase moves toward the feeding schedule while the SCN holds to the light schedule. This is the failure mode produced by ordinary behaviour — late eating, night work, daylight sleep.

**Measurement requirement.** Detecting it requires at least one central marker and at least one peripheral marker measured in the same subject over the same interval. A set composed entirely of central markers cannot detect it at any sampling density.

### 13.5 Stability

**Definition.** Low day-to-day variance in the timing of the whole system.

**Failure.** Irregularity. The average phase may be correct while the variance is large, as in social jetlag, rotating shifts, and irregular sleep–wake rhythm. Regularity of sleep timing predicts all-cause mortality more strongly than sleep duration does (Windred et al., 2024), and rest–activity amplitude predicts mood disorder and cognitive outcome independently of sleep duration (Lyall et al., 2018). Stability is measured only across many days and is invisible to any single-session assessment.

---

## 14. Operational definition of the healthy state

A person is in circadian health when all five conditions hold simultaneously, sustained across an observation window of at least fourteen days.

| # | Dimension | Criterion | Marker |
|---|---|---|---|
| 1 | Entrainment | Phase stable across the observation window; drift under approximately 30 min/week | DLMO or actigraphic L5 midpoint, repeated |
| 2a | External phase | DLMO falls in a fixed relation to local sunset appropriate to season and latitude | DLMO |
| 2b | Phase angle ψ | DLMO to habitual sleep onset approximately 2–3 h | DLMO + actigraphic sleep onset |
| 3 | Amplitude | Rest–activity relative amplitude high; diurnal cortisol slope steep; distal temperature and heart rate rhythms show full excursion | RA from actigraphy; cortisol slope; wearable temperature and HR |
| 4 | Internal alignment | Peripheral oscillator phase holds its normal offset from DLMO; glucose tolerance rhythm peaks in the morning and its phase is not displaced relative to DLMO | Hair follicle or blood clock-gene phase; timed identical test meals with CGM |
| 5 | Stability | Sleep Regularity Index high; social jetlag under 1 h | Actigraphy across ≥14 days |
| — | Light input | ≥250 lx melanopic EDI during the waking day; <10 lx in the 3 h before sleep; <1 lx during sleep (Brown et al., 2022) | Wearable light sensor |
| — | Feeding input | Eating window contained within the light phase; last intake at least 3 h before DLMO | Timestamped intake log |

The criteria in rows 1, 2b, 4, and 5 are relational: each is an interval between two measured quantities rather than an absolute value. This is the operative property of the definition. Absolute clock times are secondary, and a schedule displaced as a whole with its internal offsets preserved is a normal variant, not a disorder.

---

## 15. The markers

### 15.1 Melatonin onset

Dim light melatonin onset is the reference phase marker for the central pacemaker. Melatonin is secreted by the pineal under direct SCN control through a fixed multisynaptic pathway, is suppressed by light but otherwise unaffected by posture, activity, or meals, and is stable within an individual across weeks. Every other phase in the system is expressed as an offset from it.

Saliva is sampled every 30–60 minutes beginning approximately 6 hours before habitual sleep onset and continuing 1–2 hours past it, under illumination below 10 lux with no light-emitting screens. Onset is the crossing of a fixed threshold, commonly 3 or 4 pg/mL, or 2 SD above the individual's baseline. Posture and food are held constant across the session.

### 15.2 Body temperature

The core temperature minimum falls approximately 7 hours after DLMO and 2 hours before waking, and divides the light phase response curve. Once DLMO is known it is largely predictable from it.

Core temperature is the most heavily masked variable in the system. Activity, posture, meals, ambient temperature, and sleep itself displace the nadir, and an unmasked value requires either a constant routine protocol or an ingestible capsule logging continuously.

Distal skin temperature, and the distal–proximal gradient, are available continuously from wrist-worn sensors. They report peripheral vasodilation, which is driven by melatonin, rather than core thermoregulation, and yield a phase and amplitude estimate on every day of an observation window.

### 15.3 Cortisol

Cortisol reaches the periphery through an efferent pathway distinct from the one driving melatonin: SCN to paraventricular nucleus to CRH to ACTH to adrenal cortex, together with direct autonomic innervation of the adrenal. Divergence between the melatonin and cortisol rhythms is therefore a finding about central organisation rather than a repeated measurement.

The cortisol awakening response is a response to the act of waking, confounded by sleep quality, anticipated demand, and awakening time. It reports reactivity, not phase.

The **diurnal cortisol slope**, the decline from morning peak to evening trough, is the quantity with the established link to health outcome; flatter slopes predict morbidity and mortality across a wide range of outcomes (Adam et al., 2017). Elevated bedtime cortisol is among the more sensitive single indicators of misalignment. Four saliva samples per day — waking, 30–45 minutes after waking, midday, and bedtime — across three days yield the slope.

### 15.4 Rest–activity

Continuous accelerometry across a multi-week window is the densest single source in the system, and the only one that measures stability at all.

**Sleep parameters.** Onset, offset, duration, efficiency, fragmentation.

**Non-parametric rhythm variables.** Interdaily stability (IS), reporting entrainment strength; intradaily variability (IV), reporting fragmentation; relative amplitude (RA); and the midpoints of the most active 10 hours (M10) and least active 5 hours (L5), giving a behavioural phase estimate on every day rather than in one session.

**Regularity.** The Sleep Regularity Index, and social jetlag as the difference in sleep midpoint between work and free days.

### 15.5 Light exposure

Light is the input variable, characterising the cause rather than grading the outcome.

**Spectral weighting.** Photopic lux weights the spectrum by cone sensitivity and misrepresents the input to the non-image-forming pathway. Melanopic equivalent daylight illuminance weights it by melanopsin sensitivity and is the quantity against which thresholds are set. Melanopic weighting is not complete: melanopsin photo-regenerates, long wavelengths returning the pigment toward its resting state, so two sources of equal melanopic EDI but differing short-to-long ratio are not equivalent stimuli.

**Contrast rather than level.** The extracted signal is the day-to-night ratio. The natural day spans roughly eight orders of magnitude; a modern interior spans fewer than two, the daytime signal reduced by three orders and the night signal raised by four.

**Geometry.** Interior lighting is designed for horizontal task planes while the eye receives vertical illuminance, and outdoor melanopic dose is dominated by the solid angle of visible sky rather than by direct sun. Sensors are worn at eye level, or wrist placement is corrected.

Derived: day-to-night melanopic contrast ratio; hours above 250 lx melanopic EDI; exposure in the 3 hours before sleep; exposure during the sleep period; time from waking to first exposure above threshold.

### 15.6 Peripheral clock gene expression

The expression phase of clock genes in an accessible peripheral tissue is the direct readout of a peripheral oscillator. It is unmasked by feeding, because the transcriptional state of the oscillator is sampled rather than one of its metabolic outputs.

**Hair follicles.** Plucked scalp or beard follicles yield sufficient RNA to determine the phase of *PER3*, *NR1D1*, and *NR1D2*. Three samples across a day give a peripheral tissue phase noninvasively, and the method detects the delayed peripheral phase of shift workers relative to their central markers (Akashi et al., 2010).

**Blood.** Machine-learned transcript panels estimate internal circadian time from one or two draws without dim-light conditions or serial sampling, with accuracy approaching DLMO (Braun et al., 2018; Wittenbrink et al., 2018; Hughey, 2017). Leukocytes are a peripheral tissue with their own oscillator and desynchronise from the SCN under misalignment. Plasma metabolite panels support the same approach (Kasukawa et al., 2012).

These yield a number in the same units as DLMO, and the alignment measurement is the difference between them.

### 15.7 Glucose

Continuous glucose monitoring is the practical peripheral functional readout in free-living conditions, with its interpretation governed by masking.

The 24-hour glucose acrophase under ad libitum feeding reports the eating schedule rather than hepatic phase. Under a standardised stimulus the same signal reports the oscillator: identical test meals administered shortly after waking and late in the waking day cancel the stimulus and leave the difference in postprandial excursion, which is the phase and amplitude of the glucose tolerance rhythm.

The overnight fasted period is the interval in which glucose is under endogenous hepatic control. The timing of the nocturnal nadir and the onset of the pre-waking rise in hepatic glucose output are usable phase measures where the interval since last intake is sufficient and recorded.

### 15.8 Thyroid hormones

TSH rises in the evening and peaks around sleep onset, and its amplitude is blunted by ageing, illness, and misalignment. Recovering the rhythm requires serial venous sampling across the night. A single daytime value, the form in which TSH is normally obtained, carries no circadian information, and the measurement is moved by thyroid disease, iodine status, intercurrent illness, and medication far more than by circadian state. Its place is the screening panel, excluding thyroid disease as a confounder of temperature, energy, sleep, and mood.

### 15.9 Meal timing

Meal timing is the peripheral zeitgeber, recorded as input alongside light. A displaced peripheral phase is explained by the eating record, and the eating record is what is subsequently changed. It is also a required covariate, since the unmasked glucose windows are interpretable only against a known time of last intake.

Derived: eating window duration, eating midpoint, interval from waking to first intake, interval from last intake to DLMO, fraction of energy consumed after DLMO, and the day-to-day variance of each.

---

## 16. Measuring internal alignment

### 16.1 The problem

Melatonin, core temperature, cortisol, and rest–activity all report central pacemaker phase or behaviour driven by it, and light is the central zeitgeber. A panel composed only of these measures central timing at high resolution and internal alignment not at all, at any sampling density, because alignment is an offset between a central and a peripheral oscillator and only one term of the difference is present.

Internal desynchrony is the failure mode produced by ordinary behaviour and the one most directly linking disrupted timing to metabolic disease. Measuring it requires a peripheral marker measured concurrently with a central one.

### 16.2 Masking must be separated from entrainment

A stimulus can act on a physiological rhythm in two distinct ways, and the distinction determines what any peripheral measurement means.

**Entrainment** shifts the oscillator. The effect is persistent: it remains when the stimulus is withdrawn, and the oscillator free-runs from its new phase.

**Masking** drives the output directly, bypassing the oscillator. The effect is transient: it disappears the moment the stimulus stops, and the oscillator's phase is unchanged.

Feeding does both. A meal entrains the hepatic clock, an effect that accumulates over days and persists. A meal also raises blood glucose within minutes, an effect that reflects the meal and not the clock.

The consequence is that the acrophase of a 24-hour glucose curve in a free-living person is very largely a record of when that person ate. It is a masked variable, and it cannot serve as a phase marker for the hepatic oscillator. This applies generally: any peripheral variable acutely driven by the behaviour that also entrains it is confounded by construction.

Three strategies recover an unmasked phase. Remove the stimulus, by constant routine or extended fast. Measure a variable the stimulus does not acutely drive. Or hold the stimulus constant and read the clock from the *variation in the response* to it.

### 16.3 Direct molecular readout of peripheral phase

The literal answer to what is measured in the body is the expression phase of clock genes in an accessible peripheral tissue, expressed as an offset from DLMO. These measurements are not masked by feeding, because the transcriptional state of the oscillator is what is being sampled rather than one of its metabolic outputs.

**Hair follicle clock gene expression.** Plucked scalp or beard follicles yield sufficient RNA to determine the phase of *PER3*, *NR1D1*, and *NR1D2*. Sampling at three points across a day gives a peripheral tissue phase noninvasively, and the method detects the delayed peripheral phase of shift workers relative to their central markers (Akashi et al., 2010). This is the cheapest true peripheral oscillator measurement available.

**Blood transcriptome timing.** Machine-learned panels estimate internal circadian time from one or two blood draws without dim-light conditions or serial sampling, with accuracy approaching DLMO in validation cohorts (Braun et al., 2018; Wittenbrink et al., 2018; Hughey, 2017). Leukocytes are a peripheral tissue with their own oscillator, and they desynchronise from the SCN under misalignment.

**Blood metabolite timing.** Plasma metabolite profiles are strongly rhythmic and support the same approach, internal time being estimated from the pattern across a panel of metabolites in one or two samples (Kasukawa et al., 2012; Dallmann et al., 2012).

Each of these yields a number in the same units as DLMO. The alignment measurement is the difference between them.

### 16.4 Provocative testing: reading the clock from the gain

Feeding necessarily produces a response, and that is what makes it usable. If the stimulus is held identical and only the time of day is varied, the stimulus cancels and the difference in response is attributable to the clock.

An identical test meal — fixed composition, fixed quantity — administered shortly after waking on one day and late in the waking day on another converts the acute response from a confound into the measurement. The quantity of interest is the ratio of the postprandial glucose and insulin excursions, which reports the phase and amplitude of the glucose tolerance rhythm rather than the timing of intake.

Under normal entrainment, tolerance is highest in the morning and declines across the day; postprandial glucose to an identical load is approximately 17 per cent higher in the biological evening than in the biological morning, an effect the circadian system produces independently of behaviour (Morris et al., 2015; Scheer et al., 2009). Reduced evening tolerance is therefore normal physiology. The abnormal findings are loss of the morning advantage, and a tolerance profile whose phase is displaced relative to DLMO.

This design measures the peripheral oscillator through its function rather than its transcripts, and requires only two standardised meals and continuous glucose monitoring.

### 16.5 Continuous glucose monitoring

**Not a phase marker in free-living use.** The 24-hour glucose acrophase under ad libitum feeding reports the eating schedule.

**The substrate for provocative testing.** CGM supplies the postprandial excursions that the two-meal design compares, without venous sampling.

**Unmasked windows.** The overnight fasted period is the interval in which glucose is under endogenous hepatic control rather than under acute dietary drive. The timing of the nocturnal glucose nadir and the onset of the pre-waking rise in hepatic glucose output are usable as hepatic output timing measures, provided the interval since the last meal is sufficient and is recorded.

**Amplitude.** The magnitude of the 24-hour excursion and of nocturnal variability, interpreted alongside the input record.

### 16.6 Meal timing

Meal timing is the peripheral zeitgeber. It belongs in the input record alongside light, and it is not a marker of alignment.

Its function in the protocol is causal interpretation and intervention design. A displaced peripheral phase is explained by the eating record; the eating record is what is subsequently changed. It is also a required covariate, since the unmasked CGM windows are only interpretable against a known time of last intake.

Recorded quantities: eating window duration, eating midpoint, interval from waking to first intake, interval from last intake to DLMO, fraction of energy consumed after DLMO, and the day-to-day variance of each.

---

## 17. The measurement set

Six measurements cover the five dimensions, with each dimension carried by a marker that reports it directly and no two markers reporting the same quantity.

| Measurement | Duration | Dimension carried |
|---|---|---|
| Wrist accelerometry with light sensor, distal temperature, and heart rate | ≥14 days continuous | Entrainment, amplitude, stability, behavioural phase, light input |
| Salivary DLMO | one session | Central phase — the reference for all offsets |
| Peripheral clock phase — plucked hair follicles across one day, or a validated blood transcript panel | one day within the window | Internal alignment, transcriptional |
| Two identical test meals, early and late in the waking day, with CGM | 2 test days within the CGM window | Internal alignment, functional; peripheral amplitude |
| Salivary cortisol, 4 samples/day | 3 days within the window | Amplitude, on the second central axis |
| Timestamped intake log | same 14 days | Feeding input; covariate for the glucose windows |

**Concurrency.** Internal alignment is an offset between two markers, so central and peripheral measurement overlap in time. A DLMO obtained a month before the glucose window yields no alignment measurement.

**Redundancy.** Core temperature reports the same central phase as DLMO at roughly a fixed offset and under heavy masking, and wrist temperature supplies a continuous phase and amplitude estimate at no additional burden. A single daytime TSH carries no circadian information.

**Reduced set.** Where the full set is not available, the wearable alone yields entrainment, amplitude, stability, behavioural phase, and the light input profile — sufficient to identify irregularity, amplitude loss, and inadequate light exposure. Central phase and internal alignment require the addition of DLMO and a peripheral marker respectively; neither is recoverable from behaviour.

---

## 18. Deriving the profile

Each dimension resolves to one or two numbers.

| Component | Computed as |
|---|---|
| Entrainment | Interdaily stability; drift in L5 midpoint across the window; DLMO repeatability |
| External phase | DLMO clock time, and DLMO relative to local sunset |
| Phase angle ψ | Sleep onset minus DLMO |
| Amplitude | Relative amplitude of rest–activity; diurnal cortisol slope; peak-to-trough excursion of distal temperature and heart rate |
| Internal alignment | Peripheral clock-gene acrophase minus DLMO; morning-to-evening ratio of postprandial glucose and insulin excursion to identical meals; phase of the tolerance rhythm relative to DLMO; timing of the nocturnal glucose nadir relative to DLMO |
| Stability | Sleep Regularity Index; social jetlag; day-to-day SD of eating midpoint |
| Light input | Day-to-night melanopic contrast ratio; hours above 250 lx melanopic EDI; melanopic EDI in the 3 h pre-sleep; melanopic EDI during sleep; time from waking to first exposure above threshold |
| Feeding input | Eating window duration; eating midpoint; interval from last intake to DLMO; fraction of energy consumed after DLMO |

These are reported as a profile rather than summed. The dimensions fail independently and call for different interventions: amplitude loss calls for increased daytime light dose, phase abnormality for timed light relative to the temperature minimum, internal desynchrony for compression and advancement of the eating window, and instability for regularisation before any of the others is attempted.

Order matters in intervention. Stability is addressed first, because phase and amplitude measured over an unstable baseline are not reliable quantities, and because regularisation alone resolves a substantial fraction of cases. Amplitude is addressed second, because phase correction applied to a low-amplitude oscillator is unstable by the geometry of section 13.3 and because raising the day-to-night contrast ratio often moves phase without any timed intervention. Phase is addressed third, and internal alignment last, since the eating window is repositioned against a central phase that must first be known and stable.

A further consequence of the same geometry constrains how phase is corrected. A stimulus strong enough, delivered near enough to the critical phase, drives the oscillator toward zero amplitude rather than to a new phase; bright light near the core temperature minimum can suppress the amplitude of the subsequent melatonin rhythm rather than shift it. Phase-shifting exposures are therefore specified by both timing and intensity, and high-intensity exposure close to the temperature minimum is avoided in favour of exposure displaced clearly to one side of it.

---

## 19. Solar referencing and exposure history

Kruse (2012, 2016) anchors timing to solar events rather than to clock time, on the ground that the biologically relevant variable is position within the local photoperiod, which clock time tracks only loosely and which diverges substantially across a time zone and across seasons. Applied to this protocol, every phase quantity is expressed against local sunrise and sunset in addition to local clock time, and the light record is scored against solar elevation rather than against hour of day.

Kruse (2016, 2022) treats the spectral composition and the ordered daily sequence of exposure as carrying information that total illuminance does not, specifically the progression from red and infrared at low solar angles through UVA to UVB near solar noon. Applied to measurement, this favours a spectrally resolved light sensor over a single-channel lux meter, and the retention of exposure timing relative to solar elevation as a separate variable from cumulative dose. Melanopic EDI captures the melanopsin-weighted portion of the input and does not capture the remainder.

Kruse (2011, 2016) treats serum vitamin D as a cumulative record of UVB exposure rather than as a nutrient status alone, which makes it a low-cost dosimeter for the portion of the light history that a wearable worn for two weeks cannot recover.

Kruse (2015, 2018) treats fasting glucose as a marker of protein turnover rate rather than solely of fuel handling. Under either interpretation the measurement is already captured by CGM, and the fasting value is retained as a summary quantity within it.

---

## 20. Limits of the set

The profile characterises the central pacemaker, one peripheral oscillator, and the behavioural and environmental variables that drive both. It does not resolve tissue-specific phase in liver, muscle, or immune cells, which requires biopsy or a validated tissue-specific transcript panel. Rhythmic transcript sets are largely non-overlapping between organs, so a normal glucose rhythm establishes hepatic and pancreatic alignment and does not generalise to other tissues.

Amplitude is assessed against population norms rather than against the individual's own prior state, so a decline from an unmeasured personal baseline reads as normal if it remains within the population range. Repeated assessment at intervals is the only correction for this.

The observation window is fourteen days. Seasonal variation in photoperiod, amplitude, and phase is therefore not captured by a single assessment, and comparison across assessments requires matching for season and latitude.

---

---

# APPENDICES

---

## A. Glossary

- **Amplitude** — magnitude of oscillation; independent of phase. A rhythm can be correctly timed yet weak.
- **CBTmin** — core body temperature minimum; divides the light phase response curve. Estimated as DLMO + 7 h, or habitual wake − 2 h.
- **Chronotype** — an individual's habitual phase, a joint output of intrinsic period and zeitgeber strength rather than a fixed trait.
- **DLMO** — dim light melatonin onset; the reference phase marker for the central pacemaker.
- **Entrainment** — the process bringing an endogenous oscillator into stable phase relationship with an external cycle.
- **Internal desynchrony** — each oscillator internally coherent, but the intervals between them altered.
- **ipRGC** — intrinsically photosensitive retinal ganglion cell; expresses melanopsin; integrates photon flux over minutes.
- **Masking** — direct drive of an output, bypassing the oscillator. Transient, and not a phase shift.
- **Melanopic EDI** — equivalent daylight illuminance weighted by melanopsin sensitivity; the metric against which light thresholds are set.
- **Phase** — position within the cycle, always referenced to a named marker.
- **Phase angle of entrainment (ψ)** — the stable offset between oscillator and zeitgeber; conventionally DLMO to sleep onset.
- **PRC** — phase response curve; the shift produced by a stimulus as a function of the phase at which it arrives.
- **SCN** — suprachiasmatic nucleus; central pacemaker; phase authority rather than execution engine.
- **SRI** — Sleep Regularity Index; day-to-day reproducibility of sleep timing.
- **TTFL** — transcription–translation feedback loop; CLOCK/BMAL1 ↔ PER/CRY with REV-ERB/ROR stabilising arm.
- **Zeitgeber** — a time-giving environmental cue capable of entraining an oscillator.

---

## B. Kruse attribution index

- **2011** — sections 6, 8, 19
- **2012** — sections 4, 5, 6, 11, 19
- **2013** — sections 2
- **2015** — sections 2, 4, 6, 7, 10, 11, 19
- **2016** — sections 4, 6, 8, 19
- **2018** — sections 2, 4, 6, 7, 8, 19
- **2019** — sections 4, 5, 6
- **2022** — sections 4, 6, 10, 19
- **2023** — sections 2
- **2024** — sections 5
