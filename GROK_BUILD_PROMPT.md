# Grok Build prompt — APPIC on ux-compose 0.1.0
## Architecture era: one author door, attach notes, OverlayChrome

Pin: [bitplorer/ux-compose](https://github.com/bitplorer/ux-compose) `@ main`
SHA **`7ea3eb8813d280a975c4a41d23a2e2d4de40a506`**.
Companion law: [FEATURE_INVENTORY.md](FEATURE_INVENTORY.md) in the same repo.
Shape: ux-compose `docs/ARCHITECTURE.md` + ADR 0004 + ADR 0005.

This file is the **metaprompt**. Publish it on **bitplorer/appic**. The
executing Grok Build agent copies **everything below the line**, reads the
library first, and ships a complete foundry. If this prompt and the library
disagree, **the library wins**. Do not invent APIs.

The previous APPIC prompt (`f4aeab2`, library SHA `6b84972`) shipped Clock A,
the ownable kit, Wave 1 Signal, Typeahead hits-slot, and Relay. This prompt
**adds ADR 0004 as walkable rooms**: one author door (`act` / `field` /
`status` / `tick` / `maybe_*`), visible attach notes (`AttachNote`,
`attach_notes()`, `App.attach_notes`), and OverlayChrome (ids, swipe-on-dismiss,
handle `threshold:48`, enter distances right `x=28` / bottom `y=32`). A foundry
that hides its author door, its step-downs, or its overlay primitive is unfinished.

Repo **appic already exists**. Do not create a second repo. Consume the
running foundry; upgrade it; replace stale files that predate ADR 0004.

---

Copy **everything below this line** into Grok Build.

---

Build **APPIC** — a stunning nocturnal foundry OS — as a **complete product**
(not a widget zoo) using **https://github.com/bitplorer/ux-compose @ main**
(`7ea3eb8813d280a975c4a41d23a2e2d4de40a506`, 0.1.0) as the **only** web UI
framework. Fully utilise **every public name** in `ux_compose.__all__`, every
Clock A payload door, every ownable kit card (`uxcompose add`), OverlayChrome
(copied even though it is not a catalog stem), every Wave 1 Signal, and every
catalog pattern in `examples/`. Ship a running foundry whose radical face is this:

> **The document is the composition root made visible. Caps are seals. Intent
> is a nucleus. Ops are traces. Routes are a constellation. Skin is WebAssets.
> GET is Clock A. Action is Clock B. Payload type picks media type. Kit cards
> are rooms you own. Signal is a grammar you can feel. The author door is one.
> Attach notes refuse silence. OverlayChrome is the edge primitive. Anchored
> popovers are a different family.**

Read the library first. Clone or vendor `src/ux_compose` from that SHA **and**
the four specialists (`ux-dom`, `ux-behavior`, `ux-channel`, `ux-motion`).
Play the teaching apps (`apps/nook`, `apps/atelier_studio`, `apps/atelier_shop`,
`apps/pulse`) and `examples/` before inventing a widget.

Nook is the kit house. APPIC is the foundry that **lives in that house**.

Repo: publish to GitHub **appic** under the connected account
(**bitplorer/appic**). Create the repo only if missing. Do not create a second
repo if `appic` already exists.

Keep `FEATURE_INVENTORY.md` in the same repo. Update it if you vendor a newer SHA.

---

## NORTH STAR

APPIC is not a shop, not a component gallery, not a dashboard. It is a private
foundry for commissioning and collecting handmade objects, authored so that
**authority, motion, media type, ownership of UI, gesture grammar, the author
door, attach step-downs, and overlay family vs anchored family are first-class
rooms a human can walk.**

Editorial. Expensive. Abundant negative space. Concentric radii. One cool
accent. No purple, gold, neon, gradient-blob slop. No emoji in chrome.

A visitor should feel: *this house has laws, and I can touch them.*

---

## KILL TRIGGERS

If you do any of these, **stop, undo, and continue on the product path**.
These are not style notes. They are ship-blockers.

1. **Any product UI in React / Vue / Svelte / Solid / Next / TanStack Start /
   JSX / TSX / `.tsx` / `.jsx`.** A Grok sandbox may keep platform
   `src/router.tsx` unused — they are not the product. Do **not** scaffold
   TanStack Start for APPIC.
2. **`vite` / `npx vite` / `npm run build` / Nitro as the ship gate.** Preview
   is uvicorn on `0.0.0.0:8080`. Historical failure: Vite treated CSS as JS
   (`CssSyntaxError: Unknown word export`). CSS first token must be CSS.
   Never JS `export` in a `.css` file.
3. **HTMX as architecture.** `use_htmx=False`. HTMX is a Document opt-in and
   stays **off**.
4. **HTTP verbs on page units.** No `get` / `post` / `put` / `patch` / `delete`
   on a Component. Clock A wraps `render()`.
5. **`from ux_compose.kit import Login` (or any kit card) as the live unit.**
   Copy via `uxcompose add`, own `components/`. Allowed only in tests / Nook /
   agents.
6. **`import ux_channel` / `cek` / `cek_host` / `cek_surface` / `MotionChannel`
   in product modules.** Isolation Law. Doctor AST-scan stays green.
7. **`host="batteries"`** or `DirectoryRouter` as the product host. Fails closed.
8. **Plans with `html=`.** XOR. Morph first from `render()`, then
   `transition.play`. Close of overlays is morph-only.
9. **Root `swipe.*` on Dialog / Sheet / ActionSheet.** Swipe lives on dismiss /
   handle / Keep it / Close. Handle grammar is
   `click swipe.down swipe.vertical threshold:48`.
10. **A second helper world.** No private `_tick`. No `appic/ux.py` `act()` that
    posts a different URL than `/act/{action}`. Official helpers:
    `from ux_compose import act, tick, field, status, maybe_plan, maybe_fade, maybe_slide`.
11. **Silent `except ImportError` without `AttachNote`.** Silence was the defect.
12. **Forcing Command / Dropdown / ContextMenu / Combobox / Select through
    OverlayChrome.** Wrong family. House is anchored; `/overlay` is edge.
13. **Invented library names** (`Page`, `when`, `forall`, `ux.div`,
    `StreamingRoute`, `location.reload()` as the happy path after `.py` save).
14. **Grok platform Auth ON / Database ON.** Kit `Login` / `Otp` are foundry
    Caps against the Host store — not Grok accounts.
15. **Incomplete kit.** A stem that exists on disk but is not live in a room
    is not utilisation. 23 catalog stems + `components/overlay.py`.

---

## 0. Non-negotiable

- Public imports are `from ux_compose import …` only.
- Product modules **never** import the wire.
- **Page units have no HTTP verbs.** Extra APIs live on the FastAPI process
  `build()` returned.
- **Ownable kit.** Product units are copies under `components/`.
- Serve on `0.0.0.0:8080`. Keep Grok `extensions.js` in the shell. Do not hide
  the Created-with-Grok pill. Vanilla preview-host bridge (`postMessage`
  `grok-preview-bridge` v1: hello / navigate / history / location / routes / ready)
  if platform files exist unused.
- Canonical product path is what `uxcompose create-app` writes. Deploy looks
  for `app.py`. Default ASGI is `app:asgi`. Sandbox `startup.sh` binds uvicorn
  to `0.0.0.0:8080` via `app:asgi` or `appic.server:app` — **not** `npm run dev`.
- Auth OFF (Grok §0.5). Database OFF. Domain lives in an in-memory Host store.
- Consume the existing **bitplorer/appic** foundry if present. Upgrade rooms.
  Do not recreate a second product next to a working one.

---

## 1. What ux-compose actually is

Thin pure-Python **composition + delivery** root (`0.1.0`, Clock A, kit on `main`).
It harnesses four specialists and must **not** reimplement them:

| Specialist | Role | Unlock | Install |
|---|---|---|---|
| **ux-dom** | Tag trees, Document SSoT, serialize, className, `<link>`, package static, CSP stamp | L0 | `git+https://github.com/bitplorer/ux-dom.git` (prefers Python ≥3.14; same tag call shape on 3.10–3.13 with `HAS_DOM`) |
| **ux-behavior** | `Component`, `MorphState`, `RefState`, `@action`, Ops | L1 | `git+https://github.com/bitplorer/ux-behavior.git` |
| **ux-channel** | Intent → Cap → Result. Behind compose `wire/` only | L2 | `git+https://github.com/bitplorer/ux-channel.git#subdirectory=python` |
| **ux-motion** | Scene Plans, presence, Morph-then-Play (`transition.play`) | L3 | `git+https://github.com/bitplorer/ux-motion.git` |

**Progressive Superpower:** the **same Component class** is correct at L1
(`dispatch`) and L3 (`use_channel` + `use_motion`). Zero rewrite.

PyPI / import / CLI: `ux-compose` / `ux_compose` / **`uxcompose`**.
`ux_compose.__version__ == "0.1.0"`. Pin vendor to SHA
**`7ea3eb8813d280a975c4a41d23a2e2d4de40a506`**.

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

Then copy the kit into the product (you own the files):

```
uxcompose add --list
for s in login tabs accordion dropdown dialog sheet toast command table pagination \
         combobox sidebar breadcrumb stepper carousel calendar select otp plans \
         actionsheet contextmenu typeahead pullrefresh; do
  uxcompose add "$s" --force
done
# OverlayChrome is NOT a catalog stem — copy it anyway:
cp vendor/ux-compose-src/ux_compose/kit/overlay.py components/overlay.py
```

If the CLI is not on PATH, copy `src/ux_compose/kit/{stem}.py` into
`components/{stem}.py` with the ownable banner. Restyle `class_*` to APPIC tokens.

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
act, tick, field, status,
maybe_plan, maybe_fade, maybe_slide,
AttachNote, attach_notes,
Level, doctor, DoctorResult,
scene, fade, rise, slide,     # None until ux-motion is installed
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

From the **owned** copy `components/overlay.py` (not `ux_compose.kit`):

```
OverlayChrome, overlay
```

Kit catalog (from `ux_compose.kit.catalog` — for `uxcompose add` + Trace evidence,
not as the shipped card):

```
KitEntry, CATALOG, list_components, resolve
copy_component, find_app_root, KitCopyError
```

### App

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
app.attach_notes                  # this App's step-downs
```

Level labels: `0 static + routing` · `1 offline interactive` · `2 live channel` · `3 motion`.

### Author helpers — exact signatures (ADR 0004)

```
act(action, label, *, kind="secondary", target="#stage", on=None, **args)
    POST form to /act/{action}. Alias that path onto /action/{name}.
    on= stamps data-channel-on.

tick(comp, *, on="tick", off="tock")
    Flip comp.stamp. Product uses this — never a private _tick.

field(name, value="", *, placeholder="", kind="text")
status(text, *, kind="note")          # empty → class "sr"

maybe_plan(name, target, *, ms=140)
maybe_fade(name, target, *, ms=120)
maybe_slide(name, target, *, direction="next"|"prev", ms=180)
    return None when ux-motion is absent
```

`examples/_common.py` re-exports the same objects. Product imports from
`ux_compose`.

### OverlayChrome — exact constants

```
overlay(root_id, *, kind=None, edge=None) -> OverlayChrome
ids: {root}-scrim / {root}-panel / {root}-dismiss

swipe_on_dismiss():
  center → click swipe.down
  right  → click swipe.right
  left   → click swipe.left
  bottom → click swipe.down
  top    → click swipe.up

swipe_on_handle():
  bottom → click swipe.down swipe.vertical threshold:48
  top    → click swipe.up swipe.vertical threshold:48

open_plan(*, fade_ms=120, enter_ms=180)  # selectors only, no html=
  center → fade scrim + rise panel
  right  → fade scrim + slide x=28
  left   → fade scrim + slide x=-28
  bottom → fade scrim + slide y=32
  top    → fade scrim + slide y=-32
```

Edge family: Dialog, Sheet, ActionSheet.
Anchored family (do **not** copy these ids): Dropdown, ContextMenu, Combobox,
Select, Command.

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

### Component

- `id` is the morph + motion target (default `ClassName.lower()`).
- `render()` returns a tag tree, an HTML string, a **dict** (JSON), a **generator**
  (stream), or an already-built Response. Never a construct-time snapshot.
- `@action(caps=())` public. Non-empty caps need a live Cap or fail closed.
- Return `update_with(self, plan, extra_ops=[notify(...)])`. XOR: plans carry **no** `html=`.
- Prefer `bind(self.verb, **args)`. `control("surface.verb", **args)` is the stringly hatch.
- `morph_play("#id", plan)` once (Lab motion hop). Everywhere else: `update_with`.
- **Do not subclass ux-dom `Component`** (MRO collides).
- Kit copies: subclass the **copied** card, override the host seam
  (`authenticate`, `on_confirm`, `on_run`, `on_pick`, `on_verify`, `on_choose`,
  `on_finish`, `on_refresh`, `ACTIONS`, `SEED`, `COMMANDS`), restyle `class_*`.

### Encoding rule

| What | Where |
|---|---|
| Open / value / query / named step / named band | `MorphState` (qualitative) |
| Magnitude, lists, money, ISO dates, files, digits | `RefState` + `stamp = MorphState("idle")` |
| Stamp flip | official `tick(self)` |
| One-shot message | `notify(...)` |
| Domain stock / money / bookings | Host store, never the client plane |
| Protected verb | `@action(caps=("orders.place",))` + host mint at HTTP door |

---

## 3. Clock A — two clocks, one foundry

| Clock | Trigger | Pipeline |
|---|---|---|
| **A — page GET** | Browser hits a filesystem URL | resolve_unit → `render()` → payload dispatch |
| **B — live action** | `@action` / Channel Intent | mutate → Ops → morph |

**Payload law.** The return value of `render()` picks the HTTP container.

| `render()` returns | HTTP | Document wrap |
|---|---|---|
| tag / HTML `str` / bytes | `HTMLResponse` | yes (author Document) |
| `dict` or list-of-dicts | JSON | **no** |
| generator / async generator | `StreamingResponse` | **no** |
| already a Response | as-is | **no** |

`str` is iterable. **It is not a stream.** Path params:
`routes/atelier/[sku].py` class `Sku` → `def render(self, sku: str = "")`.
Class name never in the URL. Stem matches class. `≤1` page owner per file.

Prove Clock A with three page units (not extra FastAPI routes):

| File | URL | `render()` returns | Proves |
|---|---|---|---|
| `routes/health.py` class `Health` | `/health` | `{"ok": True, "level": …, "version": __version__, "kit": …}` | JSON payload door |
| `routes/pulse.py` class `Pulse` | `/pulse` | generator yielding `<div id="beat-n">…</div>` chunks | stream payload door |
| `routes/atelier/[sku].py` class `Sku` | `/atelier/{sku}` | tag tree, **no `get()`** | HTML + path params |

---

## 4. Ownable kit + OverlayChrome + Wave 1 Signal

### Copy, then own

```
components/           # uxcompose add drops files here
  __init__.py
  login.py            # Login, AuthDecision
  overlay.py          # OverlayChrome, overlay — NOT a catalog stem
  tabs.py … pullrefresh.py
routes/enter.py       # subclasses copied Login + Otp — not the library module
```

Every one of the **23 catalog stems** must exist as an owned file under
`components/` **and** appear, live, in a product room (Desk / House / Visit /
Door / Signal). `components/overlay.py` must exist and be used by Dialog /
Sheet / ActionSheet **and** the Overlay room. A kit card that only exists on
disk is not utilisation.

### Kit grammar (fail closed)

1. Tailwind **`class_*` only**. Restyle to APPIC tokens. No companion CSS per card.
2. Named keys on MorphState. Quantity on RefState. Stamp via official `tick()`.
3. No viewport `sm:` inside cards. Containment: `min-w-0` + `overflow-x-hidden` + wrap.
4. **Swipe lives on the handle / Keep it / Close, never on the root.**
   A host-level `swipe.vertical` swallows row clicks (Share / Cancel do nothing).
5. Overlay cards drop `relative` / overflow so `fixed` overlays are not clipped.
6. Open = Motion enter plan, selectors only, no Channel attr, no kit JS.
   Close = morph-only (panel is gone after apply).
7. Carousel: 44px overlay chevrons, dots-only bottom rail, one `#id-thumb` pip
   that **translates**. Root stamps `data-channel-id`. Copy is the live region.
8. Pagination: windowed numbers (`WINDOW=1`). 44px chevrons. First/last + gaps
   `max-sm:hidden`. Prev is one named page back, disabled on page 1. Demo 12 pages.
9. Dialog Keep it: `click swipe.down`. Delete is click-only (Cap).
10. Sheet Close/Done: `click swipe.right`. ActionSheet handle:
    `click swipe.down swipe.vertical threshold:48`.
11. ContextMenu: click **or** `longpress`. Floating panel, `menuitem` rows, not a native ul.
12. Typeahead: the field is the control — `input delay:300`. Live Results morph
    `#{id}-hits` only. The field (`#{id}-q`) is not in that HTML, so a
    pause-fired Result cannot rewrite what is still being typed. Later
    `input`/`change` of the same control aborts the in-flight Intent.
    Pick still morphs the card so the name can land in the field.
    Stamp `data-channel-target="#{id}-hits"`. No kit JS.
13. PullRefresh: list `swipe.vertical`; Refresh control `click swipe.down`. Phase is a **name**.

### Signal room

`/signal` makes the grammar visible as wax-stamped chips:

`swipe.vertical` · `swipe.horizontal` · `click swipe.down` · `click swipe.right` ·
`click swipe.left` · `longpress` · `input delay:` ·
`click swipe.down swipe.vertical threshold:48` · `data-channel-id` · `data-channel-on`

A human can **do** each one: pull the ledger, swipe a sheet closed, longpress a
mark, type into typeahead and watch the filter attach after delay, swipe the
ActionSheet handle without killing row clicks.

### Overlay vs anchored (must be two rooms)

| Room | Family | Proof |
|---|---|---|
| `/overlay` | Edge — Dialog / Sheet / ActionSheet | OverlayChrome ids, dismiss grammar, handle `threshold:48`, enter x=28 / y=32, open_plan selectors-only, close morph-only |
| `/house` | Anchored — Typeahead, Combobox, Select, Dropdown, ContextMenu, Command (Desk), plus Sheet/ActionSheet as guests | Command / Dropdown / ContextMenu **do not** stamp `{id}-scrim`. Prove the family split on Trace |

---

## 5. Product filesystem (create-app layout — locked)

```
app.py                 # composition root — build() only
settings.py            # BASE_DIR, DEBUG, WebAssets(base_dir=assets, dry_run=False)
document.py            # ONE Document + .use(XElement(), Csp.auto())
requirements.txt
assets/css/input.css
assets/static/file/css/output.css
components/            # OWNABLE KIT COPIES (23 stems + overlay.py)
appic/                 # product package
  server.py            # extra APIs on the FastAPI process (POST /action/{name} + /act/{name})
  chrome.py            # Toasts, Palette, Banner, Ribbon (fragments, no URL)
  store.py             # Host domain
  ux.py                # App helpers — re-export official act/tick/field/status/maybe_* ; do not invent a second door
  tags.py / marks.py   # SVG marks via svg/path/rect/circle + raw() once
  routes/
    index.py           # class Index → /
    atelier.py
    atelier/[sku].py   # class Sku → /atelier/{sku}  NO get()
    commission.py
    bag.py
    board.py
    studio.py
    ledger.py
    lab.py
    lattice.py
    trace.py
    clocks.py
    relay.py           # Relay — serve-dev split, soft morph, restart-channel
    health.py          # JSON
    pulse.py           # stream
    enter.py           # Door — Login + Otp
    desk.py            # Desk — Sidebar, Breadcrumb, Tabs, PullRefresh, Accordion, Command, Toast
    house.py           # House — Typeahead, Combobox, Select, Dropdown, Sheet, Carousel, Table, Pagination, ContextMenu, ActionSheet
    visit.py           # Visit — Stepper, Plans, Calendar, Dialog
    signal.py          # Signal — Wave 1 grammar made visible
    author.py          # Author — official act / field / status / tick / maybe_*
    notes.py           # Notes — AttachNote notebooks
    overlay.py         # Overlay — OverlayChrome vs anchored family
public/favicon.svg
public/og.jpg          # 1200×630 custom
src/lib/og/site.json   # { "title": "APPIC", "card": "custom", "color": "0c0d0b" }
vendor/…
startup.sh             # binds 0.0.0.0:8080 via uvicorn
FEATURE_INVENTORY.md
GROK_BUILD_PROMPT.md
```

Scan path used in product:

```python
found = scan_surfaces(PACKAGE, base_directory="routes")
validate_surfaces(found)
```

Render `bundle.surfaces`, `bundle.route_table`, `bundle.action_table`,
`bundle.unit_registry`, `bundle.sealed`, and `list_components()` on
**Trace**, **Lattice**, **Clocks**, and **Signal**.

---

## 6. Hard laws (fail closed)

1. **Isolation.** Product modules never import the wire. `doctor` AST-scan stays green.
2. **Document SSoT.** Exactly one `Document(...)` in `document.py`. Overlays stay in the tree when closed.
3. **XOR + Morph-then-Play.** Plans carry **no** `html=`. Morph first from `render()`, then `transition.play`.
4. **Cap Law.** Protected verbs fail closed without a Channel-minted Cap.
5. **Encoding.** Qualitative MorphState. Magnitudes on RefState + stamp via official `tick()`.
6. **Presence continuity.** Stable ids (`id="item-{sku}"`). `scene.stagger_in` on survivors. `scene.share(key, leave=, arrive=)` — share id is identity, not a CSS class.
7. **Cold import never pulls the wire.** `App.boot("auto")` is L1.
8. **CSS.** No CSS or client JS inside Python strings. Tokens in `assets/css/input.css`. Kit: `class_*` only. Document links `/css/output.css`. `WebAssets.mount_css` serves it. If Tailwind CLI is missing, ship a complete hand-authored `output.css` **and** still call `WebAssets`. First token of every `.css` file is CSS.
9. **HMR / tunnel** are `uxcompose serve` delivery, not `Document.use`. Expose `HMR_PATH` as a chip on Trace.
10. **Clock A.** No HTTP verbs on page units. Payload type picks media type. Author Document wraps GET.
11. **Ownable kit.** Copy, restyle, override host seams. Do not import the library kit as the shipped card.
12. **Signal.** Swipe on handle / Keep it / Close. Never a root swipe.
13. **One author door.** Official helpers only.
14. **Attach notes refuse silence.**
15. **OverlayChrome is the edge primitive.** Anchored family does not copy its ids.
16. **Leftovers expire by teaching.** Doctor flags kit-imports, `host="batteries"`, teaching `App.mount` as the product path, root swipe. It does not fail-close on them.
17. **No invented library names.**

---

## 7. CLI the product must honor

```
uxcompose create-app myapp --name APPIC --level auto --host auto
uxcompose serve dev  [app:asgi] [--host 0.0.0.0] [--port 8080] [--reload-dir PATH ...] [--tunnel none|ngrok|cloudflare]
uxcompose serve prod [app:asgi] [--host 0.0.0.0] [--port 8080]
uxcompose serve restart-channel
uxcompose build [--no-minify] [--skip-tailwind] [--skip-import] [--app app:asgi]
uxcompose deploy --provider docker|fly|render|railway|vps|checklist [--force] [--name NAME]
uxcompose doctor . --no-fail
uxcompose add --list
uxcompose add login [--page --force]
```

`uxcompose serve` with no mode **exits 2**. There is no `--hmr`, `--css-watch`,
`--one-process`, or `--reload-channel`. Soft morph is the happy path on `*.py`
save (`Idiomorph` → id replace → `location.reload()` fallback). CSS save never
kills the ui worker. Channel RAM drops only via `restart-channel` (SIGUSR1 to
the origin pidfile; missing pidfile fails closed). Tunnel is
`serve dev --tunnel ngrok|cloudflare`. `uxcompose build` is one-shot minify —
no `--watch`. Deploy starts raw uvicorn, not `serve`.

Host extra routes on the ASGI **process** (not on the class):

- `POST /action/{name}` — progressive enhancer. Cap-suffixed verbs mint then invoke.
  Morph `#surface` with Idiomorph (else outerHTML). Full page GET still works without JS.
  Accept both `dispatch(name, **kwargs)` and `dispatch(name, args={...})`.
- `POST /act/{name}` — **alias of `/action/{name}`** so official `act()` works.
- `GET /api/surfaces` — extra FastAPI JSON (proves `default_response_class` was **not** set to HTML)
- `GET /api/kit` — JSON list of owned kit stems + catalog descriptions (proves kit utilisation)
- static `/css` via `WebAssets.mount_css`
- static `/public` for og + favicon

`GET /health` is a **page unit** (`routes/health.py`), not an extra FastAPI route.

Progressive enhancer JS is a **small** host file (Idiomorph + POST `/action/{name}`
+ toast plane + `⌘K` + Channel swipe/longpress/input-delay attrs). It is not a SPA.

Cap suffixes that mint: `checkout`, `redeem`, `book`, `verify`, `wipe`,
`moderate`, `next`, `place`, `reset`, `mint`, `sell`, `login`, `signup`, `finish`,
`archive`, `pick`, `submit`.

---

## 8. Catalog — every pattern ships **in the product**

Source of truth: `ux-compose/examples/` (75 classes) **and**
`ux-compose/src/ux_compose/kit/` (23 ownable cards + overlay primitive).
Copy the *contract*, not the demo copy.

Keep every pattern from the previous APPIC prompt (Tabs through Shortcuts, Caps,
`scene.share`, stagger, command palette). Do not drop a working room to make space
for kit rooms — **add rooms**.

Every stem in §4 appears as a live card in Desk / House / Visit / Door / Signal /
Overlay. Host seams are overridden so the cards speak APPIC copy (benches, flax,
iron, wax seals) not the library's stone demo.

Login: demo any valid email/password signs in; `@blocked.test` fails closed;
signup requires a digit in the password; submit spends `auth.login` / `auth.signup`.
OTP: six digits attach; `000000` refused; `2048` (padded) or any other six verifies;
spends `auth.otp`.

---

## 9. Product — APPIC (*Intent. Presence. Caps. Kit. Signal. Author. Notes. Chrome.*)

A private foundry for commissioning and collecting handmade objects. Editorial,
expensive, abundant negative space, concentric radii. **The kit is the house
the foundry lives in.** You copy a card, restyle it, override the seam — then
it is yours. Signal is how the house listens (swipe, longpress, delayed input).
The author door is how you write. Attach notes are how the house admits a
missing specialist. OverlayChrome is how the edge family stays one primitive.

**Palette.** Dark ink `#0c0d0b`, elevated `#141512`, surface `#1a1b18`,
bone `#ebe6d8`, muted `#9a9488`, cool accent `#c8ccd4`, danger `#c17a6e`,
ok `#8fa394`. No purple, gold, neon, gradient-blob slop. No emoji in chrome.
Sparse monochrome SVG marks (`svg`/`path`/`rect`/`circle`). `raw()` used
**once** for a safe SVG mark, not CSS.

**Type.** Display **Fraunces** 500–600, body **Source Sans 3**, mono **IBM Plex Mono**.
Fluid `clamp` titles. Tabular nums on money / KPI.

**Motion tokens:** `--motion-stagger: 40ms` … `--motion-slow: 400ms`,
`--ease-out: cubic-bezier(0.22, 1, 0.36, 1)`. Honor `prefers-reduced-motion`.
Density + motion **names** on `<body>`. Kit overlays: OverlayChrome `open_plan()`
for sheets and action sheets (x=28 / y=32); fade scrim + rise panel for dialogs.

### Surfaces

| Path | Unit | Must exercise |
|---|---|---|
| `/` Table | `Index` | Pulse counter+stamp via official `tick()`, **`bind(self.beat)`**, intent field, KPI, benches, last Ops, `Level` badge, `__version__` chip, doors into Desk / House / Visit / Enter / Signal / Author / Notes / Overlay |
| `/atelier` | `Atelier` | Shelf filter/sort/`stagger_in`, wishlist, compare≤3, lightbox, add-to-bag, link to PDP |
| `/atelier/{sku}` | `Sku` | DirectoryRoutes `[sku]`. **No `get`.** `render(self, sku="")`. `scene.share` into bag |
| `/commission` | `Commission` | 4-step wizard + radio/checkbox/slider/date/file/password/autosave/limited note/OTP Cap `identity.verify` (`2048`) / place Cap `orders.place` |
| `/bag` | `Bag` | Stepper, coupon Cap `orders.coupon` (`HOUSE`/`FLAX`/`TABLE`), checkout Cap `orders.place`. After successful place, return a `RedirectResponse` to `/ledger` |
| `/board` | `Board` | Kanban optimistic + undo + data table bulk |
| `/studio` | `Studio` | Chat typing, inbox, comments moderate Cap `comments.moderate`, presence |
| `/ledger` | `Ledger` | Calendar book Cap `calendar.book`, WebAssets `css_href` chip, wipe Cap `settings.wipe` |
| `/lab` | `Lab` | Remaining examples catalog: tree, carousel, reorder, empty-retry, chips, inline, combobox, accordion, drawer, **`morph_play` hop**, share seat, Morph vs Ref |
| `/lattice` | `Lattice` | Caps as seals. Intent as nucleus. Ops as traces. **`bind(self.mint)` is a Cap.** SurfaceBundle as stars. `dispatch(..., args={})` proven |
| `/trace` | `Trace` | Live Ops log, doctor, Isolation evidence, `HMR_PATH`, `Level.label`, bundle tables, CSP header chip, `apply_html_document` note, **kit catalog list**, leftover teaching chips, OverlayChrome vs anchored family chips |
| `/clocks` | `Clocks` | Dual-clock room. Clock A GET vs Clock B action. Payload doors (HTML / JSON / stream) as three gates |
| `/relay` | `Relay` | Three serve clocks (process / HMR / CSS) as live rings. Modes as named MorphState (`dev` / `prod` / `drop`). Soft-morph law. `HMR_PATH` + `CSS_URL_PREFIX`/`OUTPUT_CSS_NAME` chips. `bind(self.drop)` is the restart-channel analogue |
| `/health` | `Health` | `render()` returns a **dict**. Includes `ok`, `level`, `label`, `version`, `sealed`, `surfaces`, `kit` |
| `/pulse` | `Pulse` | `render()` returns a **generator** of HTML chunks. StreamingResponse |
| `/enter` | `Enter` | **Door.** Owned `Login` + `Otp`. Caps `auth.login` / `auth.signup` / `auth.otp`. `@blocked.test` fails closed |
| `/desk` | `Desk` | Sidebar, Breadcrumb, Tabs, PullRefresh, Accordion, Command, Toast — all owned copies, restyled. Command is **anchored family** |
| `/house` | `House` | Typeahead, Combobox, Select, Dropdown, Sheet, Carousel, Table, Pagination, ContextMenu, ActionSheet. Anchored vs edge guests labeled |
| `/visit` | `Visit` | Stepper, Plans, Calendar, Dialog. Finish Cap `flow.finish`. Dialog confirm Cap. Calendar `on_pick` books a bench |
| `/signal` | `Signal` | Wave 1 grammar as a walkable room. Each synthesizer is a live control, not a legend. Include handle `threshold:48` |
| `/author` | `Author` | Official `act` / `field` / `status` / `tick` / `maybe_*` **imported from `ux_compose`**. POST `/act/{action}` (aliased to `/action/{name}`). `act(..., on=)` once. Attach-notes strip |
| `/notes` | `Notes` | `AttachNote`, `attach_notes()`, `App.attach_notes`. Process vs App notebooks. Doctor capabilities. Dual-write explained |
| `/overlay` | `Overlay` | OverlayChrome ids, swipe-on-dismiss, handle grammar printed live, enter distances named (right x=28, bottom y=32), `open_plan()`. Owned Dialog / Sheet / ActionSheet. Family split stated |
| Chrome | `Toasts`, `Palette`, `Banner`, `Ribbon` | `⌘K`; live Ops ribbon; wax-seal burst on Cap mint |

### Caps (real, fail closed)

`orders.place` · `orders.coupon` · `identity.verify` · `calendar.book` ·
`settings.wipe` · `comments.moderate` · `admin.reset` · `lattice.mint` ·
`auth.login` · `auth.signup` · `auth.otp` · `flow.finish` · `rows.archive`

OTP verify accepts `2048`. Coupons: `HOUSE` / `FLAX` / `TABLE`.
Login blocked: `@blocked.test`. OTP refuse: `000000`.

### Radical interactions (must all work)

1. **Hold an intent on the Table.** Type a verb, press the nucleus, Clock B
   fires, Trace records the Op, Lattice lights the matching star.
2. **Walk through the Door.** Sign in (Login Cap). Verify (OTP Cap). The ribbon
   bursts a wax seal. `@blocked.test` is refused.
3. **Sit at the Desk.** Pull-to-refresh the ledger. Command palette `⌘K` posts
   the same `/action/{name}` door. Accordion keeps several panels open.
4. **Walk the House.** Typeahead filters on `input delay:`. Longpress a mark
   for ContextMenu. ActionSheet handle swipes down (`threshold:48`) without
   killing row clicks. Carousel pip translates. Pagination windows. Sheet Close
   swipes right.
5. **Pay a Visit.** Stepper named steps; finish is a Cap. Plans radio cards.
   Calendar `on_pick`. Dialog Keep it swipes down; Delete is a Cap.
6. **Stand in Signal.** Every Wave 1 synthesizer is labeled and live, including
   handle `threshold:48`.
7. **Commission a piece.** Wizard MorphState named steps. Magnitude is RefState + official `tick()`.
8. **Sort the atelier.** Survivors keep `id="item-{sku}"` and `stagger_in`.
   Add-to-bag plays `scene.share`.
9. **Open `/health`.** JSON. The document did not wrap it.
10. **Open `/pulse`.** Chunks arrive.
11. **Open `/clocks`.** Two rings. Three gates. The foundry explains itself.
12. **Stand in Relay.** Choose serve-dev, serve-prod, or restart-channel. Soft morph is named. Drop Channel RAM — the pulse stamps dropped.
13. **Checkout without a Cap is refused.** Host-mint then succeeds.
14. **Wipe settings** is a Cap. Confirm modal stays in the tree when closed.
15. **Doctor is green.** Isolation scan of `appic/` + `components/` is clean.
16. **Own the kit.** Edit a `class_*` string; the card is yours. Trace lists 23 stems + overlay.py.
17. **Stand in Author.** Hold a presence through official `field()`. Pulse via official `act()` (posts `/act/author.pulse`). Flip official `tick()`. Play `maybe_plan` / `maybe_fade` / `maybe_slide`. Status names the last Op. One `act(..., on=)` chip.
18. **Read Notes.** `App.attach_notes` and process-wide `attach_notes()` are two notebooks. Silence was the defect. Doctor capabilities listed.
19. **Inspect OverlayChrome.** Dialog / Sheet / ActionSheet share one primitive. Ids printed. Dismiss grammar printed. Handle `click swipe.down swipe.vertical threshold:48` printed. Enter distances named. Close is morph-only. Anchored family is named as the other house.

---

## 10. Coverage matrix (must all be true before you stop)

- [ ] `from ux_compose import App, build, WebAssets, DirectoryRoutes, DirectoryASGI, RouterHooks`
- [ ] `Surface`, `SurfaceBundle`, `SurfaceError`, `scan_surfaces`, `validate_surfaces`, `mount_surfaces` imported and used
- [ ] `Component, MorphState, RefState, action, bind, control, notify, update_with, morph_play`
- [ ] `Level, doctor, DoctorResult, __version__`
- [ ] `scene, fade, rise, slide` imported with `None` fallback
- [ ] Tags: `div` … `circle`, `HAS_DOM`, `raw` (raw used once for a safe SVG mark, not CSS)
- [ ] `http_path`, `is_json_payload`, `is_stream_payload`, `apply_html_document` used on Trace / Clocks
- [ ] `settings.py` + `document.py` (`Csp.auto()`) + `app.py` + `assets/css/input.css` + `WebAssets.mount_css`
- [ ] Nested `routes/atelier/[sku].py` live PDP, `render(self, sku="")`, **no `get()` anywhere**
- [ ] JSON page unit `/health` (`dict`) and stream page unit `/pulse` (generator)
- [ ] Dual-clock room `/clocks`
- [ ] Relay room `/relay` — three serve clocks, modes as MorphState, HMR_PATH, restart-channel analogue
- [ ] **23 kit stems copied under `components/` and live in Desk / House / Visit / Enter / Signal**
- [ ] `components/overlay.py` exists (not a catalog stem) and is imported by Dialog / Sheet / ActionSheet **and** `/overlay`
- [ ] Kit host seams overridden (authenticate / on_confirm / on_run / on_pick / on_verify / on_choose / on_finish / on_refresh)
- [ ] Wave 1: ActionSheet handle swipe with `threshold:48`, ContextMenu longpress, Typeahead `input delay:`, PullRefresh `swipe.vertical`
- [ ] OverlayChrome enter distances proven: right sheet `x=28`, bottom actionsheet `y=32`
- [ ] Anchored family (Command / Dropdown / ContextMenu / Combobox / Select) does **not** copy OverlayChrome ids
- [ ] `bind()` on Pulse and Lattice mint
- [ ] `dispatch("…", args={...})` proven
- [ ] `morph_play` used once; `update_with` used everywhere else
- [ ] Caps listed above fail closed without mint; succeed after host mint
- [ ] `scene.share` atelier card → bag line; `stagger_in` on shelf sort
- [ ] Checkout success returns `RedirectResponse` (Response as-is door)
- [ ] Command palette `⌘K` posts the same `/action/{name}` door
- [ ] Extra FastAPI `GET /api/surfaces` and `GET /api/kit` stay JSON
- [ ] Custom OG + favicon + `src/lib/og/site.json`
- [ ] Mobile 390px: no overflow, 44px targets, wrap nav, bottom nav
- [ ] `startup.sh` binds `0.0.0.0:8080` via uvicorn — **not** `npm run dev` / vite
- [ ] Vendor copy of `ux_compose` + specialists + `requirements.txt` + SHA file
- [ ] Isolation scan of product package **and** `components/` is clean
- [ ] No `.tsx` / `.jsx` **product** UI
- [ ] `FEATURE_INVENTORY.md` and this prompt stay in the repo
- [ ] `act, tick, field, status, maybe_plan, maybe_fade, maybe_slide` imported from `ux_compose` and live on `/author`
- [ ] Official `tick()` used for stamp flips — no private `_tick` in product
- [ ] `act(..., on=)` demonstrated once
- [ ] `AttachNote`, `attach_notes()`, `App.attach_notes` live on `/notes`
- [ ] POST `/act/{name}` aliases `/action/{name}` for official `act()`
- [ ] CSS first token is CSS (never `export`)
- [ ] Leftover teaching chips on Trace (`host="batteries"`, kit-import, `App.mount` as product path, root swipe)

---

## 11. A-tier quality

Editorial, not playful-slop. Sparse type. Concentric radii. One accent.
Honor reduced motion. Every `@action` mutates state and morphs. Caps are real.
Motion degrades. Isolation holds. Clock A is correct. The kit is owned.
Signal is felt, not documented. The author door is one. Attach notes are
visible. OverlayChrome is the edge. Anchored is the other house.

| Check | Bar |
|---|---|
| 390px | no horizontal overflow, 44px targets, wrap nav, bottom nav |
| Desktop | abundant negative space, no dense dashboard |
| Palette | ink / bone / cool only. No purple / gold / neon |
| Type | Fraunces display, Source Sans 3 body, IBM Plex Mono traces |
| Motion | OverlayChrome `open_plan` distances; `prefers-reduced-motion` |
| Console | clean |
| Caps | fail closed, then succeed after mint |
| Doctor | Isolation green on `appic/` + `components/` |
| Preview | uvicorn on `0.0.0.0:8080`, left running |

The lattice is the product's radical face: **authority made visible.**
The trace is the product's memory: **Ops as data.**
The clocks room is the product's honesty: **GET and action are two pipelines.**
The relay is the product's delivery: **serve is two modes plus one action, not a flag soup. Soft morph first.**
The door is the product's threshold: **Login and OTP are Caps, not a SPA.**
The desk / house / visit are the product's rooms: **owned kit, not a gallery.**
The signal room is the product's grammar: **swipe, longpress, delay — as data.**
The author door is the product's honesty: **one helper world, not two.**
The notes room is the product's memory of attach: **step-downs are visible.**
The overlay room is the product's edge: **one primitive, three widgets, two families.**
The atelier PDP is the product's routing proof: **filesystem → HTTP.**
The health and pulse doors are the product's host proof: **return value picks the container.**
The skin is WebAssets: **tokens compiled, not inlined.**
The copies under `components/` are the product's ownership: **shadcn-style, MorphState-native.**

Ship a running foundry. Verify it actually renders — desktop and 390px —
with a clean console. Leave uvicorn up on `0.0.0.0:8080`.
