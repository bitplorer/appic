# APPIC

**Intent. Presence. Caps. Kit. Signal.**

A nocturnal foundry OS authored in [ux-compose](https://github.com/bitplorer/ux-compose) `17e652a6` (0.1.0 Clock A + ownable kit) — the pure-Python composition root for ux-dom, ux-behavior, ux-motion, and ux-channel.

No React. No Vue. No client runtime as source of truth. Server-authored hypermedia. Progressive L1→L3 with zero rewrite. Page units have no HTTP verbs. Payload type picks media type. **The kit is a house you own.** Signal is a grammar you can feel.

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
| `/enter` | Door — owned Login + OTP. Caps `auth.login` / `auth.otp` |
| `/desk` | Desk — Sidebar, Breadcrumb, Tabs, PullRefresh, Accordion, Command, Toast |
| `/house` | House — Typeahead, Combobox, Select, Dropdown, Sheet, Carousel, Table, Pagination, ContextMenu, ActionSheet |
| `/visit` | Visit — Stepper, Plans, Calendar, Dialog |
| `/signal` | Signal — Wave 1 grammar (swipe, longpress, input delay:) |
| `/atelier` | Filter, sort, save, compare, look, add to bag |
| `/atelier/{sku}` | DirectoryRoutes dynamic segment. No `get()`. |
| `/commission` | Four-step wizard. OTP `2048` and place are Caps |
| `/bag` | Stepper, coupon Caps `HOUSE` / `FLAX` / `TABLE`, checkout Cap |
| `/board` | Move cards, undo, bulk table |
| `/studio` | Chat, typing presence, moderate Cap |
| `/lab` | Remaining catalog floor |
| `/lattice` | Caps as seals, intent as nucleus |
| `/trace` | Live ops, doctor, isolation, CSP, kit catalog |
| `/ledger` | Book a bench (Cap), WebAssets chip, wipe (Cap) |
| `/clocks` | Dual-clock room — GET vs action, three payload doors |
| `/health` | JSON page unit (`render()` returns a dict) |
| `/pulse` | Stream page unit (`render()` returns a generator) |

Command `⌘K` issues intents without leaving the table.

## Prompt

The Grok Build prompt that specifies this product lives in [`GROK_BUILD_PROMPT.md`](GROK_BUILD_PROMPT.md). Copy everything below the line into Grok Build. Feature map against ux-compose `main` (`17e652a6`, 2026-08-27): [`FEATURE_INVENTORY.md`](FEATURE_INVENTORY.md).

Kit-era additions in this revision:

- **23 ownable kit stems** copied under `components/` (shadcn-style). Host seams overridden in `appic/owned.py`.
- **Nook rooms** — Door, Desk, House, Visit — every kit card sits in a real room.
- **Signal room** — Wave 1 grammar made visible: swipe, longpress, `input delay:`.
- **Clock A doors** — `/health` JSON, `/pulse` stream, `/clocks` dual-clock room.
- `slide.enter` helper for sheet / action-sheet presence.
