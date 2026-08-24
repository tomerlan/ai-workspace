# Measurements and tracking

This page is about measurement: what can be quantified, what proxies mislead, and what needs to be separated (UVA vs UVB, melanin amount vs type).

---

## Bottom line: what to measure, with what

### UV exposure

- **UVI for burn risk context**
  - **Device/source**: public UVI forecast, or handheld UV meter that reports erythema-weighted UV
  - **Output**: a UVB-biased “burn risk” proxy, not a UVA measure

- **Personal UV dose with UVA vs UVB separation**
  - **Device**: wearable electronic UV dosimeter with UVA/UVB channels, or paired sensors that separately report UVA and UVB
  - **Output**: time-resolved personal dose pattern; can distinguish UVA-heavy vs UVB-heavy days and exposures

- **Reference spectrum and calibration**
  - **Device**: spectroradiometer
  - **Output**: wavelength-resolved irradiance for validating lamps, window-filtered spectra, and dosimeter calibration

### Skin response and adaptation

- **Burn events and threshold**
  - **Device**: symptom and photo log for erythema and burns, plus clinical minimal erythema dose testing when available
  - **Output**: burn frequency and severity; minimal erythema dose as a personalized threshold that shifts with adaptation

- **Site-specific pigmentation, melanin index**
  - **Device**: reflectance spectroscopy device or reflectance-based melanin index meter
  - **Output**: objective pigmentation at a body site, tracked over time

### Vitamin D axis

- **Vitamin D status**
  - **Assay**: blood test for 25-hydroxyvitamin D, 25(OH)D
  - **Output**: the main biomarker used to guide supplementation and interpret “vitamin D axis” claims

### Melanin presence beyond surface reflectance

- **Melanin mapping in skin lesions**
  - **Device**: multi-wavelength photoacoustic imaging
  - **Output**: spatial map of melanin-rich structures with depth information in skin

- **Melanin imaging in melanotic melanoma**
  - **Device**: melanin-targeted PET using benzamide-class tracers
  - **Output**: a “bind-to-melanin” in vivo readout that can gate melanin-targeted therapy

### Electrophysiology endpoints for the melanin transducer route

- **Membrane potential, Vmem**
  - **Device**: patch clamp or microelectrode recordings in vitro; voltage-sensitive dyes for imaging; microelectrode arrays for populations
  - **Output**: voltage changes and set point shifts, ideally with action-spectrum dependence

- **Intracellular pH, pHi**
  - **Device**: pH-sensitive fluorescent dyes and imaging, including near-membrane microdomain approaches where feasible
  - **Output**: baseline pHi and dynamic shifts during illumination

- **Mitochondrial membrane potential, ΔΨm**
  - **Device**: potentiometric fluorescent dyes with strict controls
  - **Output**: ΔΨm changes that track the same illumination manipulations as Vmem and pHi

---

## UV exposure: what “dose” means in practice

### The basic problem
“Sun exposure” is not one variable. It mixes:
- spectrum (UVA vs UVB),
- intensity and time (dose rate vs cumulative),
- geometry (body site, shading, clothing),
- intermittency (burning vs gradual),
- and behavior/health confounding.

### Common UV metrics

#### UV Index (UVI)
UVI is a public-facing index proportional to **erythemally weighted** UV irradiance (a UVB-biased action spectrum). It is useful for burn risk and public guidance, but can be a poor proxy for UVA-heavy hypotheses.

