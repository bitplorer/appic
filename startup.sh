#!/bin/sh
set -eu
cd /workspace
export PATH="/workspace/.venv/bin:/root/.local/bin:${PATH}"
export PYTHONPATH="${PYTHONPATH:-.}"
export PYTHONUNBUFFERED=1
PY314="/root/.local/share/uv/python/cpython-3.14-linux-x86_64-gnu/bin/python3.14"

if curl -fsS --max-time 2 http://127.0.0.1:8080/health >/dev/null 2>&1 \
  || curl -fsS --max-time 2 http://127.0.0.1:8080/ >/dev/null 2>&1; then
  exit 0
fi

if [ ! -x /workspace/.venv/bin/python ]; then
  command -v uv >/dev/null 2>&1 || true
  uv python install 3.14 >/dev/null 2>&1 || true
  uv venv /workspace/.venv --python "$PY314"
  uv pip install --python /workspace/.venv/bin/python -r /workspace/requirements.txt \
    || uv pip install --python /workspace/.venv/bin/python -e "/tmp/ux-compose[serve]" fastapi "uvicorn[standard]"
fi

nohup /workspace/.venv/bin/python -m uvicorn app:asgi --host 0.0.0.0 --port 8080 \
  >/tmp/appic-uvicorn.log 2>&1 &
sleep 0.6
exit 0
