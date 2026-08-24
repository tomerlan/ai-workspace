# Melanin Transducer — Mechanism

---

## Bottom Line

Melanin in melanosomes is not only a light absorber — it is a hydrated, mixed ionic-electronic conductor whose charge, protonation, and radical state change upon illumination. The melanosome is an electrochemical interface: it maintains an acidic interior, runs active proton transport, and contains a polymer whose surface potential shifts with photon dose. That surface potential shift perturbs local ion microdomains in the nanometre-range around the organelle, coupling into the gating behavior of pH- and voltage-sensitive transporters on the melanosome membrane. From there, changes in cytoplasmic proton and ion activity propagate to whole-cell membrane potential (Vmem) and mitochondrial membrane potential (ΔΨm). Membrane potential and cytoplasmic pH are real, causally relevant variables in cancer biology — depolarization and intracellular alkalinization are both permissive for proliferation. A light-driven intervention that shifts these variables in the opposite direction, using the melanin-melanosome system as the transducer, is mechanistically distinct from every existing cancer therapy. It is not cytotoxic. It does not target a specific oncogene. It acts on the physical state variable that gates the proliferative program. The theory is internally coherent and falsifiable; what it lacks is direct experimental demonstration of the middle links.

---

## Step 1 — Melanin Is Not Just a Pigment: It Is a Conductor

The standard picture of melanin as a photon absorber that dumps energy as heat is correct but incomplete. The complete picture starts with what melanin is materially.

**Mixed ionic-electronic conductor.** Hydrated melanin conducts both electrons and protons. Electronic conduction runs through the conjugated aromatic stacks of the indolequinone polymer — the same π-system that gives melanin its broadband absorption. Ionic conduction (primarily proton hopping) runs along the quinone/hydroquinone groups distributed throughout the polymer, which can donate and accept protons in a process analogous to the proton-coupled electron transfer seen in the mitochondrial electron transport chain. Neither conduction pathway is high by inorganic semiconductor standards; neither is negligible compared to the conductivity of biological membranes.

**Humidity dependence.** Dry melanin is nearly insulating. Hydrated melanin — the physiologically relevant state, inside a melanosome bathed in ~pH 5 lumen — is a functional conductor. Conductivity increases by several orders of magnitude as hydration increases from dry to physiological. This is proton conduction through the water-melanin interface, not bulk solution conductivity. The water molecules coordinated to the quinone/hydroquinone surface sites are the conduction medium; the polymer provides the hopping template. [Mostert et al., PNAS 2012]

**Stable free radicals.** The melanin polymer contains a high density of semiquinone radicals — EPR-detectable at g ≈ 2.004. These are not defects; they are inherent to a mixed-oxidation-state quinone polymer. They make melanin a persistent, distributed redox buffer: it can donate or accept electrons from nearby redox-active species without undergoing irreversible chemistry. The radical density is measurable by EPR and varies with melanin source, oxidation state, and pH.

**Photoconductivity.** Illumination increases melanin's electronic conductivity measurably. The mechanism: photon absorption → promotion of an electron to a higher-energy state in the conjugated aromatic system → before internal conversion returns it to the ground state (which happens in <1 ps for the dominant relaxation path), a fraction of the excitations result in charge separation → transiently increased carrier density. The photoconductivity response persists longer than the optical excitation — charge carriers and radical state changes outlast the illumination pulse at physiologically relevant doses. [Bothma et al., PNAS 2008]

**Surface charge and photoacid behavior.** The quinone/hydroquinone groups on the melanin surface have pKa values in the range of 5–10, meaning they are partially protonated at melanosomal pH (~5) and become deprotonated as pH rises. Illumination can shift the effective pKa of surface chromophores — a photoacid effect — causing transient proton release from the polymer surface into the immediate aqueous environment. This is not a large-scale process, but at the interface between the polymer and the melanosome membrane, small proton activities matter.

