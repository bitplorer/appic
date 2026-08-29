"""Page unit: health.py → Health. JSON payload door. No Document wrap."""
from __future__ import annotations

from ux_compose import __version__

from settings import UX_COMPOSE_SHA_SHORT

from appic.store import HOST
from appic.ux import Component


class Health(Component):
    id = "health"

    def render(self):
        kit = sorted(HOST.pieces.keys()) if getattr(HOST, "pieces", None) else []
        level = int(getattr(HOST, "level", 0) or 0)
        labels = {
            0: "static + routing",
            1: "offline interactive",
            2: "live channel",
            3: "motion",
        }
        return {
            "ok": True,
            "app": "APPIC",
            "level": level,
            "label": labels.get(level, "offline interactive"),
            "version": __version__,
            "compose": UX_COMPOSE_SHA_SHORT,
            "sealed": True,
            "surfaces": list(kit),
            "kit": [k for k in kit if k in {
                "login","otp","sidebar","breadcrumb","tabs","pullrefresh","accordion",
                "command","toast","typeahead","combobox","select","dropdown","sheet",
                "carousel","table","pagination","contextmenu","actionsheet","stepper",
                "plans","calendar","dialog",
            }],
        }
