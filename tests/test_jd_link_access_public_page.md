# Test: JD Link Access Public Page

Input:

```bash
python3 scripts/extract_jd.py tests/fixtures/public_job.html
```

Expected behavior:
- Output valid JSON.
- Extract `title: Product Analyst`.
- Extract `company: ExampleCo`.
- Set confidence to `High` or `Medium`.
- Include visible JD content.

Pass criteria:
- No network required.
- No hidden content guessed.
