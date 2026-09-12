# Grok Build prompt — APPIC on ux-compose 0.1.0 (kit-81 + Kit Cut 1 + Cut C)

Pin: [bitplorer/ux-compose](https://github.com/bitplorer/ux-compose) `@ main`
SHA **`7546013bad9847b8ce3a1ad2aa3019c656e9c1d4`** (2026-09-12 channel Cut C +
Redis precedence + frozen serve verbs + Channel.boot).
Companion: [FEATURE_INVENTORY.md](FEATURE_INVENTORY.md).
If this prompt and the library disagree, **the library wins**.

This file is the **metaprompt**. Publish it on **bitplorer/appic**. The executing
Grok Build agent copies **everything below the line**, clones the library first,
and ships a complete foundry. Repo **appic already exists** — upgrade it; do not
create a second repo.

## 2026-09-12 — Grok Build independent re-read (this session)

Walked `src/ux_compose/**/*.py`, `kit/catalog.py` (**81** stems + `treeview`
alias counted from source), `__init__.__all__`, `docs/ARCHITECTURE.md`,
`docs/OWNERSHIP.md`, `AGENTS.md`, `CHANGELOG.md` Unreleased (Cut C / Cut 3–4 /
channel #27), `examples/README.md`, and the four product apps (`atelier_shop`,
`atelier_studio`, `nook`, `pulse`).

**Library floor this session**

| Pin | SHA |
| --- | --- |
| ux-compose | `7546013bad9847b8ce3a1ad2aa3019c656e9c1d4` |
| ux-dom | `e8be99a52bfecd6026c200fa1c3dc6a74f87aacb` |
| ux-behavior | `793f120e3b1388925772cd069b070d7918b78baa` |
| ux-motion | `67ff3f0c4912b70b7056f8226a6f226b6fe93f60` |
| ux-channel | `985e58aee76ca683774c4d4d58ab30a1d3b6efee` `#subdirectory=python` |
| cek-host / cek-surface | `>=0.1.3` |

Python **≥ 3.14**. Install: `git clone` + `pip install -e ".[serve]"` — **not PyPI**.

### Honesty locks that landed after `bf55750` (do not reopen)

1. **CUT-C** — Empty `Content-Type` on HTTP `/ux-channel/action` is `bad_request`.
   Compose never POSTs without a declared type. Live Clock B is
   `POST /ux-channel/action` (`application/ux-channel+json`).
2. **CAP-DOOR** — Cap door is **`Channel.boot`**. Not `ActionRegistry.from_config`.
   `attach_cek` still calls `apply_host_adapter`. wire/ frozen imports:
   `Channel`, `ChannelConfig`, `apply_host_adapter`, `Intent`.
3. **REDIS-1** — Channel prefers `REDIS_URL`. Doctor `scan_store_precedence`
   fails closed if both store envs remain. Do not export both.
4. **SERVE-ARGV** — Frozen verbs: `dev` / `prod` / `restart-channel`. argv
   `development` / `production` / `restart_channel` fail closed.
5. **CLI-ARGV** — `cli.py` is argv only. `serve_dev.py` starts CSS `--watch`
   + tunnel. Leftover `start_css_watcher=` is gone.
6. **HEALTH-FMT** — Channel `/ux-channel/health` `formats` (HTTP) vs `codecs`
   (library). Clock A `/health` is still `dict` JSON.
7. **ENCYCLOPEDIA** — No `FEATURES.md` / `ONTOLOGY.md`. ARCHITECTURE + OWNERSHIP.
8. **FRAGMENT** — `_fragment_for_target` stays in `helpers.py`. No `fragment.py`.
9. **VCS-PIN** — Scaffold `COMPOSE_VCS_PIN` tracks main tip.

Prior 2026-09-11 locks still hold: `LOCK-1` public `__all__`, `ISO-2` cold
import, `KIT-1` Command is not OverlayChrome, `HMR-shell`, `CSS-spawn`,
`SWALLOW-1` / `SWALLOW-boot`, `SURF-1` two walkers one door, FileStateStore
on Channel, folder law, `LEFTOVER-split`, `PYPI-1`, `DOOR-2` `create-app`,
`openapi=False`, Kit Cut 1 `shell=False`.

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
anyway because Dialog/Sheet/ActionSheet/AlertDialog import it.

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
(`POST /ux-channel/action`, `application/ux-channel+json`). Empty Content-Type
is `bad_request`. Payload type picks media type — HTML daylight, JSON pulse,
generator stream. Kit cards are rooms you own (`shell=False`). Copy press is
the ownership ritual. OverlayChrome is the edge primitive. Anchored popovers
are a different family. AlertDialog is interrupting — Escape does not dismiss
it. `/docs` is a product page. Typeahead morphs the hits slot, never the field
being typed. Channel.boot is the hinge. Redis wins.

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

# APPIC — a constitution you can walk (kit-81 + Cut C)

Build **APPIC** as a **complete product** (not a widget zoo) using
**https://github.com/bitplorer/ux-compose @ main**
(`7546013bad9847b8ce3a1ad2aa3019c656e9c1d4`, **0.1.0**) as the **only** web UI
framework.

Fully utilise **every public name** in `ux_compose.__all__`, every Clock A
payload door, every ownable kit card (`uxcompose add` — **all 81 stems**),
OverlayChrome (copied even though it is not a catalog stem), `brand_wrap`,
the copy helper, every Wave 1 Signal token, every doctor scan family
(hard: isolation, dual-Document, store-clone, **store-precedence**; teaching:
kit-import, leftovers, render-chrome, FastAPI docs collision, CEK host),
the Presence cookbook, WebAssets, `prepare_deploy` (six providers), tunnel
grammar, HMR delivery, attach-note notebooks, Tailwind resolver, probe matrix,
`morph_play` hop, `AuthDecision` verdict, Typeahead hits-slot, APG holds,
Channel Cut C (declared Content-Type), Channel.boot as Cap door, Redis
precedence, frozen serve verbs, and every unique Atelier Component class.

> **The document is the composition root made visible. Caps are wax seals
> that break when spent. Intent is a nucleus you can hold. Ops are traces
> on a ribbon. Routes are a constellation. Skin is WebAssets. GET is Clock A.
> Action is Clock B. Empty Content-Type is bad_request. Payload type picks
> media type — HTML is daylight, JSON is a pulse, a generator is a stream of
> light. Kit cards are rooms you own. The copy press is the ownership ritual.
> Signal is a grammar in the hand. The author door is one. Attach notes
> refuse silence. OverlayChrome is the edge primitive. Anchored popovers are
> a different family. AlertDialog is interrupting — Escape does not dismiss
> it. Doctor residuals expire by teaching. Presence is continuous — objects
> that stay do not remount. HMR is delivery, not a Document API. Tunnel
> starts after health is green. Probe never shells. Login secrets never sit
> on MorphState. Typeahead morphs the hits slot, never the field being typed.
> Brand lives on wrap=, never inside render(). `/docs` is a product page, not
> Swagger. Quantity is RefState. Named things are MorphState. Channel.boot
> is the hinge. Redis wins. 81 stems, one house.**

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
hits-slot law, GET brand chrome, product `/docs`, APG chrome, marketing bands,
glaze chemistry, kiln time, Channel Cut C, Channel.boot, Redis precedence,
frozen serve verbs, and the 81-stem kit house** are first-class rooms a human
can walk.

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
- Market hall is Hero + PricingSection + LogoCloud + Testimonials + Newsletter.
- Forge is Chart + Tree + Diff + Mockup + Attachment + Feed.
- `/cut` is Channel Cut C. A type is a seal. Empty Content-Type is `bad_request`.
- `/boot` is Channel.boot. Redis wins. `scan_store_precedence` is on `/trace`.
- `/docs` is a written constitution. FastAPI Swagger stays off.

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
8. **Plans with `html=`.** XOR. Morph first from `render()`, then
   `transition.play`.
9. **Root `swipe.*` on Dialog / Sheet / ActionSheet / AlertDialog / Command.**
10. **A second helper world.** Official:
    `from ux_compose import act, mark_dirty, field, status, optional_plan, optional_fade, optional_slide`.
11. **Silent `except ImportError` without `AttachNote`.**
12. **Forcing Command / Dropdown / ContextMenu / Combobox / Select / Popover /
    Tooltip / HoverCard / UserMenu / NavMenu through OverlayChrome.** Wrong
    family. Command uses local `{id}-scrim` / `{id}-panel` / `{id}-dismiss`.
13. **Invented library names** (`Page`, `when`, `forall`, `ux.div`,
    `StreamingRoute`, `FEATURES.md`).
14. **Grok platform Auth ON / Database ON.**
15. **Incomplete kit.** All **81** catalog stems + `components/overlay.py`.
16. **Treating `kit/copy.py` or `kit/catalog.py` as a catalog stem.**
17. **Companion CSS per kit card.** Catalog `css: False`.
18. **Ignoring doctor teaching residuals.**
19. **Teaching `App.mount` as the product path.** `build()` is the product door.
20. **Starting a tunnel before origin health is green.**
21. **Morphing the Typeahead field from a pause-fired Result.**
22. **Putting email / password / OTP digits / money / remaining seconds /
    bar heights / spin values on MorphState.**
23. **`probe()` starting a server or shelling out.**
24. **Hiding the Created-with-Grok pill.**
25. **GET chrome inside `Component.render()`.**
26. **Leaving FastAPI Swagger on.**
27. **Menubar / FAB removing closed submenu/menu ids from the tree.**
28. **Choosing a PricingSection tier by binding the row.** Bind the button.
29. **`create-app site` or other reserved dest names.**
30. **Shipping 23 stems and calling the kit done.**
31. **Naming `@action` the same as a MorphState or RefState on the same class.**
32. **Cloning `FileStateStore` in the product tree.**
33. **Shipping kit rooms with the Atelier kicker on.** `render(shell=False)`.
34. **Posting Clock B to `/act/{action}` and calling Channel live.** Live path
    is `POST /ux-channel/action`.
35. **Installing ux-compose on the sandbox's Python 3.10, or running `python -m pip`
    inside the uv venv.**
36. **Inventing stretch / soft-parked kit cards.**
37. **POST without a declared Content-Type.** Cut C: that is `bad_request`.
38. **Exporting both `UXCOMPOSE_STATE_STORE` and `REDIS_URL`.** Redis wins.
    `scan_store_precedence` fails closed.
39. **Calling `ActionRegistry.from_config` the Cap door.** The door is
    `Channel.boot`.
40. **Serve argv `development` / `production` / `restart_channel`.** Frozen:
    `dev` / `prod` / `restart-channel`.
41. **Adding `start_css_watcher=` back onto `serve_dev.run`.**
42. **Adding `cli/` / `serve/` / `services/` packages, or `fragment.py`.**

---

## 1. What ux-compose actually is

Thin pure-Python **composition + delivery** root. It harnesses four specialists
and must **not** reimplement them.

| Specialist | Role | Unlock | Pin |
|---|---|---|---|
| **ux-dom** | Tag trees, Document SSoT, serialize, className, `<link>`, package static, CSP | L0 | `e8be99a` |
| **ux-behavior** | `Component`, `MorphState`, `RefState`, `@action`, Ops | L1 | `793f120` |
| **ux-channel** | Intent → Cap → Result. FileStateStore. Behind compose `wire/` only | L2 | `985e58a` `#subdirectory=python` |
| **ux-motion** | Scene Plans, presence, Morph-then-Play | L3 | `67ff3f0` |

| Layer | Name |
|---|---|
| Install | git clone + `pip install -e ".[serve]"` (not on PyPI) |
| Import | `ux_compose` |
| CLI | **`uxcompose`** (sole product lifecycle) |
| Version | `0.1.0` |
| Python | ≥ 3.14 |

**Progressive Superpower:** complete install first. Levels are additive —
Level 1 page units stay correct at L2/L3. Zero rewrite.

Product path:

```
uxcompose create-app appic --level 3 --brand APPIC
# then own the kit: uxcompose add {all 81 stems}
# composition root is build()
uvicorn app:asgi --host 0.0.0.0 --port 8080
```

Grok sandbox:

```
uv python install 3.14
uv venv .venv --python 3.14
uv pip install --python .venv/bin/python -r requirements.txt
```

---

## 2. Product rooms that must exist

| Room | Path | Law you can touch |
|---|---|---|
| Table | `/` | Constellation. Sight a star, then walk it |
| Door | `/enter` `/login` `/otp` | Secrets on RefState. Caps on the hinge |
| House | `/house` | Anchored family. Hits-slot law |
| Make | `/commission` | Clay / glaze / fire. `orders.place` |
| Hall | `/market` | Hero, pricing (bind the button), newsletter |
| Forge | `/forge` | Chart, tree, diff, mockup |
| Edge | `/overlay` | OverlayChrome vs anchored family |
| Cut | `/cut` | Cut C. Declared type. Empty type is `bad_request` |
| Boot | `/boot` | Channel.boot. Redis wins. FileStateStore is Channel's |
| Law | `/docs` | Written constitution. Swagger off |
| Trace | `/trace` | Doctor: hard vs teaching vs store-clone vs **precedence** |
| Press | `/copy` | `copy_component`. Not a card |
| Ship | `/deploy` | `prepare_deploy` six providers |
| Health | `/health` | dict → JSON |
| Pulse | `/pulse` | generator → stream |
| Clocks | `/clocks` | Frozen serve verbs. Two clocks, one sky |

Every kit stem is also a room (`/dialog`, `/typeahead`, `/menubar`, …).
81 catalog stems + OverlayChrome.

---

## 3. Build order

1. Clone ux-compose @ `7546013`. Read `__all__`, `kit/catalog.py`, `AGENTS.md`,
   `docs/OWNERSHIP.md`, `CHANGELOG.md` Unreleased. Inventory every public name.
2. `uv python install 3.14`. Venv. `uv pip install -r requirements.txt` with
   the pins in this file.
3. Product path is `build()` + `routes/` page units. Brand on `wrap=`.
   `cek="require"`. `openapi=False`. `use_htmx=False`. `host="auto"`.
4. Own all 81 stems via `uxcompose add`. Subclass with `render(shell=False)`.
5. Compose a constellation Table. Sight is MorphState. Walk is GET. The verb
   is `look`.
6. Add `/cut` (Cut C) and `/boot` (Channel.boot + Redis) as walkable rooms.
   Put `scan_store_precedence` on `/trace`.
7. CSP includes `https://grok.com`. Keep `extensions.js` and the preview-host
   bridge. Never hide the Grok pill.
8. Serve uvicorn `0.0.0.0:8080`. `startup.sh` probes, starts only if down,
   backgrounds, returns fast.
9. Publish to **bitplorer/appic**. Upgrade in place.

If the prompt and the library disagree, **the library wins**.
