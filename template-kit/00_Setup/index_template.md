# Personal Health Wiki — Master Index
> **Purpose:** Paste this document at the start of any Claude conversation to provide full health context before asking questions.
> **How to use:** Replace all `[bracketed prompts]` with your own information. Leave sections `[to fill]` if you don't have the information yet — a partial index is better than no index.
> **Framework note:** This is a personal knowledge management framework, not a medical record or clinical decision support system. It supports informed conversations with clinicians — it does not replace clinical advice or judgment.
> **Last updated:** [DATE]

---

## ⚠️ How to Use This Document

- **Always paste first** before any health question — even narrow ones
- This is a **living document** — update after every blood test, GP visit, or specialist appointment
- For deep dives, combine with the relevant module file
- Sections 1 and 2 are **always relevant** — do not omit even for narrow questions
- For update and maintenance instructions, see **Section 11**

---

## 1. Identity & Background

### Demographics
- **Age:** [age], [sex/gender]
- **Ethnicity:** [ethnicity — note if clinically relevant, e.g. for reference range interpretation or drug trial representation]
- **Location:** [city, country — relevant for healthcare system context and available treatments]
- **Clinical note on demographics:** [any known clinical implications of your demographic profile — e.g. population-specific disease phenotypes, reference range caveats, underrepresentation in drug trials]

### Professional Profile
- **Role / occupation:** [role]
- **Implications for health:** [e.g. sedentary work, high cognitive load, shift work, occupational stress, limited break time, physical demands]

### Care Team
- **Primary GP / coordinator:** [name or role] — [what they manage; quality of relationship]
- **[Specialist 1]:** [what they manage; appointment frequency]
- **[Specialist 2]:** [what they manage; appointment frequency]
- **⚠️ Coordination gap:** [Document any gaps — e.g. two specialists managing the same patient with no documented communication between them; systems that are interconnected but managed separately]

### Baseline Conditions for All Blood Results
- [Date of clinical starting point — e.g. first abnormal result, diagnosis date]
- [Date deliberate lifestyle changes began, if applicable]
- [Describe lifestyle baseline under which results were obtained — alcohol, diet, exercise, stress level, supplements]
- **These results represent [ceiling / baseline / mixed conditions]** — [interpretation note]

---

## 2. Central Theme & Hypothesis Register

### 2a. Confirmed Facts Register

> These are verified data points — not interpretations. Any analysis must be consistent with all of these. Each fact carries a FACT-XX ID and a source reference.

| ID | Fact | Source | Confirmed |
|----|------|--------|-----------|
| FACT-01 | [Confirmed observation — e.g. "All liver markers normalised from Apr 2024 onward"] | [EV-XX] | [Date] |
| FACT-02 | [Confirmed observation] | [EV-XX] | [Date] |

*Add rows as facts are confirmed. Remove a fact only if new evidence contradicts it — document the contradiction.*

---

### 2b. Observed Patterns (Correlation, Not Confirmed Causation)

> These patterns are consistent across the data but have not been formally investigated as causal mechanisms.

- [Pattern 1 — e.g. "Health deterioration correlates with periods of sustained high stress across multiple documented episodes"]
- [Pattern 2]
- [Pattern 3]

*Patterns can be promoted to hypotheses (Section 2c) when they are consistent enough to warrant active tracking. They can be promoted to confirmed facts when formally investigated and verified.*

---

### 2c. Hypothesis Register

> Hypotheses are working interpretations only. They are informed by confirmed observations but are **not confirmed facts**. New data should be used to test, revise, or replace them — not simply confirm them.
> Each hypothesis carries a trace tag linking it to supporting evidence and any facts it must not contradict.

| Hypothesis | ID | Confidence | Primary Evidence | Gaps / What Could Change This | Last Updated |
|------------|----|-----------:|-----------------|-------------------------------|:------------:|
| [Hypothesis statement] | HYP-01 | High / Medium-High / Medium / Low | [EV-XX, EV-XX] | [What new data would change the confidence level] | [Date] |
| [Hypothesis statement] | HYP-02 | | | | |

