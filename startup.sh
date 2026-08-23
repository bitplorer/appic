#!/bin/sh
# Restart contract: APPIC (ux-compose) on 0.0.0.0:8080
set -eu
cd /workspace
if curl -sf -o /dev/null http://127.0.0.1:8080/api/health; then
  exit 0
fi
export PYTHONPATH="/workspace/vendor/ux-compose-src:/workspace"
if [ ! -x /workspace/.venv/bin/uvicorn ]; then
  python3 -m venv /workspace/.venv
  /workspace/.venv/bin/pip install -q fastapi "uvicorn[standard]"
  /workspace/.venv/bin/pip install -q /tmp/ux-behavior /tmp/ux-motion /tmp/ux-channel/python || true
fi
nohup /workspace/.venv/bin/uvicorn appic.server:app --host 0.0.0.0 --port 8080 \
  > /tmp/appic-uvicorn.log 2>&1 &
for i in 1 2 3 4 5 6 7 8 9 10; do
  if curl -sf -o /dev/null http://127.0.0.1:8080/api/health; then
    exit 0
  fi
  sleep 0.4
done
exit 0
