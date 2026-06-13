# Audit Prompt — Health Wiki Integrity Check
> **Usage:** Run this prompt against your `index.md` (and optionally your module files) at least monthly, or after any significant update to the wiki.
> **Purpose:** Detect reasoning drift, hypothesis violations, and knowledge hygiene issues before they accumulate.
> **How to use:** Paste this prompt into a new Claude conversation, followed by your `index.md` content (and any module files you want audited).

---

## Standard Audit Prompt

> Copy everything below this line and paste it into Claude, then paste your `index.md` content (and module files if desired) after it. For Step 0, also paste the contents of any source files you want to verify (blood test files, imaging report files).

---

Act as a clinical knowledge auditor reviewing a personal health wiki. Your job is to identify reasoning drift, violated facts, stale hypotheses, structural hygiene issues, and data layer integrity problems. Be specific, direct, and non-diplomatic — the value of this audit is in catching problems, not reassuring the author.

**Step 0 — Data layer integrity (source files)**

> Run this step when you have source files available (blood test files, imaging report files). It operates at the data layer — below the reasoning layer checked in Steps 1–7. Skip if source files are not included in this audit session.

For every source file provided:

1. **EV-XX header check (forward):** Read the EV-XX ID from the file header. Confirm it is present in the Evidence Registry (Section 11 of `index.md`). Flag any source file whose EV-XX ID does not appear in the registry — the file exists but is unregistered.

2. **EV-XX registry check (reverse):** For every entry in the Evidence Registry, confirm a corresponding source file exists with that EV-XX ID in its header. Flag any registry entry with no matching source file — the registry references something that cannot be verified.

3. **File header completeness:**
   - Blood test files: confirm fasting/non-fasting is documented; confirm supplement and medication status at time of draw is noted; confirm EV-XX ID is present.
   - Imaging report files: confirm modality, region, scan date, referring clinician, and EV-XX ID are present; confirm fasting/contrast status is noted where applicable.
   - Flag any header field left blank or marked "unknown" without a reason.

4. **Architectural violation check:** Scan each source file for values or interpretations that appear to have been sourced from `index.md` or a module file rather than a lab printout or imaging report. Signs to look for: rounded values where lab printouts typically show decimals; interpretive language ("consistent with hepatic impairment") in a section that should contain only raw data; values that exactly match what appears in `index.md` but were not separately transcribed. Flag any suspected violations — these are data integrity errors.

5. **Watch Register currency (imaging files only):** If an imaging report file has been added since the last audit, confirm that the Watch Register in `core/imaging.md` has been reviewed against the new scan — that existing "Watching" entries for the same organ/region have been updated, and that any sub-threshold findings from the new report have been assessed for inclusion.

Report all issues with the specific EV-XX IDs and file names involved.

> **PII note:** This audit does not scan for PII in source files — that is handled by the `00_Setup/utilities/scan_for_pii.py` script, which should be run after any bulk import. If during this audit you notice a field in a source file that looks structurally out of place for a clinical record (a name, ID number, or contact field), flag it for the user to investigate with the script.

---

**Step 1 — Provenance tag audit (hypothesis integrity)**

For every hypothesis in the Hypothesis Register (Section 2c), do the following:

1. Read the `[Trace: HYP-XX <- EV-XX, EV-XX | Exclude: FACT-XX | Date: YYYY-MM-DD]` tag
2. Confirm each listed EV-XX is present in the Evidence Registry (Section 11)
3. For every `Exclude: FACT-XX` listed, confirm that the hypothesis does not contradict that fact
4. Flag any hypothesis where:
   - A listed EV-XX is missing from the Evidence Registry
   - The hypothesis, if true, would contradict one of its listed Exclude facts
   - The hypothesis has not been updated in more than 6 months (Date field)
   - No Exclude facts are listed (every hypothesis should have at least one)

Report any violations with the specific IDs involved.

**Step 2 — Fact register audit**

For every confirmed fact in Section 2a:
1. Confirm it has a [Source: EV-XX | Confirmed: DATE] tag
2. Confirm the EV-XX source is in the Evidence Registry
3. Flag any fact that lacks a source tag or has an unlisted EV-XX
4. Flag any fact that appears to contradict information elsewhere in the document

