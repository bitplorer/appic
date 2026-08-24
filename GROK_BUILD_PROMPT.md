# Grok Build prompt — APPIC on ux-compose (full inventory)

Copy everything below the line into Grok Build. Do not use React, Vue, JSX, TSX, Next, TanStack UI, Svelte, or a client SPA runtime. Author the product in Python with **ux-compose**. HTMX is never the architecture.

---

Build **APPIC**, a stunning nocturnal foundry OS, as a **complete product** (not a widget zoo) using **https://github.com/bitplorer/ux-compose** as the only web UI framework. Fully utilise every public name and every catalog pattern. Publish the running product to GitHub repo **appic** under the connected account (create the repo if missing).

## What ux-compose actually is

Thin pure-Python **composition + delivery** root. It harnesses four specialists and must **not** reimplement them:

| Specialist | Role | Unlock |
|---|---|---|
| **ux-dom** | Tag trees, Document SSoT, serialize, DirectoryRoutes | L0 |
| **ux-behavior** | `Component`, `MorphState`, `RefState`, `@action`, Ops | L1 |
| **ux-channel** | Intent → Cap → Result. Live authority. Behind `wire/` only | L2 |
| **ux-motion** | Scene Plans, presence, Morph-then-Play IR | L3 |

Progressive Superpower: the **same Component class** is correct at L1 (`dispatch`) and L3 (`use_channel` + `use_motion`). Zero rewrite.

PyPI / import / CLI: `ux-compose` / `ux_compose` / **`uxcompose`** (sole product lifecycle). Version `0.1.0`.

## Public author surface (do not invent names)

Import **only** from `ux_compose`. There is no public `ux.div` / `when` / `forall` / `Page`.

```
App, Component, MorphState, RefState, action,
bind, control, notify, update_with, morph_play,
Level, doctor, DoctorResult, build,
Surface, SurfaceBundle, SurfaceError,
mount_surfaces, scan_surfaces, validate_surfaces,
scene, fade, rise,          # None until ux-motion is installed
HAS_DOM, raw,
html, head, body, title, style, meta, link, script,
div, span, h1, h2, h3, p, a, button, form, input_,
ul, li, header, footer, aside, section, article, nav, main, label,
svg, path, rect, circle
```

If Python < 3.14 (ux-dom requires ≥3.14), keep the **same call shape** with a local tag kit. HTML strings remain valid. Do not invent a second namespace.

### App (composition root)

```
App.boot(name, *, strict_caps=False, level="auto"|0..3)
app.use_host("auto"|"fastapi"|"starlette"|"asgi"|"batteries")
app.use_dom(document=None)
app.use_behavior()
app.use_channel(asgi_app=...)     # Isolation door — never import ux_channel in product
app.use_motion()
app.use_cek(mode="adapt"|"require")
app.mint_cap(action, args)
app.submit_intent / submit_intent_async(..., mint=True)
app.add(*ComponentClasses)
app.mount(package_dir, asgi_app=..., base="routes", fail_closed=..., bind_pages=..., host=...)
app.dispatch("surface.verb", **args)   # offline-first, same surface as live
app.control(...)
app.doctor(paths, fail=False)
app.level / app.behavior
```

Locked product path: filesystem page units under `routes/` + `App.mount`. Stem matches class (`home.py` → `Home`). Class name never leaks into the URL. `≤1` page owner per file; extra renderables are fragments (no URL). Define-in-module only.

### Component contract

- `id` is the morph + motion target (default `ClassName.lower()`).
- `render()` returns a tag tree (or HTML string). Never a construct-time snapshot.
- `__render__` / `__async_render__` re-run live `render()`.
- `@action(caps=(...))` returns:
  1. `None` → auto-morph dirty MorphStates
  2. `list[Op]` → exact Ops (auto suppressed)
  3. Prefer `update_with(self, scene(...).enter("#id", rise.enter(ms=140)), extra_ops=[notify("…")])`
- Do **not** subclass ux-dom `Component` (MRO collides with tree verbs `add/remove/get/clear`).

### Helpers (must appear in product code)

