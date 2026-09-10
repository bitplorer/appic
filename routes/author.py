"""Author door — act, field, status, optional_*. One helper world."""
from __future__ import annotations

from ux_compose import (
    Component,
    MorphState,
    act,
    action,
    div,
    field,
    h1,
    notify,
    optional_fade,
    optional_plan,
    optional_slide,
    p,
    section,
    span,
    status,
    update_with,
)


class Author(Component):
    id = "author"
    note = MorphState("ready")

    def render(self):
        return section(
            span("one author door", className="kicker"),
            h1("Author"),
            p(
                "act() posts /act/{action}. field() is a labeled input. "
                "status() is a live region. optional_plan / fade / slide are motion IR, not forks.",
                className="lede",
            ),
            div(
                status(str(self.note or "ready"), kind="note"),
                field("title", "", placeholder="Name the piece"),
                act("author.mark", "Mark the stage", kind="primary", target="#author"),
                className="paper stack",
            ),
            id=self.id,
            className="page",
        )

    @action(caps=())
    def mark(self, title: str = ""):
        self.note = title or "marked"
        plan = optional_plan("author-mark", "#author", ms=140)
        _ = optional_fade("author-fade", "#author", ms=120)
        _ = optional_slide("author-slide", "#author", direction="next", ms=180)
        return update_with(self, plan, extra_ops=[notify(str(self.note))])