![Eumelanin polymer structure — indolequinone units with mixed quinone/hydroquinone oxidation states](https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Eumelanin.svg/640px-Eumelanin.svg.png)
*Eumelanin polymer: indolequinone units at different oxidation states (quinone, semiquinone, hydroquinone) provide both the conjugated aromatic system for electronic conduction and the protonatable groups for ionic conduction. Source: Wikimedia Commons.*

---

## Step 2 — The Melanosome Is an Active Electrochemical Organelle

The melanosome is not a passive container for melanin. It is a membrane-bounded organelle that maintains a distinct internal chemical state through active ion transport.

**Acidic lumen.** The melanosome interior is maintained at pH ~4.5–5.5 through a V-type H⁺-ATPase that pumps protons from the cytoplasm (pH ~7.2) into the lumen. This proton gradient (ΔpH ≈ 1.7–2.7 pH units) is large — comparable to the proton gradient across the inner mitochondrial membrane. The gradient is necessary for melanogenesis (TYR has a pH optimum at 6.5–7.0, requiring partial alkalization of the lumen as melanosomes mature through stages III–IV) and is actively maintained by ATP consumption.

**Melanosome membrane transporters:**

| Transporter | Function | Electrophysiological relevance |
|---|---|---|
| V-ATPase | Pumps H⁺ into lumen | Maintains ΔpH; electrogenic; net charge transfer across membrane |
| OCA2 (P protein) | Cl⁻/HCO₃⁻ exchanger, pH regulator | Mutations cause oculocutaneous albinism type 2; OCA2 loss raises melanosomal pH, abolishing melanogenesis |
| SLC45A2 (MATP) | Sugar/H⁺ cotransporter, pH regulator | Also albinism locus; regulates lumenal pH by H⁺ co-import |
| SLC24A5 | Na⁺/K⁺/Ca²⁺ exchanger | Affects melanosomal calcium; mutations cause albinism |
| ATP7A | Cu²⁺ transporter feeding TYR | Copper loading of TYR active site |
| BLOC complexes | Membrane contact sites, lipid dynamics | Structural; governs melanosome–lysosome and melanosome–ER contact |

The key point: the melanosome membrane is not a passive lipid bilayer. It is a protein-dense ion-transport interface that actively sets and maintains the electrochemical environment inside the organelle. The polymer it contains is a conductor. The result is an organelle that functions as a biologically maintained electrochemical cell.

**The transmembrane potential.** The V-ATPase is electrogenic — it transports net positive charge into the lumen, creating a lumen-positive transmembrane potential. Anion channels (ClC-type) partially compensate, but a residual inside-positive potential across the melanosome membrane exists and is maintained by ongoing ATP hydrolysis. This is directly analogous to the inside-positive potential of lysosomes (which melanosomes are related to), except that melanosomes contain a photon-absorbing, proton-coupled conductor on the lumenal face.

---

## Step 3 — What Photon Absorption Changes

When UVA or visible photons are absorbed by melanin in a melanosome, several things change simultaneously:

**1. Electronic state of the polymer (picoseconds)**
The dominant fate of absorbed photons is internal conversion to heat in <1 ps — this is the protective mechanism. But "dominant" does not mean "exclusive." A small fraction of excited state energy results in:
- Transient charge separation in the conjugated aromatic system (photoconductivity response)
- Redistribution of semiquinone radical density along the polymer (EPR-detectable change in radical distribution)
- Population of long-lived triplet states at a small fraction of absorption events

**2. Proton state of the polymer surface (nanoseconds to microseconds)**
Photoacid behavior: illumination shifts the apparent pKa of the surface quinone/hydroquinone groups, transiently releasing protons from the polymer into the immediate lumenal environment. This is a pulse of proton activity at the inner face of the melanosome membrane — the surface that faces the transporter proteins embedded in that membrane.

**3. Local surface charge density (microseconds to milliseconds)**
A change in protonation state is a change in surface charge. Deprotonation of acidic surface groups makes the surface more negative. This changes the electrostatic potential at the melanosome membrane inner face, which changes the transmembrane potential across the membrane by the amount:

ΔVmembrane ≈ ΔΨ(surface charge contribution)