**Step 3 — Ruled-out register check**

Review Section 8 (What Has Been Ruled Out).
1. Identify any cause or condition listed in Section 8 that is also being suggested or held open as a hypothesis in Section 2c
2. Identify any cause or condition that appears to be implicitly under consideration elsewhere in the document but is not listed in Section 8
3. Flag any ruled-out item that lacks a method of exclusion (i.e. "how ruled out" is blank or vague)

**Step 4 — Stale items**

1. **Hypotheses:** Flag any hypothesis not updated in more than 6 months where new data has arrived that should have prompted a review
2. **Research files:** If research file dates are listed in any module, flag any older than 18 months in an active clinical field
3. **Pending results:** Flag any item in Section 7 that has been "pending" for more than 3 months without a noted reason for delay
4. **Open questions:** Flag any item in Section 9 that has no associated action and no noted timeline

**Step 5 — Cross-system consistency**

1. Identify any finding described in a module file that is not reflected in the corresponding section of `index.md`
2. Identify any active condition in Section 3 that does not have a matching open question in Section 9 or a completed treatment entry
3. Flag any cross-system link that is described in one module but not acknowledged in the linked module

4. **Cross-module link interpretation check:** For every "Cross-System Links" section in any loaded module, verify that the relationship is acknowledged in the linked module AND that the interpretations are directionally compatible. A link declared in one module that is absent or contradicted in the other is a logic integrity failure. If the linked module is not included in this audit session, flag it as unverifiable and recommend it be included in the next session.

5. **Interpretation conflict detection:** Identify any physiological finding or marker that appears in more than one loaded module and carries an interpretation in each. For every such shared finding:
   - If the interpretations are compatible (complementary mechanisms, different angles on the same cause) → no flag needed
   - If the interpretations differ in causal attribution (e.g. elevated ALT interpreted as metabolic/structural in one module and immune-mediated in another) → flag unless a HYP-XX entry in `index.md` Section 2c explicitly acknowledges the competing explanations and links them via trace tags
   - A divergence that is not registered in the Hypothesis Register is uncontrolled drift — flag as Critical

   Known shared marker pairs to check specifically (adjust for which modules are loaded):
   - ALT / AST / GGT: `metabolic-liver.md` ↔ `autoimmune-inflammatory.md`
   - Ferritin: `haematology.md` ↔ `autoimmune-inflammatory.md`
   - B12 / Active B12 / Folate: `haematology.md` ↔ `neurological-primary.md` or `neurological-systemic.md`
   - TSH / Free T4: `hormonal-reproductive.md` ↔ `neurological-primary.md` or `neurological-systemic.md`
   - CRP: `autoimmune-inflammatory.md` ↔ any condition module that tracks inflammatory markers

**Step 6 — Structural completeness**

Check for the following structural issues:
- Any section of `index.md` that is still blank or contains only template placeholder text (`[to fill]`, `[DATE]`, `[bracketed prompts]`)
- Any blood result in Section 6 that is missing a fasting/non-fasting notation
- Any blood result in Section 6 that is missing an EV-XX reference
- The Evidence Registry in Section 11 — flag any EV-XX referenced in the document that does not appear in the registry

**Step 7 — Summary**

Produce a prioritised list of issues found:

**Critical (must fix before next clinical conversation):**
- [Issue — specific IDs and location]

**Important (fix at next wiki update):**
- [Issue]

**Minor (housekeeping):**
- [Issue]

**No issues found in:** [List any steps where no issues were found]

---

## Extended Audit: After Major Health Events

Use this addition after a significant new event (new diagnosis, major test result, treatment decision, or specialist appointment):

> Additionally: For every section of `index.md`, confirm whether the new event requires an update to that section. For each section that should have been updated, confirm it has been. Flag any section that appears to lag the new information.

---

## Rapid Check: After Each New Blood Result

Use this lightweight version after adding a new blood test file:

> Review the most recently added blood test result in the Evidence Registry. Confirm: (1) the result has been added to Section 6 rolling window; (2) any new findings have been reflected in the relevant module file; (3) any hypothesis confidence that should change given the result has been updated in Section 2c with a date; (4) any open question in Section 9 that the result resolves or generates has been updated; (5) the EV-XX ID is registered in the Evidence Registry; (6) the file header is complete — fasting status, supplement status, and collection conditions are all documented. Report any gaps.

