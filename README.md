# APPIC

**Intent. Presence. Caps.**

A nocturnal foundry OS authored in [ux-compose](https://github.com/bitplorer/ux-compose) — the pure-Python composition root for ux-dom, ux-behavior, ux-motion, and ux-channel.

No React. No Vue. No client runtime as source of truth. Server-authored hypermedia. Progressive L1→L3 with zero rewrite.

![APPIC](public/og.jpg)

Open the table. Issue an intent (`⌘K`). Watch the document morph. Protected verbs mint Caps. Open **Trace** to see Ops as data.

## Surfaces

| Surface | What to try |
|---|---|
| Table `/` | Pulse the house. Hold an intent. Presence. |
| Atelier `/atelier` | Filter, sort, save, compare, look, add to bag. |
| Commission `/commission` | Four-step wizard. OTP `2048` is a Cap. Place is a Cap. |
| Bag `/bag` | Stepper, coupon Cap (`HOUSE` / `FLAX` / `TABLE`), review, checkout Cap. |
| Board `/board` | Move cards, undo, table bulk. |
| Studio `/studio` | Chat, typing presence, moderate Cap. |
| Lab `/lab` | Remaining 99%: tree, carousel, reorder, empty-retry, chips, inline, combobox, accordion, drawer, Morph-then-Play, share. |
| Trace `/trace` | Live Ops log. Doctor. Isolation. Shortcuts. |
| Ledger `/ledger` | Book a bench (Cap), doctor, wipe (Cap). |
| Command `⌘K` | Issue intents without leaving the table. |

## Laws kept

- **Isolation** — product modules never import `ux_channel` or CEK
- **Document SSoT** — one HTML shell
- **XOR / Morph-then-Play** — `update_with(self, scene(...))`, Plans carry no `html=`
- **Cap Law** — checkout, book, redeem, wipe, verify, moderate mint through `App.mint_cap`
- **Encoding** — qualitative MorphState; magnitudes on RefState + stamp
- **Progressive Superpower** — L1 code unchanged at L3

## Run

Python ≥3.10. `ux-dom` wants 3.14; APPIC keeps the same tag call shape without it.

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=vendor/ux-compose-src:. uvicorn appic.server:app --host 0.0.0.0 --port 8080
```

Doctor: `GET /api/doctor`. Health: `GET /api/health`.

```bash
PYTHONPATH=vendor/ux-compose-src:. python -m ux_compose.cli doctor appic --no-fail
```

## Prompt

The Grok Build prompt that specifies this product — full ux-compose inventory: [GROK_BUILD_PROMPT.md](GROK_BUILD_PROMPT.md).
