"""Page unit: lattice.py → Lattice — Caps as seals, Ops as traces, Intent as nucleus."""
from __future__ import annotations

from appic.store import HOST
from appic.ux import (
    Component,
    MorphState,
    RefState,
    a,
    action,
    bind,
    button,
    circle,
    control,
    div,
    h1,
    h2,
    h3,
    li,
    maybe_plan,
    notify,
    p,
    path,
    section,
    span,
    svg,
    tick,
    ul,
    update_with,
)

SEALS = (
    ("orders.place", "Place", "Checkout / commission. Money leaves the house.", 50.0, 16.0),
    ("orders.coupon", "Redeem", "HOUSE · FLAX · TABLE. Code is MorphState; redeem is a Cap.", 78.0, 34.0),
    ("identity.verify", "Verify", "OTP 2048. Digits on RefState. Verify is a Cap.", 78.0, 68.0),
    ("calendar.book", "Book", "A named day. Magnitude on Host. Book is a Cap.", 50.0, 84.0),
    ("settings.wipe", "Wipe", "Density, motion, locale. Wipe is a Cap.", 22.0, 68.0),
    ("comments.moderate", "Moderate", "Studio comments. Public write; moderate is a Cap.", 22.0, 34.0),
)

PUBLIC = (
    ("home.beat", "Pulse"),
    ("atelier.sort_price", "Sort"),
    ("board.move", "Move"),
    ("lab.set_floor", "Floor"),
)


class Lattice(Component):
    id = "lattice"
    selected = MorphState("orders.place")
    charged = MorphState("")
    stamp = MorphState("idle")
    last = RefState("")

    def _current(self):
        key = str(self.selected or "orders.place")
        for row in SEALS:
            if row[0] == key:
                return row
        return SEALS[0]

    def render(self):
        sel = str(self.selected or "orders.place")
        charged = str(self.charged or "")
        nodes = []
        for key, label, _blurb, x, y in SEALS:
            on = key == sel
            minted = key == charged
            nodes.append(
                button(
                    svg(
                        circle(
                            cx="16",
                            cy="16",
                            r="13",
                            fill="none",
                            stroke="currentColor",
                            stroke_width="1.4",
                        ),
                        circle(
                            cx="16",
                            cy="16",
                            r="6",
                            fill="currentColor" if minted else "none",
                            stroke="currentColor",
                            stroke_width="1.2",
                        ),
                        viewBox="0 0 32 32",
                        width="32",
                        height="32",
                        aria_hidden="true",
                    ),
                    span(label),
                    type="button",
                    className="seal-node" + (" is-on" if on else "") + (" is-minted" if minted else ""),
                    style=f"left:{x}%;top:{y}%;",
                    **control("lattice.select", cap=key),
                    id=f"seal-{key.replace('.', '-')}",
                )
            )
        traces = []
        for i, row in enumerate(reversed(list(HOST.trace or ())[-8:])):
            traces.append(
                li(
                    span(str(row.get("kind", "morph")), className="chip"),
                    span(str(row.get("verb", "")), className="mono"),
                    id=f"lat-op-{i}",
                    className="cap-row",
                )
            )
        pubs = [
            button(
                lab,
                type="button",
                className="chip",
                **control("lattice.public_fire", verb=name),
            )
            for name, lab in PUBLIC
        ]
        key, title, blurb, _x, _y = self._current()
        return section(
            div(
                span("radical instrument · Results of Ops as a constellation", className="eyebrow"),
                h1("Lattice"),
                p(
                    "Intent sits at the nucleus. Caps are seals on the ring. "
                    "Public verbs are open doors. Protected verbs fail closed until the host mints.",
                    className="lede",
                ),
                className="section-head",
            ),
            div(
                div(
                    span("Intent", className="nucleus-kicker"),
                    h2(str(HOST.intent or "unnamed")),
                    p("Hold an intent on the table. The lattice does not invent one.", className="muted tiny"),
                    className="nucleus",
                    id="lattice-nucleus",
                ),
                *nodes,
                className="lattice-sky",
                id="lattice-sky",
            ),
            div(
                div(
                    span("Selected seal", className="kicker"),
                    h3(title),
                    p(blurb, className="muted"),
                    p(key, className="mono tiny"),
                    button(
                        "Mint this Cap",
                        type="button",
                        className="btn btn-primary",
                        **bind(self.mint, cap=key),
                    ),
                    a("Open the door it guards", href=_door_for(key), className="btn btn-ghost"),
                    className="card",
                ),
                div(
                    span("Public doors", className="kicker"),
                    h3("No authority"),
                    p("Chrome and presence stay public. Caps stay off the ring of open verbs.", className="muted"),
                    div(*pubs, className="chip-row"),
                    className="card",
                ),
                className="split",
            ),
            div(
                h2("Live Ops"),
                p("The same log Trace reads. Morph first, then Play.", className="muted tiny"),
                ul(*traces, className="cap-list") if traces else p("No Ops yet. Pulse the house.", className="muted"),
                className="card",
            ),
            id=self.id,
            className="page lattice-page",
            data_charged=charged,
        )

    @action(caps=())
    def select(self, cap: str = "orders.place", **kwargs):
        keys = {row[0] for row in SEALS}
        self.selected = cap if cap in keys else "orders.place"
        tick(self)
        return update_with(
            self,
            maybe_plan("seal-select", f"#seal-{self.selected.replace('.', '-')}", ms=120),
            extra_ops=[notify(self.selected)],
        )

    @action(caps=("orders.place",))
    def mint(self, cap: str = "orders.place", **kwargs):
        keys = {row[0] for row in SEALS}
        cap = cap if cap in keys else "orders.place"
        self.selected = cap
        self.charged = cap
        self.last = cap
        HOST.last_seal = cap
        tick(self)
        return update_with(
            self,
            maybe_plan("seal-mint", "#lattice-nucleus", ms=180),
            extra_ops=[notify(f"Cap minted · {cap}")],
        )

    @action(caps=())
    def public_fire(self, verb: str = "home.beat", **kwargs):
        allowed = {name for name, _ in PUBLIC}
        self.last = verb if verb in allowed else "home.beat"
        tick(self)
        return update_with(self, extra_ops=[notify(f"public · {self.last}")])


def _door_for(cap: str) -> str:
    return {
        "orders.place": "/bag",
        "orders.coupon": "/bag",
        "identity.verify": "/commission",
        "calendar.book": "/ledger",
        "settings.wipe": "/ledger",
        "comments.moderate": "/studio",
    }.get(cap, "/")
