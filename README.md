# APPIC

**Intent. Presence. Caps. Kit. Signal. Relay. Author. Notes. Chrome. Copy. Skin. Ship.**

A constitution you can walk. A nocturnal foundry OS authored in [ux-compose](https://github.com/bitplorer/ux-compose)
`fa2ddfe3852866702f8665069bb6152207b86c2e` (0.1.0, hard-deps cut) — the
pure-Python composition root for ux-dom, ux-behavior, ux-motion, and ux-channel.

No React. No Vue. No JS/TS/TSX as source of truth. Server-authored hypermedia.
Progressive L1→L3 with zero rewrite. Page units have no HTTP verbs. Payload
type picks media type. **The kit is a house you own.** The copy press is the
ownership ritual. Signal is a grammar you can feel. The author door is one
(`act` / `mark_dirty` / `optional_*`). Attach notes refuse silence.
OverlayChrome is the edge primitive. Doctor residuals expire by teaching.
Presence is continuous. Skin is WebAssets. Ship is `prepare_deploy`. HMR is
delivery. Tunnel waits for health. Product Cap Host is `cek="require"`.

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

## Surfaces

| Path | Room |
|------|------|
| `/` | Table — pulse, hold an intent, sight a constellation star |
| `/enter` | Door — owned Login + OTP |
| `/desk` | Desk — Sidebar, Command, pull to refresh |
| `/house` | House — anchored family (Typeahead, Combobox, Select, …) |
| `/visit` | Visit — Stepper, Plans, Dialog |
| `/signal` | Signal — Wave 1 grammar |
| `/author` | Author — official `act` / `mark_dirty` / `field` / `optional_*` |
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
`main` (`fa2ddfe`), inventory 2026-09-08:
[`FEATURE_INVENTORY.md`](FEATURE_INVENTORY.md).

If the prompt and the library disagree, **the library wins**.
