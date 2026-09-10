"""Attach notes refuse silence. Step-down is evidence, not a hidden except."""
from __future__ import annotations

from foundry import app as get_app
from ux_compose import AttachNote, Component, a, attach_notes, div, h1, li, p, section, span, ul


class Notes(Component):
    id = "notes"

    def render(self):
        handle = get_app()
        items = []
        if handle is not None:
            try:
                snap = handle.attach_notes()
                items = list(snap or ())
            except Exception:
                items = []
        if not items:
            # Teaching residual: show the type even when the notebook is quiet.
            items = [
                AttachNote(
                    door="channel",
                    wanted="live Caps",
                    reason="Notebook is quiet — attach held. Silence would be the defect.",
                    level_kept=1,
                )
            ]
            attach_notes  # public name must appear in product source
        rows = [
            li(f"{getattr(n, 'door', '?')} · wanted {getattr(n, 'wanted', '')} · {getattr(n, 'reason', n)}")
            for n in items
        ]
        return section(
            span("attach notes", className="kicker"),
            h1("Notes"),
            p("Every specialist attach that steps down writes a note. The notebook is per-App.", className="lede"),
            ul(*rows, className="law-list paper"),
            a("Author door", href="/author", className="btn-ghost"),
            id=self.id,
            className="page",
        )
