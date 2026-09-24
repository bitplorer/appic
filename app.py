"""APPIC composition root.

host + live set only in build(). Isolation: no ux_channel import.
"""
from __future__ import annotations

from pathlib import Path

from starlette.staticfiles import StaticFiles
from starlette.responses import FileResponse

from ux_compose.build import build
from ux_compose import doctor
from ux_compose.brand import brand_wrap, GET_BRAND_ATTR, DEFAULT_BRAND

from chrome import foundry_wrap
from document import document
from settings import webassets, PUBLIC_DIR

PACKAGE = Path(__file__).resolve().parent


def _mount_css(asgi):
    if asgi is None or webassets is None:
        return asgi
    mount = getattr(webassets, "mount_css", None)
    if callable(mount):
        return mount(asgi)
    return asgi


def _mount_public(asgi):
    if asgi is None:
        return asgi
    public = Path(PUBLIC_DIR)
    public.mkdir(parents=True, exist_ok=True)
    grok = public / "__grok"
    if grok.is_dir():
        try:
            asgi.mount("/__grok", StaticFiles(directory=str(grok)), name="grok")
        except Exception:
            pass
    try:
        asgi.mount("/media", StaticFiles(directory=str(public), check_dir=False), name="media")
    except Exception:
        pass
    og = public / "og.jpg"
    fav = public / "favicon.svg"
    if og.is_file() and hasattr(asgi, "add_api_route"):
        asgi.add_api_route(
            "/og.jpg",
            lambda: FileResponse(str(og), media_type="image/jpeg"),
            methods=["GET"],
            include_in_schema=False,
        )
    if fav.is_file() and hasattr(asgi, "add_api_route"):
        asgi.add_api_route(
            "/favicon.svg",
            lambda: FileResponse(str(fav), media_type="image/svg+xml"),
            methods=["GET"],
            include_in_schema=False,
        )
    return asgi


def main(*, use_htmx: bool = False):
    # Evidence that brand_wrap exists; foundry_wrap is the product GET chrome.
    _ = brand_wrap, GET_BRAND_ATTR, DEFAULT_BRAND
    app, asgi, bundle = build(
        PACKAGE,
        name="APPIC",
        host="auto",
        live="auto",
        level="auto",
        base="routes",
        use_htmx=use_htmx,
        document=document,
        wrap=foundry_wrap(document, brand="APPIC"),
        cek="require",
        openapi=False,
    )
    asgi = _mount_css(asgi)
    asgi = _mount_public(asgi)
    return app, asgi, bundle


if __name__ == "__main__":
    app, asgi, bundle = main()
    print("Level:", int(app.level), f"({app.level.label})")
    print("Host ASGI:", type(asgi).__name__ if asgi is not None else None)
    print("Surfaces:", list((bundle.surfaces or {}).keys()) if bundle else [])
    print("Routes:", [r.get("path") for r in (bundle.route_table or [])] if bundle else [])
    report = doctor(
        [str(PACKAGE / "routes"), str(PACKAGE / "chrome.py"), str(PACKAGE / "app.py")],
        fail=False,
        bundle=bundle,
        app=app,
    )
    print("Doctor ok:", report.ok)
    if asgi is not None:
        print("Path: uvicorn app:asgi --host 0.0.0.0 --port 8080")

_app, asgi, _bundle = main()
UX = _app
BUNDLE = _bundle