**Inline trace tags (use in module files and Index when citing a hypothesis):**
```
HYP-01: [Hypothesis statement]
[Trace: HYP-01 <- EV-XX, EV-XX | Exclude: FACT-XX | Date: YYYY-MM-DD]
```

---

### 2d. Update Protocol
> See **Section 11** — keeping operational instructions separate from clinical content.

---

## 3. Core Diagnoses & Active Conditions

### 3.1 [Condition Name] — *[Primary / Active / Resolved / Under Investigation]*
- **Diagnosed:** [Date and method — e.g. via imaging, blood test, clinical assessment]
- **Status:** [Current state — active, monitoring, treated, resolved]
- **Trigger / suspected cause:** [If known or hypothesised — note confidence level]
- **Consequence:** [How this condition affects other systems or markers]
- **Treatment status:** [Current treatment, what has been tried, what is under discussion]

### 3.2 [Condition Name] — *[Status]*
- [Fill as above]

*Add a subsection for each active condition. Resolved conditions that remain relevant (e.g. as part of a pattern) can be noted here briefly and detailed in a module.*

---

## 4. [Patient-Specific Risk Factor or Theme]

> Use this section for any patient-specific factor that cuts across all systems and requires consistent framing in every analysis.
>
> Examples: "Stress as a documented disease trigger", "Immunosuppression history", "Family history of [condition]", "Post-treatment surveillance context"

[Describe the factor, its documented evidence, and why it must be considered in every analysis.]

**What to monitor:**
- [Signal 1]
- [Signal 2]

---

## 5. Current Lifestyle Baseline

> Note this carefully — it determines how to interpret all current results.

- **Alcohol:** [Amount / zero]
- **Diet:** [Describe key features — what you eat, what you avoid, any relevant nutritional context]
- **Exercise:** [Type, frequency, duration, any relevant notes on tolerance or response]
- **Stress:** [Current level; how managed; any relevant context]
- **Supplements / medications:** [List all supplements and medications; note start dates where relevant]
  - ⚠️ **Analytical impact:** [Note any supplements that affect interpretation of blood results — e.g. B12/folate supplementation affects those markers; iron supplementation or recent infusion affects iron studies; biotin affects thyroid panels]

---

## 6. Recent Blood Results (Rolling — 2 Most Recent Tests)

> **Full historical results:** `Raw Data/` folder — one file per test date (e.g., `Raw Data/2026-05-13.md`) with EV-XX IDs
> **Personal baselines:** Recorded in relevant module files
> **Update rule:** On new results — (1) create `Raw Data/YYYY-MM-DD.md` with EV-XX ID; (2) add block below labelled ⭐ CURRENT; (3) re-label previous CURRENT as "trend reference"; (4) move older trend reference to its raw data file; (5) update Sections 7 and 9

---

### [Month Year] — Lab ref: [REF] | [trend reference / ⭐ CURRENT]
- **Date/time:** [DD/MM/YY, HH:MM]
- **Fasting:** [Yes / No / Unknown — if non-fasting, time since last meal]
- **Circumstances:** [Routine monitoring / acute investigation / specific context]
- **EV ID:** [EV-XX — maps to `Raw Data/YYYY-MM-DD.md`]

**[Panel name — e.g. Liver Function]**
- [Marker]: [Value] [Unit] [ref range] [✅ / ⚠️ / ⚠️H / ⚠️L]

**[Panel name — e.g. Haematology]**
- [Marker]: [Value] [Unit] [ref range] [✅ / ⚠️]

*Use ✅ for within range and personal baseline, ⚠️ for notable (out of range OR above/below personal baseline), ⚠️H or ⚠️L for directional flags.*

---

## 7. Pending Results & Outstanding Tests

