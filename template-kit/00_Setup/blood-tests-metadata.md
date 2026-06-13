# Blood Test Source Files — Metadata & Design Rules
> **Purpose:** Defines the conventions, data states, and structural rules for all files in `03_Patient_Records/transcribed/`. Apply consistently across every source file.
> **How to use:** Read this file once before creating your first blood test file. Refer back whenever a new situation arises — the data states and exclusion rules in particular.
> **Personalise:** Sections marked `[personalise]` need your lab-specific details. Everything else is universal.
> **Last updated:** [DATE — update when you add a rule or resolve an edge case]

---

## 1. What These Files Are

Each file in `03_Patient_Records/transcribed/` is a **source file** — the single source of truth for raw lab results on a given date. They are:

- Stable once verified against the original lab printout
- Never edited retrospectively based on new interpretation
- The foundation that all module files and `index.md` reference — never the other way around

The data flows in one direction only: **lab printout → source file → module files → index.md**. Reversing this (e.g. copying a value from `index.md` into a source file) is an architectural violation. See Section 8.

---

## 2. File Naming

```
YYYY-MM-DD.md
```

One file per test date. If multiple panels were drawn on the same calendar date (e.g. a main blood draw and a separate iron studies draw), consolidate into one file — do not split by panel. Record each panel's lab reference and collection time separately within the file.

---

## 3. Cross-File Identifier

`[personalise]` — fill in the identifier system your lab uses.

**The unique key across files is the test date (YYYY-MM-DD).** There is one patient in this system — date alone is sufficient to uniquely identify any source file.

Within a single date, lab reference numbers are useful for matching which panels belong to the same request, but they vary by lab and cannot be used as cross-file keys.

| Field | Role | Scope |
|-------|------|-------|
| Test date | Unique file identifier | Cross-file |
| Lab Reference | Cross-panel matching within a date | Within date only |
| Patient Reference / Lab Patient ID | Cross-panel matching within a date | Within date only |

`[personalise]` — note your lab's identifier format here:
- **Your lab:** [Lab name]
- **Patient reference format:** [e.g. "Your Reference: 00170499" — appears on every panel from this lab]
- **Lab reference format:** [e.g. "Lab Ref: P456741" — one per panel request]
- **Other labs used:** [List additional labs and their identifier formats if you use more than one]

> **Note:** Different labs use different identifier systems. Always record whichever identifiers appear on the printout — but never use them as cross-file keys.

---

## 4. Data States

Four explicit states cover every possible condition for a marker on a given date. **Never leave a cell blank or use a dash** — always use one of these states. Ambiguity in source files propagates into module files and undermines auditability.

| State | Meaning | When to use |
|-------|---------|-------------|
| *(value)* | Confirmed result | Verified against original printout |
| `not tested` | Confirmed not requested | Use only after all printouts for this date are loaded and the marker is confirmed absent from all panels |
| `not resulted` | Test requested but no value produced | Lab did not return a value despite the test being on the request |
| `unknown — printout not yet uploaded` | Printout exists but not yet reviewed | Temporary build state — must be resolved before file is marked complete |
| `not confirmed — source printout missing` | Printout cannot be located | Permanent state — value is unverifiable; do not infer or carry forward |

> `not printed` (ref range column only): Use in the Ref Range column when a result value exists but the lab did not print a reference range for it on that report.

### 4a. Standing vs Conditional Sections

Some panels appear in every file as stubs even when not tested; others are included only when tested.

| Panel | Rule |
|-------|------|
| General Chemistry | Standing — stub with `not tested` if absent |
| Liver Function | Standing — stub with `not tested` if absent |
| Lipids | Standing — stub with `not tested` if absent |
| Haematology | Standing — stub with `not tested` if absent |
| Thyroid | Standing — stub with `not tested` if absent |
| Iron Studies | Standing — stub with `not tested` if absent |
| B12 / Folate | Standing — stub with `not tested` if absent |
| Tumour Markers | Standing — stub with `not tested` if absent |
| Autoimmune / Immunology | Conditional — include only when tested |
| Viral serology (Hep A/B/C, CMV, EBV, etc.) | Conditional — include only when tested |
| Coagulation | Conditional — include only when tested |
| Any one-off or specialist panel | Conditional — include only when tested |

`[personalise]` — adjust the standing/conditional split based on which panels you are routinely monitored for. Add rows as new panels are introduced.

> **Resolution rule:** All `unknown — printout not yet uploaded` entries must be resolved to one of the other states before the file's verification status is marked complete.

---

## 5. Marker Naming

