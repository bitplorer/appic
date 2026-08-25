# APPIC

**Intent. Presence. Caps.**

A nocturnal foundry OS authored in [ux-compose](https://github.com/bitplorer/ux-compose) — the pure-Python composition root for ux-dom, ux-behavior, ux-motion, and ux-channel.

No React. No Vue. No client runtime as source of truth. Server-authored hypermedia. Progressive L1→L3 with zero rewrite.

## For Grok Build

The copy-paste prompt (full public-API inventory, catalog mapping, product spec):

**[GROK_BUILD_PROMPT.md](GROK_BUILD_PROMPT.md)**

Deep dive of every ux-compose 0.1.0 feature the prompt was planned from:

**[FEATURE_INVENTORY.md](FEATURE_INVENTORY.md)**

Paste the prompt into Grok Build. It will author APPIC in Python with ux-compose only — no React / JSX / TSX — and publish back here.

## Surfaces (when the product is running)

| Surface | What to try |
|---|---|
| Table `/` | Pulse the house. Hold an intent. Sit a bench. |
| Atelier `/atelier` | Filter, sort, save, compare, look, add to bag. |
| Piece `/atelier/{sku}` | DirectoryRoutes dynamic segment. Share seat from the shelf. |
| Commission `/commission` | Four-step wizard. OTP `2048` is a Cap. Place is a Cap. |
| Bag `/bag` | Stepper, coupon Cap (`HOUSE` / `FLAX` / `TABLE`), review, checkout Cap. |
| Board `/board` | Move cards, undo, table bulk. |
| Studio `/studio` | Chat, typing presence, moderate Cap. |
| Lab `/lab` | Remaining 99%: tree, carousel, reorder, empty-retry, chips, inline, combobox, accordion, drawer, Morph-then-Play, share. |
| Lattice `/lattice` | Caps as seals. Intent as nucleus. Mint is a Cap. SurfaceBundle as stars. |
| Trace `/trace` | Live Ops log. Doctor. Isolation. Shortcuts. Bundle tables. |
| Ledger `/ledger` | Book a bench (Cap), WebAssets chip, wipe (Cap). |
| Command `⌘K` | Issue intents without leaving the table. |

## Laws kept

- **Isolation** — product modules never import `ux_channel` or CEK
- **Document SSoT** — one HTML shell (`document.py`)
- **XOR / Morph-then-Play** — `update_with(self, scene(...))`, Plans carry no `html=`
- **Cap Law** — checkout, book, redeem, wipe, verify, moderate, mint, reset through `App.mint_cap`
- **Encoding** — qualitative MorphState; magnitudes on RefState + stamp
- **WebAssets** — tokens in `assets/css/input.css`, Document links `/css/output.css`
- **DirectoryRoutes** — URL = filesystem; class name never in the path
- **Progressive Superpower** — L1 code unchanged at L3
- **`bind()`** preferred; `control()` remains the stringly hatch

## Run

Python ≥3.11. `ux-dom` wants 3.14; APPIC keeps the same tag call shape without it.

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
# product path (when app.py exists):
uxcompose build
uxcompose serve app:asgi --host 0.0.0.0 --port 8080
# fallback if the foundry is still on the package entry:
PYTHONPATH=vendor/ux-compose-src:. uvicorn appic.server:app --host 0.0.0.0 --port 8080
```

Doctor: `GET /api/doctor`. Health: `GET /api/health`. Surfaces: `GET /api/surfaces`.

```bash
uxcompose doctor . --no-fail
```
