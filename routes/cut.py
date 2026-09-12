"""Page unit — GET /cut. Channel Cut C: empty Content-Type is bad_request."""
from __future__ import annotations

from ux_compose import (
    Component,
    MorphState,
    RefState,
    action,
    act,
    bind,
    control,
    div,
    h1,
    h2,
    p,
    section,
    span,
    article,
    dl,
    dt,
    dd,
    mark_dirty,
    notify,
    optional_plan,
    status,
    update_with,
    field,
    button,
)

from store import HOST


SEALS = (
    ("declared", "Declared type", "application/ux-channel+json on POST /ux-channel/action. The legal Clock B."),
    ("empty", "Empty type", "HTTP /action with no Content-Type is bad_request. Compose never posts bare."),
    ("form", "Progressive hatch", "act() stamps POST /act/{action}. Channel JS intercepts data-channel-action."),
    ("serve", "Frozen verbs", "dev / prod / restart-channel. argv development / production / restart_channel fail closed."),
)


class Cut(Component):
    id = "cut"
    sight = MorphState("declared")
    attempts = RefState(0)
    dirty = MorphState("idle")

    def _row(self):
        key = str(self.sight or "declared")
        for row in SEALS:
            if row[0] == key:
                return row
        return SEALS[0]

    def render(self):
        seen = self._row()
        n = int(self.attempts or 0)
        chips = [
            button(
                label,
                type="button",
                className="room-link is-on" if self.sight == key else "room-link",
                data_room=key,
                **control("cut.look", room=key),
            )
            for key, label, _ in SEALS
        ]
        return section(
            span("Cut C", className="eyebrow"),
            h1("A type is a seal.", className="display"),
            p(
                "Channel Cut C: empty Content-Type on HTTP /action is bad_request. "
                "Compose does not POST without a declared type. Clock B lives at "
                "POST /ux-channel/action as application/ux-channel+json.",
                className="lede",
            ),
            div(*chips, className="hero-actions", role="list"),
            article(
                span("sighted", className="eyebrow"),
                h2(seen[1], className="sight-title"),
                p(seen[2], className="sight-law"),
                status(HOST.notice or "The wax is intact.", kind="note"),
                className="paper",
                id="cut-sight",
            ),
            dl(
                dt("Bare attempts"),
                dd(str(n)),
                dt("Live path"),
                dd("POST /ux-channel/action"),
                dt("Hatch"),
                dd("POST /act/{action}"),
                dt("Serve"),
                dd("dev · prod · restart-channel"),
                className="kpi",
            ),
            div(
                act("cut.declare", "Declare the type", kind="primary", target="#cut"),
                button(
                    "Try a bare POST",
                    type="button",
                    className="btn-ghost",
                    **bind(self.bare),
                ),
                className="hero-actions",
            ),
            p(
                "The progressive hatch still exists. Channel JS intercepts data-channel-action "
                "and signs data-channel-cap. A form without a type is not a second live path.",
                className="lede",
            ),
            field("cut-note", value="", placeholder="A note on the seal", kind="text"),
            id=self.id,
            className="room",
        )

    @action(caps=())
    def look(self, room: str = "declared"):
        keys = {row[0] for row in SEALS}
        self.sight = room if room in keys else "declared"
        HOST.log("cut.look", str(self.sight))
        return update_with(
            self,
            optional_plan("cut-sight", "#cut-sight"),
            extra_ops=[notify(str(self.sight))],
        )

    @action(caps=())
    def declare(self):
        HOST.notice = "Type declared: application/ux-channel+json"
        HOST.log("cut.declare", "application/ux-channel+json")
        mark_dirty(self)
        return update_with(self, extra_ops=[notify("declared")])

    @action(caps=())
    def bare(self):
        self.attempts = int(self.attempts or 0) + 1
        mark_dirty(self)
        HOST.notice = "Refused. Empty Content-Type is bad_request."
        HOST.log("cut.bare", "bad_request")
        return update_with(self, extra_ops=[notify("bad_request")])