At physiological ionic strength, this effect is short-range (Debye length ~1 nm in 150 mM monovalent salt). But the relevant proteins — the transporter molecules embedded in the melanosome membrane — are within this 1 nm regime of the inner membrane face.

**The key claim:** At the inner surface of the melanosome membrane, the photon-driven change in surface charge and proton activity is not screened to zero. It is sensed by the transporters embedded in that membrane.

---

## Step 4 — From Melanosome Surface to Cytoplasm: The Coupling Chain

**First coupling: polymer surface → membrane transporters.**
The V-ATPase and OCA2 that sit in the melanosome membrane are pH-sensitive proteins. Their activity is modulated by the proton activity at their cytoplasmic and lumenal faces. A transient increase in proton activity at the lumenal face (from the melanin photoacid pulse) changes the rate of proton transport across these proteins. OCA2 — the dominant pH-setter — responds to lumenal proton concentration as its transport substrate. A pulse of proton release from the melanin surface into the lumen acts as an additional substrate signal, transiently driving OCA2 toward net Cl⁻ export (alkalinizing the lumen), which then changes the whole-organelle electrochemical state.

**Second coupling: melanosomal pH → cytoplasmic pH microdomains.**
Melanosomes are not static in the cytoplasm — they are actively trafficked on microtubules and undergo membrane contact events with the ER, late endosomes, and the plasma membrane. More relevantly, each melanosome is a proton sink/source depending on its transport state. Dozens to hundreds of melanosomes in a heavily pigmented melanocyte collectively contribute a substantial H⁺ buffering load to the cytoplasm. A light-driven shift in their collective proton transport rate produces a real change in cytoplasmic H⁺ activity — not a bulk pH change across the whole cell, but a change in the pHi microdomains immediately surrounding the organelles, where many regulatory proteins and channels sit.

**Third coupling: pHi microdomains → plasma membrane channels.**
Cytoplasmic pH is a direct regulator of many plasma membrane channels and exchangers:
- **Inward-rectifier K⁺ channels (Kir family):** Inhibited by intracellular acidification, activated by alkalinization. A shift toward pHi alkalinization increases Kir conductance → hyperpolarization.
- **Na⁺/H⁺ exchangers (NHE1):** These set pHi and in doing so move net charge across the plasma membrane (electrogenic), directly contributing to Vmem.
- **HERG (Kv11.1) and other voltage-gated K⁺ channels:** pH-sensitive gating kinetics.
- **Ca²⁺ channels (L-type, T-type):** Voltage-dependent; a hyperpolarization shift reduces their open probability.

The chain is therefore: light → melanin proton pulse → melanosomal pH micro-event → cytoplasmic pHi microdomain shift → K⁺ channel conductance change → Vmem shift.

**Fourth coupling: Vmem → ΔΨm.**
Mitochondrial membrane potential (ΔΨm) and plasma membrane potential (Vmem) are coupled through cytoplasmic ion composition, particularly [Ca²⁺]cyto and [K⁺]cyto. Mitochondria sense and respond to cytoplasmic [Ca²⁺] via the uniporter and to cytoplasmic [K⁺] via the inner membrane K⁺ transport systems. A sustained shift in Vmem toward hyperpolarization, reducing Ca²⁺ entry, shifts ΔΨm through reduced Ca²⁺-driven mitochondrial activation. These are not dramatic all-or-nothing switches — they are graded shifts in set points, with correspondingly graded downstream effects on ATP production, ROS generation, and apoptotic threshold.

---

## Step 5 — Ling's Framework as a Physical Model

The coupling chain above is described in conventional channel/transporter language — second messengers, binding kinetics, gating parameters. Ling's association-induction hypothesis offers a different physical framing that may be more fundamental for the near-field coupling steps.

