# Australian Lab Manifest Seed Data
> **What this file is:** Starter abbreviation data for `blood-tests-marker-manifest.md`, pre-populated for common Australian pathology labs.
> **How the bootstrap skill uses it:** Read at execution time during Step 5e. The skill reads this file and uses the tables to pre-populate the user's manifest when their lab is Australian.
> **How users use it:** Reference only. If you encounter a marker abbreviation not listed here, add it to your own `blood-tests-marker-manifest.md` directly. Do not edit this seed file — it is a template-kit source.
> **Applies to:** Sullivan Nicolaides Pathology (SNP), Australian Clinical Labs (ACL), Laverty Pathology, QML Pathology, Dorevitch Pathology, Melbourne Pathology (Sonic Healthcare), SA Pathology, PathWest, NSW Health Pathology, St Vincent's Pathology.
> **Last updated:** 2026-06-07

---

## How to Read These Tables

- **Canonical Name** — the name used in every transcribed file and module file in the wiki; never changes once established
- **Abbrev** — standard short form
- **Type** — Measured (direct lab output) or Calculated (derived from other values)
- **Also Appears As** — known variants across Australian labs; add new ones to the user's manifest as encountered
- **Panel** — the panel category this marker appears under on lab printouts

When pre-populating a user's manifest, copy each table into the relevant panel section. Set the "First Seen" column to blank — it is populated when the first actual blood test file is transcribed.

---

## Haematology

| Canonical Name | Abbrev | Type | Also Appears As | Panel |
|---|---|---|---|---|
| Haemoglobin | Hb | Measured | HGB, Hgb, Hemoglobin | Haematology |
| Haematocrit | HCT | Measured | PCV, Hct, Packed Cell Volume | Haematology |
| Red Cell Count | RCC | Measured | RBC, Red Blood Cells | Haematology |
| Mean Corpuscular Volume | MCV | Measured | MCV | Haematology |
| Mean Corpuscular Haemoglobin | MCH | Measured | MCH | Haematology |
| Mean Corpuscular Haemoglobin Concentration | MCHC | Measured | MCHC | Haematology |
| Red Cell Distribution Width | RDW | Measured | RDW-CV, RDW-SD | Haematology |
| White Cell Count | WCC | Measured | WBC, WBC Total, Total White Cell Count | Haematology |
| Neutrophils | Neut | Measured | Neutrophils (Abs), Segs, PMN | Haematology |
| Lymphocytes | Lymph | Measured | Lymphocytes (Abs) | Haematology |
| Monocytes | Mono | Measured | Monocytes (Abs) | Haematology |
| Eosinophils | Eosino | Measured | Eosinophils (Abs), Eos | Haematology |
| Basophils | Baso | Measured | Basophils (Abs) | Haematology |
| Nucleated Red Blood Cells | NRBC | Measured | NRBC/100 WCC | Haematology |
| Platelets | PLT | Measured | Platelet Count | Haematology |

---

## Liver Function

| Canonical Name | Abbrev | Type | Also Appears As | Panel |
|---|---|---|---|---|
| Alanine Aminotransferase | ALT | Measured | ALAT, GPT | Liver Function |
| Aspartate Aminotransferase | AST | Measured | ASAT, GOT | Liver Function |
| Gamma-Glutamyl Transferase | GGT | Measured | γ-GT, Gamma GT, GGT | Liver Function |
| Alkaline Phosphatase | ALP | Measured | Alk Phos, Alkaline Phosphatase | Liver Function |
| Bilirubin Total | Bili | Measured | Total Bilirubin, TBili, Serum Bilirubin | Liver Function |
| Albumin | Alb | Measured | Albumin | Liver Function |
| Total Protein | TP | Measured | Protein Total, Prot | Liver Function |

---

## Iron Studies

| Canonical Name | Abbrev | Type | Also Appears As | Panel |
|---|---|---|---|---|
| Serum Iron | Iron | Measured | Fe, Iron Serum | Iron Studies |
| Transferrin | Transferrin | Measured | TIBC (note: TIBC is derived; Transferrin is direct — check printout) | Iron Studies |
| Ferritin | Ferritin | Measured | Serum Ferritin | Iron Studies |
| Transferrin Saturation | Sat | Calculated | TSAT, Fe Sat, % Saturation, Iron Saturation | Iron Studies |