- Use **expanded full name followed by abbreviation in parentheses** — format: `Expanded Name (Abbreviation)` — e.g. `Haemoglobin (Hb)`, `Red Cell Count (RCC)`
- This ensures readability for both clinical and non-clinical readers
- Names must be **consistent across all dates** — once a canonical name is established in the marker manifest (`blood-tests-marker-manifest.md`), use it on all subsequent files regardless of how the lab abbreviates it on that printout
- Where the lab uses multiple abbreviations for the same marker across printouts, always use the canonical name from the manifest — note lab variants in the manifest's "Also Appears As" column
- **Exception — qualitative markers:** Where a marker name includes its result descriptor as part of the lab's label (e.g. `ANA — Speckled`), record exactly as printed
- **Before writing a new marker into a date file:** Look it up in the marker manifest first. If it is not there, stop and add it to the manifest before proceeding — do not invent a name independently in a date file

---

## 6. Timestamps & Fasting Status

- **Always record collection time** — timestamp is clinically meaningful (morning vs afternoon affects cortisol, glucose, some lipids)
- **Fasting status** — confirmed by patient; never inferred from timestamp alone
- If multiple panels on the same date have different collection times, record the time per panel in the panel header table
- **Non-fasting notation:** Record as "Non-fasting — approx. [X] hours since last meal" where known. Triglycerides and glucose in particular require fasting context for interpretation.

---

## 7. File Structure

Every source file follows this structure:

### Header block
```
# Blood Test — DD Month YYYY
[Patient Reference field from your lab — e.g. "Your Reference: XXXXXXXX"]
Fasting: [Yes / No / Unknown]
Context: [One-line factual note — e.g. "Routine 6-monthly monitoring" or "Acute liver inflammation — GP-requested"]
EV ID: EV-XX  ← assign and register in index.md Evidence Registry before writing

## Panels on this date & lab references
| Panel | Lab Ref | Collected | Reported |
|-------|---------|-----------|----------|
| [Panel name] | [Lab ref] | [Date, time] | [Date] |
```

### Themes block
```
## Themes tested this visit
- [Theme name] ✅ verified against printout
- [Theme name] unknown — printout not yet uploaded

## Themes not tested this visit
- [Theme name] — confirmed not tested
```

Theme labels use the **lab's own category names** as printed on the request form (e.g. Haematology, Liver Function, Lipids, General Chemistry, Thyroid, Iron Studies). These are factual categorisations, not interpretive labels.

### Data sections
One `##` section per theme tested. Format: markdown table, one marker per row.

```
## [Theme Name]
*Lab ref: [ref] | Verified against printout ✅*
(or: *unknown — printout not yet uploaded*)

| Marker | Value | Unit | Ref Range | Flag |
|--------|-------|------|-----------|------|
| [Canonical Name (Abbrev)] | [value or data state] | [unit] | [ref range or "not printed"] | [✅ / ⚠️H / ⚠️L / —] |
```

**Flag key:**
- `✅` — within reference range
- `⚠️H` — above upper limit
- `⚠️L` — below lower limit
- `—` — not applicable (qualitative result, or a data state rather than a numeric value)

### Lab interpretive comments
```
### Lab interpretive comments
*Standard explanatory text printed on this report by the laboratory.
Transcribed verbatim — not a clinical finding or personal recommendation.*

[Comments transcribed here]
```

Include only when the lab printout contains printed interpretive text. Transcribe verbatim. Do not add comments from memory, external sources, or your own interpretation.

### Verification status block
```
## Verification status
- [x] [Theme] — verified against printout ✅
- [ ] [Theme] — printout not yet uploaded
- [ ] [Theme] — source printout missing
```

This block tracks build state. Once all items are checked, the file is complete.

---

## 8. What Never Goes in a Source File

| Excluded content | Where it belongs instead |
|-----------------|--------------------------|
| Clinical interpretation of any result | Module files (`haematology.md`, `liver.md`, etc.) |
| Cross-system significance or flags | Module files and hypothesis register in `index.md` |
| Values sourced from `index.md` or any module file | Nowhere — source files only accept values from lab printouts |
| Values carried forward from another date's file | Never — each file contains only what was measured on that date |
| GP notes, referral notes, or clinical notes from the printout header | Not recorded anywhere in the wiki |
| Handwritten annotations on printouts | Not recorded unless confirmed as official lab results |
| Your own annotations or memory of what a result "probably was" | Not recorded |

> **Alert rule:** If a value in a source file cannot be traced to a lab printout for that date, it must not be entered. Sourcing from `index.md` or a module file is an architectural violation — flag immediately and remove.

---

## 9. Source File Integrity Rule

Source files are **stable once verified**. After a section is marked verified against its printout:

- Values are not changed
- New interpretation is not added
- Cross-system linkages discovered later are not back-filled

If a genuine error is found in a verified section (e.g. a transcription mistake), correct it, note the correction with date and reason in the verification status block, and update the relevant module file if the error affected a longitudinal table.

---

## 10. Expansion Notes

Add any edge cases or new rules here as your wiki grows. Date each addition.

| Date | Rule added | Reason |
|------|-----------|--------|
| [DATE] | [Rule] | [Why it was needed] |

---

*Apply these rules to every file in `03_Patient_Records/transcribed/`. When in doubt, refer back to Section 8.*
