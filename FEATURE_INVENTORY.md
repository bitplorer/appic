# ux-compose — complete feature inventory (`060b583`)

Sourced from [bitplorer/ux-compose](https://github.com/bitplorer/ux-compose) `main`
SHA **`060b583f64512302059bd9d4ff691bb6a2f4dd3a`** (walk of `src/ux_compose/**/*.py`,
`kit/catalog.py`, `__all__`, CHANGELOG Unreleased, 2026-09-10).

If this page and the code disagree, **the code wins**.

## Specialist pins (`pyproject.toml`)

| Package | Pin |
|---|---|
| ux-compose | `060b583f64512302059bd9d4ff691bb6a2f4dd3a` |
| ux-dom | `e8be99a52bfecd6026c200fa1c3dc6a74f87aacb` |
| ux-channel | `d0fe7169e687d2935f8b74d40b990b1ee63ef3d4#subdirectory=python` |
| ux-behavior | `793f120e3b1388925772cd069b070d7918b78baa` |
| ux-motion | `67ff3f0c4912b70b7056f8226a6f226b6fe93f60` |
| cek-host / cek-surface | `>=0.1.3` |

Python floor **≥ 3.14**. Hard-deps. Missing specialists fail loud.

## Progressive levels

| Level | Attach |
|---|---|
| 0 | Static Document (ux-dom hard dep) |
| 1 | Offline MorphState + `@action` — `App.boot` |
| 2 | Live Caps + Intent — `App.use_channel(asgi_app=…)` behind `wire/` |
| 3 | Motion — `App.use_motion()` |

Level 1 code remains correct at L2/L3. Zero rewrite.

## Public author surface (`ux_compose.__all__`)

`App`, `build`, `WebAssets`, `DirectoryRoutes`, `DirectoryASGI`, `RouterHooks`,
`Surface`, `SurfaceBundle`, `SurfaceError`, `mount_surfaces`, `scan_surfaces`,
`validate_surfaces`, `Component`, `MorphState`, `RefState`, `action`, `bind`,
`control`, `notify`, `update_with`, `morph_play`, `act`, `mark_dirty`, `field`,
`status`, `optional_plan`, `optional_fade`, `optional_slide`, `AttachNote`,
`attach_notes`, `Level`, `doctor`, `DoctorResult`, `scene`, `fade`, `rise`,
`slide`, `HAS_DOM`, `raw`, plus tag constructors:
`html head body title style meta link script div span h1 h2 h3 p a button form input_ ul li header footer aside section article nav main label svg path rect circle dl dt dd table thead tbody tr th td fieldset legend hr img progress`.

`build(package_dir, *, name, host="auto", live="auto", level="auto", base="routes",
fail_closed=True, use_htmx=False, asgi_app=None, document=None, wrap=…, cek="require",
openapi=False)`.

## Kit catalog — 81 stems (`css: False`, `page: True`)

login, tabs, accordion, dropdown, dialog, sheet, toast, command, table,
pagination, combobox, sidebar, breadcrumb, stepper, carousel, calendar, select,
otp, plans, actionsheet, contextmenu, typeahead, pullrefresh, drawer (Sheet
alias), navbar, navmenu, usermenu, popover, tooltip, alertdialog, formlayout,
fieldset, datepicker, switch, card, emptystate, stats, alert, banner, progress,
skeleton, hero, footer, cta, avatar, badge, hovercard, searchbar, fileupload,
tagsinput, multiselect, descriptionlist, featuregrid, testimonials, newsletter,
bottomnav, separator, slider, menubar, toolbar, togglegroup, spinbutton,
themeswitch, filterbar, chat, questionnaire, pricingsection, logocloud,
timeline, rating, chart, resizable, tree (`treeview` alias), colorpicker, fab,
diff, countdown, mockup, attachment, scrollarea, feed.

Not stems: `catalog.py`, `copy.py`, `OverlayChrome` (copied as overlay sibling).

## Kit Cut 1 (this pin)

`render(*, shell=None, **slots)` writes documented seams (`actions`→`ACTIONS`,
`title`/`body`/`items`, …) via `ux_compose.kit_construct.apply_slots`.
`shell=False` (kwarg or `self.shell`) drops Atelier kicker/title/lede through
`kit_shell`. Unknown slots fail closed. Zero-arg `App.add(cls)` still greens.

## State law

| Kind | Field |
|---|---|
| Open / value / query / named step / named band | `MorphState` |
| Magnitude, lists, money, ISO dates, files, digits, remaining seconds, bar heights | `RefState` + `dirty = MorphState("idle")` + `mark_dirty` |
| One-shot message | `notify(...)` |
| Protected verb | `@action(caps=("…",))` |

Channel session plane refuses quantity MorphState. Rating stars are named keys
(`one`…`five`).

## Clock A payload

Return type picks media type: tag tree / str → HTML (wrap applied); dict/list →
JSON; generator → stream. Page units have **no** `get`/`post`.

## Isolation

Product modules never import `ux_channel`. Live Caps attach through
`App.use_channel` / compose `wire/`. Channel on Document is
`ux_dom.runtime.Channel`. FileStateStore is Channel-owned; compose
`serve_state.py` is lifecycle only. Doctor `scan_store_clone` fails closed.

## Doctor families

Isolation, dual-Document (hard). Kit-import, leftover aliases, render-chrome,
FastAPI docs collision, CEK host, store-clone. Teaching residuals expire by
rendering them, not by deleting the scan.

## CLI

`uxcompose create-app` · `serve {dev,prod,restart-channel}` · `build` ·
`deploy --provider docker|fly|render|railway|vps|checklist` · `doctor` ·
`add [name] [--force] [--page]` · `add --list`.

Reserved dest names: `site`, `test`, `email`, stdlib, keywords.

## GET chrome

`ux_compose.chrome.brand_wrap(document, brand=…)` + `GET_CHROME_ATTR`. Never
inside `Component.render()`. Morph payloads stay fragments.

## Overlay families

Edge (OverlayChrome): Dialog, Sheet, Drawer (`kind="drawer"`), ActionSheet,
AlertDialog (Escape/scrim do **not** dismiss), Command.

Anchored: Dropdown, Popover, Tooltip, HoverCard, ContextMenu, NavMenu, Select,
Combobox, UserMenu.

## APG holds

Menubar submenu ids `{id}-m-{key}` stay in the tree with `hidden` when closed.
FAB `{id}-menu` same. Toolbar last command `aria-current`. Tabs/login inactive
panels stay, `hidden`. Calendar/datepicker `role=grid`. Table row select binds
the checkbox, not the `<tr>`. Pricing choose binds the button, not the row.
Typeahead morphs `#typeahead-hits` only.
