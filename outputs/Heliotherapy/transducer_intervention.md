# Light-Driven Melanin Electrophysiology — Intervention

Targeted light delivery to melanin-containing tumor tissue, with the goal of shifting the tumor's electrical state away from the cancer-permissive phenotype. Melanin in melanosomes absorbs photons, which shifts the polymer's charge and proton state at the organelle surface, propagating into changes in whole-cell membrane potential and intracellular pH. Cancer cells are characteristically depolarized with alkaline intracellular pH — both features that support proliferation. The intervention targets both in the opposite direction.

This is not photodynamic therapy. There is no photosensitizer, no cytotoxic ROS burst, no cell killing. The dose limit is thermal safety to surrounding tissue. The endpoint is a shift in cellular state, not necrosis.

---

## What Is Being Measured and What We Are Optimizing

| Readout | What it captures | Target | Evidence basis | Method | Timing |
|---------|-----------------|--------|---------------|--------|--------|
| FDG-PET | Tumor glycolytic rate | Reduction from baseline | Metabolic shift consistent with Vmem repolarization | PET scan | Before and after protocol |
| Ki-67 (biopsy) | Tumor proliferation rate | Reduction from baseline | Standard oncology proliferation marker | Immunohistochemistry on biopsy | Before and after protocol |
| RECIST | Tumor size | Reduction or stable disease | Standard response assessment | CT/MRI | Per standard oncology schedule |

None of these are direct measures of the electrophysiological mechanism. They are clinical response indicators — the mechanistic measurements (Vmem, pHi) are only accessible in preclinical models.

**Primary benchmark:** reduction in FDG-PET uptake. Most sensitive to metabolic state change and earliest to reflect a shift if the mechanism is operating.

---

## Intervention Definition

**What:** Targeted light delivery to melanin-containing tumor tissue, wavelength selected by lesion depth, dosed to achieve photon saturation of the melanin without thermal damage to surrounding tissue.

**Wavelength by depth:**

| Lesion depth | Wavelength | Rationale |
|-------------|------------|-----------|
| Surface (dermis/epidermis) | UVA 315–400 nm | Peak melanin absorption |
| 1–3 mm | 405–450 nm | Violet/blue; tissue penetration at shallow depth |
| Deeper lesion | 630–680 nm | Red light penetrates to ~1 cm |

**Who is excluded:** Tumors without confirmed melanin (amelanotic melanoma, non-melanocytic tumors without biopsy-confirmed melanin). Confirmation required before proceeding.

---

## Protocol

| Step | Action | Detail |
|------|--------|--------|
| 1. Confirm melanin | T1-MRI (internal/metastatic), dermoscopy (surface), or biopsy | No melanin confirmed = do not proceed |
| 2. Select wavelength | Match to lesion depth using table above | |
| 3. Dose | Deliver to melanin-containing cells; titrate against thermal safety | Exact fluence parameters not yet established — requires preclinical program |
| 4. Track response | FDG-PET, Ki-67, RECIST per schedule above | |

---

## Evidence Summary

| Claim | Evidence quality |
|-------|-----------------|
| Melanin is a mixed ionic-electronic conductor; photon absorption shifts charge state | High — Mostert et al. PNAS 2012 |
| Melanosomal pH regulates melanin polymerization and proton dynamics | High — Bellono et al. eLife 2014 |
| Vmem and pHi are determinants of cancer cell proliferation and differentiation | High — Levin & Martyniuk, Biosystems 2018 |
| Light-driven Vmem shift in melanin-containing cells (cancer model) | Not yet demonstrated — preclinical gap |

---

## Preclinical Requirements

The mechanism is theoretically grounded but the key coupling steps have not been demonstrated in cells. Seven sequential experiments are required before clinical use — testing melaninated vs. non-melaninated cells, cancer vs. healthy, across full-spectrum / UVA / IR illumination conditions, measuring Vmem, pHi, melanosomal pH, and carcinogenic profile.
