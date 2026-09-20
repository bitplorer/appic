#!/bin/sh
# APPIC product process — ux-compose ASGI on 0.0.0.0:8080.
set -eu
cd /workspace
export PATH="/workspace/.venv/bin:/root/.local/bin:${PATH}"
export PYTHONPATH="/workspace${PYTHONPATH:+:$PYTHONPATH}"
export PYTHONUNBUFFERED=1
exec /workspace/.venv/bin/python -m uvicorn app:asgi --host 0.0.0.0 --port 8080 --log-level info
