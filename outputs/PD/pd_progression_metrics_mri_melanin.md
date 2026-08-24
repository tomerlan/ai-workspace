# Parkinson's Disease: Progression Metrics

---

## How PD Progresses

Parkinson's disease (PD) begins years or decades before motor symptoms appear. The prodromal phase — defined by preclinical tissue pathology — includes hyposmia (reduced sense of smell), constipation and gastrointestinal dysfunction, REM sleep behavior disorder (RBD, acting out dreams), depression and anxiety, and autonomic instability. These reflect degeneration in the olfactory system, enteric nervous system, and brainstem nuclei before the substantia nigra pars compacta (SNpc) is substantially involved. Pathological staging models (Braak staging) place olfactory and brainstem involvement at stage 1–2, with SNpc at stage 3 and cortical spread at stages 4–6.

Motor symptoms appear clinically only after approximately 50–70% of SNpc dopamine neurons are lost and striatal dopamine is depleted by a similar fraction. The cardinal signs — bradykinesia (slowness of movement), resting tremor, and rigidity — appear first, usually asymmetrically. Over years: gait slows, postural instability emerges, freezing of gait develops. Medication complications (dyskinesias, wearing off) typically appear after 4–6 years of levodopa therapy.

Non-motor progression is continuous and not secondary to motor change. Cognitive decline accelerates in the middle-to-late stages and can reach dementia (Parkinson's Disease Dementia, PDD) in a substantial fraction of patients, typically 10+ years in. Autonomic failure — orthostatic hypotension, urinary dysfunction — compounds disability. Psychosis emerges with disease burden and medications.

Tissue pathology (measured by imaging and biofluids) progresses from the start, ahead of symptoms, and continues throughout. The rate of dopaminergic terminal loss in the striatum slows over time (fastest in early disease, on the order of 10–12% per year in the putamen by DAT-SPECT, then decelerating). Nigral iron accumulation and neuromelanin-rich neuron loss also continue throughout.

---

## Two Axes of Measurement

**Symptoms** change on a short timescale (hours to days from medication, sleep, and mood) while also worsening irreversibly over months to years. High-frequency symptom measurement captures real variation — good days and bad days, ON/OFF medication cycling, sleep-related fluctuations — which can be averaged into a progression slope with enough data.

**Tissue pathology** (imaging and biofluids) changes slowly and continuously. The noise in a single measurement is often comparable in magnitude to the expected true change over weeks or months. High-frequency imaging in most contexts is measuring the scanner/assay, not the biology. The exceptions are: (1) a short-term intervention expected to produce measurable tissue change within weeks, and (2) deliberately accumulating repeated measurements to characterize the noise floor for a study design.

---

## Symptom-Level Measurements

The metrics below are ordered by how central they are to PD progression research — from primary endpoints used in virtually every trial to specialized or domain-specific tools.

---

### MDS-UPDRS Part III — Motor Examination
*Tier 1 — Primary endpoint in virtually every PD progression study and disease-modifying trial.*

**Movement Disorder Society Unified Parkinson Disease Rating Scale (MDS-UPDRS) Part III** is a structured examiner-administered rating of motor signs: bradykinesia (18 items), resting tremor, rigidity, gait, postural stability. Scored 0–132, higher = worse. It is the primary motor outcome in most progression studies.

**Pathological correlate.** Aggregate functional consequence of nigrostriatal dopaminergic denervation. Part III does not measure tissue directly — it measures the motor system output downstream of dopamine loss. Faster Part III worsening predicts faster striatal DAT-SPECT decline in cohort data.

**Principle.** Semi-structured clinical exam; each item scored 0–4 on defined anchor criteria. Standardized in the OFF medication state (≥12 hours without dopaminergic medication) for progression work, to remove symptom masking from therapy. ON-state scores are useful for treatment response but confound disease progression measurement.

**Signal and noise.** Within-person variability over days is substantial: sleep, stress, pain, and physical activity from the prior day all affect performance. The test–retest standard deviation in stable patients over short intervals is approximately 2–4 points. Annual progression rate in early PD is approximately 2–4 points/year. A 5-point worsening from baseline (OFF) is the established threshold for clinically meaningful motor progression.

**Maximum useful sampling frequency.** **Weekly standardized OFF-state Part III** is the biological maximum that adds progression signal. Daily would not add information — repeated same-day motor exams saturate within a single OFF window, and day-to-day within-person biological variation is not interpretable at that resolution. At weekly intervals, each exam is genuinely independent and contributes to slope estimation. More weekly measurements → tighter confidence interval on the progression slope, compressing the time needed to detect change.

---

### Wearable Sensors and Digital Motor Biomarkers
*Tier 1 — The highest-frequency measurement domain; increasingly co-primary in modern trials. The only modality where daily or continuous data genuinely outperforms conventional clinic visits.*

Accelerometers, gyroscopes, and smartphone microphones passively or semi-passively capture gait kinematics, tremor, bradykinesia, and activity throughout the day.

**Pathological correlate.** Not a direct tissue measure. Captures the real-world motor output of the dopaminergic and non-dopaminergic motor system throughout the day — including medication ON/OFF cycles, circadian motor variation, and slow irreversible motor decline. Correlates with MDS-UPDRS motor scores and DAT-SPECT (Specific Binding Ratio) in cohort data.

**Principle.** Triaxial accelerometry at 50–200 Hz captures step regularity, stride length, velocity, and tremor frequency/amplitude. Algorithms extract composite bradykinesia and gait scores. Derived daily summary metrics (mean stride velocity, tremor power, activity counts) are more stable than individual observations.

**Signal and noise.** Individual measurements are noisy. The high-frequency strategy is statistically sound: accumulate many daily observations, aggregate weekly or monthly means, and fit a regression slope over months. The noise averages down as more observations accumulate, allowing detection of slow progression that a single clinic visit could not resolve.

**Maximum useful sampling frequency.** **Continuous (24/7)** is the theoretical maximum and is technically feasible with modern wrist-worn sensors. Practically, daily summary statistics are the natural resolution. This is the domain where high-frequency measurement most clearly adds value over conventional annual clinic visits.

---

### MDS-UPDRS Parts I, II, IV — Non-Motor, Functional, and Complications
*Tier 1 — Standard co-endpoints alongside Part III in all major trials and cohort studies.*

**Part I** (13 items, 0–52) captures non-motor burden: cognitive impairment, hallucinations/psychosis, depressed mood, anxious mood, apathy, dopamine dysregulation syndrome, sleep problems (insomnia, daytime sleepiness), pain, and urinary symptoms. **Part II** (13 items, 0–52) is patient-reported motor function in daily life. **Part IV** (6 items, 0–24) captures motor complications — dyskinesia duration/disability, wearing off duration, and painful OFF dystonia.

**Pathological correlate.** Part I reflects multi-system degeneration beyond the nigrostriatal axis — locus coeruleus, raphe, pedunculopontine nucleus, cortex, autonomic ganglia. Part II integrates dopaminergic and non-dopaminergic disability. Part IV reflects the pharmacological consequences of chronic dopamine replacement on a sensitized nigrostriatal system.

**Signal and noise.** Parts I and II are more susceptible to state and recall than Part III. Mood, sleep the prior night, medication timing, and caregiver input all affect scores. Longitudinal trends are real on a 6–12 month scale.

**Maximum useful sampling frequency.** **Weekly** for Parts I and II — the biological signals here genuinely vary on weekly timescales. Mood, sleep quality, autonomic symptoms, and motor ADL performance are not stable week-to-week in PD; they are influenced by sleep the prior nights, autonomic fluctuations, and medication cycling. Weekly structured rater-administered assessment captures this variation and contributes to slope estimation. Part IV: **weekly** once complications are established and fluctuating; bi-weekly if dyskinesias are stable. Below weekly, within-day pharmacokinetic variation swamps the progression signal.

---

### PDQ-39 — Quality of Life
*Tier 1 — Standard quality-of-life endpoint required in most intervention trials.*

**Parkinson's Disease Questionnaire (PDQ-39)** is a 39-item patient-reported instrument covering 8 domains: mobility, activities of daily living, emotional wellbeing, stigma, social support, cognition, communication, bodily discomfort. Each item rates frequency of difficulty (never/occasionally/sometimes/often/always or unable to do).

**Pathological correlate.** Integrative measure of total disability burden — motor, non-motor, and psychosocial. Not a direct tissue readout.

**Signal and noise.** State and context dependent. Mood at the time of completion affects most domains. Longitudinal change is real on a 6–12 month scale.

**Maximum useful sampling frequency.** **Monthly** is the biological ceiling. PDQ-39 integrates experience over the preceding weeks — shorter intervals would sample the same experiential window repeatedly, adding recall overlap rather than new information. The bottleneck is not administration but what the instrument is measuring: cumulative disability burden over a period, not a point-in-time reading.

---

### MoCA — Cognitive Screening
*Tier 2 — Standard secondary outcome; central to tracking the cognitive progression dimension.*

**Montreal Cognitive Assessment (MoCA)** is a 30-point multidomain brief cognitive test covering memory, attention, executive function, visuospatial processing, language, and orientation. ~10 minutes to administer.

**Pathological correlate.** Overall cognitive integrity. In PD, cognitive decline correlates with cortical Lewy pathology, cholinergic (nucleus basalis) degeneration, and dopaminergic losses in the mesocortical system. Transition from mild cognitive impairment (MoCA 17–25) toward dementia (MoCA <17) is a major milestone in PD progression.

**Signal and noise.** Cross-sectional sensitivity is good. The critical limitation for high-frequency use: **practice effects**. Patients remember specific test items (the drawing, the word list) and perform better on repetition without any true cognitive improvement, masking decline or creating apparent improvement. Practice effects are largest in the first few administrations and can persist across years.

**Maximum useful sampling frequency.** **Quarterly at the absolute maximum**, and only with alternate forms (parallel versions). This is a biological constraint, not a logistical one: patients remember specific test items — the drawing, the word list, the clock — and perform better on repetition independent of any true cognitive change. Practice effects persist for months and are substantial enough to mask genuine decline or create apparent improvement. No amount of added resources removes this; it is intrinsic to the nature of the test. Quarterly with form rotation is the biological floor below which MoCA data is not interpretable as progression.

---

### SCOPA-AUT — Autonomic Dysfunction
*Tier 2 — Standard secondary; autonomic degeneration is among the earliest PD features.*

**Scales for Outcomes in Parkinson's Disease — Autonomic Dysfunction (SCOPA-AUT)** is a 25-item patient questionnaire covering gastrointestinal (salivation, swallowing, nausea, constipation), urinary (urgency, frequency, incontinence), cardiovascular (orthostatic symptoms), thermoregulatory (sweating), and sexual domains.

**Pathological correlate.** Autonomic degeneration in PD involves the dorsal motor nucleus of the vagus (parasympathetic), sympathetic ganglia, and enteric nervous system. Cardiac sympathetic denervation (measurable by MIBG scintigraphy) and constipation from enteric neurodegeneration are among the earliest PD-related changes. Orthostatic hypotension reflects sympathetic cardiovascular denervation.

**Signal and noise.** Patient-reported and varies with hydration, diet, medications, and time of day. Longitudinal trend is real but changes slowly.

**Maximum useful sampling frequency.** **Weekly** for full SCOPA-AUT — autonomic symptoms (GI, urinary, cardiovascular) have genuine week-to-week biological variation linked to autonomic tone, diet, hydration, and medication timing. Weekly structured assessment adds to slope estimation. For targeted single-domain tracking (e.g., constipation frequency, orthostatic symptoms): **daily** diary is biologically valid and more sensitive than any composite instrument — bowel movements are a discrete daily event, orthostatic symptoms occur at specific transition moments.

---

### GDS-15 — Depression
*Tier 2 — Standard secondary; depression is one of the most prevalent and disabling non-motor features of PD.*

**Geriatric Depression Scale (15 items, GDS-15)** is a patient self-report questionnaire with 15 yes/no items focused on mood-related experiences over the past week. Scores 0–15; ≥5 suggests depression.

**Pathological correlate.** Depression in PD reflects degeneration in the locus coeruleus (noradrenergic), dorsal raphe nucleus (serotonergic), and mesocorticolimbic dopaminergic projections — distinct from the nigrostriatal system responsible for motor signs.

**Signal and noise.** Mood is genuinely state-dependent — bad nights, life events, and pain all affect scores. Genuine progression of depressive symptoms occurs over months.

**Maximum useful sampling frequency.** **Weekly** — mood in PD is genuinely labile on this timescale, driven by sleep quality, pain, autonomic symptoms, and dopaminergic fluctuations. Weekly GDS-15 captures the trajectory of depressive symptom burden rather than a single-day reading. The fact that variability at weekly intervals is partly state-driven is not a reason to sample less frequently — it is a reason to accumulate more measurements and fit a slope. Daily mood ratings (single-item visual analog or brief 3-item subset) add even more data points; the GDS-15 construct requires a "past week" recall frame, so the instrument itself is calibrated to weekly.

---

### PDSS-2 / RBD Questionnaires — Sleep
*Tier 3 — Important for prodromal and sleep-specific research; less central in standard motor progression trials.*

**Parkinson's Disease Sleep Scale version 2 (PDSS-2)** is a 15-item patient-reported rating of sleep quality over the past week: night-time motor symptoms, hallucinations, urinary urgency, restlessness, pain, and RBD-related symptoms.

**REM sleep behavior disorder (RBD)** questionnaires capture the symptom of acting out dreams — vocalizing, moving, or fighting during REM sleep, reflecting loss of normal REM atonia. RBD is among the strongest prodromal markers of PD and synucleinopathies, often preceding motor diagnosis by years.

**Pathological correlate.** Sleep disruption in PD reflects brainstem degeneration (pedunculopontine nucleus, subceruleus, locus coeruleus). RBD specifically maps to degeneration of REM-atonia-controlling nuclei in the pontine tegmentum, which fall within Braak stage 2 pathology.

**Signal and noise.** Subjective and night-to-night variable. In-lab polysomnography (PSG) is the gold standard for RBD — providing full EEG, EMG (electromyography), and video confirmation of REM behavior. Home PSG devices (Alice NightOne, Nox A1) achieve near-lab quality for REM-related metrics without the ecological validity problem of sleeping in a laboratory.

**Maximum useful sampling frequency.** PDSS-2 questionnaire: **weekly** — covers "the past week" by design and captures genuine night-to-night autonomic and motor sleep variation. Home PSG: **nightly** is biologically valid and technically feasible; this is the biological maximum. Sleep architecture (REM duration, sleep efficiency, limb movement index) varies night-to-night with disease state and responds to pharmacological and behavioral interventions within days. Continuous nightly home PSG or wearable EEG is the richest high-frequency data stream in this domain.

---

### Freezing of Gait — FOG-Q
*Tier 3 — Domain-specific to mid-to-late stage PD; not relevant in early disease.*

**Freezing of Gait Questionnaire (FOG-Q)** is a 6-item patient-reported measure of the frequency and severity of FOG episodes — sudden brief inability to initiate or continue stepping. Modified versions (mFOG-Q) refine temporal estimates. Objective FOG can also be measured by accelerometer gait analysis.

**Pathological correlate.** FOG reflects degeneration of the pedunculopontine nucleus and related brainstem gait-control circuitry, combined with striatal dopaminergic loss. It emerges in mid-to-late disease, worsens with increasing striatal denervation and anticholinergic burden.

**Signal and noise.** Highly state-dependent: FOG worsens in OFF medication state, with anxiety, narrow spaces, and cognitive dual-tasking. Day-to-day and week-to-week variability is high. Wearable-based objective FOG detection (step-time variability) can be continuous.

**Maximum useful sampling frequency.** Questionnaire: monthly. Wearable FOG detection: continuous.

---

### Hoehn & Yahr — Disease Staging
*Low priority for progression tracking — useful for coarse staging and cohort characterization only.*

A 5-level staging scale (1 = unilateral mild; 5 = wheelchair/bed-bound), with half-stages 1.5 and 2.5. Describes the broad disability stage rather than tracking fine-grained change.

**Pathological correlate.** Reflects cumulative dopaminergic and non-dopaminergic disability. Stage 3 marks bilateral symptoms with impaired postural reflexes; stage 4 requires assistance to walk; stage 5 is full dependency.

**Signal and noise.** Coarse ordinal scale — many patients remain on one stage for years. Not sensitive to early or fine-grained change. Useful for cohort characterization.

**Maximum useful sampling frequency.** Annual or less. Not a high-frequency metric.

---

## Tissue Pathology Measurements

The metrics below are ordered by how widely they are used and validated in PD progression research. NM-MRI and iron MRI rank high in this section due to their direct relevance to the neuromelanin/iron axis.

---

### DAT-SPECT — Dopamine Transporter Imaging
*Tier 1 — The most validated and widely used imaging biomarker of nigrostriatal degeneration progression.*

**DAT-SPECT** (dopamine transporter single photon emission computed tomography) uses the radioligand ¹²³I-ioflupane (marketed as DaTSCAN) to image presynaptic dopamine transporter (DAT) density on nigrostriatal terminals in the striatum.

**Pathological correlate.** Loss of presynaptic dopaminergic terminals in the striatum — specifically the putamen (earliest and most affected in PD) and caudate. DAT-SPECT does not image cell bodies in the SN; it measures the surviving terminal field in the striatum. Putamen-to-occipital specific binding ratio (SBR) falls with the same timeline as nigrostriatal degeneration. DAT-SPECT is among the most validated longitudinal biomarkers of nigrostriatal disease progression.

**Principle.** ¹²³I-ioflupane is injected intravenously; SPECT imaging is performed approximately 3–4 hours later after redistribution. The tracer binds to DAT on dopaminergic axon terminals. SBR = (striatal counts − background) / background. Putaminal SBR shows faster and earlier decline than caudate SBR in PD. Dopaminergic imaging shows a characteristic pattern: reduced comma-shaped striatal uptake, asymmetric and most pronounced posterolaterally in the putamen.

**Signal and noise.** Annual putaminal SBR decline in early PD: approximately 10–12%/year (decelerating over time as the terminal field depletes). Test–retest variability on the same scanner: approximately 5–8% SBR. This means a 6-month interval in early disease (expected ~5–6% change) is near the noise floor; 12-month intervals provide more reliable progression signal. The scan involves radiotracer exposure, which constrains repeat frequency.

**Maximum useful sampling frequency.** **6 months** in an early-disease intervention study where a large dopaminergic effect is expected is technically reasonable and has been done. **12 months** is the more common choice for natural history and standard trials. Weekly or monthly DAT-SPECT has no progression-signal value and involves unnecessary radiation.

---

### Neuromelanin-Sensitive MRI (NM-MRI)
*Tier 2 — Mechanistically central: directly images the SNpc cell population lost in PD. Increasingly used as a research biomarker; the most relevant imaging modality for the neuromelanin/iron axis.*

**Pathological correlate.** Loss of neuromelanin-rich dopaminergic neurons in the SNpc and noradrenergic neurons in the locus coeruleus (LC). The SNpc appears macroscopically depigmented at PD autopsy, and NM-MRI provides a non-invasive in vivo proxy for this cell loss. The NM-MRI signal is not a pure measure of neuromelanin concentration — it reflects the tissue microenvironment of neuromelanin-containing cells, primarily through magnetization transfer properties and paramagnetic T1 shortening from neuromelanin–iron complexes.

**Principle.**

*Contrast mechanism.* An off-resonance radiofrequency (RF) pulse is applied before the image readout, selectively saturating protons that are bound to macromolecules (the "bound pool"). Saturation is then transferred to nearby free water protons, reducing the free water signal in proportion to the macromolecular content of the tissue — the magnetization transfer (MT) effect. The key anatomical fact is that the SNpc sits embedded within and adjacent to **heavily myelinated white matter** structures (primarily the crus cerebri). The crus cerebri has very high macromolecular content (myelin) and is therefore strongly suppressed by the MT preparation, appearing dark. The SNpc has **lower macromolecular content than this surrounding white matter** — so the MT suppression is less, and the SNpc appears relatively bright. This is the source of the contrast: it is a comparison to *surrounding white matter*, not to other gray matter neurons in general. An additional contribution: neuromelanin–iron complexes are paramagnetic and shorten the T1 relaxation time of nearby free water protons, enhancing the brightness of neuromelanin-rich tissue in T1-weighted GRE (gradient recalled echo) sequences.

*Sequence.* The most validated protocol is a **2D turbo spin echo (TSE) or 2D GRE sequence with MT preparation**, acquired axially through the midbrain at 3T. A common implementation: MT saturation pulse at ~1.5 kHz off-resonance, flip angle ~500–700°, followed by a GRE readout (TR ~600 ms, TE ~14 ms, flip angle ~40°). Resolution is typically 0.6–0.7 mm in-plane with 3 mm slice thickness. Multiple repetitions (4–8) are averaged online to improve SNR (signal-to-noise ratio). Scan time is approximately 8–12 minutes. **3D MT-GRE** variants improve SNR and geometric coverage and are increasingly used, particularly for combined neuromelanin + iron + nigrosome-1 acquisitions. 7T protocols achieve higher spatial resolution and diagnostic accuracy than 3T.

*Volume placement.* The acquisition volume is centered on the midbrain using anatomical landmarks — the AC–PC (anterior commissure–posterior commissure) line in the sagittal plane and the inferior border of the third ventricle in the coronal plane. Full coverage of the SNpc rostrocaudally (typically 8–12 slices at 3 mm) is verified immediately after acquisition as a quality control step, because partial coverage of the SNpc is a major source of measurement error in longitudinal studies.

*Key outputs.*
- **CNR (contrast-to-noise ratio)**: percent signal difference between the SNpc and a neuromelanin-free white matter reference region (typically the crus cerebri). Formula: CNR = [(SNpc signal − mode(crus cerebri signal)) / mode(crus cerebri signal)] × 100. Higher CNR = more neuromelanin-rich tissue signal.
- **SNpc contrast volume**: the spatial extent of suprathreshold CNR voxels within the SNpc; reflects the volume of surviving neuromelanin-rich neurons.
- **Left–right asymmetry index**: informative because PD typically begins unilaterally, so asymmetry precedes and accompanies early progression.

![NM-MRI of SNpc and locus coeruleus — healthy adult vs Parkinson's disease](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/17bf/10834262/da26ea5eb97b/awad300f1.jpg)
*NM-MRI of the midbrain at the level of the SNpc–VTA (ventral tegmental area) and LC in a healthy adult (left) and a patient with PD (right). The SNpc and LC appear as hyperintense bilateral regions on NM-MRI. In PD, the signal is reduced in extent and intensity, reflecting neuromelanin-containing neuron loss. Source: Sharif et al., Brain 2024 (CC BY — Oxford University Press).*

**Signal and noise.** Cross-sectional discrimination between PD and age-matched controls is strong — AUC (area under the receiver operating curve) >0.90 in most studies at 3T, and >0.99 at 7T for SNpc volume. The best-established source of longitudinal noise is **head positioning**: even small repositioning differences change which voxels fall within the SNpc ROI (region of interest), affecting volume and CNR estimates. Additional sources: coil loading differences, scanner drift, and hydration state (which modestly affects free water relaxation). The ICC (intraclass correlation coefficient) for voxelwise CNR in well-controlled same-scanner repeated protocols reaches ~0.90, meaning roughly 10% of variance per scan is measurement noise — comparable in magnitude to the expected annual biological change.

**Maximum useful sampling frequency.** Annual biological change in SNpc CNR or volume is estimated at 2–5% per year in PD — similar in magnitude to the scan-to-scan noise in optimized protocols. A **single scan at any given time point** is therefore a noisy estimate of the true biological state. From a signal/noise standpoint, the options are:

- *Averaging multiple scans per time point* (e.g., 2–3 scans within one week): reduces noise for that single estimate without adding temporal resolution. This is measurement science, not progression tracking.
- *Spacing time points 3 months apart*: beginning to be useful for short-term interventions with a predicted rapid biological effect (e.g., testing whether a drug changes neuromelanin-related signal within weeks). Requires same-scanner, same-protocol, same-technician repeatability.
- *Spacing time points 6–12 months apart*: the standard for progression tracking. At 6 months, expected change (~1–2.5%) is still close to noise; at 12 months (~2–5%), signal begins to reliably exceed noise in group analyses. Individual-level change detection remains difficult.

Weekly NM-MRI: no progression signal. The biological change within one week is negligible; what accumulates is a characterization of scan-to-scan noise, which is useful for methods/repeatability research.

---

### Iron-Sensitive MRI — R2* and Quantitative Susceptibility Mapping (QSM)
*Tier 2 — Mechanistically central alongside NM-MRI; directly measures the iron burden that overwhelms neuromelanin's protective capacity. Essential for iron chelation trial designs.*

**Pathological correlate.** Progressive iron accumulation in the SNpc and connected basal ganglia structures. Neuromelanin normally chelates iron in redox-inactive Fe³⁺ form; as neurons die or neuromelanin capacity is overwhelmed, iron burden grows and can participate in Fenton chemistry (Fe²⁺ + H₂O₂ → OH• + OH⁻ + Fe³⁺). Iron measures in the SN correlate with disease duration, motor severity (MDS-UPDRS Part III), and DAT-SPECT signal loss across patients.

**Principle.** Two main methods:

*R2\* relaxometry.* R2* (= 1/T2*, units: s⁻¹) is the transverse relaxation rate measured from multi-echo gradient echo acquisitions. Iron-containing compounds (ferritin, hemosiderin, neuromelanin-bound iron) accelerate dephasing of the MRI signal, increasing R2*. Higher R2* in a region → more iron-related effect. Relatively straightforward to acquire but not specific to iron alone.

*Quantitative Susceptibility Mapping (QSM).* A post-processing method applied to the phase images from gradient echo acquisitions. It estimates the local magnetic susceptibility (in parts per billion, ppb) at each voxel. Paramagnetic sources (iron) appear bright; diamagnetic sources (myelin) appear dark. QSM is more specific than R2* for separating iron from other susceptibility sources. Advanced variants (e.g., APART-QSM) can further separate paramagnetic from diamagnetic contributions within a single voxel.

The **nigrosome-1 sign** is a related iron-sensitive observation: in healthy brains, a bright ovoid region within the dorsolateral SNpc is visible on susceptibility-weighted imaging (SWI) and high-resolution T2* — corresponding to an iron-poor neuromelanin-rich sub-region. In PD, this region loses its signal as neurons are lost and iron accumulates, producing a visible structural change sometimes described as a "swallow-tail" loss.

![Nigrosome-1 "swallow-tail" sign on susceptibility-weighted imaging](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Swallow_tail.png/330px-Swallow_tail.png)
*Axial high-resolution SWI (susceptibility-weighted imaging) of the midbrain. The bright "swallow-tail" bilateral structure in the dorsolateral SNpc is the nigrosome-1 — an iron-poor, neuromelanin-rich sub-region. In PD this sign is lost as neurons degenerate and iron accumulates. Source: Schwarz et al., PLOS ONE 2014 (CC BY 4.0).*

**Signal and noise.** QSM has superior sensitivity to R2* for PD-related SNpc changes. Test–retest variability of QSM in the SN on the same scanner is approximately 5–10 ppb. The expected annual increase in nigral susceptibility in PD progression is less well established, but likely in a similar or slightly larger range. This means the signal-to-noise ratio for detecting progression from a single pair of scans is modest.

**Maximum useful sampling frequency.** For an iron chelation intervention with expected rapid change (weeks to months): **3-month imaging** is a reasonable lower bound for detecting target engagement. For natural history progression: **6-month minimum**, with 12 months more typical. Weekly iron MRI is technically redundant — true iron biology does not change meaningfully in one week, and scan variability dominates.

---

### Neurofilament Light Chain (NfL) — Plasma
*Tier 2 — The most accessible blood-based neurodegeneration biomarker; monthly sampling is feasible and biologically meaningful.*

**Neurofilament light chain (NfL)** is a structural protein of neuronal axons released into extracellular fluid upon axonal injury or death. It is detectable in CSF (cerebrospinal fluid, at higher concentrations) and in blood plasma/serum (at much lower concentrations, but measurable by ultrasensitive single-molecule array, SiMOA, assays).

**Pathological correlate.** Non-specific marker of neuroaxonal injury. Elevated in PD relative to age-matched controls and rises with disease severity and duration. Correlates with MDS-UPDRS progression and cognitive decline. Also elevated in other neurodegenerative diseases (atypical parkinsonian syndromes, ALS, etc.), limiting disease specificity, but its trajectory within a given patient is informative for progression monitoring.

**Principle.** Plasma/serum NfL: ultrasensitive immunoassay (SiMOA platform, or similar) from a venous blood draw. The blood assay has lower absolute concentrations (pg/mL range) but is non-invasive and repeatable. CSF NfL: immunoassay from lumbar puncture sample, providing higher concentration values but requiring an invasive procedure.

**Signal and noise.** Plasma NfL has meaningful within-person variability from hydration, physical exertion (intense exercise transiently raises it), and diurnal effects. True progression-related change in PD accumulates over months. Effect sizes per unit time are modest.

**Maximum useful sampling frequency.** Plasma NfL: **weekly sampling, monthly means** is the biologically optimal approach. Weekly draws allow averaging over within-week transient noise (exercise, hydration) while capturing the monthly trajectory. The assay itself has no biological minimum interval — the biological limit is the half-life of NfL in plasma (~3 weeks), which means weekly measurements are not fully independent, but averaging them still tightens the slope estimate. Monthly is the minimum meaningful single-measurement interval. CSF NfL: **3 months** is the true biological minimum for repeat lumbar puncture. The constraint is not the procedure frequency per se but the fact that repeated LP at shorter intervals causes low-grade meningeal irritation that alters CSF protein composition — a genuine biological confound. 3-month spacing allows complete recovery of CSF protein baseline between samples.

---

### Diffusion Tensor Imaging (DTI)
*Tier 3 — Research tool; sensitive to nigrostriatal microstructural degeneration but not commonly used as a primary trial endpoint.*

**Pathological correlate.** Degeneration of nigrostriatal white matter tracts and deep gray matter microstructure. In PD, progressive microstructural changes occur in the SN, putamen, globus pallidus, and white matter pathways connecting them, reflecting axonal and dendritic loss and altered tissue organization.

**Principle.** Diffusion-weighted MRI is acquired in multiple gradient directions. A diffusion tensor is fit at each voxel, yielding directional water diffusion characteristics. Key outputs:
- **FA (fractional anisotropy)**: 0–1 scale of directional coherence. Decreases with fiber loss or disorganization.
- **MD (mean diffusivity)**: magnitude of total water diffusion. Increases in degenerated or sparse tissue.
- **RD/AD (radial/axial diffusivity)**: further decompositions; RD increases with myelin damage, AD with axonal loss.

**Signal and noise.** Sensitive to motion, cardiac pulsation, eddy currents, and field inhomogeneity. Test–retest variability within the same scanner for FA in deep gray matter is approximately 2–4%. Annual FA change rate in the SN in PD is approximately 3–4%/year — comparable to noise at short intervals.

**Maximum useful sampling frequency.** **6–12 months** for detecting progression in deep gray matter. Shorter intervals mostly contribute measurement noise rather than biological signal. An intensive early-intervention study with pre-specified SN-FA endpoints might justify 3-month imaging; below that, signal is dominated by scan variability.

---

### F-DOPA PET — Dopamine Synthesis Capacity
*Tier 3 — Mechanistically informative; complementary to DAT-SPECT but higher cost and less common in standard progression protocols.*

**F-DOPA PET** uses ¹⁸F-fluorodopa — a labeled analog of L-DOPA — to measure the capacity of dopaminergic terminals to synthesize and store dopamine. It is more dynamic than DAT-SPECT: it reflects the active metabolic function of surviving terminals, not only their structural presence.

**Pathological correlate.** Dopamine synthesis activity (aromatic amino acid decarboxylase capacity) in striatal terminals and, at high resolution, in the SNpc itself. Correlates strongly with motor severity and disease duration. Complementary to DAT-SPECT and often used in combination with neuromelanin and iron MRI in multimodal mechanistic studies.

**Principle.** ¹⁸F-DOPA is administered intravenously; 90-minute dynamic PET (positron emission tomography) acquisition follows. A tracer kinetic model (usually the Patlak graphical analysis) yields an influx constant (Ki) representing the uptake rate into dopaminergic terminals. Putaminal Ki is the standard metric.

**Signal and noise.** Similar sensitivity to DAT-SPECT for progression tracking. PET provides higher resolution and better signal characteristics than SPECT. The biological constraint on repeat frequency is radiation dosimetry: ¹⁸F-DOPA delivers approximately 5–7 mSv per scan; regulatory limits in research allow ~50 mSv/year, permitting roughly 6–8 scans annually before approaching dose limits. This is a physics constraint, not a resource one.

**Maximum useful sampling frequency.** **Every 6–8 weeks** is the radiation-permitted ceiling, though biological change at that interval would only be detectable for large reversal effects. **3 months** is a rational minimum for treatment response studies expecting significant striatal dopamine synthesis recovery. **12 months** for natural history progression where the expected change is 10–12%/year in putaminal Ki.

---

### Cerebrospinal Fluid (CSF) Alpha-Synuclein and Seed Amplification Assay (SAA)
*Tier 3 — High diagnostic value for confirming Lewy pathology; limited by invasiveness for repeated longitudinal use.*

**Alpha-synuclein** is the protein that aggregates into Lewy bodies and Lewy neurites, the pathological hallmark of PD. CSF total alpha-synuclein is modestly reduced in PD relative to controls in most studies. More importantly, **seed amplification assays (SAA)** — in which CSF is incubated with recombinant alpha-synuclein under shaking conditions to amplify minute amounts of misfolded seed — can detect pathological alpha-synuclein conformers with high sensitivity and specificity in PD, including in prodromal stages (e.g., idiopathic RBD).

**Pathological correlate.** CSF total alpha-synuclein reflects neuronal release of the protein into interstitial fluid (and thence CSF). SAA positivity reflects the presence of pathologically misfolded, seeding-competent alpha-synuclein conformers in CSF — a direct readout of active Lewy-type pathology.

**Principle.** Lumbar puncture collects 5–15 mL CSF. Total alpha-syn is measured by immunoassay (ELISA or electrochemiluminescence). SAA: CSF is incubated with excess recombinant alpha-synuclein in a plate reader; absorbance kinetics (lag time to aggregation, maximum fluorescence) are measured over 48–100 hours.

**Signal and noise.** CSF total alpha-syn has moderate effect sizes and considerable overlap between PD and controls. SAA has much better sensitivity/specificity (~85–95% in clinical PD, approaching 90% in prodromal RBD in recent studies) and is binary/kinetic rather than a continuous quantity. Longitudinal change in CSF alpha-syn is modest relative to assay variability over months.

**Maximum useful sampling frequency.** **Every 3 months** is the biological minimum for repeat LP — the same meningeal recovery constraint that applies to CSF NfL. The SAA result is semi-binary (positive/negative + kinetic parameters), so it is not the kind of measure that benefits from frequent repetition as a continuous progression variable. Its value is anchoring the disease state (Lewy vs. non-Lewy) and detecting the rare case where treatment fundamentally alters the seeding-competent alpha-synuclein pool. For monitoring treatment response in a protocol where alpha-synuclein clearance is the mechanism: **3-month CSF SAA** is the minimum meaningful interval.

---

### Structural MRI — Volume and Cortical Thickness
*Low priority for progression tracking — atrophy is slow and regionally modest; most sensitive in later-stage disease.*

**Pathological correlate.** Regional brain atrophy reflecting neurodegeneration across the cortex and subcortex. In PD, cortical atrophy is most prominent in temporal, frontal, and parietal regions in later stages. Subcortical volume loss (putamen, caudate, thalamus) accompanies motor and cognitive progression. Hippocampal atrophy tracks cognitive decline toward dementia.

**Principle.** High-resolution T1-weighted MRI (e.g., MPRAGE — Magnetization Prepared Rapid Acquisition Gradient Echo) is processed through automated segmentation pipelines (FreeSurfer, FSL, CAT12) to yield cortical thickness maps and regional volume estimates. Longitudinal processing pipelines reduce scanner-related drift by using a within-subject template.

**Signal and noise.** Structural atrophy in PD is slow and regionally modest relative to the noise of segmentation and scanner drift. Annual cortical atrophy rates in most PD studies are in the range of 0.5–1.5%/year in affected regions — often close to measurement noise at the individual level.

**Maximum useful sampling frequency.** **Annual** for most regions. Accelerated morphometry (6-month) makes sense only for specific hypotheses about rapid atrophy in a focal region, with validated same-scanner longitudinal pipelines. Sub-6-month structural MRI for natural history PD tracking is not justified on signal/noise grounds.

---

### Cardiac MIBG Scintigraphy — Sympathetic Cardiac Denervation
*Low priority for progression tracking — primarily a diagnostic/differential tool; longitudinal change is slow and the scan involves a radiotracer.*

**Meta-iodobenzylguanidine (MIBG) scintigraphy** uses a radiolabeled norepinephrine analog (¹²³I-MIBG) to image cardiac sympathetic innervation. In PD, sympathetic postganglionic denervation of the heart is a common and early feature.

**Pathological correlate.** Cardiac postganglionic sympathetic neurodegeneration — the same degeneration that produces orthostatic hypotension and resting tachycardia in PD. Heart-to-mediastinum (H/M) ratio is reduced in PD, including in early and prodromal stages, and is lower in Lewy body diseases than in atypical parkinsonian syndromes (which typically spare postganglionic sympathetics), making it diagnostically useful for differential diagnosis.

**Principle.** ¹²³I-MIBG injected intravenously; planar scintigraphy at 15 minutes (early) and 4 hours (delayed). H/M ratio in the delayed image is the key metric. Reduced H/M ratio indicates sympathetic denervation.

**Signal and noise.** Good cross-sectional discrimination between PD and MSA/PSP (multiple system atrophy / progressive supranuclear palsy). Longitudinal change is slow.

**Maximum useful sampling frequency.** **Annual** in a longitudinal study if tracking autonomic denervation progression. Involves radiotracer. Not suitable for frequent repeat scanning.
