# Grok Build prompt — APPIC on ux-compose 0.1.0 (Clock A)

Copy **everything below the line** into Grok Build. Do not use React, Vue, JSX,
TSX, Next, TanStack UI, Svelte, Solid, HTMX-as-architecture, or a client SPA
runtime as the product. Author in Python with
**[ux-compose](https://github.com/bitplorer/ux-compose) @ main (`0cc83cff`, 0.1.0)**.
Publish the running product to GitHub repo **appic** under the connected account
(create the repo if missing; replace stale files that violate Clock A).

If this prompt and the library disagree, **the library wins**. Do not invent APIs.

Companion law: keep `FEATURE_INVENTORY.md` in the same repo, sourced from
`ux_compose.__all__` + `docs/reference/host.md`. Update it if you vendor a
newer SHA.

---

Build **APPIC** — a stunning nocturnal foundry OS — as a **complete product**
(not a widget zoo) using **https://github.com/bitplorer/ux-compose @ main** as
the only web UI framework. Fully utilise **every public name** in
`ux_compose.__all__`, every Clock A payload door, and every catalog pattern in
`examples/`. Ship a running foundry whose radical face is this:

> **The document is the composition root made visible. Caps are seals. Intent
> is a nucleus. Ops are traces. Routes are a constellation. Skin is WebAssets.
> GET is Clock A. Action is Clock B. Payload type picks media type.**

Read the library first. Clone or vendor `src/ux_compose` from that repo **and**
the four specialists (`ux-dom`, `ux-behavior`, `ux-channel`, `ux-motion`).
Play the teaching apps (`apps/atelier_studio`, `apps/atelier_shop`, `apps/pulse`)
and `examples/` before inventing a widget.

---

## 0. Non-negotiable

- **No React / Vue / Svelte / Next / TanStack UI / JSX / TSX / `.tsx` product UI.**
  No client SPA as source of truth. A Grok sandbox may keep platform
  `src/router.tsx` files unused; they are not the product. Do not scaffold
  TanStack Start for APPIC.
- **No HTMX architecture.** `use_htmx=False`. HTMX is a Document opt-in and
  stays **off**.
- Public imports are `from ux_compose import …` only. There is no `ux.div` /
  `when` / `forall` / `Page`.
- Product modules **never** `import ux_channel`, `cek`, `cek_host`,
  `cek_surface`, `MotionChannel`.
- **Page units have no HTTP verbs.** No `get` / `post` / `put` / `patch` /
  `delete` on a Component. Clock A wraps `render()`. Extra APIs live on the
  FastAPI process `build()` returned.
- Serve on `0.0.0.0:8080`. Keep Grok `extensions.js` in the shell. Do not hide
  the Created-with-Grok pill. Vanilla preview-host bridge (`postMessage`
  `grok-preview-bridge` v1: hello / navigate / history / location / routes / ready).
- Canonical product path is what `uxcompose create-app` writes. Deploy looks
  for `app.py`. Default ASGI is `app:asgi`. Sandbox `startup.sh` binds uvicorn
  to `0.0.0.0:8080`.
- Auth OFF. Database OFF. Domain lives in an in-memory Host store.
- `host="batteries"` is leftover and **fails closed**. Do not teach it.

---

## 1. What ux-compose actually is

Thin pure-Python **composition + delivery** root (`0.1.0`, Clock A). It
harnesses four specialists and must **not** reimplement them:

| Specialist | Role | Unlock | Install |
|---|---|---|---|
| **ux-dom** | Tag trees, Document SSoT, serialize, className, `<link>`, package static, CSP stamp | L0 | `git+https://github.com/bitplorer/ux-dom.git` (prefers Python ≥3.14; same tag call shape on 3.10–3.13 with `HAS_DOM`) |
| **ux-behavior** | `Component`, `MorphState`, `RefState`, `@action`, Ops | L1 | `git+https://github.com/bitplorer/ux-behavior.git` |
| **ux-channel** | Intent → Cap → Result. Behind compose `wire/` only | L2 | `git+https://github.com/bitplorer/ux-channel.git#subdirectory=python` |
| **ux-motion** | Scene Plans, presence, Morph-then-Play (`transition.play`) | L3 | `git+https://github.com/bitplorer/ux-motion.git` |

**Progressive Superpower:** the **same Component class** is correct at L1
(`dispatch`) and L3 (`use_channel` + `use_motion`). Zero rewrite.

PyPI / import / CLI: `ux-compose` / `ux_compose` / **`uxcompose`**.
`ux_compose.__version__ == "0.1.0"`. Python ≥3.11 (classifiers 3.11–3.14).
If the sandbox is 3.10, vendor source on `PYTHONPATH` and keep the same author seat.

Install (plus vendor so git extras can fail):

```
pip install "ux-compose @ git+https://github.com/bitplorer/ux-compose.git"
pip install "ux-behavior @ git+https://github.com/bitplorer/ux-behavior.git"
pip install "ux-motion @ git+https://github.com/bitplorer/ux-motion.git"
pip install "ux-channel @ git+https://github.com/bitplorer/ux-channel.git#subdirectory=python"
pip install "ux-dom @ git+https://github.com/bitplorer/ux-dom.git"
pip install fastapi "uvicorn[standard]" marko itsdangerous python-multipart
```

Vendor:

```
vendor/ux-compose-src/ux_compose/
vendor/specialists-src/{ux_behavior,ux_motion,ux_dom,ux_channel}/
PYTHONPATH=.pydeps:vendor/ux-compose-src:vendor/specialists-src:.
```

---

## 2. Public author surface (do not invent names)

Every name in `ux_compose.__all__` **must appear in product source**.

```
App, build, WebAssets,
DirectoryRoutes, DirectoryASGI, RouterHooks,
Surface, SurfaceBundle, SurfaceError,
mount_surfaces, scan_surfaces, validate_surfaces,
Component, MorphState, RefState, action,
bind, control, notify, update_with, morph_play,
Level, doctor, DoctorResult,
scene, fade, rise,          # None until ux-motion is installed
HAS_DOM, raw, __version__,
html, head, body, title, style, meta, link, script,
div, span, h1, h2, h3, p, a, button, form, input_,
ul, li, header, footer, aside, section, article, nav, main, label,
svg, path, rect, circle
```

Also use (from compose submodules, never from `ux_channel`):

```
ActionInfo, BuildResult, RouteRecord,
DirectoryRoutesError, HMR_PATH, attach_hmr, client_script_tag,
IsolationViolation, CSS_URL_PREFIX, OUTPUT_CSS_NAME,
http_path, is_json_payload, is_stream_payload, apply_html_document
```

### App (from `ux_compose.app.App`)

```
App.boot(name, *, strict_caps=False, level="auto"|0..3)
   # "auto" is Level 1. Channel attaches in build() once ASGI exists.
app.use_host("auto"|"fastapi"|"starlette"|"asgi")   # never "batteries"
app.use_dom(document=None, *, author=True)          # author=False = mount-only
app.use_behavior()
app.use_channel(asgi_app=...)     # Isolation door — wire/ only
app.use_motion()                  # instances, not classes
app.use_cek(mode="adapt")         # degrade if missing; never mode=require
app.mint_cap(action, args)
app.submit_intent / submit_intent_async(..., mint=True)
app.add(*ComponentClasses)
app.mount(package_dir, asgi_app=..., base="routes", fail_closed=..., bind_pages=...,
          on_surface=..., host=...)
app.dispatch("surface.verb", **args)
app.dispatch("surface.verb", args={"sku": "tee"})   # Channel-style, same door
app.control(...)
app.doctor(paths, fail=False)
app.level / app.level.label / app.behavior
```

Level labels: `0 static + routing` · `1 offline interactive` · `2 live channel` · `3 motion`.

### build()

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
    fail_closed=False,
    use_htmx=False,
    document=document,
)
asgi = webassets.mount_css(asgi)
```

`BuildResult` is a tuple with `.app` / `.asgi` / `.bundle`. Export `asgi` for uvicorn.

Orchestra (do not reimplement): `host.open` → L1 boot → author Document →
`use_channel(asgi_app=)` → `DirectoryRoutes.discover` → `host.bind(document=, wrap=)`.

### Component

- `id` is the morph + motion target (default `ClassName.lower()`).
- `render()` returns a tag tree, an HTML string, a **dict** (JSON), a **generator**
  (stream), or an already-built Response. Never a construct-time snapshot.
- `@action(caps=())` public. Non-empty caps need a live Cap or fail closed.
- Return `update_with(self, plan, extra_ops=[notify(...)])`. XOR: plans carry **no** `html=`.
- Prefer `bind(self.verb, **args)` (Pulse + Lattice mint). `control("surface.verb", **args)`
  is the stringly hatch (`data-ux-action` + `data-ux-arg-*`).
- `morph_play("#id", plan)` once (Lab motion hop). Everywhere else: `update_with`.
- **Do not subclass ux-dom `Component`** (MRO collides).

### Encoding rule (Channel session plane refuses quantity MorphState)

| What | Where |
|---|---|
| Open / value / query / named step / named band | `MorphState` (qualitative) |
| Magnitude, lists, money, ISO dates, files, digits | `RefState` + `stamp = MorphState("idle")` |
| One-shot message | `notify(...)` |
| Domain stock / money / bookings | Host store, never the client plane |
| Protected verb | `@action(caps=("orders.place",))` + host mint at HTTP door |

---

## 3. Clock A — two clocks, one foundry (the radical contract)

This is the 0.1.0 product host. Older APPIC copies that put `get()` on page
units are **stale. Replace them.**

| Clock | Trigger | Pipeline |
|---|---|---|
| **A — page GET** | Browser hits a filesystem URL | resolve_unit → `render()` → payload dispatch |
| **B — live action** | `@action` / Channel Intent | mutate → Ops → morph |

Clock A serves the document. Clock B patches it.

**Payload law.** The return value of `render()` picks the HTTP container.
Not `Accept`. Not a route class. Not FastAPI `default_response_class`.

| `render()` returns | HTTP | Document wrap |
|---|---|---|
| tag / HTML `str` / bytes | `HTMLResponse` | yes (author Document) |
| `dict` or list-of-dicts | JSON | **no** |
| generator / async generator | `StreamingResponse` | **no** |
| already a Response (`RedirectResponse`, `FileResponse`, …) | as-is | **no** |

`str` is iterable. **It is not a stream.** `"<div>"` stays buffered HTML with
`Content-Length` so CSP nonce can stamp before the first byte. HTML strings go
through `apply_html_document` as `raw()` — a positional str is never a script `src`.

Path params: `routes/atelier/[sku].py` class `Sku` → `def render(self, sku: str = "")`.
Class name never in the URL. Stem matches class. `≤1` page owner per file.
`(chrome)` skipped. `_` prefix skipped. `index.py` / `route.py` → folder URL.

Author Document (`document.py`) **wraps GET**. A synthesized Document is
mount-only (CSP/static). Dual-Document is a doctor fail.

CSP is two layers, one nonce: header via `CspMiddleware` (`document.mount`) and
stamp on `<script>`/`<style>` before first byte. `Csp.auto()` in `document.py`.
Authors never set CSP headers in page units.

FastAPI is **not** given an HTML `default_response_class`. Leftover
`StreamingRoute` is not the product path. `materialize(route_class=)` fails closed.

Prove Clock A in the product with three page units (not extra FastAPI routes):

| File | URL | `render()` returns | Proves |
|---|---|---|---|
| `routes/health.py` class `Health` | `/health` | `{"ok": True, "level": …, "version": __version__}` | JSON payload door |
| `routes/pulse.py` class `Pulse` | `/pulse` | generator yielding `<div id="beat-n">…</div>` chunks | stream payload door |
| `routes/atelier/[sku].py` class `Sku` | `/atelier/{sku}` | tag tree, **no `get()`** | HTML + path params + `resolve_unit` |

Trace renders `is_json_payload` / `is_stream_payload` / `http_path` evidence
so the two clocks and the three payload doors are **visible to a human**.

---

## 4. Product filesystem (create-app layout — locked)

```
app.py                 # composition root — build() only
settings.py            # BASE_DIR, DEBUG, WebAssets(base_dir=assets, dry_run=False)
document.py            # ONE Document + .use(XElement(), Csp.auto())
requirements.txt
assets/css/input.css
assets/static/file/css/output.css
appic/                 # product package
  server.py            # extra APIs on the FastAPI process (POST /action/{name})
  chrome.py            # Toasts, Palette, Banner, Ribbon (fragments, no URL)
  store.py             # Host domain
  ux.py                # App helpers (bind/control wrappers live here if needed)
  tags.py / marks.py   # SVG marks via svg/path/rect/circle + raw() once
  routes/
    index.py           # class Index → /           (Table)
    atelier.py         # /atelier
    atelier/[sku].py   # class Sku → /atelier/{sku}  NO get()
    commission.py
    bag.py
    board.py
    studio.py
    ledger.py
    lab.py
    lattice.py
    trace.py           # NO get() — Clock A wraps render()
    clocks.py          # Dual-clock room (A vs B made visible)
    health.py          # JSON page unit
    pulse.py           # stream page unit
