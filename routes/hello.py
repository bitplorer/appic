"""Kept from create-app. Live-safe counter: magnitude is RefState."""
from __future__ import annotations

from ux_compose import (
    Component,
    MorphState,
    RefState,
    action,
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
            span(str(n), className="text-2xl font-semibold tabular-nums"),
            button("+1", type="button", className=btn, **control("hello.inc")),
            span(str(pulses), className="text-2xl font-semibold tabular-nums"),
            button("pulse", type="button", className=btn, **control("hello.pulse")),
            id=self.id,
            className="page flex items-center gap-3 rounded-2xl border border-stone-200 bg-white p-6 text-stone-900",
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
