#!/bin/sh
# Restart contract: APPIC (ux-compose) on 0.0.0.0:8080
set -eu
cd /workspace
export PYTHONPATH="/workspace/.pydeps:/workspace/vendor/ux-compose-src:/workspace/vendor/specialists-src:/workspace:${PYTHONPATH:-}"
if curl -sf -o /dev/null --max-time 1 http://127.0.0.1:8080/api/health; then
  exit 0
fi
# :8081 is QA-only — a revive must never inherit a stale built-output preview.
node scripts/preview.mjs stop >/dev/null 2>&1 || true
PY="${PYTHON:-python3}"
if ! command -v "$PY" >/dev/null 2>&1; then
  PY=python3
fi
if [ ! -d /workspace/.pydeps/fastapi ]; then
  "$PY" -m pip install -q --target /workspace/.pydeps fastapi 'uvicorn[standard]' marko itsdangerous python-multipart || true
fi
nohup "$PY" -m uvicorn appic.server:app --host 0.0.0.0 --port 8080 \
  > /tmp/appic-uvicorn.log 2>&1 &
for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20; do
  if curl -sf -o /dev/null --max-time 1 http://127.0.0.1:8080/api/health; then
    exit 0
  fi
  sleep 0.4
done
exit 0