public/favicon.svg
public/og.jpg          # 1200×630 custom
src/lib/og/site.json   # { "title": "APPIC", "card": "custom", "color": "0c0d0b" }
vendor/…
startup.sh             # binds 0.0.0.0:8080 via uvicorn
FEATURE_INVENTORY.md
GROK_BUILD_PROMPT.md
```

`RouterHooks.resolve_unit` feeds live Behavior instances into synthetic GETs.
Prove it: atelier detail, health, pulse, clocks, and every other page have
**no** explicit `get`.

Scan path used in product:

```python
found = scan_surfaces(PACKAGE, base_directory="routes")
validate_surfaces(found)
```

Render `bundle.surfaces`, `bundle.route_table`, `bundle.action_table`,
`bundle.unit_registry`, `bundle.sealed` on **Trace**, **Lattice**, and **Clocks**.

---

## 5. Hard laws (fail closed)

1. **Isolation.** Product modules never import the wire. `doctor` AST-scan stays green.
2. **Document SSoT.** Exactly one `Document(...)` in `document.py`. Overlays stay in the tree when closed.
3. **XOR + Morph-then-Play.** Plans carry **no** `html=`. Morph first from `render()`, then `transition.play`.
4. **Cap Law.** Protected verbs fail closed without a Channel-minted Cap. Host mints at the HTTP action door for Cap-suffixed verbs then `dispatch` / `submit_intent(..., mint=True)`.
5. **Encoding.** Qualitative MorphState. Magnitudes on RefState + stamp.
6. **Presence continuity.** Stable ids (`id="item-{sku}"`). `scene.stagger_in` on survivors. `scene.share(key, leave=, arrive=)` — share id is identity, not a CSS class.
7. **Cold import never pulls the wire.** `App.boot("auto")` is L1.
8. **CSS.** No CSS or client JS inside Python strings. Tokens in `assets/css/input.css`. Document links `/css/output.css`. `WebAssets.mount_css` serves it. If Tailwind CLI is missing, ship a complete hand-authored `output.css` **and** still call `WebAssets`.
9. **HMR / tunnel** are `uxcompose serve` delivery, not `Document.use`. Expose `HMR_PATH` (`/__uxcompose/hmr`) as a chip on Trace.
10. **Clock A.** No HTTP verbs on page units. Payload type picks media type. Author Document wraps GET. Synthesized Document is mount-only.
11. **No invented library names.**

---

## 6. CLI the product must honor

```
uxcompose create-app myapp --name APPIC --level auto --host auto
uxcompose build [--watch] [--no-minify] [--skip-tailwind] [--skip-import] [--app app:asgi]
uxcompose serve app:asgi --host 0.0.0.0 --port 8080 [--no-reload --hmr --watch assets --watch routes]
uxcompose serve app:asgi --tunnel ngrok|cloudflare
uxcompose deploy --provider docker|fly|render|railway|vps|checklist
uxcompose doctor . --no-fail
```

Host extra routes on the ASGI **process** (not on the class):

- `POST /action/{name}` — progressive enhancer. Cap-suffixed verbs mint then invoke.
  Morph `#surface` with Idiomorph (else outerHTML). Full page GET still works without JS.
  Accept both `dispatch(name, **kwargs)` and `dispatch(name, args={...})`.
