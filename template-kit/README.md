# Health Wiki Template Kit
> A personal health knowledge framework for people navigating complex, multi-system conditions.
> **Version:** 1.1 — Phase 1 Template Kit (restructured)
> **Status:** Ready to use

---

## What This Is

This kit gives you a **personal health intelligence framework** — a structured, longitudinal knowledge system for people navigating complex, multi-system health conditions. It is not a medical record, a diagnostic tool, or a static data store. It reasons, audits, and compounds knowledge over time.

**What makes it distinctive:**
- Analyses your health as an interconnected system — liver, blood, hormones, and neurology reasoned together, not in the silos that specialist medicine uses
- Detects meaningful shifts within your *personal* reference range before they become clinical events — population norms are designed for 95% of healthy adults and are deliberately wide; your individual baseline detects drift that those ranges will miss entirely
- Integrates current research findings for your specific conditions and cross-checks them against your individual data — not generic health information, but research applied to your circumstances

**What it enables:**
- Track findings longitudinally across months and years, not just at each appointment
- Communicate with clinicians from a position of structured knowledge
- Detect when reasoning about your health has drifted from established facts

All data stays in your own files. Nothing leaves your environment.

---

## Who This Is For

This framework serves two equally valid users.

**The patient** who wants to take ownership of their own health picture:
- Living with a complex condition — or multiple conditions managed by more than one specialist
- Has access to test results and clinical reports
- Wants to understand their health longitudinally, not just at each appointment
- Willing to maintain the framework as new information arrives

**The family member or carer** building this on behalf of someone they love:
- A parent, partner, or child who is too unwell, too overwhelmed, or not tech-comfortable to set this up themselves
- Someone who attends appointments with the patient, holds the longitudinal memory of what has changed, and notices patterns the clinical system misses
- Someone who wants to hand the patient a structured, queryable picture of their own health — not just a folder of test results

The carer use case is not secondary. Complex chronic illness often affects the very capacity needed to manage it. The person best positioned to build the framework is frequently not the patient.

---

## How This Kit Is Organised

The template kit uses a four-layer architecture. Each layer has a distinct role — understanding this helps you use the kit correctly.

```
template-kit/
├── README.md                    ← you are here
│
├── 00_Setup/                    ← Entry point & bootstrap layer
│   ├── index_template.md        ← personalise as your index.md
│   ├── blood_test_template.md   ← copy for each blood draw
│   ├── imaging_template.md      ← copy for each scan report
│   ├── research_template.md     ← copy for each research topic
│   └── clinical-communication/  ← Australian healthcare navigation (conditional)
│
├── 01_Reasoning_Engine/         ← "The Mind" — reasoning principles and audit system
│   ├── analytical_defaults.md   ← copy to project instructions during setup
│   └── audit_prompt.md          ← run periodically for wiki integrity checks
│
├── 02_Patient_State/            ← "The Canvas" — reasoning, interpretation, cross-system links
│   └── modules/
│       ├── core/                ← near-universal; use for almost any chronic patient
│       ├── conditions/          ← add if patient has this diagnosis
│       ├── overlays/            ← add when these processes are active in any system
│       └── dual/                ← two modes; route based on symptoms
│
└── 03_Patient_Records/
    └── transcribed/             ← PII-stripped structured markdown files — what the AI reads
```

---

## Files in This Kit

### 00_Setup — Templates and bootstrap materials

| File | Purpose |
|------|---------|
| `00_Setup/index_template.md` | Master index — copy and personalise as `index.md`; the file Claude reads at the start of every health conversation |
| `00_Setup/blood_test_template.md` | Standard format for logging raw blood test results; includes CSV data block and Calculation Protocol for personal baseline deviation |
| `00_Setup/imaging_template.md` | Standard format for logging scan reports verbatim |
| `00_Setup/research_template.md` | Standard format for capturing condition-specific research |
| `00_Setup/blood-tests-metadata.md` | Structural rulebook for all blood test files — data states, naming rules, what never goes in a source file. Read before entering your first blood test. |
| `00_Setup/blood-tests-marker-manifest.md` | Canonical marker naming dictionary — personalise for your lab during setup; add markers as you go to prevent naming inconsistencies |
| `00_Setup/clinical-communication/` | Australian healthcare navigation tools — 6 files covering GP sourcing, vetting, appointment prep, SBAR briefing, and referral guidance |

