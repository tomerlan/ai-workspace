# Measurements

*What to track, how to track it, and with what device — organized by intervention and by depth of mechanism.*

---

## Intervention 1 — Solar Callus: Tracking Adaptive State

The solar callus is not a single variable. It is a set of adaptive changes — optical, biochemical, immunological, repair capacity — that develop at different rates and are measurable by different methods. Tracking requires a panel, not a single number.

---

### 1.1 Melanin Content — The Optical Endpoint

**What it measures:** Total melanin density in the epidermis. Does not distinguish eu from pheo.

**Primary device: Mexameter MX 18 (Courage & Khazaka)**
- Narrowband reflectance at 660 nm and 880 nm
- Outputs Melanin Index (MI) and Erythema Index (EI) as separate channels
- Non-invasive, contact probe, ~10 second measurement
- MI increases with eumelanin accumulation; EI tracks vasodilation/inflammation (useful for burn detection)
- Limitation: reads total melanin, not eu:pheo split; pheomelanin absorbs less at these wavelengths and can be underrepresented

**Alternative: DermaSpectrometer (Cortex Technology)**
- Same principle, comparable output; widely used in photobiology research

**Alternative: Colorimetry — Konica Minolta CM-700d or similar spectrophotometer**
- Full spectral reflectance → calculates Individual Typology Angle (ITA): ITA = arctan[(L* − 50)/b*]
- Lower ITA = darker/more pigmented skin
- Useful for population-level normalization and longitudinal tracking

**Frequency:** Baseline before protocol start; weekly during active exposure phase; monthly thereafter.
**Sites:** Forearm (inner = less-adapted reference, outer = sun-exposed); sternum or upper back (low-adaptation at baseline for most); face.

---

### 1.2 Eu:Pheo Ratio — The Quality Endpoint

This is the most important variable for cancer risk and the hardest to measure non-invasively.

**Method A: HPLC-AHPO from plucked hair (indirect proxy)**
- Hair melanin composition reflects the eu:pheo ratio in the follicle at time of synthesis
- Acid permanganate oxidation (AHPO) → pyrrole-2,3,5-tricarboxylic acid (PTCA) for eumelanin, thiazole-2,4,5-tricarboxylic acid (TTCA) for pheomelanin → HPLC separation → ratio
- Non-invasive (plucked hair), good reference method
- Limitation: reflects past synthesis (weeks to months prior), not current skin state; requires lab setup

**Method B: Raman Spectroscopy (non-invasive, in vivo)**
- Raman spectrum of melanin has characteristic bands: eumelanin shows a band at ~1580 cm⁻¹ (G-band); pheomelanin shows distinct bands at ~500–700 cm⁻¹ (S-containing chromophore modes)
- Diffuse reflectance Raman at 785 or 830 nm laser allows in vivo skin interrogation
- **Device: RiverD International RamanProbe, or inVia Raman (Renishaw) adapted with skin probe**
- Requires spectral fitting; signal is weak in vivo and requires reference spectra
- Early-stage method for eu:pheo in vivo — research context only at present

**Method C: EPR (electron paramagnetic resonance) — ex vivo only**
- Eumelanin and pheomelanin have distinct EPR spectra at low temperature
- Requires biopsied tissue or extracted hair melanin
- Gold standard for eu:pheo quantification but invasive; not suitable for longitudinal tracking in the same site
- Use: establish calibration between Raman or HPLC and true eu:pheo at baseline

**Practical recommendation:** HPLC-AHPO on plucked hair at baseline, 4 weeks, and 8 weeks. Raman spectroscopy for in vivo tracking where available.

---

### 1.3 Minimum Erythema Dose — The Functional Endpoint

MED is the UV dose at a given body site that produces just-visible redness at 24 hours. It is a direct measure of the skin's current photo-adaptive state — the practical output of the callus.

**Protocol:**
1. Solar simulator (Solar Light Co. 16S-300, or Daavlin UVA/UVB calibrated unit) → irradiate a grid of skin patches at geometrically increasing doses (e.g., ×1.25 steps over 6–8 steps)
2. Read at 24 h under standardized lighting (D65 illuminant, photography booth)
3. MED = lowest dose producing just-perceptible uniform erythema

**Erythema quantification:** Mexameter EI reading at each test site, or chromameter a* value. Both are more objective than visual grading.

**Sites:** Inner forearm (low chronic adaptation), outer forearm (moderate chronic adaptation), trunk (low adaptation baseline for most). Test the same site over protocol progression.

**Expected change:** MED should increase with solar callus progression. Typical range: 20–50% increase in MED by 6–8 weeks in a well-executed protocol in skin type II–III.

