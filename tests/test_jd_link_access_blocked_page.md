# Test: JD Link Access Blocked Page

Input:

```bash
python3 scripts/extract_jd.py https://example.invalid/job/123
```

Expected behavior:
- Return `status: blocked`.
- Return `confidence: None`.
- Include a note that the source could not be accessed.

Pass criteria:
- Does not guess title, company, salary, work mode, or responsibilities.
- Skill should ask for JD text or screenshot.
