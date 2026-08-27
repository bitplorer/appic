# ux-compose 0.1.0 — complete feature inventory

Sourced from [bitplorer/ux-compose](https://github.com/bitplorer/ux-compose) `main`
(`0cc83cff`, 2026-08-26, tagged **0.1.0 / Clock A**). Public names are
`src/ux_compose/__init__.py` `__all__`. If this page and the code disagree,
**code wins**.

This is the law for the Grok Build prompt in [GROK_BUILD_PROMPT.md](GROK_BUILD_PROMPT.md).
Do not invent a sixth product, a second namespace (`ux.*`), or React.

---

## 1. What the package is

Thin pure-Python **composition + delivery** root. It harnesses four specialists
and must **not** reimplement them.

| Specialist | Role | Unlock |
|---|---|---|
| **[ux-dom](https://github.com/bitplorer/ux-dom)** | Tag trees, Document SSoT, serialize, className, `<link>`, package static, `uxdom`, CSP stamp | L0 |
| **[ux-behavior](https://github.com/bitplorer/ux-behavior)** | `Component`, `MorphState`, `RefState`, `@action`, Ops | L1 |
| **[ux-channel](https://github.com/bitplorer/ux-channel)** | Intent → Cap → Result. Live authority. Behind compose `wire/` only | L2 |
| **[ux-motion](https://github.com/bitplorer/ux-motion)** | Scene Plans, presence, Morph-then-Play IR (`transition.play`) | L3 |

| Layer | Name |
|---|---|
| PyPI / pip | `ux-compose` |
| Import | `ux_compose` |
| CLI | **`uxcompose`** (sole product lifecycle) |
| Version | `0.1.0` (`ux_compose.__version__`) |
| Python | ≥ 3.11 (ux-dom full stack needs ≥ 3.14) |
| License | MIT |

**Progressive Superpower:** Level 1 code remains correct at L2/L3. Zero rewrite.
If you rewrite a Component “to go live”, you have violated the contract.

---

## 2. Public author surface (`__all__`)

Import **only** from `ux_compose`. There is no public `ux.div` / `when` / `forall` / `Page`.

### Composition + delivery (compose-owned)

| Export | Role |
|---|---|
| `App` | Composition root: `boot`, `add`, `mount`, `use_host`, `use_dom`, `use_behavior`, `use_channel`, `use_motion`, `use_cek`, `mint_cap`, `submit_intent`, `submit_intent_async`, `dispatch`, `control`, `doctor`, `level`, `behavior` |
| `build` | One-shot façade. Orchestra: `host.open` → L1 boot → document → Channel on asgi → discover → `host.bind`. Returns `BuildResult` = `(app, asgi, bundle)` |
| `WebAssets` | App CSS/JS folders. `from_app_root`, `ensure`, `mount_css`, `css_href`, `input_css`, `output_css` |
| `DirectoryRoutes` | Filesystem → `RouteRecord` (no framework imports). One path law: `http_path` |
| `DirectoryASGI` | Pure-ASGI host. No Starlette. JSON / stream / HTML use the same predicates |
| `RouterHooks` | `resolve_unit`, `accept_symbol`, `on_route` |
| `Surface` | One catalog unit (`id`, `cls`, `is_page`, `url_path`, `actions`, `instance`) |
| `SurfaceBundle` | Sealed evidence: `surfaces`, `route_table`, `action_table`, `unit_registry`, `errors`, `sealed` |
| `SurfaceError` | Fail-closed id/path clash |
| `mount_surfaces` | Scan → validate → Behavior.add → optional page bind |
| `scan_surfaces` | Discover define-in-module units under `routes/` |
| `validate_surfaces` | Fail-closed id/path clashes |
| `Level` | `L0..L3` IntEnum. Labels: `static + routing` / `offline interactive` / `live channel` / `motion` |
| `doctor` / `DoctorResult` | Isolation AST scan, dual-Document heuristic, capabilities, teaching |
| `__version__` | `"0.1.0"` |

Not in `__all__` but public in submodules (authors may import these **from compose**, never from `ux_channel`):

| Name | Module |
|---|---|
| `ActionInfo` | `ux_compose.surfaces` |
| `BuildResult` | `ux_compose.build` (tuple with `.app` / `.asgi` / `.bundle`) |
| `DirectoryRoutesError` / `DirectoryRouterError` | `ux_compose.routing` |
| `RouteRecord` | `ux_compose.routing` |
| `ResolveUnit` / `AcceptSymbol` / `OnRoute` | `ux_compose.routing` |
| `http_path` / `is_json_payload` / `is_stream_payload` / `apply_html_document` | `ux_compose.routing` |
| `module_exports` / `pick_page_type` / `materialize` / `mount` / `match_record` | `ux_compose.routing` |
| `HMR_PATH` / `attach_hmr` / `client_script_tag` | `ux_compose.hmr` (`HMR_PATH` = `/__uxcompose/hmr`) |
| `IsolationViolation` / `scan_isolation` / `scan_dual_document` | `ux_compose.doctor` |
| `CSS_URL_PREFIX` (`/css`) / `OUTPUT_CSS_NAME` (`output.css`) | `ux_compose.assets` |
| `require_dom` | `ux_compose.dom` |

`materialize(route_class=)` **fails closed**. Leftover `StreamingRoute` is not the product path.

### Behavior surface (via ux-behavior)

`Component`, `MorphState`, `RefState`, `action`, `bind`, `control`, `notify`, `update_with`, `morph_play`

### Motion surface (via ux-motion, else `None`)

`scene`, `fade`, `rise`

Compose wraps a Scene/Plan as one `transition.play` Op (`helpers._normalize_plan_ops`).
Authors never emit Channel wire shape.

### Tag constructors (via ux-dom when installed; else `None` / `HAS_DOM=False`)

`raw`, `html`, `head`, `body`, `title`, `style`, `meta`, `link`, `script`,
`div`, `span`, `h1`, `h2`, `h3`, `p`, `a`, `button`, `form`, `input_`,
`ul`, `li`, `header`, `footer`, `aside`, `section`, `article`, `nav`, `main`,
`label`, `svg`, `path`, `rect`, `circle`

HTML strings in `render()` remain valid at L1. Do **not** subclass ux-dom `Component`
(MRO collides with tree verbs `add`/`remove`/`get`/`clear`).

---

## 3. App API (composition root)

```
App.boot(name, *, strict_caps=False, level="auto"|0..3)
app.use_host("auto"|"fastapi"|"starlette"|"asgi")   # "batteries" leftover, fails closed
app.use_dom(document=None, *, author=True)          # author=False = synthesized, mount-only
app.use_behavior()
app.use_channel(asgi_app=...)     # Isolation door — never import ux_channel in product
app.use_motion()                  # attach_motion() returns instances, not classes
app.use_cek(mode="adapt"|"require")
app.mint_cap(action, args)
app.submit_intent / submit_intent_async(..., mint=True)
app.add(*ComponentClasses)
app.mount(package_dir, asgi_app=..., base="routes", fail_closed=..., bind_pages=...,
          on_surface=..., host=...)
app.dispatch("surface.verb", **args)
app.dispatch("surface.verb", args={"sku": "tee"})   # Channel-style Intent payload, same door
app.control(...)
app.doctor(paths, fail=False)
app.level / app.level.label / app.behavior
```

`boot(level="auto")` is **Level 1 (Behavior only)**. Channel/Motion attach in
`build()` once the ASGI process exists, or via explicit `use_channel` /
`use_motion`. A headless Channel would never land on FastAPI
(`Behavior.attach` is idempotent on `_wire`); `use_channel(asgi_app=)` rebinds.

HTMX is **never** auto-attached; opt in via `Document.use(Htmx())` or `build(use_htmx=True)`.

Cold import of `ux_compose` never pulls the wire.

---

## 4. `build()` composition façade

```python
from ux_compose import build
from document import document

app, asgi, bundle = build(
    PACKAGE,
    name="APPIC",
    host="auto",      # auto | fastapi | asgi   ("batteries" → ProductBatteriesRejected)
    live="auto",      # auto | channel | null
    level="auto",     # auto | 0..3
    base="routes",
    fail_closed=True,
    use_htmx=False,   # HTMX stays off
    document=document,
)
```

Process order (`routing/host.py`):

```text
host.open(name, host)          # FastAPI() or DirectoryASGI
App.boot(..., level=1)         # Behavior only
_attach_document(...)          # author's Document SSoT
App.use_channel(asgi_app=)     # after the process exists
DirectoryRoutes.discover()     # one path law
host.bind(document=, wrap=)    # document.mount then page routes
```

- `host="auto"` prefers FastAPI if importable, else `DirectoryASGI`.
- `live="null"` pins offline Behavior (no Channel/Motion).
- Author Document is SSoT. `build(document=)` attaches it as **wrap** (GET shell).
- A synthesized Document (`author=False`) is **mount-only** (CSP / static).
  Wrapping GET with it treats a positional HTML `str` as a script `src` and
  the fragment vanishes.
- Returns `BuildResult` with `.app` / `.asgi` / `.bundle`.
- Extra JSON/POST APIs live on the FastAPI process, not on the Component.

---

## 5. Clock A — product host (0.1.0 law)

Two clocks. Do not mix.

| Clock | Trigger | Pipeline | Owner |
|---|---|---|---|
| **A — page GET** | Browser hits a filesystem URL | resolve → `render()` → payload dispatch | `routing/fastapi.py` |
| **B — live action** | `@action` / Channel Intent | mutate → Ops → morph | ux-behavior + `wire/` |

Clock A serves the document. Clock B patches it. A page unit has **no HTTP verbs**.
No `get` / `post` / `put` / `patch` / `delete` on the class. FastAPI must not
inspect classmethods.

### Payload law (media type)

**The return value of `render()` picks the HTTP container. Not `Accept`.
Not a route class. Not FastAPI `default_response_class`.**

| `render()` returns | HTTP | Document wrap | CSP stamp |
|---|---|---|---|
| ux-dom tag / Document / Component / HTML `str` / `bytes` | `HTMLResponse` | **yes** (author wrap) | yes (`prepare_html_body`) |
| `dict` or list-of-dicts (including `[]`) | JSON | **no** | n/a (header still process-wide) |
| sync / async generator, or `__aiter__` that is not a tree | `StreamingResponse` | **no** | only if ux-dom stream prepare runs |
| already a `Response` (`HTMLResponse` / `JSONResponse` / `FileResponse` / `RedirectResponse`) | as-is | **no** | whatever that object already did |
| `None` | empty HTML | yes | — |

`str` is iterable. **It is not a stream.** `"<div>"` stays buffered HTML with
`Content-Length`. `apply_html_document` wraps HTML `str` as ux-dom `raw()` so
the fragment is body markup, not a script `src`.

Trees stay buffered so CSP nonce + `Content-Length` happen **before** the first
byte. Leftover `StreamingRoute` is not the product path. To stream a tag tree,
opt in: `return tree.__async_render__(pretty=False)` or `StreamingResponse(tree)`.

Path params come from the Request, passed into `render(**path_params)` when the
signature accepts them. `routes/atelier/[sku].py` class `Sku` → `render(self, sku="")`.

### Host values

| `host=` | Process | Fail |
|---|---|---|
| `auto` | FastAPI if importable, else DirectoryASGI | never |
| `fastapi` | FastAPI | closed if FastAPI missing |
| `asgi` | DirectoryASGI (no Starlette) | never |
| `starlette` | alias of `auto` | — |
| `batteries` / `directory_router` | — | `ProductBatteriesRejected` |

FastAPI is **not** given `default_response_class=HTMLResponse`. Author
`@asgi.get("/api/...")` returning a dict stays JSON.

### CSP on FastAPI (two layers, one nonce)

| Layer | What | When |
|---|---|---|
| **Header** | `Content-Security-Policy` on `http.response.start` | every HTTP response (`CspMiddleware` via `document.mount`) |
| **Stamp** | `nonce=` on `<script>` / `<style>` before first byte | HTML body / tree stream |

`Csp.auto()` picks `Csp.dev()` when `DEBUG` is truthy, else `Csp.prod()`.
Authors attach once in `document.py`: `.use(XElement(), Csp.auto())`.
They never set CSP headers in page units. DirectoryASGI has no middleware;
doctor reports CSP middleware is not attached.

Canonical: [docs/reference/host.md](https://github.com/bitplorer/ux-compose/blob/main/docs/reference/host.md).
Recipes: [docs/guides/HOST.md](https://github.com/bitplorer/ux-compose/blob/main/docs/guides/HOST.md).

---

## 6. Page-unit routing (DirectoryRoutes)

This is Next-style **file routing, not React**. Class name never leaks into the URL.

| File under `routes/` | URL |
|---|---|
| `index.py` / `route.py` | folder prefix or `/` |
| `hello.py` | `/hello` |
| `shop/index.py` | `/shop` |
| `shop/[sku].py` | `/shop/{sku}`  (stem-key `sku` → class `Sku`) |
| `[id]/page.py` | `/{id}/page` |
| `_private.py`, `(group)/…` | skipped |

Locked model:

- Page unit = renderable class whose **name matches the module stem**.
- `≤1` page owner per file. Extra renderables are fragments (no URL).
- Define-in-module only. Imported classes are not auto-registered.
- `fail_closed` on ambiguity / duplicates.
- `RouterHooks.resolve_unit` feeds live Behavior instances into synthetic GETs.
- HTTP verbs on the class are **ignored** (Clock A).
- `RouteRecord`: `method`, `path`, `name`, `handler`, `page_cls`, `kind` (`page` | `explicit` | `route_module`)

Product apps use `build()` / `App.mount`. Authors never implement adapters
(Invisible Strategy). `App.mount` is a **secondary door** (tests). Teaching
is `create-app` + `build()`.

---

## 7. WebAssets + Tailwind (compose-owned CSS)

Disk convention (locked with `create-app` / `build` / `/css` mount):

```
assets/css/input.css                 # author source (tokens + @source)
assets/static/file/css/output.css    # compiler output (minified)
URL: /css/output.css
```

```python
from ux_compose import WebAssets
webassets = WebAssets.from_app_root(PACKAGE, dry_run=False)
webassets.static.css    # assets/static/file/css
webassets.output_css    # .../output.css
webassets.css_href      # /css/output.css
webassets.mount_css(asgi)   # FastAPI .mount or DirectoryASGI wrapper
```

Laws:

1. Author utilities on the tree: `className="rounded-2xl border …"`.
2. Tokens + `@layer components` live in `assets/css/input.css`. **Never CSS or client JS inside Python strings. Never `style(raw(CSS))`.**
3. The Document **links** `/css/output.css`. It does not inline it.
4. Production compiles with `--minify`. Dev `--watch`. Those flags are **XOR**.
5. `cdn.tailwindcss.com` is not the product path.
6. `uxcompose serve --hmr` watches `.css` and reloads. It does **not** compile Tailwind.
7. `uxcompose deploy` does **not** run the compiler. Run `uxcompose build` first.
8. `create-app` does **not** emit `tailwind.config.js`. `@source` in `input.css` scans the app.

Optional render-only markup kit (no Ops): `from ux_dom.ui import Button, Card, CardHeader, CardTitle, CardContent`.

---

## 8. Product CLI (`uxcompose` only)

```
uxcompose create-app <dest> [--name NAME] [--level auto|0-3] [--host auto|fastapi|asgi]
uxcompose build [--watch] [--no-minify] [--skip-tailwind] [--skip-import] [--app app:asgi]
uxcompose serve [app:asgi] [--host 0.0.0.0] [--port 8080] [--reload|--no-reload]
               [--hmr] [--watch PATH ...]
               [--tunnel none|ngrok|cloudflare] [--tunnel-token TOKEN]
               [--health-path /] [--health-timeout 30]
uxcompose deploy [--provider docker|fly|render|railway|vps|checklist] [--force] [--name NAME]
uxcompose doctor [paths...] [--no-fail]
```

HMR: WebSocket `/__uxcompose/hmr` broadcasts `{type: reload}`. Needs `--no-reload`
to attach on this process. `HMR_PATH`, `attach_hmr`, `client_script_tag` live in
`ux_compose.hmr`. **Not** a `Document.use` product API.

Pure-dom stays on `uxdom doctor | lint | profile | add`.

Scaffold (`create-app`) writes:

```
settings.py          # BASE_DIR, DEBUG, WebAssets
document.py          # Document SSoT + .use(XElement, Csp.auto()); host wraps GET
app.py               # build(host=, live=, level=, document=) + WebAssets.mount_css
routes/hello.py      # page unit — render() fragment, NO get()
assets/css/input.css
requirements.txt
README.md
```

Gone from scaffold: `Hello.get()`, `document.mount(asgi)` in `main()`, class HTTP
verbs, leftover `page()`, `host="batteries"`.

Deploy looks for `app.py`. Default ASGI entry: `app:asgi`.

---

## 9. Component contract

- `id` is the morph + motion target (default `ClassName.lower()`).
- `render()` returns a ux-dom tag tree (or HTML string, or dict, or generator).
  Never a construct-time snapshot.
- `__render__(pretty=False)` / `__async_render__` re-run live `render()`.
- `@action(caps=(...))` return algebra:
  1. `None` → auto-morph dirty MorphStates
  2. `list[Op]` → exact Ops (auto suppressed)
  3. Prefer `update_with(self, scene(...).enter("#id", rise.enter(ms=140)), extra_ops=[notify("…")])`
- `bind(self.verb, **args)` — symbol-safe, preferred. Also `self.verb.ui(**args)`.
- `control("surface.verb", **args)` — stringly hatch: `data-ux-action` + `data-ux-arg-*`.
- `notify(message, level="info")` — one-shot toast Op.
- `morph_play("#id", plan)` — morph then plan ops (still XOR). Use **once** as the hop hatch; prefer `update_with`.
- `update_with` strategy default is `"idiomorph"`. Morph HTML is live `render()`.
- Do **not** subclass ux-dom `Component`.

`dispatch` is one door for tests, agents, and live:

```python
app.dispatch("cart.add", sku="tee")
app.dispatch("cart.add", args={"sku": "tee"})   # Channel Intent shape — same call
```

---

## 10. Encoding law (Channel session plane refuses quantity MorphState)

| What | Where |
|---|---|
| Open / value / query / named step / named band / bool | `MorphState` (qualitative) |
| Magnitude, lists, money, ISO dates, files, digits | `RefState` + `stamp = MorphState("idle")` |
| One-shot message | `notify(...)` |
| Domain stock / money / bookings | **Host store**, never the client plane |
| Protected verb | `@action(caps=("orders.place",))` + live mint |

Chrome (tabs, accordion, open/close) is public. Spending money, deleting, or
changing identity takes a Cap.

---

## 11. Motion XOR + Morph-then-Play

- **XOR** — `morph(target)` XOR `scene.enter(target, html=...)`. Never both.
- **Morph-then-Play** — morph Op first; `transition.play` follows.
- Plans carry **no** `html=`. Morph HTML is live `render()`.
- Isolation — Plan comes from `ux_compose.scene` (re-export), never `ux_channel`.
- Recipes: `scene("name").enter("#id", rise.enter(ms=160))`
- List continuity: stable ids (`id="item-{sku}"`) + `scene.stagger_in([...], rise.enter())` + optional `exit("#gone", fade.exit())`
- Shared element: `scene.share(key, leave="#from", arrive="#to", recipe=rise.enter(ms=120))` — share id is identity, not a CSS class. Leave and arrive must exist **after** morph.
- Without ux-motion, `scene is None` and the same `@action` still morphs.

Product-local helpers (`tick`, `maybe_plan`, …) are **not** library exports. Define them in the product if needed.

Cookbook: [cookbooks/PRESENCE.md](https://github.com/bitplorer/ux-compose/blob/main/cookbooks/PRESENCE.md).

---

## 12. Isolation + Document SSoT + Cap Law

1. Product modules never `import ux_channel`, `cek`, `cek_host`, `cek_surface`, `MotionChannel`.
2. Live path only through `App.use_channel` / `use_motion` / `use_cek` (compose `wire/`).
3. Exactly one HTML shell. Overlays are Components, not a second Document. Overlays stay in the tree when closed.
4. Dual-Document in product files is a doctor fail.
5. `Document.use` may take control, runtime (`XElement`), CSP, style. **Not** HMR, App, host strategy.
6. Protected verbs fail closed without a Channel-minted Cap. Host mints at the HTTP action door via `mint_cap` / `submit_intent(..., mint=True)`.
7. After `use_channel`, `dispatch` is Host-internal; live verification is Intent.
8. `doctor` AST-scans Isolation, reports `level_available`, `capabilities`, `surfaces`, `routes`, `teaching`.

Forbidden imports (doctor): `ux_channel`, `cek`, `cek_host`, `cek_surface`, `MotionChannel`.

---

## 13. Catalog — 99% of product UI (`examples/`)

Every pattern is one `Component`. The same class is valid at L1 (`dispatch`) and L3 (`use_channel` + `use_motion`).

| Group | File | Classes |
|---|---|---|
| Foundation | `foundation.py` | `Counter`, `Toggle`, `Planes` |
| Chrome | `chrome.py` `modal.py` `shell.py` | `Tabs`, `Accordion`, `Dropdown`, `Drawer`, `ConfirmModal`, `AppShell`, `Breadcrumbs`, `BottomNav`, `Popover`, `OverflowMenu` |
| Overlays | `overlays.py` | `Toasts`, `Confirm`, `Lightbox`, `Palette`, `Banner` |
| Forms | `forms.py` `fields.py` | `SignupForm`, `Wizard`, `Search`, `ChoiceGroup`, `Combobox`, `DateField`, `FileDrop`, `SliderField`, `OtpGate` (Cap), `PasswordField`, `Autosave`, `LimitedNote` |
| Collections | `lists.py` `table_board.py` `feeds.py` | `Shelf`, `OptimisticList`, `Pages`, `UndoSnack`, `DataTable`, `Kanban`, `Carousel`, `Comments` (Cap moderate), `Timeline`, `EmptyRetry`, `ReorderList`, `ActivityFeed` |
| Navigation | `navigation.py` | `ShopView` (region swap), `MasterDetail` |
| Commerce | `cart.py` `commerce_more.py` `systems.py` | `Cart`, `Stepper`, `Rating`, `Wishlist`, `Coupon` (Cap), `CheckoutFlow` (Cap), `StockBadge`, `CompareTray` |
| Live Caps | `live_caps.py` | `LiveOrder` |
| Motion | `motion_xor.py` | `MotionBox`, `ShareSeat` |
| Systems | `systems.py` `ops.py` | `Chat`, `NotifyCenter`, `Tree`, `Skeleton`, `Consent`, `Theme`, `Chips`, `InlineEdit`, `Calendar` (Cap), `ProgressMeter`, `CopyClip`, `Settings` (Cap), `OfflineBanner`, `Presence`, `KpiStrip`, `Shortcuts` |
| Host | `document_boot.py` `live_asgi.py` `cart_document.py` `page_unit_mount.py` | Document SSoT, `build()` Clock A GET, Isolation door; `App.mount` secondary |

Play them: `apps/atelier_studio`. Product shop: `apps/atelier_shop`. Demo pulse: `apps/pulse`.

---

## 14. Wire (not for product imports)

`ux_compose.wire.boot.attach_channel` / `attach_motion` (returns **instances**)
`ux_compose.wire.caps.mint_cap` / `submit_intent` / `async_submit_intent` / `bridge_actions` / `ops_to_wire`
`ux_compose.wire.cek.attach_cek`

Authors reach Caps through `App.mint_cap` / `App.submit_intent`. Never import `ux_channel`.

---

## 15. Names that do **not** exist (do not invent)

- `ux.div` / `when` / `forall` / `Page`
- Product CLI on `uxdom` (`create-app`, product `build`, `serve`, `deploy`)
- Tailwind compiler on ux-dom
- `WebAssets` on ux-dom
- HMR as `Document.use`
- `host="batteries"` as a thing to run
- HTTP verbs (`get`/`post`/…) on page units
- FastAPI `default_response_class=HTMLResponse`
- `StreamingRoute` / `route_class` as the product path
- `Accept` negotiation on page GET
- Dual product paths
- A copy of Channel codecs, Document serialize, or motion IR in the product
- `tick` / `maybe_plan` / `maybe_fade` / `maybe_stagger` / `maybe_share` as library APIs
- Mini HTML builder when `HAS_DOM` is false
- Wrap GET with a synthesized Document
- Scaffold `page()` as the GET wrap
- Channel boot in `App.boot("auto")`
- Logic in `routing/adapters/` (shims only)