- `GET /api/surfaces` — extra FastAPI JSON (proves `default_response_class` was **not** set to HTML)
- static `/css` via `WebAssets.mount_css`
- static `/public` for og + favicon

`GET /health` is a **page unit** (`routes/health.py`), not an extra FastAPI route.
That is the Clock A JSON door made visible.

Progressive enhancer JS is a **small** host file (Idiomorph + POST `/action/{name}`
+ toast plane + `⌘K`). It is not a SPA.

Cap suffixes that mint: `checkout`, `redeem`, `book`, `verify`, `wipe`,
`moderate`, `next`, `place`, `reset`, `mint`, `sell`.

---

## 7. Catalog — every pattern ships **in the product**

Source of truth: `ux-compose/examples/` (75 classes). Copy the *contract*, not
the demo copy. Each widget is one `Component`.

### Foundation (`foundation.py`)
Counter (RefState magnitude + MorphState stamp; increment public; **reset is a Cap**),
Toggle (bool MorphState), Morph vs Ref planes (silent RefState does not morph without stamp tick).

### Chrome (`chrome.py` `modal.py` `shell.py`)
Tabs, Accordion, Dropdown, Drawer, Modal (open MorphState, payload RefState, Cap confirm;
node stays in tree), App shell, Breadcrumbs, Bottom nav, Popover, Overflow menu.