**Ling's core claim:** The intracellular space is not a dilute aqueous solution where ions diffuse freely and Na/K-ATPase maintains gradients by continuous pumping. Instead, the cytoplasm is a structured protein-water assembly where K⁺ is preferentially adsorbed to the negatively charged carbonyl groups of protein backbones, and Na⁺ is excluded — not by a pump, but by the electronic state of the protein-water matrix. The K⁺/Na⁺ selectivity of this adsorption is controlled by *cardinal adsorbents* — small molecules that bind at key protein sites and propagate conformational/electronic changes along the backbone, shifting the adsorption preference across large protein domains. ATP is the primary cardinal adsorbent in Ling's model.

**Where melanin fits:** If the Ling model is correct (even partially), then the electronic state of a large, polyelectrolytic, charge-variable surface — such as the melanin polymer — in direct contact with the cytoplasmic protein-water matrix at the melanosome–cytoplasm interface would act as an extended cardinal adsorbent surface. A photon-driven change in melanin surface charge (more negative → enhanced K⁺ adsorption preference) would propagate through the near-field protein-water assembly in the same way a cardinal adsorbent binding event propagates — by changing the inductive electronic environment of the immediately adjacent protein backbone carbonyl groups, which shifts their K⁺/Na⁺ preference, which cascades outward.

This is a physical coupling — not a chemical signal. No second messenger, no receptor binding, no diffusing ligand. It is the near-field electrostatic consequence of a surface charge change in a system where protein-water assemblies transmit electronic state changes cooperatively.

**Why this framing matters:** Conventional signaling requires a molecular intermediary at every step. The Ling framing allows the photon-to-Vmem coupling chain to be *shorter* than the conventional model implies, because steps 2 and 3 (melanosomal pH → cytoplasmic pHi microdomain → channel gating) collapse into a single physical interaction between the melanin surface and the protein-water matrix of the near-field cytoplasm.

---

## Step 6 — Bioelectric State Is a Real Variable in Cancer

This theory has a plausible mechanism. Does it connect to cancer biology that actually matters?

**Vmem in cancer — the evidence:**
- Normal differentiated cells are electrically hyperpolarized (Vmem ≈ −50 to −90 mV in most mammalian cell types)
- Proliferating cells — embryonic, stem-like, and cancer cells — are depolarized (Vmem ≈ −10 to −30 mV)
- This is not a correlation artifact. Depolarizing voltage-gated Na⁺ channels are expressed in many cancers and their expression correlates with invasiveness. Blocking these channels in cancer cells reduces invasion
- Michael Levin's group has shown: artificially depolarizing normal frog melanocytes to cancer-compatible Vmem induces melanoma-like growth without any genetic mutation, and artificially restoring Vmem arrests it. The effect is mediated through serotonin signaling downstream of the electrical change, demonstrating that Vmem is causally upstream of transcriptional and proliferative programs, not merely correlated

**Cytoplasmic pH in cancer:**
- Cancer cells maintain a slightly alkaline pHi (~7.4–7.6) compared to normal cells (~7.0–7.2). This small shift is mechanistically important:
  - The G1→S transition requires pHi rise to ~7.3; blocking this arrests the cell cycle
  - Cytoskeletal dynamics (actin assembly, which drives invasion) are pH-sensitive in this range
  - Many glycolytic enzymes are activated at slightly alkaline pHi
- Cancer cells achieve this alkaline pHi partly through upregulation of NHE1 (Na⁺/H⁺ exchanger, which exports H⁺ at the cost of Na⁺ import), which is also electrogenic and contributes to the depolarized Vmem

**The mechanistic connection:** Depolarized Vmem + alkaline pHi form a self-consistent cancer-permissive state. They are coupled — NHE1 activity simultaneously alkalinizes pHi and depolarizes Vmem. A light-driven intervention that shifts the system toward hyperpolarization (acting on K⁺ channels via pHi microdomains) simultaneously pushes against the alkaline pHi by reducing the electrochemical driving force for NHE1 export. The two effects reinforce each other in the correct direction.

**ΔΨm in cancer:**
Many cancer cells paradoxically hyperpolarize their mitochondrial membrane potential. High ΔΨm in cancer is associated with:
- Increased ROS generation from the electron transport chain
- Anti-apoptotic signaling (cytochrome c release threshold is set by ΔΨm)
- Resistance to conventional chemotherapy

