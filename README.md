# APPIC

**A house of making you can inhabit.**

A private atelier OS authored in [ux-compose](https://github.com/bitplorer/ux-compose)
`80563abf1666e45fa43236e7303b1c4319413554` (0.1.0 — kit-81 + Kit Cut 1 + Cut C +
Channel.boot + Redis precedence + extract_by_id + **skin law** + **night watch** + **lumen** + **instrument**).
Pure-Python composition root for ux-dom, ux-behavior, ux-motion, and ux-channel.

No React. No Vue. No JS/TS/TSX as source of truth. Server-authored hypermedia.
Page units have no HTTP verbs. Payload type picks media type. **The kit is a
house you own — 81 stems, `shell=False`, restyled off stone defaults onto
APPIC tokens (`bg-ink`, `bg-raised`, `text-bone`, `text-brass`).** Caps
are wax seals. GET is Clock A. Action is Clock B
(`POST /ux-channel/action`, `application/ux-channel+json`). Empty Content-Type
is `bad_request`. Brand lives on `wrap=`, never inside `render()`. `/docs` is
a product page. FastAPI Swagger stays off. Channel owns FileStateStore. Redis
wins. Doctor `scan_store_clone`, `scan_store_precedence`, and `scan_cek_host`
fail closed. Morph fragments prefer ux-dom `extract_by_id`.

The Table is a **constellation**: rooms as named stars around a brass nucleus,
joined by faint filaments (`svg` + `path` — there is no public `line` tag).
Sight is MorphState (`look`). Walk is Clock A. The verb that sights a star is
`look` — never a same-named action, or MorphState is overwritten. Sighting a
star brightens its filament. The sky band (`night | dawn | noon | dusk`) is Host climate. Auto follows
the IST clock; naming a band is public. Occupancy is a short memory of sighted rooms.
Resonance is a path. The living instrument sits in GET chrome.

The foundry is a **loop you can walk**, always visible in chrome:

Brief → Wheel → Glaze → Make → Kiln → **Watch** → Air → Vitrine. **Now** is the instrument.

The Night Watch sits with the fire. Kiln and Watch share one hearth (`HOST.heat_remain`).
Keep is public. A bell is one-shot notify. This is not a Pulse room.

Visual skin is first-class: surgical Regular Liquid Glass on chrome, 90°
specular from the top, Linear luminance, concentric radii, Fraunces + Source
Sans 3 + IBM Plex Mono, brass `#D4B483` on ink `#07080A`. Glass is the
control layer, not a wallpaper. Grain lives on the body. Three z-layers: ink
base, raised rooms, glass chrome. Heat rings breathe. The wheel turns at rpm.

Ships at **Level 3**. `build(host="auto", live="auto", cek="require", openapi=False)`.
Product doctor on `routes/` + `chrome.py` + `app.py` is green.

## Run

Python **≥ 3.14**.

```bash
uv python install 3.14
uv venv .venv --python 3.14
source .venv/bin/activate
uv pip install -r requirements.txt
export PYTHONPATH="."
python -m uvicorn app:asgi --host 0.0.0.0 --port 8080
```

Or the product CLI:

```bash
uxcompose serve dev
```

Frozen serve verbs: `dev` / `prod` / `restart-channel`. argv `development` /
`production` / `restart_channel` fail closed.

CSS: author `assets/css/input.css`, compile with `uxcompose build` (or
`npx @tailwindcss/cli`) to `assets/static/file/css/output.css`. Linked as
`/css/output.css`.

## Walk

| Room | Path | Law you can touch |
|---|---|---|
| Table | `/` | Constellation. Sight a star, then walk it. Sky band retints the house |
| Now | `/now` | Living instrument. Clock, occupancy, heat trace, resonance |
| Brief | `/brief` | Named answers. Submit spends `form.submit` |
| Wheel | `/wheel` | Named stage. RPM is RefState. Lift is public |
| Glaze | `/glaze` | Named oxide. Load is RefState. `glaze.lock` |
| Door | `/enter` `/login` `/otp` | Secrets on RefState. Caps on the hinge |
| House | `/house` | Anchored family. Hits-slot law |
| Make | `/commission` | Clay / glaze / fire. `orders.place`. Wax seal |
| Kiln | `/kiln` | Named band. Shared hearth heat. Host shelf |
| Watch | `/watch` | Night watch. Keep the shared hearth. Ring the bell |
| Air | `/atmosphere` | Named atmosphere. Cone is RefState. Morph-then-Play |
| Orbit | `/orbit` | Firing window. Remaining hours are RefState |
| Charge | `/charge` | Intent is a nucleus. Wax is the seal. AttachNote |
| Vitrine | `/vitrine` | Drawn work. Rating is a named star |
| Hands | `/hands` | Studio floor. Log is RefState. `role=log` |
| Hall | `/market` | Hero, pricing (bind the button), newsletter |
| Forge | `/forge` | Chart, tree, diff, mockup |
| Edge | `/overlay` | OverlayChrome vs anchored family |
| Cut | `/cut` | Cut C. A type is a seal. Empty type is `bad_request` |
| Boot | `/boot` | Channel.boot is the Cap door. Redis wins |
| Law | `/docs` | Written constitution. Swagger off |
| Trace | `/trace` | Doctor: hard vs teaching vs store-clone vs precedence vs cek-host |
| Press | `/copy` | `copy_component`. Not a card |
| Ship | `/deploy` | `prepare_deploy` six providers |
| Health | `/health` | dict → JSON |
| Pulse | `/pulse` | generator → stream |
| Command | `/command` | OS palette. Query attaches. Not OverlayChrome |

Every kit stem is also a room (`/dialog`, `/typeahead`, `/menubar`, …). 81
catalog stems + OverlayChrome. Owned copies restyle to APPIC tokens.

## Prompt

The Grok Build metaprompt lives in [`GROK_BUILD_PROMPT.md`](GROK_BUILD_PROMPT.md).
Copy **everything below the line** into Grok Build. Feature map against
ux-compose `main` (`80563ab`): [`FEATURE_INVENTORY.md`](FEATURE_INVENTORY.md).

If the prompt and the library disagree, **the library wins**.

Independent Grok Build re-read + execution of ux-compose `80563ab` (2026-09-17):
Night Watch as a house room, shared hearth heat, sky band as Host atmosphere,
loop rail in GET chrome, filament brightening, concentric heat rings.

## Pins

| Package | SHA |
|---|---|
| ux-compose | `80563abf1666e45fa43236e7303b1c4319413554` |
| ux-dom | `2e894cd7bca66e1da6c2f9d42b2d1a8bb937c92c` |
| ux-behavior | `7d46979f59f284bc2d6d961ed372ec849e851dfc` |
| ux-motion | `bbe7d73466a6c1eccb47e711568c80ce3b4d5487` |
| ux-channel | `a6ab1594959b287b4754afe09d8aced5504edd8f` `#subdirectory=python` |
| cek-host / cek-surface | `>=0.1.3` |

License: MIT.
