# APPIC

**A house of making you can inhabit.**

A private atelier OS authored in [ux-compose](https://github.com/bitplorer/ux-compose)
`030226422ed24c9f5a6d91e249e11cc63dec83c5` (0.1.0 — kit-81 + Kit Cut 1 + Cut C +
Channel.boot + Redis precedence + extract_by_id + **skin law** + **night watch** + **lumen** + **instrument** + **vessel** + **kintsugi** + **score** + **chorus** + **eclipse** + **duet** + **provenance** + **threshold** + **cloth** + **tide** + **fugue** + **mirror** + **phantom** + **wedge** + **bisque** + **raku** + **ember** + **coda**).
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

**Wedge** → Brief → Wheel → **Bisque** → Glaze → Make → Kiln → **Raku** → Watch → Air → Vitrine → Mend → Gift → Score → Chorus → Tide → Fugue → **Coda**.
**Now** is the instrument. **Ember** is the last coal. **Vessel** is the inhabitant. The **cradle** in chrome keeps it. The **companion cradle** is the duet. **Eclipse** occludes the sky. **Tide** is lunar water (`data-tide`). **Fugue** hops the warp (`morph_play`). **Raku** quenches (`morph_play`, heat dumps to ash, `data-raku`). **Wedge** kneads (`bind()`, folds are RefState). **Bisque** is first fire. **Coda** closes the loop. **Mirror** is the piece looking at itself. **Phantom** is ghost occupancy. **Cloth** is the warp; occupancy is weft.

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
| Wedge | `/wedge` | Named grain. Folds are RefState. `bind()` kneads. `stagger_in` on `#fold-*` |
| Bisque | `/bisque` | First fire. Named biscuit. Remaining is RefState. Not `/kiln` |
| Raku | `/raku` | Sudden quench. Named reduction. `morph_play`. Heat dumps to ash. `data-raku` |
| Ember | `/ember` | Last coal. Named coal. Instrument fragment. Not Watch. Not Pulse |
| Coda | `/coda` | The loop closes. Named close. `morph_play` toward the table |
| Now | `/now` | Living instrument. Clock, occupancy, heat trace, resonance |
| Cloth | `/cloth` | Warp is the loop. Weft is occupancy. `stagger_in`. `bind()` weaves |
| Tide | `/tide` | Named lunar phase. `data-tide` on GET chrome. New burns hotter |
| Fugue | `/fugue` | The house plays the loop. `morph_play` hop. XOR no `html=` |
| Mirror | `/mirror` | Named face. Owned Diff, `shell=False`. The piece looking at itself |
| Phantom | `/phantom` | Ghost occupancy. Unsighted warp fades. Not Pulse |
| Vessel | `/vessel` | The piece is the house. Named stage. Presence-continuous with the cradle |
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
| Mend | `/kintsugi` | Named break. Brass is the join. `repair.join` |
| Gift | `/gift` | Named destination. `gift.send`. The cradle empties |
| Score | `/score` | House as a staff. stagger_in on `#note-*`. Host stock |
| Chorus | `/chorus` | Concurrent hands. Presence cookbook reorder |
| Eclipse | `/eclipse` | Named umbra. `data-eclipse` on GET chrome |
| Duet | `/duet` | Two cradles. `scene.share` XOR |
| Provenance | `/provenance` | Wax genealogy. Parent is the previous seal |
| Threshold | `/threshold` | `scan_surfaces` as doors. Walking is Clock A |
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
ux-compose `main` (`0302264`): [`FEATURE_INVENTORY.md`](FEATURE_INVENTORY.md).

If the prompt and the library disagree, **the library wins**.

Independent Grok Build re-read + execution of ux-compose `80563ab` (2026-09-17):
Night Watch as a house room, shared hearth heat, sky band as Host atmosphere,
loop rail in GET chrome, filament brightening, concentric heat rings.

## Pins

| Package | SHA |
|---|---|
| ux-compose | `030226422ed24c9f5a6d91e249e11cc63dec83c5` |
| ux-dom | `cdb0dd1486e58746c51e98aa51f5fd4d26841196` |
| ux-behavior | `7d46979f59f284bc2d6d961ed372ec849e851dfc` |
| ux-motion | `bbe7d73466a6c1eccb47e711568c80ce3b4d5487` |
| ux-channel | `257adac8d961974fb056622e3c900e9846b28575` `#subdirectory=python` |
| cek-host / cek-surface | `>=0.2.0` (`cek_host.catalog`; 0.1.3 is `cek_host.legal` and does not satisfy) |

License: MIT.
