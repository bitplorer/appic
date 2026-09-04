# APPIC

**Intent. Presence. Caps. Kit. Signal. Relay. Author. Notes. Chrome. Copy. Skin. Ship.**

A nocturnal foundry OS authored in [ux-compose](https://github.com/bitplorer/ux-compose)
`7ea3eb8813d280a975c4a41d23a2e2d4de40a506` (0.1.0 Clock A + ownable kit +
OverlayChrome + author door + attach notes + Typeahead hits-slot + serve-dev
split + Relay + copy press + doctor scan families + Presence cookbook +
**WebAssets skin + deploy providers + tunnel grammar**) — the
pure-Python composition root for ux-dom, ux-behavior, ux-motion, and ux-channel.

No React. No Vue. No JS/TS/TSX as source of truth. Server-authored
hypermedia. Progressive L1→L3 with zero rewrite. Page units have no HTTP verbs.
Payload type picks media type. **The kit is a house you own.** The copy press
is the ownership ritual — not a card. Skin is WebAssets. Ship is six providers.
Signal is a grammar you can feel. The author door is one. Attach notes refuse
silence. OverlayChrome is the edge primitive. Anchored popovers are a different
family. Doctor residuals expire by teaching. Presence is continuous.

`/skin` and `/deploy` are live rooms (2026-09-04): WebAssets ETag / first-token
CSS law, leftover `serve="webassets"` vs `dual_copy`, `prepare_deploy` six
providers as MorphState, prepare is Cap `ship.deploy`, tunnel `parse_provider`.
Home constellation names every door.

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
| `/` | Table — pulse, hold an intent, sit a bench, walk the constellation |
| `/enter` | Door — owned Login + OTP. Caps `auth.login` / `auth.otp` |
| `/desk` | Desk — Sidebar, Breadcrumb, Tabs, PullRefresh, Accordion, Command, Toast |
| `/house` | House — Typeahead, Combobox, Select, Dropdown, Sheet, Carousel, Table, Pagination, ContextMenu, ActionSheet. Anchored family lives here |
| `/visit` | Visit — Stepper, Plans, Calendar, Dialog |
| `/signal` | Signal — Wave 1 grammar (swipe, longpress, `input delay:`, handle `threshold:48`) |
| `/author` | Author — official `act` / `field` / `status` / `tick` / `maybe_*`. Posts `/act/{action}` |
| `/notes` | Notes — `AttachNote`, `attach_notes()`, `App.attach_notes` |
| `/overlay` | Chrome — OverlayChrome ids, swipe-on-dismiss, handle `threshold:48`, enter x=28 / y=32. Owned Dialog / Sheet / ActionSheet |
| `/copy` | Ownership — the copy press made visible. 23 stems + OverlayChrome-not-a-stem. `copy_component` / `find_app_root` / `KitCopyError` |
| `/skin` | WebAssets — `css_href`, ETag, first CSS token, leftover `serve="webassets"` vs `dual_copy` |
| `/deploy` | Ship — six providers, `prepare_deploy`, Cap `ship.deploy`, tunnel `parse_provider` |
| `/atelier` | Filter, sort, save, compare, look, add to bag. Presence cookbook on sort |
| `/atelier/{sku}` | DirectoryRoutes dynamic segment. No `get()`. |
| `/commission` | Four-step wizard. OTP `2048` and place are Caps |
| `/bag` | Stepper, coupon Caps `HOUSE` / `FLAX` / `TABLE`, checkout Cap |
| `/board` | Move cards, undo, bulk table |
| `/studio` | Chat, typing presence, moderate Cap |
| `/lab` | Remaining catalog floor |
| `/lattice` | Caps as seals, intent as nucleus |
| `/trace` | Live ops, doctor (hard + teaching), isolation, CSP, kit catalog, leftover teaching |
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

Full-utilisation (this generation) additions:

- **Skin** — `WebAssets`, `CSS_URL_PREFIX`, `OUTPUT_CSS_NAME`, ETag /
  Last-Modified, first-token CSS law. Walk it on `/skin`.
- **Ship** — `prepare_deploy` providers `docker` `fly` `render` `railway`
  `vps` `checklist`. `DeployResult`. Cap `ship.deploy`. Tunnel
  `parse_provider`. Walk it on `/deploy`. GET does not write files.
- **Constellation** — every public door on the Table.
- **No React / JS / TS / TSX** as product UI. uvicorn on `0.0.0.0:8080`.

If the prompt and the library disagree, **the library wins**.
