# Evidence for cancer outcomes

---
---

## UV promotes cancer: skin

### Net assessment
- **Cutaneous squamous cell carcinoma (SCC)** and **basal cell carcinoma (BCC)** incidence increase with solar UV exposure. **Evidence: High–VeryHigh**
- **Melanoma incidence** is UV-linked, with strong dependence on exposure pattern (intermittent burns), phenotype, and measurement. **Evidence: High**

### Hazard classification
The **International Agency for Research on Cancer (IARC)** is a World Health Organization agency that evaluates whether exposures are carcinogenic hazards.

IARC’s primary vehicle is the **IARC Monographs**: expert-reviewed reports (“monographs”) that summarize the evidence and classify an exposure by carcinogenic hazard (e.g., “carcinogenic to humans”). This is a statement about *hazard*, not about how large the risk is at a particular dose or in a specific behavior pattern.

Randomized assignment to decades-long sunlight exposure patterns with skin-cancer incidence as an endpoint is not a realistic design in humans. That constraint is why the evidence base for UV and skin cancer is built from mechanistic lesion biology, tumor genomic signatures, observational epidemiology, and artificial ultraviolet analogs rather than from “full-spectrum sunlight RCTs.”

- **Solar and ultraviolet radiation are classified as carcinogenic hazards**. **Evidence: VeryHigh**
  - [IARC Monographs Vol 55: Solar and Ultraviolet Radiation (1992)](https://publications.iarc.fr/73)
  - [IARC Monographs Vol 100D: Radiation (review volume)](https://www.who.int/publications/m/item/iarc-monographs-on-the-evaluation-of-carcinogenic-risks-to-humans-volume-100d)

### Human epidemiology (incidence)
The **World Health Organization (WHO)** and the **International Labour Organization (ILO)** have jointly synthesized occupational exposure evidence to estimate work-related disease burden.

- **Occupational solar UV exposure is associated with increased keratinocyte skin cancer risk**, with stronger associations for cutaneous squamous cell carcinoma than basal cell carcinoma in the synthesis. **Evidence: High**
  - [WHO/ILO systematic review/meta-analysis summary (ARPANSA)](https://www.arpansa.gov.au/association-between-occupational-exposure-solar-ultraviolet-radiation-and-skin-cancers-who)

The synthesis reports **relative risk (RR)** values, defined as:

```plain text
RR = risk_exposed / risk_unexposed
```

Interpretation:
- RR ≈ 2.4 for cutaneous squamous cell carcinoma means the occupationally exposed group had about 2.4× the risk of that cancer compared with the unexposed group in the pooled estimate.
- RR ≈ 1.5 for basal cell carcinoma means about 1.5× the risk.
- RR does not give absolute risk without a baseline incidence rate.

- **Artificial UV (indoor tanning)**: risk is increased for melanoma and keratinocyte cancers in meta-analyses; early age of first use shows stronger associations in some syntheses. **Evidence: High**
  - [Systematic review/meta-analysis entry point (Cancers, 2021)](https://www.mdpi.com/2072-6694/13/23/5940)
  - [IARC Q&A/context document: Artificial UV radiation and skin cancer (PDF)](https://www.iarc.who.int/wp-content/uploads/2018/07/ArtificialUVRadSkin9.pdf)

### Mechanistic convergence (tumor signatures + lesion biology)
- **UV lesions → UV signature mutations**: UVB-weighted lesions such as **cyclobutane pyrimidine dimers (CPDs)** and 6–4 photoproducts, plus UVA-weighted oxidative chemistry, link the exposure to measurable DNA damage patterns observed in skin cancers. **Evidence: VeryHigh**
  - Example mechanism: CPDs can continue forming after UVA exposure via melanin chemiexcitation (“dark CPDs”): [Premi et al., Chemiexcitation of melanin derivatives induces DNA photoproducts long after UV exposure (Science, 2015; full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4432913/)

### Gradual tanning as protection (what is and is not supported)
Gradual, non-burning exposure can induce pigmentation and epidermal thickening. These adaptations can measurably increase the **minimum erythema dose** (the ultraviolet dose that produces visible redness), but the magnitude is typically modest and does not imply “tanning prevents melanoma.”

- **Solar-simulated radiation tanning increases the minimal erythema dose modestly** in skin types II–III after repeated suberythemal exposures; induced protection factors reported in this study are on the order of ~1.4–2.3 depending on regimen. **Evidence: High (for erythema photoprotection magnitude)**
  - [Tanning in human skin types II and III offers modest photoprotection against erythema (PubMed abstract)](https://pubmed.ncbi.nlm.nih.gov/9796443/)
- **Ultraviolet A tanning can be visually deceptive and fail to protect against DNA photoproduct formation**, while ultraviolet B–induced tanning provides modest photoprotection in the experimental setup. **Evidence: High (for UVA-tan non-protection under tested conditions)**
  - [Photobiological implications of melanin photoprotection after UVB-induced tanning of human skin but not UVA-induced tanning (full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4333058/)

Human melanoma risk is pattern-dependent:
- A meta-analysis of observational studies reports that **intermittent sun exposure and sunburn history** are risk factors for melanoma, while **high occupational sun exposure** appears inversely associated in the pooled literature, with substantial heterogeneity and design sensitivity. **Evidence: Moderate (association), Low–Moderate (causality)**
  - [Gandini et al., Meta-analysis of risk factors for cutaneous melanoma: II. Sun exposure (PubMed abstract)](https://pubmed.ncbi.nlm.nih.gov/15617990/)

Sunburn history is a useful marker of intermittent, excessive exposure in the literature, but it is also a noisy exposure variable. It is typically self-reported, it collapses spectrum and dose pattern into one event label, and it is not a measure of typical day-to-day suberythemal exposure.

Avoiding burns does not make artificial tanning benign:
- In a population-based case–control study, indoor tanning was associated with increased melanoma risk even after excluding people who reported indoor-tanning burns, including among those who reported zero lifetime sunburns. **Evidence: Moderate (association), Low–Moderate (causality)**
  - [Vogel et al., Exposure to Indoor Tanning Without Burning and Melanoma Risk by Sunburn History (J Natl Cancer Inst, 2014; full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4161998/)

Melanoma relevance is an additional step:
- “tanning raises minimal erythema dose” is a measured physical endpoint
- “tanning reduces melanoma incidence” is a long-latency human endpoint and is not established by these tanning photoprotection experiments

### Confounders and alternative explanations (skin cancer-specific)
- **Socioeconomic status and healthcare access can confound UV–incidence and UV–mortality associations** because they can influence *both* the exposure proxy and the measured outcome.
  - Path 1 (detection): higher socioeconomic status/healthcare access → more dermatology visits and skin screening → more biopsies → more cancers detected (especially early/indolent lesions) → higher *recorded incidence*.
  - Path 2 (exposure correlation): socioeconomic status can correlate with sun exposure patterns (vacations, outdoor leisure, occupational class) and with sun-protection behaviors.
  - The confusion: if “higher UV exposure” groups also tend to have higher socioeconomic status and screening, then UV can look associated with higher *diagnosed* incidence even if the main driver of the difference is detection intensity. Conversely, if “higher UV exposure” groups have lower socioeconomic status and less screening, incidence can be undercounted in high-UV groups.
  - Mortality adds another path: socioeconomic status/healthcare access → earlier diagnosis and better treatment → lower mortality, which can make UV appear “protective” for mortality if UV exposure correlates with socioeconomic status.

### Exposure geometry: UVA through glass
- **Unilateral dermatoheliosis (truck driver)**: a documented clinical image of severe unilateral photoaging. Mainstream reading is chronic ultraviolet A (UVA) exposure through side windows; it is compelling for geometry and spectrum accounting. **Evidence: High (for “UVA-through-glass matters”)**
  - [Unilateral dermatoheliosis (NEJM Images in Clinical Medicine)](https://www.nejm.org/doi/full/10.1056/NEJMicm1104059)
  - Some authors emphasize “spectrum distortion through glass” as an additional hypothesis layer; the core observation is asymmetric long-term exposure + asymmetric photodamage.

### What would change my mind?
- Large prospective datasets with **personal dosimetry** (UVA/UVB separated) + **standardized screening** that show null or inverse associations for SCC/BCC/melanoma incidence under realistic exposure patterns.

---

## UV negates cancer: skin (outcomes and prognosis signals)

### Net assessment
For melanoma, there are observational signals that markers of sun exposure correlate with improved survival in some datasets, but detection, phenotype, and confounding are difficult to eliminate. **Evidence: Low–Moderate (causality)**

### Melanoma survival associations
- **Connecticut Tumor Registry melanoma survival**: solar elastosis (histologic marker of cumulative sun damage) and some sun-exposure measures were inversely associated with melanoma death after adjustment for thickness and other factors. **Evidence: Moderate (association), Low (causality)**
  - [Berwick et al., JNCI 2005 (PubMed)](https://pubmed.ncbi.nlm.nih.gov/15687362/)
  - [Berwick et al., JNCI 2005 (full text)](https://academic.oup.com/jnci/article/97/3/195/2544082)
- **GEM study melanoma survival**: larger multicenter study yields mixed/attenuated results relative to simple “more sun = better survival” readings. **Evidence: Moderate (association heterogeneity), Low (causality)**
  - [GEM study melanoma survival (PubMed abstract)](https://pubmed.ncbi.nlm.nih.gov/25069694/)

### What would change my mind?
- Studies that quantify UV dose and control detection pathways (screening, stage migration) and still show a robust survival benefit with a plausible mediator chain.

---

## UV promotes cancer: internal

### Net assessment
Most internal organs are centimeters below the body surface. In skin, UV penetrates in a strongly wavelength-dependent way: longer-wavelength ultraviolet A (UVA) reaches into the dermis, while ultraviolet B (UVB) is largely absorbed in the epidermis. This geometry makes direct irradiation of deep visceral organs by environmental UV photons physically constrained, while leaving room for direct effects in superficial compartments (epidermis, dermis, superficial vasculature, and the eye). **Evidence: High (for the physical constraint), Low (for direct visceral-organ UV effects)**

Two useful ways to think about “how much reaches deep tissue”:
- Light intensity in tissue typically falls roughly exponentially with depth. If a wavelength has a 1/e attenuation depth of even 1 mm, then at 10 mm depth the intensity is reduced by a factor of about \(e^{-10}\) (≈ 1/22,000) relative to the surface; at multi-centimeter depths it is effectively extinguished for most practical purposes. The actual attenuation depth depends on wavelength and tissue optics.
- Published skin photobiology reviews and in vivo measurements emphasize this UVA-vs-UVB stratification rather than any meaningful delivery of UV to deep organs.  
  - [UV Radiation and the Skin (review; full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3709783/)  
  - [Wavelength-dependent UV penetration depths in human skin (290–341 nm) (PubMed)](https://pubmed.ncbi.nlm.nih.gov/19021357/)

This does not exclude direct UV effects in special cases (thin tissues, unusual exposure geometries, ocular transmission differences with age/lens status), but it shifts the default internal-cancer discussion toward indirect mechanisms (vitamin D axis, skin-derived mediators, behavior/circadian coupling) unless a specific direct-penetration pathway is demonstrated.

### What would change my mind?
- Reproducible individual-level data showing increased internal-cancer incidence with quantified personal UV dose after strong control for confounding and reverse causation.

---

## UV negates cancer: internal

### Net assessment
Inverse associations are reported for some endpoints in some settings, but causal interpretation is fragile because confounding and measurement error are large. **Evidence: Low–Moderate (endpoint-dependent)**

### Latitude / ambient-UV proxy signals
- **US ecological ambient UVB vs cancer incidence/mortality (1993–2002)**: reports inverse associations for multiple internal cancer sites in non-Hispanic whites and positive associations for melanoma; ecological design cannot resolve individual causality. **Evidence: Moderate (association), Low (causality)**
  - [Boscoe & Schymura 2006, BMC Cancer (full text)](https://bmccancer.biomedcentral.com/articles/10.1186/1471-2407-6-264)
- **US solar radiation vs leading cancers**: another ecological mapping approach showing north–south gradients for some endpoints; interpretation limited by aggregation and correlated geography. **Evidence: Moderate (association), Low (causality)**
  - [Ecological mapping paper (full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4862378/)
- **Ecological fallacy caution**: this is not only “confounding exists.” It is a cross-level inference problem: region-level summaries usually do not contain enough information to recover the individual-level UV–cancer relationship.
  - Region-level analyses relate **group averages** (or totals) such as `mean_cancer_rate_in_region` to `mean_ambient_UV_in_region`. The individual-level question is about how a person’s risk changes as that person’s UV exposure changes.
  - The missing information is the **within-region** association. A useful identity is the covariance decomposition:

```plain text
Cov(Y, X) = Cov(E[Y | region], E[X | region])  +  E[ Cov(Y, X | region) ].

Ecological maps/regressions mostly use the first term (between-region).
Individual-level effects depend on the second term (within-region).
```

  - Many different individual-level realities can produce the same region averages, so the individual-level slope is often not identifiable from ecological data without strong assumptions.
  - Confounding is one common reason the between-region term differs from the within-region term, but even with “perfect” region-level covariates, aggregation can still mislead because the within-region joint distribution is not observed.
  - [Ecologic fallacy methodological discussion (AJPH)](https://ajph.aphapublications.org/doi/abs/10.2105/AJPH.84.5.819)

### Individual-level observational signals (example: lymphoid malignancies)
- **InterLymph pooled analysis**: pooled case-control data; higher personal sun exposure associated with lower NHL risk in the pooled model; directionality remains sensitive to confounding and measurement choices. **Evidence: Moderate (association), Low (causality)**
  - [InterLymph pooled analysis (PubMed)](https://pubmed.ncbi.nlm.nih.gov/17708556/)
  - [InterLymph pooled analysis (journal page)](https://onlinelibrary.wiley.com/doi/10.1002/ijc.23003)
- **Nurses’ Health Study NHL analysis**: cohort framework; provides a counterpoint showing that different UV proxies and populations can produce different associations. **Evidence: Moderate**
  - [Nurses’ Health Study NHL analysis (full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3240999/)

### Confounders and alternative explanations for inverse associations
- **Outdoor activity / baseline health**: healthier people go outside more; prodromal illness reduces sun exposure (reverse causation).
- **Latitude proxies**: latitude correlates with infections, diet, socioeconomic structure, and screening patterns.
- **Mediation ambiguity**: UV may correlate with vitamin D, circadian phase, activity, and metabolic health; UV may not be the active cause.

### What would change my mind?
- Designs that break the confounding triangle: strong instruments (credible UVA/UVB-specific instruments), quasi-experiments, or RCT-like natural experiments with measured personal UV dose and robust sensitivity analyses.

---

## Vitamin D evidence that constrains “UV negates internal cancer” stories

### Net assessment
- Vitamin D supplementation has not shown a clear reduction in **total cancer incidence** in major trials. **Evidence: High**
- Meta-analyses suggest a modest reduction in **cancer mortality** with supplementation in some designs (often daily dosing). **Evidence: Moderate–High**
- Mendelian randomization generally does not support a large causal effect of lifelong higher 25(OH)D on many cancer risks. **Evidence: Moderate–High**

### Observational evidence (25-hydroxyvitamin D in blood vs cancer outcomes)
Prospective observational studies often report that lower baseline 25-hydroxyvitamin D is associated with higher cancer mortality (and weaker/mixed associations for incidence). This is correlation, not a randomized causal test. **Evidence: Moderate (association), Low–Moderate (causality)**

- [Meta-analysis of prospective cohort studies (total cancer incidence and mortality) (PDF)](https://mdpi-res.com/d_attachment/nutrients/nutrients-11-02295/article_deploy/nutrients-11-02295.pdf?version=1569491230)
- [Vitamin D and Clinical Cancer Outcomes: A Review of Meta-Analyses (full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7839823/)

Confounding and reverse-causation pathways that can generate “low vitamin D ↔ worse cancer” correlations:
- lower outdoor time and physical activity → lower 25-hydroxyvitamin D and worse baseline health
- higher adiposity → lower measured 25-hydroxyvitamin D and higher cancer risk (multiple pathways)
- smoking, diet quality, alcohol use, sleep/circadian stability → correlate with both vitamin D status and cancer risk
- comorbidity and inflammation → lower 25-hydroxyvitamin D and higher mortality risk
- preclinical illness → reduced outdoor time/appetite → lower 25-hydroxyvitamin D before diagnosis

### Randomized trials
- **VITAL randomized controlled trial (RCT)**: vitamin D3 2000 IU/day did not significantly reduce invasive cancer incidence in the primary analysis. **Evidence: High**
  - [Manson et al., Vitamin D Supplements and Prevention of Cancer and Cardiovascular Disease (NEJM, 2019; VITAL primary)](https://www.nejm.org/doi/full/10.1056/NEJMoa1809944)
- **RCT meta-analysis**: pooled randomized trials show little/no effect on total cancer incidence but a modest reduction in cancer mortality in some analyses. **Evidence: Moderate–High**
  - [Keum et al., Vitamin D supplementation and total cancer incidence and mortality: a meta-analysis of randomized controlled trials (Annals of Oncology, 2019; full text)](https://www.annalsofoncology.org/article/S0923-7534(19)31159-7/fulltext)

### Mendelian randomization
- **Large-scope Mendelian randomization (MR) reassessment**: generally null for cancer susceptibility across many cancers; highlights how pigmentation-related traits can contaminate simple causal readings for skin endpoints. **Evidence: Moderate–High**
  - [Huang et al., A comprehensive re-assessment of the association between vitamin D and cancer susceptibility using Mendelian randomization (Nature Communications, 2020)](https://www.nature.com/articles/s41467-020-20368-w)

### Key inference point
Even if vitamin D has small causal effects, sunlight could still correlate with outcomes via:
- non–vitamin D pathways (e.g., UVA-weighted mediators),
- or non-UV confounding (activity, circadian stability).

### Skin synthesis via ultraviolet B vs oral supplementation
Vitamin D evidence is often misread as “a trial of pills tested sunlight.” It did not.

- Even within “vitamin D biology only,” **oral supplementation is not equivalent to ultraviolet B–driven skin synthesis**: the entry route (skin vs gut), kinetics (pulsed UV vs chosen dosing regimen), the possibility of D2 vs D3, and the skin’s photoregulatory ceiling make the physiological input non-identical even if the 25-hydroxyvitamin D blood level ends up similar.

- **Ultraviolet B synthesis**: in skin, ultraviolet B converts 7-dehydrocholesterol into vitamin D3, which is then processed in the liver to 25-hydroxyvitamin D and in the kidney and other tissues to active forms. This process co-occurs with other sunlight-linked inputs (ultraviolet A exposure, behavior, circadian phase, and skin biology).  
  - [NIH Office of Dietary Supplements: Vitamin D fact sheet for health professionals](https://ods.od.nih.gov/factsheets/vitamind-HealthProfessional/)
- **Oral supplementation**: pills change circulating vitamin D metabolites without reproducing the ultraviolet spectrum, skin photochemistry, or the behavioral/circadian correlates of being outdoors. Dosing pattern (daily vs bolus), baseline deficiency, adherence, and assay variability can further separate trial results from observational “sun exposure” associations.

### What would change my mind?
- Replicated trials showing clear incidence reductions in specific cancers, or MR results that remain robust under multivariable adjustment for pigmentation/behavioral traits and across populations.

---

## Lab evidence that bridges UV, melanin, and cancer-relevant intermediates

### Net assessment
Lab models establish mechanisms (DNA lesions, oxidative chemistry, melanogenesis dynamics, cell-state transitions) but translate imperfectly to long-latency human cancers. **Evidence: High for mechanism, Moderate for human endpoint translation**

### Core mechanistic anchors (primary references)
- **Ultraviolet signature mutations connect sunlight to tumor genomes**: reviews the defining mutation pattern (C→T at dipyrimidines, including CC→TT) and how it is established from experimental UV exposures and then read back in tumors.  
  - [Brash, UV Signature Mutations (Photochem Photobiol, 2015; full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4294947/)
- **Ultraviolet A can drive delayed cyclobutane pyrimidine dimer formation via melanin chemiexcitation**: shows “dark CPDs” continue forming for hours after UVA exposure in melanocytes, providing a concrete melanin-linked mechanism that is not simple UVB photoproduct formation.  
  - [Premi et al., Chemiexcitation of melanin derivatives induces DNA photoproducts long after UV exposure (Science, 2015; full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4432913/)
- **Melanocortin 1 receptor signaling enhances DNA repair in melanocytes via cAMP pathways**: demonstrates that cAMP signaling can augment nucleotide excision repair independently from pigment induction, linking pigmentation genetics to repair kinetics after UV injury.  
  - [Wolf Horrell et al., Divergence of cAMP signaling pathways mediating augmented nucleotide excision repair and pigment induction in melanocytes (Exp Dermatol, 2017; full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5507718/)
- **Pheomelanin / red-hair genetic background can promote melanoma beyond UV shielding**: in a mouse model, melanoma formation occurs in the “red hair/fair skin” background in a manner interpreted as partly ultraviolet-radiation-independent, implicating pigment chemistry and oxidative damage pathways.  
  - [Mitra et al., A UV-independent pathway to melanoma carcinogenesis in the redhair-fairskin background (Nature, 2012; full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3521494/)

### What lab evidence is weak at
- Predicting net human incidence/mortality without embedding realistic exposure patterns, immune context, and selection over years.

### What would change my mind?
- Bridging studies that couple realistic spectra/dose patterns, measured intermediate biomarkers (DNA lesions + repair + Vmem/pHi/ΔΨm where relevant), and long-term tumor outcomes in models with human-relevant pigmentation biology.
  - Here, Vmem is membrane potential, pHi is intracellular pH, and ΔΨm is mitochondrial membrane potential.

---

## UV negates cancer: skin (clinical therapy analogs)

### Net assessment
- **Claim A (specific, testable)**: In a small set of skin-limited malignancies, controlled ultraviolet-based phototherapy is an established treatment modality that can induce clinical responses in the skin. **Evidence: Moderate–High**
- **Claim B (generalization)**: This does not imply that sunlight/UV exposure is a broadly curative cancer therapy across cancers or internal disease. Comparable clinical evidence for “UV cures cancer” in general is not established. **Evidence: Low**

### Phototherapy analog: early-stage mycosis fungoides (cutaneous T-cell lymphoma)
- For early-stage, skin-limited cutaneous T-cell lymphoma (mycosis fungoides), skin-directed phototherapy is a standard option in guidelines and reviews.
  - [EORTC consensus recommendations (update 2023; full text)](https://www.ejcancer.com/article/S0959-8049(23)00645-7/fulltext)
  - [NCI PDQ: Mycosis Fungoides and the Sézary Syndrome Treatment](https://www.ncbi.nlm.nih.gov/books/NBK65849/)
- **Comparative evidence**: systematic review/meta-analysis comparing **narrowband UVB (around 311 nm)** vs **PUVA (psoralen + UVA)** for early-stage mycosis fungoides. **Evidence: Moderate**
  - [JAMA Dermatology systematic review/meta-analysis](https://jamanetwork.com/journals/jamadermatology/fullarticle/2722559)
  - [Cochrane review: interventions overview (full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7389258/)

Important constraint:
- PUVA is also a carcinogenic exposure with cumulative-dose risks (especially cutaneous squamous cell carcinoma), illustrating pleiotropy and endpoint separation. **Evidence: High**
  - [Stern et al., PUVA cohort signal (NEJM)](https://www.nejm.org/doi/full/10.1056/NEJM198405033101805)
  - [Long-term PUVA cohort follow-up (J Natl Cancer Inst)](https://academic.oup.com/jnci/article/90/17/1278/908156)

### What would change my mind?
- Replicated clinical outcome improvements tied to quantified UV dose/spectrum and a plausible intermediate biomarker chain (or clear phototherapy analogs beyond skin-limited contexts).

