# Imaging Module — Longitudinal Scan Tracking
> **Scope:** Longitudinal tracking of all imaging studies — ultrasound, MRI, CT, echocardiogram, and other modalities.
> **Category:** Core — recommended for most complex chronic patients who have had any imaging as part of their workup.
> **Always read alongside `index.md`** — this module does not repeat demographic, lifestyle, or cross-system context.
> **Raw data:** Individual scan reports are stored in `Raw Data/YYYY-MM-DD-[modality]-[region].md` using `imaging_template.md`. This module tracks longitudinal trends across those raw files.
> **Last updated:** [DATE]

---

## ⚠️ Analytical Defaults (this module)

1. **The report is the authoritative source — not the referral reason** — the radiologist's findings and impression take precedence over what the scan was ordered to look for; note unexpected findings as carefully as expected ones
2. **Comparison to prior imaging is often more valuable than a single result** — "stable," "improving," or "new finding" requires at least two data points; always note whether the radiologist had access to prior imaging when writing the report
3. **Imaging lags behind clinical changes** — structural change visible on imaging often follows functional change; a normal scan does not exclude active disease, particularly in early-stage conditions
4. **A normal result establishes a baseline — it does not exclude a condition** — review each new scan against prior scans in this module, not just against population norms; a finding within limits in isolation may be directionally significant in series; use the Watch Register (Section 4) to capture sub-threshold findings worth tracking over time
5. **Incidental findings must be tracked** — unexpected findings noted in passing on a report require follow-up; document them here and add to `index.md` Section 9 (Open Questions)
6. **Report language is probabilistic** — terms like "consistent with," "suggestive of," and "cannot exclude" indicate degrees of certainty, not confirmed diagnoses; note the language used, not just the conclusion
7. **Modality limitations matter** — ultrasound is operator-dependent and limited by body habitus; CT involves radiation; MRI has contraindications; the choice of modality affects what can and cannot be detected

---

## 1. Scan History — All Modalities

> One row per scan. Sources: `Raw Data/YYYY-MM-DD-[modality]-[region].md` files (EV-XX IDs).

| Date | Modality | Region | Key Finding | Comparison to Prior | EV Ref |
|------|:--------:|--------|------------|:------------------:|--------|
| [Date] | [US / MRI / CT / Echo / X-ray] | [Liver / Pelvis / Brain / etc.] | [1-line summary of impression] | [Stable / Improved / Worsened / No prior / Not compared] | [EV-XX] |

---

## 2. By Organ / System — Longitudinal Detail

> Add a subsection for each organ or system that has been imaged more than once. Longitudinal comparison is where imaging becomes most useful.

### 2a. [Organ/System — e.g. Liver & Upper Abdomen]

| Date | Modality | Key Findings | Impression | Change from Prior | EV Ref |
|------|:--------:|-------------|-----------|:-----------------:|--------|
| [Date] | [US] | [e.g. Mild hepatic steatosis; no focal lesions; normal biliary system] | [e.g. Mild fatty liver, unchanged] | [Stable] | [EV-XX] |

**Trajectory:** [Improving / Stable / Worsening / Insufficient data — minimum 2 scans needed]

**Notes:** [Any relevant context — e.g. "Scan conducted during period of full lifestyle optimisation — represents best-case baseline"]

---

### 2b. [Organ/System — e.g. Pelvis / Uterus]

| Date | Modality | Key Findings | Impression | Change from Prior | EV Ref |
|------|:--------:|-------------|-----------|:-----------------:|--------|
| | | | | | |

**Trajectory:**

**Notes:**

---

### 2c. [Add further subsections as needed]

---

## 3. Incidental Findings Register

> Any finding noted incidentally in a report — not the primary reason for the scan — that requires monitoring or follow-up. These are easy to lose track of across multiple reports.

| Date found | Finding | Scan type | Follow-up recommended | Action taken | Resolved? |
|-----------:|---------|:---------:|----------------------|-------------|:---------:|
| [Date] | [e.g. "Small 5mm renal cyst noted incidentally"] | [CT abdomen] | [Repeat imaging in 12 months] | [Added to index.md Section 9] | No |

---

## 4. Watch Register — Sub-Threshold Findings

