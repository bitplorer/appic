# Grok Build prompt — APPIC on ux-compose 0.1.0 (kit-81 + Kit Cut 1 + Cut C + skin law + extract-by-id)

Pin: [bitplorer/ux-compose](https://github.com/bitplorer/ux-compose) `@ main`
SHA **`80563abf1666e45fa43236e7303b1c4319413554`** (2026-09-13 tip — specialist lockstep
ux-dom `2e894cd` · ux-channel `a6ab159` · ux-behavior `7d46979` · ux-motion `bbe7d73`).
Companion: [FEATURE_INVENTORY.md](FEATURE_INVENTORY.md).
If this prompt and the library disagree, **the library wins**.

This file is the **metaprompt**. Publish it on **bitplorer/appic**. The executing
Grok Build agent copies **everything below the line**, clones the library first,
and ships a complete, **visually stunning** foundry. Repo **appic already exists**
— upgrade it in place; do not create a second repo.

---

## 2026-09-14 — devised + executed (this session)

Independent re-read of [bitplorer/ux-compose](https://github.com/bitplorer/ux-compose)
`main` @ **`80563ab`**. Walked `__all__` (86 public names), `kit/catalog.py`
(**81 stems** + `treeview` alias), `AGENTS.md`, `docs/OWNERSHIP.md`,
`docs/ARCHITECTURE.md`, `docs/guides/{PATH,HOST,UI,SNIPPETS,TAILWIND}.md`,
`CHANGELOG` Unreleased, `pyproject.toml`, `doctor.py`, `helpers._fragment_for_target`,
`scaffold.COMPOSE_VCS_PIN`, Apple Liquid Glass 2026 (WWDC25 / iOS 26 / macOS Tahoe:
Clarity, Deference, Depth, concentricity, 90° specular, Regular vs Clear glass),
Linear luminance, Raycast Command-as-OS, Stripe editorial type, visionOS layering.

Specialist pins **unchanged** from `4978576`. Compose tip moved for:

| Delta | Law |
| --- | --- |
| Soft USE `extract_by_id` | `helpers._fragment_for_target` prefers `ux_dom.response.serialize.extract_by_id`. Homemade walker KEEP as escape. No `fragment.py`. **EXTRACT-1** |
| L5 Pulse httpx locks | Existing Pulse rooms only. No new Pulse room. No MATRIX.md teaching surface. **PULSE-L5** |
| Scaffold `COMPOSE_VCS_PIN` | Still `24a182f` (chicken-egg #56). Product `requirements.txt` pins **tip `80563ab`**, not the lagging scaffold pin. **VCS-PIN-TIP** |

Visual law tightened to 2026 Liquid Glass craft: glass is a *control-layer
material* (Regular glass on chrome / overlays; never Clear glass on content
cards). Specular highlight arrives from **90°** (top inset 1px + inner wash),
not 45°. Nested radii = parent radius − padding (concentricity). HDR-like
jewel controls: brass nucleus is the only light source in the sky.

**Executed:** pin `80563ab`, restyle glass specular, constellation filaments,
⌘K command chip, constitution law for extract-by-id, doctor green, uvicorn
`0.0.0.0:8080`, published to **bitplorer/appic**.

### Honesty locks (do not reopen)

All prior locks hold: `CUT-C`, `CAP-DOOR` (`Channel.boot`), `REDIS-1`,
`SERVE-ARGV`, `CLI-ARGV`, `HEALTH-FMT`, `ENCYCLOPEDIA`, `FRAGMENT` (walker
escape KEEP), `LOCK-1`, `ISO-2`, `KIT-1`, `HMR-shell`, `CSS-spawn`,
`SWALLOW-1` / `SWALLOW-boot`, `SURF-1`, FileStateStore on Channel, folder
law, `LEFTOVER-split`, `PYPI-1`, `DOOR-2`, `openapi=False`, Kit Cut 1
`shell=False`, `CEK-HARD`, `SKIN-1`, `GLASS-1`, `VISUAL-QA`.

**New this session**

1. **PIN-80563ab** — Compose tip. Specialists lockstep as `pyproject.toml`.
2. **EXTRACT-1** — Prefer owner `extract_by_id`. Do not invent `fragment.py`.
3. **PULSE-L5** — No new Pulse room. Locks land on existing rooms.
4. **VCS-PIN-TIP** — Product pin is git tip, not lagging `COMPOSE_VCS_PIN`.
5. **SPECULAR-90** — Glass highlight from the top, not a 45° slash.
6. **CONCENTRICITY-1** — Nested radius = parent radius − padding. Always.
7. **GLASS-REGULAR** — Regular glass (adapts, stays legible) on chrome.
   Clear glass (permanently transparent) is forbidden on content rooms.

### Author surface (do not invent names)

From `ux_compose.__all__` (86):

`App`, `build`, `WebAssets`, `DirectoryRoutes`, `DirectoryASGI`, `RouterHooks`,
`Surface`, `SurfaceBundle`, `SurfaceError`, `mount_surfaces`, `scan_surfaces`,
`validate_surfaces`, `Component`, `MorphState`, `RefState`, `action`, `bind`,
`control`, `notify`, `update_with`, `morph_play`, `act`, `mark_dirty`, `field`,
`status`, `optional_plan`, `optional_fade`, `optional_slide`, `AttachNote`,
`attach_notes`, `Level`, `doctor`, `DoctorResult`, `scene`, `fade`, `rise`,
`slide`, `HAS_DOM`, DOM tags (`raw` … `progress` including `dl/dt/dd`,
`table/thead/tbody/tr/th/td`, `fieldset/legend`, `hr/img/progress`), `__version__`.

Chrome (submodule, not `__all__`): `from ux_compose.chrome import brand_wrap,
GET_CHROME_ATTR, DEFAULT_BRAND`. Brand lives on `wrap=`, never inside `render()`.

Kit is **not** a public import path. Own a copy: `uxcompose add {stem}`.
Copy `overlay.py` anyway. `drawer` is a Sheet alias. `treeview` → `tree`.

`line` is **not** a public tag. Constellation filaments use `svg` + `path`.

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

### Encoding law (Channel session plane)

| Kind | Plane |
| --- | --- |
| Open / value / query / named step / named band / theme | MorphState |
| Magnitude, lists, money, ISO dates, files, digits, remaining | RefState + `dirty = MorphState("idle")` |
| One-shot message | `notify(...)` |
| Domain stock | Host DB (`store.HOST`), never the client plane |
| Protected verb | `@action(caps=("orders.place",))` + live submit_intent |

The verb that sights a star is `look` — never a same-named action as the
MorphState field, or the field is overwritten.

XOR: morph HTML from `render()` first, then `transition.play`. Never `html=`
on a plan. Presence continuity: objects that stay do not remount.

---

Copy **everything below this line** into Grok Build. You **are** Grok Build.
Execute it. Do not stop at a README. Ship a running, **visually stunning**
foundry on `0.0.0.0:8080`. Then publish the source to **bitplorer/appic**.

---

# APPIC — a nocturnal foundry you can inhabit

Build **APPIC** as a **complete, premium product** (not a widget zoo, not a
docs site, not a kit gallery) using
**https://github.com/bitplorer/ux-compose @ main**
(`80563abf1666e45fa43236e7303b1c4319413554`, **0.1.0**) as the **only** web UI
framework.

Fully utilise **every public name** in `ux_compose.__all__`, every Clock A
payload door (HTML tree / `dict` JSON / generator stream), every ownable kit
card (`uxcompose add` — **all 81 stems** + OverlayChrome), `brand_wrap`, the
copy helper, Wave 1 Signal tokens, every doctor scan family (hard: isolation,
dual-Document, store-clone, store-precedence, **cek-host**; teaching: kit-import,
leftovers, render-chrome, FastAPI docs collision), Presence cookbook, WebAssets,
`prepare_deploy` (six providers), tunnel grammar, HMR delivery, attach-note
notebooks, Tailwind resolver, probe matrix, `morph_play` hop, `AuthDecision`
verdict, Typeahead hits-slot, APG holds, Channel Cut C, Channel.boot, Redis
precedence, frozen serve verbs, Kit Cut 1 `shell=False`, owner
`extract_by_id` (Soft USE), and the APPIC **skin**.

**No React. No Vue. No Svelte. No Solid. No Next. No TanStack Start.
No JSX / TSX / `.tsx` / `.jsx`. No client TypeScript as source of truth.**
Server-authored hypermedia. Python + ux-compose. `use_htmx=False`.
Serve `uvicorn app:asgi --host 0.0.0.0 --port 8080`.

Repo: **bitplorer/appic**. It already exists — upgrade it. Create only if
missing. Direct user law beats the sandbox React default.

A visitor should feel: *this is a private atelier OS — expensive, spatial,
keyboard-first — and every law of the stack is a room I can touch.*

---

## 1. NORTH STAR

APPIC is a **private nocturnal foundry** for commissioning handmade objects
(clay, glaze, fire) and collecting them. It is an operating surface, not a
brochure.

Craft references (steal structure, not trademarks):

- **Apple Liquid Glass 2026** (iOS 26 / macOS Tahoe / visionOS 26) — glass is a
  *material for the control layer*, not a wallpaper. Clarity, Deference, Depth.
  Concentric radii matching hardware bezels. Controls float above content and
  give way to it. Specular from **90°** (top). Regular glass adapts for
  legibility; Clear glass is only for moments where content must optically
  lens through a control. Never frost every card.
- **Linear** — dark-first luminance hierarchy. 4px grid. Muted greys; one
  accent pop. Density that still feels calm. Keyboard as the primary pointer.
- **Raycast** — Command is the OS. Query attaches. The field never remounts.
- **Stripe editorial** — one display serif for brand moments, then get out of
  the way. Negative space is a material.
- **visionOS layering** — three explicit z-layers, not box-shadow soup.

Radical product (must be *felt*, not documented):

1. **Sight ≠ walk.** The Table is a constellation. Sighting a star is MorphState
   (`look`). Walking it is Clock A GET. Two clocks, one sky. Filaments from the
   brass nucleus to every star are `svg` + `path` (there is no public `line` tag).
2. **Caps are wax seals.** Protected verbs (`orders.place`, `auth.otp`,
   `auth.logout`, `form.submit`, `list.subscribe`, `stepper.finish`, archive)
   show a seal that cracks when spent. Mint is `once=True` where checkout
   matters.
3. **Intent is a nucleus.** Hold an Intent in the home nucleus. Clock B is
   `POST /ux-channel/action` with `Content-Type: application/ux-channel+json`.
   Empty Content-Type is `bad_request` — `/cut` makes that visible.
4. **Hits-slot law.** Typeahead morphs `#hits`, never the field being typed.
5. **Two overlay families.** OverlayChrome (Dialog, Sheet, ActionSheet,
   AlertDialog — scrim + panel + dismiss, swipe on handle, never root) vs
   anchored (Popover, HoverCard, Tooltip, Dropdown, ContextMenu, Command).
   AlertDialog is interrupting: Escape / scrim do **not** dismiss it.
6. **Morph-then-Play.** Presence is continuous. Objects that stay do not
   remount. Motion is `scene` / `fade` / `rise` / `slide` / `morph_play` only.
7. **Payload type picks media type.** Tree → HTML (daylight). `dict` → JSON
   (pulse, `/health`). Generator → stream (`/pulse`). No `HTMLResponse` imports
   on page units.
8. **Theme is a named band.** `themeswitch` is a radiogroup `light | dark |
   system`, not a boolean switch. Glass and ink retint. Grain stays.
9. **Command is the OS.** `⌘K` / the FAB opens Command. Query attaches.
   Sign-out spends `auth.logout`.
10. **Ownership ritual.** `/copy` runs the copy press. Kit cards are rooms you
    own (`shell=False`). Brand lives on `wrap=`, never inside `render()`.
11. **Extract is owned.** Morph fragments prefer ux-dom `extract_by_id`.
    Homemade walker is escape only. The foundry never grows a `fragment.py`.

---

## 2. VISUAL SKIN LAW (first-class — equal to Isolation Law)

The previous APPIC failed as a *look* when kit-default `stone-*` classes
survived `uxcompose add`. That is forbidden.

### Tokens — author in `assets/css/input.css` as CSS variables, consume via
Tailwind `@theme` / utility classes. `uxcompose build` minifies to
`assets/static/file/css/output.css`. Document `<link>`s that sheet.

```css
:root {
  --ink: #07080A;
  --ink-2: #0C0D10;
  --raised: #121317;
  --raised-2: #181A20;
  --hairline: rgba(237, 232, 220, 0.08);
  --hairline-strong: rgba(237, 232, 220, 0.16);
  --bone: #EDE8DC;
  --bone-dim: #C9C3B4;
  --mute: #8A8B86;
  --brass: #D4B483;          /* only accent */
  --brass-ink: #1A140C;
  --danger: #E05D4A;
  --ok: #7D9B76;
  --glass: rgba(12, 13, 16, 0.58);
  --grain: 0.035;
  --r-ctrl: 10px;
  --r-card: 20px;
  --r-overlay: 28px;
  --z-base: 0;
  --z-raised: 10;
  --z-chrome: 40;
  --z-overlay: 60;
  --z-toast: 80;
  --grid: 4px;
}
[data-theme="light"] {
  --ink: #F4F0E6;
  --ink-2: #EBE6D8;
  --raised: #FFFFFF;
  --raised-2: #F7F4EC;
  --hairline: rgba(12, 13, 16, 0.08);
  --hairline-strong: rgba(12, 13, 16, 0.16);
  --bone: #16150F;
  --bone-dim: #3C3A32;
  --mute: #6A6B66;
  --glass: rgba(255, 252, 245, 0.64);
}
```

Type (load via `<link>` in Document, not JS):

| Role | Face | Size / tracking / weight |
| --- | --- | --- |
| Display | **Fraunces** (opsz 144, SOFT 50, wght 560) | 56–72px, ls -0.03em, lh 1.02 |
| Title | Fraunces 48/32 | ls -0.02em |
| UI | **Source Sans 3** | 14–16px, lh 1.45, wght 400/560 |
| Caption | Source Sans 3 | 12px, mute, ls 0.04em uppercase |
| Mono | **IBM Plex Mono** | 12–13px — Caps, hashes, ops, SHAs |

Never Inter as the brand face. Never Comic / Papyrus / default system-only.
Never emoji in chrome. Never purple, gold-foil, neon, mesh-gradient blobs,
rainbow borders, or 2021 “glassmorphism everywhere.”

### Three layers

1. **Ink base** — `--ink` canvas, 3.5% film grain overlay (`::before` on
   `body`, `pointer-events: none`), no glass.
2. **Raised rooms** — `--raised` panels, 1px `--hairline`, single soft shadow
   `0 24px 60px rgba(0,0,0,0.35)`, radius `--r-card`. Content lives here.
   **No** backdrop-filter.
3. **Glass chrome** — navbar, command, toast, dialog/sheet panel, menubar,
   mobile dock. Regular glass:
   `background: var(--glass); backdrop-filter: blur(24px) saturate(1.4);`
   `border: 1px solid var(--hairline-strong);`
   Specular 90°: `inset 0 1px 0 rgba(255,255,255,0.22)` plus a
   `linear-gradient(180deg, rgba(255,255,255,0.16), transparent 42%)` overlay
   (`pointer-events: none`). Inner bottom shade `inset 0 -1px 0 rgba(0,0,0,0.25)`.
   Specular, not frosted-white. Not a 45° slash.

Concentricity: a control of radius 10 inside a card of padding 16 has card
radius 26. Nested radii = parent radius − padding. Pill buttons 44× height,
radius 999. Tap targets ≥ 44px. Navbar floating island radius 24 (control
layer, rounder than content cards).

Spacing is a **4px grid**. Density is Linear-like: compact, not airy-SaaS.
Mobile 390×844: no horizontal overflow, bottomnav is the mobile landmark,
navbar desktop tree stays in the tree (hidden), not deleted. Constellation
collapses to a 3-column grid; filaments and nucleus hide.

`prefers-reduced-motion: reduce` disables travel; morph still happens.

### Restyle mandate

After `uxcompose add {stem}`:

- Keep behaviour, ids, ARIA, Caps, Morph/Ref split, OverlayChrome contracts.
- Replace every `bg-stone-*`, `text-stone-*`, `bg-white`, `bg-zinc-*`,
  `bg-neutral-*`, `shadow-md` default with APPIC tokens (`bg-ink`, `bg-raised`,
  `text-bone`, `border-hairline`, `bg-glass`, `text-brass`, `h-11`).
- `shell=False` on every kit `render()` used inside a room — the Atelier
  kicker/title/lede card is **off**. Rooms have APPIC chrome, not kit chrome.
- Unknown slots fail closed. Documented slots (`title`, `body`, `actions`,
  `links`, `items`, …) are how you retitle a stem into the foundry.

### What a first screenshot must show

Dark ink, Fraunces wordmark **APPIC**, brass accent used once in the nucleus,
glass navbar with 90° specular, constellation of named stars with faint
filaments, a Command hint `⌘K`, grain visible if you look, no purple, no
kit-kicker, no Inter-on-white dashboard, no emoji toolbar. If it could be
mistaken for shadcn/ui or Linear itself, restyle until it could not.

---

## 3. HARD STACK LAW

- **No React / Vue / Svelte / Solid / Next / TanStack Start / JSX / TSX** as
  the source of truth. Do **not** scaffold the Grok React template as the app.
- Preview: `uvicorn app:asgi --host 0.0.0.0 --port 8080`. Maintain
  `/workspace/startup.sh` so revive brings the same process up. Probe
  `http://127.0.0.1:8080/`, start only if down, background it.
- Auth/DB OFF at the Grok platform layer. Kit Login / OTP spend Host Caps,
  not Grok accounts. No `@/lib/db`, no `authMiddleware`.
- CSP must allow `https://grok.com`. Never strip the Grok pill. Never hide
  “Created with Grok”.
- Isolation: product never imports `ux_channel` / `cek` / `cek_host` /
  `cek_surface` / `MotionChannel`. Live Caps attach via `App.use_channel` /
  compose `wire/`. Cold import loads no Channel.
- `host="auto"`. Never `"batteries"` or `DirectoryRouter`.
- `build(document=, wrap=, live="auto", level=3, cek="require", openapi=False)`.
- Page units have **no HTTP verbs**. `render()` return type picks the container.
- XOR motion. No `html=` on plans. No root `swipe.*` on overlay hosts.
- `Document.use(XElement(), Csp.auto(), Channel.optional())` — one Document.
  Dual-Document fails doctor.
- HMR is not a Document API. Frozen serve verbs: `dev` / `prod` /
  `restart-channel`. argv `development` / `production` / `restart_channel`
  fail closed.
- Do not `pip install ux-compose` from PyPI. Clone + pin **tip `80563ab`**.
  Scaffold `COMPOSE_VCS_PIN` may lag (`24a182f`) — product pin is the tip.
- `from ux_compose.kit import X` is leftover. Own copies under `components/`.
- Official helpers only:
  `act, mark_dirty, field, status, optional_plan, optional_fade, optional_slide`.
- Silent `except ImportError` without `AttachNote` is a kill.
- Do not add `fragment.py`. Owner `extract_by_id` is the serialize door.
- Do not add Pulse rooms. L5 locks existing Pulse surfaces only.
- `ux-space` is a sibling repo, **not** a compose specialist. Do not import it.

Python **≥ 3.14**. Grok sandbox floor is 3.10 — `uv python install 3.14` then
`uv venv .venv --python 3.14` and `uv pip install --python .venv/bin/python`.
The venv has no pip.

---

## 4. KILL TRIGGERS

If you do any of these, **stop, undo, continue on the product path**.

1. Any product UI in React / Vue / Svelte / Solid / Next / TanStack / JSX / TSX.
2. `vite` / `npx vite` / `npm run build` / Nitro as the ship gate. Preview is
   uvicorn. First token of any CSS file must be CSS.
3. HTMX as architecture. `use_htmx=False`.
4. HTTP verbs on page units.
5. `from ux_compose.kit import …` as the live unit. Copy via `uxcompose add`.
6. `import ux_channel` / `cek*` / `MotionChannel` in product modules.
7. `host="batteries"` or `DirectoryRouter`.
8. Plans with `html=`. XOR. Morph first.
9. Root `swipe.*` on Dialog / Sheet / ActionSheet / AlertDialog / Command.
10. A second helper world. Official author helpers only.
11. Silent `except ImportError` without `AttachNote`.
12. Forcing Command / Dropdown / ContextMenu / Combobox / Select / Popover /
    HoverCard / Tooltip through OverlayChrome. Command is not OverlayChrome.
13. Login secrets / OTP digits / file names / money / remaining-ms on MorphState.
14. Typeahead remounting the field. Morph the hits slot.
15. Brand / navbar / footer inside `Component.render()`. They live on `wrap=`.
16. FastAPI Swagger (`docs_url` / `redoc_url` / `openapi_url` not None).
    `/docs` is a product page.
17. Shipping kit-default `stone-*` / Atelier kicker (`shell` left default).
18. Purple / neon / gradient-blob / emoji chrome / Inter-as-brand.
19. Glass on every card. Glass is the control layer. Clear glass on content.
20. A still frame that is a component gallery. APPIC is a house, not a catalog.
21. Exporting both `REDIS_URL` and `UXCOMPOSE_STATE_STORE`. Redis wins.
    Doctor `scan_store_precedence` fails closed.
22. Empty `Content-Type` on Clock B POST.
23. Cap door via `ActionRegistry.from_config`. Cap door is `Channel.boot`.
24. `scan_cek_host` left red. It is hard.
25. A new `fragment.py`. Owner extract is the door; homemade walker is escape.
26. A new Pulse room or `MATRIX.md` teaching surface.
27. Pinning lagging `COMPOSE_VCS_PIN` (`24a182f`) instead of tip `80563ab`.
28. 45° glass highlight slash. Specular is 90° from the top.

---

## 5. PRODUCT ROOMS (a house, not a catalog)

Ship Level 3. `build(host="auto", live="auto", cek="require", openapi=False)`.
Page units under `routes/`. Kit copies under `components/` with `shell=False`.
GET chrome in `chrome.py` via `foundry_wrap` + `GET_CHROME_ATTR`.

| Room | Path | Law you can touch |
| --- | --- | --- |
| Table | `/` | Constellation. Sight a star (`look`), then walk it. Filaments. |
| Door | `/enter` `/login` `/otp` | Secrets on RefState. Caps on the hinge. |
| House | `/house` | Anchored family. Hits-slot law. |
| Make | `/commission` | Clay / glaze / fire. `orders.place`. |
| Hall | `/market` | Hero, pricing (bind the button), newsletter. |
| Forge | `/forge` | Chart, tree, diff, mockup. |
| Edge | `/overlay` | OverlayChrome vs anchored family. |
| Cut | `/cut` | Cut C. A type is a seal. Empty type is `bad_request`. |
| Boot | `/boot` | Channel.boot is the Cap door. Redis wins. |
| Law | `/docs` | Written constitution. Swagger off. extract_by_id named. |
| Trace | `/trace` | Doctor: hard vs teaching vs store-clone vs precedence vs cek-host. |
| Press | `/copy` | `copy_component`. Not a card. |
| Ship | `/deploy` | `prepare_deploy` six providers. |
| Health | `/health` | dict → JSON. |
| Pulse | `/pulse` | generator → stream. No new Pulse rooms. |
| Command | `/command` | OS palette. Query attaches. Not OverlayChrome. |

Every kit stem is also a room (`/dialog`, `/typeahead`, `/menubar`, …). 81
catalog stems + OverlayChrome. Owned copies restyle to APPIC tokens.

The Table's first paint: Fraunces “The table is lit”, brass **APPIC** kicker,
glass island navbar, brass nucleus, 20 named stars, faint filaments, sight
card in Regular glass, four KPIs, `⌘K` chip. Sighting morphs `#sight` then
plays an optional plan. Knocking pulses the Host store.

---

## 6. BUILD SEQUENCE

1. Clone ux-compose @ `80563ab`. Count `CATALOG` keys. Confirm 81 + alias.
2. `uv python install 3.14` · `uv venv .venv --python 3.14` ·
   `uv pip install --python .venv/bin/python -r requirements.txt`.
3. Pin `requirements.txt` to tip `80563ab` + specialist SHAs from
   `pyproject.toml`. Do not pin lagging `COMPOSE_VCS_PIN`.
4. Own all 81 stems (`uxcompose add` or keep already-owned copies).
   Restyle off `stone-*`. `shell=False`. Copy `overlay.py`.
5. Author Document + `foundry_wrap` + `build(...)`. Isolation: no
   `ux_channel` in product modules.
6. Skin tokens in `assets/css/input.css`. Compile to `/css/output.css`.
   No `cdn.tailwindcss.com`. No CSS in Python strings.
7. `startup.sh`: probe `:8080`, start uvicorn only if down, bind
   `0.0.0.0:8080`. Keep `public/__grok`. CSP allows `https://grok.com`.
8. Doctor `routes/` + `chrome.py` + `app.py` with `app=` and `bundle=`.
   Hard scans green. Teaching may speak.
9. Browser: desktop 1280×800 and mobile 390×844. Sight a star. Open Command.
   No overflow, no console errors. Still frame is a house, not a catalog.
10. Publish to **bitplorer/appic**. Update this prompt's session log.

---

## 7. VERIFY

```
GET /          200  HTML  constellation + glass navbar
GET /health    200  application/json
GET /pulse     200  streamed
GET /docs      200  product constitution (not Swagger)
GET /command   200  palette, query attaches
GET /cut       200  Cut C is visible
POST /ux-channel/action  without Content-Type  → bad_request
doctor(...)    ok True, level 3
```

Python ≥ 3.14. Isolation holds. Brand on wrap. Caps as seals. Morph then
play. Glass on chrome only. Specular from the top.

If the library moved, **the library wins**. Re-count stems. Re-pin tip.
Do not invent names.
