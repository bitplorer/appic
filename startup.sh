#!/bin/sh
set -eu
cd "$(dirname "$0")"
export PYTHONPATH="${PYTHONPATH:-.}"
export PYTHONUNBUFFERED=1
if curl -fsS --max-time 2 http://127.0.0.1:8080/ >/dev/null 2>&1; then
  exit 0
fi
python -m uvicorn app:asgi --host 0.0.0.0 --port 8080
