# Protocol
## Chapter 3 — IFTTT Logic

---

This chapter defines the conditional logic that maps benchmark deviations to interventions. Chapter 1 (Measurements) specifies the benchmarks and how to evaluate them. Chapter 2 (Interventions) catalogs available actions. This chapter specifies **when** to act.

Target values and acceptable ranges for each benchmark are defined in the [Circadian Tracking Table](https://docs.google.com/spreadsheets/d/1ZSRs-0XkmKa_bJxXlISOKpBUK7OAxhki/edit?gid=1665814829#gid=1665814829). Deviations outside range trigger the rules below.

---

## 1. Protocol Principles

**Phase 1: Apply the theoretical ideal regimen** — Implement the full intervention set from Chapter 2 (Interventions) at once: wake-time anchor, morning outdoor light, evening melanopic suppression, true darkness, bright days, daytime-aligned feeding, exercise earlier, conflicting zeitgeber elimination, night cooling, plus measurement-supportive controls (caffeine cutoff, alcohol avoidance during assessment). There is no time for one-by-one introduction.

**Phase 2: Fix what doesn't optimize (after 2 weeks)** — Assess benchmarks ~2 weeks after regimen initiation. Deviations that remain outside target trigger the IFTTT rules below. Apply targeted interventions to address what failed to optimize.

**Benchmark-guided** — Protocol adjustments are driven by deviations observed in the Tracking Table.

**Zeitgeber priority** — When multiple interventions could address a deviation, prefer higher-hierarchy levers first: light → sleep → feeding → activity → consistency.

---

## 2. Central Phase Stability

*Reflects strength of central clock entrainment and resistance to phase drift.*

### IF DLMO stability is low (high day-to-day variance)

**THEN** apply, in order:

1. **Wake-time anchor** — Fixed rise time anchors SCN and reduces phase noise.
2. **Conflicting zeitgeber elimination** — Align light, sleep, feeding, activity across weekdays and weekends.
3. **Social schedule stabilization** — Minimize late nights and irregular timing.
4. **Morning outdoor light** — Strengthens photic entrainment.

---

## 3. Sleep–Circadian Alignment

*Quantifies alignment between biological night and behavioral sleep.*

### IF sleep onset phase angle is too large (sleep onset too late relative to DLMO)

**THEN** apply, in order:

1. **Evening melanopic suppression** — Earlier dimming, avoid blue/overhead light and screens.
2. **Wake-time anchor** — Stabilizes phase, may shift sleep onset earlier over time.
3. **Exercise earlier in the active phase** — Late exercise delays sleep onset.

---

### IF sleep onset phase angle is too small (sleep onset too early relative to DLMO)

**THEN** apply:

1. **Morning outdoor light** — Advances phase; may shift DLMO earlier to align with existing sleep.
2. **Wake-time anchor** — Ensure consistency; phase advance from light requires stable schedule.

---

### IF sleep midpoint phase angle is deviant (sleep midpoint misaligned with DLMO)

**THEN** apply:

1. **Wake-time anchor** — Central alignment lever for sleep timing.
2. **Evening melanopic suppression** (if phase delayed) or **Morning outdoor light** (if phase advanced).
3. **Conflicting zeitgeber elimination** — Weekend/weekday alignment.

---

### IF sleep midpoint stability is low (high day-to-day variability)

**THEN** apply, in order:

1. **Wake-time anchor** — Primary stabilizer for sleep timing.
2. **Conflicting zeitgeber elimination** — Remove schedule drift.
3. **Social schedule stabilization** — Reduce social jetlag.

---

## 4. Temperature–Circadian Alignment

*Reflects autonomic and thermoregulatory coupling to the central clock.*

### IF temperature minimum phase angle (relative to DLMO) is deviant

**THEN** apply:

1. **Morning outdoor light** — Advances phase; temperature minimum follows.
2. **Evening melanopic suppression** — Prevents phase delay.
3. **Wake-time anchor** — Stabilizes central phase; peripheral temperature couples over time.

---

### IF temperature minimum phase angle (relative to sleep midpoint) is deviant

**THEN** apply:

1. **Night cooling** — Reinforces thermal rhythm and sleep consolidation.
2. **Wake-time anchor** — Aligns sleep episode with circadian temperature cycle.

---

### IF temperature rhythm amplitude is low (flat peak-to-trough)

**THEN** apply, in order:

1. **Bright days** — Day–night thermal contrast depends on daytime activation.
2. **True darkness during sleep** — Night cooling and darkness reinforce night phase.
3. **Night cooling** — Reinforces amplitude.
4. **Daytime-aligned feeding** — Metabolic rhythm supports thermal rhythm.

---

### IF temperature minimum stability is low (high day-to-day variance)

**THEN** apply:

1. **Wake-time anchor** — Stabilizes central and peripheral timing.
2. **Conflicting zeitgeber elimination** — Reduces phase noise.

---

## 5. Rest–Activity Rhythmicity

*Reflects consolidation and consistency of behavioral rhythms.*

### IF relative amplitude is low (weak active/rest contrast)

**THEN** apply, in order:

1. **Bright days** — Light drives rest–activity consolidation.
2. **True darkness during sleep** — Sharpens day–night boundary.
3. **Daytime-aligned feeding** — Metabolic compartmentalization supports behavioral contrast.
4. **Exercise earlier in the active phase** — Reinforces active-phase signature.

---

### IF interdaily stability is low (activity pattern inconsistent across days)

**THEN** apply:

1. **Conflicting zeitgeber elimination** — Align schedules across days.
2. **Wake-time anchor** — Anchors daily structure.
3. **Social schedule stabilization** — Reduces weekend/weekday drift.

---

### IF intradaily variability is high (fragmented activity within day)

**THEN** apply:

1. **Bright days** — Consolidates wakefulness; reduces daytime napping/fragmentation.
2. **Daytime-aligned feeding** — Meal timing structures the day.
3. **Exercise earlier in the active phase** — Defines active block.
4. **Morning priming and evening downshifting** — Reduces evening fragmentation.

---

## 6. Endocrine Rhythmicity

*Reflects HPA-axis coupling and diurnal regulation.*

### IF cortisol awakening response is blunted

**THEN** apply:

1. **Wake-time anchor** — Consistent wake time entrains CAR.
2. **Morning outdoor light** — Light at wake reinforces HPA response.
3. **True darkness during sleep** — Preserves nocturnal cortisol decline and morning contrast.

---

### IF cortisol peak timing is misaligned (relative to wake time)

**THEN** apply:

1. **Morning outdoor light** — Advances phase; cortisol peak follows.
2. **Wake-time anchor** — Stabilizes phase.
3. **Evening melanopic suppression** — Prevents phase delay.

---

### IF daytime cortisol decline is blunted

**THEN** apply:

1. **Bright days / True darkness** — Amplitude depends on day–night contrast.
2. **Daytime-aligned feeding** — Night feeding elevates evening cortisol.
3. **Evening melanopic suppression** — Light at night blunts decline.

---

### IF evening cortisol suppression is insufficient

**THEN** apply:

1. **True darkness during sleep** — Light suppresses melatonin and elevates cortisol.
2. **Evening melanopic suppression** — Reduces evening light load.
3. **Daytime-aligned feeding** — Late eating extends metabolic day.

---

## 7. Metabolic Rhythmicity

*Reflects circadian regulation of glucose and metabolic compartmentalization.*

### IF nocturnal glucose stability is low (high nighttime variability)

**THEN** apply:

1. **Daytime-aligned feeding** — Night feeding drives nocturnal glucose excursions.
2. **True darkness during sleep** — Light at night disrupts metabolic quiescence.
3. **Conflicting zeitgeber elimination** — Irregular feeding fragments rhythms.

---

### IF dawn glucose rise timing is misaligned

**THEN** apply:

1. **Wake-time anchor** — Dawn rise couples to wake time.
2. **Daytime-aligned feeding** — Hepatic clock entrains to feeding; alignment with DLMO requires consistent schedule.
3. **Morning outdoor light** — Phase alignment.

---

### IF day–night glucose contrast is low (flat day/night difference)

**THEN** apply:

1. **Daytime-aligned feeding** — Confines eating to day; night becomes metabolically quiescent.
2. **Bright days / True darkness** — Light structure supports metabolic compartmentalization.
3. **Exercise earlier in the active phase** — Reinforces metabolic day.

---

### IF postprandial glucose dynamics are dysregulated

**THEN** apply:

1. **Daytime-aligned feeding** — Consistent meal timing; avoid late eating when insulin sensitivity is lowest.
2. **Exercise earlier in the active phase** — Improves insulin sensitivity; timing matters.
3. **Morning outdoor light** — Phase-dependent insulin sensitivity.

---

## 8. Cross-System Coherence

*Reflects internal synchrony across central, autonomic, behavioral, endocrine, and metabolic metrics.*

### IF phase coherence is low (subsystems out of phase with each other)

**THEN** apply, in order:

1. **Conflicting zeitgeber elimination** — Removes cue conflict; allows subsystems to realign.
2. **Wake-time anchor** — Common anchor for all systems.
3. **Morning outdoor light** — Sets SCN; periphery follows.
4. **Daytime-aligned feeding** — Aligns peripheral metabolic clocks with central phase.
5. **Exercise earlier in the active phase** — Reinforces peripheral coordination.

---

### IF composite synchrony score is below target (after 2-week assessment)

**THEN** address the most deviant benchmark first (see Tracking Table). Apply the corresponding rule above. Re-evaluate composite after next 2-week cycle. If multiple benchmarks are equally deviant, prioritize in order: phase stability → amplitude → stability → coherence.

---

## 9. Measurement-Supportive Rules

*When measurement validity is the priority.*

### IF in assessment or optimization phase (active measurement period)

**THEN** apply:

1. **Caffeine control** — Fixed early-day cutoff. Reduces masking of sleep pressure and actigraphy.
2. **Alcohol avoidance** — Avoid during assessment. Disrupts sleep architecture and hormone rhythms.
3. **Social schedule stabilization** — Minimize late nights and irregular timing during measurement periods.

---

## 10. Rule Summary

- **DLMO stability** (Low) → Wake-time anchor
- **Sleep onset phase angle** (Too large) → Evening melanopic suppression
- **Sleep onset phase angle** (Too small) → Morning outdoor light
- **Sleep midpoint stability** (Low) → Wake-time anchor
- **Temperature amplitude** (Low) → Bright days
- **Temperature minimum stability** (Low) → Wake-time anchor
- **Relative amplitude** (Low) → Bright days
- **Interdaily stability** (Low) → Conflicting zeitgeber elimination
- **Intradaily variability** (High) → Bright days
- **Cortisol awakening response** (Blunted) → Wake-time anchor
- **Cortisol peak timing** (Misaligned) → Morning outdoor light
- **Evening cortisol suppression** (Insufficient) → True darkness
- **Nocturnal glucose stability** (Low) → Daytime-aligned feeding
- **Day–night glucose contrast** (Low) → Daytime-aligned feeding
- **Phase coherence** (Low) → Conflicting zeitgeber elimination

---

*Previous: Interventions*
