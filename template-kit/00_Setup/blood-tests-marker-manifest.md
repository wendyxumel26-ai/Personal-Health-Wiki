# Blood Tests — Marker Manifest
> **Purpose:** Canonical reference for every marker that appears across any `03_Patient_Records/transcribed/` date file. All date files use names from this manifest — naming decisions are never made independently in a date file.
> **How to build:** Start empty. Add markers as you enter each blood test file, following the process in Section 2. The manifest grows with your data.
> **Scope:** Only markers verified against an original lab printout. Values from `index.md` or module files are excluded.
> **Lab context:** `[personalise — your primary lab name(s)]`
> **Last updated:** [DATE]

---

## 1. Why This File Exists

Labs print the same blood marker with different names and abbreviations. "WCC" on one printout is "WBC" on another. "Hb" and "HGB" are the same thing. Without a canonical naming dictionary, longitudinal tables in your module files silently acquire inconsistencies that make trend analysis unreliable.

This manifest is the single authority on what each marker is called in this wiki. Once a canonical name is established here, it never changes — regardless of how future labs print it.

---

## 2. How to Use This File

### When writing a new date file:
1. Read the lab printout — identify every marker as printed
2. Look up each marker in the manifest tables below
3. **Match found** → use the canonical name from Column 1 exactly; if the lab's printed variant is not yet listed in "Also Appears As", add it now
4. **No match found** → **stop; do not invent a name** — add the new marker here first (see Section 3), then write the date file
5. If you are unsure whether a new marker is genuinely new or a variant of an existing one, add it to the "Unresolved" section at the bottom and resolve before writing the date file

### When updating an existing marker entry:
- Add new "Also Appears As" variants as you encounter them — never change the canonical name
- Add a row to the Expansion Log (Section 5) noting the date and reason

---

## 3. How to Add a New Marker

1. Confirm the marker name from the lab printout
2. Search the manifest — is this a variant of something already listed?
   - If yes: add the variant to "Also Appears As" only
   - If no: add a new row with: Canonical Name, Abbreviation (if standard), Type (Measured/Calculated), "Also Appears As" (the lab's printed version), Panel, First Seen date
3. Add to Expansion Log (Section 5)
4. Then proceed to the date file

> **Rule:** A marker enters the manifest only when verified against a lab printout. Do not add markers from memory, from `index.md`, or from module files.

---

## 4. Manifest

> **How to read the table:**
> - **Canonical Name** — the name used in every date file and module file in this wiki
> - **Abbrev** — standard abbreviation (blank if none or if the full name is already short)
> - **Type** — Measured (direct lab measurement) or Calculated (derived from other values)
> - **Also Appears As** — all lab-printed variants seen so far; add new ones as encountered
> - **Panel** — the panel category this marker appears under on lab printouts
> - **First Seen** — date file where this marker first appeared (verified)

---

### Haematology

| Canonical Name | Abbrev | Type | Also Appears As | Panel | First Seen |
|----------------|--------|------|-----------------|-------|------------|
| | | | | Haematology | |

---

### General Chemistry

| Canonical Name | Abbrev | Type | Also Appears As | Panel | First Seen |
|----------------|--------|------|-----------------|-------|------------|
| | | | | General Chemistry | |

---

### Liver Function

| Canonical Name | Abbrev | Type | Also Appears As | Panel | First Seen |
|----------------|--------|------|-----------------|-------|------------|
| | | | | Liver Function | |

---

### Lipids

| Canonical Name | Abbrev | Type | Also Appears As | Panel | First Seen |
|----------------|--------|------|-----------------|-------|------------|
| | | | | Lipids | |

> **Note on LDL Cholesterol:** LDL is a calculated value. If the lab states which formula was used on the printout, note it here. Formula changes affect comparability across dates — flag in the date file if the formula changes.

---

### Thyroid

| Canonical Name | Abbrev | Type | Also Appears As | Panel | First Seen |
|----------------|--------|------|-----------------|-------|------------|
| | | | | Thyroid | |

> **Note:** Free T4 and Free T3 are not always requested alongside TSH. Record as `not tested` in date files when absent from the panel.

---

### Iron Studies

| Canonical Name | Abbrev | Type | Also Appears As | Panel | First Seen |
|----------------|--------|------|-----------------|-------|------------|
| | | | | Iron Studies | |

---

### B12 / Folate

| Canonical Name | Abbrev | Type | Also Appears As | Panel | First Seen |
|----------------|--------|------|-----------------|-------|------------|
| | | | | B12 / Folate | |

> **Note on Active B12:** Active B12 (holotranscobalamin) is a more sensitive functional marker than total Vitamin B12. If your lab offers it, it is worth requesting — particularly if B12 or folate deficiency is being investigated. Record as a separate row from total B12.

---

### Autoimmune / Immunology

| Canonical Name | Abbrev | Type | Also Appears As | Panel | First Seen |
|----------------|--------|------|-----------------|-------|------------|
| | | | | Autoimmune | |

> **ANA recording rule:** ANA results include both a titre and a pattern (e.g. Speckled, Homogeneous, Centromere). Record the pattern as part of the marker name — e.g. `ANA — Speckled` — with titre as the value. Do not split into separate rows.

---

### Hormonal

| Canonical Name | Abbrev | Type | Also Appears As | Panel | First Seen |
|----------------|--------|------|-----------------|-------|------------|
| | | | | Hormonal | |

> **Note on cycle-dependent markers:** FSH, LH, oestradiol, and progesterone are cycle-dependent. Always record the cycle day (or "unknown") in the date file alongside the result.

---

### Viral Serology

| Canonical Name | Abbrev | Type | Also Appears As | Panel | First Seen |
|----------------|--------|------|-----------------|-------|------------|
| | | | | Viral Serology | |

---

### Coagulation

| Canonical Name | Abbrev | Type | Also Appears As | Panel | First Seen |
|----------------|--------|------|-----------------|-------|------------|
| | | | | Coagulation | |

---

### Tumour Markers

| Canonical Name | Abbrev | Type | Also Appears As | Panel | First Seen |
|----------------|--------|------|-----------------|-------|------------|
| | | | | Tumour Markers | |

---

### Other / One-Off Panels

> Add additional panel sections here as they arise. Use the same table format. Add the panel name as a heading.

---

### Unresolved

> Markers encountered on a printout that have not yet been confirmed as new or as variants of existing markers. Resolve before writing them into a date file.

| Lab-printed name | Seen on | Probable match | Status |
|-----------------|---------|---------------|--------|
| | | | |

---

## 5. Manifest Statistics

> Update these counts when adding markers.

- **Total verified markers:** 0
- **Provisional entries (unverified printout):** 0
- **Panels with unconfirmed markers:** 0
- **Date files sourced from:** *(none yet)*

---

## 6. Expansion Log

| Date | Change | Reason |
|------|--------|--------|
| [DATE] | Initial file created | [Your starting point — e.g. "First blood test file being built"] |

---

## 7. Lab-Specific Notes

> `[personalise]` — use this section to record anything specific to your lab(s) that affects marker naming or interpretation.

| Lab | Note |
|-----|------|
| [Lab name] | [e.g. "Uses WBC instead of WCC"; "Prints LDL formula on every report"; "Reference ranges differ from Lab X"] |
