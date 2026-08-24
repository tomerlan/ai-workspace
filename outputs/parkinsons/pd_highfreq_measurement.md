# High-Frequency Measurement Strategy for Parkinson's Disease

The goal here is to compress the feedback loop as tightly as biology permits. The standard clinical cadence — annual or semi-annual assessments — is designed for trial logistics, not for learning fast. This document maps the landscape assuming unlimited resources: what to measure, how often, and where genuine new signal lives versus where you would be measuring noise. Every frequency limit stated here is a **biological constraint**, not a practical one.

---

## The Core Framework: Two Types of High-Frequency Value

**Averaging-down noise.** For slow biological signals, frequent measurement does not mean faster feedback — it means a more precise estimate of a slow parameter. A weekly wearable tremor score accumulates toward a monthly average that is more reliable than any single weekly measurement. The value is statistical, not temporal. This applies to most clinical scales and many biomarkers.

**Fast-changing biology.** Some measures genuinely change over days or weeks: dopaminergic compensation (medication effects), autonomic tone, sleep architecture, inflammatory markers, voice acoustics. These can detect early intervention responses within weeks. This is where high-frequency measurement earns its keep.

The practical consequence: the highest-frequency protocol should not simply replicate the standard protocol faster. It should prioritize **modalities with fast biological dynamics** and **low within-day noise**, while using averaging on the slower signals. Below, each modality is assessed against both criteria.

---

## The Medication Holiday Principle

Every measurement taken during active dopaminergic medication is a measurement of **pharmacological compensation, not disease state**. Levodopa masks the underlying motor deficit. A patient whose nigrostriatal system has lost 60% of its DAT signal can appear nearly normal on motor exam while medicated. The disease is progressing invisibly.

**Standardized OFF-state assessment** — performed after ≥12 hours without levodopa and short-acting dopamine agonists (longer washout for rotigotine patch: 24h; for pramipexole in slow progressors: 18h) — reveals the underlying neurological substrate. The OFF state is noisier moment-to-moment (tremor, dyskinesia from the previous dose, emotional distress from the OFF experience itself), but it is measuring the disease, not the drug.

For the purposes of this protocol: **all assessments designated as progression markers should be performed in standardized OFF state**. This is operationally demanding — patients are uncomfortable in the OFF state — but the data is categorically more informative. A weekly OFF-state wearable window of 2–4 hours, paired with a brief structured task, generates a progression time-series that annual ON-state exams cannot match.

---

## Tier A — Daily or Continuous: The Highest-Density Signals

These modalities genuinely benefit from daily or continuous data. Biological variation at this timescale is real and meaningful, not just noise.

---

### Wearable Motor Biomarkers — Triaxial Accelerometry + Gyroscope
*Wrist, ankle, or belt-worn. Continuous or semi-continuous. The backbone of any high-frequency PD monitoring protocol.*

Modern wearables (Empatica, Apple Watch with validated PD apps, Kinesia, STAT-ON) capture tremor frequency/amplitude, bradykinesia (reduced wrist acceleration during voluntary movement), gait cadence, stride regularity, and sit-to-stand transitions. Step-derived features include stride velocity, coefficient of variation of stride interval, and 180° turning time.

The biological signals here operate on fast timescales: a levodopa dose produces measurable motor improvement within 20–40 minutes; the OFF phase before the next dose shows motor deterioration on the same scale. Daily and within-day waveforms of motor performance directly track the dopaminergic fuel tank as it fills and empties.

**What high-frequency buys:** The full shape of the motor fluctuation curve — not just "ON" or "OFF" but the transition kinetics, the peak dose response, the tail — and how this shape changes month by month as the disease progresses. A single monthly clinic visit captures a single snapshot, which could land anywhere in the ON/OFF cycle. Continuous data captures the biological reality.

**High-frequency protocol:** Continuous 24/7 wearing during a defined measurement period. Daily summary statistics: mean gait velocity during ambulation periods, tremor power spectral density during rest periods, bradykinesia composite score. Weekly OFF-state windows (2–4 hours at minimum drug trough, typically early morning before first dose): extract a clean OFF-state motor composite for progression tracking. This is the single most information-dense modality available.

---

### Voice Acoustics — Daily Phonation and Sustained Vowel Tasks
*Smartphone, 2–5 minutes, daily. Not yet in routine clinical use but validated as a sensitive PD motor biomarker.*

Parkinson's disease produces a characteristic dysarthria pattern detectable before clinical motor diagnosis: reduced vocal amplitude (hypophonia), increased jitter (cycle-to-cycle frequency instability), increased shimmer (amplitude instability), shortened vowel duration, and reduced formant variability. These features arise because phonation requires fine rapid motor control of laryngeal and respiratory muscles — the same system affected by bradykinesia and rigidity.

**What it measures biologically.** The acoustic features are a functional readout of the basal ganglia-brainstem motor loop. Jitter and shimmer reflect the same rapid alternating movement impairment quantified by UPDRS Item III.4 (finger tapping). Voice is uniquely valuable because it can be captured without any wearable hardware — a smartphone microphone suffices — and because it is sensitive to both dopaminergic state (changes measurably in ON vs. OFF) and long-term disease progression.

