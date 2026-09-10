"""Lab — live Caps, Intent, fail-closed pulse, Clock A JSON."""
from __future__ import annotations

from ux_compose import (
    Component,
    MorphState,
    RefState,
    a,
    action,
    button,
    control,
    div,
    h1,
    h2,
    mark_dirty,
    notify,
    p,
    section,
    span,
    update_with,
)


class Lab(Component):
    id = "lab"
    pulses = RefState(0)
    last = RefState("")
    dirty = MorphState("idle")

    def render(self):
        n = int(self.pulses or 0)
        last = str(self.last or "none")
        return section(
            span("clock b", className="kicker"),
            h1("Lab"),
            p(
                "Open mint on beat. pulse spends a Cap named pulse. "
                "JSON at /pulse.json is Clock A choosing media type by return value. "
                "/stream is a generator of light.",
                className="lede",
            ),
            div(
                h2(str(n), className="display"),
                p(f"last · {last}", className="mono"),
                div(
                    button("Beat", type="button", className="btn-primary", **control("lab.beat")),
                    button("Pulse (cap)", type="button", className="btn-ghost", **control("lab.pulse")),
                    className="row",
                ),
                a("Open JSON pulse", href="/pulse.json", className="btn-ghost"),
                a("Open stream", href="/stream", className="btn-ghost"),
                className="nucleus",
            ),
            id=self.id,
            className="page",
        )

    @action(caps=())
    def beat(self):
        self.pulses = int(self.pulses or 0) + 1
        self.last = "beat"
        mark_dirty(self)
        return update_with(self, extra_ops=[notify(f"beat {self.pulses}")])

    @action(caps=("pulse",))
    def pulse(self):
        self.pulses = int(self.pulses or 0) + 1
        self.last = "pulse"
        mark_dirty(self)
        return update_with(self, extra_ops=[notify("pulsed")])
