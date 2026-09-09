# APPIC

**Intent. Presence. Caps. Kit. Signal. Relay. Author. Notes. Chrome. Copy. Skin. Ship. Market. Forge.**

A constitution you can walk. A nocturnal foundry OS authored in [ux-compose](https://github.com/bitplorer/ux-compose)
`5bb7dc22c9c9a3b9a732a1d180f346165b623b90` (0.1.0, kit-81 cut) — the
pure-Python composition root for ux-dom, ux-behavior, ux-motion, and ux-channel.

No React. No Vue. No JS/TS/TSX as source of truth. Server-authored hypermedia.
Progressive L1→L3 with zero rewrite. Page units have no HTTP verbs. Payload
type picks media type. **The kit is a house you own — 81 stems.** The copy
press is the ownership ritual. Signal is a grammar you can feel. The author
door is one (`act` / `mark_dirty` / `optional_*`). Attach notes refuse silence.
OverlayChrome is the edge primitive. AlertDialog is interrupting. Doctor
residuals expire by teaching. Presence is continuous. Skin is WebAssets. Ship
is `prepare_deploy`. HMR is delivery. Tunnel waits for health. Product Cap
Host is `cek="require"`. Brand lives on `wrap=brand_wrap(...)`, never inside
`render()`. `/docs` is a product page. FastAPI Swagger stays off.

The Table is a **constellation**: rooms as named stars around the nucleus.
Sight is MorphState. Walk is Clock A.

## Run

Python **≥ 3.14**.

```bash
python3.14 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export PYTHONPATH="."
python -m uvicorn appic.server:app --host 0.0.0.0 --port 8080
```

Or the product CLI:

```bash
uxcompose serve dev
```

## Prompt

The Grok Build metaprompt lives in [`GROK_BUILD_PROMPT.md`](GROK_BUILD_PROMPT.md).
Copy everything below the line into Grok Build. Feature map against ux-compose
`main` (`5bb7dc22`), inventory 2026-09-09:
[`FEATURE_INVENTORY.md`](FEATURE_INVENTORY.md).

If the prompt and the library disagree, **the library wins**.
