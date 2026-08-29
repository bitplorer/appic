"""APPIC host — ux-compose product path.

Page units under routes/ via App.mount. Document SSoT in this shell.
Isolation Law: never imports ux_channel. Caps mint through App.submit_intent.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlparse

from appic.chrome import Banner, Palette, Ribbon, Toasts
from appic.marks import logo
from appic.owned import KIT_CLASSES
from appic.store import HOST
from appic.tags import _child
from appic.ux import App, doctor

PACKAGE = Path(__file__).resolve().parent
STATIC = PACKAGE / "static"
PUBLIC = Path(__file__).resolve().parents[1] / "public"
NAV = (
    ("/", "Table"),
    ("/enter", "Door"),
    ("/desk", "Desk"),
    ("/house", "House"),
    ("/visit", "Visit"),
    ("/signal", "Signal"),
    ("/atelier", "Atelier"),
    ("/bag", "Bag"),
    ("/lattice", "Lattice"),
    ("/trace", "Trace"),
    ("/clocks", "Clocks"),
)

try:
    from fastapi import FastAPI, Request
    from fastapi.responses import FileResponse, HTMLResponse, JSONResponse, StreamingResponse
    from fastapi.staticfiles import StaticFiles

    HAS_FASTAPI = True
except ImportError:  # pragma: no cover
    HAS_FASTAPI = False
    FastAPI = None  # type: ignore

_IDENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
_CAP_SUFFIXES = (
    "checkout",
    "redeem",
    "book",
    "verify",
    "wipe",
    "moderate",
    "next",
    "place",
    "reset",
    "mint",
    "sell",
    "login",
    "signup",
    "finish",
    "archive",
    "pick",
    "submit",
)


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


def _page_for_path(path: str) -> str:
    p = (path or "/").rstrip("/") or "/"
    mapping = {
        "/": "home",
        "/home": "home",
        "/atelier": "atelier",
        "/commission": "commission",
        "/bag": "bag",
        "/board": "board",
        "/studio": "studio",
        "/lab": "lab",
        "/lattice": "lattice",
        "/trace": "trace",
        "/ledger": "ledger",
        "/settings": "ledger",
        "/sku": "sku",
        "/enter": "enter",
        "/desk": "desk",
        "/house": "house",
        "/visit": "visit",
        "/signal": "signal",
        "/clocks": "clocks",
        "/health": "health",
        "/pulse": "pulse",
        "/commission": "commission",
        "/lab": "lab",
        "/studio": "studio",
        "/board": "board",
    }
    if p in mapping:
        return mapping[p]
    for href, sid in (
        ("/atelier", "atelier"),
        ("/commission", "commission"),
        ("/bag", "bag"),
        ("/board", "board"),
        ("/studio", "studio"),
        ("/lab", "lab"),
        ("/lattice", "lattice"),
        ("/trace", "trace"),
        ("/ledger", "ledger"),
        ("/enter", "enter"),
        ("/desk", "desk"),
        ("/house", "house"),
        ("/visit", "visit"),
        ("/signal", "signal"),
        ("/clocks", "clocks"),
    ):
        if p.startswith(href):
            return sid
    return "home"


def _serialize(tree: Any) -> str:
    if tree is None:
        return ""
    if isinstance(tree, str):
        return tree
    return _child(tree)


def _instance(app: App, surface_id: str):
    behavior = getattr(app, "_behavior", None) or getattr(app, "behavior", None)
    if behavior is not None and hasattr(behavior, "components"):
        try:
            inst = dict(behavior.components()).get(surface_id)
            if inst is not None:
                return inst
        except Exception:
            pass
    return (getattr(app, "_registry", {}) or {}).get(surface_id)


def _invoke(app: App, action_name: str, args: dict[str, Any] | None = None) -> None:
    """Call the bound @action with HTTP args. BoundAction.__call__ keeps kwargs.

    Behavior.dispatch uses bind_action_args on BoundAction(*args, **kwargs),
    which nests named HTTP args under a kwargs dict and silently drops them.
    """
    args = dict(args or {})
    if "." not in action_name:
        return
    cid, meth = action_name.split(".", 1)
    inst = _instance(app, cid)
    if inst is None:
        return
    fn = getattr(inst, meth, None)
    if not callable(fn):
        return
    try:
        fn(**args)
        suffix = action_name.rsplit(".", 1)[-1]
        kind = "cap" if suffix in _CAP_SUFFIXES else "morph"
        HOST.log(action_name, " ".join(f"{k}={v}" for k, v in list(args.items())[:3]), kind)
    except TypeError as exc:
        msg = str(exc)
        if args and ("unexpected keyword" in msg or "positional" in msg):
            fn()
            HOST.log(action_name, "", "morph")


def _mint(app: App, action_name: str, args: dict[str, Any] | None = None) -> None:
    """Mint a Channel Cap at the HTTP door. Isolation: product never imports Channel."""
    if not hasattr(app, "mint_cap"):
        return
    try:
        app.mint_cap(action_name, dict(args or {}))
    except Exception:
        pass


def _render_surface(app: App, surface_id: str) -> str:
    inst = _instance(app, surface_id)
    if inst is None:
        return f'<p class="muted">Surface {surface_id!r} is not mounted.</p>'
    return _serialize(inst.render())


def _shell(app: App, main_html: str, *, path: str = "/") -> str:
    nav = []
    for href, label in NAV:
        current = path.rstrip("/") == href.rstrip("/") or (
            href != "/" and path.startswith(href)
        )
        if href == "/" and path in ("/", "/home", ""):
            current = True
        cls = ' class="is-current"' if current else ""
        aria = ' aria-current="page"' if current else ""
        extra = ""
        if href == "/bag":
            extra = f' <span class="bag-count" data-bag-count>{HOST.count()}</span>'
        nav.append(f'<a href="{href}"{cls}{aria}>{label}{extra}</a>')
    banner = _render_surface(app, "banner")
    palette = _render_surface(app, "palette")
    toasts = _render_surface(app, "toasts")
    ribbon = _render_surface(app, "ribbon")
    mark = _serialize(logo())
    crumbs = []
    crumbs.append('<a href="/">Table</a>')
    here = next((lab for href, lab in NAV if href != "/" and path.startswith(href)), None)
    if here:
        crumbs.append(f'<span class="crumb-sep">/</span><span>{here}</span>')
    crumb_html = f'<nav class="crumbs" aria-label="Breadcrumb">{"".join(crumbs)}</nav>'
    bottom = []
    for href, label in (("/", "Table"), ("/house", "House"), ("/enter", "Door"), ("/signal", "Signal"), ("/trace", "Trace")):
        current = path.rstrip("/") == href.rstrip("/") or (href != "/" and path.startswith(href))
        if href == "/" and path in ("/", "/home", ""):
            current = True
        cls = ' class="is-current"' if current else ""
        bottom.append(f'<a href="{href}"{cls}>{label}</a>')
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>APPIC · Intent · Presence · Caps · Kit</title>
  <meta name="description" content="A foundry OS authored in ux-compose. Intent. Presence. Caps. Ownable kit. Signal." />
  <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  <link rel="apple-touch-icon" href="/__grok/icon-180.png" />
  <meta property="og:title" content="APPIC · Intent · Presence · Caps" />
  <meta property="og:description" content="A foundry OS authored in ux-compose. Intent becomes legal Results of Ops." />
  <meta property="og:image" content="/og.jpg" />
  <meta name="theme-color" content="#0c0d0b" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Source+Sans+3:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/static/css/appic.css" />
  <link rel="stylesheet" href="/static/css/kit.css" />
  <script src="https://grok.com/grok-app-builder/extensions.js" defer></script>
</head>
<body class="density-{HOST.density} motion-{HOST.motion}">
  <div class="frame">
    <header class="top">
      <a class="brand" href="/">{mark}<span>APPIC</span></a>
      <nav class="nav">{''.join(nav)}</nav>
      <div class="top-tools">
        <button type="button" class="btn btn-ghost" data-ux-action="palette.toggle">Command <span class="kbd">⌘K</span></button>
      </div>
    </header>
    {banner}
    {ribbon}
    {crumb_html}
    <main id="main">{main_html}</main>
    <nav class="bottom-nav" aria-label="Primary">{''.join(bottom)}</nav>
    <footer class="foot">
      <span>ux-compose · f0b8da50 · ownable kit · Signal · Morph then Play · Isolation Law · Caps</span>
      <span class="mono">L{int(getattr(app, 'level', 0))} · bag {HOST.count()}</span>
    </footer>
  </div>
  {palette}
  {toasts}
  <div id="seal-burst" class="seal-burst" hidden>
    <div class="seal-ring" aria-hidden="true"></div>
    <p class="seal-label mono">Cap minted</p>
  </div>
  <script src="/static/vendor/idiomorph.min.js" defer></script>
  <script src="/static/js/appic.js" defer></script>
</body>
</html>"""