---

## Lipids

| Canonical Name | Abbrev | Type | Also Appears As | Panel |
|---|---|---|---|---|
| Total Cholesterol | Chol | Measured | Cholesterol, TC | Lipids |
| Triglycerides | TG | Measured | Trig, Triglycerides | Lipids |
| HDL Cholesterol | HDLC | Measured | HDL, HDL-C, High Density Lipoprotein | Lipids |
| LDL Cholesterol | LDLC | Calculated | LDL, LDL-C, Low Density Lipoprotein | Lipids |
| Non-HDL Cholesterol | Non-HDLC | Calculated | Non-HDL, Non-HDL Chol | Lipids |
| Cholesterol/HDL Ratio | Chol/HDLC | Calculated | Chol:HDL, Chol/HDL | Lipids |

> **LDL note:** LDL is calculated. If the lab states which formula was used on the printout, note it in the manifest's lab-specific notes section. Formula changes affect longitudinal comparability.

---

## Thyroid

| Canonical Name | Abbrev | Type | Also Appears As | Panel |
|---|---|---|---|---|
| Thyroid Stimulating Hormone | TSH | Measured | TSH (Sensitive), sTSH | Thyroid |
| Free Thyroxine | Free T4 | Measured | fT4, FT4, Free T4 | Thyroid |
| Free Triiodothyronine | Free T3 | Measured | fT3, FT3, Free T3 | Thyroid |

> **Note:** Free T4 and Free T3 are not always requested alongside TSH. Record as `not tested` in transcribed files when absent from the panel.

---

## General Chemistry

| Canonical Name | Abbrev | Type | Also Appears As | Panel |
|---|---|---|---|---|
| Sodium | Na | Measured | Sodium | General Chemistry |
| Potassium | K | Measured | Potassium | General Chemistry |
| Chloride | Cl | Measured | Chloride | General Chemistry |
| Bicarbonate | TCO2 | Measured | HCO3, Bicarb, Total CO2 | General Chemistry |
| Anion Gap | AG | Calculated | Anion Gap | General Chemistry |
| Creatinine | Creat | Measured | Creatinine, Creat (Serum) | General Chemistry |
| eGFR | eGFR | Calculated | GFR (estimated), eGFR (CKD-EPI) | General Chemistry |
| Urea | Urea | Measured | BUN, Blood Urea Nitrogen | General Chemistry |
| Glucose | Glu | Measured | BSL, Blood Sugar, Blood Glucose | General Chemistry |
| Urate | Urate | Measured | Uric Acid | General Chemistry |
| C-Reactive Protein | CRP | Measured | CRP, hsCRP, hs-CRP | General Chemistry |

---

## B12 / Folate / Vitamins

| Canonical Name | Abbrev | Type | Also Appears As | Panel |
|---|---|---|---|---|
| Vitamin B12 | B12 | Measured | Vit B12, Cobalamin, Cyanocobalamin | B12 / Folate |
| Active B12 | Active B12 | Measured | Holotranscobalamin, HoloTC, Active Cobalamin | B12 / Folate |
| Serum Folate | Folate | Measured | Folic Acid, Serum Folic Acid | B12 / Folate |
| Vitamin D | Vit D | Measured | 25(OH)D, 25-OH Vitamin D, Calcidiol | B12 / Folate |

> **Active B12 note:** Holotranscobalamin is more sensitive than total B12 for functional deficiency. Record as a separate row from total B12. Not all labs offer it routinely — request specifically if B12 status is under investigation.

---

## Adding to This Seed File

If a lab abbreviation variant is found in the wild that is not listed here, add it to the relevant "Also Appears As" column and update the "Last updated" date at the top of this file. This keeps the seed data useful for future wiki setups.

Do not add new canonical marker names to this file based on memory — only add from a verified lab printout.
