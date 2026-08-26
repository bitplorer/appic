"""DirectoryRoutes dynamic segment — stem [sku] → /atelier/{sku}.

Class Sku. No explicit get() so RouterHooks.resolve_unit feeds the live unit.
"""
from __future__ import annotations

from appic.marks import mark
from appic.store import BY_SKU, HOST
from appic.ux import (
    Component,
    MorphState,
    a,
    action,
    article,
    button,
    control,
    div,
    h1,
    h2,
    maybe_share,
    notify,
    p,
    section,
    span,
    tick,
    update_with,
)


class Sku(Component):
    id = "sku"
    current = MorphState("lamp-flax")
    stamp = MorphState("idle")

    def _piece(self):
        sku = str(self.current or "lamp-flax")
        return BY_SKU.get(sku) or BY_SKU["lamp-flax"]

    def render(self):
        prod = self._piece()
        sku = prod["sku"]
        wish = sku in HOST.wishlist
        qty = HOST.qty(sku)
        others = [p for p in BY_SKU.values() if p["sku"] != sku][:4]
        sibs = [
            a(
                span(p["name"]),
                href=f"/atelier/{p['sku']}",
                className="chip",
                id=f"sib-{p['sku']}",
            )
            for p in others
        ]
        return section(
            div(
                a("Atelier", href="/atelier", className="btn btn-text"),
                span("/", className="muted"),
                span(prod["name"], className="mono"),
                className="row crumbs-inline",
            ),
            article(
                div(mark(prod["mark"]), className="card-mark lg", id=f"pdp-{sku}"),
                h1(prod["name"]),
                p(prod["line"], className="lede"),
                div(
                    span(HOST.money(prod["price"]), className="price"),
                    span(prod["band"], className="chip"),
                    span(f"qty {qty}", className="chip"),
                    className="row",
                ),
                p(
                    "Filesystem → HTTP. Class name never in the URL. "
                    "resolve_unit supplies this live Behavior instance.",
                    className="muted",
                ),
                div(
                    button(
                        "Add to bag",
                        type="button",
                        className="btn btn-primary",
                        **control("sku.add", sku=sku),
                    ),
                    button(
                        "Saved" if wish else "Save",
                        type="button",
                        className="btn btn-ghost",
                        **control("sku.heart", sku=sku),
                    ),
                    a("Open bag", href="/bag", className="btn btn-text"),
                    className="hero-actions",
                ),
                className="card pdp",
                id=f"item-{sku}",
            ),
            div(
                h2("Also on the bench"),
                div(*sibs, className="chip-row"),
                className="card",
            ),
            id=self.id,
            className="page",
        )

    def show(self, sku: str = "") -> None:
        if sku in BY_SKU:
            self.current = sku

    @action(caps=())
    def add(self, sku: str = "", **kwargs):
        sku = sku or str(self.current)
        if sku not in BY_SKU:
            return
        HOST.set_line(sku, HOST.qty(sku) + 1)
        HOST.notice = f"Added {BY_SKU[sku]['name']}"
        tick(self)
        plan = maybe_share("line-to-bag", sku, leave=f"#pdp-{sku}", arrive="#bag", ms=160)
        return update_with(self, plan, extra_ops=[notify(HOST.notice)])

    @action(caps=())
    def heart(self, sku: str = "", **kwargs):
        sku = sku or str(self.current)
        if sku in HOST.wishlist:
            HOST.wishlist = [s for s in HOST.wishlist if s != sku]
        else:
            HOST.wishlist.append(sku)
        tick(self)
        return update_with(self, extra_ops=[notify("wishlist")])

    @action(caps=())
    def open(self, sku: str = "", **kwargs):
        self.show(sku)
        tick(self)
        return update_with(self)
