"""Ledger — Caps as seals."""
from __future__ import annotations
from ux_compose import Component, div, h1, p, section, span
from store import HOST

class Ledger(Component):
    id = "ledger"
    def render(self):
        rows = [
            div(span(r.get("at",""), className="mono"), span(r.get("kind",""), className="chip"), span(r.get("verb",""), className="mono"), className="cap-row")
            for r in reversed(HOST.ledger[-16:])
        ] or [p("No seals spent yet.", className="muted")]
        return section(
            span("Ledger", className="eyebrow"),
            h1("Every spent seal leaves a trace.", className="display"),
            p("Host DB, never the client plane. Protected verbs mint once when it matters.", className="lede"),
            div(*rows, className="stack"),
            id=self.id, className="room",
        )
