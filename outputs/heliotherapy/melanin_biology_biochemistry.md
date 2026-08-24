# Melanin Biology & Biochemistry

---

## Bottom Line

Melanin is not a pigment — it's a disordered, heterogeneous polymer that absorbs almost everything and releases almost nothing. Its defining property is **near-perfect internal energy conversion**: >99.9% of absorbed photons are dissipated as heat within picoseconds, before they can generate reactive oxygen species. That physical fact — not any single enzyme or gene — is what makes melanin the most effective biological sunscreen known. It is synthesized inside a dedicated organelle (the melanosome), trafficked by a dedicated cytoskeletal motor, and exported to neighboring cells that never synthesize it themselves. Neuromelanin is made by a completely different mechanism, accumulates over a lifetime with no known clearance route, and protects neurons until it becomes the trigger for their death.

---

## What Melanin Actually Is

Melanin is not a defined molecule. It is a family of **high-molecular-weight, amorphous polymers** built from oxidized indole and pyrrole units, crosslinked irregularly into a three-dimensional network that resists crystallization, hydrolysis, and most chemical analysis. The key building blocks for eumelanin are **5,6-dihydroxyindole (DHI)** and **5,6-dihydroxyindole-2-carboxylic acid (DHICA)** — oxidized and coupled in variable patterns. No two melanin polymer chains are identical.

Why does this matter? Because the polymer's **chemical and structural disorder is not a defect — it is the functional feature**. The heterogeneous conjugated system produces a broadband, featureless absorption spectrum from UV through visible and into the near-infrared. Sharp molecular transitions would mean sharp peaks and photochemical reactivity. The smear of overlapping chromophores is what produces flat, efficient absorption across all wavelengths.

The polymer also contains **stable semiquinone free radicals** — detectable by EPR at g ≈ 2.004 — embedded throughout the structure. These radicals are thermodynamically stable (not reactive), and the radical density correlates with eumelanin content. They are the basis of all EPR-based melanin detection methods, and they contribute to the antioxidant capacity via radical-radical quenching.

![Eumelanin polymer structure — DHI and DHICA building blocks crosslinked into the heterogeneous aromatic network](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Eumelanine.svg/600px-Eumelanine.svg.png)
*Eumelanin — DHI and DHICA units polymerized into the irregular, highly conjugated polymer backbone. The disorder is structural: no defined repeating unit, variable crosslinking. Source: Wikimedia Commons.*

