# APPIC

A nocturnal foundry OS authored entirely in **[ux-compose](https://github.com/bitplorer/ux-compose)**. No React. No Vue. No client runtime as source of truth.

Product intent becomes legal **Results of Ops**. The document morphs. Caps gate the verbs that charge.

## What it is

APPIC is a working atelier: catalog, bag, commissions, kanban board, studio, and ledger. Every surface is one `Component` with `MorphState` / `RefState` / `@action`. The same classes are valid offline (L1) and live with Channel + Motion (L3).

| Surface | What to try |
|---|---|
| Table `/` | Pulse the house. Hold an intent. |
| Atelier `/atelier` | Filter, sort (stagger), save, compare, look, add to bag. |
| Commission `/commission` | Four-step wizard: fields, OTP Cap, place Cap. |
| Bag `/bag` | Stepper, coupon Cap (`HOUSE`), review, checkout Cap. |
| Board `/board` | Move cards, undo, table bulk. |
| Studio `/studio` | Chat, typing presence, moderate Cap. |
| Ledger `/ledger` | Book a bench (Cap), doctor, wipe (Cap). |
| Command `⌘K` | Issue intents without leaving the table. |

## Laws kept

- **Isolation** — product modules never import `ux_channel` or CEK
- **Document SSoT** — one HTML shell
- **XOR / Morph-then-Play** — `update_with(self, scene(...))`, Plans carry no `html=`
- **Cap Law** — protected verbs mint through `App.submit_intent`
- **Encoding** — qualitative MorphState; magnitudes on RefState + stamp
- **Progressive Superpower** — L1 code unchanged at L3

## Run

```bash
python3.11 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=vendor/ux-compose-src:. uvicorn appic.server:app --host 0.0.0.0 --port 8080
```

Python ≥3.11 recommended (ux-compose). Level 1 offline still boots if Channel/Motion are absent.

```bash
python -m ux_compose.cli doctor --no-fail
```
