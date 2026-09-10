"""Health as a page unit (HTML). JSON lives at GET /health from the host."""
from __future__ import annotations

from ux_compose import Component, a, h1, p, section, span
from ux_compose import __version__


class Health(Component):
    id = "health"

    def render(self):
        return section(
            span("probe", className="kicker"),
            h1("Health"),
            p(f"ux-compose {__version__}. JSON probe is GET /health on the host, not this fragment.", className="lede"),
            a("JSON health", href="/health", className="btn-ghost"),
            id=self.id,
            className="page",
        )
