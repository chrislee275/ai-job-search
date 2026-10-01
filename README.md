# AI Job Search Assistant

8 commands. 1 job-search assistant skill. Review jobs, prepare applications, write recruiter replies, improve profiles, and practice interviews.

v1.0.0 · Manual-first · Privacy-first · No auto-apply

AI Job Search Assistant is a Codex skill for honest job-search support. It works with pasted job descriptions, public JD links, Chrome-visible job pages, recruiter messages, resume/profile text, source files, and saved job-search notes.

## Quick Start

Install locally:

```bash
bash install.sh
```

The installer replaces any existing local `job-search-assistant` skill copy.

Restart Codex, then ask naturally:

```text
Use $job-search-assistant to review this JD.
```

Command-style prompts also work:

```text
/ai-job-search:review
/ai-job-search:reply
/ai-job-search:interview
```

For review-before-install, custom `CODEX_HOME`, and uninstall instructions, see [docs/INSTALL.md](docs/INSTALL.md).

## Operating Model

The assistant routes each request to the smallest useful workflow. It works with pasted content by default and only uses files or connected tools when the user provides them. Every workflow keeps user action manual unless explicitly confirmed.

## Commands

| Command | Use it for |
|---|---|
| `/ai-job-search:setup` | Build or refresh a `Job Search Profile` |
| `/ai-job-search:review` | Review 1-3 jobs or job descriptions |
| `/ai-job-search:batch` | Triage 4+ jobs, alerts, or recurring job lists |
| `/ai-job-search:apply-prep` | Prepare application strategy after you decide to apply |
| `/ai-job-search:resume` | Plan resume strategy, positioning, and keywords |
| `/ai-job-search:profile` | Improve LinkedIn, job-board, ATS, or portfolio profiles |
| `/ai-job-search:reply` | Draft recruiter, HR, email, DM, or chat replies |
| `/ai-job-search:interview` | Prepare interviews and run mock practice |

Full command details live in [docs/COMMANDS.md](docs/COMMANDS.md).

## What It Helps With

- Decide if a job is worth applying to.
- Score fit and identify risks from a job description.
- Extract visible JD content from public job links.
- Triage multiple jobs from alerts or pasted lists.
- Choose a resume strategy without inventing experience.
- Improve LinkedIn, portfolio, ATS/job-platform profiles, and summaries.
- Turn recruiter or HR messages into copy-ready replies.
- Prepare interview answers and one-question-at-a-time mock practice.
- Create reusable prompts for scheduled or recurring job-search reviews.

## Safety Boundaries

This skill does not:

- Auto-apply.
- Send messages for you.
- Edit profiles for you.
- Update trackers unless explicitly requested and supported by the available tool.
- Fabricate experience, metrics, salary, work authorization, notice period, clients, certificates, projects, or outcomes.
- Assume target roles, location, salary, resume filenames, or visa/work authorization status.

## Job Search Profile

`/ai-job-search:setup` creates or refreshes a `Job Search Profile` from chat answers, source files, links, and explicit corrections. If a profile already exists, the assistant gap-fills or updates it instead of starting over.

Profile saving requires confirmation. Default filename: `YYYY-MM-DD-job-search-profile.md`.

## Examples

[JD review](examples/jd_quick_review.md) · [Batch triage](examples/batch_triage.md) · [Recruiter reply](examples/recruiter_reply.md) · [Interview prep](examples/interview_prep.md) · [Fake metric refusal](examples/fake_metric_refusal.md)

More examples live in [examples/](examples/).

## Verification

Manual QA scenarios live in [tests/](tests/). Run repository checks with:

```bash
python3 scripts/validate_repo.py
```

## Docs

- [Install](docs/INSTALL.md)
- [Commands](docs/COMMANDS.md)
- [JD link access](docs/JD_LINK_ACCESS.md)
- [Security](SECURITY.md)
- [Contributing](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)

## Disclaimer

This skill supports job-search decisions but does not guarantee interviews, offers, salary outcomes, visa approval, legal compliance, or hiring results. Verify important career, salary, immigration, and legal decisions with qualified sources.

## License

MIT. See [LICENSE](LICENSE).
