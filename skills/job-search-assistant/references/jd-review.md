# JD Quick Review

Use this for `/ai-job-search:review`, 1-3 jobs, or natural-language requests like "is this job suitable", "should I apply", "score this job", or "quick review".

## Source Quality Rules

- Full JD: full review allowed.
- Partial title/company/snippet: provisional review only; confidence max `Medium-Low`.
- Title only: direction only; no confident score.
- Link or ID only: do not guess, do not score, do not recommend applying. Output `Score: N/A`, `Decision: Need Info`, `Resume: N/A`, and ask for JD text or screenshot.
- If a JD link is provided and tools are available, use the JD link access workflow before reviewing. Prefer `scripts/extract_jd.py` for public pages, then browser-assisted review for dynamic/login pages. Score only visible content.

## JD Link Access

For public pages, use:

```bash
python3 scripts/extract_jd.py "<job-url>"
```

If the script returns `status: blocked`, `confidence: None`, or no useful `visible_text`, do not guess. Ask for JD text or screenshot.

For pages that need login or render dynamically, use browser-assisted review only when a browser tool is available. Read visible content only. Do not bypass login, captcha, paywalls, or platform restrictions.

If the user explicitly asks to use Chrome or the task depends on an existing logged-in Chrome session, use Chrome-assisted review. Read only visible page content. Do not inspect cookies, local storage, passwords, or hidden session data. Do not click Apply/Easy Apply, save jobs, send messages, or change profile settings.

Detailed rules live in `references/jd-link-access.md`.

## Output

Default to the short output. Keep the review decision-focused. Only include score breakdown, detailed company context, or longer reasoning when the user asks for detail or the JD is high-stakes/ambiguous.

```markdown
## JD Quick Review

Score:
Decision:
Resume:
Why:
Risks:
Next action:
Time budget:
Do not spend time on:
```

## Decisions

- Priority Apply
- Easy Apply Only
- Save
- Need Info
- Reply Recruiter
- Skip
- Interview Prep

## Type

Use user-specific target categories if known. Otherwise use:
- Core Target: directly matches the user's stated target role and strongest evidence.
- Adjacent Target: related enough to consider with light repositioning.
- Stretch: possible but needs skill, seniority, or domain gap handling.
- Not Target: conflicts with target direction, constraints, or avoid list.

## Scoring

- Use `Score: N/A` when JD content is unavailable. Do not use `0/100` for missing content.
- Use `N/A` for a score subfield when it is not material or there is not enough evidence. Briefly state why.
- Work mode/location must reflect the user's stated preference, not generic assumptions.
- Salary and authorization realism must use user-provided facts or be marked uncertain.
- Growth/risk is high only when growth is strong and risk is low.
- Do not name a resume version unless source files or the user provide it.
- If the user has only one known resume, write `Current resume` or `Best matching resume` instead of forcing a version name.
- Do not invent metrics or resume facts.

## Company Research

Research company facts only when the user asks, when the JD is ambiguous, or when company facts materially affect the decision. Verify current facts when browsing is available. If not available, label company context as unverified and do not invent culture, funding, layoffs, sponsorship policy, or salary bands.
