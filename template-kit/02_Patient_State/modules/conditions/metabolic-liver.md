# Metabolic & Liver Module
> **Scope:** Fatty liver (MASLD/NAFLD/MAFLD), liver function markers, lipids, triglycerides, metabolic syndrome, and hepatic functional impairment.
> **Always read alongside `index.md`** — this module does not repeat demographic, lifestyle, or cross-system context.
> **Last updated:** [DATE]

---

## ⚠️ Analytical Defaults (this module)

1. **Standard liver function tests (ALT, AST, GGT) measure structural damage, not function** — a normal LFT panel does not mean the liver is functioning normally; metabolic impairment (e.g. impaired lipid processing, protein synthesis, nutrient metabolism) can persist with fully normal LFTs
2. **Fatty liver is often a functional diagnosis** — in mild/moderate MASLD, ultrasound shows steatosis but bloodwork may be normal; do not dismiss functional impairment on the basis of normal ALT/AST/GGT alone
3. **Triglycerides require fasting interpretation** — a non-fasting triglyceride result is elevated by recent food intake; interpret with caution; note collection conditions
4. **All lifestyle causes must be confirmed excluded before attributing elevated triglycerides to hepatic impairment** — alcohol, refined carbohydrate excess, sugar, insulin resistance, hypothyroidism, and genetic hyperlipidaemia should each be explicitly assessed
5. **Lean phenotype MASLD is clinically distinct** — may occur at lower BMI thresholds than Western reference ranges assume; trial data from predominantly Western cohorts may not directly apply to all demographic groups; note relevant population context when interpreting
6. **Liver is a cross-system organ** — affects triglyceride clearance, iron metabolism (transferrin synthesis), red cell maturation (MCV, B12/folate processing), protein synthesis, and drug metabolism; do not assess liver findings in isolation

---

## 1. Personal Baselines

> Establish pre-disease liver function baseline from multiple readings before any acute event.

### 1a. Liver Function — Personal Baseline

| Marker | Personal Baseline | Ref Range (your lab) | Notes |
|--------|:-----------------:|:-------------------:|-------|
| ALP | [U/L] | [30–110 / adjust] | |
| GGT | [U/L] | [5–35 / adjust] | Sensitive to alcohol and fatty change |
| ALT | [U/L] | [5–35 / adjust] | Hepatocellular damage marker |
| AST | [U/L] | [5–30 / adjust] | |
| Bilirubin | [umol/L] | [1–20 / adjust] | |
| Albumin | [g/L] | [35–50 / adjust] | Liver synthesis marker |
| Total Protein | [g/L] | [60–80 / adjust] | |

*Source: [EV-XX — verified from pre-disease printout]*

### 1b. Lipids — Personal Baseline

| Marker | Personal Baseline | Ref Range | Notes |
|--------|:-----------------:|:---------:|-------|
| Cholesterol | [mmol/L] | [<5.5] | |
| Triglycerides | [mmol/L] | [<1.7] | Note if first measurement was post-diagnosis |
| HDLC | [mmol/L] | [>1.0] | |
| LDLC | [mmol/L] | [<3.5] | |
| Chol/HDLC ratio | | [<4.5] | |

*Note: If no pre-disease lipid data exists, state this explicitly. A first measurement taken during or after an acute event is not a baseline.*

### 1c. Metabolic Markers

| Marker | Value | Date | Notes |
|--------|:-----:|:----:|-------|
| Glucose (fasting) | [mmol/L] | | |
| Glucose (post-meal) | [mmol/L] | | Note timing |
| HbA1c | [%] | | |
| Urate | [mmol/L] | | Elevated in metabolic syndrome |
| CRP | [mg/L] | | Inflammatory marker |

---

## 2. Recent Results — Rolling Window

> **Rolling window — 3 most recent draws only.** Add newest date on the left; drop the oldest column when a 4th draw is added. Full longitudinal record is in `Raw Data/YYYY-MM-DD.md` files — this section holds only the working window for interpretation.
>
> **Δ (newest) column:** When updating this section, compute using the formula: `(newest_value − baseline) / baseline × 100`, rounded to 1 decimal place. Read baseline from Section 1 of this file — do not estimate. Use `NE` if baseline not yet established; `NA` if baseline concept does not apply.

### 2a. Liver Function — Recent

| Marker | [Newest date] | [Previous date] | [Earlier date] | Personal Baseline | Δ (newest) |
|--------|:-------------:|:---------------:|:--------------:|:-----------------:|:----------:|
| ALP (U/L) | | | | | |
| GGT (U/L) | | | | | |
| ALT (U/L) | | | | | |
| AST (U/L) | | | | | |
| Bilirubin (umol/L) | | | | | |
| Albumin (g/L) | | | | | |

