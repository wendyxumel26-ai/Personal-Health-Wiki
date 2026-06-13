# Oncology Module
> **Scope:** Cancer staging, tumour markers, treatment line tracking, surveillance monitoring, and quality-of-life considerations during and after treatment.
> **Always read alongside `index.md`** — this module does not repeat demographic, lifestyle, or cross-system context.
> **Last updated:** [DATE]

---

## ⚠️ Analytical Defaults (this module)

1. **Tumour markers are not diagnostic on their own** — CA-125, CEA, AFP, PSA and others have known false positive and false negative rates; they are most useful for monitoring trend in a confirmed diagnosis, not for initial diagnosis
2. **Interpret tumour markers against personal baseline trend, not a single threshold** — a doubling of a marker within an individual's range may be more significant than a value that crosses the population threshold; trajectory matters more than absolute value
3. **Treatment toxicity and side effects are part of the clinical picture** — haematological, hepatic, neurological, and organ-specific toxicities from chemotherapy, radiation, or targeted therapy affect interpretation of blood results obtained during or after treatment; note treatment status for every result
4. **Scan results and blood results tell different stories** — radiological response (tumour size) and biochemical response (tumour markers) can diverge; document both and note which aligns with clinical status
5. **Post-treatment surveillance has defined intervals** — the monitoring schedule reflects the specific relapse risk profile of the cancer type and treatment; document the protocol and flag any deviation
6. **Survivorship effects are long-term** — cardiac toxicity from anthracyclines, neuropathy from platinum agents, secondary malignancy risk from alkylating agents, and early menopause from certain treatments can persist years to decades post-treatment
7. **Mental health is a measurable clinical variable in oncology** — distress, anxiety, and depression affect adherence, immune function, and outcomes; document and flag as part of the clinical picture

---

## 1. Diagnosis Summary

| Field | Value |
|-------|-------|
| **Primary diagnosis** | [Cancer type — e.g. Breast cancer, Colorectal adenocarcinoma, etc.] |
| **Histology / subtype** | [e.g. Invasive ductal carcinoma, ER+/PR+/HER2-; High-grade serous ovarian; etc.] |
| **Stage at diagnosis** | [Stage I / II / III / IV — with TNM if known: T[X] N[X] M[X]] |
| **Diagnosis date** | [Date] |
| **Diagnosed by** | [Institution / Clinician] |
| **Genomic / molecular profile** | [e.g. BRCA1/2 status; MSI status; KRAS mutation; HER2 amplification — note if not tested] |
| **EV reference** | [EV-XX — pathology report] |

---

## 2. Treatment History

### 2a. Treatment Lines

| Line | Treatment | Regimen | Start Date | End Date | Reason Stopped | Response | EV Ref |
|------|-----------|---------|:----------:|:--------:|---------------|---------|--------|
| 1st line | [e.g. Chemotherapy] | [e.g. AC-T / FOLFOX / Carbo-Paclitaxel] | [Date] | [Date] | [Completed / Progression / Toxicity] | [CR / PR / SD / PD] | [EV-XX] |
| 2nd line | | | | | | | |
| [Adjuvant/Neoadjuvant] | | | | | | | |
| [Hormonal] | | | | | | | |
| [Targeted] | | | | | | | |
| [Immunotherapy] | | | | | | | |
| [Radiation] | [Site / dose / fractions] | | | | | | |
| [Surgery] | [Procedure] | | | | | | |

### 2b. Current Treatment Status
**Current status:** [On treatment / Surveillance / Completed treatment DATE / Palliative intent]
**Current regimen:** [If applicable]
**Next cycle / appointment:** [Date]
**Responsible oncologist:** [Name / Institution]

### 2c. Documented Side Effects & Toxicities

| Toxicity | Grade (CTCAE) | Onset | Resolution | Management | EV Ref |
|----------|:------------:|:-----:|:----------:|-----------|--------|
| [e.g. Peripheral neuropathy] | [1–4] | [Date/Cycle] | [Ongoing / Resolved DATE] | [Dose reduction / Stopped / Symptomatic] | |
| [e.g. Myelosuppression] | | | | | |
| [e.g. Cardiotoxicity] | | | | | |
| [e.g. Fatigue] | | | | | |
| [Other] | | | | | |

---

## 3. Tumour Markers — Rolling Window

> **Critical:** Always note whether the patient was on treatment at the time of each marker measurement — treatment significantly affects interpretation.
> **Rolling window — 3 most recent draws only.** Add newest date on the left; drop the oldest column when a 4th draw is added. Full longitudinal record is in `Raw Data/YYYY-MM-DD.md` files.
>
> **Δ vs nadir column:** When updating, compute using the formula: `(newest_value − nadir) / nadir × 100`, rounded to 1 decimal place. Read nadir from the Nadir Register below — do not estimate. Use `NE` if no nadir established yet.
>
> ⚠️ **Velocity Override Rule:** If Δ vs nadir is ≥ +50% across any three consecutive readings — even if all absolute values remain within the population reference range — this must be escalated immediately to an Open Question in Section 7. Do not wait for an out-of-range flag.

| Marker | [Newest date] | [Previous date] | [Earlier date] | Treatment Status at Each Draw | Δ vs nadir (newest) |
|--------|:-------------:|:---------------:|:--------------:|------------------------------|:-------------------:|
| [CA-125 / CEA / AFP / PSA / CA 19-9 / LDH / β-hCG / other] | | | | | |
| [Second marker if applicable] | | | | | |