A light-driven reduction in cytoplasmic [Ca²⁺] entry (via plasma membrane hyperpolarization → reduced voltage-gated Ca²⁺ channel activity) reduces mitochondrial Ca²⁺ uptake via the uniporter, which reduces ΔΨm, which sensitizes cancer cells to apoptotic stimuli and reduces mitochondrial ROS. Again, the directions are consistent.

---

## Step 7 — Action Spectrum and Dose

**The action spectrum must track melanin absorption.**
Melanin absorbs broadly from UVC through visible, decreasing monotonically toward longer wavelengths:
- UVB (280–315 nm): strong absorption; not suitable — direct DNA damage
- UVA (315–400 nm): strong melanin absorption; minimal direct DNA damage; this is the primary range
- Violet/blue (400–450 nm): still substantial absorption; no DNA damage
- Green/yellow (500–570 nm): moderate absorption; useful for deeper penetration
- Red (620–700 nm): weak but non-zero; best tissue penetration; relevant for internal delivery

**For skin surface applications:**
UVA is the natural choice. It penetrates the epidermis, is strongly absorbed by melanosomes, and the irradiance levels required for the photoconductivity/photoacid effect are well below the erythemal threshold. The erythemal threshold for UVA is approximately 30–50 J/cm² (much higher than for UVB). Sub-erythemal UVA exposures (1–10 J/cm²) are entirely achievable without sunburn chemistry.

**For internal tumors via light delivery:**
Red and near-infrared wavelengths (630–850 nm) are the tissue penetration window. Melanin absorption at 630 nm is roughly 1000-fold lower than at 360 nm. This means:
- For melanin-dense cells (melanocytes, heavily pigmented RPE): red light can still drive a measurable response at achievable irradiance levels
- For sparsely melanin-containing cells (melanin-loaded macrophages, cells post nanoparticle uptake): red light may be insufficient without supplemental melanin loading
- The depth delivery calculation requires: tissue optical properties, irradiance at the fiber tip, and the minimum melanin-surface photon flux required for a detectable proton pulse

**Dose framing:**
The goal is not maximum melanin excitation. It is a sub-threshold, repeated perturbation that chronically shifts the set point of the melanosome electrochemical state. Analogous to how low-dose circadian light cues set oscillator phase without saturating the photoreceptor. The relevant parameter is not peak intensity but time-averaged photon flux at the melanin surface over hours to days.

---

## Step 8 — The Free Melanin Question

The entire mechanism described above requires melanin to **stay inside the melanosome**. The transducer is the melanosome-as-organelle: the polymer inside, the membrane around it, the transporters in that membrane, and the coupling to cytoplasm through the outer membrane surface. A melanin polymer released from the melanosome into the cytoplasm:
- Is no longer maintained at the correct pH for proton-coupled conduction
- Has no transporter proteins to couple its surface charge changes into ion gradients
- Is a reactive quinone polymer in a reductive, protein-rich environment — it crosslinks, chelates metals, and generates radicals

So the theory is consistent with and requires compartmentalized melanin. The free-melanin problem and the transducer theory point in the same direction: the organelle is the unit. The melanosome is not a storage depot; it is the functional device.

---

## Confidence Map — What Is Established vs. Speculative

