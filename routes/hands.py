"""Page unit — hands.py → GET /hands. Studio floor. Log is RefState; typing is MorphState."""
from __future__ import annotations

from ux_compose import (
    Component,
    MorphState,
    RefState,
    action,
    bind,
    button,
    control,
    div,
    form,
    h1,
    input_,
    label,
    li,
    mark_dirty,
    notify,
    p,
    section,
    span,
    ul,
    update_with,
)
from store import HOST

SEED = (
    "Atelier: the table is lit.",
    "Kiln: remaining heat is a quantity. Do not put it on MorphState.",
    "Wheel: a body is waiting on the bat.",
)


class Hands(Component):
    id = "hands"
    draft = RefState("")
    typing = MorphState(False)
    dirty = MorphState("idle")

    def _lines(self):
        lines = list(HOST.hands) or list(SEED)
        if not HOST.hands:
            HOST.hands = list(SEED)
        return lines

    def render(self):
        lines = self._lines()
        draft = str(self.draft or "")
        typing = bool(self.typing)
        rows = [
            li(
                span(line, className="card-title" if line.startswith("You:") else "muted"),
                className="hand-line you" if line.startswith("You:") else "hand-line",
            )
            for line in lines[-16:]
        ]
        return section(
            span("Hands", className="eyebrow"),
            h1("Other hands at the table.", className="display"),
            p(
                "The log is RefState on the Host. Typing is MorphState. "
                "Send is public. Caps stay off chrome. role=log, never a modal.",
                className="lede",
            ),
            div(
                ul(
                    *rows,
                    id="hands-log",
                    className="hands-log",
                    role="log",
                    aria_live="polite",
                    aria_relevant="additions",
                    aria_label="Studio floor",
                ),
                p(
                    "Atelier is typing…" if typing else f"{len(lines)} line" + ("" if len(lines) == 1 else "s") + " on the floor.",
                    className="muted",
                    role="status",
                ),
                form(
                    label("Write a line", html_for="hands-draft", className="eyebrow"),
                    input_(
                        type="text",
                        name="text",
                        id="hands-draft",
                        value=draft,
                        placeholder="A line for the floor",
                        autocomplete="off",
                        className="field",
                        **bind(self.set_field, field="text"),
                    ),
                    div(
                        button("Send", type="button", className="btn-primary", **control("hands.send")),
                        button("Let the atelier answer", type="button", className="btn-ghost", **control("hands.peer")),
                        className="hero-actions",
                    ),
                    className="stack",
                ),
                className="paper",
                id="hands-card",
            ),
            id=self.id,
            className="room",
            data_typing="1" if typing else "0",
        )

    @action(caps=())
    def set_field(self, field: str = "", value: str = "", **kwargs):
        raw = value if value != "" else kwargs.get(field, kwargs.get("text", ""))
        self.draft = "" if raw is None else str(raw)
        mark_dirty(self)
        return update_with(self)

    @action(caps=())
    def send(self, text: str = ""):
        line = (text or str(self.draft or "")).strip() or "…"
        HOST.hands.append(f"You: {line}")
        HOST.hands = HOST.hands[-48:]
        self.draft = ""
        self.typing = False
        mark_dirty(self)
        HOST.log("hands.send", line)
        return update_with(self, extra_ops=[notify("sent")])

    @action(caps=())
    def peer(self):
        self.typing = True
        mark_dirty(self)
        HOST.hands.append("Atelier: hold the table. Sight, then walk.")
        HOST.hands = HOST.hands[-48:]
        HOST.log("hands.peer", "atelier")
        self.typing = False
        return update_with(self, extra_ops=[notify("atelier")])
