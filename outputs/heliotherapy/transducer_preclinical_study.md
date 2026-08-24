# Preclinical Study Program — Light-Driven Melanin Electrophysiology

*This program must be completed before Intervention 2 can be applied to patients. The clinical protocol exists; the dose and the mechanistic proof do not.*

---

## Rationale

The theory proposes that photon absorption by melanin in melanosomes shifts the electrophysiological state of the cell — membrane potential (Vmem) and intracellular pH (pHi) — in a direction that is anti-proliferative for cancer cells. Every component of this chain is individually grounded in published work. The chain as a whole has never been demonstrated in a cell.

The preclinical program is designed to establish or refute it sequentially. Each experiment gates the next. If any step fails, the mechanism is refuted at that level and the program stops or pivots.

---

## Cell Panel

The same light conditions must be tested across a matrix of cell types to establish both the mechanistic specificity (melanin-dependence) and the cancer-relevance (does it matter for proliferative phenotype?).

| Cell line | Melanin status | Cancer status | Purpose |
|-----------|---------------|---------------|---------|
| Primary human melanocytes (NHM) | High eumelanin | Healthy | Primary positive control for mechanism |
| TYR-null melanocytes (MC1R-KO or siTYR) | Amelanotic | Healthy | Melanin-free negative control — same lineage |
| MNT-1 (melanoma, pigmented) | High eumelanin | Cancer | Key therapeutic target — does mechanism operate in cancer? |
| SK-MEL-28 (melanoma, moderate) | Moderate | Cancer | Intermediate melanin load — threshold question |
| A375 (melanoma, amelanotic) | Near-zero | Cancer | Melanin-free cancer control |
| HaCaT (keratinocytes) | Transferred melanosomes only | Healthy | Tests whether transferred (non-synthesized) melanosomes couple |
| HeLa + melanin nanoparticles | Exogenous uptake | Cancer (cervical) | Tests whether endocytosed melanin (non-melanosome) couples |
| HeLa unloaded | Zero | Cancer | Paired negative control |

---

## Light Conditions

Four illumination conditions, applied to all cell types in the matrix:

| Condition | Spectrum | Dose range | Rationale |
|-----------|---------|------------|-----------|
| Full-spectrum solar-simulated | 290–1400 nm (AM1.5G filter) | 1, 5, 10, 20 J/cm² | Most physiologically relevant; tests integrated response |
| UVA only | 315–400 nm | 0.5, 1, 2, 5 J/cm² | Peak melanin absorption; primary mechanistic probe |
| Visible only | 400–700 nm | 5, 10, 20 J/cm² | Tests response at longer wavelengths; relevant for deeper tumors |
| IR-A only | 700–1400 nm | 10, 20, 50 J/cm² | Control for thermal effects; low melanin absorption |

**Action spectrum experiment (Experiment 4):** Monochromatic illumination at 365, 405, 450, 520, 590, 630, 680 nm — matched photon flux across wavelengths. Response should track melanin absorption spectrum if melanin is the mediator.

**Dark control:** All cell types maintained in a light-tight incubator for 4 hours before measurement. Lab ambient light is not "dark" — fluorescent/LED lighting delivers continuous UVA-depleted photon flux that would perturb melanin-loaded cells. This confound is almost universally ignored in published melanocyte work.

---

## Measurements

### Primary electrophysiological endpoints

| Measurement | Method | What it answers |
|-------------|--------|-----------------|
| Intracellular pH (pHi) | Genetically encoded sensor (SypHer3s or pHluorin2) — ratiometric, live imaging | Does light shift cytoplasmic proton activity? Is the shift melanin-dependent? |
| Melanosomal pH | LysoSensor DND-160 (lumenal) or organelle-targeted pHluorin | Does the signal originate in the melanosome before propagating to cytoplasm? |
| Membrane potential (Vmem) | DiSBAC2(3) or DiBAC4(3) (voltage-sensitive dye) + patch clamp validation | Does Vmem shift? In which direction? Hyperpolarizing = consistent with mechanism |
| Mitochondrial membrane potential (ΔΨm) | JC-1 or TMRM | Does Vmem shift propagate to mitochondria? |

**Sequencing:** Measure melanosomal pH first (Experiment 1), then cytoplasmic pHi (Experiment 2), then Vmem (Experiment 3). Do not jump to Vmem without establishing the upstream steps — the chain must be demonstrated in order.

### Carcinogenic profile endpoints

These measure whether the electrophysiological shift has functional consequences for cancer behavior:

| Measurement | Method | What it answers |
|-------------|--------|-----------------|
| Proliferation rate | Ki-67 IHC + BrdU incorporation | Does repeated illumination reduce division rate in melanin-dependent manner? |
| Cell cycle distribution | Flow cytometry (PI staining) | Which phase is arrested? G1 arrest = consistent with Vmem hyperpolarization mechanism |
| Migration | Scratch assay (wound healing) + Transwell | Does light exposure reduce migratory capacity? |
| Invasion | Matrigel invasion assay | Does it reduce invasiveness? |
| Apoptosis | Annexin V / PI staining | Is the effect cytostatic (state change) or cytotoxic (cell killing)? Critical distinction — we expect cytostatic |
| Colony formation | Soft agar assay | Long-term effect on anchorage-independent growth — melanoma-relevant |

### Mechanistic controls

| Control | Purpose |
|---------|---------|
| CCCP (mitochondrial uncoupler) | Collapses ΔΨm — does it block the pHi response? Tests mitochondrial coupling |
| EIPA (NHE1 inhibitor) | Blocks Na⁺/H⁺ exchanger — does it block Vmem shift? Tests the pHi→Vmem pathway |
| Bafilomycin A1 (V-ATPase inhibitor) | Blocks melanosomal proton pump — does it block the signal? Tests melanosome-origin requirement |
| OCA2 knockdown (siRNA) | Removes primary pH-setter on melanosome membrane — does it block propagation? |
| Glibenclamide / ML133 (Kir channel blockers) | Blocks K⁺ channels — does it prevent Vmem hyperpolarization? Tests the pHi→K⁺ channel→Vmem step |

---

## Experiment Sequence

### Experiment 1 — Melanosomal pH response

**Question:** Does UVA at non-cytotoxic doses shift lumenal pH in isolated melanosomes?

**Setup:** Purify Stage III–IV melanosomes from NHM by density-gradient centrifugation. Load with LysoSensor DND-160. Apply UVA (1–5 J/cm²) in a cuvette reader. Measure lumenal pH before, during, and for 30 min after illumination.

**Controls:** Melanosomes from TYR-null melanocytes (same protocol). Heat-inactivated melanosomes (same melanin mass, no active transporters). OCA2-inhibited preparation.

**Success criterion:** Transient lumenal pH shift (acidification or alkalinization) in wild-type but not TYR-null preparation.

**If fails:** The photon→melanosome chemistry link is absent. The mechanism is refuted at the organelle level. Stop.

---

### Experiment 2 — Cytoplasmic pHi response in intact melanocytes

**Question:** Does UVA cause a measurable cytoplasmic pHi shift in intact melanocytes — absent in melanin-free cells?

**Setup:** NHM and TYR-null melanocytes transfected with SypHer3s. Dark-adapted 4 h. Apply UVA (1, 2, 5 J/cm²). Live ratiometric imaging at 1 min intervals for 60 min post-exposure.

**Controls:** TYR-null (same lineage, no melanin). IR-A illumination at matched energy (thermal control). EIPA pre-treatment (NHE1 block).

**Success criterion:** pHi shift in NHM, absent or significantly smaller in TYR-null.

**If fails:** Signal does not propagate from melanosome to cytoplasm at detectable levels. Re-examine dose — may require higher fluence or longer protocol. If still absent at 20 J/cm²: mechanism stalls at organelle-cytoplasm coupling.

---

### Experiment 3 — Vmem response

**Question:** Does UVA shift membrane potential in melanocytes, and in which direction?

**Setup:** NHM and TYR-null loaded with DiSBAC2(3). Dark-adapted. UVA 2 J/cm². Fluorescence plate reader + live imaging. Validate with patch clamp on subset.

**Also test:** MNT-1 (melanoma) vs A375 (amelanotic melanoma) — does Vmem shift in the cancer cell, and does it differ from healthy melanocytes?

**Success criterion:** Hyperpolarization in NHM and MNT-1, absent in TYR-null and A375.

**Clinical dose gating:** This experiment defines the minimum fluence required for a measurable Vmem shift. Until this is answered, the clinical dose for Intervention 2 cannot be specified.

---

### Experiment 4 — Action spectrum

**Question:** Does the electrophysiological response track melanin's absorption spectrum?

**Setup:** Repeat pHi + Vmem measurements (from Experiments 2–3) across monochromatic wavelengths: 365, 405, 450, 520, 590, 630, 680 nm at matched photon flux.

**Success criterion:** Response magnitude correlates with melanin extinction coefficient at each wavelength (highest at 365 nm, declining toward red). If the response is flat across wavelengths — it is a non-specific thermal effect, not a melanin-mediated mechanism.

---

### Experiment 5 — Functional cancer readout

**Question:** Does repeated illumination reduce proliferation and cancer behavior in a melanin-dependent manner?

