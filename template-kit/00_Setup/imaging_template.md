# Imaging Report Entry Template
> **Usage:** Copy this file for each imaging study. Save as `Raw Data/YYYY-MM-DD-[modality]-[region].md` (e.g. `Raw Data/2026-05-13-ultrasound-liver.md`). Assign an EV-XX ID and add to the Evidence Registry in `index.md`.
> **Before writing:** Check `Raw Data/blood-tests-metadata.md` Section 8 for rules on what never goes in a source file — the same principles apply here. Source files contain what the report says, not your interpretation of it.
> **Scope:** Reports only. Storing actual scan images is flagged as a known future capability gap — the report contains the expert interpretation and is sufficient for the current framework.

---

## File Header

```
EV ID:          EV-XX              ← Assign next available ID; register in index.md Section 11
Modality:       [Ultrasound / MRI / CT / CT with contrast / PET-CT / Echocardiogram / X-ray / Other]
Region / organ: [e.g. Liver and upper abdomen / Pelvis / Brain / Chest / Heart]
Scan date:      YYYY-MM-DD
Report date:    YYYY-MM-DD (if different from scan date)
Facility:       [Imaging centre / Hospital]
Radiologist:    [Name if printed on report]
Referring clinician: [GP / Specialist — who ordered the scan]
Clinical indication: [Reason for scan as stated on the request — copy verbatim if printed]
Fasting:        [Yes / No / Not required / Unknown]
Contrast used:  [Yes — type / No / Not applicable]
```

---

## Report — Full Transcription

> Transcribe the report verbatim from the printed or digital document. Do not summarise, paraphrase, or omit sections. If a section is illegible or missing, note it explicitly.

### Clinical History (as printed on report)
[Transcribe verbatim]

### Technique
[Transcribe verbatim — e.g. "B-mode and Doppler ultrasound of the liver, biliary system, and upper abdomen performed"]

### Findings
[Transcribe verbatim — this is the most important section]

### Impression / Conclusion
[Transcribe verbatim]

### Recommendation (if printed)
[Transcribe verbatim — e.g. "Follow-up ultrasound in 6 months recommended"]

---

## Key Findings Summary

> Fill after transcription. 2–4 bullet points on what the report found that is most clinically relevant. This is a summary for quick reference — the full transcription above is the source of truth.

- [Most notable finding — e.g. "Mild hepatic steatosis (fatty liver) confirmed — grade 1/3"]
- [Second notable finding — e.g. "No focal lesions identified"]
- [Comparison to prior imaging if noted in report — e.g. "Stable compared to prior study DATE"]
- [Any follow-up recommendation]

---

## Comparison to Prior Imaging

> Note the last scan of this type and whether this report explicitly compares to it.

| Prior scan | Date | Comparison noted in report | Change |
|-----------|------|--------------------------|--------|
| [Modality + region] | [Date] | Yes — [summary] / No / Not available | [Improved / Stable / Worsened / New finding] |

---

## Index.md Update Required?

- [ ] Add to Evidence Registry (Section 11) with EV-XX ID
- [ ] Update Section 6 (Recent Results) if this scan is part of routine monitoring
- [ ] Update Section 3 (Active Conditions) if findings change condition status
- [ ] Update Section 2c (Hypothesis Register) if findings support or challenge a hypothesis
- [ ] Update Section 9 (Open Questions) — close any question this scan resolves; add any it generates
- [ ] Update `modules/core/imaging.md` longitudinal table

---

## Verification Status

- **Verified against report:** Yes / No
- **Report on file:** Yes / No — [format: printed / PDF / MyHealth Record]
- **Notes:** [Any discrepancy between digital report and printed version; or confirmation they match]

---

## Known Gap — Scan Images

The actual scan images (DICOM, JPEG, or PDF export) are not stored in this framework at this stage. The report contains the radiologist's expert interpretation and is sufficient for longitudinal tracking and clinical communication purposes. Storing raw images for AI-assisted interpretation is a planned future extension.

If you wish to retain images, store them in a separate folder (e.g. `Raw Data/images/YYYY-MM-DD-[modality].jpg`) and note the file path here:

**Image file path:** [Path or "not stored"]
