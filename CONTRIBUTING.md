# Contributing to Personal Health Wiki Project

Contributions are welcome. The most valuable areas are:

- **New condition modules** — templates for chronic conditions not yet covered (e.g. diabetes, MS, rheumatoid arthritis, IBD, cardiac conditions)
- **Lab manifest seeds** — pre-populated marker manifests for non-Australian lab formats
- **Skill improvements** — bug fixes, edge case handling, resume logic improvements
- **Analytical defaults** — refinements to the reasoning engine based on real clinical use
- **Documentation** — setup guides, worked examples, ADRs for design decisions

## What Applies Where

This project uses two licenses. Your contribution will fall under one of them depending on what you're contributing:

| What you contribute | License |
|---|---|
| Skills (`skills/`), scripts, code | Apache 2.0 |
| Templates, module files, content (`template-kit/`) | CC-BY-SA 4.0 |

**CC-BY-SA means your content contribution stays open.** Anyone who builds on or redistributes the templates must do so under the same terms. This protects the community knowledge base from being taken private.

If you're unsure which license applies to your contribution, open an issue and ask before submitting.

## How to Contribute

1. Fork the repository
2. Create a branch: `git checkout -b your-feature-or-fix`
3. Make your changes
4. Sign off your commits (see DCO below)
5. Open a pull request with a clear description of what you changed and why

For new condition modules, include a brief note on the chronic condition, which markers the module tracks, and any sources that informed the template structure.

## Developer Certificate of Origin (DCO)

By contributing, you certify that you have the right to submit your contribution under the applicable license, and that you agree to the [Developer Certificate of Origin](https://developercertificate.org/).

Add a sign-off line to each commit:

```
git commit -s -m "Your commit message"
```

This appends: `Signed-off-by: Your Name <your@email.com>`

## Privacy

Do not include personal health data in any contribution. No blood test results, imaging reports, personal wiki instances, or identifiable patient information. If you're sharing a worked example, use clearly fictional values.

The `.gitignore` excludes personal wiki instances — double-check before committing that no files from your local wiki are staged.

## Questions

Open an issue. For sensitive matters, contact the maintainers directly.