### Overlays (`overlays.py`)
Toasts, Confirm, Lightbox, Command palette (`⌘K` is a first-class intent door), Banner.

### Forms (`forms.py` `fields.py`)
Signup validation, Wizard, Typeahead / Search, Choice group, Combobox, Date, File drop,
Slider, OTP (**verify is a Cap**), Password reveal, Autosave, Limited note.

### Collections (`lists.py` `table_board.py` `feeds.py`)
Shelf filter+sort+stagger, Optimistic list, Pagination, Undo snack, Data table bulk,
Kanban, Carousel, Comments (**moderate is a Cap**), Timeline, Empty / loading / error / retry,
Reorder, Activity feed.

### Navigation (`navigation.py`)
Region swap, Master / detail split pane, **plus** DirectoryRoutes PDP at `/atelier/{sku}`.

### Commerce (`cart.py` `commerce_more.py`)
Cart, Quantity stepper, Star rating (named `one|two|…`, never MorphState(int)), Wishlist,
Coupon (**redeem Cap**), Checkout (**place Cap**), Stock band `ok|low|out`, Compare max three ids.

### Live Caps (`live_caps.py`)
Place without a Cap is refused. Host-mint succeeds. Product never imports Channel.

### Motion (`motion_xor.py` + `cookbooks/PRESENCE.md`)
`update_with(self, scene(...).enter(#id, rise.enter()))`.
`scene.share(key, leave=, arrive=, recipe=)`.
`scene.stagger_in` on shelf sort; `fade.exit` on removals.
Without ux-motion, `scene is None` and the same `@action` still morphs.

