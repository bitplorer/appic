"""Page unit — hello.py → /hello. Live-safe counter (quantity on RefState)."""
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
    mark_dirty,
    notify,
    span,
    update_with,
)


class Hello(Component):
    id = "hello"
    n = RefState(0)
    pulses = RefState(0)
    dirty = MorphState("idle")

    def render(self):
        n = int(self.n or 0)
        pulses = int(self.pulses or 0)
        btn = "btn-primary"
        return div(
            span(str(n), className="stat", id="hello-n"),
            button("+1", type="button", className=btn, **control("hello.inc")),
            span(str(pulses), className="stat", id="hello-p"),
            button("pulse", type="button", className=btn, **bind(self.pulse)),
            id=self.id,
            className="paper row",
            data_dirty=str(self.dirty or "idle"),
        )

    @action(caps=())
    def inc(self):
        self.n = int(self.n or 0) + 1
        mark_dirty(self)
        return update_with(self, extra_ops=[notify("incremented")])

    @action(caps=("pulse",))
    def pulse(self):
        self.pulses = int(self.pulses or 0) + 1
        mark_dirty(self)
        return update_with(self, extra_ops=[notify("pulsed")])
