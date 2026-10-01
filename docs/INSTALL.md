# Install

## One-Line Local Install

From the repository root:

```bash
bash install.sh
```

This copies `skills/job-search-assistant` into:

```text
~/.codex/skills/job-search-assistant
```

Then restart Codex and try:

```text
Use $job-search-assistant to review this JD.
```

## Custom Codex Home

```bash
CODEX_HOME=/path/to/.codex bash install.sh
```

## Review Before Installing

The installer only:

1. Creates `~/.codex/skills` if needed.
2. Removes the existing `~/.codex/skills/job-search-assistant`.
3. Copies `skills/job-search-assistant` into that location.

It does not install dependencies, edit profiles, connect to job boards, or configure automations.

## Uninstall

```bash
bash uninstall.sh
```

Or with a custom Codex home:

```bash
CODEX_HOME=/path/to/.codex bash uninstall.sh
```
