# Grok Build prompt — APPIC on ux-compose

Copy everything below the line into Grok Build. Do not use React, Vue, JSX, TSX, or a client SPA runtime. Author the product in Python with **ux-compose**.

---

Build **APPIC**, a stunning nocturnal foundry OS, as a **complete product** (not a widget zoo) using **https://github.com/bitplorer/ux-compose** as the only web UI framework.

## Hard constraints

- **No React / Vue / Svelte / Next / TanStack UI / JSX / TSX / HTMX-as-architecture.** HTMX is opt-in at Document only and must stay off unless explicitly unlocked.
- **All product UI is ux-compose Components.** `render()` returns tag trees (or HTML strings if ux-dom is absent). Behavior is MorphState / RefState / `@action`.
- Isolation Law: product modules **never** `import ux_channel` or CEK. Live path only through `App.use_channel(asgi_app=fastapi)` / `App.use_motion()` / `App.use_cek`.
- Document SSoT: exactly one HTML shell.
- XOR Law + Morph-then-Play: `return update_with(self, scene(...).enter("#id", rise.enter(ms=140)))`. Plans carry **no** `html=`.
- Cap Law: protected verbs fail closed without a Channel-minted Cap. Host mints via `submit_intent(..., mint=True)` at the action door.
- Encoding rule (Channel session plane refuses quantity MorphState):
  - Open / value / query / named step / named band / bool → `MorphState`
  - Magnitude, lists, money, ISO dates, files, digits → `RefState` + `stamp = MorphState("idle")`
  - One-shot message → `notify(...)`
  - Domain stock / money → Host store, never the client plane
- Progressive Superpower: the same Component class is correct at L1 (offline `dispatch`) and L3 (`use_channel` + `use_motion`). Zero rewrite.
- Locked product path: filesystem page units under `routes/` + `App.mount` (stem matches class: `home.py` → `Home`).
- Serve on `0.0.0.0:8080`. Keep Grok `extensions.js` in the shell. Do not hide the Created-with-Grok pill.
- No emoji in chrome. No purple / gold / neon / gradient-blob slop. Sparse monochrome SVG marks.

## Install specialists (progressive)

```
pip install "ux-compose @ git+https://github.com/bitplorer/ux-compose.git"
pip install "ux-behavior @ git+https://github.com/bitplorer/ux-behavior.git"
pip install "ux-motion @ git+https://github.com/bitplorer/ux-motion.git"
pip install "ux-channel @ git+https://github.com/bitplorer/ux-channel.git#subdirectory=python"
# ux-dom needs Python ≥3.14; if absent, HTML strings / local tag kit still L1-correct
pip install fastapi "uvicorn[standard]"
```

Boot:

```python
app = App.boot("APPIC", level="auto", strict_caps=False)
app.use_channel(asgi_app=asgi)
app.use_motion()
app.use_cek(mode="adapt")  # degrade if absent
bundle = app.mount(PACKAGE, asgi_app=asgi, base="routes", fail_closed=False)
```

## Product

**APPIC** — *Intent. Presence. Caps.* A private foundry for commissioning and collecting handmade objects. Dark ink `#0c0d0b`, bone `#ebe6d8`, cool accent `#c8ccd4`. Display **Fraunces**, body **Source Sans 3**, mono **IBM Plex Mono**. Editorial, expensive, abundant negative space, concentric radii.

### Surfaces (all implemented, all live)

1. **Table `/`** — manifesto, pulse MorphState, intent field (holds Host.intent), KPI tiles from Host.
2. **Atelier `/atelier`** — catalog with stable `id="item-{sku}"`, filter query MorphState, sort + `scene.stagger_in`, wishlist, compare (≤3), lightbox, add-to-bag with `scene.share` / rise enter.
3. **Commission `/commission`** — 4-step wizard MorphState covering remaining fields: radio, checkbox set, slider magnitude, date window + ISO RefState, file drop, password reveal, limited note, autosave dirty, OTP digits RefState with **Cap** `identity.verify`, place with **Cap** `orders.place`.
4. **Bag `/bag`** — lines on Host, stepper, coupon **Cap** `orders.coupon` (codes HOUSE/FLAX/TABLE), confirm modal, checkout **Cap** `orders.place`, Morph-then-Play on place.
5. **Board `/board`** — kanban + data table, optimistic move, undo stack, bulk select. Move public; no fake archive without a Cap.
6. **Studio `/studio`** — chat (typing MorphState), inbox unread RefState, presence peers, timeline, moderate **Cap** `comments.moderate`.
7. **Ledger `/ledger`** — calendar named month + day RefState, book **Cap** `calendar.book`, KPI, progress phase, copy, locale/density/motion/consent/offline, doctor capabilities + teaching, wipe **Cap** `settings.wipe`.
8. **Chrome** — command palette (`⌘K`) as first-class intent door, toast plane, line banner. Overlays are Components, not a second Document.

### Control plane

- `control("surface.verb", **args)` → `data-ux-action` + `data-ux-arg-*`
- Prefer `bind(self.verb)` when Behavior is present
- Progressive enhancer JS: POST `/action/{name}`, morph `#surface` with Idiomorph (else outerHTML)
- Full page GET still works without JS
- Action door: Cap-suffixed verbs (`checkout`, `redeem`, `book`, `verify`, `wipe`, `moderate`, `next`) use `submit_intent_async(..., mint=True)`

### Helpers that must appear

`update_with`, `notify`, `control`/`bind`, `morph_play` or `update_with(self, scene(...))`, `tick()` for RefState-only mutations, `maybe_plan` / `maybe_stagger` / `maybe_share` that no-op when `scene is None`.

### Doctor

`/api/doctor` returns level, capabilities, surfaces, routes, teaching. Ledger renders the same evidence. `python -m ux_compose.cli doctor --no-fail` stays green (Isolation scan of product package).

### Quality

- Mobile 390px: no overflow, 44px targets, wrap nav
- Reduced-motion: CSS tokens honor `prefers-reduced-motion`
- Offline banner when Host.online is false; public morphs still run
- Custom `public/og.jpg` 1200×630, `public/favicon.svg` hand-authored, `src/lib/og/site.json` `{ "title": "APPIC", "card": "custom", "color": "0c0d0b" }`
- Publish to GitHub repo **appic** under the connected account (create if missing)

Ship a running foundry, not a gallery of unfinished cards. Every `@action` mutates state and morphs. Caps are real. Motion degrades. Isolation holds.
