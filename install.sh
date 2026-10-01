#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CODEX_HOME="${CODEX_HOME:-${HOME}/.codex}"
SKILLS_DIR="${CODEX_HOME}/skills"
SOURCE_DIR="${REPO_DIR}/skills/job-search-assistant"
TARGET_DIR="${SKILLS_DIR}/job-search-assistant"

if [ ! -f "${SOURCE_DIR}/SKILL.md" ]; then
  echo "ERROR: ${SOURCE_DIR}/SKILL.md not found." >&2
  exit 1
fi

mkdir -p "${SKILLS_DIR}"
rm -rf "${TARGET_DIR}"
cp -R "${SOURCE_DIR}" "${TARGET_DIR}"

echo "Installed job-search-assistant to ${TARGET_DIR}"
echo "Restart Codex, then try: Use \$job-search-assistant to review this JD."
