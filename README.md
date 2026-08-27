# APPIC

**Intent. Presence. Caps.**

A nocturnal foundry OS authored in [ux-compose](https://github.com/bitplorer/ux-compose) 0.1.0 (Clock A) — the pure-Python composition root for ux-dom, ux-behavior, ux-motion, and ux-channel.

No React. No Vue. No client runtime as source of truth. Server-authored hypermedia. Progressive L1→L3 with zero rewrite. Page units have no HTTP verbs. Payload type picks media type.

## Run

```bash
export PYTHONPATH=".pydeps:vendor/ux-compose-src:vendor/specialists-src:."
python3 -m uvicorn app:asgi --host 0.0.0.0 --port 8080
```

Or the product CLI:

```bash
uxcompose serve app:asgi --host 0.0.0.0 --port 8080
```

## Surfaces

| Path | Room |
|------|------|
| `/` | Table — pulse, hold an intent, sit a bench |
| `/atelier` | Filter, sort, save, compare, look, add to bag |
| `/atelier/{sku}` | DirectoryRoutes dynamic segment. No `get()`. |
| `/commission` | Four-step wizard. OTP `2048` and place are Caps |
| `/bag` | Stepper, coupon Caps `HOUSE` / `FLAX` / `TABLE`, checkout Cap |
| `/board` | Move cards, undo, bulk table |
| `/studio` | Chat, typing presence, moderate Cap |
| `/lab` | Remaining catalog floor |
| `/lattice` | Caps as seals, intent as nucleus |
| `/trace` | Live ops, doctor, isolation, CSP |
| `/ledger` | Book a bench (Cap), WebAssets chip, wipe (Cap) |
| `/clocks` | Dual-clock room — GET vs action, three payload doors |
| `/health` | JSON page unit (`render()` returns a dict) |
| `/pulse` | Stream page unit (`render()` returns a generator) |

Command `⌘K` issues intents without leaving the table.

## Prompt

The Grok Build prompt that specifies this product lives in [`GROK_BUILD_PROMPT.md`](GROK_BUILD_PROMPT.md). Copy everything below the line into Grok Build. Feature map against ux-compose `main` (`0cc83cff`, 2026-08-26): [`FEATURE_INVENTORY.md`](FEATURE_INVENTORY.md).

Clock A corrections in this revision:

- Page units have **no HTTP verbs**. `get()` is gone.
- `render()` return value picks media type (HTML / JSON / stream / Response).
- Author Document wraps GET. Synthesized Document is mount-only.
- `App.boot("auto")` is Level 1. Channel attaches in `build()`.
- Dual-clock room, JSON health door, stream pulse door.
