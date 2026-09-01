"""Page unit: notes.py → Notes.

Attach step-downs made visible. ADR 0004. Isolation: no ux_channel.
"""
from __future__ import annotations

from ux_compose import (
    AttachNote,
    Component,
    MorphState,
    action,
    attach_notes,
    notify,
    tick,
    update_with,
    maybe_plan,
)

from appic.ux import (
    div,
    h1,
    h2,
    p,
    section,
    span,
    article,
    act,
    doctor,
)

from appic.store import HOST


class Notes(Component):
    id = "notes"
    stamp = MorphState("idle")
    last = MorphState("idle")

    def _rows(self):
        rows = []
        try:
            app_notes = list(getattr(HOST, "attach_notes", ()) or ())
        except Exception:
            app_notes = []
        process = []
        try:
            process = list(attach_notes())
        except Exception:
            process = []
        return app_notes, process

    def render(self):
        app_notes, process = self._rows()

        def card(item: AttachNote):
            return article(
                span(item.door, className="kicker"),
                h2(item.wanted),
                p(f"kept L{item.level_kept}", className="mono tiny"),
                p(item.reason, className="muted"),
                className="card note-card",
            )

        app_cards = [card(n) for n in app_notes] or [
            article(
                span("App", className="kicker"),
                h2("No step-down on this App"),
                p("Specialists attached, or the door was never asked.", className="muted"),
                className="card",
            )
        ]
        proc_cards = [card(n) for n in process] or [
            article(
                span("Process", className="kicker"),
                h2("Process notebook empty"),
                p("attach_notes() is process-wide when no App is bound.", className="muted"),
                className="card",
            )
        ]
        report = None
        try:
            report = doctor([], fail=False)
        except Exception:
            report = None
        caps = []
        if report is not None:
            capabilities = getattr(report, "capabilities", {}) or {}
            if isinstance(capabilities, dict):
                for name, on in capabilities.items():
                    caps.append(
                        span(
                            f"{name} · {'on' if on else 'off'}",
                            className="chip" + (" is-on" if on else ""),
                        )
                    )
        return section(
            span("attach notes · visible step-down · per-App", className="eyebrow"),
            h1("Notes"),
            p(
                "If use_channel cannot import ux-channel, the App does not raise. "
                "It stays at L1 and writes one AttachNote. Silence was the defect.",
                className="lede",
            ),
            div(
                article(
                    span("App.attach_notes", className="kicker"),
                    h2(f"{len(app_notes)} on this App"),
                    p("Two Apps in one process do not leak. This is not a message bus.", className="muted"),
                    className="card",
                ),
                article(
                    span("attach_notes()", className="kicker"),
                    h2(f"{len(process)} process-wide"),
                    p("Doctor dual-writes so the audit has a process notebook.", className="muted"),
                    className="card",
                ),
                article(
                    span("Level", className="kicker"),
                    h2(str(HOST.level)),
                    p("Boot asked for live. Kept what specialists allowed.", className="muted"),
                    className="card",
                ),
                className="law-grid",
            ),
            h2("This App"),
            div(*app_cards, className="law-grid"),
            h2("Process"),
            div(*proc_cards, className="law-grid"),
            div(*caps, className="chip-row") if caps else None,
            act("notes.refresh", "Refresh notes", kind="ghost"),
            p(f"last · {self.last}", className="mono tiny"),
            id=self.id,
            className="page",
        )

    @action(caps=())
    def refresh(self, **kwargs):
        tick(self)
        app_notes, process = self._rows()
        self.last = f"app {len(app_notes)} · process {len(process)}"
        return update_with(
            self,
            maybe_plan("notes", "#notes", ms=120),
            extra_ops=[notify(self.last)],
        )
