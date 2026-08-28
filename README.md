# APPIC

**Intent. Presence. Caps. Signal.**

A nocturnal foundry OS authored in [ux-compose](https://github.com/bitplorer/ux-compose) `17e652a6` (0.1.0 Clock A + ownable kit) — the pure-Python composition root for ux-dom, ux-behavior, ux-motion, and ux-channel.

No React. No Vue. No client runtime as source of truth. Server-authored hypermedia. Progressive L1→L3 with zero rewrite. Page units have no HTTP verbs. Payload type picks media type. The kit is chrome you own.

## Run

```bash
export PYTHONPATH=".pydeps:vendor/ux-compose-src:vendor/specialists-src:."
python3 -m uvicorn app:asgi --host 0.0.0.0 --port 8080
```

Or the product CLI:

```bash
uxcompose serve app:asgi --host 0.0.0.0 --port 8080
uxcompose add --list
uxcompose doctor . --no-fail
```

## Prompt

The Grok Build prompt that specifies this product lives in [`GROK_BUILD_PROMPT.md`](GROK_BUILD_PROMPT.md). Copy everything below the line into Grok Build.

Feature map against ux-compose `main` (`17e652a6`, 2026-08-27): [`FEATURE_INVENTORY.md`](FEATURE_INVENTORY.md).

This revision adds what Clock A + 0.1.0 left on the table:

- **Ownable kit** — all 23 stems copied via `uxcompose add`, restyled, seamed
- **Wave 1 Signal grammar** — swipe / longpress / `input delay:` with no kit JS
- **`slide`** on the public motion surface
- Ceremonial `/door` (Login + OTP Caps, not Grok accounts)
- `/signal` as a first-class room

Clock A remains law: no HTTP verbs on page units; `render()` return value picks media type; author Document wraps GET.