def build():
    asgi = FastAPI(title="APPIC") if HAS_FASTAPI else None
    app = App.boot("APPIC", level="auto", strict_caps=False)
    try:
        if asgi is not None:
            app.use_channel(asgi_app=asgi)
        else:
            app.use_channel()
    except Exception:
        pass
    try:
        app.use_motion()
    except Exception:
        pass
    try:
        app.use_cek(mode="adapt")
    except Exception:
        pass

    bundle = app.mount(
        PACKAGE,
        asgi_app=asgi,
        base="routes",
        fail_closed=False,
        include_directory_router=False,
    )
    app.add(Toasts, Palette, Banner, Ribbon)
    try:
        app.add(*KIT_CLASSES)
    except Exception:
        for cls in KIT_CLASSES:
            try:
                app.add(cls)
            except Exception:
                pass
    Sku = None
    try:
        import importlib.util

        sku_path = PACKAGE / "routes" / "atelier" / "[sku].py"
        spec = importlib.util.spec_from_file_location("appic_routes_sku", sku_path)
        if spec and spec.loader:
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            Sku = getattr(mod, "Sku", None)
            if Sku is not None:
                app.add(Sku)
    except Exception:
        Sku = None
    extras = [Toasts, Palette, Banner, Ribbon, *list(KIT_CLASSES)]
    if Sku is not None:
        extras.append(Sku)
    registry = dict(bundle.unit_registry or {})
    for extra in extras:
        sid = extra.id
        inst = _instance(app, sid)
        if inst is None:
            try:
                inst = extra()
            except Exception:
                inst = None
        if inst is not None:
            registry[sid] = inst
    app._registry = registry
    app._bundle = bundle
    HOST.pieces = dict(registry)
    HOST.level = int(getattr(app, "level", 0) or 0)

    if asgi is None:
        return app, None, bundle

    if STATIC.exists():
        asgi.mount("/static", StaticFiles(directory=str(STATIC)), name="static")

    grok_dir = PUBLIC / "__grok"
    if grok_dir.exists():
        asgi.mount("/__grok", StaticFiles(directory=str(grok_dir)), name="grok")

    @asgi.get("/favicon.svg")
    def favicon():
        path = PUBLIC / "favicon.svg"
        if path.exists():
            return FileResponse(str(path), media_type="image/svg+xml")
        return HTMLResponse("<svg xmlns='http://www.w3.org/2000/svg'/>")

    @asgi.get("/og.jpg")
    def og_jpg():
        path = PUBLIC / "og.jpg"
        if path.exists():
            return FileResponse(str(path), media_type="image/jpeg")
        return HTMLResponse("missing", status_code=404)

    @asgi.get("/health")
    def health_door():
        inst = _instance(app, "health")
        payload = inst.render() if inst is not None else {"ok": False}
        return JSONResponse(payload)

    @asgi.get("/pulse")
    def pulse_door():
        inst = _instance(app, "pulse")
        if inst is None:
            return HTMLResponse("missing pulse", status_code=404)

        def gen():
            tree = inst.render()
            if hasattr(tree, "__iter__") and not isinstance(tree, (str, bytes, dict)):
                for chunk in tree:
                    yield str(chunk)
            else:
                yield str(tree)

        return StreamingResponse(gen(), media_type="text/html; charset=utf-8")


    @asgi.get("/")
    @asgi.get("/home")
    @asgi.get("/atelier")
    @asgi.get("/commission")
    @asgi.get("/bag")
    @asgi.get("/board")
    @asgi.get("/studio")
    @asgi.get("/lab")
    @asgi.get("/lattice")
    @asgi.get("/trace")
    @asgi.get("/ledger")
    @asgi.get("/settings")
    @asgi.get("/enter")
    @asgi.get("/desk")
    @asgi.get("/house")
    @asgi.get("/visit")
    @asgi.get("/signal")
    @asgi.get("/clocks")
    async def pages(request: Request):
        path = request.url.path
        sid = _page_for_path(path)
        inner = _render_surface(app, sid)
        return HTMLResponse(_shell(app, inner, path=path))

    @asgi.get("/atelier/{sku}")
    async def sku_page(sku: str, request: Request):
        inst = _instance(app, "sku")
        if inst is not None and hasattr(inst, "show"):
            try:
                inst.show(sku=sku)
            except Exception:
                pass
        inner = _render_surface(app, "sku")
        return HTMLResponse(_shell(app, inner, path=f"/atelier/{sku}"))

    @asgi.get("/css/output.css")
    def css_output():
        from pathlib import Path as _P

        candidates = [
            PACKAGE / "static" / "css" / "appic.css",
            _P(__file__).resolve().parents[1] / "assets" / "static" / "file" / "css" / "output.css",
        ]
        for path in candidates:
            if path.exists():
                return FileResponse(str(path), media_type="text/css")
        return HTMLResponse("/* missing */", status_code=404)


    @asgi.post("/action/{name:path}")
    async def action_door(name: str, request: Request):
        args = await _parse_action_args(request)
        action_name = name
        if "." not in action_name:
            ref_path = urlparse(request.headers.get("referer") or "/").path
            action_name = f"{_page_for_path(ref_path)}.{name}"
        verb = args.get("verb") if action_name.endswith("palette.run") else None
        try:
            suffix = action_name.rsplit(".", 1)[-1]
            if suffix in _CAP_SUFFIXES:
                _mint(app, action_name, args)
            _invoke(app, action_name, args)
            if verb:
                v_suffix = str(verb).rsplit(".", 1)[-1]
                if v_suffix in _CAP_SUFFIXES:
                    _mint(app, str(verb), {})
                _invoke(app, str(verb), {})
        except Exception as exc:
            return HTMLResponse(
                f'<p class="muted">Action error: {exc}</p>',
                status_code=400,
            )

        ref_path = "/"
        try:
            ref_path = urlparse(request.headers.get("referer") or "/").path or "/"
        except Exception:
            pass
        sid = action_name.split(".", 1)[0] if "." in action_name else _page_for_path(ref_path)
        if verb:
            sid = _page_for_path(ref_path)
        inner = _render_surface(app, sid)
        target_sel = f"#{sid}"
        inst = _instance(app, sid)
        if action_name.endswith(".query_hits") and inst is not None:
            listing = getattr(inst, "_listing", None)
            if callable(listing):
                inner = _serialize(listing())
                target_sel = f"#{sid}-hits"
        hx = request.headers.get("hx-request") or request.headers.get("x-appic-morph")
        suffix = action_name.rsplit(".", 1)[-1]
        kind = "cap" if suffix in _CAP_SUFFIXES else "morph"
        headers = {
            "X-Appic-Bag": str(HOST.count()),
            "X-Appic-Surface": sid,
            "X-Appic-Kind": kind,
            "X-Appic-Op": action_name,
            "X-Appic-Target": target_sel,
        }
        if hx:
            return HTMLResponse(inner, headers=headers)
        page_sid = sid if sid not in {"palette", "toasts", "banner", "ribbon"} else _page_for_path(ref_path)
        if hx:
            return HTMLResponse(inner, headers=headers)
        page_sid = sid if sid not in {"palette", "toasts", "banner"} else _page_for_path(ref_path)
        page_html = inner if page_sid == sid else _render_surface(app, page_sid)
        return HTMLResponse(_shell(app, page_html, path=ref_path), headers=headers)
    @asgi.get("/api/doctor")
    def api_doctor():
        report = doctor([], fail=False, bundle=getattr(app, "_bundle", None))
        return {
            "ok": report.ok,
            "level": report.level_available,
            "capabilities": report.capabilities,
            "surfaces": report.surfaces,
            "routes": report.routes,
            "teaching": report.teaching,
            "diagnostics": report.diagnostics,
        }

    @asgi.get("/api/health")
    def health():
        return {
            "app": "APPIC",
            "level": int(app.level),
            "label": getattr(app.level, "label", ""),
            "surfaces": list(getattr(app, "_registry", {}).keys()),
            "bag": HOST.count(),
            "fastapi": True,
            "seal": HOST.last_seal,
            "ops": len(HOST.trace),
        }

    @asgi.get("/api/surfaces")
    def api_surfaces():
        b = getattr(app, "_bundle", None)
        return {
            "surfaces": list((getattr(b, "surfaces", None) or {}).keys()) if b else list(getattr(app, "_registry", {}).keys()),
            "route_table": list(getattr(b, "route_table", None) or []),
            "action_table": list(getattr(b, "action_table", None) or [])[:80],
            "unit_registry": list((getattr(b, "unit_registry", None) or {}).keys()) if b else [],
            "sealed": bool(getattr(b, "sealed", False)),
            "errors": list(getattr(b, "errors", None) or []),
        }

    @asgi.get("/api/kit")
    def api_kit():
        stems = sorted(HOST.pieces.keys()) if getattr(HOST, "pieces", None) else []
        owned = [c.id for c in KIT_CLASSES]
        return {
            "owned": owned,
            "mounted": stems,
            "count": len(owned),
            "sha": "f0b8da50",
        }

    return app, asgi, bundle


UX, asgi, BUNDLE = build()
app = asgi


if __name__ == "__main__":
    print("APPIC · ux-compose")
    print("  Level:", int(UX.level), getattr(UX.level, "label", ""))
    print("  Surfaces:", list(getattr(UX, "_registry", {}).keys()))
    if asgi is not None:
        print("  Serve: uvicorn appic.server:app --host 0.0.0.0 --port 8080")
    else:
        print("  Offline", UX.dispatch("home.beat"))
