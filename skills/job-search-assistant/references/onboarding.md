# Onboarding and Job Search Profile

Use this when the user runs `/ai-job-search:setup` or asks to set up, personalize, refresh, update, or save their job-search profile.

## Behavior

1. Look for resume/source files and any existing `*job-search-profile*.md` in the current workspace if file access is available.
2. If a profile exists, summarize known fields, missing fields, and stale/uncertain fields. Do not restart onboarding from scratch.
3. If no profile exists, run first setup.
4. Ask only missing key details, one question or one small related group at a time.
5. Output a `Job Search Profile`.
6. Ask whether the user wants to save it as Markdown.
7. Save only after explicit confirmation. Default filename: `YYYY-MM-DD-job-search-profile.md` in the current working directory.

## Required Fields

- Target roles.
- Location and work-mode preferences.
- Salary expectation, if relevant.
- Notice period or availability.
- Work authorization or sponsorship needs, if relevant.

## Optional Fields

- Roles to avoid.
- Skills to highlight.
- Skills to downplay or mark as exposure-only.
- Portfolio, LinkedIn, job-board, or proof links.
- Interview concerns.
- Resume versions and when to use each.

## Output

```markdown
# Job Search Profile

## Target Roles

## Location and Work Mode

## Compensation

## Availability

## Work Authorization

## Skills to Highlight

## Exposure-Only or Downplayed Skills

## Roles to Avoid

## Resume / Profile Sources

## Interview Concerns

## Missing Info
```

Do not call the profile permanent memory unless it was actually saved.