*EV IDs: [Newest] = EV-XX | [Previous] = EV-XX | [Earlier] = EV-XX*

**Trajectory:** [Rising / Falling / Stable / Responding to treatment / Rising despite treatment]

### 3a. Nadir Register

> **Nadir** = the lowest recorded post-treatment value for each marker. This is the reference point for all velocity calculations — not the pre-treatment baseline and not the population reference range.
> **Update rule:** When a new reading is lower than the stored nadir, update the nadir and record the date. Never recalculate nadir from memory — read this table.

| Marker | Nadir value | Nadir date | EV ref | Notes |
|--------|:-----------:|:----------:|--------|-------|
| [Marker name] | [Value + unit] | [YYYY-MM-DD] | [EV-XX] | [e.g. "Lowest recorded post-treatment; prior readings still declining"] |
| [Second marker] | | | | |

**Pre-treatment baseline (if known):** [Value, date, EV ref — note explicitly if no pre-treatment baseline was established]

---

## 4. Imaging & Scan Summary

| Date | Modality | Finding | Response Assessment | Compared To | EV Ref |
|------|:--------:|---------|:------------------:|:-----------:|--------|
| [Date] | [CT / PET-CT / MRI / US] | [Describe key finding — e.g. "3cm hepatic lesion; lymph node response"] | [CR / PR / SD / PD / NED] | [Prior scan DATE] | [EV-XX] |

---

## 5. Haematological Monitoring During/After Treatment

> Treatment-related haematological changes must be distinguished from disease-related or pre-existing findings. Document what pre-existed treatment.

| Marker | Pre-treatment | [On treatment — cycle X] | [Post-treatment] | Personal Baseline |
|--------|:------------:|:------------------------:|:----------------:|:-----------------:|
| Hb (g/L) | | | | |
| WCC (x10⁹/L) | | | | |
| Neutrophils (x10⁹/L) | | | | |
| Platelets (x10⁹/L) | | | | |

**Nadir management:**
- **G-CSF (growth factor support):** [Used / Not used / Protocol X]
- **Transfusion threshold:** [Hb <X → transfuse]
- **Platelet transfusion threshold:** [Platelets <X]
- **Dose reductions required:** [Yes — describe / No]

---

## 6. Organ Function Monitoring

> Many treatments require monitoring of specific organ function. Document baseline and any changes.

> **Rolling window — 3 most recent assessments only.** Add newest date on the left; drop oldest when a 4th is added. Full record in `Raw Data/` files.

| Organ / System | Baseline | [Newest date] | [Previous date] | [Earlier date] | Monitoring Protocol | Alert Threshold |
|---------------|:--------:|:-------------:|:---------------:|:--------------:|-------------------|----------------|
| Cardiac (LVEF %) | | | | | [Echocardiogram every X cycles] | [LVEF <X → hold/stop] |
| Renal (eGFR / creatinine) | | | | | | |
| Hepatic (LFTs) | | | | | | |
| Neurological | | | | | | |
| [Other organ — treatment specific] | | | | | | |

---

## 7. Surveillance Protocol

**Current protocol:** [Defined by oncologist / Institution — e.g. "CT 3-monthly for 2 years, then 6-monthly for 3 years; CA-125 each visit"]

| Component | Frequency | Next Due | Responsible Clinician |
|-----------|:---------:|:--------:|----------------------|
| [Imaging — modality] | [3-monthly / 6-monthly / Annual] | [Date] | |
| [Tumour marker(s)] | | [Date] | |
| [Clinical review] | | [Date] | |
| [Specific organ monitoring] | | [Date] | |
| [Genetic testing / family screening] | [Done / Pending / Not applicable] | | |

---

## 8. Cross-System Links

**Oncology → Haematology:** Chemotherapy causes myelosuppression — distinguish from disease-related anaemia or pre-existing haematological conditions. See `haematology.md`.

**Oncology → Liver:** Hepatotoxic chemotherapy agents (e.g. oxaliplatin, methotrexate) and tumour involvement can affect liver function. MASLD can affect drug metabolism. See `metabolic-liver.md`.

**Oncology → Hormonal:** Certain cancer treatments cause early menopause, hypogonadism, or thyroid dysfunction. These should be monitored as survivorship effects. See `hormonal-reproductive.md`.

**Oncology → Autoimmune:** Checkpoint inhibitor immunotherapy (PD-1/PD-L1 inhibitors) can trigger immune-related adverse events (irAE) including autoimmune colitis, thyroiditis, pneumonitis, and hepatitis. If applicable, autoimmune markers should be monitored during treatment. See `autoimmune-inflammatory.md`.

**Oncology → Neurological:** Platinum agents cause peripheral neuropathy; some CNS treatments affect cognition; pain medications affect neurological assessment. See `neurological.md`.

---

## 9. Open Questions

1. [Question 1 — e.g. "BRCA1/2 testing not yet done — discuss genetic referral at next appointment"]
2. [Question 2 — e.g. "Surveillance CT due DATE — confirm booking"]
3. [Question 3 — e.g. "Cardiac LVEF monitoring — last echo DATE; next due DATE per protocol"]

---

## 10. Sources

| Source | Content | Verified |
|--------|---------|---------|
| [EV-XX] `Raw Data/YYYY-MM-DD.md` | [Description] | ✅ / ⚠️ |

---

*Next update: [Trigger — e.g. "After next oncology appointment; after next scan; after next blood results; after treatment decision"]*
