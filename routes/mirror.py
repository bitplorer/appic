"""Page unit — mirror.py → GET /mirror.

The vessel looking at itself. Named face. Owned Diff, shell=False.
Before / after are Host snapshots. Not /diff. Not a Pulse room.
"""
from __future__ import annotations

from ux_compose import (
    a,
    action,
    bind,
    button,
    div,
    h1,
    mark_dirty,
    notify,
    optional_fade,
    p,
    section,
    span,
    update_with,
)
from chrome import vessel_mark
from components.diff import Diff as DiffCard
from store import HOST, _piece_line


class Mirror(DiffCard):
    id = "mirror"
    VIEWS = (("before", "Before"), ("after", "After"), ("split", "Split"))

    def render(self, *, shell=None, **slots):
        HOST.occupy("mirror")
        before = HOST.mirror_before or HOST.vessel or {}
        after = HOST.mirror_after or HOST.vessel or {}
        self.BEFORE = _piece_line(before)
        self.AFTER = _piece_line(after)
        unit = super().render(shell=False, **slots)
        faces = [
            div(
                span("before", className="eyebrow"),
                vessel_mark(before, size=88, ident="mirror-before"),
                span(_piece_line(before), className="muted"),
                className="paper mirror-face",
                id="mirror-face-before",
            ),
            div(
                span("after", className="eyebrow"),
                vessel_mark(after, size=88, ident="mirror-after"),
                span(_piece_line(after), className="muted"),
                className="paper mirror-face",
                id="mirror-face-after",
            ),
        ]
        return section(
            span("Mirror", className="eyebrow"),
            h1("The piece looking at itself.", className="display"),
            p(
                "A named face. Switching is public. Snapshots are Host stock — never "
                "MorphState(list). The kit demo at /diff stays a kit room. This is the "
                "house memory of fire. Owned Diff, shell=False.",
                className="lede",
            ),
            div(*faces, className="duet-pair mirror-pair", id="mirror-pair"),
            div(unit, className="paper lineage-card", id="mirror-card"),
            div(
                button("Hold before", type="button", className="btn-primary", **bind(self.hold_before)),
                button("Hold after", type="button", className="btn-ghost", **bind(self.hold_after)),
                a("Sit the vessel", href="/vessel", className="btn-ghost"),
                className="hero-actions",
            ),
            id=self.id,
            className="room mirror-room",
        )

    @action(caps=())
    def hold_before(self):
        HOST.snap_before()
        mark_dirty(self)
        return update_with(self, optional_fade("before", "#mirror-face-before"), extra_ops=[notify("before")])

    @action(caps=())
    def hold_after(self):
        HOST.snap_after()
        mark_dirty(self)
        return update_with(self, optional_fade("after", "#mirror-face-after"), extra_ops=[notify("after")])
