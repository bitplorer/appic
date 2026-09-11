# APPIC

**A constitution you can walk.**

A nocturnal foundry OS authored in [ux-compose](https://github.com/bitplorer/ux-compose)
`bf55750b5268867aa5931a2171e69ac533808e1e` (0.1.0 — kit-81 + Kit Cut 1 + honesty-locks + Channel FileStateStore). Pure-Python composition root for ux-dom, ux-behavior, ux-motion, and ux-channel.

No React. No Vue. No JS/TS/TSX as source of truth. Server-authored hypermedia.
Page units have no HTTP verbs. Payload type picks media type. **The kit is a house you own — 81 stems, `shell=False`.** Caps are wax seals. GET is Clock A. Action is Clock B (`POST /ux-channel/action`). Brand lives on `wrap=`, never inside `render()`. `/docs` is a product page. FastAPI Swagger stays off.
Channel owns FileStateStore. Doctor `scan_store_clone` fails closed.

The Table is a **constellation**: rooms as named stars around a nucleus.
Sight is MorphState. Walk is Clock A. The verb that sights a star is `look` — never a same-named action, or MorphState is overwritten.

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

## Walk

| Room | Path | Law you can touch |
|---|---|---|
| Table | `/` | Constellation. Sight a star, then walk it |
| Door | `/enter` `/login` `/otp` | Secrets on RefState. Caps on the hinge |
| House | `/house` | Anchored family. Hits-slot law |
| Make | `/commission` | Clay / glaze / fire. `orders.place` |
| Hall | `/market` | Hero, pricing (bind the button), newsletter |
| Forge | `/forge` | Chart, tree, diff, mockup |
| Edge | `/overlay` | OverlayChrome vs anchored family |
| Law | `/docs` | Written constitution. Swagger off |
| Trace | `/trace` | Doctor: hard vs teaching vs store-clone |
| Press | `/copy` | `copy_component`. Not a card |
| Ship | `/deploy` | `prepare_deploy` six providers |
| Health | `/health` | dict → JSON |
| Pulse | `/pulse` | generator → stream |

Every kit stem is also a room (`/dialog`, `/typeahead`, `/menubar`, …).
81 catalog stems + OverlayChrome.

## Prompt

The Grok Build metaprompt lives in [`GROK_BUILD_PROMPT.md`](GROK_BUILD_PROMPT.md).
Copy everything below the line into Grok Build. Feature map against ux-compose `main` (`bf55750`): [`FEATURE_INVENTORY.md`](FEATURE_INVENTORY.md).

If the prompt and the library disagree, **the library wins**.

Independent Grok Build re-read of ux-compose `bf55750` (2026-09-11 honesty-locks): 81 stems counted from `kit/catalog.py`, Command is not OverlayChrome, two walkers / one `build()` door, FileStateStore stays on Channel, public `__all__` lock covers host/surface/motion names.

## Pins

| Package | SHA |
|---|---|
| ux-compose | `bf55750b5268867aa5931a2171e69ac533808e1e` |
| ux-dom | `e8be99a52bfecd6026c200fa1c3dc6a74f87aacb` |
| ux-behavior | `793f120e3b1388925772cd069b070d7918b78baa` |
| ux-motion | `67ff3f0c4912b70b7056f8226a6f226b6fe93f60` |
| ux-channel | `d0fe7169e687d2935f8b74d40b990b1ee63ef3d4` `#subdirectory=python` |
| cek-host / cek-surface | `>=0.1.3` |

License: MIT.
