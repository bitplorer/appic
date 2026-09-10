"""Author door — act / mark_dirty / field / status / optional_*."""
from __future__ import annotations
from ux_compose import (
    Component, MorphState, RefState, action, act, bind, button, div, field,
    h1, mark_dirty, notify, optional_fade, optional_plan, optional_slide,
    p, section, span, status, update_with, morph_play,
)

class Author(Component):
    id = "author"
    dirty = MorphState("idle")
    note = RefState("")
    def render(self):
        return section(
            span("Author", className="eyebrow"),
            h1("One door. No second helper world.", className="display"),
            p("act() posts /act/{action}. mark_dirty flips qualitative dirty. optional_* import and use ux-motion.", className="lede"),
            div(
                field("note", str(self.note or ""), placeholder="A line"),
                act("author.tick", "Tick", kind="primary", target="#author"),
                status("Author door is open.", kind="note"),
                className="paper stack",
            ),
            id=self.id, className="room",
        )
    @action(caps=())
    def tick(self, note: str = ""):
        self.note = note
        mark_dirty(self)
        return update_with(self, optional_fade("tick", "#author"), extra_ops=[notify("tock")])
