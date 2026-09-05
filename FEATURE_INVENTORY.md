# ux-compose — complete feature inventory (delivery era · ADR 0004 · WebAssets · deploy)

Sourced from [bitplorer/ux-compose](https://github.com/bitplorer/ux-compose) `main`
(`7ea3eb8813d280a975c4a41d23a2e2d4de40a506`, refreshed 2026-09-05,
**0.1.0 / Clock A + ownable kit + OverlayChrome + author door + attach notes
+ Typeahead hits-slot + serve-dev split + soft morph + copy press + doctor
scan families + Presence cookbook + WebAssets + prepare_deploy + tunnel
+ HMR delivery + restart-channel + Tailwind resolver + probe**).


Public names: `src/ux_compose/__init__.py` `__all__`.
Kit catalog: `src/ux_compose/kit/catalog.py`.
Copy press (not a card): `src/ux_compose/kit/copy.py`.
Overlay primitive: `src/ux_compose/kit/overlay.py` (**not** a catalog stem).
Author helpers: `src/ux_compose/author.py`.
Attach notes: `src/ux_compose/attach_notes.py`.
Doctor: `src/ux_compose/doctor.py`.
Presence: `cookbooks/PRESENCE.md`.
Shape: `docs/ARCHITECTURE.md`. Decision: `docs/adr/0004-clarity-and-residuals.md`.
Serve clocks: `docs/adr/0005-serve-dev-split.md`. Host: `docs/reference/host.md`.

If this page and the code disagree, **code wins**. Do not invent a sixth product,
a second namespace (`ux.*`), React, Vue, JSX, HTMX-as-architecture, or a
client SPA as source of truth.

This is the law for [GROK_BUILD_PROMPT.md](GROK_BUILD_PROMPT.md).

---

## 0. Three doors (ADR 0004)

After 0.1.0 shipped, three widget worlds (`kit/`, `examples/`, `apps/`), two
taught HTTP doors (`build()` and `App.mount`), a shadow helper module
(`examples/_common.py`), copy-pasted overlay chrome, and silent
`except ImportError` made the repo look like it had more products than it does.

ADR 0004 closed that. APPIC must **walk** these three doors — not document them.

| Door | Rule | Product room |
|---|---|---|
| **One author door** | Public helpers live in `ux_compose.author` and are re-exported from `ux_compose.__all__`. `examples/_common.py` re-exports the **same** objects. There is no second helper world. Product never `from examples._common import`. | `/author` |
| **One product door** | `create-app` → `serve dev` → `build` → `serve prod`. `App.mount` is the scan step inside `build()` — one implementation, two callers. | `/relay` + `/clocks` |
| **One catalog** | `ux_compose.kit` is the source. `uxcompose add` copies. `examples/` is the Atelier, not a second catalog. Product trees do not import the kit as the live card. | Desk / House / Visit / Door / `/copy` |

Plus residuals that became rooms:

| Residual | Rule | Product room |
|---|---|---|
| **Attach notes refuse silence** | Missing specialists write `AttachNote` instead of raising. Per-App notebook. Dual-write to a process notebook for doctor. Not a message bus. | `/notes` |
| **OverlayChrome is the edge primitive** | Dialog / Sheet / ActionSheet take ids, dismiss/handle grammar, and the open plan from it. Anchored popovers and Command are a **different family**. | `/overlay` vs House |
| **The copy press is not a card** | `kit/copy.py` (`copy_component`, `find_app_root`, `KitCopyError`) is the ownership ritual. Not in `CATALOG`. OverlayChrome is copied by hand. | `/copy` |
| **Doctor residuals expire by teaching** | Isolation + dual-Document are hard. Kit-import and leftover aliases (`host="batteries"`, `DirectoryRouter`, `serve="webassets"`) are teaching. Doctor does not fail-close on teaching. | `/trace` |
| **Presence is continuous** | Stable ids. `stagger_in` on survivors. `scene.share` key is identity, not a CSS class. Same `@action` morphs when `scene is None`. | `/atelier` + `/bag` |
| **Skin is WebAssets** | `css_href`, `/css/output.css`, ETag / Last-Modified. First token is CSS. `serve="webassets"` leftover vs `serve="dual_copy"`. | `/skin` |
| **Ship is prepare_deploy** | Six providers. `DeployResult`. Prepare is a Cap. GET does not write. Tunnel `parse_provider` after health. | `/deploy` |

Leftovers expire by teaching. Doctor flags them in product trees. It does **not**
fail-close on them. Deleting aliases while 0.1 tests lock them is a capability drop.

| Leftover | Prefer |
|---|---|
| `from ux_compose.kit import` in an app | `uxcompose add` then own `components/` |
| `host="batteries"` / `DirectoryRouter` | `host="auto"` |
| `serve="webassets"` | `serve="dual_copy"` (package-static escape hatch) |
| Teaching `App.mount` as the product path | `build()` |
| root `swipe.*` on an overlay card | swipe on dismiss / handle |
| `from examples._common import` in product | `from ux_compose import act, tick, field, …` |
| private `_tick` | official `tick(comp)` |

---

## 1. What the package is

Thin pure-Python **composition + delivery** root. It harnesses four specialists
and must **not** reimplement them.

| Specialist | Role | Unlock | Install |
|---|---|---|---|
| **[ux-dom](https://github.com/bitplorer/ux-dom)** | Tag trees, Document SSoT, serialize, className, `<link>`, package static, CSP stamp | L0 | `git+https://github.com/bitplorer/ux-dom.git` |
| **[ux-behavior](https://github.com/bitplorer/ux-behavior)** | `Component`, `MorphState`, `RefState`, `@action`, Ops | L1 | `git+https://github.com/bitplorer/ux-behavior.git` |
| **[ux-channel](https://github.com/bitplorer/ux-channel)** | Intent → Cap → Result. Behind compose `wire/` only | L2 | `git+https://github.com/bitplorer/ux-channel.git#subdirectory=python` |
| **[ux-motion](https://github.com/bitplorer/ux-motion)** | Scene Plans, presence, Morph-then-Play (`transition.play`) | L3 | `git+https://github.com/bitplorer/ux-motion.git` |

| Layer | Name |
|---|---|
| PyPI / pip | `ux-compose` |
| Import | `ux_compose` |
| CLI | **`uxcompose`** (sole product lifecycle) |
| Version | `0.1.0` (`ux_compose.__version__`) |
| Python | ≥ 3.11 classifiers (ux-dom full stack needs ≥ 3.14; sandbox 3.10 vendors source) |
| License | MIT |
| Current SHA | `7ea3eb8813d280a975c4a41d23a2e2d4de40a506` |

**Progressive Superpower:** Level 1 code remains correct at L2/L3. Zero rewrite.
If you rewrite a Component “to go live”, you have violated the contract.

Teaching apps (play before inventing widgets):

| App | Role |
|---|---|
| `apps/atelier_studio` | Atelier of Patterns — every `examples/` card |
| `apps/atelier_shop` | Product shop / cart / presence |
| `apps/pulse` | Multi-route live product |
| `apps/nook` | **Kit house.** Every ownable kit component sits in a real room, not a kitchen-sink gallery |

---

## 2. Public author surface (`ux_compose.__all__`)

Import **only** from `ux_compose`. There is no public `ux.div` / `when` /
`forall` / `Page`.

### Composition + delivery (compose-owned)

| Export | Role |
|---|---|
| `App` | `boot`, `add`, `mount`, `use_host`, `use_dom`, `use_behavior`, `use_channel`, `use_motion`, `use_cek`, `mint_cap`, `submit_intent`, `submit_intent_async`, `dispatch`, `control`, `doctor`, `level`, `behavior`, `attach_notes` |
| `build` | Orchestra: `host.open` → L1 boot → document → Channel on asgi → discover → `host.bind`. Returns `BuildResult` = `(app, asgi, bundle)` |
| `WebAssets` | App CSS/JS folders. `from_app_root`, `ensure`, `mount_css`, `css_href`, `input_css`, `output_css`. Static emit `ETag` / `Last-Modified` |
| `DirectoryRoutes` | Filesystem → `RouteRecord`. One path law: `http_path` |
| `DirectoryASGI` | Pure-ASGI host. No Starlette |
| `RouterHooks` | `resolve_unit`, `accept_symbol`, `on_route` |
| `Surface` / `SurfaceBundle` / `SurfaceError` | Catalog unit + sealed evidence |
| `mount_surfaces` / `scan_surfaces` / `validate_surfaces` | Discover define-in-module units under `routes/` |
| `Level` | `L0..L3`. Labels: `static + routing` / `offline interactive` / `live channel` / `motion` |
| `doctor` / `DoctorResult` | Isolation AST scan, dual-Document heuristic, capabilities, leftover teaching |
| `__version__` | `"0.1.0"` |

`materialize(route_class=)` **fails closed**. `host="batteries"` **fails closed**.
`App.boot("auto")` is Level 1. Channel attaches in `build()` once ASGI exists.
`app.use_cek(mode="adapt")` — never `mode="require"`. Package-static escape
hatch is `serve="dual_copy"` (`serve="webassets"` is a leftover alias).

### Behavior (via ux-behavior)

`Component`, `MorphState`, `RefState`, `action`, `bind`, `control`, `notify`,
`update_with`, `morph_play`

XOR: `update_with` may put `html=` on the **morph payload**. Plans carry **no**
`html=`. Morph first from `render()`, then `transition.play`. `morph_play` is
the hop helper (Lab, once). Prefer `bind(self.verb)`; `control("surface.verb")`
is the stringly hatch.

### Author door (ADR 0004) — exact signatures

```
act(action, label, *, kind="secondary", target="#stage", on=None, **args)
    POST form bound to /act/{action}. control() attrs on the submit button.
    Hidden inputs for **args. data-ux=1, data-target={target}.
    on= stamps data-channel-on. className btn-{kind}; form className "inline".

tick(comp, *, on="tick", off="tock")
    Flip a qualitative MorphState stamp so RefState-only mutations morph.
    Reads/writes comp.stamp. Product code uses this — never a private _tick.

field(name, value="", *, placeholder="", kind="text")
    One input helper. className="field". autocomplete="off".

status(text, *, kind="note")
    Live region. Empty text → span("", className="sr"). Else status status-{kind} role="status".

maybe_plan(name, target, *, ms=140)   → scene.enter(target, rise.enter) or None
maybe_fade(name, target, *, ms=120)   → scene.enter(target, fade.enter) or None
maybe_slide(name, target, *, direction="next"|"prev", ms=180)
    → scene.enter(target, slide.enter(x=±dist)) or None
    dist from ux_motion.tokens.dist("md"), else 24.0
    prev → −dist, next → +dist
```

`examples/_common.py` re-exports these same objects **and** optional
`scene` / `rise` / `fade` / `slide` (None when ux-motion is absent). Product
imports from `ux_compose`. A private `_tick` or a second `act()` in
`appic/ux.py` that posts a different URL is a second helper world — forbidden.

### Attach notes

```
@dataclass(frozen=True)
class AttachNote:
    door: str          # e.g. "use_channel"
    wanted: str        # e.g. "ux-channel"
    reason: str        # why it stepped down
    level_kept: int    # default 1
```

| Name | Role |
|---|---|
| `AttachNote` | Frozen step-down record |
| `attach_notes()` | Snapshot of the **active** notebook (process-wide when no App is bound) |
| `App.attach_notes` | This App's notebook. Two Apps in one process do not leak |
| `note()` (submodule) | Record a step-down. Never raises. Dual-writes process notebook when an App is bound |
| `using(notes)` (submodule) | Bind a notebook as active for a block |
| `format_report()` (submodule) | `"attach {door}: wanted {wanted}, kept L{n} ({reason})"` |
| `clear()` (submodule) | Test helper — do not call from product |

Silence was the defect. Missing specialists write a note instead of raising.
This is **not** a message bus and **not** part of HMR.

### Doctor scan families

`doctor(paths, *, fail=True, bundle=None) -> DoctorResult`

| Family | Function | Tokens / rule | Fail-close? |
|---|---|---|---|
| Hard | `scan_isolation` | `ux_channel`, `cek`, `cek_host`, `cek_surface`, `MotionChannel` | yes (`IsolationViolation`) |
| Hard | `scan_dual_document` | more than one `Document()` in product trees | yes |
| Teaching | `scan_kit_product_imports` | `from ux_compose.kit import` / `from ux_compose.kit.X import` (skips tests, `src/ux_compose`, examples) | **no** |
| Teaching | `scan_leftover_aliases` | `host="batteries"`, `use_host("batteries")`, `DirectoryRouter`, `serve="webassets"` | **no** |

`DoctorResult`: `ok`, `level_available`, `diagnostics`, `capabilities`,
`teaching`, `surfaces`, `routes`, `raise_if_failed()`.
Capabilities from `ux_compose.dx.probe` (`ux_dom`, `ux_behavior`, `ux_motion`,
`ux_channel`, `directory_routes`). Teaching includes product path, one-catalog
rule, and `format_report()` attach notes. Hard diagnostics contain
`"violation"` or `"dual-document risk"`.

Public from `ux_compose.doctor` (not all on package `__all__`):
`IsolationViolation`, `scan_isolation`, `scan_kit_product_imports`,
`scan_leftover_aliases`. `scan_dual_document` exists and is invoked by
`doctor()` — do not invent a sixth scan.

### Motion (via ux-motion, else `None`)

`scene`, `fade`, `rise`, **`slide`**

Compose wraps a Scene/Plan as one `transition.play` Op. Authors never emit
Channel wire shape. Plans carry **no** `html=`. Morph first from `render()`,
then play.

### Tags (via ux-dom when installed; else `HAS_DOM=False`)

`raw`, `html`, `head`, `body`, `title`, `style`, `meta`, `link`, `script`,
`div`, `span`, `h1`, `h2`, `h3`, `p`, `a`, `button`, `form`, `input_`,
`ul`, `li`, `header`, `footer`, `aside`, `section`, `article`, `nav`, `main`,
`label`, `svg`, `path`, `rect`, `circle`

Do **not** subclass ux-dom `Component` (MRO collides).

### Submodule names (from compose, never from `ux_channel`)

`ActionInfo`, `BuildResult`, `RouteRecord`, `DirectoryRoutesError`,
`http_path`, `is_json_payload`, `is_stream_payload`, `apply_html_document`,
`HMR_PATH` (`/__uxcompose/hmr`), `attach_hmr`, `client_script_tag`,
`IsolationViolation`, `scan_isolation`, `scan_kit_product_imports`,
`scan_leftover_aliases`, `scan_dual_document`,
`CSS_URL_PREFIX` (`/css`), `OUTPUT_CSS_NAME` (`output.css`)

---

## 3. OverlayChrome — edge primitive (not a catalog stem)

`ux_compose.kit.overlay` (`OverlayChrome`, `overlay()`). Copied to
`components/overlay.py` with the widgets. **Not** listed by `uxcompose add --list`.
Copy the file by hand (or with the widgets). Do not invent a fourth overlay family.

```
overlay(root_id, *, kind=None, edge=None) -> OverlayChrome
```

`kind` picks the default edge when `edge` is omitted.

### Kind → edge

| kind | edge |
|---|---|
| `modal` / `dialog` | `center` |
| `sheet` / `drawer` | `right` |
| `action` / `actionsheet` | `bottom` |

### Ids (stable, never invent)

| Property | Value |
|---|---|
| `scrim_id` | `{root_id}-scrim` |
| `panel_id` | `{root_id}-panel` |
| `dismiss_id` | `{root_id}-dismiss` |

### Dismiss grammar — never the root

Root `swipe.*` swallows row clicks (ActionSheet / Sheet defect). Dismiss keeps
`click` so a tap still works without a finger swipe.

| edge | `swipe_on_dismiss()` |
|---|---|
| `center` | `click swipe.down` |
| `right` | `click swipe.right` |
| `left` | `click swipe.left` |
| `bottom` | `click swipe.down` |
| `top` | `click swipe.up` |

### Handle grammar — ActionSheet / top sheets

Handle adds vertical so row clicks survive. Dismiss does **not**.

| edge | `swipe_on_handle()` |
|---|---|
| `bottom` | `click swipe.down swipe.vertical threshold:48` |
| `top` | `click swipe.up swipe.vertical threshold:48` |
| other | same as `swipe_on_dismiss()` |

### Shipped enter distances (`open_plan()`)

`open_plan(*, fade_ms=120, enter_ms=180)` is **selectors-only** (no `html=`).
Close stays morph-only: after apply the panel is gone, so an exit recipe in
the same Result has nothing to play.

| edge | enter |
|---|---|
| `center` | fade scrim + `rise.enter` panel |
| `right` | fade scrim + `slide.enter(x=28)` |
| `left` | fade scrim + `slide.enter(x=-28)` |
| `bottom` | fade scrim + `slide.enter(y=32)` |
| `top` | fade scrim + `slide.enter(y=-32)` |

Returns `None` when ux-motion is absent.

### Two overlay families (do not mix)

| Family | Widgets | Chrome |
|---|---|---|
| **Edge overlays** | Dialog, Sheet, ActionSheet | OverlayChrome ids + dismiss/handle + open_plan |
| **Anchored / command** | Dropdown, ContextMenu, Combobox, Select, Command | **Do not** copy OverlayChrome ids. Floating / anchored / palette. Wrong interaction family. |

ADR 0004 non-goal: forcing Dropdown / ContextMenu / Combobox / Select / Command
through OverlayChrome.

Markup and Tailwind stay on the widget. The primitive owns ids, swipe, enter.

---

## 4. Clock A — two clocks, payload law

| Clock | Trigger | Pipeline |
|---|---|---|
| **A — page GET** | Browser hits a filesystem URL | resolve_unit → `render()` → payload dispatch |
| **B — live action** | `@action` / Channel Intent | mutate → Ops → morph |

**Payload type picks media type.** Not `Accept`. Not a route class. Not FastAPI
`default_response_class`.

| `render()` returns | HTTP | Document wrap |
|---|---|---|
| tag / HTML `str` / bytes | `HTMLResponse` | yes (author Document) |
| `dict` or list-of-dicts | JSON | **no** |
| generator / async generator | `StreamingResponse` | **no** |
| already a Response | as-is | **no** |

`str` is iterable. **It is not a stream.** Page units have **no HTTP verbs**.
Path: `routes/atelier/[sku].py` class `Sku` → `def render(self, sku: str = "")`.
Class name never in the URL. Stem matches class. `≤1` page owner per file.

---

## 5. Ownable kit (`uxcompose add`) — 23 stems + overlay.py

shadcn-style: **the library keeps the source of truth; `uxcompose add` copies
the module into the app; the app owns the file.**

```
uxcompose add --list
uxcompose add login
uxcompose add dialog --page --force
```

Copy lands in `components/{stem}.py`. `--page` also writes `routes/{stem}.py`.
**Product apps do not `from ux_compose.kit import Login` as the shipped unit.**
That import is for tests, the Atelier, Nook, and agents. After `add`, you own
`components/login.py` and you edit `class_*` Tailwind strings.

Also copy `src/ux_compose/kit/overlay.py` → `components/overlay.py`
(not in `add --list`).

Catalog (`ux_compose.kit.catalog.CATALOG`) — 23 entries. Every entry has
`css: False` and `page: True`.

| stem | class | description | host seam |
|---|---|---|---|
| `login` | `Login`, `AuthDecision` | Sign-in / sign-up card. Reveal attaches. Submit is a Cap | `authenticate()` → `AuthDecision(ok, message, blocked)` |
| `tabs` | `Tabs` | Segmented tabs. One MorphState key. Public select | keys / panels |
| `accordion` | `Accordion` | Open ids as a MorphState tuple. Several panels may be open | items |
| `dropdown` | `Dropdown` | Menu is presence. Value is a named key. **Anchored family** | options |
| `dialog` | `Dialog` | Public ask, Cap-protected confirm. **Edge family** | `on_confirm()`. Swipe on Keep it (`click swipe.down`) |
| `sheet` | `Sheet` | Edge panel. Close / Done accept `swipe.right`. No root swipe | open / done. Motion: fade scrim + slide `x=28` |
| `toast` | `Toast` | Server list is authority. Push is public | items |
| `command` | `Command` | Palette. Query attaches. Opening is public. **Anchored family** | `COMMANDS`, `on_run(key)` |
| `table` | `Table` | Sort key MorphState, selection RefState. Archive is a Cap | rows |
| `pagination` | `Pagination` | Opaque page keys. Windowed numbers, not one button per page | `WINDOW` (neighbors each side, default 1). 12 named pages in demo |
| `combobox` | `Combobox` | Type to filter, then pick. Query attaches on morph. **Anchored family** | options |
| `sidebar` | `Sidebar` | Collapsible rail. Active key is MorphState | items |
| `breadcrumb` | `Breadcrumb` | Trail of named crumbs. Walking back is public | crumbs |
| `stepper` | `Stepper` | Named steps. Finish spends `flow.finish` | steps, `on_finish` |
| `carousel` | `Carousel` | Named slides. Overlay prev/next. Sliding pip coalesces | slides. Root stamps `data-channel-id` |
| `calendar` | `Calendar` | Month and day are named keys | `on_pick()` |
| `select` | `Select` | Grouped options. Value is a name. Click-away scrim. **Anchored family** | groups |
| `otp` | `Otp` | Six digits attach. Verify spends `auth.otp` | `on_verify(code)`. Demo: any six except `000000` |
| `plans` | `Plans` | Radio cards. One named plan | `on_choose()` |
| `actionsheet` | `ActionSheet` | Bottom sheet. Handle swipe-down dismisses. Rows stay click. **Edge family** | `ACTIONS`, `on_pick(key)`. Handle: `click swipe.down swipe.vertical threshold:48` |
| `contextmenu` | `ContextMenu` | Click or longpress. Floating panel, not a native list. **Anchored family** | rows. Root stamps `data-channel-id` |
| `typeahead` | `Typeahead` | Live filter on `input delay:300`. Hits morph `#{id}-hits` only | `OPTIONS`, `on_pick(label)` |
| `pullrefresh` | `PullRefresh` | Vertical swipe synthesizer. Refresh accepts `swipe.down` | `SEED`, `on_refresh()` |

### 5.1 Copy press — helper, not a card

`ux_compose.kit.copy` is **not** in `CATALOG`. Do not `uxcompose add copy`.
Do not ship `components/copy.py` as a widget.

| Name | Role |
|---|---|
| `find_app_root(start=None)` | Walk up until `app.py` + `routes/` (or nested `app/`). Else `KitCopyError` |
| `copy_component(name, *, root=, force=False, as_page=False)` | Resolve, rewrite imports, stamp ownable banner, write `components/{stem}.py` |
| `KitCopyError` | Unknown stem, not inside an app, dest exists without `--force` |
| `list_components` / `resolve` | Re-exported from catalog |

Import rewrites applied to the copied file:

- `from ux_compose.kit.X import` → `from .X import`
- `from ux_compose.kit import` → `from . import`

`--page` / `as_page=True` writes `routes/{stem}.py`:

```
from components.{stem} import {Cls} as {Cls}Card
class {Cls}({Cls}Card):
    id = "{stem}"
```

Never `class Login(Login)`. Exists + no `--force` → `KitCopyError` (page file
is left in place if it already exists and `as_page` is the catalog default).

Catalog `css: False` — **no companion CSS is copied**. `uxcompose build` scans
`**/*.py`. `_wire_css_import` exists for a future `css: True` stem; no current
stem uses it. Do not invent per-card CSS.

**Kit grammar (Wave 1 Signal):**

- Tailwind **`class_*` only**. No companion CSS per card. `uxcompose build` scans `**/*.py`.
- Named keys on MorphState. Quantity stays on RefState.
- No viewport `sm:` inside cards. Containment is `min-w-0` + `overflow-x-hidden` + wrap.
- Channel grammar already on the kit: `data-channel-on` values
  `swipe.vertical` · `swipe.horizontal` · `click swipe.down` · `click swipe.left` ·
  `click swipe.right` · `click swipe.up` · `longpress` · `input delay:` ·
  `click swipe.down swipe.vertical threshold:48`.
- **Swipe lives on the handle / Keep it / Close, never on the root.**
- Overlay cards drop `relative` / overflow so a `fixed` overlay is not remapped or clipped.
- Open composes a Motion enter plan (selectors only, no Channel attr, no kit JS).
  Close is morph-only.
- Carousel: Prev/Next overlay the stage (44px), dots overlay a locked `h-72` stage,
  one `#id-thumb` pip translates across equal slots. Copy is the live region.
- Typeahead law: `input delay:300`. Live Results morph `#{id}-hits` only. The field
  (`#{id}-q`) is not in that HTML. `data-channel-target="#{id}-hits"`. Later input
  of the same control aborts the in-flight Intent. Pick morphs the card.
- Pagination: windowed numbers. First/last + gaps are `max-sm:hidden`. Prev is one
  named page back. 44px chevrons.
- Isolation: kit modules never import `ux_channel`.

Nook rooms (the kit house — copy the *rooming*, not the demo copy):

| Path | Kit used |
|---|---|
| `/` Desk | Sidebar, Breadcrumb, Tabs, PullRefresh, Accordion, Command, Toast |
| `/house` House | Typeahead, Combobox, Select, Dropdown, Sheet, Carousel, Table, Pagination, ContextMenu, ActionSheet |
| `/visit` Visit | Stepper, Plans, Calendar, Dialog |
| `/enter` Door | Login, OTP |

APPIC keeps those rooms **and** adds `/overlay` so OverlayChrome is a walkable
room, **and** `/copy` so the press is a walkable room, not a hidden CLI.

---

## 6. Encoding rule (Channel session plane refuses quantity MorphState)

| What | Where |
|---|---|
| Open / value / query / named step / named band | `MorphState` (qualitative) |
| Magnitude, lists, money, ISO dates, files, digits | `RefState` + `stamp = MorphState("idle")` |
| Stamp flip so RefState-only mutations morph | official `tick(comp)` — not a private `_tick` |
| One-shot message | `notify(...)` |
| Domain stock / money / bookings | Host store, never the client plane |
| Protected verb | `@action(caps=("orders.place",))` + host mint at HTTP door |

---

## 7. Examples catalog (75 classes — 99% of product UI)

Every pattern is one `Component`. Same class is valid at L1 and L3.

| Group | File | Cases |
|---|---|---|
| Foundation | `foundation.py` | Counter, Toggle, Planes (Morph vs Ref), Cap reset |
| Chrome | `chrome.py` `modal.py` `shell.py` | Tabs, Accordion, Dropdown, Drawer, ConfirmModal, AppShell, Breadcrumbs, BottomNav, Popover, OverflowMenu |
| Overlays | `overlays.py` | Toasts, Confirm, Lightbox, Palette, Banner |
| Forms | `forms.py` `fields.py` | SignupForm, Wizard, Search, ChoiceGroup, Combobox, DateField, FileDrop, SliderField, OtpGate, PasswordField, Autosave, LimitedNote |
| Collections | `lists.py` `table_board.py` `feeds.py` | Shelf, OptimisticList, Pages, UndoSnack, DataTable, Kanban, Carousel, Comments, Timeline, EmptyRetry, ReorderList, ActivityFeed |
| Navigation | `navigation.py` | ShopView, MasterDetail |
| Commerce | `cart.py` `commerce_more.py` | Cart, Wishlist, Coupon, CheckoutFlow, StockBadge, CompareTray |
| Live Caps | `live_caps.py` | LiveOrder — fail-closed offline, mint vs refuse live |
| Motion | `motion_xor.py` | MotionBox, ShareSeat — XOR, Morph-then-Play, `scene.share` |
| Systems | `systems.py` `ops.py` | Chat, NotifyCenter, Tree, Skeleton, Consent, Theme, Stepper, Rating, Chips, InlineEdit, Calendar, ProgressMeter, CopyClip, Settings, OfflineBanner, Presence, KpiStrip, Shortcuts |
| Host | `document_boot.py` `live_asgi.py` `cart_document.py` `page_unit_mount.py` | Document SSoT, `build()` Clock A GET, Isolation door; `App.mount` secondary |
| Thin wrappers | `form_validation.py` `list_stagger.py` `optimistic_list.py` `page_transition.py` | Point at the real card. Still count as catalog contracts |

Foundation Counter's `_tick` is the **pre-ADR-0004** form. Product code uses
`from ux_compose import tick`.

---

## 7.5 Presence cookbook

`cookbooks/PRESENCE.md`. Product code stays L1; unlocking Motion is additive.

- Stable ids on items (`id="item-{sku}"`). Morph the list region, then
  `scene.stagger_in` on survivors so presence is continuous — items that stay
  do not remount.
- Shared element: `scene.share(key, leave=, arrive=, recipe=)`. Leave and
  arrive selectors must exist after morph. The share **key is identity, not
  a CSS class**.
- Prefer `update_with(self, scene(...).share(...).enter(...))`. XOR: the Plan
  carries no `html=`. Morph first from `render()`.
- Without ux-motion, `scene` is `None`. The same `@action` still morphs via
  `update_with(self, None)`. Zero rewrite.

See also `examples/list_stagger.py`, `examples/page_transition.py`,
`apps/atelier_shop`.

---

## 8. CLI spine

```
uxcompose create-app myapp --name APPIC --level auto --host auto
uxcompose serve dev  [app:asgi] [--host 0.0.0.0] [--port 8080] [--reload-dir PATH ...] [--tunnel none|ngrok|cloudflare]
uxcompose serve prod [app:asgi] [--host 0.0.0.0] [--port 8080]
uxcompose serve restart-channel
uxcompose build [--no-minify] [--skip-tailwind] [--skip-import] [--app app:asgi]
uxcompose deploy --provider docker|fly|render|railway|vps|checklist [--force] [--name NAME]
uxcompose doctor . --no-fail
uxcompose add --list
uxcompose add login [--page] [--force]
```

`uxcompose serve` with no mode exits 2. Soft morph on `*.py` save. CSS save never
kills the ui worker. Channel RAM drop is `restart-channel`, not a flag.
Pure-dom stays on `uxdom` (`doctor` · `lint` · `profile` · `add ui Button`).
HMR / tunnel are delivery under `uxcompose serve dev`, not `Document.use`.
Product CSS is `uxcompose build` (`ux_compose.tailwind` finds / ensures the CLI).
HTML insert is `HmrClientMiddleware`, not `Document.use`.

Serve clocks (ADR 0005 — do not collapse):

| Clock | Owner | Signal |
|---|---|---|
| Process reload | ui worker, uvicorn `--reload` on `*.py` | new ui process, cold import |
| Browser live-reload | `hmr.py` WebSocket `/__uxcompose/hmr` | ui death → GET 200 → morph; `location.reload()` on fail |
| CSS | sibling Tailwind `--watch` + client HEAD `/css/output.css` | stylesheet swap. No process dies |

`serve dev` is origin + ui + channel. Always. `serve prod` is one process,
clocks off. Missing extras fail closed — no single-uvicorn fallback.

---

## 9. Hard laws

1. **Isolation.** Product modules never import the wire. `doctor` AST-scan stays green.
2. **Document SSoT.** Exactly one `Document(...)` in `document.py`. Overlays stay in the tree when closed.
3. **XOR + Morph-then-Play.** Plans carry **no** `html=`. Morph first, then `transition.play`.
4. **Cap Law.** Protected verbs fail closed without a Channel-minted Cap.
5. **Encoding.** Qualitative MorphState. Magnitudes on RefState + stamp. Stamp via official `tick()`.
6. **Presence continuity.** Stable ids. `scene.stagger_in` on survivors. `scene.share(key, leave=, arrive=)` — share id is identity, not a CSS class.
7. **Cold import never pulls the wire.** `App.boot("auto")` is L1.
8. **CSS.** No CSS or client JS inside Python strings. Tokens in `assets/css/input.css`. Kit cards: `class_*` only. CSS first token is CSS — never JS `export`. Catalog `css: False`.
9. **HMR / tunnel** are `uxcompose serve dev` delivery. Soft morph first. `restart-channel` is an action.
10. **Clock A.** No HTTP verbs on page units. Payload type picks media type. Author Document wraps GET.
11. **Ownable kit.** Copy, then edit. Do not ship `from ux_compose.kit import …` as the product unit.
12. **Signal.** Swipe on the handle / Keep it / Close. Never a root swipe that swallows row clicks.
13. **No invented library names.**
14. **One author door.** `act` / `field` / `status` / `tick` / `maybe_*` live on `ux_compose`. Do not keep a second helper world. Do not import `examples._common` from product.
15. **Attach notes refuse silence.** Step-downs write `AttachNote`. They do not raise, and they do not hide.
16. **OverlayChrome is the edge primitive.** Dialog / Sheet / ActionSheet take ids and dismiss grammar from it. Handle: `click swipe.down swipe.vertical threshold:48`. Enter: right `x=28`, bottom `y=32`. Anchored family does not copy these ids.
17. **Leftovers expire by teaching.** Doctor flags kit-imports, `host="batteries"`, `DirectoryRouter`, `serve="webassets"`, teaching `App.mount` as the product path, root swipe. It does not fail-close on them.
18. **The copy press is not a card.** `copy_component` / `find_app_root` / `KitCopyError` are the ownership ritual. OverlayChrome is copied by hand. Do not `uxcompose add copy`.

---

## 10. What this inventory is not

- Not a React / Vue / Svelte / Next / TanStack / HTMX rewrite guide.
- Not permission to invent `Page`, `when`, `forall`, `ux.div`, `StreamingRoute`,
  `host="batteries"`, or HTTP verbs on page units.
- Not permission to treat `App.mount` as the product path, or `examples/_common.py`
  as a second author door.
- Not permission to force Command / Dropdown / ContextMenu through OverlayChrome.
- Not permission to treat `kit/copy.py` as a catalog stem or to ship companion
  CSS per kit card.
- Not permission to ignore doctor teaching residuals, or to fail-close on them.

---

## 11. Delivery names that live off `__all__` (still product law)

These are compose-owned. Product rooms must **walk** them. Product modules
still never import `ux_channel`.

| Module | Names | Room |
|---|---|---|
| `ux_compose.deploy` | `prepare_deploy`, `DeployResult`, `format_deploy_result`. Providers: `docker` `fly` `render` `railway` `vps` `checklist`. Default ASGI `app:asgi`. Does not upload. | `/deploy` |
| `ux_compose.tunnel` | `parse_provider`, `TunnelHandle`, `local_probe_host`, `wait_for_health`, `start_tunnel`, `provider_available`. Providers: `none` `ngrok` `cloudflare` (aliases `cf` / `cloudflared` / `trycloudflare`). Start **after** origin health. | `/deploy` |
| `ux_compose.hmr` | `HMR_PATH` (`/__uxcompose/hmr`), `attach_hmr`, `client_script_tag`, `HmrClientMiddleware`. Soft morph on `*.py` save. CSS save never kills ui. | `/relay` |
| `ux_compose.serve_restart` | `restart_channel`, pidfile + SIGUSR1. `uxcompose serve restart-channel`. | `/relay` |
| `ux_compose.cli_build` | `find_product_root`, `run_product_build`, `ProductBuildReport`, `format_product_build_report`. | `/skin` |
| `ux_compose.tailwind` | `resolve_tailwind`, `ensure_tailwind`, `TailwindResolution`, `argv_with_io`, `discover_css_io`. Product CSS is `uxcompose build`. | `/skin` |
| `ux_compose.assets` | `WebAssets`, `CSS_URL_PREFIX` (`/css`), `OUTPUT_CSS_NAME` (`output.css`). ETag + Last-Modified. | `/skin` |
| `ux_compose.attach_notes` | `AttachNotes`, `note`, `using`, `format_report`, `current`, `clear` (tests only). | `/notes` |
| `ux_compose.dx.probe` | `probe`, `ProbeResult` (`ux_dom`, `ux_behavior`, `ux_motion`, `ux_channel`, `directory_routes`). | `/trace` |
| `ux_compose.surfaces` | `ActionInfo`, `Surface`, `SurfaceBundle`, `SurfaceError`. | `/lattice` |
| `ux_compose.build` | `BuildResult` = `(app, asgi, bundle)`. `use_htmx=False`. | `/clocks` |
| `ux_compose.progressive` | `Level` IntEnum. Labels: `static + routing` / `offline interactive` / `live channel` / `motion`. | `/clocks` |

Serve clocks (ADR 0005 — do not collapse):

| Clock | Owner | Signal |
|---|---|---|
| Process reload | ui worker, uvicorn `--reload` on `*.py` | new ui process, cold import |
| Browser live-reload | `hmr.py` WebSocket `/__uxcompose/hmr` | ui death → GET 200 → morph; `location.reload()` on fail |
| CSS | sibling Tailwind `--watch` + client HEAD `/css/output.css` | stylesheet swap. No process dies |

`serve dev` is origin + ui + channel. Always. `serve prod` is one process,
clocks off. Missing extras fail closed — no single-uvicorn fallback.
Tunnel starts after origin health is green.
