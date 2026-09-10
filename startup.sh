#!/bin/sh
set -eu
cd /workspace
export PATH="/workspace/.venv/bin:/root/.local/bin:${PATH}"
export PYTHONPATH="/workspace${PYTHONPATH:+:$PYTHONPATH}"
export DEBUG="${DEBUG:-1}"
node scripts/preview.mjs stop || true
if curl -sf -o /dev/null --max-time 2 http://127.0.0.1:8080/; then
  exit 0
fi
if [ ! -x /workspace/.venv/bin/python ]; then
  uv venv /workspace/.venv --python 3.14
  /workspace/.venv/bin/pip install -r /workspace/requirements.txt
fi
/workspace/.venv/bin/python -m uvicorn app:asgi --host 0.0.0.0 --port 8080 >>/tmp/app-startup.log 2>&1 &
for i in 1 2 3 4 5 6 7 8 9 10; do
  if curl -sf -o /dev/null --max-time 1 http://127.0.0.1:8080/; then
    exit 0
  fi
  sleep 0.5
done
exit 0
