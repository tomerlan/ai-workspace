# Circadian Organization

## Foundations and Health

---

# PART I — BIOLOGICAL FOUNDATIONS

Feedback control corrects an error after it occurs. Feedforward control acts before the disturbance arrives, and for a disturbance that is predictable it achieves lower error at lower cost. The daily light–dark cycle is the most predictable disturbance an organism experiences, and a clock converts the response to it from feedback to feedforward: enzymes are positioned before the substrate load arrives, and protective systems before the insult.

The advantage is measurable. Cyanobacterial strains whose intrinsic period matches the imposed light cycle outcompete strains whose period does not, and the advantage disappears in constant light (Ouyang et al., 1998). Plants whose clock period matches the environmental cycle accumulate more carbon and survive better (Dodd et al., 2005). Circadian organisation is maintained by selection because prediction is cheaper than reaction.

---



## 1. Scope and definitions

**Chronobiology** — the study of endogenous biological timing systems and their interaction with environmental cycles.

**Circadian rhythm** — an endogenously generated oscillation with a period of approximately 24 hours, distinguished from a merely daily (*diurnal*) pattern by three properties: it persists in constant conditions, its period is temperature-compensated, and it is entrainable by environmental cues.

### 1.1 The oscillating system

**Oscillator** — any system that generates a self-sustaining rhythm: a cell, tissue, or network capable of producing a circadian rhythm without external timing input.

**Central pacemaker** — the suprachiasmatic nucleus of the hypothalamus, the oscillator that receives light information directly and imposes timing on the rest of the organism.

**Peripheral oscillator** — a circadian oscillator in any tissue other than the central pacemaker: liver, gut, pancreas, adipose, muscle, skin, immune cells. Each runs autonomously and is entrained by a mixture of central and local signals.

**Coherence** — the degree to which a population of oscillators holds a common phase. High coherence produces a strong ensemble rhythm; loss of coherence flattens the ensemble even when every individual oscillator continues to run.

### 1.2 Properties of an oscillation

**Period** — the duration of one complete cycle.

**τ (tau)** — the period an oscillator expresses in the absence of any time cue. In humans τ averages approximately 24.2 hours (Czeisler et al., 1999).

**Phase** — the position of an oscillator within its cycle. Phase is meaningful only relative to a stated reference point, and is reported as a clock time or as an interval from another rhythm.

**Acrophase** — the clock time of the fitted peak of a rhythm.

**Amplitude** — the magnitude of oscillation, the excursion between peak and trough. Amplitude and phase are independent: a rhythm can be correctly timed yet weak.

**Mesor** — the midline about which a fitted rhythm oscillates. A rhythm can lose mesor, amplitude, or phase independently.

**Offset** — the interval between the reference points of two rhythms. Timing relations are specified by offsets rather than by absolute clock times.

### 1.3 Interaction with the environment

**Zeitgeber** — an environmental cue capable of entraining a circadian oscillator. The dominant zeitgeber for the central pacemaker is the light–dark cycle. Feeding time, temperature, physical activity, and social cues act as zeitgebers for peripheral oscillators.

**Entrainment** — the process by which an endogenous oscillator is brought into stable phase relationship with an external cycle.

**Free-running** — running at τ because no zeitgeber is reaching the oscillator, so phase drifts progressively against the solar day.

**Phase angle of entrainment (ψ)** — the stable offset an entrained oscillator holds relative to its zeitgeber, or relative to the behaviour it governs. Conventionally measured as the interval from melatonin onset to sleep onset.

**Phase response curve (PRC)** — the phase shift produced by a stimulus, plotted as a function of the phase at which the stimulus arrives. The same stimulus advances, delays, or does nothing depending on when it lands.

**Masking** — direct drive of a measured output by a stimulus, bypassing the oscillator. A masked change is transient and leaves phase unaltered, which distinguishes it from entrainment.

### 1.4 Relations between oscillators

**Internal alignment** — the condition in which the offsets between oscillators hold their normal values. Alignment is a property of the intervals between rhythms, not of their coincidence.

**Internal desynchrony** — the failure of internal alignment: each oscillator remains internally coherent while the intervals between them change.

**Circadian misalignment** — a stable but incorrect phase relationship between internal time and either the external environment or other internal oscillators.

### 1.5 Individual variation

**Chronotype** — an individual's habitual phase. It is a joint output of τ and zeitgeber strength rather than a fixed trait. The distribution is continuous and substantially heritable, with τ, PRC amplitude, and light sensitivity all varying between individuals.

**Social jetlag** — the difference in sleep midpoint between scheduled and free days.

**Genotype.** PER2 and CK1δ variants produce advanced phase; CRY1 variants produce delayed phase.

**Age.** Amplitude declines and phase advances with age. Lens yellowing reduces transmission of short wavelengths, diminishing the entraining signal reaching ipRGCs; this is one contributor to circadian fragmentation in older adults.

### 1.6 Measured quantities

**Dim light melatonin onset (DLMO)** — the clock time at which melatonin concentration crosses a fixed threshold during a session held under illumination below 10 lux. The reference phase marker for the central pacemaker.

**Core body temperature minimum (CBTmin)** — the trough of the core temperature rhythm, falling approximately 7 hours after DLMO and 2 hours before waking. The reference point dividing the light phase response curve.

**Epoch** — the interval over which a continuously sampled signal is aggregated before storage. A logger samples internally at a higher rate, reduces each interval to a summary value, and writes that. Epoch length sets the resolution of the stored series, not the fidelity of measurement: a 1-minute epoch over a fortnight yields 20,160 values. The convention matches the integration time of the system being measured, and matches published series so that derived metrics remain comparable.

**Melanopic equivalent daylight illuminance (melanopic EDI)** — illuminance weighted by the spectral sensitivity of melanopsin rather than of the cones. The quantity against which light exposure thresholds are set.

**M10 and L5** — computed from the 24-hour activity profile averaged across the recording. Activity is expressed in accelerometer counts, a device-specific quantity, or in milli-g where raw data are retained. M10 is the mean activity of the ten consecutive hours with the highest activity, L5 the mean of the five consecutive hours with the lowest. The clock time at the centre of each window gives a behavioural phase estimate: L5 midpoint approximates the middle of the rest period, M10 midpoint the middle of the active period.

**Relative amplitude (RA)** — (M10 − L5) / (M10 + L5). A dimensionless number between 0 and 1 expressing how sharply the active day separates from the resting night. It approaches 1 when a person is vigorously active by day and still by night, and falls toward 0 as daytime activity declines, night-time restlessness increases, or both. Dividing by the sum removes dependence on absolute activity level, so a sedentary person and an athlete are compared on the contrast of their rhythm rather than on how much they move.

> **Central thesis** — Circadian organisation is a global constraint system on cellular behaviour. Temporal order limits the degrees of freedom available to cells and tissues. Disease of timing follows when that constraint weakens: processes that should be sequential run concurrently, and the error rate of every one of them rises.

---



## 2. The oscillator



### 2.1 Defining properties

Self-sustained oscillation persists under constant darkness, constant temperature, and the absence of social cues. Isolated tissue, and isolated single cells, continue to oscillate for weeks in culture.

Temperature compensation holds the period nearly constant across the physiological temperature range. Reaction rates in the underlying biochemistry vary with temperature in the ordinary way; the network is arranged so that these variations cancel.

Entrainment is phase-dependent. The magnitude and direction of the shift produced by a stimulus depend on the phase at which it arrives, described by the **phase response curve (PRC)**.

### 2.2 The oscillating variable

No single quantity constitutes the clock. In a single cell the oscillator traverses a closed trajectory — a limit cycle — through a state space whose axes are the concentrations, modification states, and localisations of its components. What oscillates is that state vector. Phase is position along the trajectory, and every measurable marker is a projection of the trajectory onto one axis, which is why phase is always reported relative to a named reference such as dim light melatonin onset or the core body temperature minimum rather than in absolute terms.

The measurable variables differ by level of organisation.

**Within a cell**, the oscillating quantities are the abundance of *Per* and *Cry* transcripts, the cytoplasmic and nuclear concentrations of their protein products, the phosphorylation state of PER, the occupancy of CLOCK:BMAL1 at E-box elements, and the redox poise of the shared carrier pools. In cultured cells these are followed continuously as bioluminescence from a PER2::LUCIFERASE fusion, which reports one protein's abundance as a proxy for the whole trajectory.

**Within a tissue**, the oscillating quantity is the fraction of the transcriptome under rhythmic control, together with the rhythmic proteome and metabolome that follow from it. In any single organ roughly 5–15% of expressed transcripts cycle. Across twelve mouse organs, 43% of all protein-coding genes are rhythmic in at least one tissue, but the rhythmic sets are largely non-overlapping between organs: apart from the core clock genes themselves, each tissue cycles a different set (Zhang et al., 2014). The same timing mechanism therefore controls almost entirely different output programs in liver, adipose, and muscle. Rhythms in protein and metabolite abundance are only partly predicted by transcript rhythms, a large fraction arising post-transcriptionally.

**Within an organism**, the oscillating quantities are plasma hormone concentrations, core body temperature, blood pressure, sleep propensity, cognitive throughput, and the rates of secretion, absorption, and excretion.

Rhythmic transcripts within an organ do not all peak together. They cluster into successive waves across the day, each wave corresponding to a coordinated block of the tissue's function.

---



### 2.3 The light phase response curve

For light in humans:


| Timing relative to core temperature minimum                 | Effect                                       |
| ----------------------------------------------------------- | -------------------------------------------- |
| Several hours before (biological evening and early night)   | Phase delay                                  |
| Immediately after (biological late night and early morning) | Phase advance                                |
| Mid-subjective day                                          | Minimal phase shift; amplitude reinforcement |


Core body temperature minimum falls approximately 1–3 hours before habitual wake time. Light received before this point delays the clock; light received after it advances the clock. Magnitude scales with irradiance, duration, and spectral composition, and saturates at high intensity.

Exogenous melatonin exhibits an approximately inverted PRC: administration in the biological evening advances phase, administration in the biological morning delays it.

The PRC is the formal basis for all timing-dependent intervention. The same exposure is corrective or harmful according to when it is received.

### 2.4 Amplitude and phase on the limit cycle

An oscillator's state is a point moving on a closed orbit. A perturbation displaces that point by a fixed vector, and the resulting change in phase depends on the radius of the orbit: the same displacement applied to a small orbit rotates the state through a large angle, and applied to a large orbit rotates it through a small one.

Phase lability is therefore inversely related to amplitude. A flattened rhythm is displaced further by any given zeitgeber or disturbance. This is the mechanism by which amplitude loss precedes and predisposes to phase instability, and it implies that amplitude must be restored before phase can be reliably corrected.

The practical form of this is that daytime light determines how much damage evening light does. High daytime exposure raises amplitude, and a high-amplitude oscillator is displaced less by a given evening stimulus. Sensitivity to evening light is separately modulated by preceding daytime exposure: individuals with high daytime light exposure show reduced melatonin suppression by a given evening stimulus. The same phone at 23:00 shifts an indoor worker further than someone who spent the morning outdoors. Daytime light and evening darkness are therefore one intervention rather than two, and the daytime half determines the tolerance of the evening half.

The limit is a stimulus strong enough, delivered near enough to the critical phase, to drive the state to the centre of the orbit, where amplitude is zero and phase is undefined. Bright light applied near the core temperature minimum reduces the amplitude of the subsequent melatonin rhythm rather than shifting it, and can suppress it to near zero (Jewett, Kronauer and Czeisler, 1991). Light at the wrong phase does not only mistime the oscillator; at sufficient intensity it degrades it.

