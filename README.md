# APPIC

**Intent. Presence. Caps. Kit. Signal. Relay. Author. Notes. Chrome.**

A nocturnal foundry OS authored in [ux-compose](https://github.com/bitplorer/ux-compose)
`7ea3eb8813d280a975c4a41d23a2e2d4de40a506` (0.1.0 Clock A + ownable kit +
OverlayChrome + author door + attach notes + Typeahead hits-slot + serve-dev
split + Relay) — the pure-Python composition root for ux-dom, ux-behavior,
ux-motion, and ux-channel.

No React. No Vue. No client runtime as source of truth. Server-authored
hypermedia. Progressive L1→L3 with zero rewrite. Page units have no HTTP verbs.
Payload type picks media type. **The kit is a house you own.** Signal is a
grammar you can feel. The author door is one. Attach notes refuse silence.
OverlayChrome is the edge primitive. Anchored popovers are a different family.

## Run

```bash
export PYTHONPATH=".pydeps:vendor/ux-compose-src:vendor/specialists-src:."
python3 -m uvicorn app:asgi --host 0.0.0.0 --port 8080
```

Or the product CLI:

```bash
uxcompose serve dev
```

## Surfaces

| Path | Room |
|------|------|
| `/` | Table — pulse, hold an intent, sit a bench |
| `/enter` | Door — owned Login + OTP. Caps `auth.login` / `auth.otp` |
| `/desk` | Desk — Sidebar, Breadcrumb, Tabs, PullRefresh, Accordion, Command, Toast |
| `/house` | House — Typeahead, Combobox, Select, Dropdown, Sheet, Carousel, Table, Pagination, ContextMenu, ActionSheet. Anchored family lives here |
| `/visit` | Visit — Stepper, Plans, Calendar, Dialog |
| `/signal` | Signal — Wave 1 grammar (swipe, longpress, `input delay:`, handle `threshold:48`) |
| `/author` | Author — official `act` / `field` / `status` / `tick` / `maybe_*`. Posts `/act/{action}` |
| `/notes` | Notes — `AttachNote`, `attach_notes()`, `App.attach_notes` |
| `/overlay` | Chrome — OverlayChrome ids, swipe-on-dismiss, handle `threshold:48`, enter x=28 / y=32. Owned Dialog / Sheet / ActionSheet |
| `/atelier` | Filter, sort, save, compare, look, add to bag |
| `/atelier/{sku}` | DirectoryRoutes dynamic segment. No `get()`. |
| `/commission` | Four-step wizard. OTP `2048` and place are Caps |
| `/bag` | Stepper, coupon Caps `HOUSE` / `FLAX` / `TABLE`, checkout Cap |
| `/board` | Move cards, undo, bulk table |
| `/studio` | Chat, typing presence, moderate Cap |
| `/lab` | Remaining catalog floor |
| `/lattice` | Caps as seals, intent as nucleus |
| `/trace` | Live ops, doctor, isolation, CSP, kit catalog, leftover teaching |
| `/ledger` | Book a bench (Cap), WebAssets chip, wipe (Cap) |
| `/clocks` | Dual-clock room — GET vs action, three payload doors |
| `/relay` | Three serve clocks. Soft morph. restart-channel as a named drop |
| `/health` | JSON page unit (`render()` returns a dict) |
| `/pulse` | Stream page unit (`render()` returns a generator) |

Command `⌘K` issues intents without leaving the table.

## Prompt

The Grok Build prompt that specifies this product lives in
[`GROK_BUILD_PROMPT.md`](GROK_BUILD_PROMPT.md). Copy everything below the line
into Grok Build. Feature map against ux-compose `main` (`7ea3eb8`):
[`FEATURE_INVENTORY.md`](FEATURE_INVENTORY.md).

Architecture-era (ADR 0004) additions:

- **23 ownable kit stems** copied under `components/` (shadcn-style). Host seams overridden in `appic/owned.py`.
- **`components/overlay.py`** — OverlayChrome is **not** a catalog stem. Copy it with the widgets.
- **Nook rooms** — Door, Desk, House, Visit — every kit card sits in a real room.
- **Signal room** — Wave 1 grammar made visible, including handle `click swipe.down swipe.vertical threshold:48`.
- **Typeahead hits-slot law** — live Results morph `#typeahead-hits` only. Later input aborts the in-flight Intent.
- **Clock A doors** — `/health` JSON, `/pulse` stream, `/clocks` dual-clock room.
- **Relay room** — `serve dev` / `serve prod` / `restart-channel`. Soft morph first.
- **Author door** — official `act` / `field` / `status` / `tick` / `maybe_*` as a walkable room. POST `/act/{name}` aliases `/action/{name}`. No private `_tick`.
- **Notes room** — attach step-downs made visible. Per-App notebook vs process notebook. Dual-write.
- **OverlayChrome** — one edge primitive. Dialog / Sheet / ActionSheet take ids, dismiss grammar, and the open plan from it. Enter distances: right sheet `x=28`, bottom actionsheet `y=32`.
- **Two overlay families** — edge (Dialog / Sheet / ActionSheet) vs anchored (Command / Dropdown / ContextMenu / Combobox / Select). Do not mix.
- **Leftovers expire by teaching** — doctor flags kit-imports, `host="batteries"`, teaching `App.mount` as the product path, root swipe.

If the prompt and the library disagree, **the library wins**.