**Setup:** MNT-1 vs A375 vs NHM. Repeated UVA illumination at the dose established in Experiment 3 (e.g., daily for 5 days). Measure: Ki-67, BrdU, cell cycle (flow), scratch assay, Annexin V.

**Key distinction to establish:** Is the effect cytostatic (Vmem shift → state change → reduced proliferation) or cytotoxic (direct UV DNA damage → cell death)? UVA at the doses used should not cause significant DNA damage in melanin-loaded cells (eumelanin dissipates it); A375 (no melanin) should show UV damage while MNT-1 should show electrophysiological effect. This separation is critical for the therapeutic claim.

**Controls:** Matched IR-A exposure (thermal, no melanin photoexcitation). Bafilomycin pre-treatment (blocks melanosomal coupling). Glibenclamide (blocks K⁺ channel step).

---

### Experiment 6 — Transferred melanosomes (keratinocyte model)

**Question:** Do melanosomes transferred from melanocytes to keratinocytes retain electrophysiological coupling competence?

**Setup:** Co-culture NHM + HaCaT. Allow 48–72 h transfer. Confirm transfer by melanin index / confocal. Apply UVA. Measure pHi and Vmem in keratinocytes vs HaCaT alone (no transfer).

**Relevance:** Determines whether the solar callus built by Intervention 1 (which loads keratinocytes with transferred melanosomes) creates electrophysiological coupling competence in epidermal cells — linking the two interventions mechanistically.

---

### Experiment 7 — Exogenous melanin nanoparticles

**Question:** Does endocytosed melanin (non-melanosome route) confer light responsiveness to non-melanocyte cells?

**Setup:** Load HeLa cells with synthetic melanin nanoparticles (endocytic uptake, confirmed by TEM). Apply UVA. Measure pHi and Vmem vs unloaded HeLa.

**Relevance:** If positive — expands the therapeutic range to tumors that can be loaded with exogenous melanin. If negative — confirms that the melanosome membrane (with its specific transporter machinery) is required, not the polymer alone.

---

## What Success Looks Like

| Experiment | Minimum success criterion |
|------------|--------------------------|
| 1 | Lumenal pH shift in WT, absent in TYR-null melanosomes |
| 2 | Cytoplasmic pHi shift in NHM, absent in TYR-null |
| 3 | Vmem hyperpolarization in NHM + MNT-1, absent in A375 |
| 4 | Response tracks melanin absorption spectrum |
| 5 | Reduced proliferation in MNT-1 (cytostatic), not in A375; no apoptosis at therapeutic dose |
| 6 | pHi/Vmem response in keratinocytes post-transfer |
| 7 | Response in melanin-nanoparticle-loaded HeLa, absent in unloaded HeLa |

Experiments 1–3 are the minimum gating set. If all three succeed, the core mechanism is established and Intervention 2 has a preclinical basis. Experiments 4–7 define scope, dose, and therapeutic range.

---

## Critical Confounds to Control

**Ambient light baseline:** All cell culture in light-tight conditions for ≥4 h before any measurement. Log photon flux at cell level throughout experiment. Melanin-loaded cells are not in a "dark resting state" under standard lab lighting.

**Thermal effects vs. photochemical effects:** IR-A at matched energy is the thermal control at every step. Any effect seen with UVA but not IR-A is photochemical. Any effect seen with both is thermal.

**Cytotoxicity ceiling:** Establish cytotoxicity curves (LDH, trypan blue) for all cell types at all doses before electrophysiology experiments. All mechanistic work must be done below the cytotoxicity threshold — killing cells is not the endpoint.

**Melanin quantification:** HPLC-AHPO on cell pellets at start and end of experiment. The experiment is not interpretable unless melanin content is quantified, not just assumed from visual pigmentation.

---

## References

1. [Mostert et al. — Melanin as mixed ionic-electronic conductor, PNAS 2012](https://doi.org/10.1073/pnas.1119948109)
2. [Bellono et al. — OCA2 and melanosomal pH, eLife 2014](https://elifesciences.org/articles/04543)
3. [Levin & Martyniuk — The bioelectric code, Biosystems 2018](https://doi.org/10.1016/j.biosystems.2017.08.009)
4. [Chernet & Levin — Endogenous voltage potentials and cancer microenvironment, DMM 2013](https://doi.org/10.1242/dmm.012328)
5. [Webb et al. — Dysregulated pH: a perfect storm for cancer progression, Nat Rev Cancer 2011](https://www.nature.com/articles/nrc3110)
6. [SypHer3s — improved genetically encoded pH sensor, ACS Sensors 2020](https://pubs.acs.org/doi/10.1021/acssensors.0c00448)
7. [Raposo & Marks — Melanosomes, Nat Rev Mol Cell Biol 2007](https://pmc.ncbi.nlm.nih.gov/articles/PMC2786984/)
