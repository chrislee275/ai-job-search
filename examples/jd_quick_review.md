# Example: JD Quick Review

Prompt:

```text
/ai-job-search:review

Here is a full JD for a Product Analyst role...
```

Expected behavior:
- Score only visible JD content.
- Use the user's Job Search Profile if available.
- Keep the output short by default.
- Include detailed score breakdown only when the user asks for detail or the JD is high-stakes/ambiguous.

Short output shape:

```markdown
## JD Quick Review

Score:
Decision:
Resume:
Why:
Risks:
Next action:
Time budget:
Do not spend time on:
```
