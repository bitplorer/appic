"""Page unit: clocks.py → Clocks. Dual-clock room. Clock A vs Clock B."""
from __future__ import annotations

try:
    from ux_compose.routing import http_path, is_json_payload, is_stream_payload
except Exception:  # pragma: no cover
    def http_path(*segments: str) -> str:
        return "/" + "/".join(str(s).replace("[", "{").replace("]", "}") for s in segments if s not in {"index.py", "route.py"})

    def is_json_payload(value) -> bool:
        return isinstance(value, dict) or (isinstance(value, list) and (not value or isinstance(value[0], dict)))

    def is_stream_payload(value) -> bool:
        return hasattr(value, "__iter__") and not isinstance(value, (str, bytes, dict, list))

from appic.ux import (
    Component,
    MorphState,
    action,
    article,
    bind,
    button,
    div,
    h1,
    h2,
    p,
    span,
    tick,
    update_with,
)


class Clocks(Component):
    id = "clocks"
    ticks = MorphState("idle")
    stamp = MorphState("idle")

    def render(self):
        return div(
            span("Clocks", className="kicker"),
            h1("Two clocks. Three gates."),
            p(
                "Clock A is GET — resolve_unit, render(), payload type picks media type. "
                "Clock B is action — mutate, Ops, morph. They share a foundry. They are not one pipeline.",
                className="lede",
            ),
            div(
                article(
                    h2("Clock A"),
                    p("Page GET. The document wraps HTML. JSON and streams skip the wrap."),
                    className="clock-ring clock-a",
                    id="clock-a",
                ),
                article(
                    h2("Clock B"),
                    p("Intent. Cap. Result. Morph-then-Play."),
                    button("Tick B", type="button", **bind(self.tick_b)),
                    className="clock-ring clock-b",
                    id="clock-b",
                ),
                className="clock-pair",
            ),
            div(
                article(h2("HTML"), p("tag / str. Document wraps."), className="gate"),
                article(
                    h2("JSON"),
                    p(f"is_json_payload(dict) = {is_json_payload({'ok': True})}"),
                    p("/health is this door."),
                    className="gate",
                ),
                article(
                    h2("Stream"),
                    p(f"is_stream_payload(gen) is a generator door. /pulse."),
                    className="gate",
                ),
                className="gate-row",
            ),
            p(f"http_path index.py → {http_path('index.py')}", className="mono"),
            p(f"stamp {self.stamp}", className="mono", id="clock-stamp"),
            id=self.id,
            className="room",
        )

    @action(caps=())
    def tick_b(self):
        tick(self)
        self.ticks = "tock" if self.ticks == "tick" else "tick"
        return update_with(self)