---

## Rapid Check: After Each New Imaging Report

Use this lightweight version after adding a new scan report file:

> Review the most recently added imaging report in the Evidence Registry. Confirm: (1) the EV-XX ID is registered in the Evidence Registry with the correct source file path; (2) the scan has been added to Section 1 (Scan History) of `core/imaging.md`; (3) the relevant organ/system subsection in Section 2 has been updated with the new scan row and trajectory reassessed; (4) any finding from the new report that meets the Watch Register criteria (sub-threshold but worth tracking) has been assessed — either added to Section 4 or explicitly noted as not warranting addition; (5) any existing Watch Register entries for the same organ/region have been reviewed against the new scan and their status updated if warranted; (6) any incidental finding noted in the report has been added to Section 3 (Incidental Findings Register) and to `index.md` Section 9 (Open Questions); (7) any finding that changes an active condition status or hypothesis confidence has been reflected in `index.md` Sections 2c and 3. Report any gaps.

---

## Audit Skills Roadmap — Planned Extensions

> **Current state (v0.1):** The prompts in this file are manually run — the user pastes them into a conversation along with relevant files. They cover the full audit surface but require deliberate action.
>
> **Planned:** Three dedicated skills that automate each audit trigger, removing the manual step and enabling the audit to read and write wiki files directly.

### Skill 1 — Conversation Wrap-Up

**Trigger:** End of any health-related conversation.
**Scope:** What happened in this conversation — decisions made, new information introduced, files that need updating.
**What it automates:** Currently, the user has to remember which files to update after a health conversation. The skill captures this automatically.

Planned outputs:
- Summary of decisions and new information from the conversation
- A structured post-conversation update checklist: which files need updating, which sections, what specifically changed
- Flag any hypothesis confidence that should change based on what was discussed
- Draft of any new open question to add to `index.md` Section 9

---

### Skill 2 — Update Audit

**Trigger:** When new data is added to the wiki — a new blood test file, imaging report, clinic note, or research file.
**Scope:** One new piece of data propagating correctly through all relevant files.
**What it automates:** The Rapid Checks above, but triggered automatically when a new source file is detected in the `Raw Data/` folder, and run across all relevant files rather than requiring manual paste.

Planned checks (extending the Rapid Checks above):
- EV-XX header registered in evidence registry
- Source file header complete
- Rolling results window updated in `index.md`
- Relevant module file updated
- Hypothesis register reviewed for impact
- Open questions updated
- Watch Register reviewed (imaging)
- Incidental findings captured (imaging)
- **Lightweight cross-module check (marker-anchored):** For the specific markers updated in this data addition, identify which other modules reference those same markers. For each, check whether the new result creates an interpretation conflict with any existing entry in those modules. Flag if a conflict exists and no HYP-XX trace links the competing explanations. Scope is narrow — only modules that share the updated markers, not a full cross-module sweep.

---

### Skill 3 — Periodic Systematic Audit

**Trigger:** Scheduled — monthly or quarterly.
**Scope:** The full wiki — all source files, all modules, index.md.
**What it automates:** The Standard Audit above, but run automatically on schedule, reading all files directly rather than requiring paste, and producing a structured report the user can act on.

Planned scope (extending the Standard Audit above):
- Full Step 0 (data layer integrity) across all source files
- Full Steps 1–7 (reasoning integrity) across index.md and all module files
- Watch Register review across all imaging entries
- Research file staleness check across all `research/` files
- Structured report with prioritised issue list and suggested fixes
- **Comprehensive cross-module sweep (Steps 5.4 and 5.5):** Full verification of all declared Cross-System Links across all loaded modules, plus interpretation conflict detection across all shared markers in all rolling window tables. This is materially more demanding than Steps 1–4 — it requires all module files to be loaded simultaneously, not just `index.md`. This requirement should be accounted for in the skill's context window budgeting and file loading strategy.

---

*These skills are planned for Phase 3 of the Health Wiki Template Kit. Phase 2 (bootstrapping skill) comes first.*