### 01_Reasoning_Engine — "The Mind"

| File | Purpose |
|------|---------|
| `01_Reasoning_Engine/analytical_defaults.md` | 11 universal reasoning principles — copy into your project instructions / system prompt during setup so they are always active; paste into conversations if using the paste workflow |
| `01_Reasoning_Engine/audit_prompt.md` | Monthly audit prompt for detecting reasoning drift, hypothesis violations, cross-module conflicts, and data layer integrity issues |

### 02_Patient_State — "The Canvas" (Module Library)

The bootstrap skill (Phase 2) will recommend modules based on your conditions and symptoms. For now, select manually using the descriptions below.

**Core — near-universal**

| File | Covers |
|------|--------|
| `02_Patient_State/modules/core/haematology.md` | Full blood count, iron studies, B12/folate — the primary tracking home for these markers across the entire wiki |
| `02_Patient_State/modules/core/imaging.md` | Longitudinal scan tracking — ultrasound, MRI, CT, echocardiogram; includes Watch Register and Incidental Findings Register |

**Conditions — add if you have this diagnosis**

| File | Covers |
|------|--------|
| `02_Patient_State/modules/conditions/metabolic-liver.md` | Fatty liver (MASLD/NAFLD), lipids, triglycerides, metabolic syndrome; includes FIB-4 two-tier calculation protocol |
| `02_Patient_State/modules/conditions/hormonal-reproductive.md` | Menopause/perimenopause, thyroid, adenomyosis, fibroids, reproductive conditions; primary home for TSH/thyroid markers |
| `02_Patient_State/modules/conditions/oncology.md` | Cancer staging, tumour markers, treatment line tracking, surveillance; includes Nadir Register and velocity override rule |

**Overlays — add if these processes are active, regardless of primary diagnosis**

| File | Covers |
|------|--------|
| `02_Patient_State/modules/overlays/autoimmune-inflammatory.md` | ANA, specific antibodies, inflammatory markers, flare tracking — add when autoimmune markers are in play in any system |

**Dual-mode — select by how neurological fits your situation**

| File | Covers | Use when |
|------|--------|----------|
| `02_Patient_State/modules/dual/neurological-primary.md` | Full neurological history, diagnosis, treatment, rehabilitation | A neurological condition is your primary or a major diagnosis |
| `02_Patient_State/modules/dual/neurological-systemic.md` | Symptom tracking, mechanism identification, cross-system interpretation | You have neurological symptoms (tingling, brain fog, balance issues) arising from another primary condition |

### 03_Patient_Records — Transcribed Records

`03_Patient_Records/transcribed/` — PII-stripped structured markdown files created from your source documents (blood test files named `YYYY-MM-DD.md`; imaging files named `YYYY-MM-DD-[modality]-[region].md`). These are the only files the AI reads and analyses.

**Keep your original source documents — PDFs, printouts, and scan reports — stored outside the wiki folder**, in any location you manage on your own computer. The lab reference number in each transcribed file is what links it back to the source for manual verification. Source documents are not part of the wiki and are never accessed by the AI.

---

## Which AI and Interface Are You Using?

The framework works with any capable AI assistant: Claude, ChatGPT, Gemini, or others. What differs between platforms is how much of the workflow is automated and how files are managed.

**Any AI, paste workflow** — Works with any LLM in any interface. You maintain the wiki files locally, copy the relevant files into each conversation, and the AI works within that context. No setup beyond creating the files.