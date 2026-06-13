# Haematology Module
> **Scope:** Full Blood Count (FBC), Iron Studies, B12/Folate, and related haematological findings.
> **Always read alongside `index.md`** — this module does not repeat demographic, lifestyle, or cross-system context held there.
> **Last updated:** [DATE]

---

## ⚠️ Analytical Defaults (this module)

1. **Low-normal WCC/neutrophils may be this patient's lifelong personal baseline** — establish this from pre-disease data; do not flag as new finding if it is constitutional
2. **Interpret MCV against personal baseline, not just population range** — shifts above or below personal baseline are clinically significant even within the reference range
3. **Ferritin alone is insufficient to assess iron status** — always interpret alongside transferrin saturation, serum iron, and transferrin level; ferritin is an acute phase reactant and can be elevated by inflammation independent of iron stores
4. **B12 and Folate results taken during active supplementation are not interpretable for deficiency** — flag if supplements were taken; note washout requirement
5. **Transferrin is synthesised by the liver** — persistent sub-baseline Transferrin may reflect hepatic functional impairment, not primary iron disorder
6. **Haematology rarely exists in isolation** — liver disease affects transferrin synthesis, red cell maturation (MCV), and B12/folate processing; chronic blood loss (from any source) drives iron demand; chronic inflammation affects ferritin and WCC; identify which other systems may be contributing before drawing conclusions from FBC alone

---

## 1. Personal Baselines

> Establish pre-disease baseline values from multiple readings before any acute event. These are more clinically meaningful than population reference ranges for interpretation.

### 1a. Full Blood Count — Personal Baseline

| Marker | Personal Baseline | Ref Range (your lab) | Notes |
|--------|:-----------------:|:-------------------:|-------|
| Haemoglobin (Hb) | [g/L] | [115–165 / adjust] | |
| Red Cell Count (RCC) | [x10¹²/L] | [4.20–5.40 / adjust] | |
| Haematocrit (HCT) | | | |
| MCV | [fL] | [80–98 / adjust] | Key personal baseline marker |
| MCH | [pg] | | |
| MCHC | [g/L] | | |
| RDW | [%] | | |
| WCC | [x10⁹/L] | [4.0–11.0] | Note if constitutionally low |
| Neutrophils | [x10⁹/L] | [2.0–7.5] | Note if constitutionally low |
| Lymphocytes | [x10⁹/L] | | |
| Platelets | [x10⁹/L] | | |

*Source: [e.g. "Verified from EV-01 (Mar 2022 printout) and EV-02 (Jan 2023 printout)"]*

### 1b. Iron Studies — Personal Baseline

| Marker | Personal Baseline | Ref Range (your lab) | Notes |
|--------|:-----------------:|:-------------------:|-------|
| Serum Iron | [umol/L] | | |
| Transferrin | [g/L] | | Watch for persistent sub-baseline |
| Transferrin Saturation | [%] | | |
| Ferritin | [ug/L] | | |

*Source: [EV-XX]*

### 1c. B12 / Folate — Personal Baseline

| Marker | Personal Baseline | Date | Source |
|--------|:-----------------:|:----:|--------|
| Vitamin B12 | [pmol/L] | [Date] | [EV-XX] |
| Active B12 | [pmol/L] | [Date] | [EV-XX] |
| Serum Folate | [nmol/L] | [Date] | [EV-XX] |

---

## 2. Recent Results — Rolling Window

> **Rolling window — 3 most recent draws only.** Add newest date on the left; drop the oldest column when a 4th draw is added. Full longitudinal record is in `Raw Data/YYYY-MM-DD.md` files — this section holds only the working window for interpretation.
>
> **Δ (newest) column:** When updating this section, compute using the formula: `(newest_value − baseline) / baseline × 100`, rounded to 1 decimal place. Read baseline from Section 1 of this file — do not estimate. Use `NE` if baseline not yet established; `NA` if baseline concept does not apply.

### 2a. Full Blood Count — Recent

| Marker | [Newest date] | [Previous date] | [Earlier date] | Personal Baseline | Δ (newest) |
|--------|:-------------:|:---------------:|:--------------:|:-----------------:|:----------:|
| Hb (g/L) | | | | | |
| RCC (x10¹²/L) | | | | | |
| MCV (fL) | | | | | |
| MCH (pg) | | | | | |
| WCC (x10⁹/L) | | | | | |
| Neutrophils (x10⁹/L) | | | | | |
| Platelets (x10⁹/L) | | | | | |

*EV IDs: [Newest] = EV-XX | [Previous] = EV-XX | [Earlier] = EV-XX*

### 2b. Iron Studies — Recent

| Marker | [Newest date] | [Previous date] | [Earlier date] | Personal Baseline | Δ (newest) |
|--------|:-------------:|:---------------:|:--------------:|:-----------------:|:----------:|
| Iron (umol/L) | | | | | |
| Transferrin (g/L) | | | | | |
| Transferrin Sat (%) | | | | | |
| Ferritin (ug/L) | | | | | |

### 2c. B12 / Folate — Recent

| Marker | [Newest date] | [Previous date] | [Earlier date] | Personal Baseline | Δ (newest) |
|--------|:-------------:|:---------------:|:--------------:|:-----------------:|:----------:|
| Vitamin B12 (pmol/L) | | | | | |
| Active B12 (pmol/L) | | | | | |
| Serum Folate (nmol/L) | | | | | |

---

## 3. Active Findings & Clinical Interpretation

### 3a. Haemoglobin & RCC — Pattern Assessment

