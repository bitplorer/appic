"""APPIC composition root.

Product path: build(document=, wrap=, host=auto, live=auto, cek=require).
Page units under routes/. Isolation Law: this module never imports ux_channel.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlparse

from ux_compose import doctor
from ux_compose.build import build
from ux_compose.chrome import brand_wrap  # public GET chrome helper (also used on /trace)

from chrome import foundry_wrap
from document import document
from foundry import bind as bind_app
from owned import register_kits
from settings import BASE_DIR, BRAND, OPENAPI, webassets

PACKAGE = Path(__file__).resolve().parent
PUBLIC = PACKAGE / "public"
STATIC = PACKAGE / "appic_static"
_IDENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_.]*$")


def _clean_args(args: dict[str, Any]) -> dict[str, Any]:
    clean: dict[str, Any] = {}
    for k, v in (args or {}).items():
        if not isinstance(k, str) or not _IDENT.match(k):
            continue
        if k in {"action", "submit"}:
            continue
        if isinstance(v, (list, tuple)):
            v = v[0] if v else ""
        clean[k] = v
    return clean


async def _parse_action_args(request: Any) -> dict[str, Any]:
    ctype = (request.headers.get("content-type") or "").lower()
    raw = await request.body()
    if "application/json" in ctype:
        try:
            body = await request.json()
            return _clean_args(body if isinstance(body, dict) else {})
        except Exception:
            return {}
    parsed = parse_qs(raw.decode("utf-8", errors="replace"), keep_blank_values=True)
    return _clean_args({k: v[0] if v else "" for k, v in parsed.items()})


def _mount_static(asgi):
    if asgi is None:
        return asgi
    try:
        from starlette.staticfiles import StaticFiles
    except ImportError:
        return asgi
    css_dir = getattr(getattr(webassets, "static", None), "css", None)
    if css_dir is not None:
        Path(str(css_dir)).mkdir(parents=True, exist_ok=True)
        asgi.mount("/css", StaticFiles(directory=str(css_dir), check_dir=False), name="css")
    static_dir = PACKAGE / "static"
    static_dir.mkdir(parents=True, exist_ok=True)
    asgi.mount("/static", StaticFiles(directory=str(static_dir), check_dir=False), name="static")
    if PUBLIC.exists():
        grok = PUBLIC / "__grok"
        if grok.exists():
            asgi.mount("/__grok", StaticFiles(directory=str(grok), check_dir=False), name="grok")
    return asgi


def _wire_doors(app, asgi):
    if asgi is None or not hasattr(asgi, "post"):
        return asgi

    from fastapi import Request
    from fastapi.responses import FileResponse, JSONResponse, StreamingResponse

    @asgi.get("/healthz")
    async def health():
        notes = []
        try:
            snap = app.attach_notes()
            notes = [getattr(n, "door", str(n)) for n in (snap or ())]
        except Exception:
            notes = []
        return {
            "ok": True,
            "brand": BRAND,
            "level": int(getattr(app, "level", 1) or 1),
            "version": __import__("ux_compose").__version__,
            "attach_notes": notes,
            "kit": len(getattr(app, "_kit_registry", {}) or {}),
        }

    @asgi.get("/pulse.json")
    async def pulse_json():
        """Clock A JSON payload — media type is the return type, not Accept."""
        from store import HOST

        return {
            "kind": "pulse",
            "bag": HOST.bag_count(),
            "commissions": len(HOST.commissions),
            "authed": HOST.authed,
        }

    @asgi.get("/stream")
    async def stream_light():
        async def gen():
            yield "<!doctype html><html><body><pre>"
            for line in ("intent", "cap", "result", "morph", "presence"):
                yield f"{line}\n"
            yield "</pre></body></html>"

        return StreamingResponse(gen(), media_type="text/html; charset=utf-8")

    @asgi.get("/favicon.svg")
    async def favicon():
        path = PUBLIC / "favicon.svg"
        if path.exists():
            return FileResponse(str(path), media_type="image/svg+xml")
        return JSONResponse({"error": "missing"}, status_code=404)

    @asgi.get("/og.jpg")
    async def og_jpg():
        path = PUBLIC / "og.jpg"
        if path.exists():
            return FileResponse(str(path), media_type="image/jpeg")
        return JSONResponse({"error": "missing"}, status_code=404)

    async def _run_action(name: str, request: Request):
        args = await _parse_action_args(request)
        action_name = name
        if "." not in action_name:
            try:
                ref = urlparse(request.headers.get("referer") or "/").path
                stem = (ref.rstrip("/") or "/").split("/")[-1] or "index"
                if stem in ("", "/"):
                    stem = "index"
                action_name = f"{stem}.{name}"
            except Exception:
                action_name = name
        sealed = dict(args)
        cap = sealed.pop("cap", None) or sealed.pop("data-channel-cap", None)
        try:
            if cap:
                await app.submit_intent_async(action_name, cap=cap, args=sealed)
            else:
                app.dispatch(action_name, **sealed)
        except Exception as exc:
            return JSONResponse({"ok": False, "error": str(exc)}, status_code=400)
        return JSONResponse({"ok": True, "action": action_name})

    @asgi.post("/act/{name:path}")
    async def act_door(name: str, request: Request):
        return await _run_action(name, request)

    @asgi.post("/action/{name:path}")
    async def action_door(name: str, request: Request):
        return await _run_action(name, request)

    return asgi


def main(*, use_htmx: bool = False):
    wrap = foundry_wrap(document, brand=BRAND)
    # brand_wrap is the library door — kept imported so /trace can show it as law.
    _ = brand_wrap
    app, asgi, bundle = build(
        PACKAGE,
        name=BRAND,
        host="auto",
        live="auto",
        level="auto",
        base="routes",
        use_htmx=use_htmx,
        document=document,
        wrap=wrap,
        cek="require",
        openapi=OPENAPI,
        fail_closed=False,
    )
    bind_app(app)
    register_kits(app)
    asgi = _mount_static(asgi)
    asgi = _wire_doors(app, asgi)
    app._foundry_wrap = wrap
    app._foundry_bundle = bundle
    report = doctor([], fail=False, bundle=bundle, app=app)
    app._doctor = report
    return app, asgi, bundle


if __name__ == "__main__":
    app, asgi, bundle = main()
    print("Level:", int(app.level), f"({app.level.label})")
    print("Surfaces:", list(bundle.surfaces.keys()) if bundle else [])
    print("Routes:", [r.get("path") for r in (bundle.route_table or [])] if bundle else [])
    print("Kit:", len(getattr(app, "_kit_registry", {}) or {}))

_app, asgi, _bundle = main()
