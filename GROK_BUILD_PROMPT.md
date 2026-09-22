# GROK BUILD PROMPT — APPIC
### ux-compose 0.1.0 · kit-81 · pin `80563abf1666e45fa43236e7303b1c4319413554`
### Generation: **Aperture · Lattice · Solstice · Vault · Anvil**
### Devised 2026-09-22 for Grok Build. Library wins if this prompt and the source disagree.

---

> **How to use this file.** Copy everything below the line `COPY FROM HERE` into a Grok Build session. You are Grok Build. Plan first. Then ship. Then publish to `bitplorer/appic`.

---

# COPY FROM HERE

You are **Grok Build**. Your job is to ship a **complete, visually stunning, fully working product** — not a prompt, not a widget zoo, not a brochure.

## 0. PLAN FIRST (mandatory — do this before writing product files)

Do not scaffold, do not invent APIs, do not start rooms until this protocol is done. Write a short plan (in `PLAN.md` in the product tree) that you will follow.

### 0.1 Clone and pin the library

Clone [bitplorer/ux-compose](https://github.com/bitplorer/ux-compose) at SHA **`80563abf1666e45fa43236e7303b1c4319413554`**. Python **≥ 3.14**. Install with `pip install -e ".[serve]"`. If the sandbox has no 3.14, say so and stop — do not polyfill on 3.12.

### 0.2 Deep-dive every public name (no skipping)

Read, in this order, and **map each name to a product surface** in the plan:

1. `START_HERE.md`, `AGENTS.md`, `CRITIC.md`, `docs/OWNERSHIP.md`, `docs/ARCHITECTURE.md`, `docs/INDEX.md`
2. `src/ux_compose/__init__.py` `__all__` — every name below is legal; names not on it are illegal
3. `docs/guides/PATH.md`, `docs/guides/UI.md`, `docs/guides/SNIPPETS.md`, `docs/guides/HOST.md`, `docs/reference/host.md`
4. `cookbooks/PRESENCE.md` (Morph-then-Play, XOR, `scene.share`, `stagger_in`)
5. `docs/adr/0002-product-host.md`, `docs/adr/0005-serve-dev-split.md`
6. `src/ux_compose/kit/__init__.py` — 81 stems. Own copies with `uxcompose add <stem>` (`shell=False`). Do **not** `from ux_compose.kit import X` in product rooms.
7. `examples/README.md` encoding rule + Atelier patterns
8. Existing product: clone / pull [bitplorer/appic](https://github.com/bitplorer/appic) and **upgrade in place**. Do not empty the house.

**Author surface — these are the only verbs. Do not invent names.**

```
App  build  WebAssets
DirectoryRoutes  DirectoryASGI  RouterHooks
Surface  SurfaceBundle  SurfaceError
mount_surfaces  scan_surfaces  validate_surfaces
Component  MorphState  RefState  action
bind  control  notify  update_with  morph_play
act  mark_dirty  field  status
optional_plan  optional_fade  optional_slide
AttachNote  attach_notes
Level  doctor  DoctorResult
scene  fade  rise  slide
HAS_DOM
DOM tags: raw html head body title style meta link script
          div span h1 h2 h3 p a button form input_ ul li
          header footer aside section article nav main label
          svg path rect circle dl dt dd
          table thead tbody tr th td
          fieldset legend hr img progress
```

There is **no** `ux.div`, `when`, `forall`, `Page`, `location.reload()` happy path, `fragment.py`, `DirectoryRouter`, `host="batteries"`, or public `line` tag (filaments are `svg` + `path`).

### 0.3 Feature → product map (every name earns a room or a law)

| Public name | Product meaning in APPIC |
|---|---|
| `App.boot` / `build()` | One door. Clock A GET. `host="auto" live="auto" level="auto" cek="require" openapi=False` |
| `Component` + `id` | A morph target. Stem == file == class == `#id` |
| `MorphState` | Named qualitative: open / band / grain / season / focus / face |
| `RefState` + `dirty = MorphState("idle")` | Magnitude, lists, money, ISO dates, files, digits, folds, remaining, rpm, heat |
| `mark_dirty` | The spark on the Anvil — flips dirty so a RefState-only strike still morphs |
| `@action(caps=())` | Public verb |
| `@action(caps=("orders.place",))` etc. | Protected verb. Wax seal. Fail-closed offline |
| `bind(self.verb, **args)` | Preferred control. The strike. |
| `control("stem.verb", **args)` | Stringly hatch. Allowed, not preferred. |
| `notify(...)` | One-shot. Bell, toast, seal-crack copy. Never a state store. |
| `update_with(self, plan, extra_ops=)` | Morph-then-Play. Plan carries **no** `html=` (XOR). |
| `morph_play(id, plan)` | Hop when the unit itself is the scene. |
| `scene` / `fade` / `rise` / `slide` / `stagger_in` / `scene.share` | Presence. Objects that stay do not remount. |
| `optional_plan` / `optional_fade` / `optional_slide` | Aperture depth-of-field. Shallow vs deep motion. |
| `act` / `field` / `status` | Anvil forms. POST `/act/{action}`. Status is a note, not a store. |
| `AttachNote` / `attach_notes` | Vault slips. A note rides a presence, not a column. |
| `Surface` / `scan_surfaces` / `validate_surfaces` / `mount_surfaces` / `SurfaceBundle` / `SurfaceError` | Lattice. The house as a graph of doors. Fail-closed on id/path clash. |
| `DirectoryRoutes` / `DirectoryASGI` / `RouterHooks` | HTTP path law. Walking is Clock A. Hooks are hinges, not a second router. |
| `WebAssets` | CSS/static layout. `uxcompose build` owns Tailwind. |
| `Level` L0–L3 | Progressive. L1 code stays correct at L3. Zero rewrite. |
| `doctor` / `DoctorResult` | Trace. Hard vs teaching vs store-clone vs precedence vs cek-host. Fail closed. |
| `prepare_deploy` | Ship room. Six providers: `docker fly render railway vps checklist`. |
| `wrap=` | Brand chrome. **Never** inside `render()`. |
| Payload of `render()` | tree/`str` → HTML · `dict` → JSON · generator → stream. No HTTP verbs on page units. |

If a name on `__all__` has no row in your `PLAN.md`, you are not done planning.

---

## 1. NORTH STAR

**APPIC** is a private nocturnal foundry you can inhabit.

Not a landing page. Not a component gallery. An **atelier operating surface** for commissioning handmade objects — clay, glaze, fire — and living with them. Server-authored hypermedia. Capability-secured. Progressive. The kit is a house you own.

The foundry is a loop you can walk. Sighting a room is not walking it.

> Sight ≠ walk. The Table is a constellation. Sighting a star is `look` (MorphState). Walking it is Clock A GET. Two clocks, one sky.

**This generation** gives the house five new organs — not metaphors glued on, but the leftover public API made inhabitable:

| Organ | Path | What it is | API it must exercise |
|---|---|---|---|
| **Aperture** | `/aperture` | The viewing glass. Named focal plane. Depth of field. | `optional_plan` `optional_fade` `optional_slide` · focus MorphState · exposure RefState |
| **Lattice** | `/lattice` | The house looking at its own doors. | `scan_surfaces` `validate_surfaces` `mount_surfaces` `SurfaceBundle` `RouterHooks` |
| **Solstice** | `/solstice` | Time as craft. Named season. Firing almanac. | owned `Calendar` `DatePicker` `Countdown` · season MorphState · remaining RefState · `data-solstice` |
| **Vault** | `/vault` | Sealed archive of fired work. Slips ride presence. | `AttachNote` `attach_notes` · Caps as keys · `status` · genealogy of wax |
| **Anvil** | `/anvil` | The live strike. Bind kneads. Dirty sparks. | `bind` `mark_dirty` `act` `field` `status` · XOR `update_with` |

These five are **not Pulse rooms**. Pulse (`/pulse`) stays the generator → stream demonstration and nothing else.

**Hard product promises**

- Fully working. Every control does what it says. Empty states, error states, retry, undo where the verb implies it.
- Fully utilising ux-compose — every `__all__` name, every kit stem owned, every encoding law.
- Premium, high-end, calm. Apple Liquid Glass 2026 × Linear density × Stripe trust × Vercel restraint.
- Publish the running source to **`bitplorer/appic`** (upgrade in place; create the repo only if it is gone).
- **No React / Vue / Svelte / Solid / Next / TanStack Start / JSX / TS / TSX** as the app. Do not scaffold the Grok React template as the product. Python is the author. HTML is the runtime.

---

## 2. VISUAL SKIN LAW (first-class — equal to Isolation Law)

Take the 2026 premium bar and **commit**, do not sample:

| Source | What you steal | What you refuse |
|---|---|---|
| **Apple HIG Liquid Glass 2026** | Clarity, Deference, Depth. Concentric radii. Specular from **90° (top)**. Regular glass on chrome only. | Wallpaper glass. Rainbow refraction. `backdrop-filter` soup on content. |
| **Linear** | 4px grid, 1.5× spacing scale, near-monochrome, one accent, information density, keyboard-first. | Decoration that does not carry state. |
| **Stripe** | Sentence case. Trust before click. Whitespace as a material. Oxford comma in product copy. | Marketing gradients. Fake testimonials as UI. |
| **Vercel** | Mono as a UI font (IBM Plex Mono for digits, Caps, traces). Black/white dominance. | Neon, mesh blobs, purple wash. |
| **DTCG tokens 2026** | Three layers: primitive → semantic → component. Author primitives in `:root`, consume via Tailwind `@theme`. | Raw hex in components. |

**Tokens** — author in `assets/css/input.css`. `uxcompose build` writes `assets/static/file/css/output.css`. Document `<link>`s that sheet. Brand lives on `wrap=`.

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
  --space: 4px;
}
```

**Type.** Fraunces (opsz 144, wght 560) for display. Source Sans 3 for body. IBM Plex Mono for digits, Caps, traces, rpm, heat. **No Inter. No emoji in chrome. No purple.**

**Three z-layers.** Ink base → raised rooms → glass chrome. Grain lives on the body (`data-grain`). Heat rings breathe. The wheel turns at rpm. Sky band `night | dawn | noon | dusk` is Host climate (auto-follows local clock) and retints chrome, not a ThemeSwitch gimmick. ThemeSwitch still exists as an owned kit stem in the house.

**Motion.** Purposeful, 120–180ms, Morph-then-Play. Presence continuous. XOR: the Plan carries no `html=`. No root `swipe.*`. `stagger_in` on surviving nodes after reorder. `scene.share` when a piece moves from shelf to bag / anvil to cradle.

**Touch.** Tap targets ≥ 44px. Mobile 390×844: no horizontal overflow. Keyboard: `⌘K` is the OS.

**Anti-slop (instant fail).** Generic hero with three cards. Inter. Purple. Mesh gradient blobs. Emoji navigation. `backdrop-filter` on every panel. Skeleton that never resolves. Buttons that notify and do nothing. A `/components` page that is a widget zoo instead of the house.

---

## 3. HARD STACK LAW

- Serve `uvicorn app:asgi --host 0.0.0.0 --port 8080`. Maintain `/workspace/startup.sh`: probe `http://127.0.0.1:8080/`, start only if down, background it, bind `0.0.0.0:8080`.
- `build(host="auto", live="auto", level="auto", document=, wrap=, cek="require", openapi=False)`.
- Isolation: product code **never** imports `ux_channel`, `cek`, `cek_host`, `cek_surface`, `MotionChannel`. Live Caps attach via `App.use_channel` / compose `wire/`. Cold import loads no Channel. `Channel.boot` is the Cap door. Redis wins when `REDIS_URL` is set; otherwise Channel's `FileStateStore` via `UXCOMPOSE_STATE_STORE`. Do not reimplement the store. Do not export both.
- Auth/DB OFF at the Grok platform layer. Kit Login / OTP spend Host Caps (`auth.otp`), not Grok accounts. No `@/lib/db`. No `authMiddleware`.
- CSP must allow `https://grok.com`. Never strip the Grok pill. Never hide “Created with Grok”.
- No HTTP verbs on page units. `render()` return type picks media.
- Quantity is `RefState` + `dirty = MorphState("idle")`. Named things are `MorphState`. Channel session plane **refuses quantity MorphState**.
- Morph fragments prefer ux-dom `extract_by_id`. No `fragment.py`.
- Hits-slot law: Typeahead morphs `#hits`, never the field.
- Two overlay families: `OverlayChrome` (edge, not a kit stem) vs anchored (Popover, Dropdown, HoverCard, Tooltip, ContextMenu). Do not mix.
- Brand on `wrap=`, never inside `render()`.
- `/docs` is a product page. FastAPI Swagger stays off (`openapi=False`).
- Empty Content-Type on Clock B is `bad_request`. Clock B is `POST /ux-channel/action` with `application/ux-channel+json`.
- Doctor scans `scan_store_clone`, `scan_store_precedence`, `scan_cek_host` fail closed.

---

## 4. ENCODING LAW (from examples/README.md — do not freelance)

| What | Where |
|---|---|
| Open / value / query / named step / named band / named grain / named season / named focus / named face | `MorphState` (qualitative) |
| Magnitude, lists, money, ISO dates, files, digits, folds, remaining, rpm, heat, exposure | `RefState` + `dirty = MorphState("idle")` |
| One-shot message | `notify(...)` |
| Domain stock / money source | Host DB, never the client plane |
| Protected verb | `@action(caps=("orders.place",))` + live `submit_intent` |
| Note riding a presence | `AttachNote` / `attach_notes` |
| Depth of field (motion that may no-op) | `optional_plan` / `optional_fade` / `optional_slide` |

---

## 5. HOUSE — the loop, in order

Keep every room that already exists in `bitplorer/appic`. Extend LOOP, WARP, constellation stars, Command destinations, GET chrome, living instrument.

**Visible loop (chrome, always):**

> **Wedge → Brief → Wheel → Bisque → Glaze → Make → Kiln → Raku → Watch → Air → Vitrine → Mend → Gift → Score → Chorus → Tide → Fugue → Aperture → Lattice → Solstice → Vault → Anvil → Coda**

**Table `/`.** Constellation. Rooms as named stars around a brass nucleus, filaments `svg` + `path`. Verb that sights a star is `look` — never a same-named action. Sighting brightens the filament. Walking is GET.

**Command `/command`.** The OS. `⌘K`. Query attaches. Destinations include every house room plus verbs `knead quench coal coda focus map season seal strike`. Not OverlayChrome.

**This session — five organs you must ship fully working.** Upgrade in place. Do not regress Wedge/Bisque/Raku/Ember/Coda/Tide/Fugue/Mirror/Phantom/Cloth or any prior room.

### 5.1 Aperture — `/aperture` · APERTURE-1

The house grows a viewing glass.

- Named **focal plane**: `near | mid | far` (MorphState).
- **Exposure** is RefState (digits). `mark_dirty` on stop-down so the morph fires.
- Depth of field is motion intensity:
  - near → `optional_plan("aperture-near", "#aperture-stage", ms=120)`
  - mid → `optional_fade("aperture-mid", "#aperture-stage", ms=140)`
  - far → `optional_slide("aperture-far", "#aperture-stage", direction="next", ms=180)`
- XOR: no `html=` on the plan. The morph patch is the HTML.
- GET chrome carries `data-aperture="{plane}"`. Grain and brass respond (near is denser grain, far is thinner).
- `bind(self.stop, stops=…)` preferred. A public lift still uses `control` as the hatch so both paths stay proven.
- Not Watch. Not Pulse. Not Ember. The instrument in GET chrome gains an aperture path (iris), living.

### 5.2 Lattice — `/lattice` · LATTICE-1

The house looks at its own doors.

- On GET, `scan_surfaces` the product `routes/` (and kit rooms). `validate_surfaces` fail-closed. Render the `SurfaceBundle` as a **graph**, not a table dump: each surface is a node, filaments are legal walks (Clock A paths).
- Named **face**: `doors | clashes | hooks` (MorphState). Doors lists legal surfaces. Clashes lists `SurfaceError` (empty is an EmptyState you own). Hooks demonstrates `RouterHooks` as hinges — a named hook that annotates a walk, never a second HTTP pipeline.
- Walking a node is Clock A (`<a href=…>`), sighting it is `look` (MorphState) — same law as the Table.
- `stagger_in` on `#node-*` after a face change.
- Doctor-green: id/path clashes cannot ship.

### 5.3 Solstice — `/solstice` · SOLSTICE-1

Time is craft.

- Named **season**: `winter | spring | summer | autumn` (MorphState). `data-solstice` on GET chrome retints sky, not a fourth theme.
- Owned copies (`uxcompose add`, `shell=False`, restyled to APPIC tokens): **Calendar**, **DatePicker**, **Countdown**. They sit in this room as the firing almanac, not as demo cards.
- Remaining hours to the next fire is RefState. Cone / window already live in Orbit — Solstice is the **year**, Orbit is the **window**. Do not collapse them.
- `bind(self.season, name=…)` turns the wheel of the year. `stagger_in` on `#mark-*` (solstice marks).
- Countdown is presence-continuous with the living instrument (shared Host remaining, like Kiln/Watch share `HOST.heat_remain`). One clock, two faces.

### 5.4 Vault — `/vault` · VAULT-1

Fired work, sealed.

- Host stock of pieces (domain source — never client plane).
- Each piece carries an `AttachNote` (slip of paper: who drew it, which seal, which firing). `attach_notes` on the presence so the slip **travels** when `scene.share` moves a piece from Vault to Vitrine.
- Caps are keys. Opening a sealed drawer spends a Cap (`vault.open`). Wax seal in chrome cracks on spend (`notify` one-shot). Fail-closed offline.
- `status(..., kind="note")` for the slip line. Empty vault is owned EmptyState, not a blank.
- Genealogy: parent seal is the previous firing (Provenance remains the long form; Vault is the **body** of work). Do not duplicate Provenance — link it.

### 5.5 Anvil — `/anvil` · ANVIL-1

The live strike.

- The piece on the anvil is named (MorphState). The blow count is RefState.
- `bind(self.strike, force=…)` is the preferred control. Each strike: increment RefState, `mark_dirty(self)`, `update_with(self, optional_plan("anvil-spark", "#anvil-piece", ms=120), extra_ops=[notify("struck")])`.
- `act("anvil.quench", "Quench", kind="primary", target="#anvil-stage")` + `field("temp", kind="text")` prove the author helpers. Quench is a protected verb (`caps=("orders.place",)` or a dedicated `anvil.quench` Cap) — wax seal.
- XOR morph_play toward the cradle in GET chrome (`scene.share` leave `#anvil-piece` arrive `#cradle-vessel`).
- `status` reports last strike. Not Pulse. Not Wheel (Wheel is throwing; Anvil is striking).

---

## 6. KIT-81 — a house you own, not a zoo

Every stem in `src/ux_compose/kit/__init__.py` is an owned copy (`uxcompose add`, `shell=False`), restyled off stone defaults onto APPIC tokens (`bg-ink`, `bg-raised`, `text-bone`, `text-brass`). OverlayChrome is the edge primitive and is **not** addable via the CLI.

Each stem has a room (`/dialog`, `/typeahead`, …) **and** a job in the house. A stem with only a gallery card has failed.

| Stem | House job |
|---|---|
| Login, Otp | Door `/enter` `/login` `/otp`. Secrets on RefState. Caps on the hinge. |
| Navbar, NavMenu, UserMenu, Sidebar, BottomNav, Breadcrumb, Menubar, Toolbar | Chrome families. Glass layer. |
| Command | OS. `/command`. |
| Tabs, Accordion, Stepper, ToggleGroup, Switch, ThemeSwitch | Named bands and qualitative flips. |
| Dialog, AlertDialog, Sheet, Drawer, ActionSheet | OverlayChrome family. |
| Popover, Dropdown, HoverCard, Tooltip, ContextMenu | Anchored family. Hits-slot when they search. |
| Toast, Banner, Alert, EmptyState, Skeleton, Progress | System voice. Skeleton always resolves. |
| Table, Pagination, FilterBar, SearchBar, Typeahead, Combobox, Select, MultiSelect, TagsInput | Collections. Hits-slot law. |
| FormLayout, Fieldset, FileUpload, Slider, SpinButton, DatePicker, Calendar, ColorPicker | Forms. Quantities RefState. |
| Card, Hero, Footer, Cta, FeatureGrid, Testimonials, Newsletter, PricingSection, Plans, LogoCloud | Hall `/market`. Bind the pricing button. |
| Avatar, Badge, Separator, DescriptionList, ScrollArea, Resizable | Furniture. |
| Chat, Feed, Timeline, Rating, Chart, Tree, Diff, Mockup, Attachment | Forge `/forge` + Hands `/hands` + Vitrine. |
| Carousel, Fab, PullRefresh, Countdown, Questionnaire | Spatial / mobile / almanac. |
| Stats | Living instrument + `/now`. |
| OverlayChrome, overlay | Edge. Not a stem. |

`treeview` is an alias of Tree. Do not add a second catalog.

---

## 7. RADICAL FEATURES (must all work — not copy)

These are the product, not the kit.

1. **Two clocks, one sky.** Clock A GET (Document, HMR-safe). Clock B POST `/ux-channel/action`. Empty type is `bad_request`. `/cut` teaches this. `/health` is `dict` → JSON. `/pulse` is generator → stream. Do not add more Pulse rooms.
2. **Sight ≠ walk.** Table constellation. `look` morphs. `<a>` walks.
3. **Caps as wax seals.** Protected verbs show a seal that cracks when spent. Fail-closed offline. `/boot` teaches `Channel.boot`. Redis wins.
4. **Command as OS.** `⌘K`. Query attaches. Destinations + verbs.
5. **Shared hearth.** Kiln and Watch share `HOST.heat_remain`. Solstice and the instrument share remaining-to-fire. One number, two faces.
6. **Presence-continuous vessel.** Cradle in chrome. `scene.share` moves occupant. Cloth / Vessel / Anvil / Vault all honour the same `#cradle-vessel`.
7. **Sky band + climate attributes.** `data-grain` `data-coal` `data-raku` `data-tide` `data-eclipse` `data-aperture` `data-solstice` on GET chrome. Host climate, not a CSS carnival.
8. **Morph-then-Play XOR.** No `html=` on plans. `stagger_in` on `#fold-*` `#hop-*` `#coda-*` `#node-*` `#mark-*`.
9. **Hits-slot.** Typeahead morphs `#hits`.
10. **Doctor as constitution.** `/trace` runs `doctor(".")` and shows hard vs teaching. `/docs` is the written law. Swagger off.
11. **Ship.** `/deploy` calls `prepare_deploy` for all six providers and shows the checklist as a room, not a README.
12. **Aperture / Lattice / Solstice / Vault / Anvil** as specified in §5 — fully working, not stubs.

---

## 8. EXECUTION ORDER

1. Plan (`PLAN.md`) with the feature map from §0.3 ticked.
2. Pin library. Own any missing kit copies.
3. Skin tokens + chrome `wrap=` + constellation + Command destinations for the five new organs.
4. Implement the five rooms in order: Aperture → Lattice → Solstice → Vault → Anvil. Each room is a real `Component` with `id`, Morph/Ref correctly encoded, `bind` preferred, XOR motion, empty/error states.
5. Extend LOOP, WARP, GET chrome (`data-aperture`, `data-solstice`), living instrument (iris + almanac hand), doctor-green `routes/` + `chrome.py` + `app.py`.
6. Serve on `0.0.0.0:8080`. Verify in a real browser: Table, each new room, Command, a Cap spend, a `scene.share` into the cradle, `/health` JSON, `/pulse` stream, mobile 390×844.
7. Publish source to **`bitplorer/appic`** (upgrade in place). MIT. Update `README.md` and `FEATURE_INVENTORY.md` honestly — claim only what works.
8. Leave the server up. Do not ask the user to run commands.

---

## 9. SHIP GATE (all must be true)

- [ ] Python ≥ 3.14, library SHA `80563abf`, Isolation intact (no product `ux_channel` import)
- [ ] Every `__all__` name mapped and exercised
- [ ] All 81 kit stems owned, restyled, and employed in the house
- [ ] Five new organs fully working with the APIs in §5
- [ ] Encoding law held (no quantity MorphState)
- [ ] XOR held (no `html=` on plans)
- [ ] Brand on `wrap=` only
- [ ] Visual skin: Liquid Glass chrome, brass on ink, Fraunces/Source Sans 3/IBM Plex Mono, 4px grid, no Inter/emoji-chrome/purple/mesh
- [ ] `⌘K` Command includes the new destinations and verbs
- [ ] Constellation shows the new stars; sight ≠ walk
- [ ] `/health` JSON, `/pulse` stream, `/docs` product page, Swagger off
- [ ] Browser: visible content, no console errors, mobile usable
- [ ] Published to `bitplorer/appic` with honest README + FEATURE_INVENTORY
- [ ] `startup.sh` revives the same process on `0.0.0.0:8080`

If a gate is red, do not declare done. Fix it.

---

## 10. HONESTY LOCKS (do not reopen)

- Library wins.
- No React as the app.
- No new Pulse rooms.
- No second HTTP pipeline.
- No store clone.
- OverlayChrome is not a kit stem.
- Wedge / Bisque / Raku / Ember / Coda / Tide / Fugue / Mirror / Phantom / Cloth and every prior house room stay working.
- Aperture, Lattice, Solstice, Vault, Anvil are not Pulse, not Watch, not Kiln, not ThemeSwitch.

# COPY TO HERE

---

## Appendix — session history (do not paste; context for agents)

APPIC has been inhabited across sessions. The house already contains the foundry loop, kit-81, Liquid Glass skin, constellation Table, Command OS, wax-seal Caps, shared hearth, vessel/cradle, climate attributes, and rooms including Wedge, Bisque, Raku, Ember, Coda, Cloth, Tide, Fugue, Mirror, Phantom, Vessel, Score, Chorus, Eclipse, Duet, Provenance, Threshold, and the rest listed in `README.md`.

This file **replaces** the accreted dated prompts as the master. The copy-block above is self-contained. Previous generation nicknames (tide, fugue, cloth, score, …) remain product rooms; they are not Pulse.

Pin remains ux-compose `@ 80563abf1666e45fa43236e7303b1c4319413554`.