| Helper | Law |
|---|---|
| `control("surface.verb", **args)` | Progressive attrs `data-ux-action` + `data-ux-arg-*` |
| `bind(self.verb, **args)` | Prefer when Behavior is present |
| `notify(message, level="info")` | One-shot toast Op |
| `update_with(self, plan=None, extra_ops=[…])` | Morph HTML from live `render()` (XOR-safe) |
| `morph_play("#id", plan)` | Morph-then-Play list of Ops |
| `tick(self)` | Flip qualitative `stamp` MorphState so RefState-only mutations morph |
| `maybe_plan` / `maybe_fade` / `maybe_stagger` / `maybe_share` | No-op when `scene is None` |

### Surfaces catalog

`scan_surfaces` → `validate_surfaces` (fail-closed id/path clashes) → `mount_surfaces` (Behavior.add + optional page router). `SurfaceBundle` exposes `surfaces`, `route_table`, `action_table`, `unit_registry`, `errors`, `sealed`.

### CLI (product lifecycle only)

```
uxcompose create-app myapp --level 1
uxcompose serve app:asgi --host 0.0.0.0 --port 8080 [--hmr] [--tunnel ngrok|cloudflare]
uxcompose deploy --provider docker|fly|render|railway|vps|checklist
uxcompose doctor . --no-fail
```

HMR (`/__uxcompose/hmr`) and tunnel live under **serve**, never as `Document.use`. Pure-dom tooling stays on `uxdom doctor|lint|build|profile`.

### Doctor

AST Isolation scan (`ux_channel` / `cek` / `MotionChannel` forbidden in product). Dual-Document heuristic. Reports level, capabilities, surfaces, routes, teaching. Expose `GET /api/doctor` and render the same evidence in Ledger + Trace.

---

## Hard laws (fail closed)

1. **Isolation.** Product modules never `import ux_channel`, `cek`, `cek_host`, `MotionChannel`. Live path only through `App.use_channel` / `use_motion` / `use_cek`.
2. **Document SSoT.** Exactly one HTML shell. Overlays are Components, not a second Document. HTMX is opt-in at Document only and stays **off**.
3. **XOR + Morph-then-Play.** Plans carry **no** `html=`. Morph first from `render()`, then `transition.play`. `scene.enter("#id", rise.enter())` — recipes only.
4. **Cap Law.** Protected verbs fail closed without a Channel-minted Cap. Host mints at the HTTP action door via `mint_cap` / `submit_intent(..., mint=True)`. After `use_channel`, `dispatch` is Host-internal; live verification is Intent.
5. **Encoding (Channel session plane refuses quantity MorphState).**

   | What | Where |
   |---|---|
   | Open / value / query / named step / named band / bool | `MorphState` |
   | Magnitude, lists, money, ISO dates, files, digits | `RefState` + `stamp = MorphState("idle")` |
   | One-shot message | `notify(...)` |
   | Domain stock / money / bookings | **Host store**, never the client plane |
   | Protected verb | `@action(caps=("orders.place",))` + live mint |

6. **Presence continuity.** Stable ids (`id="item-{sku}"`). `scene.stagger_in` on survivors. `scene.share(key, leave=, arrive=)` — share id is identity, not a CSS class. Leave and arrive must exist after morph.
7. **Cold import never pulls the wire.**
8. **No React / Vue / Svelte / Next / TanStack UI / JSX / TSX.** No client SPA as source of truth.

Serve on `0.0.0.0:8080`. Keep Grok `extensions.js` in the shell. Do not hide the Created-with-Grok pill. Vanilla preview-host bridge (postMessage `grok-preview-bridge` v1: hello / navigate / history / location / routes / ready).

---

## Install (progressive)

```
pip install "ux-compose @ git+https://github.com/bitplorer/ux-compose.git"
pip install "ux-behavior @ git+https://github.com/bitplorer/ux-behavior.git"
pip install "ux-motion @ git+https://github.com/bitplorer/ux-motion.git"
pip install "ux-channel @ git+https://github.com/bitplorer/ux-channel.git#subdirectory=python"
# ux-dom needs Python ≥3.14; if absent, local tag kit / HTML strings still L1-correct
pip install fastapi "uvicorn[standard]"
```

Boot:

