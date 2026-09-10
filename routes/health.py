"""Page unit — GET /health. Payload type picks media type: dict → JSON."""
from __future__ import annotations

from ux_compose import Component, HAS_DOM, Level, __version__

from store import HOST


class Health(Component):
    id = "health"

    def render(self):
        kpi = HOST.kpi()
        return {
            "ok": True,
            "name": "APPIC",
            "version": __version__,
            "has_dom": bool(HAS_DOM),
            "level": int(Level.L1),
            "kpi": kpi,
            "clock": "A",
            "payload": "json",
        }
