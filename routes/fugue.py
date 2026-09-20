"""Page unit — fugue.py → GET /fugue.

The house plays the loop. Named station. Morph-then-Play hop.
Stations keep stable ids. XOR: the Plan carries no html=.
The vessel travels. Not a Pulse room.
"""
from __future__ import annotations

from ux_compose import (
    Component,
    MorphState,
    a,
    act,
    action,
    bind,
    button,
    div,
    h1,
    h2,
    li,
    mark_dirty,
    morph_play,
    notify,
    optional_slide,
    p,
    section,
    span,
    ul,
    update_with,
    scene,
    rise,
)
from chrome import vessel_mark
from store import HOST, WARP_HREF


class Fugue(Component):
    id = "fugue"
    station = MorphState("brief")
    dirty = MorphState("idle")

    def _plan(self, land: str):
        return (
            scene("fugue-hop")
            .stagger_in('[id^="hop-"]', rise.enter(ms=72), gap_ms=28)
            .enter(f"#hop-{land}", rise.enter(ms=140))
        )

    def render(self):
        HOST.occupy("fugue")
        station = str(self.station or HOST.fugue_station or "brief")
        keys = HOST.warp_keys()
        if station not in keys:
            station = keys[0] if keys else "brief"
        HOST.fugue_station = station
        piece = HOST.vessel
        hops = []
        for i, key in enumerate(keys):
            on = key == station
            href = WARP_HREF.get(key, f"/{key}")
            hops.append(
                li(
                    span(f"{i + 1:02d}", className="warp-idx"),
                    span(key, className="warp-name"),
                    a("walk", href=href, className="warp-walk"),
                    id=f"hop-{key}",
                    className="warp-thread is-on" if on else "warp-thread",
                    data_station=key,
                )
            )
        seated = []
        if piece:
            seated = [
                div(
                    vessel_mark(piece, size=72, ident="fugue-vessel"),
                    span(
                        span(str(piece.get("clay") or "clay"), className="cradle-clay"),
                        span(f"{station} · {piece.get('stage') or 'drawn'}", className="cradle-stage"),
                        className="cradle-copy",
                    ),
                    className="cloth-seat",
                    id="fugue-seat",
                )
            ]
        return section(
            span("Fugue", className="eyebrow"),
            h1("The house plays itself.", className="display"),
            p(
                "A hop is Morph-then-Play. Stations keep stable ids. Morph the fugue, "
                "then play a stagger on the surviving hops — objects that stay do not remount. "
                "XOR: the Plan carries no html=. bind() names the station. Caps stay off chrome.",
                className="lede",
            ),
            div(
                div(
                    span("subject", className="eyebrow"),
                    ul(*hops, className="warp", id="fugue-hops", role="list"),
                    className="paper cloth-warp",
                ),
                div(
                    span("voice", className="eyebrow"),
                    h2(station, className="sight-title"),
                    p(
                        "Each hop names the next warp station. The vessel travels with the voice. "
                        "Hold shares presence into the cradle.",
                        className="sight-law",
                    ),
                    *seated,
                    div(
                        button("Hop", type="button", className="btn-primary", **bind(self.hop)),
                        act("fugue.hold", "Hold the voice", kind="ghost", target="#fugue"),
                        a("Name the tide", href="/tide", className="btn-ghost"),
                        className="hero-actions",
                    ),
                    className="paper cloth-weft",
                    id="fugue-voice",
                ),
                className="kiln-split",
            ),
            id=self.id,
            className="room fugue-room",
            data_station=station,
        )

    @action(caps=())
    def hop(self):
        nxt = HOST.hop_fugue()
        self.station = nxt
        mark_dirty(self)
        # morph_play is the hop helper. XOR forbids html= on the plan, so the
        # Morph is from render() via update_with; morph_play names the land.
        land = morph_play(f"#hop-{nxt}", optional_slide("land", f"#hop-{nxt}", direction="next"))
        return update_with(self, self._plan(nxt), extra_ops=[notify(nxt), *land[1:]])

    @action(caps=())
    def hold(self):
        HOST.occupy("fugue")
        mark_dirty(self)
        HOST.notice = "The fugue is held."
        HOST.log("fugue.hold")
        plan = (
            scene("fugue-hold")
            .share("vessel", leave="#fugue-vessel", arrive="#cradle-vessel", recipe=rise.enter(ms=140))
            .enter("#fugue-voice", rise.enter(ms=160))
        )
        return update_with(self, plan, extra_ops=[notify("held")])