**Frequency:** Baseline; every 4 weeks during active protocol; after any gap in exposure.

---

### 1.4 Epidermal Thickness — The Structural Endpoint

Stratum corneum thickening is part of the photoprotective adaptation and is measurable non-invasively.

**Device: High-frequency ultrasound — DermaScan C (Cortex Technology), 20 MHz**
- Produces A-mode and B-mode images of skin layers
- Epidermis appears as a thin hyperechoic band; dermis is less reflective
- Epidermal thickness measurable to ~20 µm resolution
- **Alternative: Optical coherence tomography (OCT) — VivoSight (Michelson Diagnostics)**
  - Higher resolution (~3–5 µm axial), direct visualization of stratum corneum and viable epidermis
  - More expensive; better suited for research settings

**Sites and reference:** Match sites with Mexameter measurements. Baseline thickness varies by body site (forearm epidermis ~60–80 µm; adapted sole of foot can exceed 400 µm as an extreme reference).

**Frequency:** Baseline; 6 weeks; 12 weeks. Thickness changes are slow (weeks).

---

### 1.5 Vitamin D Status

**Measurement: 25(OH)D serum — standard clinical assay**
- Target range for this protocol: 50–80 ng/mL (125–200 nmol/L). The standard clinical "sufficient" cutoff (20 ng/mL) is a deficiency prevention threshold, not an optimization target.
- Timing: fasting morning sample, standardized by season
- Note: 25(OH)D has a long half-life (~15 days) and reflects integrated synthesis + dietary input over 4–8 weeks. Do not expect rapid changes.

**Additional: 1,25(OH)₂D (calcitriol) — optional**
- The active form; more metabolically relevant but tightly regulated
- Less useful as a tracking variable because it is homeostatically controlled unless deficiency is severe

**Frequency:** Baseline; 8 weeks; 16 weeks. Monthly in heavily depleted patients.

---

### 1.6 Post-UV Oxidative Damage — The Dark CPD Proxy

Dark CPD formation (chemiexcitation) is not directly measurable non-invasively in the field. Proxy markers for oxidative damage in the post-UV window:

**Urinary 8-isoprostane (8-epi-PGF2α)**
- Stable lipid peroxidation product; systemic marker of oxidative stress
- Collection: first-morning urine spot, normalized to creatinine
- **ELISA kit:** Cayman Chemical 8-isoprostane EIA (or Oxford Biomedical ELISA); requires −80°C storage
- Collect baseline and 2–4 h post-UV exposure during protocol sessions. A decreasing post-UV isoprostane response over weeks of protocol = improving post-UV oxidative management.

