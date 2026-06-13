# Personal Health Wiki Project

A framework for building and maintaining a personal health knowledge base — structured around your actual clinical data, blood test results, specialist reports, and ongoing research.

The goal is to support informed conversations with clinicians, track findings over time, and maintain a queryable personal health record that you own and control.

## What This Is

This project provides:

- **Template kit** — a wiki skeleton with module templates for common chronic conditions (haematology, liver/metabolic, hormonal-reproductive, autoimmune-inflammatory, neurological, oncology, imaging)
- **Skills** — Cowork agent skills that automate the mechanical work: wiki setup, data import, PII stripping, baseline establishment, and rolling window updates
- **Reasoning engine** — analytical defaults and an audit prompt for maintaining reasoning quality over time

The framework is AI-platform-agnostic. Wiki files produced by the skills work with Claude, ChatGPT, Gemini, or any capable AI.

## Getting Started

> **Skills are in active development and will be released shortly.** In the meantime, use the manual setup path below — the template kit is fully functional without them.

**Using the skills (recommended, coming soon):** You need [Cowork](https://claude.ai) to run the skills.

1. Connect this folder to Cowork
2. Say: **"Start my health wiki set up"** — the bootstrap skill runs a guided interview and builds your personalised wiki skeleton
3. When ready to add data: **"Import my health data"** — the data import skill handles transcription, PII stripping, baselines, and computed values

**Setting up manually (without Cowork):** Copy the `template-kit/` folder, then paste the full contents of `template-kit/01_Reasoning_Engine/analytical_defaults.md` into your AI project instructions or system prompt before starting any health conversation. This file contains the emergency protocol and analytical reasoning principles that govern safe use of the wiki. Do not skip this step.

Your personal wiki instance lives locally on your machine. It is never part of this repository.

## Repository Structure

```
template-kit/        — wiki skeleton templates (CC-BY-SA 4.0)
  00_Setup/          — blood test templates, marker manifest, imaging template
  01_Reasoning_Engine/ — analytical defaults, audit prompt
  02_Patient_State/  — module templates by condition
skills/              — Cowork agent skills (Apache 2.0)
  health-wiki-bootstrap/
  health-wiki-data-import/
docs/                — design decisions, research notes
```

## Contributing

Contributions are welcome — particularly new condition modules, lab manifest seeds for non-Australian labs, and improvements to existing templates.

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to contribute and which license applies to your contribution.

## Medical Disclaimer

This project is a personal knowledge management framework. It is not a medical record system, not a clinical decision support tool, and not a substitute for professional medical advice, diagnosis, or treatment.

Nothing in this repository constitutes medical advice. All information is provided for personal organisational purposes only. Always consult a qualified healthcare professional for medical decisions.

Contributors to this project are not liable for any health outcomes resulting from its use.

## License

**Skills and code** (`skills/`): Apache 2.0 — see [LICENSE](LICENSE)

**Templates and content** (`template-kit/`): Creative Commons Attribution-ShareAlike 4.0 International — see [LICENSE-CONTENT](LICENSE-CONTENT)

This means: you can use, modify, and redistribute the skills commercially with attribution. If you build on or redistribute the templates and module content, your version must remain open under the same terms.
