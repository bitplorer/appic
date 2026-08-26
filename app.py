"""APPIC composition root.

Canonical product path: uxcompose serve app:asgi
Host + live set only here (Invisible Strategy). Isolation: no ux_channel import.
"""
from __future__ import annotations

from pathlib import Path

from ux_compose import (
    DirectoryASGI,
    DirectoryRoutes,
    RouterHooks,
    build,
    doctor,
    scan_surfaces,
    validate_surfaces,
)
from ux_compose.build import BuildResult

from appic.server import BUNDLE, UX, asgi as _asgi
from settings import webassets

PACKAGE = Path(__file__).resolve().parent / "appic"

app = UX
asgi = _asgi
bundle = BUNDLE

if asgi is not None and webassets is not None:
    mount = getattr(webassets, "mount_css", None)
    if callable(mount):
        try:
            asgi = mount(asgi)
        except Exception:
            pass

# Evidence that the public names are live (Trace + Lattice also render bundle tables).
_found = scan_surfaces(PACKAGE, base_directory="routes")
validate_surfaces(_found)


def _evidence() -> dict:
    report = doctor([str(PACKAGE)], fail=False, bundle=bundle)
    return {
        "ok": report.ok,
        "level": int(app.level),
        "label": getattr(app.level, "label", ""),
        "surfaces": list((bundle.surfaces or {}) if bundle else []),
        "routes": [r.get("path") for r in (getattr(bundle, "route_table", None) or [])],
        "sealed": getattr(bundle, "sealed", False),
        "directory_routes": DirectoryRoutes.__name__,
        "directory_asgi": DirectoryASGI.__name__,
        "router_hooks": list(RouterHooks.__slots__),
        "build_result": BuildResult.__name__,
        "webassets": getattr(webassets, "css_href", "/css/output.css"),
    }


if __name__ == "__main__":
    print("APPIC", _evidence())
    print("Serve: uxcompose serve app:asgi --host 0.0.0.0 --port 8080")
