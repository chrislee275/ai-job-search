# Test: Cover Letter Framework

Input:

```text
/ai-job-search:apply-prep
Write a cover letter for this JD.
```

Expected behavior:
- State Required / Worth writing / Optional / Not necessary first.
- Use the required cover letter structure.
- Do not invent company facts or metrics.

Pass criteria:
- Starts with `Dear Hiring Manager,` unless a contact is provided.
- Avoids "I am writing to apply for..."
