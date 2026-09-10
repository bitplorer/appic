# APPIC

**Intent. Presence. Caps. Kit. Signal.**

A constitution you can walk. A nocturnal foundry OS authored in
[ux-compose](https://github.com/bitplorer/ux-compose)
`060b583f64512302059bd9d4ff691bb6a2f4dd3a` (0.1.0) — the pure-Python
composition root for ux-dom, ux-behavior, ux-motion, and ux-channel.

No React. No Vue. No JS/TS/TSX as source of truth. Server-authored hypermedia.
Progressive L1→L3 with zero rewrite. Page units have no HTTP verbs. Payload
type picks media type. **The kit is a house you own — 81 stems.** Brand lives
on `wrap=`, never inside `render()`. `/docs` is a product page. FastAPI
Swagger stays off.

The Table is a constellation: rooms as named stars around an Intent nucleus.
Sight is MorphState. Walk is Clock A.

## Run

Python **≥ 3.14**.

```bash
python3.14 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export PYTHONPATH="."
python -m uvicorn app:asgi --host 0.0.0.0 --port 8080
```

Or the product CLI:

```bash
uxcompose serve dev
```

## Walk

| Room | What you touch |
|------|----------------|
| `/` | Table. Hold an Intent. Sight a star. Walk it. |
| `/enter` | Login + OTP. Secrets on RefState. Submit is a Cap. |
| `/house` | All 81 owned kit stems, grouped into wings. `shell=False`. |
| `/atelier` | Market hall — Hero, pricing, marks, quotes, newsletter. |
| `/commission` | Questionnaire + stepper + plans. Finish spends `orders.place`. |
| `/bag` | Cart. Quantity is RefState. Checkout is a Cap. |
| `/forge` | Glaze (named swatches), kiln timer, chart, tree, diff. |
| `/studio` | `role=log` chat, feed, attachments. |
| `/chrome` | Menubar / toolbar APG holds. Caps off chrome. |
| `/overlay` | OverlayChrome family vs anchored family. |
| `/lab` | Open mint vs Cap. JSON pulse. Stream of light. |
| `/docs` | Written constitution. Not Swagger. |
| `/copy` | Ownership ritual. `uxcompose add`. |

## Prompt

The Grok Build metaprompt lives in [`GROK_BUILD_PROMPT.md`](GROK_BUILD_PROMPT.md).
Feature map against ux-compose `main` (`060b583`), inventory 2026-09-10:
[`FEATURE_INVENTORY.md`](FEATURE_INVENTORY.md).

If the prompt and the library disagree, **the library wins**.
