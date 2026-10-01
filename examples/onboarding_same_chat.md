# Example: Same-Chat Setup

Prompt:

```text
/ai-job-search:setup

I have uploaded my resume. Help me set up my job search profile.
```

Expected behavior:
- Read source files if available.
- Ask only missing key details.
- Output `Job Search Profile`.
- Ask before saving Markdown.

The assistant must not claim permanent memory unless it actually saves a file.