**Validation.** Tsanas et al. (2013, Oxford) demonstrated that machine learning classifiers applied to 16 dysphonia features could track MDS-UPDRS motor severity (Part III) with r ~0.87 from remote smartphone recordings. Parkinson's Voice Initiative collected >10,000 voice recordings across 42 countries. AUC for PD diagnosis vs. controls exceeds 0.90 in multiple independent validations. Longitudinal sensitivity to progression is emerging but not yet as well-established as cross-sectional discrimination.

**High-frequency protocol.** Two tasks, 2 minutes combined: (1) sustained vowel /ahhh/ for 5 seconds × 3 repetitions; (2) rapid alternating syllables /pa-ta-ka/ for 10 seconds (diadochokinetic rate). Both recorded on a calibrated smartphone at fixed distance. Done daily at a fixed time, in the same room, in standardized OFF state 3×/week and ON state daily. Acoustic features extracted automatically. Daily → weekly mean is the progression-relevant unit.

**Novel angle.** Because voice changes acutely with dopaminergic state, it can serve as a near-real-time **medication response monitor**: the kinetics of voice improvement after each morning levodopa dose, day by day, month by month. Flattening of this response curve signals declining levodopa efficacy — an early marker of striatal terminal depletion — months before the patient notices motor wearing-off clinically.

---

### Digital Motor Tasks — Spiral Drawing and Finger Tapping
*Smartphone/tablet touchscreen or digitizer tablet, 3–5 minutes, daily.*

**Spiral drawing.** Micrographia (progressively smaller, slower handwriting) is one of the most specific PD motor signs. A standardized Archimedean spiral drawn on a touchscreen or digitizer tablet yields: pen velocity, pressure (on digitizer tablets with stylus), intrastroke regularity, and final spiral tightness ratio. Drawing velocity declines with disease and improves within 30–60 minutes of levodopa administration.

**Finger tapping.** UPDRS III.4 quantifies alternating finger tapping by examiner observation. A smartphone app (FingerTapping, UPDRS Digital) captures tap-to-tap interval, amplitude (accelerometer), and regularity computationally. Tap frequency and inter-tap interval coefficient of variation are the most sensitive features. These metrics detect UPDRS motor changes below the examiner's detection threshold.

**High-frequency protocol.** Daily: 30 seconds bilateral finger tapping (each hand separately), one spiral each hand. Generate per-hand composite bradykinesia scores. Track daily mean and OFF-state scores separately. The inter-hand asymmetry index is particularly valuable early in the disease when one hemisphere is disproportionately involved.

---

### Heart Rate Variability and Autonomic Wearables
*Continuous wrist photoplethysmography (PPG) or chest ECG patch. Parasympathetic/sympathetic balance as a progression proxy.*

Cardiac autonomic dysfunction is among the earliest PD pathological changes — cardiac sympathetic denervation (MIBG scintigraphy positive) and reduced vagal tone precede motor diagnosis by years. Heart rate variability (HRV), specifically the high-frequency component (HF-HRV, 0.15–0.40 Hz), reflects parasympathetic (vagal) modulation of heart rate. PD patients show chronically reduced HF-HRV relative to age-matched controls. This worsens with disease duration.

**What makes this high-frequency worthy.** HRV changes on timescales of days to weeks — with sleep quality, physical activity, hydration, and disease state. Critically, HRV responds to pharmacological interventions within days: a drug that reduces autonomic dysfunction will produce a detectable HRV shift before motor changes are measurable. HRV is a leading indicator, not a lagging one.

**Novel angle.** Morning resting HRV (5-minute supine, fixed time) as a daily biomarker. Autonomic state before the first dose of medication captures the overnight recovery pattern — a sensitive reflection of the brainstem locus coeruleus/vagal nuclei state that standard motor exams miss entirely. Combine with a 1-minute head-tilt orthostatic test (stand from lying, measure blood pressure and heart rate response with a continuous blood pressure wearable): the orthostatic blood pressure drop and compensatory heart rate rise reflect peripheral sympathetic denervation and are measurable at home with a validated automated device.

---

## Tier B — Weekly: High-Information, Feasible with Protocol

---

### Standardized OFF-State Video Motor Assessment
*Structured 10-minute video, weekly, patient-filmed or clinic-filmed. OFF state (≥12h drug holiday).*

A structured video protocol captures most of the information in a clinical UPDRS III exam without requiring a rater to be physically present: (1) face at rest, 30 seconds (tremor, masked facies); (2) bilateral finger tapping and hand opening/closing × 10 cycles each; (3) gait across a fixed 4-meter corridor and back, then 180° turn; (4) standing with arms outstretched (postural tremor). This takes 8–10 minutes and can be performed at home.

**Rater:** A dedicated rater scores each video, blinded to date and treatment condition. Automated computer vision scoring exists as an additional layer — validated algorithms for bradykinesia from video achieve performance approaching trained rater agreement and allow continuous algorithmic monitoring between human-reviewed sessions. Running both in parallel removes inter-rater drift and cross-validates the automated system.

