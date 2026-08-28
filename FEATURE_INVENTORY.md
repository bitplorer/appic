# ux-compose — complete feature inventory

Sourced from [bitplorer/ux-compose](https://github.com/bitplorer/ux-compose) `main`
(`17e652a6`, 2026-08-27, **0.1.0 / Clock A** + unreleased **ownable kit**).
Public names are `src/ux_compose/__init__.py` `__all__`. Kit names are
`src/ux_compose/kit/catalog.py` `CATALOG`. If this page and the code disagree,
**code wins**.

Companion: [GROK_BUILD_PROMPT.md](GROK_BUILD_PROMPT.md).
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
| `BuildResult` | `ux_compose.build` |
| `DirectoryRoutesError` / `DirectoryRouterError` | `ux_compose.routing` |
| `RouteRecord` | `ux_compose.routing` |
| `http_path` / `is_json_payload` / `is_stream_payload` / `apply_html_document` | `ux_compose.routing` |
| `HMR_PATH` / `attach_hmr` / `client_script_tag` | `ux_compose.hmr` (`HMR_PATH` = `/__uxcompose/hmr`) |
| `IsolationViolation` / `scan_isolation` / `scan_dual_document` | `ux_compose.doctor` |
| `CSS_URL_PREFIX` (`/css`) / `OUTPUT_CSS_NAME` (`output.css`) | `ux_compose.assets` |
| `KitCopyError` / `copy_component` | `ux_compose.kit.copy` (CLI `uxcompose add` owns this; product owns the dropped file) |
| `CATALOG` / `list_components` / `resolve` | `ux_compose.kit.catalog` |

`materialize(route_class=)` **fails closed**. Leftover `StreamingRoute` is not the product path.

### Behavior surface (via ux-behavior)

`Component`, `MorphState`, `RefState`, `action`, `bind`, `control`, `notify`, `update_with`, `morph_play`

### Motion surface (via ux-motion, else `None`)

`scene`, `fade`, `rise`, **`slide`**

Compose wraps a Scene/Plan as one `transition.play` Op (`helpers._normalize_plan_ops`).
Authors never emit Channel wire shape.

### Tag constructors (via ux-dom when installed; else `None` / `HAS_DOM=False`)

`raw`, `html`, `head`, `body`, `title`, `style`, `meta`, `link`, `script`,
`div`, `span`, `h1`, `h2`, `h3`, `p`, `a`, `button`, `form`, `input_`,
`ul`, `li`, `header`, `footer`, `aside`, `section`, `article`, `nav`, `main`,
`label`, `svg`, `path`, `rect`, `circle`

Do **not** subclass ux-dom `Component` (MRO collides).

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
`build()` once the ASGI process exists.

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
    use_htmx=False,
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

---

## 5. Clock A — product host (0.1.0 law)

Two clocks. Do not mix.

| Clock | Trigger | Pipeline | Owner |
|---|---|---|---|
| **A — page GET** | Browser hits a filesystem URL | resolve → `render()` → payload dispatch | `routing/fastapi.py` |
| **B — live action** | `@action` / Channel Intent | mutate → Ops → morph | ux-behavior + `wire/` |

Clock A serves the document. Clock B patches it. A page unit has **no HTTP verbs**.

### Payload law (media type)

**The return value of `render()` picks the HTTP container. Not `Accept`.
Not a route class. Not FastAPI `default_response_class`.**

| `render()` returns | HTTP | Document wrap |
|---|---|---|
| ux-dom tag / Document / Component / HTML `str` / `bytes` | `HTMLResponse` | **yes** (author wrap) |
| `dict` or list-of-dicts (including `[]`) | JSON | **no** |
| sync / async generator, or `__aiter__` that is not a tree | `StreamingResponse` | **no** |
| already a `Response` | as-is | **no** |
| `None` | empty HTML | yes |

`str` is iterable. **It is not a stream.** HTML strings go through
`apply_html_document` as `raw()`.

Path params: `routes/atelier/[sku].py` class `Sku` → `def render(self, sku: str = "")`.

---

## 6. Page-unit routing (DirectoryRoutes)

This is Next-style **file routing, not React**. Class name never leaks into the URL.

| File under `routes/` | URL |
|---|---|
| `index.py` / `route.py` | folder prefix or `/` |
| `hello.py` | `/hello` |
| `shop/index.py` | `/shop` |
| `shop/[sku].py` | `/shop/{sku}` |
| `_private.py`, `(group)/…` | skipped |

- Page unit = renderable class whose **name matches the module stem**.
- `≤1` page owner per file. Extra renderables are fragments (no URL).
- Define-in-module only. Imported classes are not auto-registered.
- HTTP verbs on the class are **ignored** (Clock A).

---

## 7. WebAssets + Tailwind (compose-owned CSS)

```
assets/css/input.css                 # author source (tokens + @source)
assets/static/file/css/output.css    # compiler output (minified)
URL: /css/output.css
```

Laws: no CSS or client JS inside Python strings. Document **links** `/css/output.css`.
`cdn.tailwindcss.com` is not the product path. `uxcompose serve --hmr` watches `.css`;
it does **not** compile. `uxcompose deploy` does **not** run the compiler.

Kit components style via `class_*` Tailwind strings on the copied file. **No companion CSS.**

---

## 8. Product CLI (`uxcompose` only)

```
uxcompose create-app <dest> [--name NAME] [--level auto|0-3] [--host auto|fastapi|asgi]
uxcompose build [--watch] [--no-minify] [--skip-tailwind] [--skip-import] [--app app:asgi]
uxcompose serve [app:asgi] [--host 0.0.0.0] [--port 8080] [--reload|--no-reload]
               [--hmr] [--watch PATH ...]
               [--tunnel none|ngrok|cloudflare] [--tunnel-token TOKEN]
uxcompose deploy [--provider docker|fly|render|railway|vps|checklist] [--force] [--name NAME]
uxcompose doctor [paths...] [--no-fail]
uxcompose add [name] [--force] [--page] [--root PATH]
uxcompose add --list
```

`uxcompose add` is shadcn-style **ownable copy**. The library keeps the source of
truth. The dropped file is yours to edit. Prefer the copy over
`from ux_compose.kit import …` in product apps.

Default drop: `components/{stem}.py`. `--page` also writes `routes/{stem}.py`
so GET `/{stem}` hosts the card.

Pure-dom stays on `uxdom doctor | lint | profile | add`.

---

## 9. Ownable kit (`ux_compose.kit.catalog.CATALOG`) — 23 components

Every kit unit is one `Component`. Tailwind `class_*` only. Same class is valid
at L1 (`dispatch`) and L3 (`use_channel` + `use_motion`). Host seams are
overridable methods. Copy with `uxcompose add {stem}` then restyle `class_*`
to the product palette.

### Wave 0 — studio chrome

| stem | Class | Contract | Host seam / Cap |
|---|---|---|---|
| `login` | `Login`, `AuthDecision` | Sign-in / sign-up card. Chrome MorphState. Secrets RefState. Reveal attaches before morph. | `authenticate()` · Caps `auth.login` / `auth.signup`. Demo refuse: `@blocked.test` |
| `tabs` | `Tabs` | Segmented tabs. One MorphState key. Public select. Stable panel ids. | — |
| `accordion` | `Accordion` | Open ids as a MorphState tuple. Several panels may be open. Open uses `maybe_plan`. | — |
| `dropdown` | `Dropdown` | Menu is presence. Value is a named key. | — |
| `dialog` | `Dialog` | Public ask, Cap-protected confirm. Swipe lives on Keep (`click swipe.down`), not the root. Open composes Motion enter (fade scrim, rise panel) — selectors only, no Channel attr, no kit JS. Cancel/confirm are morph-only. | `on_confirm()` |
| `sheet` | `Sheet` | Edge panel. Close / Done accept `click swipe.right`. No root swipe. Open: fade scrim, slide panel. | — |
| `toast` | `Toast` | Server list is authority. Push is public. | — |
| `command` | `Command` | Command palette. Query attaches. | `on_run()` |
| `table` | `Table` | Sort key MorphState, selection RefState. Archive is a Cap. | archive Cap |
| `pagination` | `Pagination` | Opaque page keys. Windowed numbers (`WINDOW` neighbors, default 1). First/last + gaps `max-sm:hidden`. 44px chevrons. | — |
| `combobox` | `Combobox` | Type to filter, then pick. Query attaches on morph. | — |
| `sidebar` | `Sidebar` | Collapsible rail. Active key is MorphState. | — |
| `breadcrumb` | `Breadcrumb` | Trail of named crumbs. Walking back is public. | — |
| `stepper` | `Stepper` | Named steps. Finish spends `flow.finish`. | — |
| `carousel` | `Carousel` | Named slides. Overlay prev/next (44px). Sliding pip `#id-thumb` coalesces. Root stamps `data-channel-id`. `data-channel-on` swipe + directional slide/rise/fade. | — |
| `calendar` | `Calendar` | Month and day are named keys. | `on_pick()` |
| `select` | `Select` | Grouped options. Value is a name. Click-away scrim. | — |
| `otp` | `Otp` | Six digits attach. Verify spends `auth.otp`. | — |
| `plans` | `Plans` | Radio cards. One named plan. | `on_choose()` |

### Wave 1 — Signal grammar

`data-channel-on` for `swipe.vertical` / `longpress` / `input delay:`.
No kit JS. Swipe never lives on a root that also has clickable rows.

| stem | Class | Contract |
|---|---|---|
| `actionsheet` | `ActionSheet` | Bottom sheet. Handle is a 44px hit that accepts `click swipe.down`. Rows stay click (Share / Cancel). Root stamps `data-channel-id`. Card is not `relative`. |
| `contextmenu` | `ContextMenu` | Click or longpress. Floating panel (`list-none`, rows are `menuitem`). Card no longer `overflow-hidden`. Root stamps `data-channel-id`. |
| `typeahead` | `Typeahead` | Live filter on `input delay:`. The field is the control. |
| `pullrefresh` | `PullRefresh` | Vertical swipe synthesizer. Refresh control accepts `swipe.down`. |

Kit source of truth stays in the library. Product apps **own the copy**.
`from ux_compose.kit import Login` stays for tests, the Atelier, and agents.

`kit/copy.py` is the CLI copier (`KitCopyError`, `copy_component`). It is **not**
a UI widget and is **not** in `CATALOG`. Do not treat it as a 24th component.

---

## 10. Component contract

- `id` is the morph + motion target (default `ClassName.lower()`).
- `render()` returns a ux-dom tag tree (or HTML string, or dict, or generator).
- `@action(caps=(...))` return algebra:
  1. `None` → auto-morph dirty MorphStates
  2. `list[Op]` → exact Ops (auto suppressed)
  3. Prefer `update_with(self, scene(...).enter("#id", rise.enter(ms=140)), extra_ops=[notify("…")])`
- `bind(self.verb, **args)` — symbol-safe, preferred. Also `self.verb.ui(**args)`.
- `control("surface.verb", **args)` — stringly hatch: `data-ux-action` + `data-ux-arg-*`.
- `notify(message, level="info")` — one-shot toast Op.
- `morph_play("#id", plan)` — morph then plan ops (still XOR). Use **once** as the hop hatch.
- `update_with` strategy default is `"idiomorph"`. Morph HTML is live `render()`.
- Do **not** subclass ux-dom `Component`.

```python
app.dispatch("cart.add", sku="tee")
app.dispatch("cart.add", args={"sku": "tee"})   # Channel Intent shape — same call
```

---

## 11. Encoding law

| What | Where |
|---|---|
| Open / value / query / named step / named band / bool | `MorphState` (qualitative) |
| Magnitude, lists, money, ISO dates, files, digits, secrets | `RefState` + `stamp = MorphState("idle")` |
| One-shot message | `notify(...)` |
| Domain stock / money / bookings | **Host store**, never the client plane |
| Protected verb | `@action(caps=("orders.place",))` + live mint |

Chrome is public. Spending money, deleting, or changing identity takes a Cap.

---

## 12. Motion XOR + Morph-then-Play

- **XOR** — `morph(target)` XOR `scene.enter(target, html=...)`. Never both.
- **Morph-then-Play** — morph Op first; `transition.play` follows.
- Plans carry **no** `html=`. Morph HTML is live `render()`.
- Recipes: `scene("name").enter("#id", rise.enter(ms=160))` / `slide.enter()` / `fade.exit()`
- List continuity: stable ids + `scene.stagger_in` + optional `exit("#gone", fade.exit())`
- Shared element: `scene.share(key, leave="#from", arrive="#to", recipe=rise.enter(ms=120))`
- Overlay open: Dialog fade scrim + rise panel; Sheet fade scrim + slide panel. Selectors only.
- Without ux-motion, `scene` / `fade` / `rise` / `slide` are `None` and the same `@action` still morphs.

Cookbook: [cookbooks/PRESENCE.md](https://github.com/bitplorer/ux-compose/blob/main/cookbooks/PRESENCE.md).

---

## 13. Isolation + Document SSoT + Cap Law

1. Product modules never `import ux_channel`, `cek`, `cek_host`, `cek_surface`, `MotionChannel`.
2. Live path only through `App.use_channel` / `use_motion` / `use_cek` (compose `wire/`).
3. Exactly one HTML shell. Overlays stay in the tree when closed.
4. Dual-Document in product files is a doctor fail.
5. `Document.use` may take control, runtime (`XElement`), CSP, style. **Not** HMR, App, host strategy.
6. Protected verbs fail closed without a Channel-minted Cap.
7. `doctor` AST-scans Isolation.

---

## 14. Catalog — 99% of product UI (`examples/`)

Every pattern is one `Component`. Play them: `apps/atelier_studio`.
Product shop: `apps/atelier_shop`. Demo pulse: `apps/pulse`. House: `apps/nook`.

| Group | File | Classes |
|---|---|---|
| Foundation | `foundation.py` | `Counter`, `Toggle`, `Planes` |
| Chrome | `chrome.py` `modal.py` `shell.py` | `Tabs`, `Accordion`, `Dropdown`, `Drawer`, `ConfirmModal`, `AppShell`, `Breadcrumbs`, `BottomNav`, `Popover`, `OverflowMenu` |
| Overlays | `overlays.py` | `Toasts`, `Confirm`, `Lightbox`, `Palette`, `Banner` |
| Forms | `forms.py` `fields.py` | `SignupForm`, `Wizard`, `Search`, `ChoiceGroup`, `Combobox`, `DateField`, `FileDrop`, `SliderField`, `OtpGate` (Cap), `PasswordField`, `Autosave`, `LimitedNote` |
| Collections | `lists.py` `table_board.py` `feeds.py` | `Shelf`, `OptimisticList`, `Pages`, `UndoSnack`, `DataTable`, `Kanban`, `Carousel`, `Comments` (Cap moderate), `Timeline`, `EmptyRetry`, `ReorderList`, `ActivityFeed` |
| Navigation | `navigation.py` | `ShopView`, `MasterDetail` |
| Commerce | `cart.py` `systems.py` `commerce_more.py` | `Cart`, `Stepper`, `Rating`, `Wishlist`, `Coupon` (Cap), `CheckoutFlow` (Cap), `StockBadge`, `CompareTray` |
| Live Caps | `live_caps.py` | `LiveOrder` |
| Motion | `motion_xor.py` | `MotionBox`, `ShareSeat` |
| Systems | `systems.py` `ops.py` | `Chat`, `NotifyCenter`, `Tree`, `Skeleton`, `Consent`, `Theme`, `Chips`, `InlineEdit`, `Calendar` (Cap), `ProgressMeter`, `CopyClip`, `Settings` (Cap), `OfflineBanner`, `Presence`, `KpiStrip`, `Shortcuts` |
| Host | `document_boot.py` `live_asgi.py` `cart_document.py` `page_unit_mount.py` | Document SSoT, `build()` Clock A GET; `App.mount` secondary |

The kit is the **ownable** form of chrome. Examples are the **teaching** form.
A product uses kit copies as chrome and example contracts as domain rooms.
Do not ship a widget zoo.

---

## 15. Wire (not for product imports)

`ux_compose.wire.boot.attach_channel` / `attach_motion` (returns **instances**)
`ux_compose.wire.caps.mint_cap` / `submit_intent` / `async_submit_intent`
`ux_compose.wire.cek.attach_cek`

Authors reach Caps through `App.mint_cap` / `App.submit_intent`.

---

## 16. Names that do **not** exist (do not invent)

- `ux.div` / `when` / `forall` / `Page`
- Product CLI on `uxdom` (`create-app`, product `build`, `serve`, `deploy`)
- Tailwind compiler on ux-dom / `WebAssets` on ux-dom
- HMR as `Document.use`
- `host="batteries"` as a thing to run
- HTTP verbs (`get`/`post`/…) on page units
- FastAPI `default_response_class=HTMLResponse` / `StreamingRoute`
- `Accept` negotiation on page GET
- Kit JS / Channel attrs on motion plans
- Root-level swipe that swallows row clicks
- `from ux_compose.kit import …` as the product path (copy first)
- A 24th kit widget named `copy` (that module is the CLI copier)
- Dual product paths / a copy of Channel codecs, Document serialize, or motion IR
- `tick` / `maybe_plan` as library APIs (product-local helpers only)
- Wrap GET with a synthesized Document
- Channel boot in `App.boot("auto")`