### Systems / ops (`systems.py` `ops.py`)
Chat, Inbox, Tree, Skeleton, Consent, Theme / density / motion **names** on `<body>`,
Chips, Inline edit, Calendar (**book Cap**), Progress, Copy clip, Settings (**wipe Cap**),
Offline banner, Presence peers, KPI, Shortcuts.

---

## 8. Product — APPIC (*Intent. Presence. Caps.*)

A private foundry for commissioning and collecting handmade objects. Editorial,
expensive, abundant negative space, concentric radii.

The radical idea is not “another shop”. It is that **authority, motion, and
media type are first-class rooms a human can walk**. Caps are wax seals.
Intent is a nucleus you hold. Ops are traces that do not forget. Routes are
a constellation you can read. GET and action are two clocks you can see
ticking. JSON, stream, and HTML are three doors of the same page-unit law.

**Palette.** Dark ink `#0c0d0b`, elevated `#141512`, surface `#1a1b18`,
bone `#ebe6d8`, muted `#9a9488`, cool accent `#c8ccd4`, danger `#c17a6e`,
ok `#8fa394`. No purple, gold, neon, gradient-blob slop. No emoji in chrome.
Sparse monochrome SVG marks (`svg`/`path`/`rect`/`circle`). `raw()` used
**once** for a safe SVG mark, not CSS.

