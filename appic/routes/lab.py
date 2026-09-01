"""Page unit: lab.py → Lab — remaining catalog patterns as a working floor."""
from __future__ import annotations

from appic.store import BY_SKU, CATALOG, HOST
from appic.ux import (
    Component,
    MorphState,
    RefState,
    a,
    action,
    act,
    aside,
    button,
    control,
    div,
    form,
    h1,
    h2,
    h3,
    input_,
    li,
    maybe_plan,
    maybe_share,
    maybe_stagger,
    morph_play,
    notify,
    p,
    section,
    span,
    tick,
    ul,
    update_with,
)

FLOORS = (
    ("house", "House"),
    ("fields", "Fields"),
    ("chrome", "Chrome"),
    ("motion", "Motion"),
)
TREE = (
    ("house", None, "House"),
    ("linen", "house", "Linen"),
    ("oak", "house", "Oak"),
    ("wool", "house", "Wool"),
    ("iron", "house", "Iron"),
)


class Lab(Component):
    id = "lab"
    floor = MorphState("house")
    expanded = MorphState(("house",))
    selected = MorphState("linen")
    carousel = RefState(0)
    order = RefState(tuple(p["sku"] for p in CATALOG))
    ready = MorphState("ready")
    combo_q = MorphState("")
    combo_v = MorphState("")
    chip = MorphState("all")
    editing = MorphState("")
    draft = MorphState("")
    copied = MorphState(False)
    pct = RefState(36)
    phase = MorphState("run")
    stars = MorphState("four")
    acc = MorphState(("tree",))
    drop_open = MorphState(False)
    drop_val = MorphState("oil")
    drawer = MorphState(False)
    pop = MorphState(False)
    overflow = MorphState(False)
    hop = MorphState("a")
    stamp = MorphState("idle")

    def render(self):
        floor = str(self.floor or "house")
        tabs = [
            act(
                "lab.set_floor",
                lab,
                kind="chip-on" if key == floor else "chip",
                key=key,
            )
            for key, lab in FLOORS
        ]
        body = {
            "house": self._house(),
            "fields": self._fields(),
            "chrome": self._chrome(),
            "motion": self._motion(),
        }.get(floor, self._house())
        return section(
            div(
                span("page unit · remaining 99%", className="eyebrow"),
                h1("Lab"),
                p(
                    "A working floor, not a zoo. Tabs are MorphState. "
                    "Each verb still morphs one id.",
                    className="lede",
                ),
                div(*tabs, className="chip-row", role="tablist"),
                className="section-head",
            ),
            body,
            id=self.id,
            className="page",
            data_floor=floor,
        )

    def _house(self):
        opened = set(self.expanded or ())
        sel = str(self.selected or "linen")
        nodes = []
        for key, parent, lab in TREE:
            if parent and parent not in opened:
                continue
            pad = " is-child" if parent else ""
            nodes.append(
                li(
                    button(
                        ("▾ " if key in opened and not parent else "▸ " if not parent else "· ")
                        + lab,
                        type="button",
                        className="tree-node" + (" is-on" if key == sel else ""),
                        **control("lab.tree_pick", key=key),
                    ),
                    className="tree-row" + pad,
                    id=f"tree-{key}",
                )
            )
        n = int(self.carousel or 0) % len(CATALOG)
        piece = CATALOG[n]
        skus = list(self.order or ())
        rows = []
        for sku in skus:
            prod = BY_SKU.get(sku)
            if not prod:
                continue
            rows.append(
                li(
                    span(prod["name"]),
                    button("Up", type="button", className="btn btn-text", **control("lab.up", sku=sku)),
                    className="hit",
                    id=f"ord-{sku}",
                )
            )
        activity = [li(x, className="hit") for x in (HOST.activity or ())[-6:]]
        empty = str(self.ready or "ready")
        stage = {
            "loading": div(div(className="skeleton"), div(className="skeleton"), className="stack"),
            "error": div(
                p("The shelf did not answer.", className="empty-title"),
                act("lab.retry", "Retry", kind="primary"),
                className="empty-card",
            ),
            "empty": p("Nothing on this floor.", className="empty"),
            "ready": ul(*rows, className="hit-list") if rows else p("Empty order.", className="empty"),
        }[empty if empty in ("loading", "error", "empty", "ready") else "ready"]
        return div(
            div(
                div(
                    h2("Tree"),
                    p("Expanded is a set of names. Selected is a name.", className="muted tiny"),
                    ul(*nodes, className="tree"),
                    className="card",
                ),
                div(
                    h2("Carousel"),
                    p(f"{n + 1} / {len(CATALOG)}", className="muted tiny"),
                    h3(piece["name"], id=f"car-{piece['sku']}"),
                    p(piece["line"], className="muted"),
                    div(
                        act("lab.prev", "Prev", kind="ghost"),
                        act("lab.next", "Next", kind="primary"),
                        className="row",
                    ),
                    className="card",
                ),
                className="split",
            ),
            div(
                div(
                    h2("Reorder · empty · retry"),
                    p("List lives on RefState. Stage is a named MorphState.", className="muted tiny"),
                    div(
                        act("lab.stage", "Ready", kind="chip-on" if empty == "ready" else "chip", key="ready"),
                        act("lab.stage", "Load", kind="chip-on" if empty == "loading" else "chip", key="loading"),
                        act("lab.stage", "Error", kind="chip-on" if empty == "error" else "chip", key="error"),
                        act("lab.stage", "Empty", kind="chip-on" if empty == "empty" else "chip", key="empty"),
                        className="chip-row",
                    ),
                    stage,
                    className="card",
                ),
                div(
                    h2("Activity"),
                    p("Host owns the rest of the log. has_more is a boolean.", className="muted tiny"),
                    ul(*activity, className="hit-list") if activity else p("Quiet.", className="empty"),
                    className="card",
                ),
                className="split",
            ),
            className="stack",
        )

    def _fields(self):
        q = str(self.combo_q or "")
        val = str(self.combo_v or "")
        names = [p["name"] for p in CATALOG]
        hits = [x for x in names if q.lower() in x.lower()] if q else names
        combo_rows = [
            li(
                button(x, type="button", className="palette-row", **control("lab.combo_pick", key=x)),
                className="palette-hits",
            )
            for x in hits[:5]
        ]
        chip = str(self.chip or "all")
        stars = str(self.stars or "four")
        STAR = ("one", "two", "three", "four", "five")
        n = int(self.pct or 0)
        band = "empty" if n == 0 else "low" if n < 50 else "mid" if n < 100 else "full"
        stock_sku = "lamp-flax"
        qty = int(HOST.stock.get(stock_sku, 0))
        sband = "out" if qty <= 0 else "low" if qty < 4 else "ok"
        return div(
            div(
                div(
                    h2("Combobox"),
                    p(f"Chosen · {val or 'none'}", className="muted tiny"),
                    form(
                        input_(
                            type="search",
                            name="q",
                            value=q,
                            placeholder="Filter the house…",
                            className="field",
                            autocomplete="off",
                        ),
                        button("Filter", type="submit", className="btn btn-ghost", **control("lab.combo_q")),
                        className="intent-row",
                        method="post",
                        action="/action/lab.combo_q",
                        data_ux="1",
                    ),
                    ul(*combo_rows, className="hit-list"),
                    className="card",
                ),
                div(
                    h2("Chips · inline · copy"),
                    div(
                        act("lab.set_chip", "All", kind="chip-on" if chip == "all" else "chip", key="all"),
                        act("lab.set_chip", "Ready", kind="chip-on" if chip == "ready" else "chip", key="ready"),
                        act("lab.set_chip", "Make", kind="chip-on" if chip == "make" else "chip", key="make"),
                        className="chip-row",
                    ),
                    p(HOST.inline or "Flax shade", className="lede")
                    if not self.editing
                    else form(
                        input_(
                            type="text",
                            name="text",
                            value=str(self.draft or HOST.inline),
                            className="field",
                        ),
                        button("Save", type="submit", className="btn btn-primary", **control("lab.save_inline")),
                        className="intent-row",
                        method="post",
                        action="/action/lab.save_inline",
                        data_ux="1",
                    ),
                    div(
                        act("lab.edit", "Edit", kind="ghost"),
                        act("lab.copy", "Copy", kind="ghost"),
                        span("Copied" if self.copied else "", className="muted tiny"),
                        className="row",
                    ),
                    className="card",
                ),
                className="split",
            ),
            div(
                div(
                    h2("Progress · rating · stock"),
                    p(
                        span(f"{n}%", className="num"),
                        span(str(self.phase), className="chip"),
                        className="counter-face",
                    ),
                    div(className=f"bar bar-{band}"),
                    div(
                        act("lab.bump", "Advance", kind="primary"),
                        act("lab.finish", "Finish", kind="ghost"),
                        className="row",
                    ),
                    div(
                        *[
                            act(
                                "lab.rate",
                                "★",
                                kind="chip-on" if STAR.index(stars) >= i else "chip",
                                key=STAR[i],
                            )
                            for i in range(5)
                        ],
                        className="chip-row",
                    ),
                    p(
                        f"{BY_SKU[stock_sku]['name']} · {qty} · {sband}",
                        className="muted",
                        id="stock-lamp-flax",
                    ),
                    act("lab.sell", "Sell one", kind="ghost", sku=stock_sku),
                    className="card",
                ),
                className="split",
            ),
            className="stack",
        )

    def _chrome(self):
        acc = set(self.acc or ())
        panels = []
        for key, title, body in (
            ("tree", "Tree law", "Expanded is a tuple of names. Nested pages are siblings, not a second tree."),
            ("xor", "XOR law", "Plans carry recipes only. Morph HTML comes from live render()."),
            ("cap", "Cap law", "Protected verbs mint at the door. Isolation holds."),
        ):
            panels.append(
                div(
                    button(
                        title,
                        type="button",
                        className="acc-head",
                        **control("lab.toggle_acc", key=key),
                    ),
                    p(body, className="muted") if key in acc else None,
                    className="acc-panel" + (" is-open" if key in acc else ""),
                    id=f"acc-{key}",
                )
            )
        drop = None
        if self.drop_open:
            drop = ul(
                li(act("lab.drop_pick", "Oil", kind="text", key="oil")),
                li(act("lab.drop_pick", "Wax", kind="text", key="wax")),
                li(act("lab.drop_pick", "Raw", kind="text", key="raw")),
                className="drop-menu",
            )
        drawer = None
        if self.drawer:
            drawer = div(
                div(className="scrim", **control("lab.close_drawer")),
                aside(
                    h2("Peek"),
                    p(f"{HOST.count()} in the bag. Not a second Document.", className="muted"),
                    act("lab.close_drawer", "Close", kind="ghost"),
                    className="drawer-panel",
                ),
                className="drawer",
                id="lab-drawer",
            )
        pop = (
            div(p("Origin-aware. Caps stay off chrome.", className="muted tiny"), className="popover")
            if self.pop
            else None
        )
        over = (
            ul(
                li(act("lab.overflow", "Close", kind="text")),
                li(a_nav()),
                className="overflow-menu",
            )
            if self.overflow
            else None
        )
        return div(
            div(*panels, className="accordion card"),
            div(
                h2("Dropdown · drawer · popover · overflow"),
                div(
                    div(
                        button(
                            f"Finish · {self.drop_val}",
                            type="button",
                            className="btn btn-ghost",
                            **control("lab.toggle_drop"),
                        ),
                        drop,
                        className="drop",
                    ),
                    act("lab.toggle_drawer", "Drawer", kind="ghost"),
                    div(
                        button("Popover", type="button", className="btn btn-ghost", **control("lab.toggle_pop")),
                        pop,
                        className="pop-wrap",
                    ),
                    div(
                        button("Overflow", type="button", className="btn btn-ghost", **control("lab.toggle_over")),
                        over,
                        className="pop-wrap",
                    ),
                    className="row",
                ),
                drawer,
                className="card",
            ),
            className="stack",
        )

    def _motion(self):
        side = str(self.hop or "a")
        leave = "#hop-a" if side == "a" else "#hop-b"
        arrive = "#hop-b" if side == "a" else "#hop-a"
        return div(
            div(
                h2("Morph-then-Play"),
                p("Plan has no html=. Patch is live render().", className="muted tiny"),
                div(
                    div("A", id="hop-a", className="hop" + (" is-on" if side == "a" else "")),
                    div("B", id="hop-b", className="hop" + (" is-on" if side == "b" else "")),
                    className="hop-row",
                ),
                act("lab.hop", "Hop", kind="primary"),
                className="card",
            ),
            div(
                h2("Shared element"),
                p("Leave and arrive must exist after morph. Share id is identity.", className="muted tiny"),
                div(
                    span("Shelf", id="share-leave", className="share-seat"),
                    span("Bag", id="share-arrive", className="share-seat"),
                    className="hop-row",
                ),
                act("lab.share", "Share flax", kind="ghost"),
                className="card",
            ),
            className="split",
        )

    @action(caps=())
    def set_floor(self, key: str = "house", **kwargs):
        self.floor = key if key in {k for k, _ in FLOORS} else "house"
        tick(self)
        return update_with(self, maybe_plan("lab-floor", "#lab", ms=160))

    @action(caps=())
    def tree_pick(self, key: str = "linen", **kwargs):
        opened = set(self.expanded or ())
        if key in {k for k, p, _ in TREE if p is None}:
            if key in opened:
                opened.remove(key)
            else:
                opened.add(key)
            self.expanded = tuple(opened)
        self.selected = key
        return update_with(self)

    @action(caps=())
    def prev(self, **kwargs):
        self.carousel = (int(self.carousel or 0) - 1) % len(CATALOG)
        tick(self)
        sku = CATALOG[self.carousel]["sku"]
        return update_with(self, maybe_plan("car", f"#car-{sku}", ms=120))

    @action(caps=())
    def next(self, **kwargs):
        self.carousel = (int(self.carousel or 0) + 1) % len(CATALOG)
        tick(self)
        sku = CATALOG[self.carousel]["sku"]
        return update_with(self, maybe_plan("car", f"#car-{sku}", ms=120))

    @action(caps=())
    def up(self, sku: str = "", **kwargs):
        rows = list(self.order or ())
        if sku in rows:
            i = rows.index(sku)
            if i:
                rows[i - 1], rows[i] = rows[i], rows[i - 1]
            self.order = tuple(rows)
            tick(self)
        ids = [f"#ord-{s}" for s in (self.order or ())]
        return update_with(self, maybe_stagger("reorder", ids, ms=70))

    @action(caps=())
    def stage(self, key: str = "ready", **kwargs):
        self.ready = key if key in {"ready", "loading", "error", "empty"} else "ready"
        tick(self)
        return update_with(self)

    @action(caps=())
    def retry(self, **kwargs):
        self.ready = "ready"
        tick(self)
        return update_with(self, extra_ops=[notify("shelf recovered")])

    @action(caps=())
    def combo_q(self, q: str = "", **kwargs):
        self.combo_q = q
        return update_with(self)

    @action(caps=())
    def combo_pick(self, key: str = "", **kwargs):
        self.combo_v = key
        self.combo_q = key
        return update_with(self, extra_ops=[notify(key)])

    @action(caps=())
    def set_chip(self, key: str = "all", **kwargs):
        self.chip = key
        return update_with(self)

    @action(caps=())
    def edit(self, **kwargs):
        self.editing = "on"
        self.draft = HOST.inline
        return update_with(self)

    @action(caps=())
    def save_inline(self, text: str = "", **kwargs):
        HOST.inline = (text or "").strip() or HOST.inline
        self.editing = ""
        tick(self)
        return update_with(self, extra_ops=[notify("held")])

    @action(caps=())
    def copy(self, **kwargs):
        self.copied = True
        HOST.copied = HOST.inline
        return update_with(self, extra_ops=[notify("copied")])

    @action(caps=())
    def bump(self, **kwargs):
        self.pct = min(100, int(self.pct or 0) + 12)
        self.phase = "done" if self.pct >= 100 else "run"
        tick(self)
        return update_with(self)

    @action(caps=())
    def finish(self, **kwargs):
        self.pct = 100
        self.phase = "done"
        tick(self)
        return update_with(self)

    @action(caps=())
    def rate(self, key: str = "four", **kwargs):
        self.stars = key
        return update_with(self)

    @action(caps=())
    def sell(self, sku: str = "lamp-flax", **kwargs):
        HOST.stock[sku] = max(0, int(HOST.stock.get(sku, 0)) - 1)
        tick(self)
        return update_with(self, extra_ops=[notify("sold")])

    @action(caps=())
    def toggle_acc(self, key: str = "", **kwargs):
        cur = set(self.acc or ())
        if key in cur:
            cur.remove(key)
        elif key:
            cur.add(key)
        self.acc = tuple(cur)
        return update_with(self)

    @action(caps=())
    def toggle_drop(self, **kwargs):
        self.drop_open = not bool(self.drop_open)
        return update_with(self)

    @action(caps=())
    def drop_pick(self, key: str = "oil", **kwargs):
        self.drop_val = key
        self.drop_open = False
        return update_with(self)

    @action(caps=())
    def toggle_drawer(self, **kwargs):
        self.drawer = not bool(self.drawer)
        return update_with(self, maybe_plan("drawer", "#lab-drawer", ms=180))

    @action(caps=())
    def close_drawer(self, **kwargs):
        self.drawer = False
        return update_with(self)

    @action(caps=())
    def toggle_pop(self, **kwargs):
        self.pop = not bool(self.pop)
        self.overflow = False
        return update_with(self)

    @action(caps=())
    def toggle_over(self, **kwargs):
        self.overflow = not bool(self.overflow)
        self.pop = False
        return update_with(self)

    @action(caps=())
    def overflow(self, **kwargs):
        self.overflow = False
        return update_with(self)

    @action(caps=())
    def hop(self, **kwargs):
        self.hop = "b" if self.hop == "a" else "a"
        target = "#hop-b" if self.hop == "b" else "#hop-a"
        plan = maybe_plan("hop", target, ms=140)
        if plan is not None:
            return morph_play(target, plan)
        tick(self)
        return update_with(self)

    @action(caps=())
    def share(self, **kwargs):
        plan = maybe_share("flax", "sku-flax", "#share-leave", "#share-arrive", ms=160)
        return update_with(self, plan, extra_ops=[notify("shared flax")])


def a_nav():
    return a("Open bag", href="/bag", className="palette-row")
