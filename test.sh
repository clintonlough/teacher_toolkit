#!/usr/bin/env bash
set -euo pipefail

# activate venv (optional if already active)
source .venv/bin/activate

# ensure live flag is set for THIS process
export OPENAI_LIVE=1

# ensure API key is present (either already exported or read from .env)
if [[ -f .env && -z "${OPENAI_API_KEY:-}" ]]; then
  # naive .env load (works for simple KEY=VALUE lines)
  set -a
  source .env
  set +a
fi

python3 -m unittest discover -s test_files -p "test_*.py" -v