*EV IDs: [Newest] = EV-XX | [Previous] = EV-XX | [Earlier] = EV-XX*

### 2b. Lipids — Recent

| Marker | [Newest date] | [Previous date] | [Earlier date] | Personal Baseline | Δ (newest) |
|--------|:-------------:|:---------------:|:--------------:|:-----------------:|:----------:|
| Cholesterol (mmol/L) | | | | | |
| Triglycerides (mmol/L) | | | | | |
| HDLC (mmol/L) | | | | | |
| LDLC (mmol/L) | | | | | |

*Fasting status: [Newest] = [fasting/non-fasting] | [Previous] = ... (critical for triglyceride interpretation)*

### 2c. Ultrasound / Imaging Summary

| Date | Finding | Performed by | EV Ref |
|------|---------|-------------|--------|
| [Date] | [e.g. Mild fatty liver / No steatosis / Moderate steatosis] | [Radiologist / gastroenterologist] | [EV-XX] |

### 2d. Fibrosis Assessment (if done)

| Date | Tool | Result | Score | Risk Category | EV Ref |
|------|------|--------|:-----:|:-------------:|--------|
| [Date] | FibroScan / FIB-4 / APRI | [Result] | [Score] | [Low / Indeterminate / High] | [EV-XX] |

#### FIB-4 Calculation Protocol

**Formula:** FIB-4 = (Age × AST) / (Platelets × √ALT)

**Risk thresholds:** < 1.30 = Low | 1.30 – 2.67 = Indeterminate | > 2.67 = High

**⚠️ Do not compute this formula using inline reasoning.** The square root step produces arithmetic errors when reasoned as prose. Use the method appropriate for your platform:

**Cowork (preferred — deterministic):**
Attempt bash execution first. If bash is available, run:
```bash
python3 -c "import math; age=AGE; ast=AST; alt=ALT; plt=PLATELETS; score=round((age*ast)/(plt*math.sqrt(alt)),2); cat='Low' if score<1.30 else ('High' if score>2.67 else 'Indeterminate'); print(f'FIB-4: {score} → {cat}')"
```
Substitute AGE, AST, ALT, PLATELETS with values from the current blood test file and patient profile. Read age from `index.md`. Store the printed result directly — do not re-derive it.

**All other platforms (step-by-step — required if bash unavailable):**
Work through each step explicitly before combining:
```
Step 1 — Gather inputs:
  Age:       [X] years          ← from index.md
  AST:       [X] U/L            ← from Raw Data/YYYY-MM-DD.md
  ALT:       [X] U/L            ← from Raw Data/YYYY-MM-DD.md
  Platelets: [X] × 10⁹/L       ← from Raw Data/YYYY-MM-DD.md

Step 2 — Compute √ALT:
  √ALT = [show working, e.g. √42 ≈ 6.48]

Step 3 — Numerator:
  Age × AST = [X × X] = [result]

Step 4 — Denominator:
  Platelets × √ALT = [X × X] = [result]

Step 5 — FIB-4:
  Numerator / Denominator = [result], rounded to 2 decimal places

Step 6 — Risk category:
  [< 1.30 → Low | 1.30–2.67 → Indeterminate | > 2.67 → High]
```
Flag the result: *"AI-computed — verify with an independent FIB-4 calculator before clinical use."*

---

## 3. Active Findings & Clinical Interpretation

### 3a. Liver Function — Current Status

**Current pattern:** [All markers normalised / Persistent transaminase elevation / Isolated GGT elevation / etc.]

**Trajectory:** [Improving / Stable / Worsening]

**Acute event history:** [Document any acute liver inflammation episodes with dates and peak values]

**Structural vs. functional impairment distinction:**
- Structural markers (ALT, AST, GGT, ALP): [Current status]
- Functional markers (Albumin, Bilirubin, Transferrin — see haematology module): [Current status]
- **Key insight:** [e.g. "LFTs within range but functional impairment suspected given declining Albumin trend and rising Bilirubin across three draws"]

---

### 3b. Fatty Liver (MASLD) — Status

**Diagnosis basis:** [Ultrasound / CT / MRI / Clinical — date]
**Current grade:** [Mild / Moderate / Severe / Resolving — with date and source]

**Lifestyle optimisation status:**
- Alcohol: [Eliminated / Reduced / Ongoing]
- Diet: [Description of changes made]
- Exercise: [Changes made]
- Duration of optimisation: [X months]
- Response: [Improved / Unchanged — if unchanged after 12+ months of full optimisation, lifestyle causes are effectively excluded]

