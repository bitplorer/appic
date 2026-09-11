# Grok Build prompt — APPIC on ux-compose 0.1.0 (kit-81 + Kit Cut 1)

Pin: [bitplorer/ux-compose](https://github.com/bitplorer/ux-compose) `@ main`
SHA **`bf55750b5268867aa5931a2171e69ac533808e1e`** (2026-09-11 honesty-locks + FileStateStore).
Companion: [FEATURE_INVENTORY.md](FEATURE_INVENTORY.md).
If this prompt and the library disagree, **the library wins**.

This file is the **metaprompt**. Publish it on **bitplorer/appic**. The executing
Grok Build agent copies **everything below the line**, clones the library first,
and ships a complete foundry. Repo **appic already exists** — upgrade it; do not
create a second repo.

## 2026-09-11 — Grok Build independent re-read (this session)

Walked `src/ux_compose/**/*.py`, `kit/catalog.py` (**81** keys counted from source),
`__init__.__all__`, `docs/ARCHITECTURE.md`, `docs/OWNERSHIP.md`, `AGENTS.md`,
`CHANGELOG.md` Unreleased honesty-locks (PR #68), `examples/README.md`, and the
four product apps (`atelier_shop`, `atelier_studio`, `nook`, `pulse`).

**Library floor this session**

| Pin | SHA |
| --- | --- |
| ux-compose | `bf55750b5268867aa5931a2171e69ac533808e1e` |
| ux-dom | `e8be99a52bfecd6026c200fa1c3dc6a74f87aacb` |
| ux-behavior | `793f120e3b1388925772cd069b070d7918b78baa` |
| ux-motion | `67ff3f0c4912b70b7056f8226a6f226b6fe93f60` |
| ux-channel | `d0fe7169e687d2935f8b74d40b990b1ee63ef3d4` `#subdirectory=python` |
| cek-host / cek-surface | `>=0.1.3` |

Python **≥ 3.14**. Install: `git clone` + `pip install -e ".[serve]"` — **not PyPI**.

### Honesty locks that are now law (do not reopen)

These are the 2026-09-10 → 2026-09-11 delta. Previous APPIC pins (`060b583`) missed them.

1. **LOCK-1** — Public `__all__` covers host / surface / motion names (`WebAssets`,
   `DirectoryRoutes`, `DirectoryASGI`, `RouterHooks`, `Surface*`, `DoctorResult`,
   `scene` / `fade` / `rise` / `slide`). Product source must cite every name.
2. **ISO-2** — `__init__.py` is AST + text locked against `wire` / `ux_channel`
   imports. Product modules never import `ux_channel`, `cek`, `cek_host`,
   `cek_surface`. Cold import never pulls the wire.
3. **KIT-1** — Command palette **does not** import OverlayChrome. Local
   `{id}-scrim` / `{id}-panel` / `{id}-dismiss` + `click keydown.escape`.
   Dialog / Sheet / ActionSheet / AlertDialog stay on OverlayChrome.
4. **HMR-shell** — `insert_live_client` leaves HTML fragments unwrapped. No
   synthesized `<!DOCTYPE html>` shell on morph payloads.
5. **CSS-spawn** — Sibling Tailwind `--watch` lives in `tailwind.py`
   (`start_tailwind_watch`). `hmr.py` does not `Popen`.
6. **SWALLOW-1 / SWALLOW-boot** — `_live_channel` swallows `ImportError` only.
   `ChannelConfig(secret=)` and `Channel.boot` fail closed. `App.use_channel`
   stamps L2 only when a Channel instance exists.
7. **SURF-1** — Two walkers, one door: `App.mount` / `scan_surfaces` is catalog
   scan; `DirectoryRoutes.discover` is HTTP path law. `build()` orchestrates both.
   Do not merge the walks. Do not teach `App.mount` as a second product path.
8. **FileStateStore** — Channel owns the JSON sqlite store. `serve_state.py` is
   lifecycle only (`UXCOMPOSE_STATE_STORE`). Doctor `scan_store_clone` fails
   closed if a store class reappears in the product tree. APPIC `store.py` is
   Host memory (commissions, bag, ledger) — **not** a Channel store clone.
9. **Folder law** — `kit/` is ownable-copy prefix. `kit_construct.py` stays next
   to `component.py`. CLI verbs stay as library modules, not a `cli/` package.
   `uxcompose add` rewrites `from ux_compose.kit.X` → `from .X` and **keeps**
   `from ux_compose.kit_construct import`.
10. **LEFTOVER-split** — Doctor-scanned tokens (`from ux_compose.kit import`,
    `host="batteries"`, `DirectoryRouter`, `stunning-root`, nav brand in
    `render()`) vs agent-only locks (`cli/` package, argv `create`,
    `docs/MODULE_MAP.md`). Do not credit doctor for names it does not scan.
11. **PYPI-1** — Brand tables never claim PyPI.
12. **DOOR-2** — CLI argv `create` is gone. Frozen verb is `uxcompose create-app`.
13. **openapi=False** — FastAPI Swagger stays off so product `/docs` can own GET.
14. **Kit Cut 1** — `render(*, shell=False, **slots)`. No `Kit` base. Kits stay
    `Component` subclasses. `shell=False` drops the Atelier kicker/title/lede.

### Author surface (do not invent names)

From `ux_compose.__all__`:

`App`, `build`, `WebAssets`, `DirectoryRoutes`, `DirectoryASGI`, `RouterHooks`,
`Surface`, `SurfaceBundle`, `SurfaceError`, `mount_surfaces`, `scan_surfaces`,
`validate_surfaces`, `Component`, `MorphState`, `RefState`, `action`, `bind`,
`control`, `notify`, `update_with`, `morph_play`, `act`, `mark_dirty`, `field`,
`status`, `optional_plan`, `optional_fade`, `optional_slide`, `AttachNote`,
`attach_notes`, `Level`, `doctor`, `DoctorResult`, `scene`, `fade`, `rise`,
`slide`, `HAS_DOM`, DOM tags (`raw` … `progress` including `dl/dt/dd`,
`table/thead/tbody/tr/th/td`, `fieldset/legend`, `hr/img/progress`).

Chrome (submodule, not `__all__`): `from ux_compose.chrome import brand_wrap,
GET_CHROME_ATTR, DEFAULT_BRAND`. Brand lives on `wrap=`, never inside `render()`.

Kit is **not** a public import path. Own a copy: `uxcompose add {stem}`.

### 81 kit stems (counted from `kit/catalog.py`)

login tabs accordion dropdown dialog sheet toast command table pagination
combobox sidebar breadcrumb stepper carousel calendar select otp plans
actionsheet contextmenu typeahead pullrefresh drawer navbar navmenu usermenu
popover tooltip alertdialog formlayout fieldset datepicker switch card
emptystate stats alert banner progress skeleton hero footer cta avatar badge
hovercard searchbar fileupload tagsinput multiselect descriptionlist featuregrid
testimonials newsletter bottomnav separator slider menubar toolbar togglegroup
spinbutton themeswitch filterbar chat questionnaire pricingsection logocloud
timeline rating chart resizable tree colorpicker fab diff countdown mockup
attachment scrollarea feed

Alias: `treeview` → `tree`. OverlayChrome is **not** a stem — copy `overlay.py`
anyway because Dialog/Sheet/ActionSheet import it.

### Encoding law (Channel session plane)

| Kind | Plane |
| --- | --- |
| Open / value / query / named step / named band | MorphState |
| Magnitude, lists, money, ISO dates, files, digits | RefState + `dirty = MorphState("idle")` |
| One-shot message | `notify(...)` |
| Domain stock | Host DB (`store.HOST`), never the client plane |
| Protected verb | `@action(caps=("orders.place",))` + live submit_intent |

The verb that sights a star is `look` — never a same-named action as the
MorphState field, or the field is overwritten.

### Product (do not ship a widget zoo)

**APPIC** — a nocturnal foundry OS. A constitution you can walk.

The document is the composition root made visible. Caps are wax seals that
break when spent. Intent is a nucleus. Ops are traces on a ribbon. Routes are
a constellation. Skin is WebAssets. GET is Clock A. Action is Clock B
(`POST /ux-channel/action`, `application/ux-channel+json`). Payload type picks
media type — HTML daylight, JSON pulse, generator stream. Kit cards are rooms
you own (`shell=False`). Copy press is the ownership ritual. OverlayChrome is
the edge primitive. Anchored popovers are a different family. AlertDialog is
interrupting — Escape does not dismiss it. `/docs` is a product page. Typeahead
morphs the hits slot, never the field being typed.

### Hard stack law

- **No React, Vue, Svelte, Solid, Next, TanStack Start, JSX/TSX as source of truth.**
- Server-authored hypermedia only. `use_htmx=False`.
- Preview: `uvicorn app:asgi --host 0.0.0.0 --port 8080`.
- Auth/DB OFF. Kit Login/OTP use Host store Caps, not Grok accounts.
- CSP must include `https://grok.com`. Never strip the Grok pill.
- Isolation: product never imports `ux_channel` outside compose `wire/`.
- `host="auto"`. Never `"batteries"` or `DirectoryRouter`.
- Python 3.14 via `uv python install 3.14`. `uv venv` + `uv pip`.

---


Copy **everything below this line** into Grok Build. You **are** Grok Build.
Execute it. Do not stop at a README. Ship a running foundry on `0.0.0.0:8080`.

---

# APPIC — a constitution you can walk (kit-81)

Build **APPIC** as a **complete product** (not a widget zoo) using
**https://github.com/bitplorer/ux-compose @ main**
(`bf55750b5268867aa5931a2171e69ac533808e1e`, **0.1.0**) as the **only** web UI
framework.

Fully utilise **every public name** in `ux_compose.__all__` (including the new
table / definition-list / form / media tags), every Clock A payload door, every
ownable kit card (`uxcompose add` — **all 81 stems**), OverlayChrome (copied even
though it is not a catalog stem), `brand_wrap`, the copy helper, every Wave 1
Signal token, every doctor scan family (hard + teaching, including render-chrome,
FastAPI docs collision, CEK host), the Presence cookbook, WebAssets,
`prepare_deploy` (six providers), tunnel grammar, HMR delivery, attach-note
notebooks, Tailwind resolver, probe matrix, `morph_play` hop, `AuthDecision`
verdict, Typeahead hits-slot, APG holds (menubar submenu ids stay in the tree,
toolbar `aria-current`, alertdialog no-escape-dismiss, FAB menu id stays hidden),
and every one of the **72 unique** Atelier Component classes in `examples/`.

> **The document is the composition root made visible. Caps are wax seals
> that break when spent. Intent is a nucleus you can hold. Ops are traces
> on a ribbon. Routes are a constellation. Skin is WebAssets. GET is Clock A.
> Action is Clock B. Payload type picks media type — HTML is daylight, JSON
> is a pulse, a generator is a stream of light. Kit cards are rooms you own.
> The copy press is the ownership ritual. Signal is a grammar in the hand.
> The author door is one. Attach notes refuse silence. OverlayChrome is the
> edge primitive. Anchored popovers are a different family. AlertDialog is
> interrupting — Escape does not dismiss it. Doctor residuals expire by
> teaching. Presence is continuous — objects that stay do not remount.
> HMR is delivery, not a Document API. Tunnel starts after health is green.
> Probe never shells. Login secrets never sit on MorphState. Typeahead
> morphs the hits slot, never the field being typed. Brand lives on wrap=,
> never inside render(). `/docs` is a product page, not Swagger. Quantity
> is RefState. Named things are MorphState. 81 stems, one house.**

**No React. No Vue. No JS/TS/TSX as source of truth.** Server-authored
hypermedia. Python + ux-compose. Serve uvicorn on `0.0.0.0:8080`.

Repo: **bitplorer/appic**. Create only if missing. Consume the running foundry.

Grok sandbox: Auth OFF. Database OFF. Do **not** scaffold TanStack Start /
React / Vite / Nitro. Kit `Login` / `Otp` are foundry Caps against the Host
store. Direct user law beats the sandbox's React default.

A visitor should feel: *this house has laws, and I can touch every room.*

---

## NORTH STAR

APPIC is a private nocturnal foundry for commissioning and collecting handmade
objects, authored so that **authority, motion, media type, ownership of UI,
the copy ritual, gesture grammar, the author door, attach step-downs, overlay
family vs anchored family, interrupting alerts vs public dialogs, doctor
residuals, presence continuity, skin, ship, HMR clocks, tunnel, probe, the
hits-slot law, GET brand chrome, product `/docs`, APG chrome (menubar /
toolbar / spinbutton / tree / feed / timer), marketing bands, glaze chemistry
(colorpicker), kiln time (countdown), and the 81-stem kit house** are
first-class rooms a human can walk.

Editorial. Expensive. Abundant negative space. Concentric radii. One cool
accent (`#c8ccd4` on ink `#0c0d0b`). Bone type `#ebe6d8`. Fraunces + Source
Sans 3 + IBM Plex Mono. No purple, gold, neon, gradient-blob slop. No emoji
in chrome. Film grain at 3.5% overlay. Pill buttons 44px. Hairline borders.
Soft single shadow. `prefers-reduced-motion`.

The Table is a **constellation**: named stars around a nucleus. Sight is
MorphState (looking is not walking). Walk is Clock A GET. Pulse is Clock B.

Radical product, not a kitchen sink:

- Hold an Intent in the nucleus. Watch the Cap seal crack when spent.
- Sight a star (MorphState) then walk it (GET) — two clocks, one sky.
- Commission a piece through Questionnaire + Stepper + Plans + Checkout Caps.
- Glaze chemistry is ColorPicker + named swatches, never a quantity hue.
- The kiln is Countdown (`role=timer`, remaining RefState) + Progress.
- Studio Chat is `role=log` presence, not a SPA socket toy.
- Market hall is Hero + PricingSection + LogoCloud + Testimonials + Newsletter
  as a real storefront for the foundry, not a component gallery.
- Forge is Chart + Tree + Diff + Mockup + Attachment + Feed — the workbench.
- Chrome gallery is Menubar + Toolbar + ToggleGroup + SpinButton + ThemeSwitch
  + FilterBar — APG holds, Caps off chrome.
- `/docs` is a written constitution page. FastAPI Swagger stays off.

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
9. **Root `swipe.*` on Dialog / Sheet / ActionSheet / AlertDialog / Command.**
   Swipe lives on dismiss / handle. Handle grammar:
   `click swipe.down swipe.vertical threshold:48`.
10. **A second helper world.** Official:
    `from ux_compose import act, mark_dirty, field, status, optional_plan, optional_fade, optional_slide`.
    `act()` posts `/act/{action}`. No private `_tick`. No
    `from examples._common import`.
11. **Silent `except ImportError` without `AttachNote`.**
12. **Forcing Command / Dropdown / ContextMenu / Combobox / Select / Popover /
    Tooltip / HoverCard / UserMenu / NavMenu through OverlayChrome.** Wrong
    family. House is anchored; `/overlay` is edge. AlertDialog **is** edge
    (interrupting). Command **is** edge (takes OverlayChrome ids).
13. **Invented library names** (`Page`, `when`, `forall`, `ux.div`,
    `StreamingRoute`).
14. **Grok platform Auth ON / Database ON.**
15. **Incomplete kit.** All **81** catalog stems + `components/overlay.py`
    must be live owned copies. `drawer` is the Sheet alias — still own it.
16. **Treating `kit/copy.py` or `kit/catalog.py` as a catalog stem.** The press
    is the ritual, not a card.
17. **Companion CSS per kit card.** Catalog `css: False`. Markup is Tailwind
    `className`. `uxcompose build` scans `**/*.py`.
18. **Ignoring doctor teaching residuals.** Isolation + dual-Document are hard.
    Kit-import, leftover aliases, render-chrome, docs collision expire by
    teaching — render them as chips on `/trace`.
19. **Teaching `App.mount` as the product path.** `build()` is the product door.
    Mount is the scan step inside it. `materialize(route_class=)` fails closed.
20. **Starting a tunnel before origin health is green.**
21. **Morphing the Typeahead field from a pause-fired Result.** Hits morph
    `#typeahead-hits` only.
22. **Putting email / password / OTP digits / money / remaining seconds /
    bar heights / spin values on MorphState.** RefState + `mark_dirty(self)`.
    Channel session plane refuses quantity MorphState. Rating stars are named
    keys (`one`…`five`), never `MorphState(int)`.
23. **`probe()` starting a server or shelling out.** It is import-spec only.
24. **Hiding the Created-with-Grok pill, stripping `extensions.js`, or dropping
    the vanilla preview-host bridge.**
25. **GET chrome (brand nav, `stunning-root`) inside `Component.render()`.**
    Brand is `build(wrap=brand_wrap(document, brand="APPIC"))`. Morph payloads
    stay fragments. Doctor `scan_render_chrome` will catch you.
26. **Leaving FastAPI Swagger on** so it steals `/docs`. Default `openapi` off.
    Own `routes/docs.py` as a product constitution page.
27. **Menubar / FAB removing closed submenu/menu ids from the tree.** Ids stay;
    closed state is `hidden`. Toolbar last command is `aria-current`, not
    `aria-pressed`. AlertDialog Escape/scrim do not dismiss.
28. **Choosing a PricingSection tier by binding the row.** Bind the button.
29. **`create-app site` or other reserved dest names.** Dest is `appic` / `.`.
30. **Shipping 23 stems and calling the kit done.** The library now has 81.

31. **Naming `@action` the same as a MorphState or RefState on the same class.**
    The action descriptor overwrites the state. Sight the star with MorphState
    `sight`; the verb is `look`. Host quantities are not action names.
32. **Cloning `FileStateStore` (or Memory/Redis/StateConflict/EditSlot) in the
    product tree.** Channel owns the store. Doctor `scan_store_clone` fails closed.
33. **Shipping kit rooms with the Atelier kicker on.** Product units call
    `render(shell=False)`. `apply_slots` / `kit_shell` live in
    `ux_compose.kit_construct`, not under `kit/`.
34. **Posting Clock B to `/act/{action}` and calling Channel live.** Live path
    is `POST /ux-channel/action` (`application/ux-channel+json`). `act()` is the
    progressive hatch; Channel JS intercepts `data-channel-action`.

35. **Installing ux-compose on the sandbox's Python 3.10, or running `python -m pip`
    inside the uv venv.** The venv has no pip. `uv python install 3.14` then
    `uv pip install --python /workspace/.venv/bin/python`.
36. **Inventing stretch / soft-parked kit cards** (navbar menuitem, flat tree,
    chart legend, open-mint blurbs). They are parked. 81 stems is the catalog.

---

## 1. What ux-compose actually is

Thin pure-Python **composition + delivery** root. It harnesses four specialists
and must **not** reimplement them.

| Specialist | Role | Unlock | Pin |
|---|---|---|---|
| **ux-dom** | Tag trees, Document SSoT, serialize, className, `<link>`, package static, CSP | L0 | `e8be99a` |
| **ux-behavior** | `Component`, `MorphState`, `RefState`, `@action`, Ops | L1 | `793f120` |
| **ux-channel** | Intent → Cap → Result. FileStateStore. Behind compose `wire/` only | L2 | `d0fe716` `#subdirectory=python` |
| **ux-motion** | Scene Plans, presence, Morph-then-Play | L3 | `67ff3f0` |

**Progressive Superpower:** the **same Component class** is correct at L1
(`dispatch`) and L3 (`use_channel` + `use_motion`). Zero rewrite. If you
rewrite a Component “to go live”, you have violated the contract.

`Level` is an `IntEnum`: `L0=0` `static + routing` · `L1=1` `offline interactive`
· `L2=2` `live channel` · `L3=3` `motion`. `app.level.label` is the string.

PyPI / import / CLI: `ux-compose` / `ux_compose` / **`uxcompose`**.
`ux_compose.__version__ == "0.1.0"`. Python **≥ 3.14**. Hard-deps including
`cek-host>=0.1.3` / `cek-surface>=0.1.3`. Missing specialists fail loud.

Product path:

```
uxcompose create-app myapp --level 1 --brand APPIC
cd myapp
pip install -r requirements.txt
uxcompose serve dev          # origin + ui + channel + CSS watch, 0.0.0.0:8080
uxcompose build              # Tailwind minify → /css/output.css
uxcompose serve prod         # clocks hard off
uxcompose serve restart-channel
uxcompose deploy --provider docker|fly|render|railway|vps|checklist
uxcompose doctor .
uxcompose add --list
```

`uxcompose serve` without a mode exits 2. Deploy runs raw uvicorn, not `serve`.
Tunnel (`--tunnel ngrok|cloudflare`) starts **after** origin health is green.
Aliases: `cf` / `cloudflared` / `trycloudflare`. `[serve]` extra: uvicorn,
watchfiles, httpx, starlette, websockets.

Pure-dom tooling stays on **`uxdom`** (`doctor` · `lint` · `profile` · `add`).

On this Grok sandbox, bind **uvicorn `0.0.0.0:8080`**. `startup.sh` must be
idempotent: probe `http://127.0.0.1:8080/`, start only if down, background,
return fast. Do **not** start Vite. Do **not** `npm run dev`.

Then own the kit — **every stem**:

```
STEMS="login tabs accordion dropdown dialog sheet toast command table pagination \
combobox sidebar breadcrumb stepper carousel calendar select otp plans \
actionsheet contextmenu typeahead pullrefresh drawer navbar navmenu usermenu \
popover tooltip alertdialog formlayout fieldset datepicker switch card \
emptystate stats alert banner progress skeleton hero footer cta avatar badge \
hovercard searchbar fileupload tagsinput multiselect descriptionlist featuregrid \
testimonials newsletter bottomnav separator slider menubar toolbar togglegroup \
spinbutton themeswitch filterbar chat questionnaire pricingsection logocloud \
timeline rating chart resizable tree colorpicker fab diff countdown mockup \
attachment scrollarea feed"

for s in $STEMS; do uxcompose add "$s" --force; done
# overlay is copied as a rewritten sibling by add dialog|sheet|actionsheet
# still ensure it exists:
test -f components/overlay.py || cp "$(python -c 'import ux_compose.kit.overlay as o, pathlib; print(pathlib.Path(o.__file__))')" components/overlay.py
```

Do **not** copy `kit/copy.py` or `kit/catalog.py` as widgets.
`copy_component(name, *, root=None, force=False, as_page=False)` writes
`components/{stem}.py` and optionally `routes/{stem}.py`. `find_app_root`
walks until `app.py` + `routes/`. `resolve("treeview")` aliases to `tree`.

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
act, mark_dirty, field, status,
optional_plan, optional_fade, optional_slide,
AttachNote, attach_notes,
Level, doctor, DoctorResult,
scene, fade, rise, slide,
HAS_DOM, raw, __version__,
html, head, body, title, style, meta, link, script,
div, span, h1, h2, h3, p, a, button, form, input_,
ul, li, header, footer, aside, section, article, nav, main, label,
svg, path, rect, circle,
dl, dt, dd, table, thead, tbody, tr, th, td,
fieldset, legend, hr, img, progress
```

Also use (compose submodules, never `ux_channel`):

```
ActionInfo, BuildResult, RouteRecord,
DirectoryRoutesError, HMR_PATH, attach_hmr, client_script_tag, HmrClientMiddleware,
IsolationViolation, CSS_URL_PREFIX, OUTPUT_CSS_NAME,
http_path, is_json_payload, is_stream_payload, apply_html_document,
scan_isolation, scan_kit_product_imports, scan_leftover_aliases, scan_dual_document,
scan_render_chrome, scan_fastapi_docs_collision, scan_cek_host,
prepare_deploy, DeployResult, format_deploy_result,
parse_provider, TunnelHandle, local_probe_host, wait_for_health, start_tunnel, provider_available,
find_product_root, run_product_build, ProductBuildReport, format_product_build_report,
restart_channel,
probe, ProbeResult,
note, using, format_report, current,   # attach_notes submodule
resolve_tailwind, ensure_tailwind, TailwindResolution,
ProductBatteriesRejected,
brand_wrap, GET_CHROME_ATTR, DEFAULT_BRAND
```

From owned `components/overlay.py`: `OverlayChrome`, `overlay`.

From owned `components/login.py`: `Login`, `AuthDecision`.

From `ux_compose.kit.catalog` / `kit.copy` — evidence, **not** shipped cards:

```
KitEntry, CATALOG, list_components, resolve, ALIASES
copy_component, find_app_root, KitCopyError
```

From owned `components/pagination.py`: `page_slots`.

### App / build

```
App.boot(name, *, strict_caps=False, level="auto"|0..3)
   # "auto" is Level 1. Channel attaches in build() once ASGI exists.
app.use_host("auto"|"fastapi"|"starlette"|"asgi")   # never "batteries"
app.use_dom(document=None, *, author=True)
app.use_behavior()
app.use_channel(asgi_app=...)     # Isolation door — wire/ only
app.use_motion()
app.use_cek(mode="require")        # default product Cap Host; adapt is lab-only
app.mint_cap(action, args, once=False)   # once=True where spend-once matters
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

```
from ux_compose.build import build
from ux_compose.chrome import brand_wrap
from document import document

app, asgi, bundle = build(
    PACKAGE,
    name="APPIC",
    host="auto",
    live="auto",
    level="auto",
    base="routes",
    cek="require",
    openapi=False,
    use_htmx=False,
    document=document,
    wrap=brand_wrap(document, brand="APPIC"),
)
```

Orchestra: `host.open` → L1 boot → document → Channel on asgi → discover →
`host.bind`. Payload type picks media type, not Accept.

### Author helpers (ADR 0004)

Exact signatures live in FEATURE_INVENTORY §1. Product uses them. A private
`_tick` or a second `act()` that posts a different URL is a second helper world
— forbidden.

---

## 3. Room map (constellation)

Every room is a page unit under `routes/`. Stem == class name. `render()`
returns a ux-dom tree. No HTTP verbs. Sight on the Table is MorphState.
Walk is GET.

| Path | Room | What it must make felt |
|---|---|---|
| `/` | Table | Nucleus + constellation. Hold an Intent. Sight a star. Pulse. Command `⌘K` |
| `/enter` | Door | Owned Login + OTP. `AuthDecision`. Secrets on RefState |
| `/desk` | Desk | Sidebar, Command (OverlayChrome), PullRefresh, SearchBar, UserMenu |
| `/house` | House | Anchored family: Typeahead (hits-slot), Combobox, Select, Dropdown, ContextMenu, Popover, Tooltip, HoverCard, MultiSelect, TagsInput |
| `/visit` | Visit | Stepper, Plans, Dialog, Calendar, DatePicker |
| `/signal` | Signal | Wave 1 grammar: click, swipe.*, threshold, input delay, longpress, Escape |
| `/author` | Author | Official `act` / `mark_dirty` / `field` / `status` / `optional_*` |
| `/notes` | Notes | AttachNote notebook. Silence is the defect |
| `/overlay` | Chrome-edge | OverlayChrome edge family: Dialog, Sheet, Drawer alias, ActionSheet, AlertDialog. Contrast with House |
| `/copy` | Press | `copy_component` / `find_app_root` / `KitCopyError` / `resolve("treeview")`. Not a card |
| `/skin` | Skin | WebAssets, `css_href`, ETag / Last-Modified, ThemeSwitch |
| `/deploy` | Ship | `prepare_deploy` six providers. Prepare is a Cap. GET does not write |
| `/atelier` | Presence | Presence cookbook on sort. Stable ids. `scene.share` |
| `/commission` | Commission | Questionnaire + four-step wizard + Plans + Checkout Caps |
| `/bag` | Bag | Cart, quantity stepper (SpinButton), Coupon, Checkout, Wishlist, Compare |
| `/board` | Board | Table bulk, Kanban, undo, Pagination `page_slots` |
| `/studio` | Studio | Chat `role=log`, typing presence, Feed, Attachment |
| `/lab` | Lab | Remaining atelier classes as host seams, not a second catalog |
| `/lattice` | Lattice | Caps as seals. `mint_cap(..., once=True)` on place/checkout |
| `/trace` | Trace | Doctor: hard + teaching (kit-import, leftovers, render-chrome, docs collision, CEK) |
| `/ledger` | Ledger | Book a bench. DescriptionList + Stats + Progress |
| `/clocks` | Clocks | GET vs action. Payload types |
| `/relay` | Relay | Three serve clocks. HMR path. `restart_channel`. Tunnel-after-health |
| `/health` | Health | JSON page unit (`dict` → JSON) |
| `/pulse` | Pulse | Stream page unit (generator → stream) |
| `/docs` | Constitution | Product docs page. Swagger off. Teach the collision |
| `/market` | Market | Hero, Cta, PricingSection (bind the button), LogoCloud, Testimonials, Newsletter (`list.subscribe`), FeatureGrid, Footer, Rating (named stars) |
| `/forge` | Forge | Chart (RefState heights), Tree / treeview alias, Resizable, ColorPicker, Fab (menu id stays), Diff, Countdown (timer/RefState), Mockup, ScrollArea, FileUpload (`sketch.png`) |
| `/chrome` | APG chrome | Menubar (submenu ids stay hidden), Toolbar (`aria-current`), ToggleGroup, SpinButton, FilterBar, Navbar (two trees), NavMenu, BottomNav, Separator, Badge, Avatar, Card, Alert, Banner, Skeleton, EmptyState, Switch, Slider, Accordion, Tabs |
| `/form` | Form | FormLayout (`form.submit`), Fieldset, TagsInput, MultiSelect, FileUpload, Newsletter |

Keep `/hello` if scaffold emitted it. Index (`/`) is the Table, not 404.

Command palette (`⌘K` / `Ctrl+K`) issues intents without leaving the Table.

---

## 4. Design system (non-negotiable)

Tokens in `assets/css/input.css`. First token of any CSS file is CSS.
`uxcompose build` compiles to `/css/output.css`.

```css
:root {
  --bg: #0c0d0b;
  --bg-elevated: #141511;
  --bg-subtle: #1b1c17;
  --fg: #ebe6d8;
  --fg-muted: #a39e90;
  --fg-subtle: #6f6b60;
  --accent: #c8ccd4;
  --accent-fg: #0c0d0b;
  --border: color-mix(in oklab, var(--fg) 12%, transparent);
  --radius-xs: 4px; --radius-sm: 8px; --radius-md: 12px;
  --radius-lg: 16px; --radius-xl: 24px;
  --font-display: "Fraunces", serif;
  --font-body: "Source Sans 3", system-ui, sans-serif;
  --font-mono: "IBM Plex Mono", ui-monospace, monospace;
}
```

- Concentric radii: `outer = inner + padding`.
- Pill buttons 44px min. Hairline borders. One soft shadow.
- Film grain 3.5% overlay. No emoji in chrome. No purple/gold/neon.
- `prefers-reduced-motion: reduce` — opacity only or instant.
- Motion: Morph-then-Play. Plans are selectors-only. Asymmetric open/close.
- Mobile 390px: no horizontal overflow. BottomNav is the phone landmark.
- Navbar builds **two link trees** (desktop + mobile). Do not morph one into
  the other by deleting ids.

---

## 5. Execution order (do not skip)

1. Clone ux-compose `@ bf55750b5268867aa5931a2171e69ac533808e1e`. Python ≥ 3.14 venv. `pip install -e ".[serve]"`
   plus specialist pins from `pyproject.toml`. Fail loud if import of ux-dom /
   ux-behavior / ux-motion / channel-behind-wire fails.
2. Product path: `document.py` (one Document; `.use(XElement, Csp.auto(), Channel.optional)`
   via `ux_dom.runtime` Channel alias — not `ux_channel.Channel`), `settings.py`
   (`WebAssets`), `app.py` (`build(...)` as above), `routes/`.
3. `uxcompose add` **all 81 stems**. Confirm `components/overlay.py` exists.
4. Write every room in the map. Host-seam the 72 unique Atelier classes — do not
   `from examples import` as the live card; copy the law into owned units.
5. `brand_wrap` on `build(wrap=)`. Zero brand markup in `routes/*.py` `render()`.
6. JSON `/health`, stream `/pulse`, HTML everywhere else.
7. Caps on protected verbs: `auth.login` `auth.signup` `auth.otp` `auth.logout`
   `orders.place` `orders.confirm` `stepper.finish` `form.submit` `list.subscribe`
   `admin.reset`. `mint_cap(..., once=True)` on checkout/place.
8. `uxcompose build` then serve uvicorn `0.0.0.0:8080`. `startup.sh` idempotent.
9. `uxcompose doctor .` — hard must pass. Teaching residuals become `/trace` chips.
10. Preview-host bridge: vanilla `postMessage` listener near `<body>` top if the
    Vite injector is absent. Do not hide the Grok pill. Do not add a CSP that
    blocks `https://grok.com`.
11. Push the foundry + this prompt + FEATURE_INVENTORY to **bitplorer/appic**.

---

## 6. Completeness checklist (not done until every box)

- [ ] Python 3.14, specialists imported, `HAS_DOM` true, `Level` L3 available
- [ ] `build(cek="require", openapi=False, use_htmx=False, wrap=brand_wrap(...))`
- [ ] Every `__all__` name appears in product source (including `dl/dt/dd`,
      `table/thead/tbody/tr/th/td`, `fieldset/legend`, `hr/img/progress`)
- [ ] All **81** kit stems owned under `components/` + OverlayChrome
- [ ] `resolve("treeview")` evidence on `/copy`
- [ ] Edge family vs anchored family vs interrupting AlertDialog — three rooms
- [ ] Typeahead hits-slot law demonstrated
- [ ] Login/OTP secrets on RefState; `AuthDecision` felt
- [ ] Wave 1 grammar felt on `/signal` (every token in the table)
- [ ] `mark_dirty` / `optional_plan` / `optional_fade` / `optional_slide` / `act`
- [ ] Attach notes refuse silence
- [ ] Doctor hard + teaching rendered
- [ ] JSON + stream + HTML payload doors
- [ ] Presence: stable ids, stagger on survivors, `scene.share`
- [ ] WebAssets ETag / Last-Modified
- [ ] `prepare_deploy` six providers
- [ ] HMR path named; tunnel-after-health taught
- [ ] `probe()` import-spec only
- [ ] `/docs` is a product page
- [ ] Menubar submenu ids stay; FAB menu id stays; toolbar `aria-current`
- [ ] PricingSection binds the button; Rating uses named stars
- [ ] Countdown is `role=timer` + RefState; SpinButton is not a timer
- [ ] Chart heights RefState; Tree is APG treeview
- [ ] 72 unique Atelier classes have a host seam
- [ ] No React / Vue / JSX / Vite as source of truth
- [ ] Running on `0.0.0.0:8080`, verified in a real browser, clean console
- [ ] Mobile 390px usable; 44px targets; no horizontal overflow
- [ ] Pushed to bitplorer/appic

A visitor can walk the constellation, hold an intent, spend a seal, morph a
presence, feel a swipe, own a card, and read the constitution — without a
single React component.
