# Contributing

Contributions should make the skill clearer, safer, or easier to use.

## Good Contributions

- New examples for common job-search scenarios.
- Manual QA tests for risky cases.
- Clearer wording for truth boundaries.
- Better recruiter reply, interview prep, or profile optimization patterns.
- Region-specific guidance that avoids hard-coded assumptions.

## Rules

- Do not add private user data.
- Do not add fake resume facts, fake metrics, or misleading examples.
- Do not add auto-apply or auto-send behavior.
- Keep `SKILL.md` concise; put detailed workflow guidance in `references/`.
- Add or update a manual QA test when changing a boundary or output format.

## Local Validation

Run:

```bash
python3 scripts/validate_repo.py
```

Also run the Codex skill validator if available:

```bash
python3 /path/to/quick_validate.py skills/job-search-assistant
```
