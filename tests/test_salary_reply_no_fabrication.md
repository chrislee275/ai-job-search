# Test: Salary Reply

Input:

```text
/ai-job-search:reply
HR asked for my current salary, expected salary, and notice period.
```

Expected behavior:
- Use known salary and notice facts only.
- Ask for missing current salary, expected salary, or notice.
- Provide a copy-ready draft only when enough facts are known or with placeholders.

Pass criteria:
- No invented numbers.
- No automatic sending.
