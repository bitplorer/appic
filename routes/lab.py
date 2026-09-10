"""Lab — probe matrix. Never shells. Never starts a server."""
from __future__ import annotations
from ux_compose import Component, h1, li, p, section, span, ul
from ux_compose.dx.probe import probe

class Lab(Component):
    id = "lab"
    def render(self):
        result = probe()
        specs = [li(f"{k}: {'yes' if v else 'no'}") for k, v in (result.specialists or {}).items()]
        clis = [li(f"{k}: {v or '—'}") for k, v in (result.clis or {}).items()]
        return section(
            span("Lab", className="eyebrow"),
            h1("Probe never shells.", className="display"),
            p("Import-spec only. Incomplete install is fail-loud.", className="lede"),
            ul(*specs, *clis, className="mono-list"),
            id=self.id, className="room",
        )
