# Blood Test Entry Template
> **Usage:** Copy this file for each blood draw. Save as `Raw Data/YYYY-MM-DD.md`. Assign an EV-XX ID and add to the Evidence Registry in `index.md`.
> **Before writing:** Read `Raw Data/blood-tests-metadata.md` for structural rules (data states, what never goes in a source file). Look up every marker in `Raw Data/blood-tests-marker-manifest.md` before entering it — add new markers to the manifest first if they are not already there.
> One file per draw date. If multiple panels were drawn on different dates on the same day (e.g. main draw + iron studies separately), note each draw in the same file with distinct timing.

---

## File Header

```
EV ID:       EV-XX              ← Assign next available ID; register in index.md Section 11
Lab ref:     [Lab reference number from the printout]
Draw date:   YYYY-MM-DD
Draw time:   HH:MM (if known)
Lab:         [Lab name — affects reference ranges; note if different from usual]
Fasting:     Yes / No / Unknown
  └─ If non-fasting: approx. [X] hours since last meal
Circumstances: [e.g. routine 6-monthly monitoring / acute investigation / GP-requested / self-requested]
Supplements / medications at time of draw:
  - [List all — especially B12, folate, iron, hormones, biotin, statins, immunosuppressants]
  - None
Stress level at draw: [Low / Moderate / High — and brief note if relevant]
Other context: [e.g. recovering from illness, mid-cycle, day 2 of period, post-infusion, etc.]
```

---

## Results

> **Format:** [Marker]: [Value] [Unit] [ref range] [flag]
> **Flags (lab range):** ✅ within range | ⚠️H above range | ⚠️L below range
> **Personal baseline comparison:** captured in `pb_delta` in the CSV block below — do not encode in narrative flags

### [Panel Name — e.g. Liver Function]

- [Marker]: [Value] [Unit] [ref: X–Y] [flag]
- [Marker]: [Value] [Unit] [ref: X–Y] [flag]

### [Panel Name — e.g. Haematology / Full Blood Count]

- [Marker]: [Value] [Unit] [ref: X–Y] [flag]

### [Panel Name — e.g. Iron Studies]

- [Marker]: [Value] [Unit] [ref: X–Y] [flag]

### [Panel Name — e.g. Lipids]

- [Marker]: [Value] [Unit] [ref: X–Y] [flag]

### [Panel Name — e.g. Thyroid]

- [Marker]: [Value] [Unit] [ref: X–Y] [flag]

### [Panel Name — e.g. Vitamins / Nutritional]

- [Marker]: [Value] [Unit] [ref: X–Y] [flag]

### [Panel Name — e.g. Metabolic / General Chemistry]

- [Marker]: [Value] [Unit] [ref: X–Y] [flag]

### [Panel Name — e.g. Autoimmune / Immunology]

- [Marker]: [Value] [Unit] [ref: X–Y] [flag]

### [Panel Name — e.g. Tumour Markers]

- [Marker]: [Value] [Unit] [ref: X–Y] [flag]

---

## Lab Comments

> Copy any interpretive comments printed on the lab report verbatim — these often contain clinically relevant context.

- [Lab comment 1]
- [Lab comment 2]
- *None printed*

---

## Notable Results Summary

> Fill this section after reviewing results. 2–5 bullet points on what matters — use as a quick reference.

- [Most notable finding — e.g. "Transferrin Saturation 17%L — below reference range; iron deficiency re-emerging"]
- [Second notable finding]
- [Third, if applicable]
- [Any result flagged by the lab or clinician]

---

## Index.md Update Required?

- [ ] New result changes Section 2a (confirmed facts) → add FACT-XX
- [ ] New result changes Section 2c (hypothesis confidence) → update with date and reasoning
- [ ] New result changes Section 3 (active condition summary)
- [ ] Add to Section 6 rolling window (CURRENT block)
- [ ] Update Section 7 (pending results) — mark received
- [ ] Update Section 9 (open questions) — address or close any
- [ ] Module file update required → [which module?]

---

## Calculation Protocol

> **When to run:** After completing the Results section above. Before filling the CSV block below.
> **Purpose:** Compute `pb_delta` for every marker. Store the result once — do not re-derive it in future analysis conversations.

**Formula:**
```
pb_delta = (value − baseline) / baseline × 100
```
- Round to 1 decimal place
- Sign is mandatory: use + for above baseline, − for below
- Do not include the % symbol in the CSV column (the column name implies it)

**Reference point:** Read `baseline` from Section 1 of the relevant module file (e.g. `haematology.md` §1, `metabolic-liver.md` §1). Do not estimate or recall from memory.

**Sentinel values — use these instead of leaving pb_delta blank:**

| Value | Meaning | When to use |
|-------|---------|-------------|
| `NE` | Not Established | Baseline concept applies but no baseline has been set yet for this marker. Flag in Notable Results. |
| `NA` | Not Applicable | Baseline concept does not apply — qualitative markers (e.g. ANA positive/negative), one-off diagnostics, or markers where only population range is meaningful. |

---

## Raw CSV Data Layer

> **Do not edit this block manually after generation.**
> **When to fill:** After completing the Calculation Protocol above.
> **Column definitions:**
> - `date` — draw date (YYYY-MM-DD)
> - `marker` — canonical name from `blood-tests-marker-manifest.md`
> - `value` — numeric result as reported by lab
> - `unit` — unit as reported by lab
> - `ref_low` / `ref_high` — lab reference range bounds (numeric only; leave blank if range is one-sided or not provided)
> - `flag` — lab range flag only: `OK`, `H` (above range), `L` (below range)
> - `pb_delta` — computed per Calculation Protocol above; use `NE` or `NA` where applicable

```csv
date,marker,value,unit,ref_low,ref_high,flag,pb_delta
YYYY-MM-DD,[Marker],[Value],[Unit],[ref_low],[ref_high],[OK/H/L],[pb_delta or NE or NA]
YYYY-MM-DD,[Marker],[Value],[Unit],[ref_low],[ref_high],[OK/H/L],[pb_delta or NE or NA]
```

---

## Verification Status

- **Verified against printout:** Yes / No / Partial
- **Printout on file:** Yes / No
- **Notes:** [Any discrepancies between digital results and printout; or confirmation they match]
