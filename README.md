# APPIC

**Intent. Presence. Caps. Kit. Signal. Relay. Author. Notes. Chrome. Copy. Skin. Ship.**

A nocturnal foundry OS authored in [ux-compose](https://github.com/bitplorer/ux-compose)
`7ea3eb8813d280a975c4a41d23a2e2d4de40a506` (0.1.0) — the pure-Python composition
root for ux-dom, ux-behavior, ux-motion, and ux-channel.

No React. No Vue. No JS/TS/TSX as source of truth. Server-authored hypermedia.
Progressive L1→L3 with zero rewrite. Page units have no HTTP verbs. Payload
type picks media type. **The kit is a house you own.** The copy press is the
ownership ritual. Signal is a grammar you can feel. The author door is one.
Attach notes refuse silence. OverlayChrome is the edge primitive. Doctor
residuals expire by teaching. Presence is continuous. Skin is WebAssets. Ship
is `prepare_deploy`. HMR is delivery. Tunnel waits for health.

The Table is a **constellation**: rooms as named stars around the nucleus.
Sight is MorphState. Walk is Clock A.

## Run

```bash
export PYTHONPATH=".pydeps:vendor/ux-compose-src:vendor/specialists-src:."
python3 -m uvicorn appic.server:app --host 0.0.0.0 --port 8080
```

Or the product CLI:

```bash
uxcompose serve dev
```

## Surfaces

| Path | Room |
|------|------|
| `/` | Table — pulse, hold an intent, sight a constellation star |
| `/enter` | Door — owned Login + OTP |
| `/desk` | Desk — Sidebar, Command, pull to refresh |
| `/house` | House — anchored family (Typeahead, Combobox, Select, …) |
| `/visit` | Visit — Stepper, Plans, Dialog |
| `/signal` | Signal — Wave 1 grammar |
| `/author` | Author — official `act` / `tick` / `field` / `maybe_*` |
| `/notes` | Notes — AttachNote |
| `/overlay` | Chrome — OverlayChrome edge family |
| `/copy` | Press — copy_component (not a card) |
| `/skin` | Skin — WebAssets |
| `/deploy` | Ship — six providers |
| `/atelier` | Presence cookbook on sort |
| `/commission` | Four-step wizard |
| `/bag` | Coupon + checkout Caps |
| `/board` | Kanban, undo, bulk |
| `/studio` | Chat, typing presence |
| `/lab` | Remaining catalog |
| `/lattice` | Caps as seals |
| `/trace` | Doctor (hard + teaching) |
| `/ledger` | Book a bench |
| `/clocks` | GET vs action |
| `/relay` | Three serve clocks |
| `/health` | JSON page unit |
| `/pulse` | Stream page unit |

Command `⌘K` issues intents without leaving the table.

## Prompt

The Grok Build metaprompt lives in [`GROK_BUILD_PROMPT.md`](GROK_BUILD_PROMPT.md).
Copy everything below the line into Grok Build. Feature map against ux-compose
`main` (`7ea3eb8`), refreshed 2026-09-05: [`FEATURE_INVENTORY.md`](FEATURE_INVENTORY.md).

If the prompt and the library disagree, **the library wins**.