**OFF-state calibration.** The drug holiday creates a brief period of maximal symptom expression. The patient's OFF-state severity is a purer function of underlying nigrostriatal reserve than any ON-state measure. A weekly time-series of OFF-state motor scores, collected at the same hour every week (e.g., 7:00 AM, 2 hours after waking, before first dose), creates a progression signal invisible to standard trials.

---

### Pupillary Light Reflex — Autonomic and Melanopsin Readout
*Smartphone-based or dedicated pupillometer, 3 minutes, weekly. Novel.*

The pupillary light reflex (PLR) — constriction of the pupil in response to a light flash — is driven by two systems: the classical retinal pathway (rods/cones → optic nerve → olivary pretectal nucleus → Edinger-Westphal nucleus → pupil constrictor) and the melanopsin-expressing intrinsically photosensitive retinal ganglion cells (ipRGCs), which sustain the pupil constriction during prolonged bright light exposure (the "sustained pupil response" or post-illumination pupil response, PIPR). The ipRGC-melanopsin pathway is the same system responsible for circadian light entrainment.

**Why it is relevant in PD.** Multiple independent groups have documented reduced PLR amplitude and slowed re-dilation kinetics in PD relative to age-matched controls. Impaired sympathetic re-dilation (from locus coeruleus degeneration), reduced parasympathetic tone, and possibly altered retinal ipRGC function all contribute. The melanopsin-specific component (PIPR) has not been well characterized in longitudinal PD cohorts — this is a genuine open question.

**Mechanistically, this connects two threads.** (1) The autonomic degeneration axis — measurable early, before motor signs. (2) The melanopsin/circadian axis — because ipRGC-driven circadian dysfunction in PD may reflect both downstream retinal pathology and upstream SCN vulnerability. A weekly PIPR measurement, done with a smartphone-based pupillometer (PupilScreen, or validated open-source protocol with a fixed white screen flash), takes 3 minutes and could track both autonomic and melanopsin biology with no radiation, no blood draw, no specialist.

**Protocol.** 5 minutes of dark adaptation. Deliver a high-irradiance blue light flash (470 nm, 1 second, fixed luminance using screen calibration) to one eye. Record the pupil diameter time series for 30 seconds post-flash via smartphone front camera (720p at 30fps is sufficient). Extract: peak constriction amplitude, constriction latency, redilation time constant (τ), and PIPR at 6 seconds post-flash. The PIPR at 6 seconds reflects melanopsin-driven sustained activation and is independent of rod/cone input at that time point.

---

### Olfactory Testing — Brief Standardized Smell Identification
*5 minutes, monthly. Biological adaptation limits higher frequency.*

Hyposmia (reduced smell) is one of the earliest and most prevalent PD prodromal features — present in 70–90% of PD patients, often predating motor diagnosis by years. The Sniffin' Sticks identification test or the Brief Smell Identification Test (B-SIT, a 12-item subset of the UPSIT) can be administered in under 5 minutes.

