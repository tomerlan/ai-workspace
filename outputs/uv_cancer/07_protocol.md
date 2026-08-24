# Protocol

---

## Inputs

- **Clinical intent**: prevention/photoadaptation, curative, adjuvant, palliative, symptom control.
- **Cancer type and site (if treating cancer)**: skin-limited vs internal; primary vs metastatic.
- **Exposure pattern and burn history**: intermittent blistering burns vs repeated suberythemal exposure; body-site differences.
- **Pigment state where relevant**:
  - for melanoma: melanotic vs amelanotic behavior (tumor uptake of melanin-targeting agents is the gate, not skin color).
  - for photoadaptation: site-specific melanin content/phototype proxies are modifiers, not endpoints.
- **Photosensitivity and contraindications**: history of photosensitivity disorders; immunosuppression; prior high cumulative ultraviolet exposure; medication photosensitizers.
- **Vitamin D status**: baseline **25-hydroxyvitamin D [25(OH)D]** and calcium where supplementation is considered.

---

## High-level gating logic

Separate the workflow by intent:

- **Prevention / photoadaptation**: prioritize burn avoidance while quantifying adaptation (melanin index proxies, minimal erythema dose (MED) proxies) and mediator status (25(OH)D).
- **Cancer treatment**: use only indication-specific clinical phototherapy where established; treat vitamin D as an adjunct; treat melanin/electrophysiology as an experimental program gated by measurable intermediate endpoints.

---

## Protocol branches

### Prevention: photoadaptation (“solar callus”) to reduce burning

Intervention option:
- repeated, non-burning sunlight exposures designed to increase baseline photoadaptation (delayed pigmentation plus stratum corneum thickening), with an explicit constraint of avoiding sunburn.

Measurements to align with this protocol:
- **UV exposure**: track spectrum-aware context (ultraviolet index (UVI) as a burn proxy; note that UVI is UVB-biased and does not capture UVA well).
- **Pigmentation**: site-specific reflectance-based “melanin index” where available; record body site explicitly.
- **Burn events**: log any erythema/burn episodes (timing, body site, severity).
- **Vitamin D axis**: baseline and follow-up 25(OH)D if the goal includes maintaining vitamin D status.

Quantitative regimen:

- Choose one body site for progression and treat other sites separately. Do not use “whole body minutes” as a dose unit.

- Frequency:
  - 3 to 5 sessions per week for 4 to 8 weeks, then maintenance 2 to 3 sessions per week.

- Track A, MED-based dosing:
  - Start at 0.25 to 0.35 times MED for that body site.
  - If there is no visible erythema the next day, increase the next session by 10 to 15 percent.
  - If there is mild erythema the next day, hold dose or reduce by 10 percent.
  - If there is significant erythema, pain, or tenderness, reduce by 25 to 50 percent and pause until baseline is restored.
  - Practical target range for conditioning is 0.6 to 0.8 times MED without next-day erythema.

- Track B, no-MED dosing:
  - Define Tburn for that body site as the exposure duration under a chosen time-of-day and UVI context where extending exposure would reliably produce a burn in your own history.
  - Start at 0.25 times Tburn.
  - Every 2 to 3 sessions with no next-day erythema, increase the next session by 10 to 15 percent.
  - Do not intentionally approach Tburn. Stop increasing once sessions reach about 0.6 to 0.7 times Tburn for that season and site without next-day erythema.

Operational rule:
- The primary success metric is fewer burn events at a given lifestyle exposure pattern. Darker appearance is not a safety metric.

Core balance:
- UVB is the main driver of vitamin D3 synthesis and also produces DNA photoproducts. Photoadaptation can reduce burning and inflammation for a given external dose, but it does not make UV exposure biologically “free.” If the goal is mediator status (e.g., 25(OH)D), supplementation is the non-UV substitute.

Stop conditions:
- any blistering burn event
- repeated erythema at the same dose context (indicates the conditioning schedule is not calibrated to the site/season)

---

### Skin-limited cutaneous T-cell lymphoma (mycosis fungoides)

Intervention option:
- **narrowband ultraviolet B (NB-UVB)** or **psoralen + ultraviolet A (PUVA)** under specialist protocols.

Rationale:
- bounded clinical use case where controlled ultraviolet can induce clinical responses in skin-limited disease. **Evidence: Moderate–High**

