# Test: LinkedIn Public Job Page

Input:

```bash
python3 scripts/extract_jd.py tests/fixtures/linkedin_public_job.html
```

Expected behavior:
- Extract `title: AI Specialist`.
- Extract `company: Confidential`.
- Extract visible JD text before similar jobs.
- Extract responsibilities and requirements when visible.

Pass criteria:
- Similar jobs are not mixed into the primary JD text.
- No hidden content is guessed.

Chrome-assisted note:
- If Chrome opens the LinkedIn URL but text extraction is blocked by Chrome settings, mark Chrome-assisted extraction as blocked and fall back to public extraction or pasted JD text.
