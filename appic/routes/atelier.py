"""Page unit: atelier.py → Atelier — catalog, filter, sort, wishlist, compare, lightbox."""
from __future__ import annotations

from appic.marks import mark
from appic.store import BY_SKU, CATALOG, HOST
from appic.ux import (
    Component,
    MorphState,
    a,
    action,
    act,
    article,
    button,
    control,
    div,
    h1,
    h2,
    h3,
    maybe_plan,
    maybe_stagger,
    notify,
    p,
    section,
    span,
    tick,
    update_with,
)


class Atelier(Component):
    id = "atelier"
    query = MorphState("")
    order = MorphState("alpha")
    lightbox = MorphState("")
    stamp = MorphState("idle")

    def _visible(self):
        q = str(self.query or HOST.intent or "").lower()
        rows = list(CATALOG)
        if q:
            rows = [p for p in rows if q in p["name"].lower() or q in p["sku"] or q in p["line"].lower()]
        if self.order == "price":
            rows = sorted(rows, key=lambda p: p["price"])
        else:
            rows = sorted(rows, key=lambda p: p["name"].lower())
        return rows

    def render(self):
        wish = set(HOST.wishlist)
        cmp_ = list(HOST.compare)
        rows = self._visible()
        cards = []
        for prod in rows:
            sku = prod["sku"]
            on = sku in wish
            compared = sku in cmp_
            cards.append(
                article(
                    div(mark(prod["mark"]), className="card-mark"),
                    h3(prod["name"]),
                    p(prod["line"], className="muted"),
                    div(
                        span(HOST.money(prod["price"]), className="price"),
                        span(prod["band"], className="chip"),
                        className="card-meta",
                    ),
                    div(
                        button(
                            "Add",
                            type="button",
                            className="btn btn-primary",
                            **control("atelier.add", sku=sku),
                        ),
                        button(
                            "Saved" if on else "Save",
                            type="button",
                            className="btn btn-ghost",
                            **control("atelier.heart", sku=sku),
                        ),
                        button(
                            "Compare" if not compared else "In compare",
                            type="button",
                            className="btn btn-text",
                            **control("atelier.compare", sku=sku),
                        ),
                        button(
                            "Look",
                            type="button",
                            className="btn btn-text",
                            **control("atelier.look", sku=sku),
                        ),
                        a("Piece", href=f"/atelier/{sku}", className="btn btn-text"),
                        className="card-actions",
                    ),
                    className="card product" + (f" tone-{prod['tone']}" if prod.get("tone") else ""),
                    id=f"item-{sku}",
                )
            )
        light = None
        if self.lightbox and self.lightbox in BY_SKU:
            prod = BY_SKU[self.lightbox]
            light = div(
                div(className="scrim", **control("atelier.close_look")),
                div(
                    div(mark(prod["mark"]), className="card-mark lg"),
                    h2(prod["name"]),
                    p(prod["line"], className="lede"),
                    p(f"{HOST.money(prod['price'])} · {prod['band']}", className="muted"),
                    button("Close", type="button", className="btn btn-ghost", **control("atelier.close_look")),
                    className="lightbox-panel",
                    role="dialog",
                    aria_modal="true",
                ),
                className="lightbox",
                id="lightbox",
            )
        cmp_panel = None
        if cmp_:
            bits = []
            for sku in cmp_[:3]:
                prod = BY_SKU.get(sku)
                if not prod:
                    continue
                bits.append(
                    div(
                        h3(prod["name"]),
                        p(HOST.money(prod["price"]), className="price"),
                        p(prod["line"], className="muted tiny"),
                        className="compare-col",
                    )
                )
            cmp_panel = div(*bits, className="compare-strip")
        return section(
            div(
                div(
                    h1("Atelier"),
                    p("Filter is MorphState. Rows are Host. Stamp dirties. Presence ids stay.", className="muted"),
                ),
                div(
                    span(f"{len(rows)} pieces", className="chip"),
                    span(f"{HOST.count()} in bag", className="chip"),
                    className="row",
                ),
                className="section-head spread",
            ),
            div(
                act("atelier.set_query", "All", kind="chip-on" if not self.query else "chip", q=""),
                act("atelier.set_query", "Flax", kind="chip-on" if self.query == "flax" else "chip", q="flax"),
                act("atelier.set_query", "Iron", kind="chip-on" if self.query == "iron" else "chip", q="iron"),
                act("atelier.set_query", "Oak", kind="chip-on" if self.query == "oak" else "chip", q="oak"),
                act("atelier.sort_alpha", "Name", kind="chip-on" if self.order == "alpha" else "chip"),
                act("atelier.sort_price", "Price", kind="chip-on" if self.order == "price" else "chip"),
                className="chip-row",
            ),
            div(*cards, className="product-grid") if cards else p("Nothing held by that intent.", className="empty"),
            cmp_panel,
            light,
            id=self.id,
            className="page",
        )

    @action(caps=())
    def set_query(self, q: str = "", **kwargs):
        self.query = q
        HOST.intent = q
        tick(self)
        ids = [f"#item-{p['sku']}" for p in self._visible()]
        return update_with(self, maybe_stagger("shelf", ids), extra_ops=[notify(q or "all")])

    @action(caps=())
    def sort_alpha(self, **kwargs):
        self.order = "alpha"
        tick(self)
        return update_with(self, extra_ops=[notify("Sorted by name")])

    @action(caps=())
    def sort_price(self, **kwargs):
        self.order = "price"
        tick(self)
        ids = [f"#item-{p['sku']}" for p in self._visible()]
        return update_with(self, maybe_stagger("shelf-price", ids), extra_ops=[notify("Sorted by price")])

    @action(caps=())
    def add(self, sku: str = "", **kwargs):
        if sku not in BY_SKU:
            return
        HOST.set_line(sku, HOST.qty(sku) + 1)
        HOST.notice = f"Added {BY_SKU[sku]['name']}"
        tick(self)
        return update_with(
            self,
            maybe_plan("bag-pop", f"#item-{sku}", ms=140),
            extra_ops=[notify(HOST.notice)],
        )

    @action(caps=())
    def heart(self, sku: str = "", **kwargs):
        if sku in HOST.wishlist:
            HOST.wishlist = [s for s in HOST.wishlist if s != sku]
        else:
            HOST.wishlist.append(sku)
        tick(self)
        return update_with(self)

    @action(caps=())
    def compare(self, sku: str = "", **kwargs):
        if sku in HOST.compare:
            HOST.compare = [s for s in HOST.compare if s != sku]
        elif len(HOST.compare) < 3:
            HOST.compare.append(sku)
        tick(self)
        return update_with(self)

    @action(caps=())
    def look(self, sku: str = "", **kwargs):
        self.lightbox = sku
        return update_with(self, maybe_plan("look", "#lightbox", ms=180))

    @action(caps=())
    def close_look(self, **kwargs):
        self.lightbox = ""
        return update_with(self)
