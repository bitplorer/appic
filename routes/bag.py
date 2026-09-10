"""Bag — Host stock. Quantity never MorphState."""
from __future__ import annotations
from ux_compose import Component, MorphState, RefState, action, button, control, div, h1, li, mark_dirty, notify, p, section, span, ul, update_with
from store import HOST
PIECES = ("linen shirt", "oak board", "wool throw", "clay pourer")

class Bag(Component):
    id = "bag"
    dirty = MorphState("idle")
    items = RefState(())
    def render(self):
        held = list(self.items or HOST.bag)
        return section(
            span("Bag", className="eyebrow"),
            h1("What you keep.", className="display"),
            p("Lists live on RefState. Checkout would spend orders.place.", className="lede"),
            div(*[button(name, type="button", className="choice", **control("bag.add", name=name)) for name in PIECES], className="choices"),
            ul(*[li(n) for n in held] or [li("Empty.")], className="mono-list"),
            id=self.id, className="room",
        )
    @action(caps=())
    def add(self, name: str = ""):
        if name not in PIECES:
            name = PIECES[0]
        HOST.bag.append(name)
        self.items = tuple(HOST.bag)
        mark_dirty(self)
        HOST.log("bag.add", name)
        return update_with(self, extra_ops=[notify(name)])