```python
app = App.boot("APPIC", level="auto", strict_caps=False)
app.use_host("fastapi")
app.use_channel(asgi_app=asgi)
app.use_motion()
app.use_cek(mode="adapt")
bundle = app.mount(PACKAGE, asgi_app=asgi, base="routes", fail_closed=False, bind_pages=False)
```

Vendor `src/ux_compose` so the product boots if git installs fail. `PYTHONPATH=vendor/ux-compose-src:.`

---

## Catalog — 99% of product UI (every pattern must ship, in the product, not a zoo)

Each pattern is one `Component`. Map them into APPIC surfaces below. Do not leave a pattern unimplemented.

### Foundation (`examples/foundation.py`)
- **Counter** — RefState magnitude + MorphState stamp. Increment public. Reset is a Cap.
- **Toggle** — boolean MorphState.
- **Morph vs Ref (Planes)** — silent RefState does not morph without `tick`.

### Chrome (`chrome.py`, `modal.py`, `shell.py`)
- **Tabs** — one MorphState key; panels keep stable ids.
- **Accordion** — set of open ids (tuple of names).
- **Dropdown** — open flag + value.
- **Drawer** — presence flag; not a second Document.
- **Modal** — open MorphState, payload RefState, Cap confirm. Keep the node in the tree when closed so Motion can address it.
- **App shell** — named route + collapsed rail.
- **Breadcrumbs** — path as names.
- **Bottom nav** — mobile; Caps stay off chrome.
- **Popover** / **Overflow menu** — origin-aware; click-away is Host JS.

### Overlays (`overlays.py`)
- **Toasts**, **Confirm**, **Lightbox**, **Command palette**, **Banner**.

### Forms (`forms.py`, `fields.py`)
- **Signup** (validation public), **Wizard** (named steps), **Typeahead / Search**.
- **Choice group** (radio MorphState + checkbox set RefState).
- **Combobox** (query + value MorphState).
- **Date** (named window MorphState; ISO RefState).
- **File drop** (filenames RefState + stamp).
- **Slider** (magnitude RefState + stamp).
- **OTP** (digits RefState; **verify is a Cap**).
- **Password reveal** (bool MorphState; secret RefState).
- **Autosave** (dirty MorphState; draft RefState).
- **Limited note** (length derived from RefState).

### Collections (`lists.py`, `table_board.py`, `feeds.py`)
- **Shelf** filter+sort+stagger, **Optimistic list**, **Pagination**, **Undo snack**.
- **Data table** bulk select, **Kanban** optimistic move.
- **Carousel**, **Comments** (moderate is a Cap), **Timeline**.
- **Empty / loading / error / retry**, **Reorder**, **Activity feed**.

### Navigation (`navigation.py`)
- **Region swap** list ↔ detail on one id (`mode` MorphState, selected RefState).
- **Master / detail** split pane.

### Commerce (`cart.py`, `systems.py`, `commerce_more.py`)
- **Cart**, **Quantity stepper**, **Star rating** (named `one|two|…`, never MorphState(int)).
- **Wishlist**, **Coupon** (code MorphState; **redeem Cap**).
- **Checkout** named steps; **place Cap**.
- **Stock** qty silent, band named (`ok|low|out`).
- **Compare** max three ids.

### Live Caps (`live_caps.py`)
- Place without a Cap is refused. Host-mint succeeds. Product never imports Channel.

### Motion (`motion_xor.py`, `cookbooks/PRESENCE.md`)
- **Morph-then-Play hop** — `update_with(self, scene(...).enter(#id, rise.enter()))`.
- **Shared element** — `scene.share(key, leave=, arrive=, recipe=)`.
- Without ux-motion, `scene is None` and the same `@action` still morphs.

### Systems / ops (`systems.py`, `ops.py`)
- **Chat** (typing MorphState), **Inbox** (unread RefState), **Tree**, **Skeleton**.
- **Consent**, **Theme / density / motion names**, **Chips**, **Inline edit**.
- **Calendar** (month name, day RefState, **book Cap**).
- **Progress** (pct RefState, phase named).
- **Copy clip**, **Settings** (**wipe Cap**), **Offline banner**, **Presence peers**.
- **KPI** (values silent, stamp dirties), **Shortcuts** (same shape as the palette).