Monthly is the biological ceiling — not a logistical one. Olfactory identification tests produce cross-adaptation: exposure to an odor at one session primes recognition at the next, independent of any true improvement. With a large bank of alternate odorant sets (Sniffin' Sticks provides 12 pens × 4 forced-choice options), parallel forms can be rotated to delay adaptation — but even with complete form rotation, semantic priming persists across sessions shorter than ~4 weeks. The biology (slow peripheral olfactory neuron turnover, even slower central olfactory bulb volume change) also does not produce signal at sub-monthly resolution. Monthly is therefore both the instrument limit and the biological limit. The key value remains: objective, medication-state-independent, and measuring a dimension of neurodegeneration entirely invisible to motor scales.

---

### Plasma Biomarker Panel — Blood Draw
*Monthly. Plasma NfL + GFAP + alpha-synuclein + uric acid.*

The blood-based biomarker landscape for neurodegeneration has matured substantially. A single monthly venous blood draw, processed on ultrasensitive immunoassay platforms, yields a multi-biomarker snapshot of complementary biology:

**Plasma NfL (neurofilament light chain)** — axonal injury and death. Already established as a PD progression biomarker with effect sizes distinguishing fast from slow progressors. Monthly sampling averages over transient noise (exercise, illness) and builds a slope.

**Plasma GFAP (glial fibrillary acidic protein)** — astrocyte activation and neuroinflammation. GFAP is elevated in multiple neurodegenerative diseases and rises with cognitive burden in PD. Less studied longitudinally than NfL, but emerging as complementary. Reflects glial biology rather than neuronal death per se.

**Plasma phospho-alpha-synuclein** — still emerging. Blood-based alpha-synuclein measures are complicated by red blood cell contamination, but phosphorylated Ser129 alpha-synuclein (pS129-α-syn) in plasma-derived neuronal extracellular vesicles is showing promise as a Lewy-specific signal. This is not yet clinical-grade, but in a research protocol, it adds the one dimension that NfL and GFAP lack: disease-specific Lewy pathology.

**Uric acid** — a proxy for systemic antioxidant capacity and neuroprotective potential. Cheap, routine lab. Lower uric acid correlates with faster PD progression in cohort data. In the context of an intervention (dietary change, supplementation), monthly uric acid is a direct engagement biomarker.

**Inflammatory panel (optional):** IL-6, hs-CRP. Non-specific but changes within days of intervention and can confirm target engagement for anti-inflammatory strategies before structural change is detectable.

---

## Tier C — Monthly: Informative but Slow-Moving

---

### Retinal OCT and Dopaminergic Amacrine Layer Thickness
*Optical coherence tomography, 10 minutes, monthly. Novel and emerging.*

The retina is embryologically part of the brain and contains dopaminergic neurons — specifically the dopaminergic amacrine cells of the inner nuclear layer (INL). In PD, thinning of the retinal nerve fiber layer (RNFL) and the inner plexiform layer (IPL) has been documented in multiple studies, with the IPL showing superior sensitivity. The INL thickness may directly reflect dopaminergic amacrine cell loss.

**Why this is interesting for high-frequency work.** Retinal imaging is completely non-invasive, takes 10 minutes, requires no drug holiday, and generates quantitative volume data from a structure that is neurologically equivalent to the brain. A home-based retinal OCT scanner (iCare HOME, NIDEK) is available for self-administered measurements. Monthly retinal layer thickness, tracked over 6–12 months, may provide an accessible surrogate for nigrostriatal pathology with a much lower burden than brain MRI.

**The open question.** Current published data establishes cross-sectional RNFL/IPL thinning in PD but longitudinal sensitivity to progression has not been rigorously characterized. Annual rates of RNFL thinning in PD are in the 1–2 µm/year range — near the noise floor of current instruments (~1 µm test-retest variability). IPL may have better signal. Monthly sampling at this scale would primarily characterize noise — but the noise characterization itself is valuable for establishing whether monthly retinal OCT can eventually detect progression.

---

### EEG Beta Oscillations — Motor Cortex and Subthalamic Synchrony
*Single-channel dry-electrode EEG, 15 minutes, weekly or monthly. Emerging for at-home use.*

Exaggerated beta-band (13–35 Hz) oscillations in the basal ganglia-cortical motor loop are one of the most replicated neurophysiological findings in PD. Beta power in the subthalamic nucleus (STN) is elevated in the OFF state and suppressed by levodopa — the suppression correlates with motor improvement. The same beta excess is detectable in motor cortex EEG, non-invasively.

**What it measures.** The degree of pathological motor circuit synchronization — a functional readout of the nigrostriatal dopaminergic deficit that is distinct from structural imaging. Beta power is dopamine-sensitive (responds acutely to medication), but the baseline OFF-state beta magnitude also correlates with motor severity and (in some studies) dopaminergic terminal density.

**At-home EEG.** Consumer-grade single-channel EEG headsets (Muse, Neurosity, Emotiv) have been validated for detecting resting motor cortex beta power asymmetry in PD in research settings. A 10-minute resting OFF-state recording (eyes open, minimal movement), using electrodes over Cz/C3/C4, generates motor cortex beta power estimates. Signal quality is limited by motion artifacts and electrode contact, but weekly averages aggregate over noise.

**Novel application.** Because beta power is acutely levodopa-sensitive, weekly OFF-state EEG + post-dose EEG (at peak dose effect, 1 hour post-medication) generates a within-person beta suppression index — a proxy for remaining dopaminergic responsiveness. Diminishing suppression over months signals declining terminal reserve. This is a direct pharmacodynamic readout that is invisible to standard motor rating.

---

### Stool Microbiome Composition
*16S rRNA or metagenomic sequencing from self-collected stool, monthly.*

The gut microbiome is altered in PD in a characteristic pattern — reduced Prevotellaceae, elevated Verrucomicrobiaceae (Akkermansia), altered short-chain fatty acid producers — and these changes predate motor diagnosis in prospective studies. The enteric nervous system is considered a site of early alpha-synuclein pathology, and the gut-vagus-brain axis is a proposed route of pathology spread (Braak stages 1–2).

The microbiome is dynamic on a timescale of days — dietary shifts produce measurable compositional changes within 2–3 days. For an intervention targeting gut composition (diet, FMT, probiotic), **weekly sampling** is biologically valid and captures the trajectory of community restructuring. For slower natural history monitoring, monthly is sufficient. DNA extraction and sequencing turnaround is not a constraint with a dedicated laboratory; samples can be frozen immediately and batched. Weekly sampling for the first 3 months of an intervention, then monthly, is the biologically optimal strategy.

**The open frontier.** Whether gut microbiome composition can serve as a **progression biomarker** — not just a cross-sectional correlate — is not established. But for someone studying a gut-targeted intervention (diet, probiotic, FMT), monthly microbiome is the primary engagement assay.

---

## Novel / Exploratory: Mechanistically Grounded but Not Yet Validated for PD Progression

---

### Skin Sebum Volatile Metabolomics
*Non-invasive swab from forehead/neck skin, batch analysis monthly or quarterly.*

Joy Milne, a Scottish nurse with an unusual ability to smell Parkinson's disease on affected individuals, triggered research that identified a reproducible alteration in the sebum volatile metabolome of PD patients: elevated levels of eicosadienoic acid, hippuric acid, and several other compounds, detectable by mass spectrometry from a simple cotton swab of the face/neck skin. Published in Nature Communications 2019 (Trivedi et al.), the PD sebum signature was validated in an independent cohort (AUC 0.85).

**Why this is interesting.** Sebum is continuously produced by sebaceous glands. Its metabolite composition reflects systemic lipid, oxidative, and inflammatory biology. Uniquely, the collection is non-invasive, completely painless, and repeatable as often as desired — no drug holiday, no blood draw. The metabolome changes faster than neurodegeneration, potentially tracking disease activity rather than structural loss.

**Current state.** Cross-sectional validation is solid. Longitudinal progression tracking has not been published. The analytical pipeline requires laboratory mass spectrometry (not a point-of-care device). For a well-resourced research protocol, monthly swab collection with batch analysis is feasible and would generate novel longitudinal data. **This is a genuine gap in the literature.**

---

### Infrared Spectroscopy Patterns of Dried Blood Spot
*Dried blood spot (finger prick) + FTIR spectroscopy, weekly. Experimental.*

Fourier-transform infrared spectroscopy (FTIR) of dried blood spots captures the overall biochemical fingerprint of blood — protein secondary structure, lipid oxidation state, nucleic acid content — in a single non-directed scan. In neurodegenerative diseases, FTIR spectral changes (particularly in the amide I/II bands and lipid carbonyl region) have been reported in small case-control studies. The technical appeal: a finger prick on filter paper, dried, analyzed by FTIR in a core laboratory. No antibody, no specific target, hypothesis-free readout of systemic biochemical state.

This is speculative — no validated PD progression longitudinal FTIR study exists. But in the context of a well-designed single-patient or small-cohort protocol tracking a multimodal panel, weekly FTIR adds a systemic biology dimension at near-zero collection cost.

---

### Near-Infrared Transcranial Spectroscopy — Cerebral Oxygenation
*Wearable NIRS headband, continuous or daily. Experimental.*

Functional near-infrared spectroscopy (fNIRS) measures changes in cerebral oxygenated and deoxygenated hemoglobin concentration in the cortex at depths of 1–2 cm, via the relative transparency of tissue to near-infrared light (700–900 nm). Consumer-grade fNIRS devices (Kernel Flow, fnirs.org research headbands) are now available. Prefrontal cortex oxygenation during cognitive tasks and motor cortex oxygenation during movement are measurable.

**The PD relevance.** Frontal and parietal cortex hypoperfusion has been documented in PD in fNIRS studies during gait and dual-task conditions. Dopaminergic medication partially normalizes this. The pattern tracks with cognitive and gait severity.

**The novel hypothesis.** If photobiomodulation with near-infrared light is being tested as a PD intervention (transcranial or otherwise), fNIRS provides a direct readout of cortical hemodynamic response to light exposure — distinguishing biological target engagement from placebo. Weekly fNIRS could monitor whether NIR exposure produces measurable cortical oxygenation changes over weeks.

---

## Proposed High-Frequency Protocol: The Fast Feedback Stack

Combining the modalities above into a biologically-maximal monitoring stack. Every frequency here reflects the biological signal limit, not a logistical one.

**Continuous / daily:**
- Wrist/ankle wearable: 24/7 motor monitoring — bradykinesia, gait, tremor. Dedicated OFF-state windows extracted every morning (pre-dose, fixed duration).
- Morning voice recording (2 minutes, standard phonation + diadochokinetic task, before first dose, daily).
- Digitized finger tapping + spiral drawing: twice daily — pre-dose (OFF state) and at peak dose effect (1 hour post-dose).
- Resting HRV: 5 minutes supine, fixed time, daily (wearable PPG or dedicated ECG chest strap).
- Home PSG or wearable EEG: nightly sleep architecture, REM monitoring, limb movement index.

**Weekly:**
- Standardized OFF-state video motor assessment (10 minutes, filmed by an accompanying observer in a fixed environment, scored by blinded rater).
- MDS-UPDRS Parts I, II, IV — structured rater interview (OFF state).
- Cognitive battery: digit span, choice reaction time, trail-making, N-back (validated digital versions, 15 minutes, same time of day).
- Pupillary light reflex + PIPR (3 minutes, calibrated smartphone protocol, OFF state).
- EEG resting beta power, 15 minutes (dry-electrode headset, OFF state, before and 1 hour post-dose to capture beta suppression index).
- PDSS-2 + GDS-15 + SCOPA-AUT — rater administered.
- Sebum swab (if metabolomics pipeline running).
- Stool sample (if gut intervention; weekly for first 3 months, then monthly).
- Blood draw: plasma NfL, GFAP, pS129-α-syn EVs, uric acid, hs-CRP, IL-6.

**Monthly:**
- PDQ-39 (covers the preceding month by design — biological ceiling).
- Brief smell test (B-SIT) — biological ceiling due to adaptation.
- Retinal OCT — IPL + RNFL thickness.
- MDS-UPDRS Part III scored by a second independent blinded rater (cross-validation of weekly video scores).

**Every 3 months:**
- MoCA with alternate form — biological ceiling due to learning effects.
- NM-MRI + iron QSM (3T, same scanner, same protocol). Minimum interval for detecting reversal-type effects.
- MR spectroscopy: NAA/Cr + glutamate in striatum and SNpc.
- CSF: NfL, alpha-synuclein SAA, GFAP, total alpha-syn. Minimum interval constrained by meningeal recovery biology.

**Every 6 months:**
- DAT-SPECT (putaminal SBR): structural anchor and confirmatory endpoint.
- F-DOPA PET (if dopamine synthesis capacity is a primary endpoint).
- DTI (FA/MD in SN and nigrostriatal tracts).

**As-needed / baseline + key timepoints:**
- TSPO PET (neuroinflammation): baseline, 8 weeks, 16 weeks — radiation dose limits ~6-week minimum intervals.
- Structural MRI (volumetry, cortical thickness): baseline + annually; not useful at shorter intervals.
- Cardiac MIBG scintigraphy: baseline for differential staging; annually if autonomic denervation progression is a study endpoint.

---

## Tissue-Level Tracking for Treatment Response

Natural history tissue metrics change slowly and were designed to characterize a disease, not to evaluate a treatment. In the treatment context, a different question applies: **what is the fastest tissue-level evidence that the intervention is doing anything at all?**

The answer depends critically on what type of effect you are looking for. There are three distinct cases, and they have very different detection timelines.

**Reversal / restoration** — the intervention actively improves a tissue metric that was abnormal. Iron drops, neuromelanin signal recovers, dopamine terminal density increases, neuroinflammation resolves. This is the easiest case. Change moves in the opposite direction from natural history and can accumulate quickly on top of a large baseline deficit. Detection windows of 6–12 weeks are plausible for fast-responding metrics.

**Stopping progression** — the intervention halts ongoing degeneration but does not recover lost tissue. The metric should show zero change over the observation window. Detection requires demonstrating absence of change against a backdrop of known measurement noise. The signal is the *difference between expected decline and observed decline*. Even with zero noise, you need long enough that the expected natural history change exceeds the measurement noise floor. For most tissue metrics, this is 12–18 months minimum.

**Slowing progression** — the intervention reduces but does not eliminate the rate of decline. This is statistically the hardest case. A 30% reduction in an already-slow decline rate is essentially undetectable at the individual level within a year, and requires group comparisons with large N and 2+ year follow-up.

The implication for protocol design: **if your treatment has any plausible mechanism for reversal, instrument it for reversal detection first**. Stopping and slowing require far more time and, in most cases, require a control arm.

---

### Neuroinflammation — TSPO PET: Fastest Tissue Window
*Target engagement within 4–8 weeks. The most responsive tissue metric for anti-inflammatory interventions.*

Activated microglia overexpress the translocator protein (TSPO) on their outer mitochondrial membrane. Radiolabeled TSPO ligands — [¹¹C]PK11195 (older, lower signal/noise), [¹⁸F]DPA-714, [¹¹C]PBR28 (second-generation, better signal) — bind to TSPO and allow PET imaging of microglial activation. In PD, TSPO signal is elevated in the SNpc, putamen, and globus pallidus, tracking both disease severity and local neurodegeneration.

**Why this is the fastest tissue-level readout.** Neuroinflammation is not the primary neurodegenerative lesion — it is a consequence and amplifier. As such, it can be suppressed before structural loss is reversed or halted. A treatment that reduces microglial activation (GLP-1 agonists, NAD+ supplementation, photobiomodulation, anti-inflammatory dietary intervention) might produce measurable TSPO signal reduction within 4–8 weeks, well before any NM-MRI or DAT-SPECT change would be detectable.

**Detection timeline for reversal:** 4–8 weeks is biologically plausible for partial neuroinflammation resolution. Most published intervention studies use 12-week minimum imaging intervals, which likely underestimates what is detectable earlier. TSPO PET involves radiotracer exposure (limits repeat frequency to approximately every 6 weeks minimum) and specialist facility access. In a well-resourced protocol: **baseline → 8 weeks → 16 weeks** captures both early response and trajectory.

---

### Iron — QSM: Fast Response to Chelation, Slow Natural Accumulation
*Treatment response detectable at 6–12 weeks with active chelation.*

Nigral iron accumulation is a continuous process in PD and feeds the Fenton oxidative damage cycle. Iron chelation with deferiprone (or newer chelators: desferrioxamine intranasal, VK-28 analogs) directly removes iron from tissue. The FAIRPARK-II trial showed significant nigral iron reduction by QSM at 12 months of deferiprone; pilot data suggests 6-month changes are detectable. More intensive chelation protocols might show QSM change within 6–12 weeks.

**Why this is faster than NM-MRI.** Iron levels can be actively manipulated pharmacologically. QSM reflects iron concentration, which responds to removal within weeks, long before neuronal structural integrity (NM-MRI, DAT-SPECT) changes. QSM is therefore the **primary target engagement biomarker** for any iron-targeting intervention — it tells you within weeks whether the drug is reaching its molecular target in the SNpc.

**Detection timeline:** For active chelation targeting a 10% reduction in nigral susceptibility (roughly 10–20 ppb change against test-retest noise of 5–10 ppb): **8–12 weeks** in optimized same-scanner protocols. For monitoring natural history slowing without active removal: 12 months minimum.

**MR spectroscopy complement.** Proton MR spectroscopy (¹H-MRS) in the striatum and SNpc measures metabolite ratios within a single acquisition — N-acetylaspartate/creatine (NAA/Cr, neuronal viability), glutamate (excitotoxicity), lactate (energy failure), choline/Cr (membrane turnover). An intervention that reduces mitochondrial dysfunction (e.g., ketogenic diet, NAD+ precursors) might produce a detectable striatal NAA/Cr improvement within 4–8 weeks — faster than any structural change. MRS is typically added to MRI sessions at minimal extra time (10–15 minutes). This is underused in PD intervention trials.

---

### NM-MRI — SNpc Volume and CNR: Months for Reversal, Year+ for Slowing
*Primary structural biomarker of neuromelanin-rich neuron survival.*

Under natural history, SNpc CNR declines at approximately 2–5% per year, with scan-to-scan noise of ~5–10% in optimized protocols. This puts natural history tracking at 12-month minimum intervals.

**For treatment response, the timeline compresses if the effect is reversal-type.** A treatment that increases NM-MRI signal (by reducing neuromelanin degradation, increasing neuromelanin synthesis, or reducing the oxidative environment that drives neuromelanin auto-oxidation) would produce change in the direction *opposite* to noise drift. Because the expected natural history change is negative, any positive signal change is unambiguously treatment-related. A 5–10% NM-MRI signal increase would be individually detectable at **3 months** in a carefully controlled same-scanner protocol.

**What could plausibly reverse NM-MRI signal?** Two mechanisms: (1) A treatment that reduces neuromelanin-iron complex formation might free neuromelanin capacity and change its MRI relaxation properties, even without new neuronal survival. (2) A treatment that genuinely reduces ongoing neuronal loss — slowing the loss of neuromelanin-containing neurons — would produce a *shallower decline* rather than reversal. At 3–6 months, a reversal is clearly detectable; slowing would not be.

**Practical protocol for treatment monitoring:** 3T same-scanner, same protocol, same technician, same session time. Acquire at baseline, 3 months, 6 months. Blinded ROI analysis. If no signal is observed at 6 months, the treatment has not produced a tissue-level NM-MRI effect at the sensitivity level of this protocol — a meaningful negative result that informs the next step.

---

### DAT-SPECT: 6-Month Minimum for Treatment Effect
*Dopaminergic terminal density — the gold-standard structural endpoint.*

Annual putaminal SBR decline: 10–12%/year in early PD (decelerating). Test-retest: ~5–8%. For treatment response:

- **Reversal** (actual increase in DAT density — possible theoretically with neuroprotection that allows sprouting): detectable at **6 months** if effect size is >8% (above noise). No published treatment has demonstrated this.
- **Stopping** (zero decline): requires **12 months** to show absence of expected ~10% drop with sufficient confidence.
- **Slowing by 50%**: requires **18–24 months** in an adequately powered trial.

The radiotracer exposure limits scan frequency: 6-month minimum in any reasonable protocol.

---

### Plasma Biomarker Kinetics: The Fastest Blood-Based Tissue Signal
*Monthly sampling; NfL and GFAP respond on 4–8 week timescales.*

Plasma NfL does not directly measure neurons — it measures the rate of neuronal axon injury. This is actually valuable: it is a **flow rate** rather than a stock measure, meaning it responds faster than structural volume metrics. If a treatment reduces the rate of neurodegeneration, plasma NfL should fall within 4–8 weeks — long before DAT-SPECT or NM-MRI show structural improvement.

**The detection logic.** In untreated PD, plasma NfL rises gradually (effect size roughly 0.3–0.5 pg/mL/year above age-matched controls, though absolute values are highly variable between individuals). An effective neuroprotective treatment should produce a detectable plateau or decline in NfL within 4–8 weeks if it substantially reduces ongoing axonal injury. This has been shown for rapidly neurotoxic diseases (MS attacks, Alzheimer's treatment with amyloid-clearing drugs) — the principle transfers to PD.

**Within-person tracking.** Because NfL variability between individuals is high but within-person variability is lower (CV ~10–15% month-to-month), each patient serves as their own control. A pre-treatment NfL trajectory (3 months of monthly measurements to establish baseline slope) followed by post-treatment monthly measurements gives a within-person slope change detectable at **3–4 months** post-treatment initiation.

**GFAP** tracks astrocyte activation/neuroinflammation. Faster dynamics than NfL, responds to acute neurological events within days. For chronic PD treatment monitoring: same monthly protocol, complementary biology (astrocyte vs. axonal compartments).

---

## Detection Timeline: What Change Is Visible in What Time

The table below synthesizes the signal/noise numbers from across the document. All figures assume a single-patient protocol (the hardest case) in standardized OFF state, well-controlled measurement conditions, and a treatment with a genuine biological effect. "Detectable" is defined as observed change > 2× the noise SD (roughly 95% confidence of a real effect).

| Metric | Natural history change rate | Scan-to-scan noise | **Reversal detectable** | **Stopping detectable** | **Slowing (50%) detectable** |
|---|---|---|---|---|---|
| Voice acoustics (jitter/shimmer) | ~3–5%/year worsening | ~8–10% per session | **2–4 weeks** | 6 months | 12+ months |
| Wearable bradykinesia (weekly OFF means) | ~5–10%/year | ~10–15% per week | **2–4 weeks** | 4–6 months | 12+ months |
| HRV (morning resting, weekly mean) | ~3–5%/year decline | ~10–12% per week | **4–6 weeks** | 6–8 months | Not feasible individually |
| TSPO PET (neuroinflammation) | Unknown (increases with progression) | ~10–15% | **4–8 weeks** | 6 months | 12+ months |
| MR spectroscopy NAA/Cr (striatum) | ~1–2%/year decline | ~5–8% per scan | **6–10 weeks** | 12 months | Not feasible individually |
| Plasma NfL (monthly, within-person slope) | ~0.3–0.5 pg/mL/year | ~10–15% per draw | **6–10 weeks** | 4–6 months | 8–12 months |
| Plasma GFAP (monthly) | Unknown in PD | ~12–18% per draw | **6–8 weeks** | 4–6 months | Not established |
| Iron QSM (with active chelation) | ~5–10 ppb/year | ~5–10 ppb | **8–12 weeks** | 12 months | 18+ months |
| NM-MRI SNpc CNR (same-scanner) | ~2–5%/year decline | ~5–10% per scan | **3 months** | 12–18 months | Not feasible individually |
| DAT-SPECT putamen SBR | ~10–12%/year decline | ~5–8% | **6 months** | 12–18 months | 24+ months |
| Retinal OCT IPL thickness | ~1–2 µm/year decline | ~1 µm | **4–6 months** | 18+ months | Not feasible |
| Structural MRI volume | ~0.5–1.5%/year | ~1–2% | **Not feasible** | 24+ months | Not feasible |

---

### Reading the Table

**Functional metrics (voice, wearables, HRV) are the fastest feedback layer** — not because they measure tissue, but because they measure the *functional output* of tissue that is continuously operating. A treatment that genuinely improves basal ganglia function should register in voice and motor wearables within weeks. The tradeoff is that these metrics are multi-factorial: sleep, mood, and systemic illness confound them. High-frequency sampling (daily) is the solution — enough data points that confounders average out.

**TSPO PET and MR spectroscopy are the fastest tissue-level readouts** and are conspicuously underused in PD intervention trials. If you are testing an anti-inflammatory treatment (GLP-1 agonist, NAD+ supplementation, photobiomodulation), a 6-week TSPO PET can confirm target engagement at the tissue level before any structural marker would budge.

**Plasma NfL is the fastest accessible biomarker with tissue meaning.** Monthly draws, within-person slope analysis, 4–8 week response. Every serious intervention protocol should include it.

**NM-MRI at 3 months is the minimum useful tissue structural window** — and only if you are looking for reversal. Slowing or stopping is a 12-month question at minimum.

**DAT-SPECT at 6 months is the hard anchoring endpoint** — slow, expensive, radiation-limited, but the field's most accepted structural biomarker. Everything faster above is a leading indicator; DAT-SPECT is the confirmatory terminal.

---

### Multimodal Triangulation: The Logic of Layered Evidence

No single metric is sufficient. The value of a dense multimodal protocol is **triangulation**: independent metrics converging on the same conclusion give far more confidence than any single biomarker, even at short intervals.

The convergence logic: if voice improves at 4 weeks, plasma NfL drops at 8 weeks, and iron QSM falls at 12 weeks — all in the same direction — the probability that all three are confounded simultaneously is low. Conversely, if only one metric moves and the others do not, the single-metric signal is likely noise or a domain-specific effect unrelated to neurodegeneration.

**A minimal viable tissue monitoring stack for a treatment trial:**
1. Plasma NfL + GFAP: monthly from Day 0.
2. TSPO PET: baseline, Week 8, Week 16 (if anti-inflammatory mechanism).
3. Iron QSM: baseline, Week 8, Month 6 (if iron-related mechanism).
4. NM-MRI: baseline, Month 3, Month 6.
5. DAT-SPECT: baseline, Month 6, Month 12.

Functional metrics (wearables, voice, HRV) run in parallel from Day 0. They provide the earliest signal. Tissue metrics confirm mechanism. DAT-SPECT provides the structurally anchored endpoint that the field requires for claims of disease modification.

---

## Why Medication Holidays Unlock the Protocol

The most underused experimental lever is systematic OFF-state measurement. A standard PD cohort study measures patients in their usual medication state, which varies person to person and fluctuates within each person by the hour. Signal is buried in pharmacological noise.

A protocol that fixes the measurement context — always early morning, always before first dose, always the same number of hours after last dose — removes this source of variance almost entirely. The resulting time-series is measuring disease, not medication titration.

The tradeoff: patient discomfort in the OFF state. Tremor, rigidity, and occasionally dysphoria are real. The protocol requires careful patient selection (early-to-moderate disease, patients who can tolerate 1–2 hours OFF with support), informed consent, and standby access to medication. These are manageable constraints. The information gain is not subtle — OFF-state assessments in early PD can detect motor progression at 6-month intervals that ON-state assessments miss entirely at 12-month intervals.