> **What belongs here:** Findings from scan reports that are currently within normal limits or below the radiologist's reporting threshold — but are worth tracking longitudinally because of their direction, context, or relationship to your other conditions. These are not confirmed findings and do not belong on the ruled-out list. They sit between "normal" and "incidental finding" — in the space where early signals often live.
>
> **Distinction from Incidental Findings (Section 3):** Incidental findings are confirmed and present — they were flagged by the radiologist and require follow-up. Watch Register entries are *sub-threshold* — not flagged, not confirmed, but contextually or directionally worth monitoring.
>
> **Status progression:** Entries move through states as the longitudinal picture develops:
> `Watching` → `Escalated` (promoted to incidental finding or hypothesis) / `Closed — remains normal` (unchanged across N scans) / `Incorporated` (resolved by becoming a confirmed finding or ruled-out cause)

| Date first noted | Observation | Source scan | Why worth watching | Next check trigger | Status |
|-----------------:|------------|:-----------:|-------------------|-------------------|:------:|
| [Date] | [Verbatim or paraphrased from report — e.g. "Liver echotexture mildly coarser than prior scan; within normal limits"] | [EV-XX] | [e.g. "Directional change across two scans; consistent with early steatosis trajectory even though not yet reported as fatty liver"] | [e.g. "Review against next liver ultrasound; escalate if trend continues"] | Watching |
| [Date] | [e.g. "4mm nodule right lobe — too small to characterise, likely benign; follow-up recommended in 12 months"] | [EV-XX] | [e.g. "Radiologist recommended follow-up — not yet confirmed but requires active tracking"] | [e.g. "Repeat ultrasound DATE"] | Watching |

**Review rule:** Revisit every Watch Register entry when a new scan of the same region is added. Ask: has this observation changed, resolved, or become more significant? Update the status accordingly. A finding that remains unchanged across 3+ scans with no relevant symptom change can be moved to `Closed`.

---

## 5. Scheduled / Outstanding Scans

| Scan | Reason | Due | Ordered by | Status |
|------|--------|:---:|:----------:|--------|
| [e.g. Liver ultrasound — 6-monthly monitoring] | [MASLD surveillance] | [Date] | [Gastroenterologist] | [Booked / Not yet booked] |
| [FibroScan] | [Fibrosis staging before pharmacological treatment] | [When arranged] | | [Pending referral] |

---

## 6. Cross-System Links

**Imaging → Active Conditions:** Scan findings are a primary source of evidence for condition status in `index.md` Section 3. When a scan shows change (improvement, worsening, new finding), update the relevant active condition summary and hypothesis register.

**Imaging → Hypothesis Register:** Structural findings on imaging can confirm or challenge working hypotheses. A fatty liver confirmed on ultrasound supports the hepatic triglyceride clearance hypothesis. A normal pelvic scan would challenge an adenomyosis hypothesis. Always cross-reference with `index.md` Section 2c.

**Imaging → Haematology:** Liver imaging findings inform interpretation of haematological markers — fatty liver supports the hepatic mechanism for sub-baseline Transferrin and MCV shifts. See `core/haematology.md`.

**Imaging → Specialist Coordination:** Scan reports are generated by radiologists and sent to the referring clinician. They are not automatically shared between specialists. If a gastroenterologist orders a liver ultrasound, the gynaecologist does not automatically receive the result. Carry the report and EV reference to any appointment where it is relevant.

**Imaging gap — raw images:** Actual scan images are not stored in this framework at this stage. See `imaging_template.md` for the known gap documentation and optional image file path field.

---

## 7. Open Questions

1. [Question 1 — e.g. "Next liver ultrasound due DATE — book with gastroenterologist"]
2. [Question 2 — e.g. "FibroScan not yet done — needed before pharmacological treatment eligibility"]
3. [Incidental finding follow-up — e.g. "Renal cyst noted DATE — repeat imaging due DATE"]

---

## 8. Sources

| Source | Content | Verified |
|--------|---------|---------|
| [EV-XX] `Raw Data/YYYY-MM-DD-[modality]-[region].md` | [Description] | ✅ / ⚠️ |

---

*Next update: [Trigger — e.g. "After next scheduled scan; after FibroScan; after any new imaging"]*
