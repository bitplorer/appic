# Grok Build prompt — APPIC on ux-compose 0.1.0 (`060b583`)

Pin: [bitplorer/ux-compose](https://github.com/bitplorer/ux-compose) `@ main`
SHA **`060b583f64512302059bd9d4ff691bb6a2f4dd3a`** (2026-09-09, FileStateStore + kit slots).
Companion: [FEATURE_INVENTORY.md](FEATURE_INVENTORY.md).
If this prompt and the library disagree, **the library wins**.

This file is the **metaprompt**. Publish it on **bitplorer/appic**. The executing
Grok Build agent copies **everything below the line**, clones the library first,
and ships a complete foundry. Repo **appic already exists** — upgrade it; do not
create a second repo.

## 2026-09-10 — independent re-read

Re-walked `src/ux_compose/**/*.py` on **`060b583`**. Breaking cut vs the
2026-09-09 kit-81 pin (`5bb7dc22`):

| Was (`5bb7dc22`) | Now (`060b583`) |
|---|---|
| Channel pin `31a60bd` | Channel pin **`d0fe716`** (`FileStateStore`) |
| Compose SHA `5bb7dc22` / scaffold `6d61c9e` | Compose **`060b583`**. Scaffold VCS pin may lag — **code wins** |
| Kit `render()` always Atelier chrome | **Kit Cut 1:** `render(*, shell=None, **slots)` + `apply_slots` / `kit_shell`. `shell=False` drops kicker/title/lede |
| serve-dev pickled MorphState into a cwd file | Channel owns **FileStateStore** (JSON sqlite). `serve_state.py` is lifecycle only. Doctor **`scan_store_clone`** fails closed if a store class reappears in compose |
| Kit APG residuals in flight | Menubar/FAB closed menu ids stay in the tree (`hidden`). Toolbar `aria-current`. Filterbar radios rove `tabindex`. Resizable chips are `role=radio` |

Public `__all__` still exports `App`, `build`, `WebAssets`, `DirectoryRoutes`,
`DirectoryASGI`, `RouterHooks`, `Surface*`, `mount_surfaces` / `scan_surfaces` /
`validate_surfaces`, `Component`, `MorphState`, `RefState`, `action`, `bind`,
`control`, `notify`, `update_with`, `morph_play`, `act`, `mark_dirty`, `field`,
`status`, `optional_plan`, `optional_fade`, `optional_slide`, `AttachNote`,
`attach_notes`, `Level`, `doctor`, `DoctorResult`, `scene`, `fade`, `rise`,
`slide`, `HAS_DOM`, tag constructors including `dl dt dd table thead tbody tr th td fieldset legend hr img progress`.
`tick` / `maybe_*` are **not** public. OverlayChrome is still not a catalog stem.
CLI: `create-app` · `serve {dev,prod,restart-channel}` · `build` · `deploy` ·
`doctor` · `add`. Specialist pins: ux-dom `e8be99a`, ux-behavior `793f120`,
ux-channel `d0fe716`, ux-motion `67ff3f0`, cek-host/cek-surface `>=0.1.3`.
Python **≥ 3.14**.

---

Copy **everything below this line** into Grok Build. You **are** Grok Build.
Execute it. Do not stop at a README. Ship a running foundry on `0.0.0.0:8080`.

---

# APPIC — a constitution you can walk (060b583)

Build **APPIC** as a **complete product** (not a widget zoo) using
**https://github.com/bitplorer/ux-compose @ main**
(`060b583f64512302059bd9d4ff691bb6a2f4dd3a`, **0.1.0**) as the **only** web UI
framework.

Fully utilise **every public name** in `ux_compose.__all__`, every Clock A
payload door (HTML / JSON / stream), every ownable kit card (`uxcompose add` —
**all 81 stems** plus owned `overlay.py` and the Drawer alias), OverlayChrome,
`brand_wrap` / custom GET wrap with `GET_CHROME_ATTR`, kit **render slots**
(`shell=False`, `apply_slots`, `kit_shell`), FileStateStore law (do not clone
Channel's store), every doctor scan family including `scan_store_clone`, the
Presence cookbook, WebAssets, `prepare_deploy` (six providers), tunnel grammar,
HMR delivery, attach-note notebooks, Tailwind resolver, `morph_play` hop,
`AuthDecision` verdict, Typeahead hits-slot, APG holds, and the Atelier
Component classes in `examples/`.

**No React. No Vue. No JS/TS/TSX as source of truth.** Server-authored
hypermedia. Python + ux-compose. Serve uvicorn on `0.0.0.0:8080`.

Repo: **bitplorer/appic**. Create only if missing. Consume the running foundry.

Grok sandbox: Auth OFF. Database OFF. Do **not** scaffold TanStack Start /
React / Vite / Nitro as the product UI. Direct user law beats the sandbox's
React default. Keep the Grok preview bridge (vanilla) and `extensions.js`.
Never hide the Created-with-Grok pill.

A visitor should feel: *this house has laws, and I can touch every room.*

## NORTH STAR

APPIC is a private nocturnal foundry for commissioning and collecting handmade
objects. Authority, motion, media type, kit ownership, copy ritual, gesture
grammar, author door, attach notes, overlay vs anchored, interrupting alerts,
doctor residuals, presence, skin, ship, HMR, tunnel, kit slots, FileStateStore,
and the 81-stem house are first-class rooms a human can walk.

Editorial. Expensive. Abundant negative space. Concentric radii. One cool
accent (`#c8ccd4` on ink `#0c0d0b`). Bone type `#ebe6d8`. Fraunces + Source
Sans 3 + IBM Plex Mono. No purple, gold, neon, gradient-blob slop. No emoji
in chrome. Film grain at 3.5% overlay. Pill buttons 44px. Hairline borders.
Soft single shadow. `prefers-reduced-motion`.

## KILL TRIGGERS

1. Any product UI in React / Vue / Svelte / Solid / Next / TanStack / JSX / TSX.
2. `vite` / `npx vite` / Nitro as the **product** ship gate. Preview is uvicorn on `0.0.0.0:8080`.
3. HTMX as architecture. `use_htmx=False`.
4. HTTP verbs on page units. Clock A wraps `render()`.
5. `from ux_compose.kit import Login` as the live unit. Copy via `uxcompose add`.
6. `import ux_channel` / `cek` / `cek_host` in product modules.
7. `host="batteries"`. Use `host="auto"`.
8. Plans with `html=`. XOR. Morph first, then `transition.play`.
9. Root `swipe.*` on OverlayChrome family. Swipe lives on dismiss / handle.
10. A second helper world. Official: `act`, `mark_dirty`, `field`, `status`, `optional_*`.
11. Silent `except ImportError` without `AttachNote`.
12. Forcing Command / Dropdown / Popover / Tooltip / HoverCard through OverlayChrome. Wrong family. AlertDialog **is** edge.
13. Invented library names (`Page`, `when`, `forall`, `ux.div`).
14. Grok platform Auth ON / Database ON.
15. Incomplete kit. All **81** catalog stems + `components/overlay.py`. Own `drawer`.
16. Treating `kit/copy.py` or `kit/catalog.py` as a catalog stem.
17. Companion CSS per kit card. Catalog `css: False`.
18. Ignoring doctor teaching residuals. Isolation is hard. `scan_store_clone` is hard.
19. Teaching `App.mount` as the product path. `build()` is the product door.
20. Morphing the Typeahead field from a pause-fired Result. Hits morph `#typeahead-hits` only.
21. Quantity / secrets / remaining seconds / bar heights on MorphState. Use RefState + `mark_dirty`. Rating stars are named keys.
22. GET chrome inside `Component.render()`. Brand is `wrap=` with `GET_CHROME_ATTR`.
23. Leaving FastAPI Swagger on so it steals `/docs`.
24. Menubar / FAB removing closed submenu ids from the tree.
25. Reimplementing Channel's FileStateStore in compose or the app.
26. Calling kit `render()` without offering `shell=False` in product rooms (Atelier kicker is demo chrome).
27. Hiding the Created-with-Grok pill.

## PRODUCT PATH

```bash
python3.14 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt   # pins compose @ 060b583 + specialists
uxcompose create-app . --name APPIC --level 1 --host auto   # dest must not be reserved (no `site`)
# then author routes/, own components/ via uxcompose add, wrap= GET chrome
uxcompose serve dev --host 0.0.0.0 --port 8080
```

Composition root:

```python
from ux_compose.build import build
from chrome import foundry_wrap
from document import document

app, asgi, bundle = build(
    PACKAGE,
    name="APPIC",
    host="auto",
    live="auto",
    level="auto",
    document=document,
    wrap=foundry_wrap(document, brand="APPIC"),
    cek="require",
    openapi=False,
    use_htmx=False,
)
```

Document: `Document.use(XElement(), Csp…, Channel.optional())`. Isolation: Channel is the **ux_dom.runtime** alias.

Own every catalog stem:

```bash
uxcompose add --list
uxcompose add login --force
# … all 81, including drawer (Sheet alias) and overlay sibling
```

Then `app.add` the owned classes (subclass Drawer with `id = "drawer"` so both edges exist). Product rooms call `inst.render(shell=False, **slots)`.

## ROOMS (must all exist and work)

`/` Table constellation · `/enter` Door · `/house` 81-stem wings · `/atelier` market · `/commission` stepper+plans+Cap · `/bag` cart · `/forge` glaze/kiln/chart/tree · `/studio` chat+feed · `/chrome` APG · `/overlay` two families · `/lab` Caps + `/pulse.json` + `/stream` · `/author` act/field/status/optional_* · `/docs` constitution · `/trace` doctor · `/notes` AttachNote · `/skin` WebAssets+ThemeSwitch · `/ship` prepare_deploy ×6 · `/signal` swipe grammar · `/copy` add ritual · `/clocks` Clock A vs B · `/hello` live-safe RefState counter.

## VERIFY BEFORE YOU STOP

- `GET /` returns HTML with visible APPIC chrome and constellation.
- `GET /healthz` JSON includes `level` ≥ 1 and kit count.
- Click Hold intent → morphs to "Intent held" without remounting the page.
- `/house` Door wing shows owned Login + OTP with `shell=False`.
- `/docs` is the constitution, not Swagger.
- No React/TSX in product UI.
- Push the running tree to **bitplorer/appic**.
