"""Bag — cart with RefState quantities. Checkout is a Cap."""
from __future__ import annotations

from store import CATALOG, HOST
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
    optional_plan,
    p,
    section,
    span,
    update_with,
)


class Bag(Component):
    id = "bag"
    count = RefState(0)
    last_sku = RefState("")
    dirty = MorphState("idle")

    def render(self):
        count = int(self.count or HOST.bag_count())
        cards = []
        for item in CATALOG:
            n = int(HOST.bag.get(item["sku"]) or 0)
            cards.append(
                div(
                    h2(item["name"]),
                    p(item["lede"], className="muted"),
                    p(f"{item['price']} · in bag {n}", className="mono"),
                    button(
                        f"Add {item['name']}",
                        type="button",
                        className="btn-primary",
                        **control("bag.add", sku=item["sku"]),
                    ),
                    className="paper",
                )
            )
        return section(
            span("orders.place on checkout", className="kicker"),
            h1("Bag"),
            p(
                f"{count} objects. Quantity is RefState. Named sku is Morph-safe. "
                "Checkout spends orders.place.",
                className="lede",
            ),
            div(*cards, className="kit-grid"),
            button("Checkout", type="button", className="btn-primary", **control("bag.checkout")),
            a("Commission instead", href="/commission", className="btn-ghost"),
            id=self.id,
            className="page",
        )

    @action(caps=())
    def add(self, sku: str = "cup"):
        n = HOST.add_bag(sku or "cup")
        self.count = HOST.bag_count()
        self.last_sku = sku
        mark_dirty(self)
        plan = optional_plan("bag-pop", f"#{self.id}", ms=140)
        return update_with(self, plan, extra_ops=[notify(f"added {sku} · {n}")])

    @action(caps=("orders.place",))
    def checkout(self):
        self.count = 0
        HOST.bag.clear()
        mark_dirty(self)
        return update_with(self, extra_ops=[notify("checkout sealed")])
