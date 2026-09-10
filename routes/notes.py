"""Attach notes refuse silence."""
from __future__ import annotations
from ux_compose import Component, AttachNote, attach_notes, h1, li, p, section, span, ul

class Notes(Component):
    id = "notes"
    def render(self):
        notes = list(attach_notes() or ())
        if not notes:
            notes = [AttachNote(door="boot", wanted="complete install", reason="Python ≥3.14 + pinned specialists", level_kept=1)]
        items = [li(f"{n.door} · {n.wanted} · {n.reason} · L{n.level_kept}") for n in notes]
        return section(
            span("Notes", className="eyebrow"),
            h1("Silence was the defect.", className="display"),
            p("AttachNote is not a message bus. Step-downs are written down.", className="lede"),
            ul(*items, className="mono-list"),
            id=self.id, className="room",
        )