**Fibrosis risk assessment:**
- FIB-4 score: [Calculate] — [Risk category]
- FibroScan result: [If done]
- **Staging needed before pharmacological treatment:** Yes / No / Already done

---

### 3c. Triglycerides — Assessment

**Three or more data points required to establish a trajectory.** Document each:

| Date | Value | Fasting? | Context |
|------|:-----:|:--------:|---------|
| [Date] | [mmol/L] | [Y/N] | [e.g. During acute inflammation / stable lifestyle / post-meal] |

**Cause assessment (all must be addressed before concluding hepatic cause):**

| Cause | Status | Evidence |
|-------|:------:|---------|
| Alcohol | ❌ Excluded / ⚠️ Active / ✅ Not applicable | |
| Refined carbohydrates / sugar | ❌ Excluded / ⚠️ Active | |
| Insulin resistance | ❌ Excluded (Glucose/HbA1c normal) / ⚠️ Suspected | |
| Hypothyroidism | ❌ Excluded / ⚠️ Suspected / ✅ TSH normal | |
| Genetic hyperlipidaemia | ❌ Excluded / ⚠️ Suspected | |
| Hepatic clearance impairment | ⚠️ Most plausible remaining cause / ❌ Excluded | |

**Trajectory:** [Stable / Slowly rising / Improving / Resolving]

---

## 4. Treatment Status

### 4a. Lifestyle Interventions
| Intervention | Status | Duration | Documented Response |
|-------------|:------:|:--------:|-------------------|
| Alcohol cessation | [Done / Not indicated] | | |
| Dietary modification | [Done / Partial / Pending] | | |
| Exercise programme | [Done / Partial / Pending] | | |
| Weight management | [Done / Not applicable] | | |
| **Lifestyle ceiling reached?** | **Yes / No / Uncertain** | | |

### 4b. Pharmacological Options

> Note: All pharmacological options require clinician assessment. Document what has been discussed and its status.

| Option | Regulatory Status | Evidence Level | Discussion Status | Notes |
|--------|:-----------------:|:--------------:|:-----------------:|-------|
| [e.g. Semaglutide / GLP-1] | [Approved for MASLD / Off-label] | [Phase 3 trial data] | [Discussed / Pending / Declined] | [Cost, contraindications, monitoring requirements] |
| [e.g. Vitamin E] | | | | |
| [Other] | | | | |

### 4c. Monitoring Plan
- **Ultrasound frequency:** [e.g. 6-monthly]
- **LFT frequency:** [e.g. 6-monthly]
- **Lipid panel frequency:** [e.g. Annual]
- **FibroScan:** [Scheduled / Not yet done / Completed date]
- **Responsible clinician:** [GP / Gastroenterologist]

---

## 5. Cross-System Links

**Liver → Haematology (Transferrin):** Transferrin is synthesised by the liver. Persistent sub-baseline Transferrin across multiple readings may reflect ongoing hepatic functional impairment, independent of iron level or infusion history. See `haematology.md`.

**Liver → Haematology (MCV):** Liver disease can cause macrocytic changes in red cells independent of B12/folate deficiency. MCV above personal baseline with normal B12/folate warrants assessment for hepatic contribution.

**Liver → Lipids (Triglycerides):** Impaired hepatic triglyceride clearance is the mechanism for persistently elevated triglycerides in MASLD. Resolution requires treating the underlying fatty liver, not adjusting diet alone (if diet is already optimised).

**Liver → Drug Metabolism:** Liver functional impairment affects metabolism of many drugs. Relevant when starting new medications — flag to prescriber.

**Gynaecology → Liver (Hormonal Effects):** Oestrogen fluctuation in perimenopause can affect lipid metabolism. Hormonal context should be noted when interpreting lipid trends. See `hormonal-reproductive.md`.

---

## 6. Research Notes

> Summary of current treatment landscape for this patient's conditions. Full detail in `research/` files.

| Topic | EV Ref | Researched | Key Finding | Refresh Due |
|-------|--------|:----------:|------------|:-----------:|
| [e.g. GLP-1 for MASLD] | [EV-XX] | [Date] | [1-line summary] | [Date] |

---

## 7. Open Questions

1. [Question 1 — e.g. "FibroScan needed before formal pharmacological treatment eligibility can be assessed"]
2. [Question 2 — e.g. "Discuss pharmacological options at next specialist appointment — note any contraindications from other active conditions"]
3. [Question 3]

---

## 8. Sources

| Source | Content | Verified |
|--------|---------|---------|
| [EV-XX] `Raw Data/YYYY-MM-DD.md` | [Description] | ✅ / ⚠️ |

---

*Next update: [Trigger — e.g. "After next ultrasound; after next lipid panel; after pharmacological treatment decision"]*