### 2.5 The range of entrainment

An oscillator entrains to a driving cycle only when the mismatch between its intrinsic period and the driving period is small enough relative to the strength of the coupling. The set of period and strength combinations that permit entrainment forms a wedge that narrows to a point as coupling weakens.

Two consequences follow. The range of intrinsic periods that can be entrained contracts under a weak zeitgeber, so individuals with periods far from 24 hours fail to entrain under dim indoor conditions and entrain normally outdoors. And the phase angle at which entrainment settles is a function of both intrinsic period and zeitgeber strength: a long intrinsic period under a weak zeitgeber entrains at a delayed phase angle. Late chronotype under indoor conditions is the expected output of that relation rather than an independent trait, which is why a week of natural light exposure advances phase and compresses the spread between chronotypes (Wright et al., 2013).

### 2.6 The transcription–translation feedback loop

The core molecular oscillator in mammals is a delayed negative feedback loop operating on a period of approximately 24 hours.

**Positive arm.** The basic helix-loop-helix PAS-domain transcription factors **CLOCK** and **BMAL1** heterodimerise, translocate to the nucleus, and bind **E-box** elements (consensus CACGTG) in target promoters, activating transcription.

**Negative arm.** Among the genes activated are **PER1**, **PER2**, **PER3**, **CRY1**, and **CRY2**. Their protein products accumulate in the cytoplasm, form complexes with casein kinase 1δ/ε, re-enter the nucleus, and inhibit CLOCK/BMAL1-mediated transactivation, suppressing their own transcription. Progressive degradation of the repressor complex relieves inhibition and the cycle restarts.

**Stabilising arm.** CLOCK/BMAL1 additionally drive **REV-ERBα/β** and **RORα/β/γ**, which compete for ROR response elements in the *Bmal1* promoter, REV-ERB repressing and ROR activating. This generates the antiphase *Bmal1* rhythm and confers robustness against perturbation.

Cryptochrome carries a second, unrelated function as the leading candidate magnetoreceptor, through a radical-pair mechanism established in birds and insects and not established in humans.

The output of this loop is the set of **clock-controlled genes**. Rhythmic transcripts are enriched for rate-limiting enzymes and pharmacological targets. Most rhythmic genes cycle in only one or two tissues; there is no single circadian program, but many tissue-specific programs sharing a timing reference.

### 2.7 Determination of period

Period is set principally by imposed delays at the post-translational level: phosphorylation, nuclear entry, and regulated degradation.

**Phosphorylation.** CK1δ/ε phosphorylate PER proteins at multiple sites, governing both stability and the timing of nuclear entry. In familial advanced sleep phase syndrome, a PER2 mutation (S662G) abolishes a CK1 phosphorylation site and advances phase by approximately four hours; mutation of CK1δ produces the same phenotype.

**Ubiquitination and proteasomal degradation.** β-TrCP targets phosphorylated PER; FBXL3 targets CRY. Loss-of-function in FBXL3 substantially lengthens period.

**Additional modifications.** SUMOylation, acetylation, and O-GlcNAcylation further modulate stability and activity.

Period is therefore largely determined by protein turnover kinetics.

Kruse (2015) develops this observation into a general principle of cellular economics. Protein synthesis is the dominant energetic expenditure of eukaryotic cells, each peptide bond costing approximately five ATP — several times the cost of nucleotide polymerisation. Because ubiquitin marking governs the rate of that expenditure, and because clock proteins are themselves regulated by ubiquitin-mediated degradation, Kruse treats organism-wide ubiquitination rate as the principal quantity that circadian organisation exists to control. In this framing, chronic elevation of protein turnover — driven by signalling errors originating in the light environment — constitutes the common pathway from environmental mismatch to accelerated cellular ageing, replicative exhaustion, and telomere attrition. Kruse (2018) extends the same logic to interpret elevated fasting glucose as a marker of raised ubiquitination rate rather than solely of impaired fuel handling.

### 2.8 Non-transcriptional oscillators

