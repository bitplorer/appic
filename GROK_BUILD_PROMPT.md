# Grok Build prompt — APPIC on ux-compose 0.1.0

Pin: [bitplorer/ux-compose](https://github.com/bitplorer/ux-compose) `@ main`
SHA **`7ea3eb8813d280a975c4a41d23a2e2d4de40a506`**.
Companion: [FEATURE_INVENTORY.md](FEATURE_INVENTORY.md).
If this prompt and the library disagree, **the library wins**.

This file is the **metaprompt**. Publish it on **bitplorer/appic**. The executing
Grok Build agent copies **everything below the line**, clones the library first,
and ships a complete foundry. Repo **appic already exists** — upgrade it; do not
create a second repo.

Deep-dived **2026-09-06** from a full AST of `src/ux_compose/` plus the four
specialists' public seams:

- `ux_compose.__all__` (composition, author door, tags, motion, attach notes)
- `kit/catalog.py` — 23 stems, `css: False`, `page: True`, `KitEntry`
- `kit/copy.py` — `copy_component`, `find_app_root`, `KitCopyError` (not a card)
- `kit/overlay.py` — `OverlayChrome`, `overlay`, `KIND_EDGE`, `EDGE_SWIPE`,
  `HANDLE_SWIPE`, `EDGE_SLIDE` (not a catalog stem)
- `kit/login.py` — `AuthDecision` NamedTuple; secrets never on MorphState
- `kit/typeahead.py` — hits-slot law (`#{id}-hits` only)
- `kit/pagination.py` — `page_slots`
- `author.py` — `act` / `tick` / `field` / `status` / `maybe_*`
- `attach_notes.py` — `AttachNote`, `AttachNotes`, `note`, `using`,
  `format_report`, `current`, `clear` (test-only)
- `helpers.py` — `bind`, `control`, `notify`, `update_with` (strategy
  `idiomorph`, XOR), `morph_play`
- `app.py` — boot, use_*, mint/submit, add, mount, dispatch, doctor
- `build.py` — `BuildResult`, orchestra, `use_htmx=False`
- `doctor.py` — hard + teaching scans
- `dx/probe.py` — `ProbeResult`, `probe` (never shells)
- `assets.py` — `WebAssets`, `CSS_URL_PREFIX=/css`, `OUTPUT_CSS_NAME=output.css`
- `deploy.py` — `prepare_deploy`, `DeployResult`, six `Provider`s
- `tunnel.py` — `parse_provider`, `TunnelHandle`, `wait_for_health`
- `hmr.py` — `HMR_PATH=/__uxcompose/hmr`, `attach_hmr`, `HmrClientMiddleware`
- `serve_dev.py` — origin + ui + channel workers
- `serve_restart.py` — `restart_channel`
- `tailwind.py` — `TailwindResolution`, `resolve_tailwind`, `ensure_tailwind`
- `routing/` — `DirectoryRoutes`, `DirectoryASGI`, `RouterHooks`
  (`resolve_unit`, `accept_symbol`, `on_route`), `http_path`,
  `is_json_payload`, `is_stream_payload`, `apply_html_document`,
  `ProductBatteriesRejected`, `materialize` fail-closed
- `surfaces.py` — `Surface`, `SurfaceBundle`, `SurfaceError`, `ActionInfo`
- `progressive.py` — `Level` IntEnum L0–L3 + `.label`
- `cli.py` — `uxcompose` only; serve without a mode exits 2
- `cookbooks/PRESENCE.md`, `docs/FLOW.md`, ADR 0004 / 0005
- `examples/` — **75 Component classes** (Atelier, not a second catalog)
- teaching apps `nook` / `atelier_studio` / `atelier_shop` / `pulse`

---

Copy **everything below this line** into Grok Build. You **are** Grok Build.
Execute it. Do not stop at a README. Ship a running foundry on `0.0.0.0:8080`.

---

# APPIC — a constitution you can walk

Build **APPIC** as a **complete product** (not a widget zoo) using
**https://github.com/bitplorer/ux-compose @ main**
(`7ea3eb8813d280a975c4a41d23a2e2d4de40a506`, **0.1.0**) as the **only** web UI
framework.

Fully utilise **every public name** in `ux_compose.__all__`, every Clock A
payload door, every ownable kit card (`uxcompose add`), OverlayChrome
(copied even though it is not a catalog stem), the copy helper, every Wave 1
Signal, every doctor scan family, the Presence cookbook, WebAssets,
prepare_deploy (six providers), tunnel grammar, HMR delivery, attach-note
notebooks, Tailwind resolver, probe matrix, morph_play hop, AuthDecision
verdict, Typeahead hits-slot, and every one of the **75** Atelier Component
classes in `examples/`.

> **The document is the composition root made visible. Caps are wax seals
> that break when spent. Intent is a nucleus you can hold. Ops are traces
> on a ribbon. Routes are a constellation. Skin is WebAssets. GET is Clock A.
> Action is Clock B. Payload type picks media type — HTML is daylight, JSON
> is a pulse, a generator is a stream of light. Kit cards are rooms you own.
> The copy press is the ownership ritual. Signal is a grammar in the hand.
> The author door is one. Attach notes refuse silence. OverlayChrome is the
> edge primitive. Anchored popovers are a different family. Doctor residuals
> expire by teaching. Presence is continuous — objects that stay do not
> remount. HMR is delivery, not a Document API. Tunnel starts after health
> is green. Probe never shells. Login secrets never sit on MorphState.
> Typeahead morphs the hits slot, never the field being typed.**

**No React. No Vue. No JS/TS/TSX as source of truth.** Server-authored
hypermedia. Python + ux-compose. Serve uvicorn on `0.0.0.0:8080`.

Repo: **bitplorer/appic**. Create only if missing. Consume the running foundry.

Grok sandbox: Auth OFF. Database OFF. Do **not** scaffold TanStack Start /
React / Vite / Nitro. Kit `Login` / `Otp` are foundry Caps against the Host
store. Direct user law beats the sandbox's React default.

A visitor should feel: *this house has laws, and I can touch them.*

---

## NORTH STAR

APPIC is a private nocturnal foundry for commissioning and collecting handmade
objects, authored so that **authority, motion, media type, ownership of UI,
the copy ritual, gesture grammar, the author door, attach step-downs, overlay
family vs anchored family, doctor residuals, presence continuity, skin, ship,
HMR clocks, tunnel, probe, and the hits-slot law** are first-class rooms a
human can walk.

Editorial. Expensive. Abundant negative space. Concentric radii. One cool
accent (`#c8ccd4` on ink `#0c0d0b`). Bone type `#ebe6d8`. Fraunces + Source
Sans 3 + IBM Plex Mono. No purple, gold, neon, gradient-blob slop. No emoji
in chrome. Film grain at 3.5% overlay. Pill buttons 44px. Hairline borders.
Soft single shadow. `prefers-reduced-motion`.

The Table is a **constellation**: named stars around a nucleus. Sight is
MorphState (looking is not walking). Walk is Clock A GET. Pulse is Clock B.

---

## KILL TRIGGERS

If you do any of these, **stop, undo, and continue on the product path**.

1. **Any product UI in React / Vue / Svelte / Solid / Next / TanStack Start /
   JSX / TSX / `.tsx` / `.jsx` / client TypeScript as the source of truth.**
2. **`vite` / `npx vite` / `npm run build` / Nitro as the ship gate.** Preview
   is uvicorn on `0.0.0.0:8080`. First token of any CSS file must be CSS.
3. **HTMX as architecture.** `use_htmx=False`.
4. **HTTP verbs on page units.** No `get` / `post` on a Component. Clock A
   wraps `render()`.
5. **`from ux_compose.kit import Login` (or any kit card) as the live unit.**
   Copy via `uxcompose add`, own `components/`.
6. **`import ux_channel` / `cek` / `cek_host` / `cek_surface` / `MotionChannel`
   in product modules.** Isolation Law.
7. **`host="batteries"`** or `DirectoryRouter`. Use `host="auto"`.
   `ProductBatteriesRejected` is the fail-closed. `serve="webassets"` leftover
   — prefer `serve="dual_copy"`.
8. **Plans with `html=`.** XOR. Morph first from `render()`, then
   `transition.play`. `update_with` may put `html=` on the **morph** payload.
9. **Root `swipe.*` on Dialog / Sheet / ActionSheet.** Swipe lives on dismiss /
   handle. Handle grammar: `click swipe.down swipe.vertical threshold:48`.
10. **A second helper world.** Official:
    `from ux_compose import act, tick, field, status, maybe_plan, maybe_fade, maybe_slide`.
    `act()` posts `/act/{action}`. No private `_tick`. No
    `from examples._common import`.
11. **Silent `except ImportError` without `AttachNote`.**
12. **Forcing Command / Dropdown / ContextMenu / Combobox / Select through
    OverlayChrome.** Wrong family. House is anchored; `/overlay` is edge.
13. **Invented library names** (`Page`, `when`, `forall`, `ux.div`,
    `StreamingRoute`).
14. **Grok platform Auth ON / Database ON.**
15. **Incomplete kit.** 23 catalog stems + `components/overlay.py` must be live.
16. **Treating `kit/copy.py` as a catalog stem.** It is the press, not a card.
17. **Companion CSS per kit card.** Catalog `css: False`. Markup is Tailwind
    `class_*` / `className`.
18. **Ignoring doctor teaching residuals.** Isolation + dual-Document are hard.
    Kit-import and leftover aliases expire by teaching — render them as chips.
19. **Teaching `App.mount` as the product path.** `build()` is the product door.
    Mount is the scan step inside it. `materialize(route_class=)` fails closed.
20. **Starting a tunnel before origin health is green.**
21. **Morphing the Typeahead field from a pause-fired Result.** Hits morph
    `#typeahead-hits` only.
22. **Putting email / password / OTP digits on MorphState.** RefState +
    `tick(self)`. Channel session plane refuses quantity MorphState.
23. **`probe()` starting a server or shelling out.** It is import-spec only.
24. **Hiding the Created-with-Grok pill, stripping `extensions.js`, or dropping
    the vanilla preview-host bridge.**

---

## 1. What ux-compose actually is

Thin pure-Python **composition + delivery** root. It harnesses four specialists
and must **not** reimplement them.

| Specialist | Role | Unlock | Install |
|---|---|---|---|
| **ux-dom** | Tag trees, Document SSoT, serialize, className, `<link>`, package static, CSP | L0 | `git+https://github.com/bitplorer/ux-dom.git` (Python ≥3.14 full; 3.10–3.13 `HAS_DOM` shim) |
| **ux-behavior** | `Component`, `MorphState`, `RefState`, `@action`, Ops | L1 | `git+https://github.com/bitplorer/ux-behavior.git` |
| **ux-channel** | Intent → Cap → Result. Behind compose `wire/` only | L2 | `git+https://github.com/bitplorer/ux-channel.git#subdirectory=python` |
| **ux-motion** | Scene Plans, presence, Morph-then-Play | L3 | `git+https://github.com/bitplorer/ux-motion.git` |

**Progressive Superpower:** the **same Component class** is correct at L1
(`dispatch`) and L3 (`use_channel` + `use_motion`). Zero rewrite. If you
rewrite a Component “to go live”, you have violated the contract.

`Level` is an `IntEnum`: `L0=0` `static + routing` · `L1=1` `offline interactive`
· `L2=2` `live channel` · `L3=3` `motion`. `app.level.label` is the string.

PyPI / import / CLI: `ux-compose` / `ux_compose` / **`uxcompose`**.
`ux_compose.__version__ == "0.1.0"`.

Product path:

```
uxcompose create-app myapp --level 1
uxcompose serve dev          # origin + ui + channel + CSS watch, 0.0.0.0:8080
uxcompose build              # Tailwind minify → /css/output.css
uxcompose serve prod         # clocks hard off
uxcompose serve restart-channel
uxcompose deploy --provider docker|fly|render|railway|vps|checklist
uxcompose doctor .
uxcompose add login          # ownable kit copy
uxcompose add --list
```

`uxcompose serve` without a mode exits 2. Deploy runs raw uvicorn, not `serve`.
Tunnel (`--tunnel ngrok|cloudflare`) starts **after** origin health is green.
Aliases: `cf` / `cloudflared` / `trycloudflare`. `[serve]` extra: uvicorn,
watchfiles, httpx, starlette, websockets.

Pure-dom tooling stays on **`uxdom`** (`doctor` · `lint` · `profile` · `add`).

Vendor so git extras can fail (sandbox Python 3.10–3.11):

```
vendor/ux-compose-src/ux_compose/
vendor/specialists-src/{ux_behavior,ux_motion,ux_dom,ux_channel}/
PYTHONPATH=.pydeps:vendor/ux-compose-src:vendor/specialists-src:.
```

Then own the kit:

```
for s in login tabs accordion dropdown dialog sheet toast command table pagination \
         combobox sidebar breadcrumb stepper carousel calendar select otp plans \
         actionsheet contextmenu typeahead pullrefresh; do
  uxcompose add "$s" --force
done
cp vendor/ux-compose-src/ux_compose/kit/overlay.py components/overlay.py
```

Do **not** copy `kit/copy.py` or `kit/catalog.py` as widgets.
`copy_component(name, *, root=None, force=False, as_page=False)` writes
`components/{stem}.py` and optionally `routes/{stem}.py`. `find_app_root`
walks until `app.py` + `routes/`. Markup is Tailwind on the class — no
companion CSS is copied (`uxcompose build` scans `**/*.py`).

Teaching apps (play before inventing widgets):

| App | Role |
|---|---|
| `apps/nook` | Kit house. Every ownable component sits in a real room |
| `apps/atelier_studio` | Atelier of Patterns — every `examples/` card |
| `apps/atelier_shop` | Product shop / cart / presence |
| `apps/pulse` | Multi-route live product |

---

## 2. Public author surface (`ux_compose.__all__`)

Every name **must appear in product source**.

```
App, build, WebAssets,
DirectoryRoutes, DirectoryASGI, RouterHooks,
Surface, SurfaceBundle, SurfaceError,
mount_surfaces, scan_surfaces, validate_surfaces,
Component, MorphState, RefState, action,
bind, control, notify, update_with, morph_play,
act, tick, field, status,
maybe_plan, maybe_fade, maybe_slide,
AttachNote, attach_notes,
Level, doctor, DoctorResult,
scene, fade, rise, slide,     # None until ux-motion
HAS_DOM, raw, __version__,
html, head, body, title, style, meta, link, script,
div, span, h1, h2, h3, p, a, button, form, input_,
ul, li, header, footer, aside, section, article, nav, main, label,
svg, path, rect, circle
```

Also use (compose submodules, never `ux_channel`):

```
ActionInfo, BuildResult, RouteRecord,
DirectoryRoutesError, HMR_PATH, attach_hmr, client_script_tag, HmrClientMiddleware,
IsolationViolation, CSS_URL_PREFIX, OUTPUT_CSS_NAME,
http_path, is_json_payload, is_stream_payload, apply_html_document,
scan_isolation, scan_kit_product_imports, scan_leftover_aliases, scan_dual_document,
prepare_deploy, DeployResult, format_deploy_result,
parse_provider, TunnelHandle, local_probe_host, wait_for_health, start_tunnel, provider_available,
find_product_root, run_product_build, ProductBuildReport, format_product_build_report,
restart_channel,
probe, ProbeResult,
note, using, format_report, current,   # attach_notes submodule
resolve_tailwind, ensure_tailwind, TailwindResolution,
ProductBatteriesRejected
```

`scan_dual_document` exists on `ux_compose.doctor` and is invoked by `doctor()`.

From owned `components/overlay.py`: `OverlayChrome`, `overlay`.

From owned `components/login.py`: `Login`, `AuthDecision`.

From `ux_compose.kit.catalog` / `kit.copy` — evidence, **not** shipped cards:

```
KitEntry, CATALOG, list_components, resolve
copy_component, find_app_root, KitCopyError
```

From `ux_compose.kit.pagination` (owned copy): `page_slots`.

### App

```
App.boot(name, *, strict_caps=False, level="auto"|0..3)
   # "auto" is Level 1. Channel attaches in build() once ASGI exists.
app.use_host("auto"|"fastapi"|"starlette"|"asgi")   # never "batteries"
app.use_dom(document=None, *, author=True)
app.use_behavior()
app.use_channel(asgi_app=...)     # Isolation door — wire/ only
app.use_motion()
app.use_cek(mode="adapt")         # never mode=require in product
app.mint_cap(action, args)
app.submit_intent / submit_intent_async(..., mint=True)
app.add(*ComponentClasses)
app.mount(package_dir, asgi_app=..., base="routes", fail_closed=..., bind_pages=...)
app.dispatch("surface.verb", **args)
app.dispatch("surface.verb", args={"sku": "tee"})
app.control(...)
app.doctor(paths, fail=False)
app.level / app.level.label / app.behavior
app.attach_notes
```

`materialize(route_class=)` **fails closed**. `host="batteries"` **fails closed**
(`ProductBatteriesRejected`). `App.mount` is the scan step inside `build()` —
teaching it as the product path is a leftover chip.

`build(package_dir, *, name="App", host="auto", live="auto", level="auto",
base="routes", fail_closed=True, use_htmx=False, asgi_app=None, document=None)`
returns `BuildResult` = `(app, asgi, bundle)` with `.app` `.asgi` `.bundle`.

Orchestra: `host.open` → L1 boot → document → Channel on asgi → discover →
`host.bind`. Payload type picks media type, not Accept.

### Author helpers (ADR 0004)

```
act(action, label, *, kind="secondary", target="#stage", on=None, **args)
    POST form to /act/{action}. Alias that path onto /action/{name}.
    Hidden inputs for **args. data-ux=1, data-target={target}.
    on= stamps data-channel-on. control() attrs on the submit button.

tick(comp, *, on="tick", off="tock")
    Flip comp.stamp. Never a private _tick.

field(name, value="", *, placeholder="", kind="text")
    className="field". autocomplete="off".

status(text, *, kind="note")
    empty → span("", className="sr"); else status status-{kind} role="status".

maybe_plan(name, target, *, ms=140)   → scene.enter(target, rise.enter) or None
maybe_fade(name, target, *, ms=120)   → scene.enter(target, fade.enter) or None
maybe_slide(name, target, *, direction="next"|"prev", ms=180)
    dist from ux_motion.tokens.dist("md"), else 24.0
    prev → −dist, next → +dist
```

### OverlayChrome (exact tables)

```
overlay(root_id, *, kind=None, edge=None) -> OverlayChrome
ids: {root}-scrim / {root}-panel / {root}-dismiss

KIND_EDGE: modal/dialog → center; sheet/drawer → right; action/actionsheet → bottom
EDGE_SWIPE: center click swipe.down; right click swipe.right; left click swipe.left;
            bottom click swipe.down; top click swipe.up
HANDLE_SWIPE: bottom click swipe.down swipe.vertical threshold:48
              top   click swipe.up   swipe.vertical threshold:48
EDGE_SLIDE: right x=28; left x=-28; bottom y=32; top y=-32
open_plan: center fade+rise; else fade scrim + slide panel
Returns None when ux-motion is absent. No html= on the plan.
Close stays morph-only (panel is gone — an exit recipe has nothing to play).
```

Edge family: Dialog, Sheet, ActionSheet.
Anchored family (do **not** copy these ids): Dropdown, ContextMenu, Combobox,
Select, Command.

### Attach notes

```
@dataclass(frozen=True)
class AttachNote:
    door: str          # e.g. "use_channel"
    wanted: str        # e.g. "ux-channel"
    reason: str
    level_kept: int    # default 1
```

`app.attach_notes` is this App. `attach_notes()` is process-wide. Missing
specialists write a note instead of raising. Submodule: `note()`, `using()`,
`format_report()`, `current()`. `clear()` is a test helper — do not call from
product. Two Apps in one process do not leak. Not a message bus. Not HMR.

### Doctor + probe

Hard: Isolation (`ux_channel` / `cek*` / `MotionChannel` in product), dual-Document.
Teaching: kit-import, leftover aliases (`host="batteries"`, `DirectoryRouter`,
`serve="webassets"`). Teaching does not fail-close. Render both families on `/trace`.

`DoctorResult`: `ok`, `level_available`, `diagnostics`, `capabilities`,
`teaching`, `surfaces`, `routes`, `raise_if_failed()`.

`probe()` → `ProbeResult(specialists, clis, labels, level_available)`.
Specialists: `ux_dom`, `ux_behavior`, `ux_motion`, `ux_channel`. Never starts
a server. Never shells. Render the matrix on `/trace` and `/relay`.

### State law

| Kind | Field |
|---|---|
| Open / value / query / named step / named band | `MorphState` (qualitative) |
| Magnitude, lists, money, ISO dates, files, digits, secrets | `RefState` + `stamp = MorphState("idle")` then `tick(self)` |
| One-shot message | `notify(...)` |
| Protected verb | `@action(caps=("…",))` + live Cap |
| Channel session plane | **refuses quantity MorphState** |
| Login / OTP secrets | **never MorphState** |

Prefer `bind(self.add, sku="tee")` over stringly `control("add", sku="tee")`.

`update_with(component, plan=None, *fields, html=None, strategy="idiomorph", extra_ops=None)`
returns morph Op first, then plan ops (`transition.play`), then extra_ops.
`morph_play` is the hop helper — use **once** in the Lab, not as a second world.

### Clock A payload doors

`render()` return type picks media type. No HTTP verbs on the class.

| Return | Door | Room |
|---|---|---|
| ux-dom tag tree / HTML string | HTML | every page |
| `dict` | JSON | `/health` |
| generator | stream | `/pulse` |

`is_json_payload` / `is_stream_payload` / `apply_html_document` are the host
seams. Trees stay buffered (CSP + `Content-Length`). `str` is HTML, never JSON,
never a stream. `http_path` is the one path law.

### Presence cookbook

Stable ids (`id="item-{sku}"`). Morph the list, then `stagger_in` on survivors.
`scene.share(key, leave=..., arrive=...)` — key is identity, not a CSS class.
Without motion, `scene is None` and the same `@action` still morphs.

### Wave 1 signal grammar

These tokens are Channel grammar. They live as `data-channel-on` / control
attrs. Walk them on `/signal`.

| Token | Meaning | Where |
|---|---|---|
| `click` | tap / mouse | every control; always keep click on dismiss |
| `swipe.down` / `swipe.up` / `swipe.left` / `swipe.right` | edge dismiss | OverlayChrome dismiss, never the overlay root |
| `swipe.vertical` | let row clicks survive | ActionSheet handle |
| `threshold:48` | px before swipe commits | handle only |
| `input delay:300` | pause-fired live filter | Typeahead field |
| `longpress` | floating panel | ContextMenu |

Typeahead hits-slot: live Results morph `#{id}-hits` only — the field is not
in that HTML, so a pause-fired Result cannot rewrite what is still being typed.
Query is RefState so pick / empty-q still know the string.

### WebAssets + deploy + tunnel + HMR + Tailwind

- `WebAssets(base_dir=...)`. `css_href` → `/css/output.css`. Disk:
  `assets/css/input.css` → `assets/static/file/css/output.css`. ETag /
  Last-Modified (`W/"{mtime_ns}-{size}"`). First token of any CSS file must
  be CSS (never `export`).
- `prepare_deploy(provider=)` writes Dockerfile / fly.toml / render.yaml /
  railway.json / systemd / checklist. Does not upload. Default ASGI `app:asgi`.
  Returns `DeployResult(root, provider, files_written, instructions, notes)`.
- Tunnel `parse_provider("none"|"ngrok"|"cloudflare")`. Start after health.
  `TunnelHandle.public_url`. `wait_for_health`, `local_probe_host`,
  `provider_available`.
- HMR is `uxcompose serve dev` delivery. Path `/__uxcompose/hmr`.
  `attach_hmr` / `client_script_tag` / `HmrClientMiddleware`. Soft morph on
  `*.py` save. CSS save never kills the ui worker. Channel RAM drop is
  `uxcompose serve restart-channel` (`restart_channel()`).
- `serve dev` is **three processes**: origin + ui + channel. `serve prod` is
  one process, clocks off. No `--hmr` / `--no-reload` / `--css-watch` flags.
- `resolve_tailwind` / `ensure_tailwind` → `TailwindResolution`. Finder order:
  env, PATH, pytailwindcss, node_modules, cached binary, download, npx.

### Kit catalog (23 stems)

login, tabs, accordion, dropdown, dialog, sheet, toast, command, table,
pagination, combobox, sidebar, breadcrumb, stepper, carousel, calendar, select,
otp, plans, actionsheet, contextmenu, typeahead, pullrefresh.

Style by editing `class_*` Tailwind strings on the owned copy. Host seams are
`on_*` / `authenticate` / `OPTIONS` overrides — not forks of the library.

`Login.authenticate` returns `AuthDecision(ok, message="", blocked=False)`.
Show/Hide and tab switches attach live form values onto RefState *before*
the morph. Submit spends `auth.login` / `auth.signup`. OTP verify spends
`auth.otp`.

`uxcompose add NAME --page` also writes `routes/{stem}.py`.

### Atelier roster (75 classes — all must be walkable)

Foundation: Counter, Toggle, Planes.
Chrome: Tabs, Accordion, Dropdown, Drawer, ConfirmModal.
Shell: AppShell, Breadcrumbs, BottomNav, Popover, OverflowMenu.
Overlays: Toasts, Confirm, Lightbox, Palette, Banner.
Forms: SignupForm, Wizard, Search.
Fields: ChoiceGroup, Combobox, DateField, FileDrop, SliderField, OtpGate,
PasswordField, Autosave, LimitedNote.
Lists: Shelf, OptimisticList, Pages, UndoSnack.
Feeds: Carousel, Comments, Timeline, EmptyRetry, ReorderList, ActivityFeed.
Table/board: DataTable, Kanban.
Nav: ShopView, MasterDetail.
Commerce: Cart, Wishlist, Coupon, CheckoutFlow, StockBadge, CompareTray, Rating.
Live Caps: LiveOrder.
Motion: MotionBox, ShareSeat.
Systems: Chat, NotifyCenter, Tree, Skeleton, Consent, Theme, Stepper, Chips,
InlineEdit.
Ops: Calendar, ProgressMeter, CopyClip, Settings, OfflineBanner, Presence,
KpiStrip, Shortcuts.
Host demos: Badge, Index, Hello.

Play them in `/lab` and `/atelier`. Do not invent a second catalog.

---

## 3. Product rooms (walkable)

| Path | Room |
|------|------|
| `/` | Table — pulse, hold an intent, sight a constellation star, sit a bench |
| `/enter` | Door — owned Login + OTP + `AuthDecision`. Caps `auth.login` / `auth.otp` |
| `/desk` | Desk — Sidebar, Breadcrumb, Tabs, PullRefresh, Accordion, Command, Toast |
| `/house` | House — Typeahead (hits-slot), Combobox, Select, Dropdown, Sheet, Carousel, Table, Pagination (`page_slots`), ContextMenu, ActionSheet. Anchored family |
| `/visit` | Visit — Stepper, Plans, Calendar, Dialog |
| `/signal` | Signal — Wave 1 grammar (swipe, longpress, `input delay:`, handle `threshold:48`) |
| `/author` | Author — official `act` / `field` / `status` / `tick` / `maybe_*`. Posts `/act/{action}` |
| `/notes` | Notes — `AttachNote`, `attach_notes()`, `App.attach_notes` |
| `/overlay` | Chrome — OverlayChrome ids, swipe-on-dismiss, handle `threshold:48`, enter x=28 / y=32 |
| `/copy` | Press — 23 stems + OverlayChrome-not-a-stem. `copy_component` / `find_app_root` / `KitCopyError` |
| `/skin` | Skin — WebAssets, ETag, first-token CSS, `dual_copy` leftover chip |
| `/deploy` | Ship — six providers. `prepare_deploy` is a Cap. Tunnel chips |
| `/atelier` | Filter, sort, save, compare, look, add to bag. Presence cookbook on sort |
| `/atelier/{sku}` | DirectoryRoutes dynamic segment. No `get()`. |
| `/commission` | Four-step wizard. OTP `2048` and place are Caps |
| `/bag` | Stepper, coupon Caps `HOUSE` / `FLAX` / `TABLE`, checkout Cap |
| `/board` | Move cards, undo, bulk table |
| `/studio` | Chat, typing presence, moderate Cap |
| `/lab` | Remaining 75-class Atelier floor + `morph_play` hop (once) |
| `/lattice` | Caps as seals, intent as nucleus |
| `/trace` | Live ops, doctor (hard + teaching), isolation, CSP, leftover teaching, `probe()` matrix |
| `/ledger` | Book a bench (Cap), WebAssets chip, wipe (Cap) |
| `/clocks` | Dual-clock room — GET vs action, three payload doors |
| `/relay` | Three serve clocks. Soft morph. restart-channel as a named drop |
| `/health` | JSON page unit (`render()` returns a dict) |
| `/pulse` | Stream page unit (`render()` returns a generator) |

Command `⌘K` issues intents without leaving the table.

---

## 4. Visual law

Tokens (encode once in `:root`, never scatter hex):

```
--bg: #0c0d0b; --bg-elevated: #141512; --surface: #1a1b18;
--fg: #ebe6d8; --fg-muted: #9a9488; --fg-subtle: #6f6a60;
--accent: #c8ccd4; --accent-fg: #0c0d0b;
--danger: #c17a6e; --ok: #8fa394;
```

Concentric radii (`4 / 8 / 12 / 20 / 28`). Pill buttons 44px. One accent.
Hairline borders. Soft single shadow. Film grain overlay at 0.035.
`prefers-reduced-motion`. Mobile ~390: hide desktop nav, 6-item bottom nav,
no horizontal overflow. Tap targets ≥ 44px.

Keep Grok `extensions.js` in the shell. Vanilla preview-host bridge
(`grok-preview-bridge` v1: hello / navigate / history / location / routes / ready).
Do not hide the Created-with-Grok pill.

---

## 5. Sandbox + serve

```
export PYTHONPATH=".pydeps:vendor/ux-compose-src:vendor/specialists-src:."
python3 -m pip install --target .pydeps fastapi 'uvicorn[standard]' marko itsdangerous python-multipart
python3 -m uvicorn appic.server:app --host 0.0.0.0 --port 8080
```

`startup.sh` is the revive contract: probe `/api/health` (or `/health`), start
only if down, background, bind `0.0.0.0:8080`. Default ASGI `app:asgi` or
`appic.server:app`. Use `python3.11` when present.

On Python 3.10–3.13, `HAS_DOM` may be False — ship a Tag shim (`appic/tags.py`)
with the same call shape. Do not pip-install ux-dom together with marko on 3.10.

Do **not** run `npm run build` / Vite as the product gate. User law: no React.
Verify with a real browser against `http://127.0.0.1:8080`: visible Table,
clean console, mobile 390, Command `⌘K`, Door login, Atelier sort, Bag
checkout Cap, Trace doctor chips.

Publish to GitHub **bitplorer/appic**. Keep this prompt and FEATURE_INVENTORY.md
in the same repo.

If the prompt and the library disagree, **the library wins**.