**Type.** Display **Fraunces** 500–600, body **Source Sans 3**, mono **IBM Plex Mono**.
Fluid `clamp` titles. Tabular nums on money / KPI.

**Motion tokens:** `--motion-stagger: 40ms` … `--motion-slow: 400ms`,
`--ease-out: cubic-bezier(0.22, 1, 0.36, 1)`. Honor `prefers-reduced-motion`.
Density + motion **names** on `<body>`.

### Surfaces

| Path | Unit | Must exercise |
|---|---|---|
| `/` Table | `Index` | Pulse counter+stamp, **`bind(self.beat)`**, intent field, KPI, benches, last Ops, `Level` badge, `__version__` chip |
| `/atelier` | `Atelier` | Shelf filter/sort/`stagger_in`, wishlist, compare≤3, lightbox, add-to-bag, link to PDP |
| `/atelier/{sku}` | `Sku` | DirectoryRoutes `[sku]`. **No `get`.** `render(self, sku="")`. `scene.share` into bag |
| `/commission` | `Commission` | 4-step wizard + radio/checkbox/slider/date/file/password/autosave/limited note/OTP Cap `identity.verify` (`2048`) / place Cap `orders.place` |
| `/bag` | `Bag` | Stepper, coupon Cap `orders.coupon` (`HOUSE`/`FLAX`/`TABLE`), checkout Cap `orders.place`. After successful place, return a `RedirectResponse` to `/ledger` (Response as-is door) |
| `/board` | `Board` | Kanban optimistic + undo + data table bulk |
| `/studio` | `Studio` | Chat typing, inbox, comments moderate Cap `comments.moderate`, presence |
| `/ledger` | `Ledger` | Calendar book Cap `calendar.book`, WebAssets `css_href` chip, wipe Cap `settings.wipe` |
| `/lab` | `Lab` | Remaining catalog: tree, carousel, reorder, empty-retry, chips, inline, combobox, accordion, drawer, **`morph_play` hop**, share seat, Morph vs Ref |
| `/lattice` | `Lattice` | Caps as seals. Intent as nucleus. Ops as traces. **`bind(self.mint)` is a Cap.** SurfaceBundle as stars. `dispatch(..., args={})` proven |
| `/trace` | `Trace` | Live Ops log, doctor, Isolation evidence, `HMR_PATH`, `Level.label`, bundle tables, CSP header chip, `apply_html_document` note |
| `/clocks` | `Clocks` | Dual-clock room. Clock A GET vs Clock B action drawn as two concentric rings. Payload doors (HTML / JSON / stream) as three gates. `http_path` / `is_json_payload` / `is_stream_payload` chips |
| `/health` | `Health` | `render()` returns a **dict**. JSON. No Document wrap. Includes `ok`, `level`, `label`, `version`, `sealed`, `surfaces` |
| `/pulse` | `Pulse` | `render()` returns a **generator** of HTML chunks (foundry heartbeat). StreamingResponse. No Document wrap |
| Chrome | `Toasts`, `Palette`, `Banner`, `Ribbon` | `⌘K`; live Ops ribbon; wax-seal burst on Cap mint |

### Caps (real, fail closed)

`orders.place` · `orders.coupon` · `identity.verify` · `calendar.book` ·
`settings.wipe` · `comments.moderate` · `admin.reset` · `lattice.mint`

OTP verify accepts `2048`. Coupons: `HOUSE` / `FLAX` / `TABLE`.

### Radical interactions (must all work)

1. **Hold an intent on the Table.** Type a verb, press the nucleus, Clock B
   fires, Trace records the Op, Lattice lights the matching star.
