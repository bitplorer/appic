#!/bin/sh
# Restart contract: APPIC (ux-compose) on 0.0.0.0:8080
set -eu
cd /workspace
export PYTHONPATH="/workspace/.pydeps:/workspace/vendor/ux-compose-src:/workspace:${PYTHONPATH:-}"
if curl -sf -o /dev/null --max-time 1 http://127.0.0.1:8080/api/health; then
  exit 0
fi
if [ ! -d /workspace/.pydeps/fastapi ]; then
  python3 -m pip install -q --target /workspace/.pydeps fastapi 'uvicorn[standard]' || true
fi
nohup python3 -m uvicorn appic.server:app --host 0.0.0.0 --port 8080 \
  > /tmp/appic-uvicorn.log 2>&1 &
for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16; do
  if curl -sf -o /dev/null --max-time 1 http://127.0.0.1:8080/api/health; then
    exit 0
  fi
  sleep 0.4
done
exit 0
