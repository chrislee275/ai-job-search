# JD Link Access

This repository supports JD links in three tiers.

## Tier 1: Public Page Extraction

Use the bundled `scripts/extract_jd.py` for public job pages and local HTML files:

```bash
python3 scripts/extract_jd.py "https://company.example/jobs/123"
```

The script outputs JSON with:

- `title`
- `company`
- `location`
- `work_mode`
- `salary`
- `visible_text`
- `confidence`
- `notes`

It prefers structured `JobPosting` JSON-LD when available, then falls back to visible HTML text.

## Tier 2: Browser-Assisted Review

Use browser-assisted review when a job page needs login, has dynamic content, or blocks direct fetching.

Rules:

1. Open the job link in the user's browser or available browser tool.
2. Read only visible content.
3. Do not bypass login, paywalls, captcha, platform restrictions, or robots-style access controls.
4. If the page is blocked or incomplete, ask the user to paste JD text or provide a screenshot.
5. Never infer salary, work mode, sponsorship, seniority, or responsibilities from platform reputation alone.

## Access Outcomes

| Outcome | Skill behavior |
|---|---|
| Full JD visible | Run full JD review. |
| Partial snippet visible | Run provisional review; confidence max `Medium-Low`. |
| Link only / blocked | `Score: N/A`, `Decision: Need Info`, ask for JD text or screenshot. |
| Login/captcha required | Stop and ask user for visible content. |

## Tier 3: Chrome-Assisted Review

Use Chrome-assisted review when the user explicitly wants to use their existing Chrome state, such as an already logged-in LinkedIn, JobStreet, Indeed, or company careers session.

Rules:

1. Open or claim the JD link in Chrome.
2. Read only content visible to the user in Chrome.
3. Do not inspect cookies, local storage, passwords, session tokens, or hidden profile data.
4. Do not click Apply, Easy Apply, message recruiters, save jobs, submit forms, or change profile settings.
5. Do not bypass login, paywalls, captcha, platform restrictions, or permission prompts.
6. If Chrome shows a login/captcha/restricted page, stop and ask the user to log in or provide JD text/screenshot.
7. If Chrome shows more complete JD content than public extraction, use Chrome-visible content as the review source and label it as Chrome-assisted.

Chrome implementation note:

- The Codex Chrome extension is the preferred Chrome-assisted path when available.
- If using macOS AppleScript as a fallback, Chrome must enable `View > Developer > Allow JavaScript from Apple Events` before page text can be read.
- If Chrome opens the page but text access is blocked by browser settings, do not guess. Ask the user to enable the setting, use the extension, or paste the visible JD text.

Recommended order:

```text
extract_jd.py public extraction -> browser-assisted review -> Chrome-assisted review -> ask for pasted JD/screenshot
```

## Safety Boundary

JD link access improves source collection. It does not change the manual-first rule: the skill must not auto-apply, send messages, edit profiles, or guess hidden job details.
