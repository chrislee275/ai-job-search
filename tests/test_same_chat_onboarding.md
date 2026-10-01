# Test: Same-Chat Onboarding

Input:

```text
/ai-job-search:setup
I uploaded my resume. Please set up my assistant.
```

Expected behavior:
- Read available source files if possible.
- Ask missing info one small group at a time.
- Produce `Job Search Profile`.
- Ask before saving Markdown.

Pass criteria:
- Does not ask user to paste a short/full profile into project instructions.
- Does not claim permanent memory unless saved.