Evidence:
- [EORTC consensus recommendations for cutaneous T-cell lymphoma (update 2023; full text)](https://www.ejcancer.com/article/S0959-8049(23)00645-7/fulltext)
- [NCI PDQ: Mycosis Fungoides and the Sézary Syndrome Treatment](https://www.ncbi.nlm.nih.gov/books/NBK65849/)

Stop conditions:
- new blistering/burning reactions
- progressive lesions on-treatment despite protocol adherence
- cumulative-dose concerns under PUVA where squamous cell carcinoma risk becomes clinically relevant
  - [Stern et al., Risk of cutaneous squamous-cell carcinoma in patients treated with PUVA (NEJM)](https://www.nejm.org/doi/full/10.1056/NEJM198405033101805)

---

### Melanotic metastatic melanoma with demonstrable melanin-targeting uptake

Intervention option:
- **Melanin-binding benzamide targeted radionuclide therapy**, gated by demonstrable tumor uptake (theranostic selection).

Rationale:
- uses tumor melanin as a target to deliver systemic beta radiation; early clinical series report uptake, dosimetry, and antitumor effects in selected patients. **Evidence: Low–Moderate**

Evidence:
- [Radiopharmaceutical Therapy of Patients with Metastasized Melanoma with the Melanin-Binding Benzamide 131I-BA52 (J Nucl Med)](https://jnm.snmjournals.org/content/55/1/9)

Stop conditions:
- absent or insufficient tumor uptake on the diagnostic/selection step
- dose-limiting organ dosimetry (organ-at-risk constraints)
- unacceptable toxicity in the therapeutic course

---

### Vitamin D3 as an adjunct (UV-linked mediator pathway)

Intervention option:
- **Daily oral vitamin D3 supplementation**, especially when baseline **25(OH)D** is low.

Rationale:
- targets a UV-linked mediator pathway without requiring ultraviolet exposure; randomized trials and meta-analyses constrain the plausible effect size on cancer outcomes. **Evidence: Moderate–High**

Evidence:
- [Manson et al., Vitamin D Supplements and Prevention of Cancer and Cardiovascular Disease (NEJM, 2019; VITAL primary)](https://www.nejm.org/doi/full/10.1056/NEJMoa1809944)
- [Keum et al., Vitamin D supplementation and total cancer incidence and mortality: a meta-analysis of randomized controlled trials (Annals of Oncology, 2019; full text)](https://www.annalsofoncology.org/article/S0923-7534(19)31159-7/fulltext)

Stop conditions:
- hypercalcemia or symptoms consistent with vitamin D toxicity
- rising calcium with continued supplementation

---

### Action-spectrum UVA/visible illumination with electrophysiology endpoints

Intervention candidate:
- controlled **UVA/visible illumination** chosen to match melanin absorption, paired with membrane potential (**Vmem**), intracellular pH microdomains (**pHi microdomains**), and mitochondrial membrane potential (**ΔΨm**) readouts.

Rationale:
- tests whether light shifts electrical set points in melanin-containing cells before asserting any clinical anticancer effect. **Evidence: VeryLow**

Stop conditions:
- no reproducible shift in Vmem/pHi/ΔΨm across repeats with temperature control
- effect does not track melanin absorption (no action-spectrum specificity)
- effect disappears when conductances/pumps are blocked in ways that falsify the coupling chain

### Increase melanin interface area + action-spectrum illumination (Ling-style amplification strategy)

Intervention candidate:
- deliver a **melanin-like or melanin-binding material** to increase interface area near tumor tissue, then apply controlled UVA/visible illumination, with Vmem/pHi/ΔΨm as primary endpoints.

Rationale:
- Ling-style framing treats large polymer interfaces as capable of shifting effective ion activities and therefore Vmem set points; this is a direct attempt to amplify the “interface → electrophysiology” step. **Evidence: VeryLow**

Stop conditions:
- no action-spectrum specificity consistent with melanin absorption
- outcomes explained by bulk heating rather than electrophysiology
- inability to localize the interface to the intended compartment (no proximity to the “port” that sets Vmem)

### Melanocortin 1 receptor (MC1R) agonism as a combination step

Intervention option:
- pharmacologic **MC1R** agonism to increase epidermal melanin before or alongside controlled UVA/visible protocols.

Gate:
- only consider where increasing epidermal melanin is mechanistically relevant to the intended illumination geometry (skin-accessible compartments).

Evidence:
- [Nle4-D-Phe7 alpha-melanocyte-stimulating hormone significantly increased pigmentation and decreased UV damage in fair-skinned Caucasian volunteers (PubMed)](https://pubmed.ncbi.nlm.nih.gov/16763547/)