Reference definition and practical guide:
- [WHO/WMO/UNEP/ICNIRP, Global Solar UV Index: A Practical Guide (2002/2003 PDF)](https://iris.who.int/bitstream/handle/10665/42459/9241590076.pdf)

Erythema action spectrum anchor:
- [CIE reference erythema action spectrum (McKinlay & Diffey, 1987): overview figure](https://ec.europa.eu/health/scientific_committees/opinions_layman/en/sunbeds/figtableboxes/figure-2.htm)

#### Minimal erythema dose (MED)
MED is an individualized threshold concept: the smallest UV dose that produces minimal visible erythema on that person’s skin under a specified test spectrum/geometry, assessed hours to ~24 hours after exposure depending on protocol. It is used clinically to set safe starting doses for phototherapy and, conceptually, it is the most direct way to quantify “burn sensitivity” at a body site (and how that sensitivity shifts with photoadaptation).

Open-access protocol example:
- [Heckman et al., Minimal Erythema Dose (MED) Testing (Journal of Visualized Experiments, 2013; full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3734971/)

#### Ambient UV at residence
Ambient UV proxies are easy to obtain and often show latitude gradients, but they are not personal dose. They are vulnerable to ecological fallacy and behavior confounding (indoor time, clothing, vacations, work).

Example ecological ambient-UVB analysis (hypothesis-generating):
- [Boscoe & Schymura, Solar ultraviolet-B exposure and cancer incidence and mortality in the United States, 1993–2002 (BMC Cancer, 2006; full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1665523/)

Ecological fallacy caution:
- [The fallacy of the ecological fallacy (AJPH)](https://ajph.aphapublications.org/doi/abs/10.2105/AJPH.84.5.819)

#### Personal UV dosimetry
Personal dosimeters can measure individual exposure patterns, but require calibration and typically report an erythema-weighted signal unless specifically designed for UVA/UVB separation.

Review:
- [Use of Electronic UV Dosimeters in Measuring Personal UV Exposures and Public Health Education (Atmosphere, 2020)](https://www.mdpi.com/2073-4433/11/7/744)

Example methodological comparison (shade vs sun; device limitations):
- [Dobbinson et al., Comparing Handheld Meters and Electronic Dosimeters for Measuring UV Levels Under Shade and In The Sun (Photochem Photobiol, 2016; full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5629966/)

---

## UVA vs UVB separation

Many endpoint claims depend on separating UVA-heavy vs UVB-heavy exposures:
- **UVB**: more direct DNA photoproduct weighting; also vitamin D synthesis driver.
- **UVA**: deeper skin penetration; oxidative chemistry; can matter even when UVI (erythema) is not high.

Practical implication:
- A “low UVI day” does not imply low UVA.
- “Sun through a window” is typically **UVA-dominant** (UVB is strongly attenuated by glass).

UVA through vehicle windows (measurement-relevant examples):
- [Assessment of Levels of Ultraviolet A Light Protection in Automobile Windshields and Side Windows (JAMA Ophthalmology, 2016)](https://jamanetwork.com/journals/jamaophthalmology/fullarticle/2522190)
- NEJM image case illustrating chronic one-sided exposure: [Unilateral dermatoheliosis (NEJM Images in Clinical Medicine)](https://www.nejm.org/doi/full/10.1056/NEJMicm1104059)

---

## Dose pattern: intermittency, dose rate, and burns

To compare studies, exposures should be characterized by:
- **cumulative dose** (e.g., seasonal integrated exposure),
- **dose rate** (short intense peaks vs long low-grade),
- **intermittency** (especially burn events),
- **life stage** (childhood vs adulthood patterns).

Even if two people have the same annual dose, these pattern variables can shift:
- repair opportunity,
- adaptation (tanning, epidermal thickening),
- and behavior-associated confounding (vacation sun vs occupational sun).

---

## “Water structure” / melanin transducer hypotheses: what must be measured

If the claim is UVA/visible → melanin → interfacial water/electrostatics → Vmem/pHi/ΔΨm shifts, then the measurement priority is:
- spectrum-resolved exposure (UVA/visible weighted by melanin absorption, not only UVI),
- electrophysiology readouts (Vmem, pHi microdomains, ΔΨm),
- and mediation tests (channel/pump dependence).

### Reference ranges (order-of-magnitude anchors)
These are not “optimal” in a universal sense, but they are the typical magnitudes that make electrophysiology claims falsifiable in practice.

- **Membrane potential (Vmem)**:
  - differentiated excitable tissues are often ~ −60 to −90 mV at rest
  - many proliferative/cancer phenotypes are more depolarized (often reported in the ~ −10 to −30 mV range, model-dependent)
  - open-access review entry points: [Bioelectric Dysregulation in Cancer Initiation, Promotion, and Progression (2022; full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8964134/), [Membrane potential and cancer progression (2013; full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3713347/)

- **Intracellular pH (pHi)**:
  - many normal cells sit near ~7.2 at rest (cell-type dependent)
  - solid tumors commonly show the “reversed gradient” motif: relatively alkaline pHi with acidic extracellular pH
  - review entry point: [The chemistry, physiology and pathology of pH in cancer (2014; full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3917353/)

- **Mitochondrial membrane potential (ΔΨm)**:
  - typical magnitude is on the order of ~150–190 mV (negative inside), with interpretation depending strongly on method and on whether ΔΨm is being used as a proxy for proton motive force versus other charge carriers
  - practical measurement guide: [Mitochondrial membrane potential probes and the proton gradient: a practical usage guide (2011; full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3115691/)

---

## Pigmentation and melanin

### Phenotype proxies
- **Fitzpatrick skin type**: common, subjective, conflates burn/tan response with behavior.
- Self-reported ancestry/skin tone scales: useful for stratification, not mechanism.

### Optical measures
Diffuse reflectance spectroscopy and reflectance-based “melanin index” measures provide objective pigmentation quantification at a site.

Example (reflectance measures predicting UV sensitivity; melanin quantification context):
- [Non-invasive diffuse reflectance measurements of cutaneous melanin content can predict human sensitivity to UVR (full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3609039/)

### Imaging measures
If the question is “how much melanin is present, and where,” some modalities can move beyond surface reflectance.

- **Photoacoustic imaging**: melanin is a strong optical absorber, so multi-wavelength photoacoustic imaging can map melanin-rich structures and estimate depth in skin. A key limitation is that quantification can be biased by skin tone and other chromophores, so calibration and model assumptions matter.  
  - [Fakhoury et al., Photoacoustic imaging for cutaneous melanoma assessment: a comprehensive review (J Biomed Opt, 2024; full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10785699/)

- **Neuromelanin-sensitive magnetic resonance imaging (MRI)**: specialized MRI sequences can visualize and quantify signal in neuromelanin-rich brain nuclei (substantia nigra, locus coeruleus). The contrast mechanism is still debated (melanin/metal complexes vs tissue microstructure/water), so it is best treated as an in vivo imaging biomarker rather than a direct “melanin concentration assay.”  
  - [Trujillo et al., Neuromelanin-sensitive MRI as a promising biomarker of catecholamine function (Brain, 2023; full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10834262/)

- **Melanin-targeted positron emission tomography (PET)**: benzamide-class radiotracers with melanin affinity have been developed to image melanotic melanoma, demonstrating a concrete “bind-to-melanin” measurement concept in vivo. This is not a general-purpose whole-body melanin measure, but it is a real example of targeted melanin imaging chemistry.  
  - [Ren et al., Melanin Targeted Pre-clinical PET Imaging of Melanoma Metastasis (J Nucl Med, 2009; full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4215196/)

### Chemical measures
If you need subtype composition, chemical degradation + chromatography is the canonical route. Common marker approach:
- **Eumelanin**: PTCA (and related oxidation products)
- **Pheomelanin**: TTCA and/or 4-AHP–based markers (method-dependent)

Reference for tissue/hair melanin chemical analysis (overview entry point):
- [Ito et al., AHPO melanin analysis methods (PubMed)](https://pubmed.ncbi.nlm.nih.gov/21535429/)

### Genetics as effect modifier: melanocortin 1 receptor (MC1R)
MC1R variants shift melanogenesis bias (eumelanin vs pheomelanin tendency) and correlate with sun sensitivity and melanoma risk; in causal inference they can act as effect modifiers and as sources of pleiotropy in genetic instruments.

---

## Vitamin D

### Biomarkers
- **25-hydroxyvitamin D [25(OH)D]** is the main status biomarker (reflects inputs from sun + diet + supplements).
- **1,25-dihydroxyvitamin D [1,25(OH)₂D]** is the active hormone but is tightly regulated and can be a misleading “status” measure.

Authoritative overview:
- [NIH Office of Dietary Supplements: Vitamin D fact sheet for health professionals](https://ods.od.nih.gov/factsheets/vitamind-HealthProfessional/)

### Reference ranges and common action thresholds (25(OH)D)
Different groups use different cut points; the table below is a compact summary of ranges commonly used in the literature.

NCBI Bookshelf summary table (includes NAM framing and common descriptors):
- [Appendix A Table 1, Serum Vitamin D Level Reference Ranges (USPSTF evidence review, 2018)](https://www.ncbi.nlm.nih.gov/books/NBK525404/table/app_1/)

Commonly used ranges (ng/mL with nmol/L equivalent):
- **<12 ng/mL** (**<30 nmol/L**): high-risk / “severe deficiency” range
- **12–20 ng/mL** (**30–50 nmol/L**): deficiency range in many clinical uses
- **20–30 ng/mL** (**50–75 nmol/L**): disputed (“insufficiency” vs “sufficiency,” depending on authority)
- **>30 ng/mL** (**>75 nmol/L**): often treated as “sufficient” in many clinical discussions; no consistent additional benefit for bone outcomes is expected purely from being above this threshold in NAM framing
- **>50 ng/mL** (**>125 nmol/L**): “cause for concern” range in NAM framing (toxicity risk is mediated by hypercalcemia rather than 25(OH)D itself)

### Assay standardization
25(OH)D assays vary by method (immunoassay vs LC-MS/MS), cross-reactivity, and handling of metabolites (e.g., epimers). Standardization programs exist to reduce bias and improve comparability.

VDSP assay variability/bias study (PMC):
- [Wise et al., Vitamin D Standardization Program (VDSP) Intralaboratory Study for the Assessment of 25-Hydroxyvitamin D Assay Variability and Bias (J Steroid Biochem Mol Biol, 2021; full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8403635/)

Practical consequences:
- If a study combines multiple labs/methods without harmonization, “dose–response” analyses can be distorted.
- Baseline deficiency vs sufficiency matters; many trials enroll largely sufficient populations.

---

## Measurement pipeline

True UV exposure (spectrum × time × geometry) is typically represented using proxies (ambient UV, questionnaires, wearables). Those proxies introduce measurement error and misclassification, which then distort estimated UV–cancer associations.

Two additional bias channels are common:
- Confounding: outdoor activity, socioeconomic status, baseline health can affect both exposure and cancer risk.
- Screening and surveillance: detection intensity can change recorded incidence independent of biology.

Interpretation:
- Good biology can be erased by bad exposure measurement.
- Good exposure measurement can be swamped by confounding if endpoints are detection-sensitive.