| Test | Status | Notes |
|------|--------|-------|
| [Test name] | 🔲 Pending / ✅ Received | [Context — why ordered, what hypothesis it will resolve] |

---

## 8. What Has Been Ruled Out

| Condition / Cause | How Ruled Out |
|-------------------|---------------|
| [Condition] | [Method — e.g. blood test, imaging, formal investigation; date] |

*This section exists to prevent wasted time revisiting confirmed exclusions. Do not suggest causes listed here without new evidence.*

---

## 9. Open Questions & Active Investigations

1. **[Question 1]** — [Context and what needs to happen to resolve it]
2. **[Question 2]** — [Context]
3. **[Standing recommendation: test / referral]** — [What, when, why]

*This section is the agenda for appointments. Each open question should map to an action (test, referral, treatment decision, specialist consultation).*

---

## 10. Critical Notes for Any Clinician or AI Analysis

1. **[Key analytical constraint — e.g. "Never analyse any single system in isolation"]**
2. **[Personal baseline note — e.g. "Elevated ESR is this patient's long-standing constitutional baseline — do not treat as a sign of active flare in isolation"]**
3. **[Ruled-out note — e.g. "Do not suggest medication non-adherence as a cause — confirmed excluded; adherence formally verified"]**
4. **[Ethnicity / demographics note if applicable]**
5. **[Results interpretation note — e.g. "All results reflect best-case conditions — lifestyle fully optimised"]**

---

## 11. Evidence Registry

> Maps all EV-XX IDs to their source files. Add a row when a new file is created.

| EV ID | Source File | Content | Verified |
|-------|------------|---------|---------|
| EV-01 | `Raw Data/YYYY-MM-DD.md` | [Brief description — e.g. "Blood draw Jan 2024 — acute liver inflammation"] | ✅ / ⚠️ |
| EV-02 | `modules/[module].md` | [Brief description] | |
| EV-03 | `research/[topic].md` | [Brief description] | |

---

## 12. Maintenance Protocol

> **This index is the master document.** It controls update sequencing across all wiki files.

### Hypothesis updates
- New finding supporting or challenging a hypothesis → update confidence in Section 2c with date and reasoning
- New cause ruled out → add to Section 8
- Hypothesis confidence change requires at least one new independent data point; note what changed and why
- New confirmed fact → add to Section 2a with FACT-XX ID and EV-XX source; remove from hypothesis register if previously listed there
- New evidence file → add to Evidence Registry (Section 11) with EV-XX ID

### Blood test rotation (Section 6)
1. Create `Raw Data/YYYY-MM-DD.md` with complete raw results; assign EV-XX ID; add to Evidence Registry
2. Add new block to Section 6 labelled ⭐ CURRENT
3. Re-label previous CURRENT block as "trend reference"
4. Move older trend reference block to its raw data file if not already there
5. Update Section 7 — mark received items, remove resolved items
6. Check Section 9 — update or close any questions the new results address
7. Check Sections 2a and 3 — update confirmed observations or active condition summaries if warranted

### Module file update sequencing
When a new event, appointment, or result occurs, update files in this order:

**Step 1 — Relevant module file first:** Update longitudinal tables, trajectory notes, and open questions in the domain module. Note the EV-XX ID of the source.

**Step 2 — This index last:**
- Update Section 2a (confirmed facts), Section 2c (hypothesis confidence), Section 3 (active conditions), Section 7 (pending items), Section 9 (open questions) as warranted
- Cross-file consistency check: any hypothesis confidence change must be traceable to evidence in a module file with an EV-XX reference
- Update the *Next update* footer

### Research file updates
- Flag research files older than 12–18 months in active fields for refresh
- Add a "Last reviewed" date to each research file on refresh
- Update the relevant module's "Research notes" section if findings have changed

---

*Next update: [Describe what triggers the next update — e.g. "After next GP appointment / after [specific test] results arrive / after [treatment] decision"]*
