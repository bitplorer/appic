"""Page unit — watch.py → GET /watch. The night watch keeps shared hearth heat."""
from __future__ import annotations

from ux_compose import (
    Component,
    MorphState,
    RefState,
    action,
    a,
    button,
    control,
    div,
    h1,
    h2,
    li,
    mark_dirty,
    notify,
    optional_fade,
    optional_plan,
    p,
    progress,
    section,
    span,
    ul,
    update_with,
)
from store import HOST

HOURS = ("first", "middle", "last")
HOUR_COPY = {
    "first": "First watch. The kiln is a new animal. Sit with it.",
    "middle": "Middle watch. The glaze is still. Do not open the door.",
    "last": "Last watch. The fire is leaving. Dawn is a named band.",
}
HOUR_LABEL = {
    "first": "First",
    "middle": "Middle",
    "last": "Last",
}


def _hour_for(remain: int, firing: bool) -> str:
    if not firing:
        return "first"
    if remain <= 3:
        return "last"
    if remain <= 7:
        return "middle"
    return "first"


class Watch(Component):
    id = "watch"
    hour = MorphState("first")
    remain = RefState(0)
    dirty = MorphState("idle")
    bell = MorphState("quiet")

    def _n(self) -> int:
        try:
            return max(0, int(self.remain or 0))
        except (TypeError, ValueError):
            return 0

    def render(self):
        hour = str(self.hour or "first")
        if hour not in HOURS:
            hour = "first"
        n = int(HOST.heat_remain) if HOST.firing else self._n()
        pct = 0 if not HOST.firing else max(0, min(100, int(((12 - n) / 12) * 100)))
        bells = [li(line, className="hand-line") for line in reversed(HOST.watch_bells[-8:])] or [
            li("No bell yet. The house is listening.", className="hand-line")
        ]
        hours = [
            button(
                HOUR_LABEL[key],
                type="button",
                className="seg is-on" if hour == key else "seg",
                **control("watch.shift", hour=key),
            )
            for key in HOURS
        ]
        piece = ""
        if HOST.last_firing:
            piece = f"{HOST.last_firing.get('clay', 'clay')} · {HOST.last_firing.get('glaze', 'glaze')}"
        elif HOST.pending_fire:
            piece = "A piece waits on the shelf."
        return section(
            span("Watch", className="eyebrow"),
            h1("Keep the fire in the dark.", className="display"),
            p(
                "The hour is MorphState. Remaining heat is Host stock, the same "
                "hearth the kiln ticks. Keep is public. A bell is one-shot notify. "
                "This is not a Pulse room — it is the foundry after hours.",
                className="lede",
            ),
            div(
                div(
                    span("bell", className="eyebrow"),
                    div(
                        span("", className="ember", aria_hidden="true"),
                        span("", className="heat-ring r1", aria_hidden="true"),
                        span("", className="heat-ring r2", aria_hidden="true"),
                        span("", className="heat-ring r3", aria_hidden="true"),
                        className="watch-hearth",
                    ),
                    p(piece or "The hearth is dark.", className="hearth-piece"),
                    p(
                        str(n),
                        className="stat",
                        role="timer",
                        aria_live="polite",
                        aria_label="Remaining heat",
                    ),
                    p(HOUR_COPY[hour], className="muted"),
                    className=f"hearth band-{hour} {'is-lit' if HOST.firing else 'is-dark'}",
                    data_hour=hour,
                    id="watch-bell",
                ),
                div(
                    span("hours", className="eyebrow"),
                    h2(HOUR_LABEL[hour] + " watch", className="sight-title"),
                    p(HOUR_COPY[hour], className="sight-law"),
                    div(*hours, className="segs", role="radiogroup", aria_label="Watch hour"),
                    progress(
                        value=str(pct),
                        max="100",
                        className="fire-bar",
                        role="progressbar",
                        aria_valuemin="0",
                        aria_valuemax="100",
                        aria_valuenow=str(pct),
                        aria_label="Watch progress",
                    ),
                    div(
                        button(
                            "Keep the watch",
                            type="button",
                            className="btn-primary",
                            **control("watch.keep"),
                        ),
                        button(
                            "Ring the bell",
                            type="button",
                            className="btn-ghost",
                            **control("watch.ring"),
                        ),
                        a("Walk to the kiln", href="/kiln", className="btn-ghost"),
                        a("Walk to the vitrine", href="/vitrine", className="btn-ghost")
                        if str(HOST.notice).startswith("Drawn")
                        else span(""),
                        className="hero-actions",
                    ),
                    ul(*bells, className="hands-log", role="log", aria_label="Watch bells"),
                    className="paper",
                    id="watch-card",
                ),
                className="kiln-split",
            ),
            id=self.id,
            className="room watch-room",
            data_hour=hour,
        )

    @action(caps=())
    def shift(self, hour: str = "first"):
        if hour not in HOURS:
            hour = "first"
        self.hour = hour
        HOST.log("watch.hour", hour)
        return update_with(self, extra_ops=[notify(hour)])

    @action(caps=())
    def keep(self):
        if HOST.firing:
            band = HOST.tick_heat()
            self.remain = int(HOST.heat_remain)
            self.hour = _hour_for(int(HOST.heat_remain), HOST.firing or band == "done")
            mark_dirty(self)
            HOST.watch_bells.append(f"kept · {band} · {HOST.heat_remain} remaining")
            HOST.watch_bells = HOST.watch_bells[-16:]
            HOST.log("watch.keep", band)
            return update_with(self, optional_plan("keep", "#watch"), extra_ops=[notify(band)])
        if HOST.pending_fire or HOST.last_firing or HOST.commissions:
            piece = HOST.pending_fire or HOST.last_firing or HOST.commissions[-1]
            HOST.light(piece)
            self.remain = 12
            self.hour = "first"
            mark_dirty(self)
            HOST.notice = "The watch lit the kiln."
            HOST.watch_bells.append("first watch · kiln lit from the dark")
            HOST.log("watch.light", str(piece.get("clay", "")))
            return update_with(self, extra_ops=[notify("warm")])
        HOST.notice = "Nothing to keep. Commission a piece first."
        return update_with(self, extra_ops=[notify("empty shelf")])

    @action(caps=())
    def ring(self):
        self.bell = "rung"
        mark_dirty(self)
        HOST.watch_bells.append(f"bell · {self.hour} watch")
        HOST.watch_bells = HOST.watch_bells[-16:]
        HOST.log("watch.ring", str(self.hour))
        HOST.notice = "A bell crossed the house."
        return update_with(self, extra_ops=[notify("bell")])
