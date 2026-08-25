# Grok Build prompt — APPIC on ux-compose 0.1.0

Copy **everything below the line** into Grok Build. Do not use React, Vue, JSX, TSX, Next, TanStack UI, Svelte, Solid, HTMX-as-architecture, or a client SPA runtime as the product. Author in Python with **[ux-compose](https://github.com/bitplorer/ux-compose)**. Publish the running product to GitHub repo **appic** under the connected account (create the repo if missing; replace stale files).

---

Build **APPIC** — a stunning nocturnal foundry OS — as a **complete product** (not a widget zoo) using **https://github.com/bitplorer/ux-compose @ main** as the only web UI framework. Fully utilise **every public name** in `ux_compose.__all__` and every catalog pattern in `examples/`. Ship a running foundry, not a gallery of unfinished cards.

Read the library first. Clone or vendor `src/ux_compose` from that repo. If code and this prompt disagree, **the library wins**. Do not invent APIs.

## 0. Non-negotiable

- **No React / Vue / Svelte / Next / TanStack UI / JSX / TSX / `.tsx` product UI.** No client SPA as source of truth.
- **No HTMX architecture.** `use_htmx=False`. HTMX is a Document opt-in and stays **off**.
- Public imports are `from ux_compose import …` only. There is no `ux.div` / `when` / `forall` / `Page`.
- Product modules **never** `import ux_channel`, `cek`, `cek_host`, `cek_surface`, `MotionChannel`.
- Serve on `0.0.0.0:8080`. Keep Grok `extensions.js` in the shell. Do not hide the Created-with-Grok pill. Vanilla preview-host bridge (`postMessage` `grok-preview-bridge` v1: hello / navigate / history / location / routes / ready).
- Canonical product path is what `uxcompose create-app` writes. Deploy looks for `app.py`. Default ASGI is `app:asgi`.

## 1. What ux-compose actually is

Thin pure-Python **composition + delivery** root. It harnesses four specialists and must **not** reimplement them:

| Specialist | Role | Unlock | Install |
|---|---|---|---|
| **ux-dom** | Tag trees, Document SSoT, serialize, className, `<link>`, package static | L0 | Python ≥3.14 · `pip install "ux-dom @ git+https://github.com/bitplorer/ux-dom.git"` |
| **ux-behavior** | `Component`, `MorphState`, `RefState`, `@action`, Ops | L1 | `pip install "ux-behavior @ git+https://github.com/bitplorer/ux-behavior.git"` |
| **ux-channel** | Intent → Cap → Result. Behind compose `wire/` only | L2 | `pip install "ux-channel @ git+https://github.com/bitplorer/ux-channel.git#subdirectory=python"` |
| **ux-motion** | Scene Plans, presence, Morph-then-Play | L3 | `pip install "ux-motion @ git+https://github.com/bitplorer/ux-motion.git"` |

Progressive Superpower: the **same Component class** is correct at L1 (`dispatch`) and L3 (`use_channel` + `use_motion`). Zero rewrite. Pin `level=1` until Channel is intentional, then unlock — do not fork the class.

PyPI / import / CLI: `ux-compose` / `ux_compose` / **`uxcompose`**. Version `0.1.0`. Python ≥3.11 (ux-dom wants 3.14). If Python < 3.14, keep the **same tag call shape** with a local tag kit; HTML strings remain valid; `HAS_DOM` may be false.

Install:

```
pip install "ux-compose @ git+https://github.com/bitplorer/ux-compose.git"
pip install "ux-behavior @ git+https://github.com/bitplorer/ux-behavior.git"
pip install "ux-motion @ git+https://github.com/bitplorer/ux-motion.git"
pip install "ux-channel @ git+https://github.com/bitplorer/ux-channel.git#subdirectory=python"
pip install fastapi "uvicorn[standard]"
```

Vendor `src/ux_compose` so the product boots if git installs fail. `PYTHONPATH=vendor/ux-compose-src:.`

## 2. Public author surface (do not invent names)

Every name below **must appear in product source** (import, call, or render evidence). Local helpers (`tick`, `maybe_plan`) are product code, not library APIs.

```
App, build, WebAssets,
DirectoryRoutes, DirectoryASGI, RouterHooks,
Surface, SurfaceBundle, SurfaceError,
mount_surfaces, scan_surfaces, validate_surfaces,
Component, MorphState, RefState, action,
bind, control, notify, update_with, morph_play,
Level, doctor, DoctorResult,
scene, fade, rise,          # None until ux-motion is installed
HAS_DOM, raw,
html, head, body, title, style, meta, link, script,
div, span, h1, h2, h3, p, a, button, form, input_,
ul, li, header, footer, aside, section, article, nav, main, label,
svg, path, rect, circle
```

Also use (from compose submodules, never from `ux_channel`):

```
ActionInfo, BuildResult, RouteRecord,
DirectoryRoutesError, HMR_PATH, attach_hmr, client_script_tag,
IsolationViolation, CSS_URL_PREFIX, OUTPUT_CSS_NAME
```

Optional render-only kit (no Ops): `from ux_dom.ui import Button, Card, CardHeader, CardTitle, CardContent`. Use it on **one** surface (Ledger tokens) to prove the path; the rest of the product stays `ux_compose` tags.

### App

```
App.boot(name, *, strict_caps=False, level="auto"|0..3)
app.use_host("auto"|"fastapi"|"starlette"|"asgi")   # batteries leftover — do not use
app.use_dom(document=None)
app.use_behavior()
app.use_channel(asgi_app=...)     # Isolation door
app.use_motion()
app.use_cek(mode="adapt")         # degrade if missing; never mode=require in this product
app.mint_cap(action, args)
app.submit_intent / submit_intent_async(..., mint=True)
app.add(*ComponentClasses)
app.mount(package_dir, asgi_app=..., base="routes", fail_closed=..., bind_pages=...,
          on_surface=..., host=...)
app.dispatch("surface.verb", **args)
app.control(...)
app.doctor(paths, fail=False)
app.level / app.behavior
```

### build()

Locked composition façade. Host + live set **only** here (Invisible Strategy).

```python
from pathlib import Path
from ux_compose import build
from document import document
from settings import webassets

PACKAGE = Path(__file__).resolve().parent
app, asgi, bundle = build(
    PACKAGE,
    name="APPIC",
    host="auto",
    live="auto",
    level="auto",
    base="routes",
    fail_closed=False,   # teach errors in Ledger rather than crash boot
    use_htmx=False,
    document=document,
)
asgi = webassets.mount_css(asgi)
```

`BuildResult` exposes `.app` / `.asgi` / `.bundle`. Export `asgi` for uvicorn.

### Component

- `id` is the morph + motion target (default `ClassName.lower()`).
- `render()` returns a tag tree (or HTML string). Never a construct-time snapshot.
- `__render__` / `__async_render__` re-run live `render()`. Use `__async_render__` on at least one page GET (streaming-capable).
- `@action(caps=())` public. Non-empty caps need a live Cap or fail closed.
- Return: `None` (auto-morph dirty MorphStates) **or** `list[Op]`. Prefer `update_with(self, plan, extra_ops=[notify(...)])`.
- **Do not subclass ux-dom `Component`** (MRO collides with tree verbs `add/remove/get/clear`).

### Helpers

| Helper | Law |
|---|---|
| `bind(self.verb, **args)` | Preferred. Symbol-safe. Also `self.verb.ui(**args)`. Must appear on Pulse + Lattice mint. |
| `control("surface.verb", **args)` | Stringly hatch: `data-ux-action` + `data-ux-arg-*`. Use where you have no method object. |
| `notify(message, level="info")` | One-shot toast Op. |
| `update_with(self, plan=None, extra_ops=[…], strategy="idiomorph")` | Morph HTML from live `render()`. XOR-safe. |
| `morph_play("#id", plan)` | Morph-then-Play list. Must appear once (Lab motion hop). |

## 3. Product filesystem (create-app layout — locked)

```
app.py                 # composition root: build() + WebAssets.mount_css + extra host routes
settings.py            # BASE_DIR, DEBUG, WebAssets.from_app_root(..., dry_run=False)
document.py            # ONE Document + .use(XElement(), Csp.auto()) + page() + link /css/output.css
requirements.txt
assets/css/input.css   # tokens + @source of app.py and routes/**/*.py
assets/static/file/css/output.css   # uxcompose build output (hand-authored fallback if CLI missing)
routes/
  home.py              # class Home → /
  atelier.py           # /atelier
  atelier/
    [sku].py           # class Sku → /atelier/{sku}   DirectoryRoutes dynamic segment
  commission.py
  bag.py
  board.py
  studio.py
  ledger.py
  lab.py
  lattice.py
  trace.py
  (chrome)/            # route GROUP — no URL segment
    toasts.py          # fragment, not a page
  _marks.py            # private — skipped
public/favicon.svg
public/og.jpg          # 1200×630, custom
src/lib/og/site.json   # { "title": "APPIC", "card": "custom", "color": "0c0d0b" }
vendor/ux-compose-src/ux_compose/   # vendored library
```

Page-unit law: stem matches class (`home.py` → `Home`). Class name never in the URL. `≤1` page owner per file. Extra renderables are fragments. Define-in-module only. `[sku]` → `{sku}`. `(chrome)` is skipped in the path. `_` prefix skipped.

`RouterHooks.resolve_unit` feeds live Behavior instances into synthetic GETs. Prove it: atelier detail `[sku].py` has **no** explicit `get` so resolve_unit runs. One other page (Trace) may define explicit `get` to prove the bypass.

`on_surface` callback appends every mounted Surface to Host.trace as kind `surface`. `RouterHooks.on_route` (via mount) is evidence in Trace.

Scan path used in product (not only via `build`):

```python
found = scan_surfaces(PACKAGE, base_directory="routes")
validate_surfaces(found)
bundle = mount_surfaces(...)   # or rely on build()/app.mount — still import these names
```

Render `bundle.surfaces`, `bundle.route_table`, `bundle.action_table`, `bundle.unit_registry`, `bundle.sealed` on **Trace** and **Lattice**.

## 4. Hard laws (fail closed)

1. **Isolation.** Product modules never import the wire. Live path only through `App.use_channel` / `use_motion` / `use_cek`. `doctor` AST-scan of the product package stays green (`--no-fail` still prints teaching).
2. **Document SSoT.** Exactly one `Document(...)` in product files (`document.py`). Overlays are Components. Keep overlay nodes in the tree when closed so Motion can address them.
3. **XOR + Morph-then-Play.** Plans carry **no** `html=`. Morph first from `render()`, then `transition.play`. `scene.enter("#id", rise.enter())` — recipes only. `morph_play` still obeys XOR.
4. **Cap Law.** Protected verbs fail closed without a Channel-minted Cap. Host mints at the HTTP action door: Cap-suffixed verbs call `app.mint_cap` then `app.dispatch` / `submit_intent(..., mint=True)`.
5. **Encoding.** Qualitative `MorphState`. Magnitudes/lists/money/ISO/files/digits on `RefState` + `stamp = MorphState("idle")`. Domain stock/money/bookings on **Host store**. Channel session plane refuses quantity MorphState — teach the live-safe form so L2 is zero rewrite.
6. **Presence continuity.** Stable ids (`id="item-{sku}"`). `scene.stagger_in` on survivors. `scene.share(key, leave=, arrive=)` — share id is identity, not a CSS class. Leave and arrive must exist after morph.
7. **Cold import never pulls the wire.**
8. **CSS.** No CSS or client JS inside Python strings. No `style(raw(CSS))`. No Tailwind CDN. Tokens in `assets/css/input.css`. Document links `/css/output.css`. `WebAssets.mount_css` serves it. `uxcompose build` is the compiler path; if the Tailwind CLI is missing, ship a complete hand-authored `output.css` that covers every utility you used **and** still call `WebAssets`.
9. **HMR / tunnel** are `uxcompose serve` delivery, not `Document.use`. Expose `HMR_PATH` (`/__uxcompose/hmr`) as a chip on Trace. Do not attach HMR in production.
10. **No invented library names.**

## 5. CLI the product must honor

```
uxcompose create-app myapp --name APPIC --level auto --host auto
uxcompose build [--watch] [--no-minify] [--skip-tailwind] [--skip-import] [--app app:asgi]
uxcompose serve app:asgi --host 0.0.0.0 --port 8080 [--no-reload --hmr --watch assets --watch routes]
uxcompose serve app:asgi --tunnel ngrok|cloudflare
uxcompose deploy --provider docker|fly|render|railway|vps|checklist
uxcompose doctor . --no-fail
```

Ship `app.py` so `uxcompose serve app:asgi` and `uxcompose deploy --provider docker` are not a lie. Also keep a sandbox `startup.sh` that binds `0.0.0.0:8080`.

Host extra routes on the ASGI app `build()` returned (do not create a second app):

- `POST /action/{name}` — progressive enhancer. Cap-suffixed verbs mint then invoke. Morph `#surface` with Idiomorph (else outerHTML). Full page GET still works without JS.
- `GET /api/health` · `GET /api/doctor` (same evidence as Ledger + Trace)
- `GET /api/surfaces` — `bundle` tables as JSON
- static `/css` via `WebAssets.mount_css`
- static `/public` for og + favicon

Progressive enhancer JS is a **small** host file (Idiomorph + POST `/action/{name}` + toast plane + `⌘K`). It is not a SPA. It is not React.

## 6. Catalog — every pattern ships **in the product**

Each pattern is one `Component`. Map them into APPIC surfaces. Do not leave a pattern unimplemented. Do not ship a zoo: patterns live inside the foundry's rooms.

### Foundation
Counter (RefState magnitude + MorphState stamp; increment public; **reset is a Cap**), Toggle (bool MorphState), Morph vs Ref planes (silent RefState does not morph without stamp tick).

### Chrome
Tabs (one MorphState key; panels keep stable ids), Accordion, Dropdown, Drawer, Modal (open MorphState, payload RefState, Cap confirm; node stays in tree), App shell (named route + collapsed rail), Breadcrumbs, Bottom nav (mobile; Caps stay off chrome), Popover, Overflow menu (click-away is Host JS).

### Overlays
Toasts, Confirm, Lightbox, Command palette (`⌘K` is a first-class intent door), Banner.

### Forms
Signup (validation public), Wizard (named steps), Typeahead / Search, Choice group (radio MorphState + checkbox set RefState), Combobox (query + value MorphState), Date (named window MorphState; ISO RefState), File drop (filenames RefState + stamp), Slider (magnitude RefState + stamp), OTP (digits RefState; **verify is a Cap**), Password reveal (bool MorphState; secret RefState), Autosave (dirty MorphState; draft RefState), Limited note (length derived from RefState).

### Collections
Shelf filter+sort+stagger, Optimistic list, Pagination, Undo snack, Data table bulk select, Kanban optimistic move, Carousel, Comments (**moderate is a Cap**), Timeline, Empty / loading / error / retry, Reorder, Activity feed.

### Navigation
Region swap list ↔ detail on one id (`mode` MorphState, selected RefState), Master / detail split pane, **plus** real DirectoryRoutes PDP at `/atelier/{sku}`.

### Commerce
Cart, Quantity stepper, Star rating (named `one|two|…`, never MorphState(int)), Wishlist, Coupon (code MorphState; **redeem Cap**), Checkout named steps; **place Cap**, Stock (qty silent, band named `ok|low|out`), Compare max three ids.

### Live Caps
Place without a Cap is refused. Host-mint succeeds. Product never imports Channel. Offline `strict_caps` teaching on Trace.

### Motion
Morph-then-Play hop — `update_with(self, scene(...).enter(#id, rise.enter()))`.
Shared element — `scene.share(key, leave=, arrive=, recipe=)`.
Stagger — `scene.stagger_in` on shelf sort; `fade.exit` on removals.
Without ux-motion, `scene is None` and the same `@action` still morphs. Prove both seats.

### Systems / ops
Chat (typing MorphState), Inbox (unread RefState), Tree, Skeleton, Consent, Theme / density / motion **names** on `<body>`, Chips, Inline edit, Calendar (month name, day RefState, **book Cap**), Progress (pct RefState, phase named), Copy clip, Settings (**wipe Cap**), Offline banner, Presence peers, KPI (values silent, stamp dirties), Shortcuts (same shape as the palette).

## 7. Product — APPIC (*Intent. Presence. Caps.*)

A private foundry for commissioning and collecting handmade objects. Editorial, expensive, abundant negative space, concentric radii. The radical face: **the document is the composition root made visible.** Caps are seals. Intent is a nucleus. Ops are traces. Routes are a constellation. Skin is WebAssets.

**Palette.** Dark ink `#0c0d0b`, elevated `#141512`, surface `#1a1b18`, bone `#ebe6d8`, muted `#9a9488`, cool accent `#c8ccd4`, danger `#c17a6e`, ok `#8fa394`. No purple, gold, neon, gradient-blob slop. No emoji in chrome. Sparse monochrome SVG marks (`svg`/`path`/`rect`/`circle` from `ux_compose`).

**Type.** Display **Fraunces** 500–600, body **Source Sans 3**, mono **IBM Plex Mono**. Fluid `clamp` titles. Tabular nums on money / KPI. Load fonts via Document `<link>` (not CSS-in-Python).

**Motion tokens** in `assets/css/input.css`: `--motion-stagger: 40ms` … `--motion-slow: 400ms`, `--ease-out: cubic-bezier(0.22, 1, 0.36, 1)`. Honor `prefers-reduced-motion`. Density + motion **names** on `<body>` (`data-density`, `data-motion`).

### Surfaces (all live, all morph)

| Path | Unit | Patterns it must exercise |
|---|---|---|
| `/` Table | `Home` | Pulse counter+stamp, **`bind()`**, intent field, KPI, benches (named presence), last Ops, manifesto, lattice teaser, `Level` badge |
| `/atelier` | `Atelier` | Shelf filter/sort/`stagger_in`, wishlist, compare≤3, lightbox, rating, stock band, region swap list↔detail, add-to-bag + `scene.share` |
| `/atelier/{sku}` | `Sku` | **DirectoryRoutes `[sku]`**. Master/detail PDP. Share seat from shelf card. No explicit `get` (resolve_unit). |
| `/commission` | `Commission` | 4-step wizard + radio/checkbox/slider/date/file/password/autosave/limited note/OTP Cap `identity.verify` / place Cap `orders.place` |
| `/bag` | `Bag` | Lines on Host, stepper, coupon Cap `orders.coupon` (`HOUSE`/`FLAX`/`TABLE`), confirm modal, checkout Cap `orders.place`, Morph-then-Play |
| `/board` | `Board` | Kanban optimistic + undo + data table bulk. Move public |
| `/studio` | `Studio` | Chat typing, inbox unread, comments moderate Cap `comments.moderate`, timeline, presence peers |
| `/ledger` | `Ledger` | Calendar book Cap `calendar.book`, progress, copy, locale/density/motion/consent/offline, **WebAssets css_href chip**, optional `ux_dom.ui` Card, wipe Cap `settings.wipe` |
| `/lab` | `Lab` | Remaining 99% as a working floor — tabs of house/fields/chrome/motion: tree, carousel, reorder, empty-retry, activity, chips, inline edit, combobox, accordion, dropdown, drawer, popover, overflow, skeleton, **`morph_play` hop**, share seat, Morph vs Ref planes, toggle, signup validation, typeahead, pagination |
| `/lattice` | `Lattice` | **Radical: Caps as seals on a constellation. Intent as nucleus. Ops as traces. `bind(self.mint)` is a Cap. Public doors stay public. SurfaceBundle + RouteRecord drawn as stars.** |
| `/trace` | `Trace` | **Radical: the document showing its own Results of Ops.** Live Ops log (RefState + stamp), doctor capabilities as chips, Isolation evidence, `HMR_PATH`, `Level.label`, shortcuts, copy a row, bundle tables, IsolationViolation teaching. Explicit `get` to prove resolve_unit bypass. |
| Chrome | `Toasts`, `Palette`, `Banner`, `Ribbon`, `Drawer` | Command `⌘K`; line banner; live Ops ribbon; bag-peek drawer; toast plane; wax-seal burst on Cap mint. Fragments live under `routes/(chrome)/`. |

### Control plane

- Progressive enhancer: POST `/action/{name}`, morph with Idiomorph. GET still works without JS.
- Cap-suffixed verbs (`checkout`, `redeem`, `book`, `verify`, `wipe`, `moderate`, `next`, `place`, `reset`, `mint`) mint then invoke.
- Every successful action **appends an Op row** to Host.trace (kind `morph|cap|notify|surface`). Trace + Lattice + Ribbon render that log. This is the radical instrument: **Ops-as-data, visible.**
- Offline banner when Host.online is false; public morphs still run.

### Caps (real, fail closed)

`orders.place` · `orders.coupon` · `identity.verify` · `calendar.book` · `settings.wipe` · `comments.moderate` · `admin.reset` (Pulse reset) · `lattice.mint`

OTP verify accepts `2048`. Coupons: `HOUSE` / `FLAX` / `TABLE`.

### Doctor + Level

Expose `GET /api/doctor` and render the same evidence in Ledger + Trace: `ok`, `level_available`, `capabilities`, `diagnostics`, `teaching`, `surfaces`, `routes`. Show `int(app.level)` and `app.level.label`. `uxcompose doctor . --no-fail` stays Isolation-green on the product package.

## 8. Coverage matrix (must all be true before you stop)

Tick every row in product source, not comments.

- [ ] `from ux_compose import App, build, WebAssets, DirectoryRoutes, DirectoryASGI, RouterHooks`
- [ ] `Surface`, `SurfaceBundle`, `scan_surfaces`, `validate_surfaces`, `mount_surfaces` imported and used
- [ ] `Component, MorphState, RefState, action, bind, control, notify, update_with, morph_play`
- [ ] `Level, doctor, DoctorResult`
- [ ] `scene, fade, rise` imported with `None` fallback
- [ ] Tags: `div` … `circle`, `HAS_DOM`, `raw` (raw used once for a safe SVG mark, not CSS)
- [ ] `settings.py` + `document.py` + `app.py` + `assets/css/input.css` + `WebAssets.mount_css`
- [ ] Nested `routes/atelier/[sku].py` live PDP
- [ ] Route group `routes/(chrome)/` fragments
- [ ] `bind()` on Pulse and Lattice mint; `control()` remains the stringly hatch
- [ ] `morph_play` used once; `update_with` used everywhere else
- [ ] At least one `__async_render__` page path
- [ ] Caps listed above fail closed without mint; succeed after host mint
- [ ] `scene.share` atelier card → bag line; `stagger_in` on shelf sort
- [ ] Command palette `⌘K` posts the same `/action/{name}` door
- [ ] `GET /api/health`, `/api/doctor`, `/api/surfaces`
- [ ] Custom OG + favicon + `src/lib/og/site.json`
- [ ] Mobile 390px: no overflow, 44px targets, wrap nav, bottom nav
- [ ] `startup.sh` binds `0.0.0.0:8080`
- [ ] Vendor copy of `ux_compose` + `requirements.txt`
- [ ] Isolation scan of `app.py` / `settings.py` / `document.py` / `routes/` is clean
- [ ] No `.tsx` / `.jsx` product UI; no React imports in product code

## 9. Quality

Editorial, not playful-slop. Sparse type. Concentric radii. One accent. Honor reduced motion. Every `@action` mutates state and morphs. Caps are real. Motion degrades. Isolation holds. The lattice is the product's radical face: **authority made visible.** The trace is the product's memory: **Ops as data.** The atelier PDP is the product's routing proof: **filesystem → HTTP, class name never in the URL.** The skin is WebAssets: **tokens compiled, not inlined.**

Ship a running foundry.
