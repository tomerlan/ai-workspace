# MRI Physics for Parkinson's Disease Imaging

MRI does not directly image tissue damage. It images **physical properties of water protons** in tissue — how quickly they relax after excitation, how constrained their motion is, how their local magnetic environment is perturbed by surrounding molecules. Different tissue pathologies alter these properties in different ways, and each MRI contrast mechanism is tuned to one or more of them. This document unpacks the physics behind each method used to track PD progression, starting from first principles where they matter.

---

## What MRI Actually Measures

A proton (¹H nucleus) has a magnetic moment — it behaves like a tiny bar magnet. In a strong external field B₀ (3 Tesla, roughly 60,000 times Earth's magnetic field), proton magnetic moments preferentially align with the field, producing a net bulk magnetization **M** pointing along B₀. A radiofrequency (RF) pulse tuned to the proton Larmor frequency ω₀ = γB₀ (where γ is the gyromagnetic ratio, 42.58 MHz/T for protons) tips this magnetization away from B₀. After the pulse ends, **M** returns to equilibrium — this return process is called **relaxation**, and its time constants encode tissue composition.

Two independent relaxation processes occur simultaneously:

**Longitudinal (T1) relaxation:** The component of **M** along B₀ recovers exponentially with time constant T1 — the spin-lattice relaxation time. T1 measures how efficiently protons transfer energy to the surrounding molecular environment (the "lattice").

**Transverse (T2 and T2*) relaxation:** The component of **M** perpendicular to B₀ decays exponentially with time constant T2 — the spin-spin relaxation time — because neighboring protons exchange energy with each other, destroying their phase coherence. T2* is shorter than T2 because it also includes dephasing from static field inhomogeneities that are not reversed by the MRI sequence. T2* = 1/(1/T2 + γΔB₀) where ΔB₀ is the local field variation.

The image intensity in any MRI sequence depends on how the pulse sequence parameters (TR — repetition time, TE — echo time, flip angle) weight these tissue properties against each other.

---

## T1 Relaxation: Why Neuromelanin-Iron Appears Bright

### The Physical Origin of T1

T1 relaxation occurs when fluctuating local magnetic fields at the proton's location match the Larmor frequency and trigger energy exchange with the lattice. The fluctuations arise from molecular tumbling, rotation, and diffusion. The key parameter is the **correlation time τ_c** — the characteristic time for molecular motion. Maximum T1 relaxation enhancement occurs at the resonance condition ω₀τ_c ≈ 1. Free water molecules tumble very rapidly (τ_c ~10⁻¹² s), placing them far from the resonance condition at clinical field strengths, so pure water has a very long T1 (~3–4 seconds). Binding water to macromolecules slows the effective tumbling and moves τ_c closer to the resonance condition, shortening T1. This is why proteins, lipids, and myelin all have shorter T1 than free water.

### Paramagnetic Relaxation Enhancement

Paramagnetic substances carry unpaired electrons. Electrons have a magnetic moment approximately 658 times larger than a proton. When a water molecule diffuses near a paramagnetic center, the proton experiences a large, fluctuating magnetic field driven by the electron spin. This dramatically enhances both T1 and T2 relaxation through dipole-dipole interaction.

The relaxation rate enhancement is described by the Solomon-Bloembergen-Morgan (SBM) equations. For a paramagnetic ion with spin S and electron correlation time τ_c, the inner-sphere T1 enhancement is:

\[ \frac{1}{T_{1,IS}} = \frac{2}{15} \cdot \frac{\mu_0}{4\pi}^2 \cdot \frac{\gamma_I^2 g^2 \mu_B^2 S(S+1)}{r^6} \left( \frac{7\tau_c}{1+\omega_S^2\tau_c^2} + \frac{3\tau_c}{1+\omega_I^2\tau_c^2} \right) \]

The key proportionality: relaxation enhancement scales as **1/r⁶** where r is the proton-to-metal distance (extremely short range — only protons directly coordinated to or within ~5 Å of the metal are significantly affected), and scales with **S(S+1)** — the electron spin quantum number factor. Iron in the Fe³⁺ state (S = 5/2) has 5 unpaired electrons and thus provides very strong paramagnetic enhancement. In contrast, Fe²⁺ (S = 2, 4 unpaired electrons) provides less enhancement and its electronic relaxation behavior is more complex.

### Neuromelanin as a Paramagnetic T1 Agent

Neuromelanin is a polymer that chelates iron in its Fe³⁺ form at specific high-affinity binding sites. The bound Fe³⁺ is held in proximity to the water protons that hydrate the neuromelanin macromolecule. These protons exchange with bulk free water in the tissue, transferring the T1-shortening effect to the surrounding water pool. The result: tissue containing neuromelanin-iron complexes has a shorter T1 — it recovers faster after an RF pulse and appears **brighter** in T1-weighted sequences (those with TR chosen to maximize the signal difference between short-T1 and long-T1 tissues).

**Why healthy SNpc is bright, and why PD SNpc is darker:** In a healthy young adult, the SNpc contains ~450,000 neuromelanin-laden dopaminergic neurons per hemisphere, each densely packed with neuromelanin-iron complexes accumulated over decades. This creates a tissue region with measurably shorter T1 than the surrounding structures. As PD depletes these neurons, the local neuromelanin-iron concentration falls, T1 lengthens toward that of surrounding tissue, and the SNpc signal on T1-weighted or MT-prepared sequences diminishes.

---

## Magnetization Transfer: The Engine of NM-MRI Contrast

### Two Pools of Protons

Tissue contains two distinct proton populations that behave very differently in MRI:

**The free water pool** has narrow spectral linewidth (~100 Hz at 3T) because water molecules tumble rapidly, averaging out local field variations. This is the pool that produces the MRI signal we detect. Its T2 is long (40–100 ms in gray matter).

**The bound (macromolecular) pool** consists of protons attached to proteins, lipids, and myelin. These protons tumble slowly or are immobile, so local fields average poorly — their spectral linewidth is extremely broad (~10–50 kHz). Their T2 is very short (~10–100 µs), making them essentially invisible in standard MRI acquisition (the signal decays before we can detect it).

### The Magnetization Transfer Mechanism

Even though we cannot directly image the bound pool, it communicates with the free water pool through two pathways: **dipolar cross-relaxation** (direct energy exchange between adjacent protons via magnetic dipole-dipole coupling) and **chemical exchange** (actual transfer of protons between bound sites and free water). Both transfer saturation between the pools.

An off-resonance RF pulse — applied far off the water resonance (e.g., 1,000–3,000 Hz away) — saturates the broad spectral linewidth of the bound pool without directly affecting free water. The saturation then transfers to the free water pool, reducing its signal in proportion to the bound pool's size and the exchange rate:

\[ MTR = \frac{M_0 - M_{sat}}{M_0} \times 100\% \]

High MTR → large bound pool → lots of macromolecular content. Heavily myelinated white matter (like the crus cerebri adjacent to the SNpc) has MTR ~40–55% at 3T, among the highest values in the brain. Gray matter typically shows MTR ~25–35%. The SNpc, containing neuromelanin-laden neurons but far fewer myelinated fibers than surrounding white matter, has MTR lower than the crus cerebri.

### Why This Creates SNpc Contrast

The critical structural fact is that the SNpc is anatomically embedded within and flanked by the **crus cerebri** — a large bundle of heavily myelinated corticospinal and corticopontine fibers. The MT preparation pulse strongly suppresses the crus cerebri signal. The SNpc, being less myelinated, is less suppressed and appears **relatively bright by comparison** — even if its absolute signal intensity in a non-MT sequence would not stand out from surrounding gray matter.

The contrast in NM-MRI is therefore a **differential suppression contrast**: the SNpc appears bright not because its signal is intrinsically high, but because everything around it is suppressed more aggressively. This makes the contrast exquisitely dependent on the anatomy: NM-MRI works for the SNpc specifically because of where it sits. The same sequence applied elsewhere in cortical gray matter would not produce the same differential.

The T1 shortening from neuromelanin-iron (Section 1) provides an **additive enhancement** on top of the MT differential: it actively brightens the SNpc signal in T1-weighted readouts. The two mechanisms — MT suppression of surroundings plus T1 enhancement of the SNpc — compound into the observed contrast. At 7T, where T1 lengthens for all tissues (reducing the MT differential somewhat), the neuromelanin-specific T1 shortening becomes proportionally more important.

### Sequence Design Consequences

The off-resonance saturation pulse is placed at ~1,500 Hz from water resonance, at a flip angle of ~500–700°, which is large enough to partially saturate the broad bound pool but not so large as to cause off-resonance direct saturation of the narrow free water resonance. A gradient-recalled echo (GRE) readout with short TE (~14 ms at 3T) minimizes T2* signal loss in the iron-containing SNpc region (which would darken it). TR is set to ~600 ms — short enough to provide T1 weighting (favoring the short-T1 neuromelanin tissue) while allowing partial recovery in surrounding tissue.

The entire contrast depends on **field strength**: at 3T, the Larmor frequency is 128 MHz. At 7T, it is 298 MHz. Because the MT effect is partially mediated by direct dipolar coupling (distance-dependent, field-independent), but the T1-shortening effect scales with field through ω₀ in the SBM denominator, the relative contributions of the two mechanisms shift with field. 7T gains dramatically in spatial resolution (voxel volume can be reduced ~8×) and in signal-to-noise, at the cost of more complex RF pulse design and more severe B1 inhomogeneity in the midbrain region.

---

## T2* Relaxation and Iron Imaging

### From T2 to T2*

T2 decay (spin-spin relaxation) arises from random, time-varying local magnetic field fluctuations that cause neighboring protons to dephase irreversibly. These fluctuations average to zero over time but still accelerate signal decay. T2 is an intrinsic tissue property — it cannot be reversed by the scanner.

T2* additionally includes **static field inhomogeneities** — spatial variations in B₀ that are fixed in time but vary across space. Protons at slightly different positions precess at slightly different frequencies, causing coherent dephasing. This is reversible with a spin echo (a 180° refocusing pulse). In a gradient echo (no refocusing pulse), both T2 and the static dephasing contribute, giving T2*:

\[ \frac{1}{T2^*} = \frac{1}{T2} + \frac{1}{T2'} \]

where 1/T2' = γΔB₀ captures the field-inhomogeneity contribution. Tissues with larger microscopic field inhomogeneities have shorter T2* — they dephase faster and lose signal more rapidly in GRE sequences.

### How Iron Creates Field Inhomogeneity

Iron in biological tissue exists primarily in **ferritin** — a protein shell (~12 nm diameter) containing up to 4,500 iron atoms in a ferrihydrite mineral core. Ferritin cores are **superparamagnetic** at room temperature: they have a large collective magnetic moment that aligns with B₀, but they do not maintain permanent magnetization outside the field. This large net moment creates a dipolar magnetic field perturbation around each ferritin particle:

\[ \Delta B(r,\theta) = \frac{\mu_0}{4\pi} \cdot \frac{m(3\cos^2\theta - 1)}{r^3} \]

where m is the ferritin magnetic moment, r is the distance from the particle center, and θ is the angle with respect to B₀. The dipole field falls off as 1/r³, meaning it affects water molecules several nanometers away — a much longer-range effect than the paramagnetic T1 shortening, which requires direct coordination at ~5 Å. Because ferritin particles are distributed heterogeneously in tissue, water protons diffusing through these dipole fields acquire random phase variations → faster T2* decay.

**R2\* = 1/T2\*** is approximately linearly proportional to iron concentration in tissue under the assumption that proton diffusion through the ferritin dipole field is slow compared to the echo time (static dephasing regime). Empirically:

\[ R2^* \approx R2^*_0 + r_2^* \cdot [Fe] \]

where R2\*₀ is the baseline (iron-free) rate, r₂\* is the relaxivity (~0.09–0.13 s⁻¹ per µg/g tissue/mL at 3T in brain tissue), and [Fe] is the iron concentration. This linear relationship allows R2\* maps to serve as quantitative iron concentration maps within the assumptions.

**Hemosiderin** (aggregated, partly denatured ferritin) is less well-organized but still paramagnetic and creates even larger local field perturbations than ferritin. It is more prominent in cells with very high iron turnover.

### R2\* Acquisition

R2\* is measured from **multi-echo GRE**: a single RF excitation followed by several successive gradient echoes at increasing TE values (e.g., TE₁ = 5 ms, TE₂ = 10 ms, TE₃ = 15 ms... up to ~40–50 ms at 3T). The signal at each echo:

\[ S(TE) = S_0 \cdot e^{-TE/T2^*} \]

Fitting this monoexponential (or multiexponential, for voxels with multiple tissue compartments) decay gives T2\* per voxel, and R2\* = 1/T2\*. The SNpc in PD shows elevated R2\* (shorter T2\*) compared to age-matched controls and compared to the patient's own contralateral side in early asymmetric disease. The SNpc iron increase is approximately 30–40% above control values in established PD.

---

## Magnetic Susceptibility and QSM

### What Susceptibility Is

All materials respond to an applied magnetic field. The **magnetic susceptibility** χ (dimensionless) describes the degree of magnetization per unit field:

\[ \mathbf{M} = \chi \mathbf{H} \]

For biological relevance, two categories matter:

**Paramagnetic materials** (χ > 0) become magnetized in the direction of B₀ — they add to the local field. This includes iron in its high-spin states (Fe³⁺ in ferritin: χ ~0.52 × 10⁻⁶ SI per ppm; hemosiderin is larger), deoxyhemoglobin, and molecular oxygen.

**Diamagnetic materials** (χ < 0) are weakly magnetized opposite to B₀ — they slightly reduce the local field. Most biological molecules are diamagnetic, including water (χ ≈ −9 × 10⁻⁶ SI), most proteins, and importantly **myelin** (whose cholesterol and phospholipid molecules have negative susceptibility).

In a voxel containing both paramagnetic iron and diamagnetic myelin, the measured susceptibility reflects the balance of both contributions — which is why susceptibility maps in white matter reflect the interplay between iron (bright) and myelin (dark).

### Phase Accumulation and the Forward Problem

In a gradient echo sequence, a proton at position **r** accumulates phase proportional to the local frequency offset Δω(**r**) over the echo time:

\[ \phi(\mathbf{r}, TE) = \Delta\omega(\mathbf{r}) \cdot TE = \gamma \cdot \Delta B(\mathbf{r}) \cdot TE \]

The local field perturbation ΔB(**r**) is related to the susceptibility distribution χ(**r**) through the **dipole kernel** d(**r**):

\[ \Delta B(\mathbf{r}) = \frac{1}{3}\chi(\mathbf{r}) \cdot B_0 + B_0 \int \chi(\mathbf{r}') \cdot d(\mathbf{r}-\mathbf{r}') d\mathbf{r}' \]

In k-space (Fourier domain), the forward problem simplifies to a multiplication:

\[ \tilde{\Delta B}(\mathbf{k}) = B_0 \cdot D(\mathbf{k}) \cdot \tilde{\chi}(\mathbf{k}) \]

where D(**k**) = (1/3) − k_z²/|**k**|² is the dipole kernel in k-space. This is the elegant version of the relationship: measured phase is a filtered (blurred, directionally smeared) version of the underlying susceptibility source.

### The Inverse Problem: Reconstructing QSM

Given the measured phase, we want to recover χ(**r**). In principle, divide by D(**k**) in k-space. The problem: D(**k**) is zero on a conical surface at the "magic angle" (54.7° from B₀) — the so-called **cone of silence**. Division by zero is ill-posed; small noise in the phase at these k-space locations becomes infinitely amplified.

This is the central challenge of QSM reconstruction. Three algorithmic steps are required:

**Step 1 — Phase unwrapping.** The measured phase is wrapped to the range [−π, π). Unwrapping recovers the true continuous phase. In brain tissue with large susceptibility gradients (e.g., SN/ventricle boundaries), phase wraps can be dense and require robust spatial unwrapping algorithms (ROMEO, SEGUE).

**Step 2 — Background field removal.** The brain is surrounded by air (strongly paramagnetic) and bone, which create large background field variations that swamp the tissue contributions. These background fields are smooth and slowly varying compared to tissue susceptibility variations. Removal methods include SHARP (spherical mean value filtering), PDF (projection onto dipole fields), or LBV (Laplacian-based approaches). This step is critical — residual background field creates streaking artifacts in the final susceptibility map.

**Step 3 — Dipole inversion.** Given the tissue phase (after background removal), invert the dipole kernel to recover susceptibility. Regularized inversion methods add prior information to stabilize the solution: MEDI (Morphology Enabled Dipole Inversion) uses the magnitude image structure as a spatial prior; TKD (threshold k-space division) simply avoids dividing near the zero cone; iterative approaches minimize a cost function balancing data fidelity against smoothness or edge-preserving priors.

The result: a quantitative susceptibility map where each voxel value represents magnetic susceptibility in parts per billion (ppb), with iron appearing bright (positive) and myelin appearing dark (negative). The SNpc in PD shows elevated positive susceptibility relative to controls — roughly proportional to the pathological iron accumulation.

### APART-QSM: Separating Iron from Myelin

A limitation of standard QSM is that it measures the **net** susceptibility, which is iron (positive) minus myelin (negative) in white matter. This is problematic for the SN, where neurodegeneration simultaneously increases iron and reduces myelinated fibers — the two effects partially cancel, underestimating both. Advanced QSM variants that combine R2\* and QSM data (e.g., χ-separation, APART-QSM) can disambiguate paramagnetic and diamagnetic contributions within each voxel:

\[ \chi_{total}(\mathbf{r}) = \chi_{para}(\mathbf{r}) + \chi_{dia}(\mathbf{r}) \]

by exploiting the fact that iron contributes to both R2\* (short-range dipolar relaxation) and positive susceptibility, while myelin contributes only to diamagnetic susceptibility and independently to T2. This decomposition provides separate iron and myelin density maps — more specific than either R2\* or QSM alone.

### The Nigrosome-1 Sign: Susceptibility Anatomy

Within the SNpc, a sub-region called **nigrosome-1** in the dorsolateral SNpc is particularly rich in neuromelanin-containing neurons and relatively poor in iron — because these neurons represent the most metabolically active, highest-neuromelanin-producing population. In healthy tissue, this creates a focal region of reduced susceptibility (less iron, more neuromelanin with diamagnetic properties) within the otherwise iron-accumulating SNpc. On SWI and T2\* maps, nigrosome-1 appears as a small bright oval (low iron → less T2\* decay → brighter signal) within the dark SN. Because the SN flanks the red nucleus and lateral to it is the medial lemniscus, the two bright nigrosome-1 patches appear on axial slices like the two swallow tails of a butterfly — giving rise to the "swallow-tail sign."

In PD, the nigrosome-1 neurons are preferentially and early affected. As these cells die, neuromelanin is lost and iron accumulates in their place. The focal T2\*-bright region disappears — the swallow-tail sign is lost. This qualitative sign achieves AUC ~0.88–0.90 for PD diagnosis at 3T with experienced readers, and approaches 1.0 at 7T with quantitative analysis. It is among the most visually striking disease-specific findings on brain MRI.

---

## Diffusion Tensor Imaging

### Brownian Motion and the Diffusion-Weighted Signal

Water molecules undergo thermal Brownian motion — random displacements with a Gaussian distribution whose width (mean squared displacement) grows linearly with time and diffusion coefficient D:

\[ \langle x^2 \rangle = 2Dt \]

In free water at 37°C, D ≈ 3.0 × 10⁻³ mm²/s. In tissue, diffusion is hindered and restricted by cell membranes, myelin sheaths, and macromolecular obstacles, reducing the apparent diffusion coefficient (ADC) to ~0.6–0.8 × 10⁻³ mm²/s in gray matter.

To encode diffusion in MRI, a pair of magnetic field gradients is applied around a 180° refocusing pulse (Stejskal-Tanner sequence). Protons that do not move between the two gradients accumulate equal and opposite phase shifts — they cancel perfectly. Protons that diffuse along the gradient direction acquire a residual phase proportional to their net displacement. Because displacements are random and have a distribution, the net effect is signal **attenuation** rather than phase shift:

\[ S = S_0 \cdot e^{-b \cdot ADC} \]

where the **b-value** encodes the sensitivity to diffusion:

\[ b = \gamma^2 G^2 \delta^2 \left(\Delta - \frac{\delta}{3}\right) \]

(G = gradient amplitude, δ = gradient duration, Δ = time between gradients). Higher b-values → more sensitive to diffusion → more signal attenuation in freely diffusing tissue.

### The Diffusion Tensor

Biological tissue is anisotropic: a water molecule in a myelinated axon diffuses easily along the axon axis but is restricted perpendicular to it (membrane barriers, tight myelin wrapping). A single scalar ADC cannot capture this. The **diffusion tensor** D is a 3×3 symmetric positive definite matrix that fully characterizes diffusion in 3D:

\[ S(\hat{g}) = S_0 \cdot e^{-b \cdot \hat{g}^T \mathbf{D} \hat{g}} \]

where **ĝ** is the unit vector of the applied diffusion gradient direction. By acquiring diffusion-weighted images in at least 6 non-collinear gradient directions (plus one b=0 image), D can be estimated at each voxel. The tensor has three eigenvectors and eigenvalues (λ₁ ≥ λ₂ ≥ λ₃). The principal eigenvector points along the primary diffusion direction (the local fiber orientation in white matter). The eigenvalues represent diffusion magnitudes along the three principal axes.

From these, composite metrics are derived:

**MD (mean diffusivity)** = (λ₁ + λ₂ + λ₃)/3 — the overall magnitude of diffusion. Increases when tissue structure is lost (axons die, membranes break down, interstitial space expands). In the SN in PD: MD increases progressively.

**FA (fractional anisotropy):**
\[ FA = \sqrt{\frac{3}{2}} \cdot \frac{\sqrt{(\lambda_1-\bar\lambda)^2 + (\lambda_2-\bar\lambda)^2 + (\lambda_3-\bar\lambda)^2}}{\sqrt{\lambda_1^2+\lambda_2^2+\lambda_3^2}} \]
FA ranges from 0 (perfectly isotropic — equal diffusion in all directions, e.g., CSF or gray matter) to 1 (perfectly anisotropic — all diffusion along one axis, e.g., a coherent white matter tract). In highly organized white matter tracts (corpus callosum), FA > 0.7. In gray matter, FA < 0.2. In the SN, which contains both myelinated fibers (nigrostriatal tract) and gray matter neurons, FA is intermediate (~0.2–0.35 in healthy tissue) and falls in PD as nigrostriatal fibers degenerate.

**RD (radial diffusivity)** = (λ₂ + λ₃)/2 — diffusion perpendicular to the primary fiber direction. Increases with demyelination (myelin restricts radial diffusion; its loss removes the barrier).

**AD (axial diffusivity)** = λ₁ — diffusion along the primary fiber. Decreases with axonal loss.

### DTI in PD

The nigrostriatal tract runs from SNpc neurons through the medial forebrain bundle and internal capsule to dopaminergic terminals in the striatum. This tract cannot be reliably visualized with standard structural MRI but is detectable by DTI-based tractography. In PD: reduced FA and elevated MD in the SN are among the most replicated DTI findings, present even in early disease. The FA reduction reflects the combination of axon loss (dopaminergic fibers projecting to striatum), gliosis (glial proliferation filling the spaces left by dead neurons, increasing isotropic diffusion), and possibly iron accumulation (which shortens T2\* and can affect the T2-weighted diffusion signal). TBSS (tract-based spatial statistics) analyses show additional white matter changes in prefrontal, cingulate, and parietal tracts as cognitive involvement develops.

A practical limitation: DTI of the SN is technically challenging because the SN is small (~70 mm³ per hemisphere), surrounded by structures with very different diffusion properties (crus cerebri, red nucleus), and adjacent to CSF-filled spaces. Susceptibility-induced distortions in EPI (echo-planar imaging, the standard DTI readout) can geometrically displace and blur the SN. High-resolution multi-shot diffusion sequences and reverse-polarity distortion correction are essential for accurate quantitative SN-DTI.

---

## MR Spectroscopy

### Chemical Shift: Reading Molecular Environment from Frequency

The Larmor frequency of a proton is not just γB₀ — electrons orbiting the nucleus partially shield it from the external field, and different chemical environments provide different degrees of shielding. The frequency offset is characterized by the **chemical shift** δ (in parts per million, ppm) relative to a reference compound (tetramethylsilane, TMS):

\[ \delta = \frac{\nu_{sample} - \nu_{ref}}{\nu_{ref}} \times 10^6 \text{ ppm} \]

This tiny frequency difference — a few Hz at clinical field strengths — is sufficient to separate major brain metabolites in the MR spectrum.

### Key Brain Metabolites in PD

**N-acetylaspartate (NAA)** resonates at 2.02 ppm (N-acetyl CH₃ group). NAA is synthesized exclusively in mitochondria of neurons — it is not present in astrocytes or oligodendrocytes. It is the most prominent peak in the healthy brain spectrum. Reduced NAA/Cr ratio indicates neuronal loss or dysfunction. In PD striatum and SN: modest NAA reduction correlates with disease severity. In the context of mitochondrial dysfunction (a central PD mechanism), reduced NAA reflects directly the failure of mitochondria to synthesize it.

**Creatine (Cr)** at 3.02 ppm — phosphocreatine + creatine. Used as a reference because it is relatively stable across conditions. It represents energy buffering capacity.

**Choline (Cho)** at 3.22 ppm — primarily glycerophosphocholine and phosphocholine, markers of membrane synthesis and degradation. Elevated Cho/Cr suggests increased membrane turnover — relevant in inflammatory or demyelinating processes.

**Glutamate (Glu)** at ~2.1–2.35 ppm and **glutamine (Gln)** nearby. The Glx (Glu+Gln) peak is visible at lower field strengths. Elevated glutamate in a region suggests excitotoxic stress. This is relevant in the subthalamic nucleus (STN), which is overactive in PD — elevated STN Glu has been reported.

**Lactate (Lac)** at 1.33 ppm — a doublet due to J-coupling between the CH₃ and CH protons (separated by 7.1 Hz). Lactate is the end product of anaerobic glycolysis and appears when mitochondrial oxidative phosphorylation fails. Elevated lactate in the SN or striatum in PD would be direct evidence of mitochondrial energy failure — this measurement has been technically challenging due to the proximity of the Lac doublet to lipid peaks from the skull, but modern MEGA-PRESS editing sequences can isolate it.

**GABA (gamma-aminobutyric acid)** at 3.01 ppm (overlapping with Cr) — edited with MEGA-PRESS spectral editing. GABA is the major inhibitory neurotransmitter. Abnormal GABAergic tone in putamen and motor cortex is implicated in PD pathophysiology. Editing sequences can resolve GABA separately from creatine.

### Acquisition: Single-Voxel vs. MRSI

**Single-voxel spectroscopy (PRESS, STEAM)** places a rectangular voxel (typically 20–30 mm³) in a region of interest. Three orthogonal slice-selective RF pulses generate the voxel. PRESS (Point-Resolved Spectroscopy) uses a 90°–180°–180° scheme; STEAM uses 90°–90°–90°, allowing shorter TE at the cost of half the signal. SN spectroscopy requires careful voxel placement to minimize partial volume contamination from surrounding CSF and white matter.

**Magnetic Resonance Spectroscopic Imaging (MRSI)** acquires spectra from a 2D or 3D array of voxels simultaneously, providing metabolite maps. Limited by lower SNR per voxel and longer acquisition times. Useful for mapping metabolite distributions across the basal ganglia and cortex in a single session.

**Key PD application.** An intervention targeting mitochondrial function (ketone supplements, NAD+ precursors, complex I rescue) should — if effective at the cellular level — increase striatal NAA/Cr and potentially reduce lactate. MRS is the only MRI technique that reads mitochondrial metabolism directly. Changes in NAA/Cr could be detectable within 4–8 weeks of effective treatment — faster than any structural MRI metric.

---

## Combined Multimodal Protocols: Getting Everything in One Session

Modern 3T and 7T scanners can acquire multiple contrasts in a single session with careful protocol design. A well-optimized 45-minute session can yield:

**Multi-echo 3D GRE (15 min):** Acquires magnitude images at multiple echo times → R2\* map + susceptibility phase images → QSM. The same dataset provides susceptibility-weighted images (SWI) for visual nigrosome-1 assessment. At 3T, 6 echoes with TE from 4 to 30 ms is a common scheme.

**MT-prepared GRE (10 min):** NM-MRI acquisition with MT saturation pulse. Acquired at same spatial resolution as GRE for coregistration. Yields CNR map and SNpc volume. Shares geometric prescription with multi-echo GRE to enable direct voxelwise correlation of neuromelanin and iron metrics.

**DTI (12 min):** 64 diffusion directions at b = 1000 s/mm², 2-mm isotropic resolution. Tractography-based SN-putamen connectivity and SN voxelwise FA/MD. Requires separate acquisition (spin-echo EPI, not GRE).

**PRESS spectroscopy (5 min):** Single voxel in posterior putamen (most affected early) and one in the pons (reference). NAA/Cr, Glu, Cho/Cr.

**T1 MPRAGE (5 min):** 1 mm isotropic structural reference for segmentation, registration, and cortical thickness. Not a progression metric at short intervals but required for all spatial normalization steps.

From this 45-minute session, the outputs are: SNpc neuromelanin volume and CNR, nigral iron QSM, R2\*, nigrosome-1 sign, SN white matter microstructure (FA/MD), striatal metabolite ratios, and a structural reference — a complete mechanistic picture of the neuromelanin/iron/white matter axis simultaneously. Longitudinal analysis at 3-month intervals, with rigid same-session registration and a blinded ROI analyst, provides the tissue monitoring backbone for a high-frequency intervention study.

---

## A Note on Field Strength

At **3T**, all methods above are clinically applicable. The SN (~70 mm³) spans roughly 30–40 voxels at 0.7-mm in-plane NM-MRI resolution, which is adequate for volume and CNR estimation. R2\* and QSM precision are good. 3T is the current research standard.

At **7T**, the SNR gain (~2× for the same acquisition time) translates directly into either higher spatial resolution (voxel volume ~8× smaller, resolving individual nigrosome sub-regions) or higher temporal efficiency (same quality in half the time). QSM at 7T achieves phase SNR sufficient to detect individual ferritin-rich cell clusters within the SN. NM-MRI at 7T resolves individual nigral laminae. The tradeoff: more severe B₁ inhomogeneity in the midbrain (deep brain coverage is harder at 7T without special RF coils), and the B₁ inhomogeneity complicates MT saturation efficiency. Purpose-built RF coils for midbrain coverage at 7T are active areas of development. For a dedicated PD research protocol, 7T is the optimal platform where available.
