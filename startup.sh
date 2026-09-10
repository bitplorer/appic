#!/bin/sh
set -eu
cd /workspace
export PATH="/workspace/.venv/bin:/root/.local/bin:${PATH}"
export PYTHONPATH="${PYTHONPATH:-.}"
export PYTHONUNBUFFERED=1

if curl -fsS --max-time 2 http://127.0.0.1:8080/health >/dev/null 2>&1 \
  || curl -fsS --max-time 2 http://127.0.0.1:8080/ >/dev/null 2>&1; then
  exit 0
fi

if [ ! -x /workspace/.venv/bin/python ]; then
  uv venv /workspace/.venv --python /root/.local/share/uv/python/cpython-3.14-linux-x86_64-gnu/bin/python3.14
  /workspace/.venv/bin/uv pip install -e "/tmp/ux-compose[serve]" fastapi 2>/dev/null || \
    /workspace/.venv/bin/pip install -r /workspace/requirements.txt
fi

nohup /workspace/.venv/bin/python -m uvicorn app:asgi --host 0.0.0.0 --port 8080 \
  >/tmp/appic-uvicorn.log 2>&1 &
sleep 0.4
exit 0