### Host proofs
- Document SSoT, FastAPI Isolation door, page-unit mount (`examples/page_unit_mount.py`).

---

## Product — APPIC (*Intent. Presence. Caps.*)

A private foundry for commissioning and collecting handmade objects. Editorial, expensive, abundant negative space, concentric radii.

**Palette.** Dark ink `#0c0d0b`, elevated `#141512`, surface `#1a1b18`, bone `#ebe6d8`, muted `#9a9488`, cool accent `#c8ccd4`, danger `#c17a6e`, ok `#8fa394`. No purple, gold, neon, gradient-blob slop. No emoji in chrome. Sparse monochrome SVG marks.

**Type.** Display **Fraunces** 500–600, body **Source Sans 3**, mono **IBM Plex Mono**. Fluid `clamp` titles. Tabular nums on money / KPI.

**Motion tokens.** `--motion-stagger 40ms` … `--motion-slow 400ms`, `--ease-out cubic-bezier(0.22,1,0.36,1)`. Honor `prefers-reduced-motion`. Density + motion names on `<body>`.

### Surfaces (all live, all morph)

| Path | Unit | Patterns it must exercise |
|---|---|---|
| `/` Table | `Home` | Pulse counter+stamp, intent field, KPI, presence, manifesto, shortcuts teaser |
| `/atelier` | `Atelier` | Shelf filter/sort/stagger, wishlist, compare≤3, lightbox, rating, stock band, region swap list↔detail, add-to-bag + `scene.share` |
| `/commission` | `Commission` | 4-step wizard + radio/checkbox/slider/date/file/password/autosave/limited note/OTP Cap `identity.verify` / place Cap `orders.place` |
| `/bag` | `Bag` | Lines on Host, stepper, coupon Cap `orders.coupon` (`HOUSE`/`FLAX`/`TABLE`), confirm modal, checkout Cap `orders.place`, Morph-then-Play |
| `/board` | `Board` | Kanban optimistic + undo + data table bulk. Move public |
| `/studio` | `Studio` | Chat typing, inbox unread, comments moderate Cap `comments.moderate`, timeline, presence peers |
| `/ledger` | `Ledger` | Calendar book Cap `calendar.book`, progress, copy, locale/density/motion/consent/offline, doctor, wipe Cap `settings.wipe` |
| `/lab` | `Lab` | **Remaining 99% as a working floor** — tabs of house/fields/chrome/motion: tree, carousel, reorder, empty-retry, activity, chips, inline edit, combobox, accordion, dropdown, drawer, popover, overflow, skeleton, motion hop, share seat |
| `/trace` | `Trace` | **Radical: the document showing its own Results of Ops.** Live Ops log (RefState + stamp), doctor capabilities as chips, Isolation evidence, level badge, shortcuts, copy a row |
| Chrome | `Toasts`, `Palette`, `Banner`, `Drawer` | Command `⌘K` as first-class intent door; line banner; bag-peek drawer; toast plane |

### Control plane

- Progressive enhancer JS: POST `/action/{name}`, morph `#surface` with Idiomorph (else outerHTML). Full page GET still works without JS.
- Action door: Cap-suffixed verbs (`checkout`, `redeem`, `book`, `verify`, `wipe`, `moderate`, `next`, `place`, `reset`) mint then invoke.
- Every successful action **appends an Op row** to Host.trace (kind `morph|cap|notify`). Trace renders that log. This is the radical instrument: Ops-as-data, visible.

### Caps (real, fail closed)

`orders.place` · `orders.coupon` · `identity.verify` · `calendar.book` · `settings.wipe` · `comments.moderate`

### Quality

- Mobile 390px: no overflow, 44px targets, wrap nav, bottom nav.
- Offline banner when Host.online is false; public morphs still run.
- Custom `public/og.jpg` 1200×630, `public/favicon.svg` hand-authored, `src/lib/og/site.json` `{ "title": "APPIC", "card": "custom", "color": "0c0d0b" }`.
- `GET /api/health` and `GET /api/doctor`. `python -m ux_compose.cli doctor --no-fail` stays green (Isolation scan of the product package).

Ship a running foundry, not a gallery of unfinished cards. Every `@action` mutates state and morphs. Caps are real. Motion degrades. Isolation holds.
