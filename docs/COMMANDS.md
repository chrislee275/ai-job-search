# Commands

Use slash-style commands when you want explicit routing. Natural language also works.

| Command | Use |
|---|---|
| `/ai-job-search:setup` | Create, refresh, or gap-fill a `Job Search Profile`. |
| `/ai-job-search:review` | Review 1-3 jobs or job descriptions. |
| `/ai-job-search:batch` | Triage 4+ jobs, alerts, or recurring job lists. |
| `/ai-job-search:apply-prep` | Prepare application strategy after you decide to apply. |
| `/ai-job-search:resume` | Plan resume strategy, positioning, and keywords. |
| `/ai-job-search:profile` | Improve LinkedIn, job-board, ATS, or portfolio profiles. |
| `/ai-job-search:reply` | Draft recruiter, HR, email, DM, or chat replies. |
| `/ai-job-search:interview` | Prepare interviews and run mock practice. |

## Subflows

- JD link access uses `scripts/extract_jd.py` for public pages and browser-assisted review when available.
- Cover letters are handled inside `/ai-job-search:apply-prep` and only when explicitly requested or required.
- Mock interviews are handled inside `/ai-job-search:interview`.
- Company research is used only when requested or needed for application/interview context.
- Optional automation prompts are handled through `/ai-job-search:batch` or `/ai-job-search:reply` style workflows.

## Natural Language Examples

```text
Is this job worth applying to?
Help me rank these 8 jobs.
Help me reply to this recruiter.
Which resume version should I use?
Prepare me for this interview.
```
