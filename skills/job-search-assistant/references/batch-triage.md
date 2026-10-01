# Batch JD Triage

Use this for `/ai-job-search:batch`, 4+ jobs, daily review lists, job alerts, pasted job tables, or automation-style job recommendations.

Do not deep review every job unless explicitly asked. Detail only the top 1-2 roles after triage.

## Output Table

```markdown
| Rank | Role/Company | Source | Score | Decision | Type | Main Risk | Resume/Version | Time Budget | Next Action |
|---|---|---:|---|---|---|---|---|---|
```

## Rules

- Full JD: score normally.
- Partial snippet: provisional score only; confidence max `Medium-Low`.
- Link only: `Score: N/A`, `Decision: Need Info`.
- Do not infer missing JD details from title, platform, or user profile.
- Do not write cover letters during triage unless explicitly requested.
- Spend minimal effort on low-fit roles.
- If a job appears multiple times, keep the best/most complete entry and flag duplicates.
- If applied history is unavailable, write `Applied status unknown`; do not claim already applied.