**Current pattern:** [Describe — e.g. persistently low-normal, stable, deteriorating, improving]

**Trajectory:** [Summarise direction across available data points]

**Context:** [Note what conditions were present during collection — lifestyle state, concurrent illness, supplement status]

**Documented symptoms consistent with this pattern:**
- [e.g. Fatigue, pallor, exertional breathlessness, palpitations]

---

### 3b. MCV — Assessment

**Current pattern:** [Within personal baseline / Above personal baseline / Below personal baseline]

**If elevated (macrocytosis) — assessment:**
- B12 deficiency: [Ruled out / Cannot exclude / Confirmed — note why]
- Folate deficiency: [Ruled out / Cannot exclude / Confirmed — note why]
- Liver disease effect: [Plausible / Under investigation / Ruled out]
- Hypothyroidism: [Ruled out / Under investigation]

**If reduced (microcytosis) — assessment:**
- Iron deficiency: [Ruled out / Cannot exclude / Confirmed]
- Thalassaemia trait: [Ruled out / Untested / Confirmed]
- Chronic disease: [Plausible / Under investigation]

---

### 3c. WCC & Neutrophils — Assessment

**Constitutional baseline established:** Yes / No — [note source if yes]

**Current trend:** [Stable at personal baseline / Improving / Declining / Below personal baseline]

**Monitoring note:** [e.g. "Any drop below [X] for neutrophils or [X] for WCC would be clinically meaningful for this patient"]

---

### 3d. Iron Studies — The Full Picture

**Infusion or supplementation history:** [Document any iron infusions or supplementation; note dates; note that post-infusion Ferritin elevation does not indicate iron adequacy until saturation and serum iron are confirmed]

**Current functional iron status:** [Adequate / Deficient / Overloaded — with evidence]
- Serum Iron: [value and interpretation]
- Transferrin Saturation: [value — this is the most sensitive functional marker; below ~20% indicates functional deficiency]
- Ferritin: [value — context-dependent; elevated in inflammation; post-infusion residual; note caveats]
- Transferrin: [value vs. personal baseline — persistent sub-baseline may indicate hepatic impairment]

**Key distinction:** Transferrin Saturation and Serum Iron reflect *available* iron for red cell production. Ferritin reflects *stored* iron. These can dissociate — high Ferritin with low Saturation indicates functional deficiency despite adequate stores.

---

### 3e. B12 / Folate — Current Status

> ⚠️ If supplements were being taken at time of draw: results are not interpretable for deficiency. Document supplement status and note washout requirement.

**Current status:** [Within range and off supplements → adequate / On supplements → supplemented status only / Cannot exclude deficiency]

**Washout re-test required:** Yes / No — [reason]

**Active B12 status:** [Tested and normal / Tested and low / Not tested — this is the more sensitive functional marker]

---

## 4. Contributor Assessment

| Contributor | Status | Evidence | EV Ref |
|-------------|:------:|---------|--------|
| **Chronic blood loss** (menstrual, GI, or other source) | ✅ Confirmed / ⚠️ Suspected / ❌ N/A | [Evidence — note source] | [EV-XX] |
| **Iron deficiency** | ✅ Confirmed / ⚠️ Suspected / ❌ Excluded | | |
| **B12 deficiency** | ✅ Confirmed / ⚠️ Cannot exclude / ❌ Excluded | | |
| **Folate deficiency** | ✅ Confirmed / ⚠️ Cannot exclude / ❌ Excluded | | |
| **Hepatic functional impairment** | ✅ Confirmed / ⚠️ Probable / ❌ Excluded | | |
| **Hypothyroidism** | ✅ Confirmed / ⚠️ Suspected / ❌ Excluded | | |
| **Chronic disease (other)** | ✅ Confirmed / ⚠️ Suspected / ❌ Excluded | | |

---

## 5. Cross-System Links

**Liver → Transferrin:** Transferrin is synthesised by the liver. Sub-baseline Transferrin across multiple readings despite adequate iron stores may indicate ongoing hepatic functional impairment. See `[liver module]`.

**Liver → MCV:** Liver disease is a recognised cause of macrocytosis independent of B12/folate. If MCV is above personal baseline and B12/folate are confirmed normal, assess for hepatic contribution.

**Gynaecology → Iron:** Menstrual blood loss from conditions such as adenomyosis or fibroids chronically elevates iron demand. If iron deficiency recurs despite correction, consider the adequacy of gynaecological management. See `[hormonal-reproductive module]`.

**Anaemia → Exercise Tolerance:** Low Hb limits exercise capacity and recovery. Post-exercise fatigue and HRV dips may reflect haematological constraint, not cardiovascular deconditioning. Calibrate exercise intensity against current Hb.

**WCC/Neutrophils → Immune Load:** Trending WCC/neutrophils are an early signal of immune stress or systemic illness. A downward trend during a high-stress period or acute illness is clinically meaningful — compare against the patient's personal constitutional baseline before flagging as new.

---

## 6. Open Questions

1. [Question 1 — e.g. "Has the GP been informed of re-emerging iron deficiency? Is repeat infusion indicated?"]
2. [Question 2 — e.g. "Re-test B12, Active B12, and Folate off supplements — when is washout complete?"]
3. [Question 3]

---

## 7. Sources

| Source | Content | Verified |
|--------|---------|---------|
| [EV-XX] `Raw Data/YYYY-MM-DD.md` | [Description] | ✅ / ⚠️ |

---

*Next update: [Trigger — e.g. "After next FBC; after repeat iron studies; after gynaecology treatment decision"]*
