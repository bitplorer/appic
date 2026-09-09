# ux-compose — complete feature inventory (kit-81 era)

Sourced from [bitplorer/ux-compose](https://github.com/bitplorer/ux-compose) `main`
SHA **`5bb7dc22c9c9a3b9a732a1d180f346165b623b90`** (2026-09-09 walk of
`src/ux_compose/**/*.py`, `kit/catalog.py`, `__all__`, CHANGELOG Unreleased).

Previous APPIC pin `fa2ddfe` is historical. If this page and the code disagree,
**the code wins**.

This is the law for [GROK_BUILD_PROMPT.md](GROK_BUILD_PROMPT.md).

Do not invent a sixth product, a second namespace (`ux.*`), React, Vue, JSX,
HTMX-as-architecture, or a client SPA as source of truth.

---

## 2026-09-09 — independent re-read (delta over `fa2ddfe`)

Walked `src/ux_compose/` + `kit/catalog.py` + `__init__.__all__` + CHANGELOG
Unreleased + `examples/` class roster + `chrome.py` + `doctor.py` + `build.py`.

| Was (`fa2ddfe`) | Now (`5bb7dc22`) |
|---|---|
| Kit catalog **23** stems | Kit catalog **81** stems, `css: False`, `page: True` |
| OverlayChrome used by Dialog / Sheet / ActionSheet | Also AlertDialog + Command. `kind="drawer"` is Sheet-right. `dismiss_on()` appends `keydown.escape`. `focus_attrs()` |
| `__all__` tags stop at `svg, path, rect, circle` | Also `dl, dt, dd, table, thead, tbody, tr, th, td, fieldset, legend, hr, img, progress` |
| No Document GET brand helper | `ux_compose.chrome.brand_wrap(document, brand=…)` + `GET_CHROME_ATTR` + `DEFAULT_BRAND` |
| FastAPI Swagger default-on | Swagger **off**. `build(openapi=True)` or `settings.OPENAPI = True` to opt in. `routes/docs.py` may own GET `/docs` |
| Doctor: isolation, dual-Document, kit-import, leftover aliases | Plus `scan_render_chrome`, `scan_fastapi_docs_collision`, `scan_cek_host` |
| `uxcompose add dialog` did not copy overlay | `add dialog\|sheet\|actionsheet` copies rewritten `components/overlay.py` |
| `optional_*` could return None | Names kept; they **import and use** ux-motion. Not an optional fork |
| Atelier **75/76** Component classes | **73** class statements / **72** unique (`Cart` in `cart.py` + `cart_document.py`) |
| No catalog aliases | `ALIASES = {"treeview": "tree"}` |
| `create-app` any dest name | Rejects reserved basenames (`site`, `test`, `email`, stdlib, keywords) |

Specialist pins (from `pyproject.toml`):

| Package | Pin |
|---|---|
| ux-dom | `e8be99a52bfecd6026c200fa1c3dc6a74f87aacb` |
| ux-channel | `31a60bdd40a1b52aea1fd13159ad09c293c63fd6#subdirectory=python` |
| ux-behavior | `793f120e3b1388925772cd069b070d7918b78baa` |
| ux-motion | `67ff3f0c4912b70b7056f8226a6f226b6fe93f60` |
| cek-host / cek-surface | `>=0.1.3` |

Python floor **≥ 3.14**. Hard-deps. Missing specialists fail loud.

---

## 0. What the package is

Thin pure-Python **composition + delivery** root. It harnesses four specialists
and must **not** reimplement them.

| Specialist | Role | Unlock | Install |
|---|---|---|---|
| **ux-dom** | Tag trees, Document SSoT, serialize, className, `<link>`, package static, CSP | L0 | pinned git SHA |
| **ux-behavior** | `Component`, `MorphState`, `RefState`, `@action`, Ops | L1 | pinned git SHA |
| **ux-channel** | Intent → Cap → Result. Behind compose `wire/` only | L2 | pinned git SHA |
| **ux-motion** | Scene Plans, presence, Morph-then-Play | L3 | pinned git SHA |

| Layer | Name |
|---|---|
| PyPI / pip | `ux-compose` |
| Import | `ux_compose` |
| CLI | **`uxcompose`** (sole product lifecycle) |
| Version | `0.1.0` (`ux_compose.__version__`) |
| Python | **≥ 3.14** |
| License | MIT |
| Current SHA | `5bb7dc22c9c9a3b9a732a1d180f346165b623b90` |

**Progressive Superpower:** Level 1 code remains correct at L2/L3. Zero rewrite.
Levels are additive attach APIs on a **complete install**, not an optional-package
unlock ladder.

Teaching apps: `apps/nook` (kit house), `apps/atelier_studio` (examples cards),
`apps/atelier_shop` (shop / cart / presence), `apps/pulse` (multi-route live).

---

## 1. Public author surface (`ux_compose.__all__`)

Every name **must appear in product source**. Import only from `ux_compose`.
There is no public `ux.div` / `when` / `forall` / `Page`.

### Composition + delivery

| Export | Role |
|---|---|
| `App` | `boot`, `add`, `mount`, `use_host`, `use_dom`, `use_behavior`, `use_channel`, `use_motion`, `use_cek`, `mint_cap`, `submit_intent`, `submit_intent_async`, `dispatch`, `control`, `doctor`, `level`, `behavior`, `attach_notes` |
| `build` | Orchestra. Returns `BuildResult` = `(app, asgi, bundle)` |
| `WebAssets` | App CSS/JS folders. `from_app_root`, `ensure`, `mount_css`, `css_href`, `input_css`, `output_css`. Static emit `ETag` / `Last-Modified` |
| `DirectoryRoutes` | Filesystem → `RouteRecord`. One path law: `http_path` |
| `DirectoryASGI` | Pure-ASGI host. No Starlette |
| `RouterHooks` | `resolve_unit`, `accept_symbol`, `on_route` |
| `Surface` / `SurfaceBundle` / `SurfaceError` | Catalog unit + sealed evidence |
| `mount_surfaces` / `scan_surfaces` / `validate_surfaces` | Discover define-in-module units under `routes/` |
| `Level` | `L0..L3`. Labels: `static + routing` / `offline interactive` / `live channel` / `motion` |
| `doctor` / `DoctorResult` | Isolation, dual-Document, kit-import, leftover aliases, render-chrome, FastAPI docs collision, CEK host |
| `__version__` | `"0.1.0"` |

`build(package_dir, *, name="App", host="auto", live="auto", level="auto",
base="routes", fail_closed=True, use_htmx=False, asgi_app=None, document=None,
wrap=_UNSET, cek="require", openapi=_UNSET)`

- `cek="require"` — product Cap Host (cek-runtime). Skip when `live="null"`.
  `adapt` is compare-only lab. `off` is honest off.
- `openapi` default **False** so `routes/docs.py` can own GET `/docs`.
- `wrap=` is author Document wrap. `brand_wrap(document, brand=…)` is the GET
  chrome door. Morph HTML must **not** include brand.
- `use_htmx=False`.
- `host="auto"` (FastAPI). `host="batteries"` fails closed
  (`ProductBatteriesRejected`).
- `materialize(route_class=)` fails closed.
- `App.boot("auto")` is Level 1. Channel attaches in `build()` once ASGI exists.

### Behavior (via ux-behavior)

`Component`, `MorphState`, `RefState`, `action`, `bind`, `control`, `notify`,
`update_with`, `morph_play`

XOR: `update_with` may put `html=` on the **morph payload**. Plans carry **no**
`html=`. Morph first from `render()`, then `transition.play`. Prefer
`bind(self.verb)`; `control("surface.verb")` is the stringly hatch.

### Author door (ADR 0004)

```
act(action, label, *, kind="secondary", target="#stage", on=None, **args)
    POST form to /act/{action}. control() attrs on the submit button.
    Hidden inputs for **args. data-ux=1, data-target={target}.
    on= stamps data-channel-on. className btn-{kind}; form className "inline".

mark_dirty(comp, *, on="tick", off="tock")
    Flip comp.dirty. Never a private _tick.

field(name, value="", *, placeholder="", kind="text")
    className="field". autocomplete="off".

status(text, *, kind="note")
    empty → span("", className="sr"); else status status-{kind} role="status".

optional_plan(name, target, *, ms=140)   → scene.enter(target, rise.enter)
optional_fade(name, target, *, ms=120)   → scene.enter(target, fade.enter)
optional_slide(name, target, *, direction="next"|"prev", ms=180)
    dist from ux_motion.tokens.dist("md")
```

Product imports these from `ux_compose`. Never `from examples._common import`.

### Attach notes

```
@dataclass(frozen=True)
class AttachNote:
    door: str
    wanted: str
    reason: str
    level_kept: int = 1
```

`attach_notes()`, `App.attach_notes`, submodule `note` / `using` / `format_report`
/ `current` / `clear` (test-only). Silence was the defect. Not a message bus.

### Motion (via ux-motion)

`scene`, `fade`, `rise`, `slide` — hard deps. `morph_play` is the hop helper.

### DOM tags (via ux-dom)

`HAS_DOM`, `raw`, `html`, `head`, `body`, `title`, `style`, `meta`, `link`,
`script`, `div`, `span`, `h1`, `h2`, `h3`, `p`, `a`, `button`, `form`, `input_`,
`ul`, `li`, `header`, `footer`, `aside`, `section`, `article`, `nav`, `main`,
`label`, `svg`, `path`, `rect`, `circle`,
**`dl`, `dt`, `dd`, `table`, `thead`, `tbody`, `tr`, `th`, `td`, `fieldset`,
`legend`, `hr`, `img`, `progress`**.

### Chrome (compose submodule, not `__all__` but product-required)

```
from ux_compose.chrome import brand_wrap, GET_CHROME_ATTR, DEFAULT_BRAND
```

`brand_wrap(document, brand="APPIC")` returns `wrap(child)` that places nav brand
**outside** `Component.render()`. Clock A GET includes brand once. Clock B morph
HTML has brand=0. Requires a callable Document. There is no Document-absent string
shell. Doctor `scan_render_chrome` flags `stunning-root` and `class="nav"` + brand
inside `routes/*.py` `render()`.

---

## 2. Kit catalog — 81 stems

`css: False`. `page: True`. Markup is Tailwind `className`. Own via
`uxcompose add {stem}`. Product never `from ux_compose.kit import Login` as the
live unit. OverlayChrome is **not** a catalog stem; `add dialog|sheet|actionsheet`
copies `components/overlay.py` as a rewritten sibling. Alias: `treeview` → `tree`.
`drawer` is a Sheet alias (same Host, right edge) — not a second overlay Host.

### Wave 0 — original 23

| Stem | Export | Law |
|---|---|---|
| login | Login, AuthDecision | Mode tabs tablist+tabpanel. Secrets never MorphState. Submit Cap |
| tabs | Tabs | `{id}-tab-{k}` / `{id}-p-{k}`. Inactive stay `hidden` |
| accordion | Accordion | Open ids MorphState tuple. `{id}-p-{key}` |
| dropdown | Dropdown | Menu is presence. Value is a named key. Anchored family |
| dialog | Dialog | Public ask, Cap confirm. OverlayChrome center. `on_confirm()` |
| sheet | Sheet | Right edge. Close/Done `swipe.right`. No root swipe |
| toast | Toast | Server list is authority. Sealed-args must be html-unescaped |
| command | Command | Palette. Query attaches. Sign out spends `auth.logout`. OverlayChrome |
| table | Table | Sort MorphState, selection RefState. Bind checkbox, not `<tr>` |
| pagination | Pagination | Opaque keys. Windowed numbers. `page_slots` |
| combobox | Combobox | Type then pick. `{id}-form` / `{id}-opt-n`. Anchored |
| sidebar | Sidebar | Collapsible rail. Active key MorphState |
| breadcrumb | Breadcrumb | Named crumbs. Walking back is public |
| stepper | Stepper | Named steps. Finish spends `stepper.finish` |
| carousel | Carousel | Named slides. Overlay chevrons. Sliding pip coalesces |
| calendar | Calendar | `role=grid` + row/gridcell. Day is a name. `on_pick()` |
| select | Select | Grouped options. Label for ↔ trigger. Anchored |
| otp | Otp | Six digits RefState. Verify spends `auth.otp` |
| plans | Plans | Radio group. `role=radio` `aria-checked`. `on_choose()` |
| actionsheet | ActionSheet | Bottom. Autofocus. Handle swipe-down. Rows stay click |
| contextmenu | ContextMenu | Click or `longpress`. `aria-controls`. Anchored |
| typeahead | Typeahead | `input delay:300`. Hits morph `#{id}-hits` **only** |
| pullrefresh | PullRefresh | Vertical swipe synthesizer. Refresh accepts `swipe.down` |

### Expansion — chrome / overlay / form / status / marketing

| Stem | Export | Law |
|---|---|---|
| drawer | Drawer | Sheet alias. Same Host. Right edge |
| navbar | Navbar | Landmark. Desktop + mobile are **two trees** |
| navmenu | NavMenu | Disclosure of named destinations |
| usermenu | UserMenu | Identity menu. Sign-out spends `auth.logout` |
| popover | Popover | Non-modal, anchored. Escape dismisses. Not OverlayChrome |
| tooltip | Tooltip | `role=tooltip` described-by. Not a modal |
| alertdialog | AlertDialog | `role=alertdialog`. Escape/scrim do **not** dismiss. Confirm Cap |
| formlayout | FormLayout | label for ↔ id. Submit spends `form.submit` |
| fieldset | Fieldset | Native fieldset + legend radiogroup |
| datepicker | DatePicker | Day key + month grid. Day is a name, not a quantity |
| switch | Switch | `role=switch`. Boolean MorphState. Public |
| card | Card | Titled article with a public action |
| emptystate | EmptyState | Void region + CTA. Filling is public Morph |
| stats | Stats | Named metrics on RefState. `dirty` is the morph clock |
| alert | Alert | Inline `role=alert`. Dismiss public |
| banner | Banner | Page-level region notice. Not `role=alert` |
| progress | Progress | `progressbar`. Magnitude RefState, never MorphState |
| skeleton | Skeleton | `aria-busy`. Bars `aria-hidden` |
| hero | Hero | Landing band with a public CTA |
| footer | Footer | `contentinfo`. Named links, `aria-current` |
| cta | Cta | Titled call to action. Demo act public |
| avatar | Avatar | Initials `role=img` `aria-label` |
| badge | Badge | Named status chips. `aria-pressed` on selected |
| hovercard | HoverCard | Non-modal preview. Escape dismisses. Anchored |
| searchbar | SearchBar | Labeled search. Hits are a listbox |
| fileupload | FileUpload | Names on RefState. Demo names `sketch.png` |
| tagsinput | TagsInput | Named chips + labeled field. List RefState |
| multiselect | MultiSelect | Multi listbox. Select-all is not a row toggle |
| descriptionlist | DescriptionList | `dl/dt/dd` facts. Not a data table |
| featuregrid | FeatureGrid | Named tiles. Active key MorphState |
| testimonials | Testimonials | Named quotes. `which` is a key, not a quantity |
| newsletter | Newsletter | Labeled email. Subscribe spends `list.subscribe` |
| bottomnav | BottomNav | Mobile sections landmark. `aria-current` |
| separator | Separator | Composite labeled rule. Not a bare `hr` atom |
| slider | Slider | Labeled range. Magnitude RefState. `role=slider` |

### Batch A — chrome P1 (APG)

| Stem | Export | Law |
|---|---|---|
| menubar | Menubar | APG menubar. Submenu ids `{id}-m-{key}` stay in tree with `hidden` |
| toolbar | Toolbar | Groups + separators. Last command `aria-current` (not pressed) |
| togglegroup | ToggleGroup | Exclusive radiogroup. Value is a name. Not Tabs (no panels) |
| spinbutton | SpinButton | APG spinbutton. Magnitude RefState. Label for ↔ id. Not Stepper |
| themeswitch | ThemeSwitch | Named theme radiogroup (light/dark/system). Not a boolean switch |
| filterbar | FilterBar | Labeled query + named filter radiogroup. Hits filter in place |

### Batch B — product

| Stem | Export | Law |
|---|---|---|
| chat | Chat | Thread `role=log`. Composer labeled. Send is public |
| questionnaire | Questionnaire | Named questions as fieldset radiogroups. Submit spends `form.submit` |

### Batch C — marketing

| Stem | Export | Law |
|---|---|---|
| pricingsection | PricingSection | Comparison table. Choose binds the **button**, not the row |
| logocloud | LogoCloud | Named marks with alt. Selected `aria-pressed` |
| timeline | Timeline | Named event lanes. Filter radiogroup. Not FilterBar |
| rating | Rating | Named stars (`one`…`five`). Radiogroup. Never MorphState(int) |

### Batch D — P2

| Stem | Export | Law |
|---|---|---|
| chart | Chart | Named SVG bars. Heights RefState. `role=img` labelled |
| resizable | Resizable | Named split (even/wide/rail). Radiogroup + labelled separator |
| tree | Tree | APG treeview. Expanded ids are names. `add treeview` resolves here |
| colorpicker | ColorPicker | Named swatches radiogroup. Hex field labeled |
| fab | Fab | Speed-dial. Menu id `{id}-menu` always in the tree (`hidden` when closed) |
| diff | Diff | Named before/after. Radiogroup |
| countdown | Countdown | `role=timer`. Remaining RefState. Not SpinButton |
| mockup | Mockup | Named device frame. Radiogroup |
| attachment | Attachment | File name chips on RefState. Label for ↔ id |
| scrollarea | ScrollArea | Labelled overflow pane. Named jump. Composite, not a raw atom |
| feed | Feed | APG feed of articles. Items RefState. Append public |

Copy press (not a card): `copy_component(name, *, root=None, force=False, as_page=False)`,
`find_app_root`, `KitCopyError`, `list_components`, `resolve`, `KitEntry`, `CATALOG`.

---

## 3. OverlayChrome exact tables (`kit/overlay.py`)

```
KIND_EDGE = {modal,dialog→center; sheet,drawer→right; action,actionsheet→bottom}
EDGE_SWIPE = {center: click swipe.down; right: click swipe.right;
              left: click swipe.left; bottom: click swipe.down; top: click swipe.up}
HANDLE_SWIPE = {bottom: click swipe.down swipe.vertical threshold:48;
                top:    click swipe.up   swipe.vertical threshold:48}
EDGE_SLIDE = {right: x=28.0; left: x=-28.0; bottom: y=32.0; top: y=-32.0}
ids: {root}-scrim / {root}-panel / {root}-dismiss
dismiss_on() = swipe_on_dismiss() + " keydown.escape"
open_plan() selectors-only (no html=). Close stays morph-only.
focus_attrs() → {tabindex: "-1"}
```

**Edge family (OverlayChrome):** Dialog, Sheet, Drawer (alias), ActionSheet,
AlertDialog, Command.

**Anchored family (do not reuse OverlayChrome ids):** Dropdown, ContextMenu,
Combobox, Select, Popover, Tooltip, HoverCard, UserMenu, NavMenu.

Root `swipe.*` on an overlay card is a defect (swallows row clicks).

---

## 4. Wave 1 Channel grammar

| Token | Meaning | Where it is legal |
|---|---|---|
| `click` | tap / mouse | every control; always keep click on dismiss |
| `swipe.down` / `.up` / `.left` / `.right` | edge dismiss | OverlayChrome dismiss, **never** the overlay root |
| `swipe.vertical` | let row clicks survive | ActionSheet handle |
| `threshold:48` | px before swipe commits | handle only |
| `input delay:300` | pause-fired live filter | Typeahead field (`data-channel-on`) |
| `longpress` | floating panel | ContextMenu |
| `keydown.escape` | public close | OverlayChrome `dismiss_on()`; **not** AlertDialog scrim/escape |

Typeahead: live Results morph `#{id}-hits` only. The field is **not** in that
HTML. Query is RefState. Value is MorphState (the chosen name).

---

## 5. Encoding rule (session plane)

| What | Where |
|---|---|
| Open / value / query / named step / named band / named star | `MorphState` (qualitative) |
| Magnitude, lists, money, ISO dates, files, digits, hex, remaining | `RefState` + `dirty = MorphState("idle")` then `mark_dirty(self)` |
| One-shot message | `notify(...)` |
| Domain stock / money source | Host DB, never the client plane |
| Protected verb | `@action(caps=("orders.place",))` + live `submit_intent` |
| Email / password / OTP digits | RefState. Never MorphState |

Channel's session plane **refuses quantity MorphState** (ints, numeric strings).
Rating stars are named keys (`one`…`five`). Countdown remaining is RefState.
SpinButton magnitude is RefState. Chart heights are RefState.

Login: `AuthDecision = NamedTuple(ok: bool, message: str = "", blocked: bool = False)`.
Show/Hide and tab switches attach live form values onto RefState *before* the morph.
Submit spends `auth.login` / `auth.signup`. OTP verify spends `auth.otp`.

---

## 6. Doctor scan families

`doctor(paths, *, fail=True, bundle=None) -> DoctorResult`

| Family | Function | Rule | Fail-close? |
|---|---|---|---|
| Hard | `scan_isolation` | `ux_channel`, `cek`, `cek_host`, `cek_surface`, `MotionChannel` | yes (`IsolationViolation`) |
| Hard | `scan_dual_document` | more than one `Document()` in product trees | yes |
| Teaching | `scan_kit_product_imports` | `from ux_compose.kit import` in product | **no** |
| Teaching | `scan_leftover_aliases` | `host="batteries"`, `DirectoryRouter`, `serve="webassets"` | **no** |
| Teaching | `scan_render_chrome` | GET chrome (`stunning-root`, `class="nav"` + brand) inside `routes/*.py` `render()` | **no** |
| Teaching | `scan_fastapi_docs_collision` | surface path collides `/docs` `/redoc` `/openapi.json` | **no** |
| Teaching | `scan_cek_host` | `cek=require` + Channel live but registry is not `CekHostCapService` / `kernel_ssot=cek-runtime` | **no** (doctor fail-loud on incomplete stack unless `--no-fail`) |

`DoctorResult`: `ok`, `level_available`, `diagnostics`, `capabilities`,
`teaching`, `surfaces`, `routes`, `raise_if_failed()`.

---

## 7. Delivery / CLI / DX

```
uxcompose create-app myapp --level 1 [--brand LABEL]
uxcompose serve dev          # origin + ui + channel + CSS watch
uxcompose serve prod         # clocks hard off
uxcompose serve restart-channel
uxcompose build              # Tailwind minify → /css/output.css
uxcompose deploy --provider docker|fly|render|railway|vps|checklist
uxcompose doctor .
uxcompose add {stem}
uxcompose add --list
```

- `uxcompose serve` without a mode **exits 2**.
- Tunnel (`--tunnel ngrok|cloudflare`, aliases `cf` / `cloudflared` / `trycloudflare`)
  starts **after** origin health is green.
- Deploy runs raw uvicorn, not `serve`. `prepare_deploy` does not upload.
- HMR path: `/__uxcompose/hmr`. `attach_hmr`, `client_script_tag`, `HmrClientMiddleware`.
- CSS: `CSS_URL_PREFIX=/css`, `OUTPUT_CSS_NAME=output.css`.
- `probe()` / `ProbeResult` — import-spec only. Never shells. Never starts a server.
- `create-app` rejects reserved dest basenames (`site`, `test`, `email`, …).
- Scaffold emits `routes/index.py` so GET `/` is not 404. `/hello` stays.
- `[serve]` extra: uvicorn, watchfiles, httpx, starlette, websockets.

WebAssets disk: `assets/css/input.css` → `assets/static/file/css/output.css`.

Package-static escape hatch is `serve="dual_copy"` (`serve="webassets"` leftover).

---

## 8. Clock A payload law

Page units have **no HTTP verbs**. Host wraps `render()`. Payload type picks
media type, not Accept.

| `render()` returns | Media |
|---|---|
| tree / str | HTML (Document wrap, CSP, Content-Length) |
| dict | JSON |
| generator / async generator | stream |
| Response | as-is |

One path law (`http_path`): `index.py` / `route.py` → `/`, `[param]` → `{param}`.

---

## 9. Atelier roster — 73 class statements / 72 unique

`examples/` is the Atelier, not a second catalog.

Foundation: Counter, Toggle, Planes.
Chrome: Tabs, Accordion, Dropdown, Drawer.
Shell: AppShell, Breadcrumbs, BottomNav, Popover, OverflowMenu.
Overlays: Toasts, Confirm, Lightbox, Palette, Banner.
Forms: SignupForm, Wizard, Search.
Fields: ChoiceGroup, Combobox, DateField, FileDrop, SliderField, OtpGate,
PasswordField, Autosave, LimitedNote.
Lists: Shelf, OptimisticList, Pages, UndoSnack.
Feeds: Carousel, Comments, Timeline, EmptyRetry, ReorderList, ActivityFeed.
Table/board: DataTable, Kanban.
Nav: ShopView, MasterDetail.
Commerce: Cart (two host demos), Wishlist, Coupon, CheckoutFlow, StockBadge,
CompareTray, Rating.
Live Caps: LiveOrder.
Motion: MotionBox, ShareSeat.
Systems: Chat, NotifyCenter, Tree, Skeleton, Consent, Theme, Stepper, Chips,
InlineEdit.
Ops: Calendar, ProgressMeter, CopyClip, Settings, OfflineBanner, Presence,
KpiStrip, Shortcuts.
Host: Badge (`document_boot`), ConfirmModal (`modal.py`).

---

## 10. Leftovers expire by teaching

| Leftover | Prefer |
|---|---|
| `from ux_compose.kit import` in an app | `uxcompose add` then own `components/` |
| `host="batteries"` / `DirectoryRouter` | `host="auto"` |
| `serve="webassets"` | `serve="dual_copy"` |
| Teaching `App.mount` as the product path | `build()` |
| Root `swipe.*` on an overlay card | swipe on dismiss / handle |
| `from examples._common import` | `from ux_compose import act, mark_dirty, field, …` |
| private `_tick` | `mark_dirty(comp)` |
| GET chrome inside `render()` | `build(wrap=brand_wrap(document, brand=…))` |
| FastAPI Swagger eating `/docs` | keep `openapi` off; own `routes/docs.py` |
| Quantity MorphState | RefState + `mark_dirty` |
| Plans with `html=` | XOR. Morph first |
| HTMX as architecture | `use_htmx=False` |