**Urinary 8-OHdG (8-hydroxy-2'-deoxyguanosine)**
- Oxidative DNA damage product; excreted in urine
- **ELISA:** Japan Institute for the Control of Aging (JaICA) 8-OHdG ELISA, or Cayman equivalent
- Same collection protocol as isoprostane

**Practical note:** These are useful for research validation; less practical for routine clinical tracking. In a protocol context, monitor in the first 2–4 sessions to establish the individual's post-UV oxidative response, then use as needed.

---

### 1.7 Immune Calibration Markers — The Systemic Endpoint

The photoimmune calibration signal is the hardest to measure cleanly. Options in approximate order of practicality:

**Serum IL-10**
- Anti-inflammatory cytokine induced by UVA-driven mast cell and keratinocyte signaling
- Elevated post-UV exposure in a calibrated manner; chronically elevated in the solar callus state
- **ELISA or multiplex bead array (Luminex-based)** from serum or plasma
- Useful as a research marker; variability is high without standardized sampling timing relative to last UV exposure

**Complete blood count with differential**
- Tracks NK cell and lymphocyte fractions broadly; extremely non-specific
- Useful as baseline health monitoring, not as a specific photoimmune readout

**Flow cytometry: Treg fraction (CD4+CD25+FoxP3+)**
- The most mechanistically direct measure of photoimmune calibration
- Requires fresh PBMC isolation and staining — **BD LSRFortessa or Beckman Coulter CytoFLEX** (clinical flow cytometer)
- Expensive and requires lab infrastructure
- Best for research protocol validation, not routine clinical monitoring

**Recommendation for clinical tracking:** Serum 25(OH)D + CBC with differential as minimum immunological tracking. Add IL-10 and Treg fraction for research-grade protocols.

---

## Intervention 2 — Light Electrophysiology: Tracking the Mechanism and Response

This intervention is currently experimental. The measurement stack has two layers: mechanism validation (confirming the physical coupling) and cellular/tissue response tracking.

---

### 2.1 Membrane Potential (Vmem) — The Primary Mechanistic Endpoint

**Gold standard: Patch clamp (whole-cell configuration)**
- **Equipment:** Multiclamp 700B amplifier (Molecular Devices) + Digidata 1550B digitizer + pClamp software
- Measures absolute Vmem to ±1 mV precision
- Invasive (ruptures membrane), measures one cell at a time
- Use for: establishing dose-response relationship and action spectrum in cultured melanocytes
- Cannot be used for tissue-level or in vivo tracking

**Population-level imaging: Voltage-sensitive fluorescent dyes**
- **DiSBAC₂(3) or DiBAC₄(3)** — anionic Nernstian dyes; partition into membrane based on Vmem; fluorescence increases with depolarization
  - Applied to cells in culture; imaging by standard fluorescence microscope or plate reader
  - **Device:** Olympus IX83 or Zeiss Axio Observer with appropriate filter (535/617 nm for DiSBAC₂)
  - Dynamic range: ~5–10% ΔF/F per 10 mV change; sufficient for population-level Vmem shifts
- **FLIPR Membrane Potential Assay Kit (Molecular Devices)** — plate-reader format; FLIPR Tetra instrument
  - High throughput; less spatial resolution
  - Useful for dose-response screening

**Genetically encoded voltage indicators (GEVIs) — research grade**
- **QuasAr2/3** (Hochbaum et al.) or **ASAP3** — expressed from lentiviral vector in melanocyte cell lines
- Near-IR excitation; high signal-to-noise; fast kinetics
- Requires confocal or epifluorescence microscope with 640 nm laser
- Best for resolving temporal dynamics (does Vmem shift during UV exposure or hours after?)

---

### 2.2 Intracellular pH (pHi) — The Ion Microdomain Proxy

pHi is the most tractable proxy for the melanosome-to-cytoplasm coupling step and is measurable with high precision in live cells.

**Ratiometric fluorescent dye: BCECF-AM**
- AM ester form is cell-permeable; cleaved intracellularly to BCECF
- Two-wavelength excitation (490/440 nm), single emission (535 nm); ratio is pH-calibrated
- Calibration: nigericin high-K⁺ method to generate pH-fluorescence calibration curve
- Resolution: ~0.05 pH units with careful calibration
- **Device:** Any fluorescence microscope with dual-excitation capability, or a FLIPR with appropriate filters
- Collect: baseline pHi; pHi during UV exposure; pHi kinetics over 0–4 h post-exposure

**Genetically encoded pHi sensor: pHluorin (ecliptic or ratiometric)**
- Expressed from lentiviral vector; no dye loading required; no dye extrusion artifacts
- Ratiometric pHluorin: two-excitation wavelengths (395/475 nm), emission 509 nm
- **Device:** Same as above; confocal preferred for subcellular resolution (can distinguish pHi near melanosomes vs. bulk cytoplasm)

**Key experiment:** Measure pHi in wild-type melanocytes (melanin-loaded) vs. TYR-null amelanotic melanocytes (no melanin) under identical UVA dose. Melanin-dependent pHi shift = evidence for the coupling step.

---

### 2.3 Mitochondrial Membrane Potential (ΔΨm) — Downstream Coupling

**JC-1 (5,5',6,6'-tetrachloro-1,1',3,3'-tetraethylbenzimidazolylcarbocyanine iodide)**
- Monomer at low ΔΨm (fluorescence ~527 nm, green); J-aggregate at high ΔΨm (fluorescence ~590 nm, red)
- Ratio 590/527 directly reports ΔΨm; independent of mitochondrial mass
- **Device:** Fluorescence microscope or flow cytometer (FITC/PE channels); BD Accuri C6 is sufficient
- Limitation: JC-1 is sensitive to solvent and can aggregate non-specifically; TMRE or MitoTracker Red CMXRos are more robust alternatives for absolute ΔΨm

**TMRE (tetramethylrhodamine ethyl ester)**
- Accumulates in mitochondria proportional to ΔΨm; single fluorescence channel (555/580 nm)
- Use with FCCP (protonophore) as a depolarization control to set the zero
- **Device:** Confocal microscope with 543 nm laser; or standard widefield with TRITC filter set

---

### 2.4 Melanin Content in Target Cells — Confirming the Transducer Is Present

Before interpreting any electrophysiological readout, confirm melanin is actually present in the irradiated cells at the expected quantity.

**Fontana-Masson staining (histology)**
- Argyrophilic reduction of silver nitrate by melanin → black deposits
- Standard histochemistry; no special equipment
- Use on biopsy or cell pellet sections to confirm melanin loading and distribution

**EPR (electron paramagnetic resonance) on cell extracts**
- Quantifies total melanin by semiquinone radical signal at g ≈ 2.004
- **Device:** Bruker EMX or MiniScope MS5000 (benchtop EPR)
- Freeze-dried cell pellets; correlate EPR signal intensity with melanin content (calibrated to synthetic eumelanin standard)
- This is the only method that cleanly quantifies melanin polymer content independently of location or organelle

**Reflectance spectrophotometry on cell pellets**
- Quick, quantitative; measures at 660/880 nm as with the skin Mexameter
- Less sensitive than EPR but practical for confirming gross melanin content differences between experimental groups

---

### 2.5 Clinical Tracking of Tumor Response (If Intervention Is Advanced)

For a clinical or translational context where the electrophysiology intervention has moved beyond cell culture:

**Skin/superficial tumors:**
- **Electrical impedance spectroscopy (EIS):** measures the electrical properties of tissue in situ
  - **Device: Nevisense (SciBase)** — originally developed for melanoma detection; measures EIS at skin surface
  - In principle, if Vmem shifts in tumor cells, tissue-level impedance should change measurably
  - No established reference data for this application; would require matched pre/post biopsies for validation

- **Dermoscopy + sequential digital dermoscopy imaging (SDDI)**
  - Track morphological changes in melanocytic lesions under the intervention
  - **Device: DermLite DL4 + FotoFinder or MoleMax HD** (digital dermoscopy with standardized imaging)
  - Endpoint: lesion size, color, and structure change over weeks to months

- **Multiphoton microscopy / FLIM (fluorescence lifetime imaging)**
  - Non-invasive depth-resolved imaging of skin metabolic state (NADH/FAD ratio = optical redox ratio)
  - ΔΨm shifts → change in mitochondrial NADH/FAD balance → detectable in FLIM
  - **Device: Leica SP8 DIVE or JenLab DermaInspect**
  - Research grade; not yet clinical standard

**Internal tumors:**
- Standard clinical imaging: MRI, PET-CT (FDG) for tumor volume and metabolic activity
- **Neuromelanin-sensitive MRI (NM-MRI)** — if melanin-containing cells at depth are the target, NM-MRI can non-invasively map melanin distribution changes
  - MT-prepared T1-weighted sequence (3T MRI scanner, standard clinical hardware)
  - Originally developed for substantia nigra neuromelanin tracking in Parkinson's; applicable to any melanin-dense tissue
- **Photoacoustic imaging (PAI)** — melanin is the dominant optical absorber in tissue, making it the ideal PAI target
  - Pulsed laser illumination → acoustic signal → 3D map of melanin-containing cells
  - **Device: iThera Medical MSOT (Multispectral Optoacoustic Tomography)** — clinical-grade small-animal / translational device; human-scale systems in development
  - Can track melanin loading in tumor tissue and surrounding stroma non-invasively

---

## Measurement Summary Table

| Variable | Method | Device | Invasion | Frequency |
|---|---|---|---|---|
| Melanin index | Narrowband reflectance | Mexameter MX 18 | None | Weekly |
| Eu:pheo ratio | HPLC-AHPO | Plucked hair + HPLC | Minimal | Every 4 wk |
| Eu:pheo in vivo | Raman spectroscopy | RiverD RamanProbe | None | Every 4 wk |
| MED | Solar simulator + chromameter | Solar Light 16S-300 + Mexameter | None | Every 4 wk |
| Epidermal thickness | HF ultrasound | DermaScan C (20 MHz) | None | Every 6 wk |
| Vitamin D | 25(OH)D serum | Clinical lab (CLIA) | Venipuncture | Every 8 wk |
| Oxidative stress | Urinary 8-isoprostane/8-OHdG | ELISA kit | Urine | Post-UV sessions |
| Immune calibration | IL-10 serum / Treg fraction | ELISA / Flow cytometer | Venipuncture / PBMC | Every 8 wk |
| Vmem (cells) | Patch clamp | Multiclamp 700B | Yes (cells) | Per experiment |
| Vmem (population) | Voltage dye imaging | FLIPR Tetra / fluorescence scope | None (cells) | Per experiment |
| pHi | BCECF-AM ratiometry | Fluorescence microscope | None (cells) | Per experiment |
| ΔΨm | TMRE or JC-1 | Confocal / flow cytometer | None (cells) | Per experiment |
| Melanin quantity (cells) | EPR | Bruker MiniScope MS5000 | Ex vivo | Per experiment |
| Tumor response (skin) | EIS | Nevisense | None | Monthly |
| Tumor response (skin) | FLIM | JenLab DermaInspect | None | Monthly |
| Tumor response (internal) | PAI | iThera MSOT | None | Per protocol |
| Melanin at depth | NM-MRI | 3T MRI (standard) | None | Per protocol |