| Claim | Status | Evidence |
|---|---|---|
| Melanin is a mixed ionic-electronic conductor | **Established** | Mostert et al. PNAS 2012; multiple solid-state measurements |
| Melanin is photoconductive | **Established** | Bothma et al. PNAS 2008; thin-film measurements |
| Melanin has stable semiquinone radicals measurable by EPR | **Established** | Extensive EPR literature; g ≈ 2.004 |
| Illumination changes melanin radical distribution | **Established** | EPR on illuminated melanin in vitro |
| The melanosome maintains an acidic lumen (~pH 5) | **Established** | Direct measurement; albinism genetics (OCA2/SLC45A2) |
| V-ATPase, OCA2, SLC24A5 are melanosome membrane transporters | **Established** | Genetics, biochemistry |
| Vmem is depolarized in cancer vs normal cells | **Established** | Multiple cell types; patch clamp |
| Artificial Vmem depolarization induces cancer-like behavior | **Established** | Levin lab, Xenopus melanocyte model |
| pHi is alkaline in cancer cells | **Established** | Multiple cancer types; mechanistically linked to NHE1 |
| Illumination drives a proton pulse from melanin surface (photoacid) | **Plausible** | Inferred from pKa shift of quinones under excitation; not directly measured in melanosomes |
| Melanin surface charge change couples to melanosome transporters | **Plausible** | Structural plausibility; no direct measurement |
| Melanosomal transport rate change shifts cytoplasmic pHi | **Plausible** | Requires quantitative modeling; not measured |
| pHi shift propagates to Vmem via K⁺ channels/NHE | **Plausible** | Known coupling pathways; not shown in UVA context |
| Sub-erythemal UVA drives measurable Vmem shift in melanocytes | **Not demonstrated** | The core experimental gap |
| This Vmem shift is anti-proliferative | **Not demonstrated** | Would require cell biology experiments |
| Ling's framework is the right physical model | **Contested** | Ling's interpretation of ion distribution data is minority view; near-field coupling concept is not experimentally resolved |

---

## Range of Applicability

The mechanism depends on three things being present simultaneously: (1) melanin in sufficient quantity to generate a detectable surface charge/proton pulse under illumination, (2) a surrounding membrane with ion transporters that can convert that pulse into a net ion flux, and (3) enough of this happening in enough organelles per cell to shift whole-cell pHi and Vmem above the noise floor of the cell's other regulatory signals.

**Tier 1 — Strong coupling, theory applies cleanly:**

*Melanocytes (stage III–IV melanosome load).* This is the system the theory was built for. Densely loaded mature melanosomes, V-ATPase running continuously, OCA2 and SLC45A2 embedded in the membrane as dedicated pH regulators, large total melanin surface area per cell (100–1000 organelles × ~500 nm diameter each). All three requirements are met.

*RPE cells.* Similar argument: heavily and stably melanin-loaded (some of the highest melanin density in the body), long-lived, metabolically active. The melanosomes are mature and metal-loaded. Potentially even more relevant to the theory than melanocytes because RPE cells are directly and chronically exposed to visible light from retinal illumination — the action spectrum overlap is there by design.

**Tier 2 — Partial coupling, uncertain threshold:**

*Keratinocytes with supranuclear melanosome caps.* Melanosomes transferred from melanocytes retain their membrane and some of their transporter proteins for a period after transfer — they do not immediately convert to generic endosomes. As the melanosome ages inside the keratinocyte and its membrane proteins turn over, the coupling degrades. This is probably the most important uncertain case for the solar callus context, because keratinocytes are the numerically dominant cell type in the epidermis.

*Melanoma cells.* Vary enormously in melanin content — from densely pigmented to completely amelanotic. Pigmented melanoma cells have abundant mature melanosomes and likely sit in Tier 1. Poorly differentiated, amelanotic melanoma cells have minimal melanin and would not be addressable by this mechanism at all.

**Tier 3 — Weak or absent coupling:**

*Macrophages and other cells with phagocytosed melanin.* When a macrophage ingests extracellular melanin, the material ends up in phagolysosomes — degradation compartments without the specialized melanosome transporter proteins. The photon→surface charge change still occurs on the polymer, but the coupling to a directed ion flux is poor.

*Cells loaded with exogenous melanin nanoparticles.* Similar to macrophages — nanoparticles end up in endosomes/lysosomes. The mechanism is weakened but not necessarily absent; this is what experiment 5 in the experimental program is designed to test.

*Neuromelanin-containing SN/LC neurons.* Neuromelanin is stored in autophagic double-membrane granules — structurally distinct from melanosomes, no dedicated ion transport machinery. These neurons are also not meaningfully light-exposed under normal conditions. The transducer theory is largely inapplicable here in a therapeutic sense.

