"""Page unit — charge.py → GET /charge.

The wax press. Intent is held on the Host. AttachNote refuses silence.
Charging is a named MorphState; the notebook is not a message bus.
"""
from __future__ import annotations

from ux_compose import (
    Component,
    MorphState,
    RefState,
    action,
    AttachNote,
    attach_notes,
    button,
    control,
    div,
    h1,
    h2,
    li,
    mark_dirty,
    notify,
    optional_plan,
    p,
    section,
    span,
    ul,
    update_with,
    a,
    circle,
    path,
    svg,
)
from store import HOST

INTENTS = (
    ("hold", "Hold the table"),
    ("throw", "Throw a body"),
    ("lock", "Lock a recipe"),
    ("place", "Place a commission"),
    ("draw", "Draw from the kiln"),
)


class Charge(Component):
    id = "charge"
    intent = MorphState("hold")
    pressed = MorphState(False)
    dirty = MorphState("idle")
    last = RefState("")

    def render(self):
        key = str(self.intent or "hold")
        label = next((lab for k, lab in INTENTS if k == key), "Hold the table")
        notes = list(attach_notes() or ())
        if not notes:
            notes = [
                AttachNote(
                    door="boot",
                    wanted="complete install",
                    reason="Python ≥3.14 + pinned specialists. Silence was the defect.",
                    level_kept=3,
                )
            ]
        chips = [
            button(
                lab,
                type="button",
                className="choice is-on" if self.intent == k else "choice",
                **control("charge.hold", intent=k),
            )
            for k, lab in INTENTS
        ]
        items = [
            li(
                span(n.door, className="mono"),
                span(n.wanted, className="card-title"),
                span(n.reason, className="muted"),
                className="hand-line",
            )
            for n in notes[:8]
        ]
        return section(
            span("Charge", className="eyebrow"),
            h1("An Intent is a nucleus. Wax is the seal.", className="display"),
            p(
                "Named Intent is MorphState. The notebook is AttachNote — not a bus. "
                "Pressing the wax writes Host stock. Caps mint on Clock B; empty type is bad_request.",
                className="lede",
            ),
            div(
                div(
                    span("press", className="eyebrow"),
                    svg(
                        circle(cx="64", cy="64", r="46", fill="none", stroke="currentColor", stroke_width="1.4", className="charge-ring"),
                        circle(cx="64", cy="64", r="28", fill="currentColor", className="charge-wax"),
                        path(
                            d="M64 28 v8 M64 92 v8 M28 64 h8 M92 64 h8",
                            fill="none",
                            stroke="currentColor",
                            stroke_width="1.6",
                            className="charge-cross",
                        ),
                        viewBox="0 0 128 128",
                        className="charge-svg",
                        aria_hidden="true",
                    ),
                    p(label, className="hearth-piece"),
                    p("Wax spent" if self.pressed else "Wax intact", className="stat"),
                    p(str(self.last or HOST.intent or "hold the table"), className="muted"),
                    className="hearth charge-press" + (" is-spent" if self.pressed else ""),
                    data_intent=key,
                    id="press",
                ),
                div(
                    span("intent", className="eyebrow"),
                    h2(label, className="sight-title"),
                    p("Hold a named Intent. Press writes the Host. Walk Cut to see empty type fail closed.", className="sight-law"),
                    div(*chips, className="choices", role="radiogroup", aria_label="Intent"),
                    div(
                        span("", className="seal is-spent" if self.pressed else "seal", aria_hidden="true"),
                        span(
                            "Wax spent · charge.press" if self.pressed else "Wax intact · mint on press",
                            className="mono",
                        ),
                        className="cap-row",
                    ),
                    div(
                        button(
                            "Already pressed" if self.pressed else "Press the wax",
                            type="button",
                            className="btn-primary",
                            **control("charge.press"),
                        ),
                        a("Walk Cut C", href="/cut", className="btn-ghost"),
                        a("Open Command", href="/command", className="btn-ghost"),
                        className="hero-actions",
                    ),
                    className="paper",
                    id="charge-card",
                ),
                className="kiln-split",
            ),
            div(
                span("notebook", className="eyebrow"),
                p("AttachNote is one App's notebook. Step-downs are written down.", className="muted"),
                ul(*items, className="hands-log", role="list"),
                className="paper",
            ),
            id=self.id,
            className="room",
        )

    @action(caps=())
    def hold(self, intent: str = "hold"):
        keys = {k for k, _ in INTENTS}
        self.intent = intent if intent in keys else "hold"
        label = next((lab for k, lab in INTENTS if k == self.intent), "Hold the table")
        HOST.intent = label
        HOST.log("charge.hold", str(self.intent))
        mark_dirty(self)
        return update_with(
            self,
            optional_plan("intent", "#press"),
            extra_ops=[notify(str(self.intent))],
        )

    @action(caps=())
    def press(self):
        label = next((lab for k, lab in INTENTS if k == self.intent), "Hold the table")
        self.pressed = True
        self.last = label
        HOST.intent = label
        HOST.notice = f"Wax spent · {label}"
        HOST.log("charge.press", label, "cap")
        mark_dirty(self)
        return update_with(
            self,
            optional_plan("press", "#press"),
            extra_ops=[notify("spent")],
        )
