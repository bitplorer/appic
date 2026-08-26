# APPIC

**Intent. Presence. Caps.**

A nocturnal foundry OS authored in [ux-compose](https://github.com/bitplorer/ux-compose) — the pure-Python composition root for ux-dom, ux-behavior, ux-motion, and ux-channel.

No React. No Vue. No client runtime as source of truth. Server-authored hypermedia. Progressive L1→L3 with zero rewrite.

## Run

```bash
export PYTHONPATH=".pydeps:vendor/ux-compose-src:vendor/specialists-src:."
python3 -m uvicorn appic.server:app --host 0.0.0.0 --port 8080
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
| `/atelier/{sku}` | DirectoryRoutes dynamic segment |
| `/commission` | Four-step wizard. OTP `2048` and place are Caps |
| `/bag` | Stepper, coupon Caps `HOUSE` / `FLAX` / `TABLE`, checkout Cap |
| `/board` | Move cards, undo, bulk table |
| `/studio` | Chat, typing presence, moderate Cap |
| `/lab` | Remaining catalog floor |
| `/lattice` | Caps as seals, intent as nucleus |
| `/trace` | Live ops, doctor, isolation |
| `/ledger` | Book a bench (Cap), WebAssets chip, wipe (Cap) |

Command `⌘K` issues intents without leaving the table.

## Prompt

The Grok Build prompt that specifies this product lives in [`GROK_BUILD_PROMPT.md`](GROK_BUILD_PROMPT.md). Feature map: [`FEATURE_INVENTORY.md`](FEATURE_INVENTORY.md).