**The threshold question:**
How much melanin per cell is enough? A rough estimate: if a single melanosome generates a proton pulse of ~10⁻¹⁸ mol H⁺ per illumination event, and a melanocyte has ~500 melanosomes, the collective pulse is ~5×10⁻¹⁶ mol H⁺ — small but potentially within the range that affects cytoplasmic pHi given the cell's buffering capacity. A keratinocyte with 50 transferred melanosomes generates one-tenth that. Where the signal crosses the threshold of biological relevance is the key unknown, and it is experiment 2 in the program (pHi response in melanocytes vs TYR-null controls) that begins to define it.

---

## Ambient Light as a Continuous Input — and an Experimental Confound

The transducer mechanism, if real, does not only engage during deliberate UV exposure. Melanin-containing cells in tissue receive continuous photon flux from ambient visible and UVA light — the mechanism would operate as a tonic, ongoing modulation whose magnitude tracks the ambient photon environment, not as a switch that activates during UV sessions.

**Biological implication:**
Melanocyte Vmem/pHi set points would track chronic light environment, not just acute exposures. Chronic indoor living (near-zero UV, low visible intensity, artificial spectral composition) would correspond to a different melanocyte electrical baseline than chronic outdoor living — through the melanin electrophysiology route, independently of vitamin D and NO pathways.

**In-vitro experimental confound:**
Standard tissue culture is conducted under fluorescent or LED laboratory lighting, typically at 200–500 lux continuous illumination during working hours. If the transducer mechanism operates, melanin-loaded cells in culture are being held at a light-conditioned Vmem/pHi baseline, not a "dark resting" state. Controls run in the "dark" may actually be run under ambient lab light, making the control condition poorly defined.

Practically, this means the experimental program requires:
- **Dark-adapted baseline**: cells maintained in light-tight incubator conditions for a defined period before measurement
- **Light dose logging**: continuous photon flux at cell level measured and reported for all conditions
- **Amelanotic controls run under identical light conditions**: the only variable should be the presence or absence of melanin
- **Spectral control**: lab fluorescent lighting has a very different spectrum from sunlight, particularly depleted in UVA. The effective dose at melanin's absorption peak under lab conditions vs. sunlight differs by orders of magnitude.

---

## References

1. Mostert, A.B. et al. — Role of semiconductivity and ion transport in the electrical conduction of melanin. *PNAS* 2012. [DOI](https://doi.org/10.1073/pnas.1119948109)
2. Bothma, J.P. et al. — Evidence for Conformational Heterogeneity in Melanin. *PNAS* 2008.
3. Meredith, P. & Sarna, T. — The physical and chemical properties of eumelanin. *Pigment Cell Res* 2006. [DOI](https://doi.org/10.1111/j.1600-0749.2006.00345.x)
4. [Raposo & Marks — Melanosomes, *Nat Rev Mol Cell Biol* 2007](https://pmc.ncbi.nlm.nih.gov/articles/PMC2786984/)
5. Levin, M. & Martyniuk, C.J. — The bioelectric code. *Biosystems* 2018. [DOI](https://doi.org/10.1016/j.biosystems.2017.08.009)
6. Chernet, B. & Levin, M. — Endogenous Voltage Potentials and the Microenvironment of the Frog Embryo. *Disease Models & Mechanisms* 2013.
7. Stock, C. & Schwab, A. — Protons make tumor cells move like clockwork. *Pflügers Archiv* 2009.
8. Webb, B.A. et al. — Dysregulated pH: a perfect storm for cancer progression. *Nat Rev Cancer* 2011.
9. Ling, G.N. — A Physical Theory of the Living State: The Association–Induction Hypothesis. Blaisdell, 1962.
10. Ando, H. et al. — Melanosome transfer mechanisms. *Pigment Cell & Melanoma Research* 2012. [DOI](https://doi.org/10.1111/j.1755-148X.2012.01082.x)
11. Bellono, N.W. et al. — OCA2 and melanosomal pH regulation. *eLife* 2014. [DOI](https://elifesciences.org/articles/04543)
