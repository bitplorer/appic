"""Board — table of commissions as a floor."""
from __future__ import annotations

from ux_compose import Component, h1, p, section, span, table, tbody, td, th, thead, tr

from store import HOST


class Board(Component):
    id = "board"

    def render(self):
        if HOST.commissions:
            rows = [
                tr(td(r.get("clay", "")), td(r.get("glaze", "")), td(r.get("note", "") or "—"))
                for r in HOST.commissions
            ]
        else:
            rows = [tr(td("No commissions"), td("—"), td("—"))]
        return section(
            span("Board", className="eyebrow"),
            h1("The floor is a table.", className="display"),
            p("Native table tags are in __all__. Kit Table is a different room.", className="lede"),
            table(thead(tr(th("Clay"), th("Glaze"), th("Note"))), tbody(*rows), className="plain-table"),
            id=self.id,
            className="room",
        )
