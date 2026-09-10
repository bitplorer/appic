"""Page unit — GET /pulse. Generator → stream of light."""
from __future__ import annotations

from ux_compose import Component, __version__

from store import HOST


class Pulse(Component):
    id = "pulse"

    def render(self):
        kpi = HOST.kpi()

        def chunks():
            yield f"APPIC pulse stream  version={__version__}\n"
            yield f"pulse={kpi['pulse']} bag={kpi['bag']} seals={kpi['seals']}\n"
            yield "clock=A payload=stream\n"

        return chunks()
