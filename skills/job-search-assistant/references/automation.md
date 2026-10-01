# Optional Automation Workflows

The skill is not an automation engine. Use this only when the user asks for automation, recurring review, scheduled checks, daily job review, weekly summary, recruiter inbox screening, job alert screening, interview invite watch, assessment watch, duplicate checks, applied-job checks, or automation-ready prompts.

Do not assume Gmail, calendar, browser, job platform, or tracker access. If connected tools are unavailable, ask the user to paste the job list, tracker rows, or email content.

## Supported Workflows

- Daily job review.
- Recruiter inbox review.
- Weekly pipeline summary.
- Interview/assessment watch.
- Duplicate and applied-job handling.

## Safety Boundaries

- Never auto-apply.
- Never auto-send recruiter replies.
- Never delete, archive, label, or modify emails without explicit confirmation.
- Never update trackers without explicit confirmation.
- Never mark a job as applied unless the user confirms or an application confirmation is clearly provided.
- Never fabricate missing JD details, salary, work mode, sponsorship, or seniority.

## Daily Job Review Prompt

Review new job recommendations from the provided source. Compare them against the user's active target roles, location/work mode preferences, salary expectations, work authorization needs, and avoid list. Skip duplicates and already-applied roles only if that status is provided. Output a ranked triage table with Top Matches, Easy Apply Only, Save for Later, Skip, and Need Info. Do not apply, send messages, delete emails, label emails, or update trackers without explicit user confirmation.

## Recruiter Inbox Review Prompt

Review recruiter or job-related messages from the provided source. Categorize them into Needs Attention, Worth Reviewing, Low Priority/Skip, Duplicates/Already Applied, and Missing Info. Identify interview invites, assessment requests, salary questions, recruiter outreach, rejection emails, and application confirmations. Do not reply, archive, delete, label, or mark anything as applied unless explicitly confirmed by the user.

## Weekly Summary Prompt

Summarize this week's job search pipeline from the provided tracker or job list. Show applications submitted, interviews, recruiter replies, pending actions, high-fit roles to follow up, skipped roles, and next week's priority actions. Do not invent application status or outcomes.

## Interview Watch Prompt

Check the provided messages for interview invitations, assessment links, recruiter follow-ups, scheduling requests, or urgent deadlines. Notify the user only if there is something requiring action. If nothing meaningful changed, say no action needed.