![Melanin ball-and-stick 3D model](https://upload.wikimedia.org/wikipedia/commons/7/7b/Melanin_ball_and_stick.png)
*Ball-and-stick 3D representation of the eumelanin polymer. The extended aromatic system (blue/grey) provides the broadband absorption. Source: Wikimedia Commons.*

---

## Three Melanins, Three Different Chemistries

These are not just color variants — they are chemically distinct compounds with different synthesis routes, physical properties, and biological behaviors.

**Eumelanin (brown-black)**
DHI/DHICA-derived polymer. Dominant in dark skin, dark hair, retinal pigment epithelium. Strongest UV absorber; highest free radical density; best photoprotection per unit mass. Contains iron and copper ions sequestered in the polymer matrix.

**Pheomelanin (yellow-red)**
Requires cysteine + dopaquinone → cysteinyldopa → benzothiazine/benzothiazole units. Dominant in red hair, light skin. Pheomelanin is **phototoxic under UV** — it absorbs and reacts rather than dissipating, generating superoxide, H₂O₂, and singlet oxygen under UVA.

Pheomelanin carries two distinct liabilities. The first is UV-amplified: photolysis generates ROS. The second is UV-independent: pheomelanin synthesis consumes cysteine, a key glutathione precursor, reducing antioxidant buffering capacity in melanocytes regardless of light exposure. Both run at all times; UV amplifies the first but not the second. Mice with pheomelanin-dominant phenotype develop melanoma in complete darkness — demonstrating the UV-independent mutagenic baseline ([Mitra et al., Nature 2012](https://pmc.ncbi.nlm.nih.gov/articles/PMC3521494/)).

**Why pheomelanin exists.** Pheomelanin is not a UV-defense molecule and was not selected for photoprotection. It is a coloration molecule — producing yellow, red, and auburn pigmentation with independent selective value (mate signaling, camouflage in sandy environments, population differentiation). It coexists with the high-latitude adaptation for lighter skin: reduced MC1R signaling → higher pheomelanin → lighter, more reflective skin → better vitamin D synthesis at low UV angles. At the latitudes this phenotype evolved in, the UVA dose is low enough that pheomelanin's photochemical ROS output is tolerable. The liability emerges specifically when a pheomelanin-dominant phenotype encounters high UV — an ancestrally rare combination.

The eu:pheo ratio in skin determines not just color but net UV protection or damage per photon absorbed.

**Neuromelanin (dark brown)**
Not made by melanocytes, not made in melanosomes, not via the Raper-Mason pathway. It accumulates in midbrain dopaminergic and noradrenergic neurons from the **auto-oxidation of excess cytosolic catecholamines** (dopamine, norepinephrine) not captured by vesicles. The resulting polymer is embedded with lipids, proteins, and high iron loads (Fe³⁺ bound at a ratio of ~1 iron per 5 DHI units). Accumulates continuously from birth; there is no known degradation or clearance mechanism.

```
LOCATION: cytoplasm of substantia nigra / locus coeruleus neurons (midbrain)
─────────────────────────────────────────────────────────────────────────────

Excess cytosolic dopamine or norepinephrine
(not captured by synaptic vesicles)
    │
    ▼ auto-oxidation — NO TYR, NO DCT, NO TYRP1
Dopamine/norepinephrine quinones
    │
    ▼ spontaneous polymerization
    + lipids + proteins + Fe³⁺ accumulates (~1 Fe per 5 DHI units)
    │
    ▼
NEUROMELANIN granule
stored in autophagic double-membrane organelle (NOT a melanosome)
    │
    ├── neuroprotective while neuron survives
    │   (sequesters Fe²⁺, prevents Fenton chemistry)
    │
    └── neurotoxic when neuron dies
        released NM activates:
          → NLRP3 inflammasome (via Fe release)
          → TLR4 (via polymer surface)
          → complement cascade (via opsonization)
        → microglial phagocytosis → neuroinflammation → PD propagation

─────────────────────────────────────────────────────────────────────────────
```

![Pheomelanin polymer structure — cysteine-derived benzothiazine units](https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Pheomelanine.svg/600px-Pheomelanine.svg.png)
*Pheomelanin — benzothiazine/benzothiazole units from cysteine + dopaquinone condensation. Unlike eumelanin, this polymer generates ROS under UV rather than absorbing it. Source: Wikimedia Commons.*

---

## Synthesis: The Raper-Mason Pathway

All enzymatic melanin synthesis runs through a single gateway reaction: **L-Tyrosine → L-DOPA → Dopaquinone**, both catalyzed by **tyrosinase (TYR)**. Dopaquinone is the last regulated intermediate; everything downstream is either spontaneous or handled by accessory enzymes.

**Location: inside the melanosome lumen** (melanocyte). TYR, TYRP1, and DCT are all transmembrane melanosomal enzymes — their active sites face the lumen. Synthesis never occurs in the cytoplasm.

```
LOCATION: melanosome lumen (melanocyte)
─────────────────────────────────────────────────────────────
L-Tyrosine
    │
    ▼ [TYR — tyrosinase]
L-DOPA
    │
    ▼ [TYR]
Dopaquinone  ◄── last regulated step
    │
    ├──────────────────────────────────────────────┐
    │  no free cysteine available                  │  free cysteine present
    │                                              │
    ▼ (spontaneous)                                ▼
Leucodopachrome                             Cysteinyldopa
    │                                              │
    ▼ (spontaneous)                                ▼ (oxidation + cyclization)
Dopachrome                                  Benzothiazine / benzothiazole units
    │                                              │
    ├──────────────────┐                           ▼
    │                  │                    PHEOMELANIN (yellow-red)
    ▼ [DCT/TYRP2]      ▼ (spontaneous)      phototoxic under UV — generates ROS
  DHICA               DHI
    │                  │
    ▼ [TYRP1]          ▼ (spontaneous)
 oxidized          oxidized
    │                  │
    └────────┬──────────┘
             ▼
        EUMELANIN (brown-black)
        photoprotective — dissipates UV as heat
─────────────────────────────────────────────────────────────
```

The **eu:pheo ratio** is set by free cysteine availability. More cysteine → more pheomelanin → less UV protection, more ROS under UV. This ratio is the key determinant of photoprotective vs. phototoxic outcome.

![Raper-Mason melanin synthesis pathway — from tyrosine through dopaquinone to eumelanin and pheomelanin](https://upload.wikimedia.org/wikipedia/commons/4/4f/Pepmel_pathway.jpg)
*Raper-Mason pathway. Tyrosine → DOPA → dopaquinone (TYR). Eumelanin route (left): via leucodopachrome, dopachrome, DHI/DHICA. Pheomelanin route (right): cysteine addition at dopaquinone → benzothiazine units. Key enzymes: TYR, DCT, TYRP1. Source: Wikimedia Commons.*

---

## The Master Switch: MITF

**Microphthalmia-associated transcription factor (MITF)** is the single most important regulatory node in melanin biology. It directly drives expression of TYR, TYRP1, DCT, and the melanosome structural proteins (Pmel17/gp100, MART-1). No MITF → no melanosome biogenesis, no synthesis enzymes, no melanin.

Multiple parallel UV signals converge on MITF. Melanin synthesis is therefore not contingent on DNA damage — it is triggered directly by photon absorption through several independent channels.

```
LOCATION: starts in keratinocytes (epidermis), signal crosses to melanocytes (basal layer)
─────────────────────────────────────────────────────────────────────────────────────────

  UV photons
      │
      ├──────────────────────────────────────────────────────┐
      │ hits keratinocytes                                   │ hits melanocytes directly
      │                                                      │
      ▼                                                      ├──────────────────┐
  p53 activation                                             │                  │
      │                                                      ▼                  ▼
      ▼                                              c-Kit / SCF         Endothelin receptor
  POMC → α-MSH (secreted into dermis)                       │                  │
      │                                                      └────────┬─────────┘
      ▼ [paracrine]                                                   │
  MC1R on melanocyte surface                                          │
      │                                                               │
      ▼                                                               │
  adenylyl cyclase → cAMP → PKA → CREB                               │
      │                                                               │
      └───────────────────────────────┬───────────────────────────────┘
                                      │
                                      ▼
                              MITF activated  [LOCATION: melanocyte nucleus]
                                      │
                          ┌───────────┼───────────┐
                          ▼           ▼           ▼
                         TYR        TYRP1        DCT
                       expressed  expressed   expressed
                          │
                          ▼
                  melanosome biogenesis begins
─────────────────────────────────────────────────────────────────────────────────────────
```

Mutations in MITF cause Waardenburg syndrome (deafness + pigment loss). MITF amplification drives the most treatment-resistant melanomas. A single gene runs the entire program.

**The MC1R axis coordinates melanin synthesis and DNA repair simultaneously.** MC1R/cAMP/CREB signaling not only upregulates eumelanin synthesis and shifts eu:pheo ratio — it independently upregulates nucleotide excision repair (NER) capacity in melanocytes via the same CREB-dependent transcriptional program ([Wolf Horrell et al., Exp Dermatol 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5507718/)). The two processes are co-induced but mechanistically separable. This means eumelanin content is partly a proxy for the entire MC1R protective program: more eumelanin correlates with better eu:pheo ratio and better repair machinery for the DNA damage that does get through. The adaptive UV response is a coordinated program, not just pigment deposition.

![MITF protein 3D structure — the master transcriptional regulator of melanocyte differentiation and melanin synthesis](https://upload.wikimedia.org/wikipedia/commons/1/1d/MITF_protein.png)
*MITF protein 3D structure. The bHLH-LZ domain mediates DNA binding to E-box sequences in promoters of TYR, TYRP1, DCT, and melanosome structural proteins. Loss of MITF abolishes melanogenesis entirely. Source: Wikimedia Commons.*

---

## Chemiexcitation: The Dark CPD Mechanism

After UVA exposure, CPDs in melanocytes continue accumulating for hours — with the majority forming *after* the UV source is removed. These "dark CPDs" carry the same C→T mutation signature as direct UV photoproducts and occur specifically in melanocytes, not in adjacent keratinocytes ([Premi et al., Science 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4432913/)).

**Mechanism:**

```
UVA exposure ends
    │
    ├──────────────────────────────────┐
    │                                  │
    ▼                                  ▼
NOS activated in melanocyte      NADPH oxidase (NOX) activated
    │                                  │
    ▼                                  ▼
Nitric oxide (NO)              Superoxide (O₂•⁻)
    │                                  │
    └──────────────────┬────────────────┘
                       ▼
              Peroxynitrite (ONOO⁻)
                       │
                       ▼
    reacts with melanin synthesis intermediates
    (dopaquinone, DHI, their derivatives)
                       │
                       ▼
    Excited triplet carbonyl species
                       │
                       ▼
    Transfer of excitation energy to adjacent DNA pyrimidines
                       │
                       ▼
    CPD formation — without any photon (2–4 hrs post-UV)
```

This is chemiexcitation: a chemical pathway that produces an electronically excited state equivalent to UV photon absorption in DNA. It runs for hours because NOS and NOX activity persists after UV ends, and melanin synthesis intermediates are continuously available while melanogenesis is active.

**Key implications:**
- UV dose is an incomplete exposure metric for melanoma risk. The relevant variable includes the post-UV oxidative environment during recovery.
- Two individuals with identical UV dose but different antioxidant status (glutathione, NOS regulation) accumulate very different CPD burdens — a source of variance invisible to all epidemiological tools.
- This is not evidence against eumelanin protection. It is a second-order consequence of active melanin *synthesis* — not the mature polymer. Cells with substantial eumelanin already in place are protected; cells actively synthesizing in response to UV generate the reactive intermediates. The same UV signal that leads to more protection with the finished product generates a transient mutagenic byproduct during the manufacturing process.
- The post-UV antioxidant state is a targetable window: peroxynitrite scavenging, glutathione maintenance, and NOS/NOX modulation all affect the dark CPD burden per UV event.

---

## Melanosome Biology: A Dedicated Organelle

Melanin is never synthesized in the cytoplasm. It is made inside the **melanosome** — a lysosome-related organelle (LRO) that provides the acidic, metal-rich, enzyme-loaded environment required for controlled polymerization. Free melanin polymer in the cytosol would be catastrophic: it would crosslink proteins, chelate essential metals, and generate radical cascades.

```
LOCATION: melanocyte cytoplasm — organelle trafficking from trans-Golgi to dendrite tip
─────────────────────────────────────────────────────────────────────────────────────────

trans-Golgi network
    │
    ▼  Pmel17/gp100 sorted out
STAGE I — clathrin-coated vesicle
    │      intralumenal vesicles form
    │      fibrillar scaffold begins on vesicle membranes
    │
    ▼  TYR, TYRP1, DCT arrive (via AP-3 + BLOC-1/2/3 sorting complexes)
STAGE II — elongated ellipsoid
    │       dense Pmel17/MART-1 fibrillar matrix (amyloid-like fibrils)
    │       NO melanin yet — scaffold only
    │
    ▼  TYR becomes active; synthesis begins
STAGE III — melanin deposition starts
    │        DHI/DHICA polymerize on fibrillar template
    │        fibrils become electron-dense
    │
    ▼  synthesis complete
STAGE IV — fully opaque melanosome
             fibrils obscured by melanin mass
             ready for export

─────────────────────────────────────────────────────────────────────────────────────────
```

The Pmel17 fibrillar scaffold is not passive — it is the template on which polymerization is physically organized. It self-assembles into amyloid-like fibrils in the acidic lumen — one of the very few known beneficial amyloids in biology.

**Melanosome biogenesis — four stages:**

| Stage | Contents | What happens |
|---|---|---|
| I | Clathrin-coated vesicle; intralumenal vesicles; fibrillar scaffold beginning | Pmel17/gp100 sorted from trans-Golgi; fibrils begin forming on ILV membranes |
| II | Elongated ellipsoid; dense fibrillar matrix (Pmel17, MART-1); no melanin yet | Fibrillar scaffold complete; TYR, TYRP1, DCT arrive via AP-3 and BLOC complexes |
| III | Melanin deposition begins; fibrils become electron-dense | TYR active; DHI/DHICA polymerize on fibrillar template |
| IV | Fully opaque; fibrils obscured by melanin mass | No further synthesis; mature melanosome ready for export |

![TEM of human melanoma cells — all four stages of melanosome development visible](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/5fa0/2786984/074c36b99929/nihms154774f1.jpg)
*TEM of MNT-1 human melanoma cells (high pressure freezing, cryosubstitution). Stage I: bilayered coat + intralumenal vesicles (arrows). Stage II: proteinaceous fibrils (arrows). Stages III–IV: progressive melanin deposition until fully opaque. Bar = 0.5 µm. [Raposo & Marks, Nat Rev Mol Cell Biol 2007]*

![Model of melanosome maturation — trafficking, sorting, and organelle development from stage I to IV](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/5fa0/2786984/7c888040ca59/nihms154774f4.jpg)
*Model of melanosome maturation. Stage I precursors derive from early endosomes. Cargo (TYR, TYRP1, DCT) is sorted by AP-3 and BLOC-1/2/3 complexes. Stage IV melanosomes are transported to dendrite tips via microtubule motors and captured by **Myosin Va** on F-actin for peripheral positioning. [Raposo & Marks, Nat Rev Mol Cell Biol 2007]*

---

## Transfer: The Melanin Gets Exported

A fully loaded Stage IV melanosome is useless inside the melanocyte. Its job is photoprotection of keratinocyte DNA — cells that produce no melanin themselves. One melanocyte supplies 30–40 keratinocytes via its dendrites.

```
LOCATION: melanocyte dendrite tip → keratinocyte (basal layer of epidermis)
─────────────────────────────────────────────────────────────────────────────

Stage IV melanosome
    │
    ▼  transported along microtubules toward dendrite tip
    │  captured by Myosin Va on F-actin for final peripheral positioning
    │
    ├──────────────────────────────────────────────────┐
    │ dominant route (human skin)                      │ UV-triggered route
    │                                                  │
    ▼                                                  ▼
Melanocyte releases melanosome cores          Ca²⁺-dependent lysosomal exocytosis
    │                                         releases melanin-containing EVs
    ▼                                                  │
Keratinocyte engulfs them via                          ▼
PAR-2-dependent phagocytosis                  Keratinocyte takes up EVs
(Rac1, Cdc42, RhoA actin remodeling)                  │
    │                                                  │
    └──────────────────────┬───────────────────────────┘
                           │
                           ▼  LOCATION: inside keratinocyte
                 Rab5b non-degradative endosome
                 (melanin NOT digested — persists long-term)
                           │
                           ▼
                 Supranuclear cap assembled
                 polarized shield over nucleus
                 oriented toward skin surface
                           │
                           ▼
                 UV photoprotection of keratinocyte DNA

─────────────────────────────────────────────────────────────────────────────
```

![Micrograph of keratinocytes, basal melanocytes and suprabasal keratinocytes in the epidermis](https://upload.wikimedia.org/wikipedia/commons/c/c3/Micrograph_of_keratinocytes%2C_basal_cells_and_melanocytes_in_the_epidermis.jpg)
*Histological cross-section of human epidermis. Melanocytes (pale, dendritic) at the basal layer supply melanin to surrounding keratinocytes, which carry it into the suprabasal layers as they differentiate and migrate upward. Source: Wikimedia Commons.*

---

## Physical Properties: Why Melanin Is Interesting Beyond UV

**Broadband absorption, no peaks**
Eumelanin absorbs from 200 nm into the near-infrared with no sharp spectral features. Absorption coefficient increases monotonically toward shorter wavelengths. This is the fingerprint of a disordered heterogeneous polymer — no defined transitions, just an ensemble of overlapping chromophores. In vivo, this means melanin absorbs UV, visible light, and near-IR heat.

**Ultrafast energy dissipation**
Photoexcited eumelanin relaxes to the ground state in **<1 picosecond** via internal conversion — one of the fastest known processes in biological molecules. This means the absorbed energy is converted to heat before any photochemical reaction (ROS generation, DNA damage) can occur. This is the primary photoprotective mechanism, not radical scavenging.

**Stable free radicals**
The semiquinone radicals embedded in the polymer are EPR-detectable (g ≈ 2.004) and thermodynamically stable. They can participate in redox reactions — donating or accepting electrons — and this underlies the antioxidant/pro-oxidant duality: melanin is an antioxidant in low-oxidative-stress environments, but may act as a pro-oxidant under photolysis or very high UV dose.

**Metal chelation**
Melanin has high-affinity binding sites for di- and trivalent metals — Fe²⁺/³⁺, Cu²⁺, Zn²⁺, Mn²⁺. In RPE melanin, iron accumulates with age, progressively converting the antioxidant polymer into a Fenton-chemistry substrate. This metal-loading dynamic — not melanin per se — is thought to contribute to AMD. In neuromelanin, iron binding is both neuroprotective (sequestering redox-active Fe²⁺) and the mechanism by which released NM upon neuronal death triggers neuroinflammation.

**Electrical properties**
Melanin is a mixed ionic–electronic conductor. It conducts protons along the polymer via a quinone/hydroquinone hydrogen-bonding network and has semiconductor-like electrical conductivity (~10⁻¹⁰ S/cm, orders of magnitude below metals). These properties have driven interest in melanin as a biocompatible electronic material, and they underlie Kruse's "quantum semiconductor" model and Herrera's "water-splitting" claims — neither of which have been demonstrated in physiological systems.

---

## Functions: What Is Agreed vs. What Is Claimed

| Function | Status | Evidence quality |
|---|---|---|
| UV photoprotection (DNA shielding in keratinocytes) | Mainstream, well-established | Supranuclear cap structure, sunburn cell data, epidemiological skin cancer data |
| ROS scavenging / antioxidant | Mainstream, accepted | In vitro EPR, cell culture, HPLC-AHPO radical quenching assays |
| Metal sequestration (RPE, neuromelanin-Fe) | Mainstream, accepted | TEM-EDX, HPLC-metal studies, iron quantification in aging RPE |
| Thermoregulation (heat from light absorption) | Plausible, under-studied | Photoacoustic heat generation well-characterized in vitro |
| Hearing / cochlear function | Emerging | Stria vascularis melanocytes linked to K⁺ recycling, deafness in albinos |
| Cardiac rhythm (cardiac melanocytes) | Emerging | JCI 2009; animal models; mechanism unclear |
| Water photolysis for cellular energy | Fringe (Herrera) | No replication; mechanism violates known photochemistry |
| Quantum energy transduction, mitochondrial bypass | Fringe (Kruse) | No experimental demonstration in mammalian systems |

---

## Neuromelanin: A Different Beast

Neuromelanin (NM) defies the melanocyte model on every axis:

- **No TYR, no TYRP1, no DCT** — synthesized by the non-enzymatic auto-oxidation of cytosolic dopamine/norepinephrine
- **No melanosome** — stored in autophagic, double-membrane-bound granules with a heterogeneous lipid-protein-polymer matrix
- **Not transferred** to neighboring cells
- **Accumulates from birth**, no clearance, linear increase over lifetime
- **Iron-loaded**: Fe³⁺ at ~1 per 5 DHI equivalents; also contains neuromelanin-associated proteins (NM-AP), including markers of mitochondrial dysfunction
- **Neuroprotective while neurons survive** (sequesters Fe²⁺ away from Fenton chemistry) — and **neurotoxic when neurons die** (released NM triggers NLRP3 inflammasome activation and microglial phagocytosis cascade)

This means NM is simultaneously the reason SN/LC neurons survive for decades under high dopamine flux, and the reason their death is inflammatory rather than silent.

![Neuromelanin granules in a dopaminergic neuron of the substantia nigra — dark brown autophagic organelles](https://upload.wikimedia.org/wikipedia/commons/4/48/Neuromelanin_in_a_neuron_of_the_substantia_nigra.jpg)
*Neuromelanin in a substantia nigra dopaminergic neuron — dark brown intracytoplasmic granules, visible without staining. These accumulate throughout life, contain iron, and are associated with mitochondria-derived proteins. Source: Wikimedia Commons.*

---

## Degradation and Fate

**In the epidermis:** Melanosomes in keratinocytes are partly degraded as cells differentiate and migrate upward. The mechanism is disputed — some compartments are non-degradative (persisting in corneocytes) and others are cleared by lysosomal proteolysis. By the stratum corneum, most melanin is dispersed from granules, and it is shed with the dead keratinocytes.

**In the dermis:** When melanocytes die or melanosomes are released extracellularly (UV damage, inflammation), dermal macrophages phagocytose the free melanin, becoming **melanophages**. These carry melanin through lymphatics to regional lymph nodes — a documented systemic clearance route. Melanophage-laden lymph nodes are visible to the naked eye in melanocytic disease.

**In the brain:** Neuromelanin has **no clearance mechanism**. It accumulates from ~3 years of age through adulthood. In normal aging, NM levels plateau in late life as SN neuron density naturally declines. In Parkinson's disease, residual neurons have paradoxically *higher* NM concentrations, detectable by NM-MRI — because the neurons that die first tend to be the less-pigmented ones (lower NM, less buffering against dopamine oxidative stress), so the surviving population is progressively enriched for heavily NM-loaded cells. Released NM from dead neurons activates microglia and astrocytes: **NLRP3 inflammasome** via Fe release; **TLR4** via polymer surface; **complement cascade** via opsonization. This is why PD pathology, once initiated, propagates.

---

## References

1. [Raposo & Marks — Melanosomes: dark organelles enlighten endosomal membrane transport, Nat Rev Mol Cell Biol 2007](https://pmc.ncbi.nlm.nih.gov/articles/PMC2786984/)
2. [Melanin transfer in the epidermis, IJMS 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8123122/)
3. [Moreiras et al. — Melanocore uptake by keratinocytes, Traffic 2022](https://run.unl.pt/bitstream/10362/140396/1/Traffic_2022_Moreiras_Melanocore_uptake_by_keratinocytes_occurs_through_phagocytosis_and_involves_protease_activated.pdf)
4. [Melanin Transferred to Keratinocytes Resides in Nondegradative Endocytic Compartments, JID 2017](https://www.jidonline.org/article/S0022-202X(17)33065-8/fulltext)
5. [Borovanský & Riley — Melanins and Melanosomes (book synthesis)](https://pubmed.ncbi.nlm.nih.gov/22154051/)
6. [d'Ischia et al. — Melanin biopolymers: synthesis, structure, properties, Pigment Cell Res 2009](https://doi.org/10.1111/j.1600-0749.2009.00612.x)
7. [Fedorow et al. — Neuromelanin in human dopaminergic neurons: comparison with peripheral melanins and relevance to Parkinson's disease, Prog Neurobiol 2005](https://pubmed.ncbi.nlm.nih.gov/15680582/)
8. [Zucca et al. — Interactions of iron, dopamine and neuromelanin pathways in brain aging and Parkinson's disease, Prog Neurobiol 2017](https://pubmed.ncbi.nlm.nih.gov/27090489/)
9. [Meredith & Sarna — The physical and chemical properties of eumelanin, Pigment Cell Res 2006](https://doi.org/10.1111/j.1600-0749.2006.00345.x)
10. [Extracellular vesicles from keratinocytes regulate melanosome transfer, PNAS 2024](https://www.pnas.org/doi/10.1073/pnas.2321323121)
