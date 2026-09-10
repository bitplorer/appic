"""Commission a piece — questionnaire + stepper + plans. Finish is a Cap."""
from __future__ import annotations

from foundry import kit_tree
from store import HOST
from ux_compose import (
    Component,
    MorphState,
    RefState,
    action,
    button,
    control,
    div,
    h1,
    mark_dirty,
    notify,
    p,
    section,
    span,
    update_with,
)


class Commission(Component):
    id = "commission"
    placed = RefState(0)
    last = RefState("")
    dirty = MorphState("idle")

    def render(self):
        n = int(self.placed or 0)
        last = str(self.last or "")
        return section(
            span("orders.place", className="kicker"),
            h1("Commission"),
            p(
                "Named questions, named steps, named plans. Magnitude of orders sits on RefState. "
                "Finish spends a Cap. The Host ledger keeps the object.",
                className="lede",
            ),
            p(f"Placed · {n}" + (f" · last {last}" if last else ""), className="mono"),
            div(
                kit_tree("questionnaire"),
                kit_tree("stepper"),
                kit_tree("plans"),
                kit_tree("formlayout"),
                className="stack-paper",
            ),
            button(
                "Seal the commission",
                type="button",
                className="btn-primary",
                **control("commission.place"),
            ),
            id=self.id,
            className="page",
        )

    @action(caps=("orders.place",))
    def place(self):
        item = HOST.place("basin", "ash", "atelier", "sealed from the table")
        self.placed = int(self.placed or 0) + 1
        self.last = item.sku
        mark_dirty(self)
        return update_with(self, extra_ops=[notify(f"commissioned {item.sku}")])
