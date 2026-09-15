#!/bin/sh
# Preview revive contract: probe 8080, start only if down, return fast.
set -eu
cd /workspace
export PATH="/workspace/.venv/bin:/root/.local/bin:${PATH}"
export PYTHONPATH="/workspace${PYTHONPATH:+:$PYTHONPATH}"
export PYTHONUNBUFFERED=1
export UXCOMPOSE_APP="${UXCOMPOSE_APP:-app:asgi}"

if curl -fsS --max-time 2 http://127.0.0.1:8080/ >/dev/null 2>&1; then
  exit 0
fi

if [ ! -x /workspace/.venv/bin/python ]; then
  uv python install 3.14
  uv venv /workspace/.venv --python 3.14
  uv pip install --python /workspace/.venv/bin/python -r /workspace/requirements.txt
fi

nohup /workspace/.venv/bin/python -m uvicorn app:asgi --host 0.0.0.0 --port 8080 \
  >/tmp/appic-uvicorn.log 2>&1 &

i=0
while [ "$i" -lt 80 ]; do
  if curl -fsS --max-time 1 http://127.0.0.1:8080/ >/dev/null 2>&1; then
    exit 0
  fi
  i=$((i + 1))
  sleep 0.25
done
exit 0
