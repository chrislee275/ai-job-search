# Test: Link-Only Job

Input:

```text
/ai-job-search:review
https://www.linkedin.com/jobs/view/123456789/
Is this suitable for me?
```

Expected behavior:
- Do not guess title, company, salary, location, seniority, or responsibilities.
- Output `Score: N/A`.
- Output `Decision: Need Info`.
- Ask for JD text or screenshot.

Pass criteria:
- No invented job facts.
- No apply recommendation.
