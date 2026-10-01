#!/usr/bin/env bash
set -euo pipefail

CODEX_HOME="${CODEX_HOME:-${HOME}/.codex}"
TARGET_DIR="${CODEX_HOME}/skills/job-search-assistant"

if [ ! -d "${TARGET_DIR}" ]; then
  echo "job-search-assistant is not installed at ${TARGET_DIR}"
  exit 0
fi

rm -rf "${TARGET_DIR}"
echo "Removed ${TARGET_DIR}"
