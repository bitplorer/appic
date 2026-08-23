"""Page unit: bag.py → Bag — cart, stepper, coupon Cap, confirm, checkout Cap."""
from __future__ import annotations

from appic.store import BY_SKU, HOST
from appic.ux import (
    Component,
    MorphState,
    action,
    act,
    button,
    control,
    div,
    form,
    h1,
    h2,
    input_,
    li,
    maybe_fade,
    maybe_plan,
    notify,
    p,
    section,
    span,
    tick,
    ul,
    update_with,
)


class Bag(Component):
    id = "bag"
    confirm_open = MorphState(False)
    coupon = MorphState("")
    stamp = MorphState("idle")

    def render(self):
        rows = HOST.lines
        items = []
        for sku, qty in rows:
            prod = BY_SKU.get(sku) or {"name": sku, "price": 0}
            items.append(
                li(
                    span(prod["name"], className="bag-name"),
                    span(f"× {qty}", className="muted"),
                    span(HOST.money(prod["price"] * qty), className="price"),
                    div(
                        button("−", type="button", className="btn btn-ghost", **control("bag.dec", sku=sku)),
                        button("+", type="button", className="btn btn-ghost", **control("bag.inc", sku=sku)),
                        button("Remove", type="button", className="btn btn-text", **control("bag.remove", sku=sku)),
                        className="row",
                    ),
                    className="bag-line",
                    id=f"bag-{sku}",
                )
            )
        modal = None
        if self.confirm_open:
            modal = div(
                div(className="scrim", **control("bag.close_confirm")),
                div(
                    p("Order", className="kicker"),
                    h2("Place this order", id="confirm-title"),
                    p(
                        f"{HOST.count()} piece(s) · {HOST.money()}. "
                        "The verb is Cap-protected (orders.place).",
                        className="lede",
                    ),
                    div(
                        act("bag.close_confirm", "Keep looking", kind="ghost"),
                        act("bag.checkout", "Place order", kind="primary"),
                        className="row",
                    ),
                    className="modal-panel",
                    role="dialog",
                    aria_modal="true",
                    aria_labelledby="confirm-title",
                ),
                className="lightbox",
                id="confirm",
            )
        body = (
            ul(*items, className="bag-lines")
            if items
            else div(
                p("The bag is empty", className="empty-title"),
                p("Choose a piece from the atelier. Nothing is held until you place.", className="muted"),
                className="empty",
            )
        )
        return section(
            div(
                h1("Bag"),
                p("Quantities silent. Stamp dirties. Coupon and checkout are Caps.", className="muted"),
                className="section-head",
            ),
            body,
            div(
                span("Subtotal", className="muted"),
                span(HOST.money(), className="price xl"),
                className="spread",
            )
            if items
            else None,
            form(
                input_(
                    type="text",
                    name="code",
                    placeholder="House coupon",
                    className="field",
                    value=str(self.coupon or HOST.coupon or ""),
                ),
                button("Redeem", type="submit", className="btn btn-ghost", **control("bag.redeem")),
                className="row",
                method="post",
                action="/action/bag.redeem",
                data_ux="1",
            )
            if items
            else None,
            p(HOST.notice, className="muted") if HOST.notice else None,
            div(
                act("bag.clear", "Clear", kind="ghost") if items else None,
                act("bag.request_checkout", "Review order", kind="primary") if items else None,
                className="row",
            ),
            modal,
            id=self.id,
            className="page",
        )

    @action(caps=())
    def inc(self, sku: str = "", **kwargs):
        HOST.set_line(sku, HOST.qty(sku) + 1)
        tick(self)
        return update_with(self, maybe_plan("qty", f"#bag-{sku}", ms=90))

    @action(caps=())
    def dec(self, sku: str = "", **kwargs):
        HOST.set_line(sku, max(0, HOST.qty(sku) - 1))
        tick(self)
        return update_with(self)

    @action(caps=())
    def remove(self, sku: str = "", **kwargs):
        HOST.set_line(sku, 0)
        HOST.notice = "Removed"
        tick(self)
        return update_with(self, extra_ops=[notify("Removed")])

    @action(caps=())
    def clear(self, **kwargs):
        HOST.lines = []
        HOST.discount = 0
        HOST.notice = "Bag cleared"
        tick(self)
        return update_with(self)

    @action(caps=())
    def request_checkout(self, **kwargs):
        if not HOST.lines:
            HOST.notice = "Bag is empty"
            return update_with(self, extra_ops=[notify("Empty bag")])
        self.confirm_open = True
        return update_with(self, maybe_plan("confirm", "#confirm", ms=180))

    @action(caps=())
    def close_confirm(self, **kwargs):
        self.confirm_open = False
        return update_with(self)

    @action(caps=("orders.coupon",))
    def redeem(self, code: str = "", **kwargs):
        code = (code or "").strip().upper()
        self.coupon = code.lower()
        HOST.coupon = code
        if code in {"HOUSE", "FLAX", "TABLE"}:
            HOST.discount = 8
            HOST.notice = f"Coupon {code} · 8 held off"
        else:
            HOST.discount = 0
            HOST.notice = "Unknown coupon"
        tick(self)
        return update_with(self, extra_ops=[notify(HOST.notice)])

    @action(caps=("orders.place",))
    def checkout(self, **kwargs):
        if not HOST.lines:
            HOST.notice = "Bag is empty"
            return update_with(self, extra_ops=[notify("Empty bag")])
        total = HOST.subtotal()
        HOST.orders.append({"total": total, "lines": list(HOST.lines)})
        HOST.kpi["placed"] = int(HOST.kpi.get("placed", 0)) + 1
        HOST.lines = []
        HOST.discount = 0
        self.confirm_open = False
        HOST.notice = f"Order placed · {HOST.money(total)}"
        tick(self)
        return update_with(
            self,
            maybe_fade("order-placed", "#bag", ms=160),
            extra_ops=[notify("Order placed")],
        )
