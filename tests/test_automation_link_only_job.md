# Test: Automation Link-Only Job

Input:

```text
/ai-job-search:batch
Daily alert: LinkedIn job URL only, no title or JD.
```

Expected behavior:
- `Score: N/A`.
- `Decision: Need Info`.
- Ask for JD/screenshot.

Pass criteria:
- No guessing from platform or user profile.