Human erythrocytes are anucleate and transcriptionally inert. Maintained in buffer without substrate and in constant darkness, they sustain a 24-hour rhythm in peroxiredoxin oxidation state (O'Neill and Reddy, 2011). The same rhythm appears in bacteria, archaea and eukaryotes alike (Edgar et al., 2012). In cyanobacteria three purified proteins with ATP — KaiA, KaiB, KaiC — sustain a circadian rhythm in a test tube for days (Nakajima et al., 2005).

A second oscillator therefore underlies the transcriptional loop, older in evolutionary terms and independent of it.

What oscillates is redox poise: the ratio of reduced to oxidised carrier across the shared NAD, NADP, glutathione and thioredoxin pools. Every reaction that consumes electrons draws from the same pool that every reaction producing them fills, so the ratio is a single intensive quantity, comparable to a voltage, coupling all metabolism simultaneously. Peroxiredoxin reports it.

The rhythm arises because oxidation triggers the response that reverses it, and that response takes hours to arrive. Meal timing shifts its phase, which is the mechanism by which feeding entrains peripheral clocks (5.3).

### 2.9 The origin of the redox signal

Respiratory electron transfer proceeds by quantum tunnelling between redox centres, at rates that fall exponentially with distance and become negligible beyond approximately 14 Å. The spacing of centres within and between respiratory complexes is held below that limit, which makes the arrangement of the chain a physical constraint rather than a matter of convenience, and makes supercomplex organisation and cristae geometry determinants of transfer efficiency.

Superoxide production at complex I rises steeply with the mitochondrial membrane potential, particularly under reverse electron transport when the potential is high and the ubiquinone pool is reduced. Oxidant load is therefore a function of the thermodynamic state of the membrane rather than a fixed leak fraction, and the redox oscillation of 2.8 is driven by a quantity that responds within minutes to substrate supply and demand.

Inner membrane lipid composition modulates both. Cardiolipin is required for supercomplex assembly and for the activity of several complexes, and the degree of unsaturation of membrane fatty acids alters proton permeability and the packing environment of the respiratory chain. Kruse (2015) builds on this in treating docosahexaenoic acid as a determinant of the gain of light-driven signalling, on the ground that the highly unsaturated membranes of retina and neural tissue are the ones in which photic signal transduction occurs.

### 2.10 Coupling of the redox and transcriptional oscillators

The two systems are reciprocally connected rather than arranged as master and slave.

Redox state acts directly on the transcriptional loop at the level of DNA binding. The reduced cofactors NADH and NADPH enhance binding of CLOCK:BMAL1 and NPAS2:BMAL1 heterodimers to E-box elements, while the oxidised forms inhibit it (Rutter et al., 2001). The ratio of reduced to oxidised nicotinamide cofactors — a direct readout of metabolic flux — therefore gates transcriptional output with no intervening signalling cascade. NAD⁺ availability, set by the clock-controlled salvage enzyme NAMPT, drives SIRT1-mediated deacetylation of BMAL1 and PER2, closing a second metabolic feedback onto the loop (Nakahata et al., 2009; Ramsey et al., 2009).

The dependency runs in both directions. Peroxiredoxin and redox rhythms persist in cells lacking BMAL1 or both cryptochromes, but with reduced amplitude and reduced robustness; transcriptional rhythms in turn degrade when the redox environment is perturbed.

Circadian organisation is therefore layered: a redox-based oscillator of great evolutionary antiquity, running on the chemistry of fuel oxidation and requiring no genome, overlaid by a transcriptional loop that provides amplification, tissue-specific outputs, and the interface through which photic input entrains the whole system.

Kruse (2013) treats this architecture as foundational rather than peripheral. If timekeeping precedes and outlasts gene expression, then the genome cannot be the timekeeper; genes amplify and stabilise a timing signal that originates elsewhere. On this account circadian control is imposed by the physical environment on cellular redox state, and transcriptional machinery is downstream of, and subordinate to, that imposed rhythm. Kruse (2023) restates the principle in general form: environmental electromagnetic input determines gene expression rather than the reverse, and disorders arising from disrupted timing will therefore present without any alteration to DNA sequence.

## 3. The central pacemaker



### 3.1 The suprachiasmatic nucleus

The **suprachiasmatic nucleus (SCN)** is a paired hypothalamic structure of approximately 20,000 neurons situated immediately dorsal to the optic chiasm.

Its status as master pacemaker rests on three lines of evidence: ablation abolishes behavioural rhythmicity; transplantation of SCN tissue into an arrhythmic host restores rhythmicity with the *donor's* period (Ralph et al., 1990); and isolated SCN tissue sustains oscillation in culture indefinitely.

### 3.2 Network organisation

Individual SCN neurons are imprecise oscillators: period varies by hours between cells and drifts within a cell, while the intact nucleus keeps time to within minutes. Precision is a property of the coupled network rather than of its elements, arising because neurons synchronise through VIP and GABA signalling and the ensemble averages the noise of its members.

The **core**, ventrolateral and retinorecipient, expresses vasoactive intestinal peptide (VIP) and gastrin-releasing peptide. The **shell**, dorsomedial, expresses arginine vasopressin (AVP).

VIP signalling through the **VPAC2** receptor is required for network synchrony. Deletion of VIP or VPAC2 renders the animal behaviourally arrhythmic, not by silencing individual oscillators but by desynchronising them.

Coupling strength governs a trade-off. A strongly coupled network is precise and resists perturbation: the SCN shifts slowly in response to abrupt changes in the light–dark cycle, which accounts for the multi-day time course of re-entrainment after transmeridian travel, and it is not reset by the temperature rhythm it generates. Weakly coupled peripheral networks shift quickly and are reset by temperature and feeding. The hierarchy between central and peripheral oscillators follows from differing coupling strength rather than from any difference in the underlying molecular mechanism.

### 3.3 Output pathways

The SCN distributes timing information through autonomic outflow, through humoral signals — principally glucocorticoids — and through the daily body temperature rhythm. The multi-synaptic pathway to the pineal runs SCN → paraventricular nucleus → intermediolateral cell column → superior cervical ganglion → pineal.

---



## 4. Photic input



### 4.1 The non-image-forming pathway

Photic entrainment is mediated by a photoreceptive system anatomically and functionally distinct from the image-forming system.

**Intrinsically photosensitive retinal ganglion cells (ipRGCs)** constitute approximately 1–2% of retinal ganglion cells and express the photopigment **melanopsin (OPN4)**. They depolarise to light directly, in the absence of rod and cone input (Berson, Dunn and Takao, 2002).

Their properties are those of an irradiance detector rather than an image detector: peak spectral sensitivity near **480 nm**, slow kinetics, sustained response, high threshold, and integration over minutes. Phototransduction proceeds through Gq/11 → PLCβ4 → TRPC6/7.

Rods and cones adapt within milliseconds and report contrast. Melanopsin-expressing ipRGCs depolarise slowly, sustain their response for the duration of the stimulus, and decay slowly after it ends. The cell integrates photon capture over minutes to tens of minutes, which makes it an irradiance detector rather than a contrast detector, and makes cumulative dose rather than peak brightness the quantity the clock receives.

ipRGC axons form the **retinohypothalamic tract**, projecting to the SCN and additionally to the olivary pretectal nucleus, intergeniculate leaflet, habenula, and ventrolateral preoptic nucleus.

Rods and cones contribute to entrainment through convergence onto ipRGCs, particularly at low irradiance; complete abolition of entrainment requires elimination of all three photoreceptor classes (Hattar et al., 2003). The ipRGC constitutes the final common path.

Clinically, individuals blind from outer retinal disease but retaining intact ipRGCs entrain normally despite absent visual perception. Individuals lacking all light perception free-run with τ slightly exceeding 24 hours, producing **non-24-hour sleep–wake disorder**, in which sleep timing drifts progressively later and cycles in and out of alignment over weeks.

### 4.2 The retina as a timing organ

Kruse (2015) makes the functional separation between the two retinal systems the organising principle of the entire framework: the eye is a clock before it is a camera, and its timing function is hierarchically superior to its imaging function. Under this framing the inner retina constitutes the top of a control hierarchy governing every downstream oscillator, and ocular pathology reports on the state of that hierarchy. The consequences are taken up in section 10.

The clinical corollaries Kruse (2016) draws from this position govern much of the protocol: light must reach the retina unfiltered, since spectacles, contact lenses, sunglasses, windscreens, and window glass each remove portions of the spectrum that the non-image-forming system requires; and exposure must occur at the times when the required frequencies are present in terrestrial sunlight.

### 4.3 Chromophore stability

Melanopsin binds the chromophore **retinal** through a Schiff base linkage. This linkage is comparatively susceptible to spontaneous cleavage in mammals, and is particularly unstable in human melanopsin.

Melanopsin is also photo-regenerating. The pigment interconverts between resting and signalling states under illumination, long wavelengths driving the signalling state back toward rest while short wavelengths drive it forward, so the pigment sustains its own chromophore supply independently of the retinal pigment epithelium (Emanuel and Do, 2015). The ratio of short to long wavelengths therefore sets the steady-state fraction of pigment available for signalling, and two spectra with identical melanopic weighting drive the pathway differently. A blue-enriched, red-depleted source and a broadband source of the same melanopic irradiance are not equivalent stimuli.

Kruse (2018) builds a mechanism of photoreceptor injury on this instability. Excess short-wavelength exposure, particularly in the absence of the balancing red and infrared frequencies present in natural light, liberates retinal from its protein. Free retinal is a reactive aldehyde and an efficient photosensitiser, and in the free state damages chromophores throughout the photoreceptive apparatus. Damaged chromophores no longer absorb light at their design frequencies, degrading the optical signalling on which timing depends. Kruse (2018) identifies this as the proximate lesion underlying the blue light hazard.

### 4.4 Additional opsins

**OPN5 (neuropsin)** is sensitive to ultraviolet and violet light and photoentrains local oscillators in the retina and cornea independently of melanopsin (Buhr et al., 2015).

Kruse (2016) assigns neuropsin a central role in tissue regeneration, proposing that UVA acting through corneal and cutaneous neuropsin initiates the melatonin-dependent programme by which mitochondrial populations are renewed and the proportion of defective mitochondrial genomes — **heteroplasmy** — is reduced. On this account the daily UVA signal is not merely a timing cue but the trigger for a repair cycle, and its chronic absence permits heteroplasmy to accumulate, which Kruse (2016) treats as the principal substrate of ageing and degenerative disease.

Opsins are expressed outside the eye. **OPN4** and **OPN3** are present in skin, and **OPN3** in adipocytes, where light exposure modulates lipolysis. Kruse (2012) predicted extra-ocular photoreception in skin and subsequently in subcutaneous adipose tissue on the grounds that the cold and light protocols produced systemic effects too rapid and too large to be mediated through the eye alone.

### 4.5 Membrane substrate

Docosahexaenoic acid (DHA) is concentrated in photoreceptor outer segments and synaptic membranes to a degree unmatched elsewhere in the body, and constitutes approximately half of central nervous system polyunsaturated fatty acid. Retinal DHA content exceeds that of brain. Despite the availability of docosapentaenoic acid, which differs by a single double bond and is both cheaper to synthesise and less susceptible to peroxidation, DHA has not been substituted at these positions across approximately 600 million years of eukaryotic evolution.

DHA-rich phospholipids provide the membrane environment permitting G-protein-coupled photoreceptive events. Photoreceptor discs contain phospholipids bearing ω-3 chains at both SN-1 and SN-2 positions; these species constitute approximately 52% of phosphatidylserine and 31% of phosphatidylcholine in the disc membrane. The DHA-derived docosanoid **neuroprotectin D1** upregulates Bcl-2 and Bcl-xL and downregulates Bax and Bad, generating a pro-survival transcriptional state in the retinal pigment epithelium.

Kruse (2015) treats DHA concentration as the gain control of the circadian system. Because melanopsin is a G-protein-coupled photopigment dependent on its lipid environment, and because DHA is subject to photo-oxidative destruction by short-wavelength light, tissue DHA status sets the fidelity with which light is transduced into a timing signal. Kruse (2015) accordingly holds that dietary DHA sufficiency is a prerequisite for circadian function rather than a general nutritional recommendation, and that DHA loss and light injury are mutually reinforcing.

### 4.6 Irradiance and dose–response

The magnitude of the entraining signal depends on irradiance, spectral composition, duration, and timing.


| Environment                         | Approximate illuminance  |
| ----------------------------------- | ------------------------ |
| Direct sunlight                     | 30,000–100,000 lux       |
| Overcast daylight, outdoors         | 1,000–10,000 lux         |
| Well-lit interior                   | 300–500 lux              |
| Domestic interior, evening          | 50–200 lux               |
| Threshold for melatonin suppression | approximately 30–100 lux |


Phase shift magnitude and melatonin suppression follow a saturating function of the logarithm of irradiance. Half-maximal melatonin suppression occurs at illuminances on the order of a hundred lux, well below ordinary interior lighting, and the curve is steepest at the low end of its range.

The practical consequences run in both directions. At night, the first increment of light above darkness carries most of the biological effect, so the difference between complete darkness and dim light exceeds the difference between dim light and bright light. During the day, returns diminish above the saturating range, so additional illuminance beyond a threshold adds little.

Intensity and duration are not fully interchangeable. Sequences of brief bright pulses produce phase shifts approaching those of continuous exposure of the same total duration, because the pathway responds to the onset of illumination more strongly than to its maintenance (Gronfier et al., 2004).

The quantity the system extracts is the contrast between day and night rather than the absolute level of either. Outdoor illuminance spans approximately eight orders of magnitude across the natural day, from above 100,000 lux in direct sun to below 0.001 lux under an overcast moonless sky. A modern interior spans less than two.

Indoor daytime illuminance is one to two orders of magnitude below the level that holds a stable phase angle at high amplitude. Evening indoor illuminance sits above the melatonin suppression threshold and lands in the delay portion of the phase response curve. The strongest input of the day therefore arrives in the evening, and entrainment settles at a late phase.

The compression is bilateral: the daytime signal is reduced by three orders of magnitude and the night signal raised by four. Either alone reduces the contrast; together they reduce it to a fraction of the natural value, and oscillator amplitude follows the contrast. Measurement and intervention are therefore directed at the ratio rather than at either level in isolation.

### 4.7 Spectral composition

Spectral composition varies systematically through the solar day. At sunrise and sunset the solar disc is viewed through maximal atmospheric path length, and the spectrum reaching the eye is dominated by red and near-infrared frequencies with minimal ultraviolet. Ultraviolet A appears as solar elevation increases; ultraviolet B becomes available only above a solar elevation of approximately 30 degrees, and therefore only during the hours surrounding solar noon, and at higher latitudes only during part of the year.

Kruse (2016, 2022) organises the protocol around this sequence. The ordered daily progression from infrared and red, through ultraviolet A, to ultraviolet B constitutes the signal the system evolved to read, and the sequence carries information that no single component reproduces. Viewing the sunrise establishes the phase reference; subsequent exposure as ultraviolet becomes available supplies the frequencies required for the photochemical steps in 4.4 and 6.1. Kruse (2022) specifies exposure beginning at sunrise and continuing as ultraviolet becomes available, using ultraviolet index 1 as the practical threshold for UVA availability.

Ordinary window glass transmits visible light while removing essentially all ultraviolet B, the majority of ultraviolet A, and a substantial fraction of infrared A. Kruse (2019) treats indoor daytime occupancy as spectral truncation rather than merely reduced intensity: the light reaching the retina indoors is not a weaker version of sunlight but a different signal, retaining the short-wavelength component that suppresses melatonin while omitting the components that drive the compensating photochemistry.

The dose required to produce a given effect varies with the receiver. Constitutive melanin density determines the ultraviolet dose needed for equivalent cutaneous photochemistry, and therefore the exposure appropriate at a given latitude and season. Kruse (2015, 2022) treats latitude, season, and pigmentation as jointly determining the appropriate exposure, and holds that dietary composition should correspond to the photoperiod and latitude in which it is consumed, on the grounds that carbohydrate availability historically covaried with long photoperiod and that the two signals are read together.

### 4.8 Tissue optics

Absorption and scattering in tissue vary strongly with wavelength. Between approximately 650 and 1350 nm, haemoglobin absorption has fallen and water absorption has not yet risen, producing an optical window in which penetration is greatest. Blue light is attenuated within a fraction of a millimetre of the skin surface; red penetrates several millimetres; near infrared penetrates centimetres.

Extraocular photoreception is therefore constrained by wavelength. Short-wavelength effects are restricted to the eye and to superficial skin, where opsins are in fact expressed: OPN5 mediates local light entrainment of peripheral tissues, and OPN3 in adipocytes supports light-dependent regulation of lipolysis and thermogenesis (Buhr et al., 2015; Nayak et al., 2020). Long-wavelength effects can reach deep tissue, and the principal deep chromophore is cytochrome c oxidase, whose absorption bands near 660 and 810 nm underlie measurable increases in complex IV activity under red and near-infrared illumination.

Kruse (2012) states the prediction that photoreception is not confined to the eye and that skin and subcutaneous tissue respond directly to light; the opsin findings establish the general claim, and the wavelength constraint sets its limits.

---



## 5. Peripheral oscillators and internal synchrony



### 5.1 Distribution

Essentially every nucleated cell contains a functional transcription–translation feedback loop. Liver, gut, pancreas, adipose tissue, skeletal muscle, kidney, skin, and immune cells all oscillate autonomously in culture.

The SCN synchronises these oscillators, holding a common phase across tissues whose individual periods differ.

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



### 5.2 What drives a tissue rhythm

A rhythmic transcript in liver has three possible sources, and they have been separated by deleting the clock in one organ while leaving the rest of the animal intact.

**The local oscillator.** Explanted liver, lung, and pituitary continue to oscillate in culture for weeks with no external input, so the oscillator is intrinsic to the tissue rather than imposed on it.

**Systemic cues.** In liver-specific *Bmal1* knockouts the majority of hepatic transcript rhythms persist, driven by feeding time, body temperature, and glucocorticoid rhythm. Only a minority require the local clock. The same result appears from the other direction: imposing a rhythmic feeding schedule on clock-deficient animals restores a large fraction of liver rhythms.

**Both together.** A third set requires the local clock and a systemic signal simultaneously, and is lost when either is removed. The adrenal works this way: it carries its own clock and receives ACTH drive, so the cortisol rhythm reflects central timing gated by a local oscillator.

Some tissues hold no oscillator at all and report only the signal reaching them. The pineal is the clearest case — it has no autonomous clock, and melatonin output tracks sympathetic drive from the SCN. This is why DLMO is the reference phase marker: it reports pacemaker state with nothing local added. Plasma glucose and blood pressure are similarly driven, by feeding and by autonomic tone.

The practical consequence is that a flattened peripheral rhythm does not localise the fault. It is produced by a damaged local oscillator, by loss of the systemic cue, or by their misalignment, and distinguishing them requires measuring the cue and the rhythm separately — which is why 15.6 logs intake timing alongside the glucose stream.

### 5.3 Peripheral zeitgebers

Seven signals carry timing from the pacemaker and the environment to peripheral tissue.

**Feeding time** is the dominant zeitgeber for hepatic and gastrointestinal oscillators. Restricted feeding at a phase opposed to the light–dark cycle uncouples the liver clock from the SCN entirely, shifting hepatic gene expression within days while the SCN, entrained by light, remains in place (Damiola et al., 2000; Stokkan et al., 2001). In humans, delaying meals by five hours delays adipose tissue clock gene rhythms without shifting central phase markers (Wehrens et al., 2017).

**Temperature.** The SCN-driven body temperature rhythm entrains peripheral oscillators. Peripheral clocks are resettable by temperature while the SCN itself is not, preventing the master oscillator from being reset by its own output (Buhr, Yoo and Takahashi, 2010).

**Glucocorticoids.** The daily cortisol pulse acts on glucocorticoid receptors present in most tissues, and is the broadest single synchronising signal the pacemaker emits.

**Autonomic outflow.** Sympathetic and parasympathetic tone vary across the day and reach every organ, including the sympathetic pathway that drives pineal melatonin synthesis.

**Melatonin.** Acting through MT1 and MT2 receptors, it carries the darkness signal to tissues including the pancreatic beta cell.

**Nutrient state.** Insulin, glucose, and the NAD⁺/SIRT1 and AMPK pathways report feeding at the level of cellular metabolism rather than as a behavioural event (6.8).

**Activity and mechanical load.** Locomotion, and the oxygen and mechanical cues accompanying it, shift muscle and cardiovascular oscillators.

**The retina** is exceptional among peripheral tissues in entraining directly to light and maintaining autonomous rhythmicity while supplying the central signal.

### 5.4 Hierarchy and override

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

**Broadcast, not correction.** The SCN emits one signal set — cortisol, temperature, and the feeding rhythm it drives through behaviour — identical to every tissue. No channel returns tissue phase to the SCN, so the pacemaker holds no information about where liver or kidney currently sits. Each tissue locks onto the broadcast through its own phase response curve, as the SCN locks onto light.

Three consequences follow. Tissues settle at different phase angles to the same signal, because each has its own τ and sensitivity, which is why organs peak at different clock times rather than together. A tissue whose τ lies too far from 24 hours, or which receives the signal too weakly, free-runs inside an otherwise entrained body. And conflicting broadcasts split the periphery: night eating delivers a feeding signal to liver at one phase while temperature and cortisol arrive at another, and the tissues follow different signals.

**Override rules.** Light overrides melatonin. Feeding overrides the liver clock. No single signal overrides everything downstream of it. Chronic conflict between signals produces desynchrony rather than a winner.

> **Key.** When cues conflict chronically — bright light at night with daytime feeding — subsystems drift apart. The clocks still run. They disagree.

---



## 6. Output pathways

The pacemaker emits five signals: melatonin, cortisol, body temperature, autonomic outflow, and thyrotropin. The processes those signals gate follow from 6.6.

### 6.1 Melatonin

Pineal melatonin is synthesised from serotonin, with **AANAT** as rate-limiting enzyme, under SCN control through the pathway described in 3.3. Secretion occurs only in darkness and is acutely suppressed by light. **Dim light melatonin onset** is the reference marker of circadian phase.

Melatonin functions as a signal of darkness rather than as a hypnotic, which accounts for its modest sedative effect and substantial phase-shifting effect. Low doses in the range 0.3–0.5 mg are as effective as higher doses for phase shifting, with fewer residual next-day effects.

**The extrapineal pool.** Melatonin is synthesised well beyond the pineal: in the gastrointestinal tract in far greater total quantity than in the pineal, and in retina, skin, bone marrow, lymphocytes, thymus, gonads, and within mitochondria. Pinealectomy abolishes the circulating rhythm without eliminating tissue melatonin. Extrapineal melatonin is largely non-rhythmic and acts locally, functioning principally as an antioxidant.

Kruse (2022) makes mitochondrial melatonin central. Melatonin is both lipid- and water-soluble, distributes across all subcellular compartments, and acts as a direct free radical scavenger and indirect antioxidant, stimulating superoxide dismutase, glutathione peroxidase, glutathione reductase, and catalase. Kruse (2022) holds that its production is driven locally by near-infrared and ultraviolet A penetrating tissue, and that consequently melatonin status is a function of daytime light exposure rather than solely of nighttime darkness. On this account melatonin is the principal agent limiting mitochondrial heteroplasmy, and sleep quality serves as an index of mitochondrial competence rather than only as its cause.

Kruse (2022) further proposes the daily photochemical sequence: morning ultraviolet exposure supplies the energy for conversion of tryptophan toward serotonin, with neuropsin setting the rhythm; the accumulated serotonin pool is converted to melatonin in darkness. Under this model the quantity of melatonin available at night is determined by the ultraviolet exposure received that morning, and darkness alone is insufficient if the daytime signal was absent.

### 6.2 Cortisol

Cortisol rises steeply in the period preceding waking and peaks approximately 30–45 minutes after waking, declining across the day to a nadir near midnight. The cortisol awakening response is SCN-driven through the hypothalamic–pituitary–adrenal axis and functions as a synchronising signal to peripheral oscillators.

Kruse (2012) treats the morning cortisol peak as the terminal step of a sequence initiated by photic input. The precedence he assigns to the flattened profile is in 10.

### 6.3 Body temperature

Core body temperature oscillates with an amplitude of approximately 1°C, reaching its minimum 1–3 hours before habitual wake time. It serves both as a phase marker and, as described in 5.2, as a zeitgeber for peripheral oscillators.

### 6.4 Autonomic outflow

The SCN reaches the periphery directly through the autonomic nervous system, by way of the subparaventricular zone and the paraventricular nucleus to preganglionic sympathetic and parasympathetic neurons. This is the route to the pineal described in 3.3, and equally the route to liver, pancreas, adrenal cortex, and adipose tissue, carrying phase information independently of any circulating hormone. Denervation of a target organ alters that organ's rhythm while leaving the SCN intact.

Sympathetic tone rises in the hours before waking; parasympathetic tone dominates during night sleep. Heart rate and blood pressure follow, with a morning surge and a nocturnal fall of 10–20%. High-frequency heart rate variability, which indexes vagal activity, peaks during night sleep. A nocturnal blood pressure fall below 10% — **non-dipping** — is the established marker of a flattened autonomic rhythm and predicts cardiovascular events independently of daytime pressure.

### 6.5 Thyrotropin

**Thyrotropin (TSH)** is secreted under hypothalamic TRH control with a distinct circadian profile: a nadir in the late morning and afternoon, a rise beginning in the early evening, and a peak in the hours around sleep onset and the early night.

Sleep acutely inhibits secretion, so the nocturnal level is the product of a circadian rise and a sleep-dependent brake acting against it. Sleep restriction raises nocturnal TSH; displaced sleep separates the two components and the peak appears without its brake.

Amplitude falls under chronic misalignment, which is the quantity the bedtime-to-waking ratio in 12.3 reports.

### 6.6 Sleep–wake regulation

Sleep timing is determined by the interaction of two processes (Borbély). **Process S** is homeostatic sleep pressure, accumulating with time awake and dissipating during sleep, with adenosine as the principal candidate substrate. **Process C** is the circadian alertness signal, independent of prior sleep.

The circadian system actively promotes wakefulness during the biological evening, opposing accumulated sleep pressure, and promotes sleep in the early morning as pressure declines. Misalignment between the two processes, rather than abnormality in either alone, underlies most disorders of sleep initiation and maintenance.

### 6.7 Glucose regulation

MT1 and MT2 melatonin receptors are expressed on pancreatic beta cells, where melatonin inhibits insulin secretion. The **MTNR1B** locus, encoding MT2, is among the most consistently replicated type 2 diabetes risk loci in human genetics, and genotype at that locus modifies the glucose response to eating inside the melatonin window. Food consumed during the period of elevated circulating melatonin produces measurably impaired glucose tolerance, an effect modified by MTNR1B genotype.

Kruse (2016) treats melatonin and insulin as opposed metronomes carrying complementary information: insulin encodes the high-energy signal associated with long photoperiod and carbohydrate availability, melatonin encodes darkness and the suspension of feeding. Where light at night is present, the opposition collapses, and insulin secretion proceeds at a phase where melatonin should be suppressing it. Kruse (2016) therefore treats insulin resistance as a disorder of light exposure expressed through carbohydrate handling rather than a disorder of carbohydrate intake as such, and prohibits food intake after dark on this basis.

### 6.8 Metabolic coupling

The clock and cellular metabolism are reciprocally coupled through nicotinamide adenine dinucleotide.

**NAD⁺** concentration oscillates. **NAMPT**, the rate-limiting enzyme of the NAD⁺ salvage pathway, is a clock-controlled gene. **SIRT1**, an NAD⁺-dependent deacetylase, deacetylates BMAL1 and PER2, acting back on the core loop. The clock therefore drives NAD⁺ availability, and NAD⁺ availability drives the clock.

Kruse (2015, 2019) places this loop at the centre of the relationship between light and metabolism, expressing it as the sequence: sunlight and fasting raise the NAD⁺/NADH ratio, NAD⁺ activates SIRT1, SIRT1 modulates BMAL1 and CLOCK, which drive NAMPT, which regenerates NAD⁺. Kruse (2019) holds that the entry point of this cycle is the light environment, that artificial light lowers NAD⁺ at complex I, and that the cycle therefore cannot be driven by dietary intervention when the light environment is deficient.

### 6.9 Energy balance and adiposity signalling

**Leptin** is secreted by adipose tissue in proportion to fat mass and acts on hypothalamic receptors, activating POMC/CART neurons and inhibiting NPY/AgRP neurons. Its action is asymmetric: falling leptin produces a powerful signal of energy deficit, while elevated leptin produces a comparatively weak signal of sufficiency. In obesity, circulating leptin is elevated without corresponding central effect — leptin resistance — attributed to impaired transport across the blood–brain barrier, to upregulation of the negative regulators SOCS3 and PTP1B, and to hypothalamic inflammation.

Leptin secretion is rhythmic, rising through the evening and peaking during the night. Sleep restriction lowers leptin and raises ghrelin.

Kruse (2011) treats sleep and energy balance as a single system rather than two interacting ones, on the grounds that arousal and feeding are governed by an overlapping hypothalamic population, and that leptin resistance therefore necessarily presents with disordered sleep. Kruse (2018) resolves the relationship between adiposity signalling and photoreception by proposing that leptin carries optical as well as energetic information from the skin surface to the hypothalamus, and that free retinal liberated by inappropriate light exposure damages leptin in subcutaneous tissue. On this account leptin resistance is a consequence of photoreceptive failure, and is corrected by repair of the light environment rather than by dietary restriction.

### 6.10 Cell cycle, repair, and immunity

Circadian gating of the **cell cycle** operates partly through PER2, with downstream effects on Cyclin D1, c-Myc, and Wee1. *Per2*-mutant animals show elevated tumour incidence. **DNA repair** capacity, including nucleotide excision repair, is rhythmic. **Immune function** is rhythmic: TLR9 expression and responsiveness oscillate, and both sepsis severity and vaccine response vary with time of administration.

Kruse (2011) identifies the coupling of circadian and cell cycles as the mechanism linking disrupted timing to oncogenesis, and Kruse (2016, 2018) develops this into the position that malignancy is fundamentally a disorder of timing: sustained failure of temporal control removes the constraint separating proliferation from repair, and the resulting genomic changes are consequences rather than causes.

# PART II — CIRCADIAN DISRUPTION

Under a solar cycle every signal that sets the clock agrees. In the modern environment they separate: artificial light after dark, meals at uncoordinated hours, irregular waking. The clock receives contradictory input, the systems it held together drift apart, and synchrony breaks down.

---



## 7. Mechanisms of harm

### 7.1 Loss of temporal segregation

Circadian organisation separates incompatible processes in time. These pairs are normally phase-separated; disruption permits overlap, and overlap raises error rates.


| Process         | Normally separated from   | Consequence of overlap                     |
| --------------- | ------------------------- | ------------------------------------------ |
| DNA replication | DNA repair                | Replication across unrepaired lesions      |
| Anabolism       | Catabolism                | Futile cycling; wasted ATP                 |
| Proliferation   | Inflammation              | Growth amid damage signalling              |
| Feeding         | Insulin sensitivity nadir | Glycaemic load at the least tolerant phase |
| Replication     | Oxidative stress peak     | Mutation during synthesis                  |


Four further consequences follow from the same loss. Repair windows are mistimed, and autophagy and mitophagy fall with them. Nocturnal immune coordination weakens and inflammatory tone becomes chronic. Metabolic gating is lost and glycolytic bias sets in. Rhythmic expression of adhesion molecules is lost, destabilising tissue architecture. Genomic instability, dysregulated metabolism, and chronic inflammation then act together on initiation, growth, invasion, and metastasis.

### 7.2 Signalling at inappropriate phase

Nutrient intake during the melatonin window impairs glucose handling; glucocorticoid elevation at the wrong phase disrupts peripheral entrainment.

### 7.3 Amplitude collapse

Reduced oscillator amplitude propagates to every downstream rhythm, including the NAD⁺/SIRT1 cycle and the rhythm of DNA repair.

### 7.4 Loss of signal acquisition

Kruse (2015, 2018) places this mechanism upstream of the other three. Chronic exposure to short-wavelength light without balancing red and infrared frequencies degrades the photoreceptive apparatus itself, through the chromophore mechanism of 4.3 and through photo-oxidative loss of membrane DHA. Under this account the system loses not only correct timing but the capacity to acquire timing information, and correction requires restoration of the input signal before any downstream intervention can take effect.

### 7.5 The order of failure

**Staging.** Kruse (2015, 2018) adds an ordering claim: circadian failure presents in a fixed sequence, beginning in the organ that carries the clock. Cataract and glaucoma appear first, as the timing apparatus itself degrades; then autoimmune disease; then neurodegeneration; then cancer, at the point where both arms of the feedback loop have collapsed. The clinical corollary is that ophthalmic findings are sentinel signs of systemic timing failure rather than isolated ocular disease.

The sequence is his own and unestablished. It is testable: it predicts that ocular findings precede systemic diagnoses in matched cohorts, and registry data adequate to check that already exist.

**Precedence.** Kruse (2012) makes a second ordering claim, at the level of measurement rather than diagnosis: the flattened or inverted diurnal cortisol profile is the earliest measurable sign of circadian mismatch, appearing before overt metabolic disease. The two orderings run from different organs — the staging sequence begins in the eye, this one in the adrenal output — and Kruse holds both without reconciling them.

The claim is checkable with the protocol in 14. The baseline yields a within-person standard deviation for every metric, which is what fixes how large a change has to be before it counts as movement. Precedence then means the cortisol slope in 12.3 leaves its own baseline interval before any other tracked metric leaves its own, in the same person, under a known change in exposure. Nothing in the published record establishes it.

---



## 8. Cancer

Cancer is in part a failure of temporal separation: when timing signals weaken or misalign, proliferation, metabolism, stress response, and immune evasion overlap in ways that favour malignant growth.

### 8.1 Cell cycle gating

The circadian and cell division cycles are coupled, and the coupling is directional: the circadian oscillator gates progression through the cell cycle rather than the reverse.

CLOCK:BMAL1 drives transcription of *Wee1*, whose product inhibits the CDK1–cyclin B complex and controls the G2/M transition. PER proteins act on Cyclin D1, c-MYC, and p21, coupling G1 progression to circadian phase. *Per1* and *Per2* behave as tumour suppressors in this setting, and *Bmal1* holds a comparable role in several tissues.

Proliferating tissue therefore confines DNA synthesis and mitosis to defined windows. Where gating is lost, replication proceeds at phases when nucleotide supply, chromatin state, and repair capacity are positioned for other work.

Clock gene expression is damped, phase-shifted, or absent in many human tumours, and the degree of loss tracks grade and prognosis: in breast cancer, loss of clock gene expression is associated with tumour progression [[Cadenas 2014](https://pubmed.ncbi.nlm.nih.gov/25485508/)].

### 8.2 Repair at the wrong phase

Nucleotide excision repair, the pathway that removes ultraviolet photoproducts and platinum adducts, oscillates across the day. Its rate-limiting factor XPA is under circadian control at both transcript and protein level, and excision rates in mouse tissue vary several-fold between peak and trough.

Genotoxic exposure therefore carries a mutational cost that depends on the phase at which it arrives. The same dose delivered at the repair trough leaves a larger residual lesion burden than at the peak, which connects mistimed exposure to mutation rate at a fixed exposure.

### 8.3 Melatonin as an oncostatic signal

Melatonin has direct oncostatic activity independent of its role as a phase marker. Signalling through MT1 suppresses tumour uptake of linoleic acid and its conversion to the mitogenic metabolite 13-HODE, removing a growth signal from the tumour.

The tumour-relevant variable is the melatonin content of circulating blood, and the light environment sets it (9.2).

### 8.4 Kruse's account

Kruse (2011) identifies the coupling of circadian and cell cycles as the mechanism linking disrupted timing to oncogenesis. Kruse (2016, 2018) develops this into the position that malignancy is primarily a disorder of cellular timing and energy handling, with mutation accumulating as a consequence of replication and repair proceeding at the wrong phase, and with the light environment acting as an upstream carcinogenic variable through melatonin amplitude, repair timing, and cell cycle gating rather than through direct genotoxicity.

The mechanisms this requires are 8.1, 8.2 and 8.3, each independently established. What he adds is a ranking: these constitute the primary route to malignancy, and a light environment is therefore carcinogenic in the sense a chemical is. The mainstream position holds the same mechanisms as contributory, alongside direct genotoxic, inherited, and infectious routes.

His claim about the order in which timing failure presents clinically is in 7.

---



## 9. Evidence

### 9.1 Epidemiological

**Shift work.** Chronic circadian disruption from long-term night work, irregular sleep–wake timing, or nocturnal light exposure is associated with increased cancer incidence and worse prognosis. IARC classified shift work involving circadian disruption as **Group 2A, probably carcinogenic to humans**, in 2007, on limited human and sufficient experimental evidence [[Straif 2007](https://pubmed.ncbi.nlm.nih.gov/19271347/)], and reinforced the classification in the 2020 monograph. Large cohorts report elevated breast cancer risk in long-term night-shift nurses [[Stevens 2011](https://pubmed.ncbi.nlm.nih.gov/20953253/)].

The human cancer evidence is genuinely mixed: several large subsequent cohorts, including the Million Women Study, found no association. The discrepancy is unresolved, and the exposure metric is the likely reason — years of night work records schedule, not the degree of internal desynchrony achieved. Working group guidance emphasises measuring circadian impact rather than hours worked [[IARC Working Group](https://pubmed.ncbi.nlm.nih.gov/20962033/)].

Metabolic and cardiovascular associations are more consistent than the oncological ones: meta-analyses report elevated type 2 diabetes, obesity, metabolic syndrome, myocardial infarction, and ischaemic stroke, with risk rising by duration of exposure.

**Light at night.** Totally blind women have lower breast cancer incidence than sighted women [[Hahn 1991](https://pubmed.ncbi.nlm.nih.gov/2054403/)], and the reduction follows a gradient with degree of light perception rather than with blindness as a category: women with no conscious light perception show the risk reduction, while those retaining some perception do not [[Flynn-Evans 2009](https://pubmed.ncbi.nlm.nih.gov/19649715/)]. This is the observation least susceptible to the confounding that affects shift work studies, since the exposure differs without the accompanying differences in schedule, sleep, and occupation.

Satellite-measured outdoor light at night co-distributes with breast cancer incidence across countries [[Kloog 2010](https://pubmed.ncbi.nlm.nih.gov/20680434/)]. In a study combining satellite imagery with individual questionnaire data, exposure was associated with both breast and prostate cancer, and the association was concentrated in the short-wavelength fraction rather than in total illuminance [[Garcia-Saenz 2018](https://pubmed.ncbi.nlm.nih.gov/29687979/)]. These are ecological or semi-ecological designs; regional light level covaries with urbanisation, and the spectral finding is the part least explained by that.

Bedroom light at night measured in the sleeping environment is associated with obesity and dyslipidaemia [[Obayashi 2013](https://pubmed.ncbi.nlm.nih.gov/23118419/)] and predicts incident depressive symptoms longitudinally [[Obayashi 2018](https://pubmed.ncbi.nlm.nih.gov/28992236/)], in an elderly cohort in which exposure was recorded directly rather than reported.

**Rest–activity rhythm and mortality.** Blunted or irregular rest–activity rhythms predict reduced survival. In NHANES, low relative amplitude was associated with all-cause, cardiovascular, and cancer mortality, outperforming most traditional predictors [[Xu 2022](https://pubmed.ncbi.nlm.nih.gov/36450759/)]. In cancer patients, wearable-measured disruption — low amplitude, low mesor, high fragmentation — predicted all-cause, cancer-specific, and cardiovascular mortality and outperformed traditional risk factors [[2024](https://pubmed.ncbi.nlm.nih.gov/40930750/)].

Regularity of sleep timing predicts all-cause mortality more strongly than sleep duration (Windred et al., 2024). Low relative amplitude is associated with mood disorder, lower wellbeing, and impaired cognition independently of sleep duration (Lyall et al., 2018). These metrics correspond to stability and amplitude rather than phase, and carry predictive weight that timing measures alone do not.

**Chronotype, social jetlag, and eating time.** Evening chronotype is associated with elevated all-cause mortality and with metabolic and psychiatric morbidity, substantially mediated by the mismatch between endogenous phase and imposed schedule rather than by lateness itself — the epidemiological expression of the phase angle criterion. Social jetlag is associated with adiposity, adverse lipid and inflammatory markers, and depressive symptoms. In a weight loss intervention, participants eating the principal meal later lost less weight on matched energy intake, with no difference in reported intake or activity (Garaulet et al., 2013).

### 9.2 Controlled human disruption

Experimental misalignment of behavioural and circadian time induces cancer-relevant molecular changes within days.

Night-shift schedules cause circadian dysregulation of DNA repair genes and elevated DNA damage in blood [[Cheung 2021](https://pubmed.ncbi.nlm.nih.gov/33638890/)]. Simulated night work misaligns the peripheral blood mononuclear cell transcriptome, damping rhythmic expression across immune and signalling pathways including natural killer cell, Jun/AP-1, and STAT programs [[Kervezee 2018](https://pubmed.ncbi.nlm.nih.gov/29735673/)].

Under forced misalignment on a 28-hour day with diet and sleep duration controlled, subjects showed reduced leptin, elevated glucose and insulin, elevated mean arterial pressure, and in three of eight a postprandial glucose response in the prediabetic range (Scheer et al., 2009). Combined sleep restriction and circadian disruption reduces insulin secretion and raises postprandial glucose (Buxton et al., 2012). The circadian system affects glucose tolerance independently of behaviour, postprandial glucose being approximately 17 per cent higher in the biological evening (Morris et al., 2015).

A perfusion design carries the same logic to a tumour endpoint. Blood collected from women during the biological night, when melatonin is at physiological nocturnal concentrations, suppresses growth in human breast cancer xenografts; blood collected from the same women after exposure to light at night, with melatonin suppressed, stimulates it [[Blask 2005](https://pubmed.ncbi.nlm.nih.gov/16322268/)].

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

**Genetic disruption.** *Per2*-mutant mice show elevated spontaneous tumour incidence and markedly increased lymphoma after ionising radiation, with deficient p53-mediated apoptosis [[Fu 2002](https://pubmed.ncbi.nlm.nih.gov/12372299/)]. In regenerating mouse liver, mitosis is confined to a restricted window each day, and clock disruption abolishes the confinement [[Matsuo 2003](https://pubmed.ncbi.nlm.nih.gov/12934012/)]. BMAL1 disruption promotes metastasis through PAI-1–TGF-β–dependent mechanisms [[BMAL1](https://pubmed.ncbi.nlm.nih.gov/37330661/)]. Disruption-induced tumours show increased stemness, immunosuppression, and metabolic deregulation.

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

> **Inference.** The case rests on convergence across these lines together with the mechanisms of Part I. Cohort associations are the weakest element of the evidence base and the most frequently cited.

---

---



# PART III — CIRCADIAN HEALTH

Humans evolved under a solar cycle: light by day, darkness by night, and eating and activity at fixed hours. Physiology took that periodicity as its input and built programmes on it — melatonin, cortisol, body temperature, glucose handling, cell division.

---



## 10. Defining circadian health

Two accounts. They specify different things to measure.

### 10.1 One quantity

Circadian health is cellular redox state, assayed as mitochondrial heteroplasmy. Phase, amplitude and stability are its readouts and degrade together, so measuring them separately records one failure repeatedly.

Section 2.8 establishes the premise: redox poise is a single intensive quantity coupling all metabolism, and it oscillates in cells that cannot transcribe.

Kruse (2016, 2022) holds this clinically. The ocular, metabolic and oncological presentations are one disease measured at different sites, and they appear in order — ocular findings first, then autoimmunity, neurodegeneration, cancer (7). On this account a patient with normal sleep timing and rising heteroplasmy is already ill, and the timing metrics will not detect it.

Measure: heteroplasmy, plus the exposure record in 12.2.

### 10.2 Five properties

Circadian health comprises entrainment, phase, amplitude, internal alignment and stability. Each can be intact or impaired independently, each fails in a different way, and each is corrected differently.

Measure: all five, separately, per 12.1 and 12.3. Each is defined in 10.2.1 to 10.2.5.

Both are measured. The five dissociate in individuals and a single number does not say what to change; heteroplasmy detects failure before any of the five moves. Repeat assessment separates the accounts: if the five are one quantity their within-person changes co-vary, and if they are not, they do not.

Environmental input — the timing and intensity of light, food and temperature — causes these properties rather than being one of them, and is scored separately in 12.2.

#### 10.2.1 Entrainment

Entrainment is the condition in which the oscillator adopts the period of the environmental cycle and maintains a constant phase relationship to it. In health the expressed period is 24.0 hours and the relationship to the solar day persists across weeks.

Entrainment fails when zeitgeber input is insufficient to correct the difference between τ and 24 hours. The oscillator then free-runs and phase drifts progressively. The condition is characteristic of total blindness, where it presents as non-24-hour sleep–wake disorder, and is uncommon in sighted individuals.

Entrainment is logically prior to the four properties that follow: phase, amplitude, alignment, and stability are defined only for an oscillator held at a fixed period.

#### 10.2.2 Phase

Phase is the position the oscillator occupies within the 24-hour cycle. Two quantities are required to specify it.

**External phase** is the position of the oscillator relative to the solar day, expressed as the interval between DLMO and a solar reference such as sunset.

**Phase angle of entrainment (ψ)** is the interval between the oscillator and the behaviour it governs, conventionally DLMO to habitual sleep onset. In health ψ is approximately 2–3 hours.

The two dissociate, and the distinction determines what is wrong. An individual sleeping from 02:00 to 10:00 with DLMO at 00:00 has a late external phase and a normal ψ: the timing system is internally consistent and conflicts only with convention. An individual sleeping from 23:00 to 07:00 with the same DLMO has a conventional external phase and a ψ of one hour, initiating sleep before the biological night has begun.

Phase is determined jointly by τ and by zeitgeber strength, so a delayed phase recorded under low daytime illuminance reports the light environment as much as the oscillator.

#### 10.2.3 Amplitude

Amplitude is the magnitude of the oscillation, measured as the excursion between peak and trough of any rhythmic output.

Reduced amplitude preserves the phase relationships of the system while diminishing the excursion of every rhythm within it. It is the predominant impairment in populations occupying interior environments, and it is found by measuring excursion — relative amplitude from actigraphy, distal temperature range, the cortisol peak-to-bedtime ratio.

Amplitude and phase do not respond independently to perturbation: a low-amplitude oscillator undergoes a larger phase shift than a high-amplitude one for the same stimulus (2.4).

#### 10.2.4 Internal alignment

Internal alignment is the condition in which the phase intervals between oscillators hold their normal values. It is a property of those intervals rather than of coincidence: the oscillators of a healthy system reach their peaks at different times, in a fixed and reproducible order.

Alignment fails when the intervals change while each oscillator remains internally coherent. Hepatic and adipose oscillators entrain to the feeding schedule while the suprachiasmatic nucleus remains entrained to light, and the two diverge. This is the impairment produced by late feeding, night work, and sleep displaced into daylight.

#### 10.2.5 Stability

Stability is the reproducibility of the system's timing from one day to the next.

The corresponding impairment is elevated variance rather than displaced mean: phase may be correct on average while its day-to-day dispersion is wide. Social jetlag, rotating shift schedules, and irregular sleep–wake patterns produce this state. Regularity of sleep timing predicts all-cause mortality more strongly than sleep duration does (Windred et al., 2024).

Stability is defined over a series of days and has no single-day value.

---



## 11. The internal phase map



### 11.1 The hormonal day

Approximate mean values for adults conventionally entrained to a 23:00–07:00 sleep schedule, drawn from constant-routine and forced-desynchrony studies. Individual variation is substantial, and the reproducible quantity is the interval between markers rather than the clock time of any one of them.


| Variable                              | Approximate phase                                                                     |
| ------------------------------------- | ------------------------------------------------------------------------------------- |
| Melatonin onset (DLMO)                | 21:00, about 2 h before sleep onset                                                   |
| Melatonin peak                        | 03:00–04:00                                                                           |
| Melatonin offset                      | shortly after waking                                                                  |
| Core body temperature minimum         | 05:00, about 2 h before waking                                                        |
| Core body temperature maximum         | 17:00–19:00                                                                           |
| Cortisol nadir                        | around sleep onset                                                                    |
| Cortisol rise begins                  | 03:00, during sleep                                                                   |
| Cortisol peak (awakening response)    | 30–45 min after waking                                                                |
| Growth hormone principal pulse        | first slow-wave sleep episode, shortly after sleep onset                              |
| Prolactin peak                        | mid to late night                                                                     |
| TSH peak                              | late evening to early night                                                           |
| Aldosterone and renin peak            | late night to early morning                                                           |
| Insulin sensitivity maximum           | morning, declining across the day                                                     |
| Blood pressure                        | dips 10–20% during sleep, surges on waking                                            |
| Platelet aggregability and PAI-1 peak | 06:00–09:00                                                                           |
| Airway calibre minimum                | 04:00                                                                                 |
| Bone resorption markers peak          | night                                                                                 |
| Gastric acid secretion peak           | late evening                                                                          |
| Alertness and cognitive throughput    | bimodal, with a post-prandial trough and an evening peak preceding the melatonin rise |
| Epithelial proliferation              | DNA synthesis and mitosis gated to separate restricted windows                        |


These offsets encode an anticipatory program. Cortisol rises hours before waking so that fuel is mobilised before it is required. The temperature minimum precedes waking and anchors the phase response curve, light before it delaying and light after it advancing. Melatonin marks the biological night and simultaneously suppresses insulin secretion, so that the metabolic consequence of a meal depends on whether melatonin is present when it is eaten. The antiphase relationship between melatonin and cortisol is the most visible instance of a general rule rather than a special case.

Healthy variation moves the whole map while preserving its internal structure. Chronotype displaces every marker earlier or later by up to several hours without altering the offsets between them. Seasonal photoperiod changes the width of the melatonin window rather than its relationship to sleep. Within the pacemaker itself, day length is encoded by the degree of phase dispersion among SCN neurons — longer days producing a wider spread of individual neuronal phases — so that phase relationships within the network carry the seasonal signal directly.

Pathology is the alteration of the offsets themselves.

---



### 11.2 The spectral day

The table above maps the day in hormonal terms. Kruse (2016, 2022) maps the same day in spectral terms, and the two run in parallel.


| Interval                         | Spectrum reaching the eye                             | Claimed function                                      |
| -------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| Sunrise                          | Infrared and red dominant; ultraviolet absent         | Sets the phase reference; primes mitochondrial repair |
| Morning, as elevation rises      | Ultraviolet A appears, conventionally from UV index 1 | Drives tryptophan toward serotonin via OPN5           |
| Solar noon, elevation above ~30° | Ultraviolet B available                               | Cutaneous vitamin D synthesis                         |
| Afternoon and sunset             | Ultraviolet withdraws, red and infrared return        | Closes the sequence                                   |
| After dark                       | No light                                              | Serotonin converted to melatonin                      |


The ordering is a real property of atmospheric path length and solar elevation, and the UVB threshold is correct: below roughly 30° elevation, atmospheric absorption removes essentially all of it, which is why UVB is unavailable at high latitude for part of the year.

What is his, and unsupported, is that the *sequence itself* carries information beyond its components — that receiving the same total irradiance in a different order produces a different biological result. Stated as a measurement, this is why 14.2 logs ultraviolet index against outdoor intervals separately from melanopic EDI: melanopic weighting is blind to spectral order by construction.

---



## 12. Metrics



### 12.1 Health

Phase, amplitude, internal alignment and stability are measured directly. Entrainment is read from the phase trend across the recording: a phase that holds its position over weeks.

Five metrics have a reference value.

**Phase angle ψ.** The interval from DLMO to habitual sleep onset, in hours, computed from the evening melatonin series and actigraphy together. In entrained adults DLMO precedes sleep onset by approximately 2 to 3 hours. A short ψ places sleep onset before the biological night begins; a long ψ places it deep inside the biological night.

The reference value is a descriptive norm from small laboratory samples, not an outcome-derived threshold. The outcome evidence for ψ concerns mood: taking the interval from DLMO to mid-sleep, depression severity rises with deviation from an optimum near 6 hours in either direction, and correcting the interval with appropriately timed melatonin improves symptoms (Lewy et al., 2006). No association with mortality or cancer has been established for ψ, and the reason is methodological — the large cohorts that produced the mortality associations for regularity and amplitude used accelerometry, which scales to tens of thousands of participants, while ψ requires a melatonin series that does not. ψ is retained because it separates a late clock from a person sleeping against their own clock, which no accelerometry metric does, and because it is the reference point from which the alignment metrics are measured.

**Sleep Regularity Index.** The probability, on a scale of 0 to 100, that a person is in the same state — asleep or awake — at any given minute as they were exactly 24 hours earlier. Computed from actigraphy. A consistently late sleeper scores high; an erratic sleeper on a conventional schedule scores low. All-cause mortality falls across the population range up to roughly 80 (Windred et al., 2024).

**Relative amplitude.** From actigraphy. Collapse the fortnight into a single average 24-hour activity profile. M10 is the mean activity across the ten consecutive hours with the most movement, L5 the mean across the five consecutive hours with the least. Relative amplitude is (M10 − L5) / (M10 + L5), a number between 0 and 1 measuring how sharply the active day separates from the resting night. Dividing by the sum makes the value independent of how much the person moves. Low values come from inactive days, restless nights, or both, and mark elevated risk of mood disorder, cognitive impairment, and mortality (Lyall et al., 2018; Xu et al., 2022). No fixed cut-point exists; read the value against a cohort distribution matched for age.

**Morning-to-evening glucose ratio.** The postprandial glucose excursion to two identical meals, one taken shortly after waking and one late in the waking day, expressed as early divided by late. The meal is held constant and only its timing varies, so the difference is attributable to the clock. Evening postprandial glucose runs about 17% higher than morning (Morris et al., 2015), placing the expected ratio below 1. A ratio at or above 1 indicates the peripheral tolerance rhythm has flattened or shifted.

**Omega-3 index.** The percentage of EPA and DHA in erythrocyte membrane fatty acids, assayed from a dried blood spot. Above 8% is the desirable band, below 4% the high-risk band (Harris and von Schacky, 2004). Erythrocyte turnover spans roughly 120 days, so the value integrates membrane composition over months and reports the capacity of the system to transduce light. Kruse (2015) treats docosahexaenoic acid as the gain control of the circadian system: melanopsin is a G-protein-coupled photopigment whose transduction depends on a highly unsaturated membrane, and short-wavelength light photo-oxidises that substrate. The gain-control claim is his extrapolation; the assay and its reference values are standard.

ψ, the Sleep Regularity Index, and relative amplitude come from a fortnight of actigraphy, with an evening melatonin series additionally required for ψ. The glucose ratio needs the two-meal probe; the omega-3 index a single dried blood spot.

**Post-illumination pupillary response (PIPR).** The sustained pupil constriction that persists after a blue light stimulus is extinguished, expressed as percentage of baseline diameter at 6 s post-offset. Rod and cone responses decay within about a second; what remains is melanopsin-driven, which makes PIPR the only non-invasive assay of ipRGC function available in clinic. It is attenuated in glaucoma, in seasonal affective disorder, and with age as the crystalline lens yellows and transmits less short-wavelength light.

This measures the input stage directly. The other health metrics read an output rhythm and infer that the input arrived; PIPR reports whether the photoreceptor is working. Kruse (2015, 2018) makes degradation of the photoreceptive apparatus the upstream lesion in his framework, and stratifies patients in his own practice by their pupillary response to blue light — but he never invokes the validated form of the measurement. A cohort with high lifetime indoor exposure and UV-blocked ocular history should show attenuated PIPR against matched outdoor controls; that comparison appears not to have been made.

*Status:* validated instrument with published normative data; no fixed cut-point for circadian purposes. Read against age-matched reference.

### 12.2 Exposure

Environmental input is the cause of circadian state rather than a component of it, and is scored separately. Six environmental quantities are measured, plus one biomarker of integrated exposure.

**1. Daytime melanopic EDI.**
*Measure:* melanopic-capable or spectrally resolved sensor at eye height — spectacle clip or pendant — logging 1-minute epochs through all waking hours. Wrist placement underestimates and requires a correction factor.
*Target:* ≥ 250 lx sustained (Brown et al., 2022).
The melanopsin action spectrum peaks near 480 nm and differs from the photopic curve an ordinary lux meter applies, so a room can be comfortably lit and deliver very little of what the clock reads.

**2. Evening melanopic EDI.**
*Measure:* same sensor; take the median over the three hours before sleep onset.
*Target:* < 10 lx (Brown et al., 2022).
The threshold is this low because the irradiance–response relation is compressive: melatonin suppression is half-maximal around a hundred lux, below ordinary domestic lighting, and the curve is steepest at its low end.

**3. Sleep-period melanopic EDI.**
*Measure:* same sensor, worn or placed at the pillow; median across the sleep period.
*Target:* < 1 lx (Brown et al., 2022).
Light reaching the retina during sleep suppresses melatonin without waking the sleeper.

**4. Day-to-night melanopic contrast.**
*Measure:* log₁₀ of the waking median divided by the sleep median, from the same record.
*Target:* ≥ 4 log units (working target).
The signal the system extracts is contrast, not level. Outdoor daylight against true darkness spans seven to eight log units; a modern interior spans under two. Four is achievable with outdoor daytime exposure and a dark bedroom, and is the quantity both other light targets serve.

**5. Ultraviolet index during outdoor exposure.**
*Measure:* published forecast for the location, or a personal UV sensor, logged against the time of each outdoor interval.
*Target:* ≥ 3 during at least one exposure per day, when season and latitude allow; ≥ 1 as the floor.
Kruse (2016, 2022) anchors exposure to the solar spectrum rather than to illuminance, and this is the measure worth taking from that corpus, because melanopic EDI is blind to it by construction. The melanopsin weighting carries no information about ultraviolet or infrared content, and window glass removes nearly all ultraviolet while leaving the melanopic reading largely intact — so two environments can score identically on measures 1 to 3 and differ completely in the photochemistry they permit. UV index folds solar elevation, season, latitude, and cloud into one number. Index 1 is the practical floor for meaningful UVA; UVB sufficient for cutaneous synthesis requires a solar zenith angle under roughly 60°, corresponding to an index near 3.

**6. Interval from last caloric intake to DLMO.**
*Measure:* timestamped intake log against the melatonin series.
*Target:* positive — intake ends before melatonin onset.
Melatonin suppresses insulin secretion through MT1 and MT2 receptors on the pancreatic beta cell, so the same meal is handled worse inside the melatonin window than outside it, and more so in carriers of the common *MTNR1B* variant. This is the peripheral zeitgeber and the input that governs internal alignment.

Timing for all six is recorded against local solar events as well as clock time. Solar noon varies by up to an hour across a single time zone, daylight saving displaces the population twice a year, and a given clock hour is a different solar elevation in every season (Kruse, 2012, 2016).

**7. Serum 25-hydroxyvitamin D.**
*Measure:* venous or dried blood spot; sample in the same season across assessments.
*Target:* within the laboratory reference interval, stable or rising across the sunlit half of the year. Items 1–6 record light arriving at the sensor. This records ultraviolet-B that reached living tissue and produced a product, integrated over weeks. The two dissociate: sunscreen, clothing, glass, latitude, season, skin pigmentation, and age all sever the link between measured ambient UV index and cutaneous synthesis, so exposure logged without a biomarker can substantially overstate dose delivered. Kruse (2019) treats low vitamin D status as evidence of spectral truncation rather than as a nutrient deficiency to be supplemented, and the distinction matters here: supplementation raises the assay while leaving the exposure it was standing in for unchanged, which destroys its value as a proxy. Record supplement use alongside the value or the metric is uninterpretable.

### 12.3 Tracked quantities

These have no validated diagnostic cut-point. Each still carries a target, so that each assessment has a direction to move in; the targets are working values, derived from reference ranges or from what is physically achievable rather than from outcome studies.

**Interdaily stability.** From actigraphy. Target > 0.6.

**Diurnal cortisol slope.** From the four-sample series. Target: bedtime cortisol at the low end of the assay reference range, and a peak-to-bedtime ratio above 5. Flatter slopes predict worse outcomes across a wide range of conditions (Adam et al., 2017); the ratio is the tracking quantity.

**Glycaemic variability.** From CGM. Target: coefficient of variation ≤ 36%, the consensus boundary for stable glycaemia.

**Distal temperature amplitude.** Daily peak-to-trough from the wrist sensor. Target: increase from the individual's own baseline.

**Sleep respiratory quotient.** The ratio of carbon dioxide produced to oxygen consumed, by indirect calorimetry, sampled early and late in the sleep period. Glucose oxidation yields ~1.0 and fat oxidation ~0.7, so the overnight decline reports the switch to fat as the dominant substrate. Target: a fall across the sleep period, and an increase in that fall from the individual's own baseline. A flat nocturnal RQ indicates the metabolic switch is not occurring. Kruse (2025) proposes melatonin as the driver of this shift; the shift itself is established physiology and is measurable independently of that mechanism.

**TSH and leptin bedtime-to-waking ratios.** From the capillary series. Target: above 1, and increasing across assessments. Both rhythms flatten under misalignment.

**Peripheral clock-gene acrophase minus DLMO.** From follicle sampling against the melatonin series. Target: unchanged between assessments. A shift indicates the peripheral oscillator has moved relative to the pacemaker.

**Latency from waking to first exposure above 250 lx.** From the light record. Target: under 60 minutes.

---



## 13. Raw measurements

Every metric in section 12 is computed from these streams. Seven run continuously; five are collected once or on a short schedule.

### 13.1 Acceleration

**Device.** Triaxial accelerometer  
**Placement.** Non-dominant wrist  
**Sampling.** Raw 25–100 Hz, or 30–60 s epochs  
**Duration.** ≥14 days; 28 days preferred  
**Timing.** Continuous, including sleep  

- Record raw where storage allows. Raw permits recomputing any epoch length later; binned data does not.
- Include both work days and free days. The regularity metrics require both.
- Detect non-wear and exclude those intervals. A removed device reads as perfect rest and inflates relative amplitude and the Sleep Regularity Index.



### 13.2 Light

**Device.** Melanopic-capable or spectrally resolved sensor  
**Placement.** Eye level — spectacle clip or pendant  
**Sampling.** 1 min epochs, mean and maximum  
**Duration.** ≥14 days  
**Timing.** All waking hours, plus the sleep period at the pillow  

- Record melanopic EDI. A photopic lux meter cannot produce the thresholds in 12.2.
- Retain the full spectrum where the sensor resolves it. Equal melanopic EDI with a different short-to-long ratio drives the pathway differently.
- Store mean and maximum per epoch. The dose–response saturates; the mean alone misrepresents a brief outdoor excursion.
- Mount at eye level. Interiors are lit for horizontal task planes, and a wrist sensor is shadowed by sleeve and posture. Wrist placement requires a documented correction factor.
- Sensor range: 100,000 lx without saturating, resolution below 1 lx.
- Confirm epoch length and stored statistic before recording. Firmware binning cannot be undone.



### 13.3 Skin temperature

**Device.** Wrist thermistor; second sensor for the distal–proximal gradient  
**Placement.** Wrist, plus ankle or infraclavicular chest  
**Sampling.** 1 min epochs at 0.1 °C  
**Duration.** ≥14 days  
**Timing.** Continuous  

- Add the second sensor where the gradient is required.
- Log ambient temperature alongside. The signal moves with room temperature and bedding.
- For phase without masking, use an ingestible core capsule for one 24-hour period.



### 13.4 Cardiac

**Device.** PPG or ECG patch  
**Placement.** Wrist or chest  
**Sampling.** Beat-to-beat intervals  
**Duration.** ≥14 days  
**Timing.** Continuous  

- Extract the nocturnal heart rate minimum, its clock time, and the amplitude of the HRV rhythm.
- Log alcohol, illness, and training load. Each displaces both.



### 13.5 Interstitial glucose

**Device.** Continuous glucose monitor  
**Placement.** Upper arm or abdomen  
**Sampling.** 1–5 min  
**Duration.** ≥14 days  
**Timing.** Continuous, concurrent with the intake log  

- Do not read the free-living 24-hour curve as a rhythm. Its acrophase reports when the person ate. Use two windows instead.
- **Overnight fasted window.** Take the nocturnal nadir and the onset of the pre-waking rise. Valid only where time since last intake exceeds 6 hours.
- **Standardised probe.** Two identical meals, one within an hour of waking, one 10–12 hours later, on separate days. The ratio of the two postprandial excursions is the amplitude of the tolerance rhythm. Draw capillary insulin at 0, 30, 60, and 120 min to separate secretion from sensitivity.



### 13.6 Intake log

**Device.** Photograph-based log  
**Sampling.** Every caloric event, timestamped  
**Duration.** ≥14 days  
**Timing.** At the moment of intake  

- Photograph at the time. Do not reconstruct from recall.
- Timing governs; composition is secondary.
- Required covariate. The fasted glucose window is uninterpretable without time of last intake.



### 13.7 Ultraviolet index

**Device.** Published forecast for the location, or a personal UV sensor  
**Sampling.** Once per outdoor interval  
**Duration.** ≥14 days  
**Timing.** Start and end of every outdoor interval  

- Log at the time. The melanopic record carries no ultraviolet information, so the index cannot be recovered afterwards.



### 13.8 Capillary blood

**Device.** Point-of-care immunoassay analyser  
**Sampling.** 10–100 µL per assay  
**Duration.** 3 sampling days  
**Timing.** Per the schedule below; all series end at sleep onset  


| Analyte   | Series                                                                  | Yields                                |
| --------- | ----------------------------------------------------------------------- | ------------------------------------- |
| Melatonin | Every 30–60 min, from 6 h before habitual sleep onset until sleep onset | DLMO; central phase                   |
| TSH       | On waking, midday, and at bedtime                                       | Evening-to-morning ratio              |
| Cortisol  | Waking, +30–45 min, midday, bedtime, over 3 days                        | Diurnal slope                         |
| Insulin   | 0, 30, 60, 120 min after each probe meal                                | Tolerance rhythm, secretion component |
| Leptin    | On waking and at bedtime                                                | Evening-to-morning ratio              |


**Melatonin.** Plasma concentrations run roughly threefold saliva, so the DLMO threshold is approximately 10 pg/mL against 3–4 pg/mL in saliva; fix one medium and one threshold and hold both across repeat assessments. Sample under illumination below 10 lux with no emitting screens. Where the analyser menu excludes melatonin, collect dried blood spots or saliva across the same schedule for laboratory assay.

**TSH.** TSH is lowest in the late morning and rises through the evening. Sample on waking, at midday, and at bedtime, and report the bedtime-to-waking ratio.

**Cortisol.** Serum reports total cortisol and saliva the free fraction; either supports the slope. Take waking time from the accelerometer rather than self-report, since the first two samples are defined against it.

**Analyser requirements.** Rhythm work measures change within a person, so within-run precision binds harder than absolute accuracy: specify coefficient of variation under 10% across the physiological range of each analyte, and verify it at the low end, where melatonin and nocturnal TSH sit. Capillary volume at or under 100 µL per assay keeps a 10-sample evening series tolerable. Time-to-result under 20 minutes permits sampling decisions during the series. Confirm the menu covers melatonin, TSH, cortisol, insulin, and leptin before purchase; melatonin is the analyte most often absent.

- Sample melatonin below 10 lux with no emitting screens. Plasma runs roughly threefold saliva: the DLMO threshold is ~10 pg/mL in plasma, 3–4 pg/mL in saliva. Fix one medium and one threshold and hold both across assessments.
- Where the analyser menu excludes melatonin, collect dried blood spots or saliva on the same schedule.
- Cortisol: serum gives total, saliva the free fraction. Either supports the slope. Take waking time from the accelerometer, not self-report.
- Analyser: coefficient of variation under 10% across the physiological range, verified at the low end. ≤100 µL per assay. Result under 20 minutes.
- Confirm melatonin is on the analyser menu before purchase. It is the analyte most often absent.



### 13.9 Dried blood spot

**Device.** Collection card, finger prick, posted to a laboratory  
**Sampling.** Single sample, two assays  
**Duration.** One day  
**Timing.** Any day for omega-3; same season across assessments for vitamin D  

- One card, two assays. Request them together.
- **Omega-3 index.** No fasting, no timing constraint. Erythrocyte membrane composition does not vary across the day.
- **25-hydroxyvitamin D.** Record supplement use on the card. Supplementation raises the value without changing the exposure it stands proxy for.



### 13.10 Follicle

**Device.** Plucked scalp or beard follicles  
**Sampling.** 3 samples  
**Duration.** One day  
**Timing.** Spread across waking hours  

- Assay *PER3*, *NR1D1*, and *NR1D2*.
- Timestamp each sample against the melatonin series. The alignment metric in 12.3 is computed against DLMO.
- A blood transcript panel substitutes, from the capillary stream.



### 13.11 Pupillometry

**Device.** Chromatic pupillometer, blue stimulus near 480 nm  
**Placement.** Monocular stimulus, both eyes recorded  
**Sampling.** Continuous diameter through stimulus and ≥30 s after offset  
**Duration.** Single session  
**Timing.** Afternoon, after ≥10 min dark adaptation; same hour on repeat  

- Report diameter at 6 s post-offset as a percentage of dark-adapted baseline.
- Record a red stimulus in the same session as control. Cone-driven constriction recovers within about a second; a normal red response with an attenuated blue one localises the deficit to the melanopsin pathway rather than the iris or the efferent limb.
- Exclude: mydriatic or anticholinergic use, uncorrected media opacity.
- Record age. Pupil size falls with age.



### 13.12 Indirect calorimetry

**Device.** Metabolic cart or ventilated canopy  
**Sampling.** 20–30 min of steady-state gas exchange per period  
**Duration.** Two periods in one night  
**Timing.** Early and late in the sleep period  

- Standardise the evening meal in composition and timing. Substrate availability at sleep onset sets the starting quotient.
- Record any nocturnal waking. The measurement is invalid across an arousal.
- Use a canopy, not a mask. Better tolerated overnight.

---



## 14. Acquisition



### 14.1 Baseline

Four weeks, with no intervention attempted and no deliberate change to routine.

Continuous streams start on day 0 and run without interruption. The episodic panel is collected twice, in week 2 and week 4.


| Day   | Action                                                                                      |
| ----- | ------------------------------------------------------------------------------------------- |
| 0     | Fit wearable and CGM; begin intake log and UV log                                           |
| 8     | Probe meal, early; capillary insulin series                                                 |
| 10–12 | Capillary cortisol, 4 per day                                                               |
| 12    | Probe meal, late; capillary insulin series                                                  |
| 13    | TSH and leptin: waking, midday, bedtime                                                     |
| 14    | Melatonin series, evening to sleep onset, under 10 lux; follicle sampling; dried blood spot |
| 22    | Probe meal, early                                                                           |
| 26    | Probe meal, late                                                                            |
| 27    | TSH and leptin                                                                              |
| 28    | Melatonin series; follicle sampling                                                         |


Four weeks rather than two for three reasons. The regularity metrics need several scheduled and free days to be representative. The drift estimate for entrainment improves with the square of the recording length. And two determinations of each episodic marker, taken two weeks apart with nothing changed between them, are what establish how much each measurement varies on its own.

### 14.2 What the baseline produces

For every metric, a mean and a within-person standard deviation.

The second quantity is what makes later measurements interpretable. Change is detectable only above the noise of the measurement itself, and the smallest real difference between two single determinations is approximately 2.77 times the within-person standard deviation. A difference exceeding that band is what counts as change. Metrics with no external reference — the whole of section 12.3 — are usable from this point onward, because the individual's own baseline and its spread now supply the comparison.

Where the two baseline determinations of an episodic marker disagree by more than expected, the marker is repeated before any intervention begins rather than averaged.

### 14.3 Season

A baseline is specific to the photoperiod in which it was taken. Season moves phase, amplitude, and the achievable daytime light dose, and a winter measurement compared against a summer baseline will show change that has nothing to do with the intervention.

Repeat the full panel near both solstices and both equinoxes through the first year. From the second year, compare each assessment against the baseline from the matching season. Express every phase metric against sunrise and sunset in addition to clock time, which removes part of the seasonal shift before comparison.

### 14.4 Continuing measurement

Wearable streams run continuously and indefinitely. A month is comparable to other months when at least 16 hours of wear are recorded on at least 20 days; below that the metrics move for reasons of data completeness rather than physiology.

CGM runs for one 14-day block per quarter unless continuous wear is tolerated. The two probe meals sit inside that block.

The episodic panel repeats quarterly, aligned to the seasonal points, and again before and after any deliberate change to the light environment, the schedule, or the eating window.

### 14.5 Keeping a long series comparable

Over years, the largest threat to the record is the instrument rather than the physiology.

**Replace devices with overlap.** Run the old and new device concurrently for at least 14 days, compute the offset between them on every shared metric, and carry that offset forward. A device swapped without overlap breaks the series at that point.

**Hold the assay constant.** Use the same laboratory and the same method for melatonin, omega-3, and the capillary analytes. Record the lot number. A change of method requires the same overlap treatment as a change of device.

**Record the configuration.** Device model, firmware version, sensor placement, epoch length, and analysis software version, stored with every segment.

**Store raw data, not summaries.** Metric definitions and algorithms change. Raw acceleration, raw light, and raw interstitial glucose permit every metric to be recomputed on a consistent definition across the whole series; stored summary values do not.

---



## 15. Limits

The profile characterises the central pacemaker, one peripheral oscillator, and the behavioural and environmental variables that drive both. It does not resolve tissue-specific phase in liver, muscle, or immune cells, which requires biopsy or a validated tissue-specific transcript panel. Rhythmic transcript sets are largely non-overlapping between organs, so a normal glucose rhythm establishes hepatic and pancreatic alignment and does not generalise to other tissues.

Several amplitude metrics have no population threshold and are read against the individual's own baseline, so a first assessment establishes a reference rather than a verdict: a decline from an unmeasured prior state reads as normal while it remains within the population range. Repeated assessment at intervals is the only correction.

The observation window is fourteen days. Seasonal variation in photoperiod, amplitude, and phase is therefore not captured by a single assessment, and comparison across assessments requires matching for season and latitude.

---



# APPENDICES

---



## Kruse attribution index

Sections in which each year's claims are cited.

- **2011** — sections 6, 8
- **2012** — sections 4, 6, 7, 12
- **2013** — sections 2
- **2015** — sections 2, 4, 6, 7, 12
- **2016** — sections 4, 6, 8, 10, 11, 12
- **2018** — sections 2, 4, 6, 7, 8, 12
- **2019** — sections 4, 6, 12
- **2022** — sections 4, 6, 10, 11, 12
- **2023** — sections 2
- **2025** — sections 12
