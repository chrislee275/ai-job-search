# Test: Scoring N/A When Not Material

Input:

```text
/ai-job-search:review
Junior Marketing Assistant, remote, part-time, no salary listed. The user has no work authorization constraints for this country.
```

Expected behavior:
- Use `N/A` for score subfields that are not material or not supported by evidence.
- Do not force salary or authorization scoring when information is missing or irrelevant.
- Explain missing evidence briefly.

Pass criteria:
- No fake salary or authorization assumptions.
- Decision remains provisional if salary or key JD details are unavailable.