2. **Commission a piece.** Wizard state is MorphState named steps. Magnitude
   (budget, date, file) is RefState + stamp. OTP `2048` is a Cap. Place is a Cap.
3. **Sort the atelier.** Survivors keep `id="item-{sku}"` and `stagger_in`.
   Add-to-bag plays `scene.share` from the card to the bag line.
4. **Open `/health`.** The browser shows JSON. The document did not wrap it.
   Trace cites this as the JSON door.
5. **Open `/pulse`.** Chunks arrive. Trace cites this as the stream door.
6. **Open `/clocks`.** Two rings. Three gates. The foundry explains itself.
7. **⌘K** posts the same `/action/{name}` door as a button. No second pipeline.
8. **Checkout without a Cap is refused.** Host-mint then succeeds. Wax-seal
   burst on the ribbon.
9. **Wipe settings** is a Cap. Confirm modal stays in the tree when closed.
10. **Doctor is green.** Isolation scan of `appic/` is clean.

---

## 9. Coverage matrix (must all be true before you stop)

- [ ] `from ux_compose import App, build, WebAssets, DirectoryRoutes, DirectoryASGI, RouterHooks`
- [ ] `Surface`, `SurfaceBundle`, `SurfaceError`, `scan_surfaces`, `validate_surfaces`, `mount_surfaces` imported and used
- [ ] `Component, MorphState, RefState, action, bind, control, notify, update_with, morph_play`
- [ ] `Level, doctor, DoctorResult, __version__`
- [ ] `scene, fade, rise` imported with `None` fallback
- [ ] Tags: `div` … `circle`, `HAS_DOM`, `raw` (raw used once for a safe SVG mark, not CSS)
- [ ] `http_path`, `is_json_payload`, `is_stream_payload`, `apply_html_document` used on Trace / Clocks
- [ ] `settings.py` + `document.py` (`Csp.auto()`) + `app.py` + `assets/css/input.css` + `WebAssets.mount_css`
- [ ] Nested `routes/atelier/[sku].py` live PDP, `render(self, sku="")`, **no `get()` anywhere**
- [ ] JSON page unit `/health` (`dict`) and stream page unit `/pulse` (generator)
- [ ] Dual-clock room `/clocks`
- [ ] `bind()` on Pulse and Lattice mint
- [ ] `dispatch("…", args={...})` proven (Channel-style unpack)
- [ ] `morph_play` used once; `update_with` used everywhere else
- [ ] Caps listed above fail closed without mint; succeed after host mint
- [ ] `scene.share` atelier card → bag line; `stagger_in` on shelf sort
- [ ] Checkout success returns `RedirectResponse` (Response as-is door)
- [ ] Command palette `⌘K` posts the same `/action/{name}` door
- [ ] Extra FastAPI `GET /api/surfaces` stays JSON (no HTML `default_response_class`)
- [ ] Custom OG + favicon + `src/lib/og/site.json`
- [ ] Mobile 390px: no overflow, 44px targets, wrap nav, bottom nav
- [ ] `startup.sh` binds `0.0.0.0:8080`
- [ ] Vendor copy of `ux_compose` + specialists + `requirements.txt`
- [ ] Isolation scan of product package is clean
- [ ] No `.tsx` / `.jsx` **product** UI
- [ ] `FEATURE_INVENTORY.md` and this prompt stay in the repo

---

## 10. Quality

Editorial, not playful-slop. Sparse type. Concentric radii. One accent.
Honor reduced motion. Every `@action` mutates state and morphs. Caps are real.
Motion degrades. Isolation holds. Clock A is correct: no verbs on units,
payload type picks media type, author Document wraps GET.

The lattice is the product's radical face: **authority made visible.**
The trace is the product's memory: **Ops as data.**
The clocks room is the product's honesty: **GET and action are two pipelines.**
The atelier PDP is the product's routing proof: **filesystem → HTTP, class name never in the URL.**
The health and pulse doors are the product's host proof: **return value picks the container.**
The skin is WebAssets: **tokens compiled, not inlined.**

Ship a running foundry. Verify it actually renders — desktop and 390px —
with a clean console. Leave uvicorn up on `0.0.0.0:8080`.
