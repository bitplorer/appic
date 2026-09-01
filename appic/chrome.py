"""Shared chrome units: toasts, command palette, banner. Not pages."""
from __future__ import annotations

from appic.store import HOST
from appic.ux import (
    Component,
    MorphState,
    RefState,
    a,
    action,
    act,
    button,
    control,
    div,
    form,
    h2,
    input_,
    li,
    p,
    span,
    tick,
    ul,
    update_with,
    notify,
    maybe_plan,
)


COMMANDS = (
    ("/", "Open table", "nav"),
    ("/atelier", "Open atelier", "nav"),
    ("/commission", "Start a commission", "nav"),
    ("/bag", "Open bag", "nav"),
    ("/board", "Open board", "nav"),
    ("/studio", "Open studio", "nav"),
    ("/lab", "Open lab", "nav"),
    ("/lattice", "Open lattice", "nav"),
    ("/trace", "Open trace", "nav"),
    ("/ledger", "Open ledger", "nav"),
    ("/enter", "Open the door", "nav"),
    ("/desk", "Sit at the desk", "nav"),
    ("/house", "Walk the house", "nav"),
    ("/visit", "Pay a visit", "nav"),
    ("/signal", "Feel the signal", "nav"),
    ("/clocks", "Watch the clocks", "nav"),
    ("/relay", "Stand in relay", "nav"),
    ("/author", "Open the author door", "nav"),
    ("/notes", "Read attach notes", "nav"),
    ("/overlay", "Inspect OverlayChrome", "nav"),
    ("lattice.mint", "Mint the selected Cap", "act"),
    ("home.beat", "Pulse the house", "act"),
    ("atelier.sort_price", "Sort atelier by price", "act"),
    ("lab.set_floor", "Open the motion floor", "act"),
    ("trace.clear", "Clear the ops log", "act"),
    ("bag.request_checkout", "Review order", "act"),
    ("ledger.book", "Book the bench (Cap)", "act"),
)


class Toasts(Component):
    id = "toasts"
    items = RefState(())
    stamp = MorphState("idle")
    _seq = RefState(0)

    def render(self):
        rows = list(self.items or ())[-4:]
        lis = [
            li(str(row.get("message", "")), id=f"toast-{row.get('id')}", className="toast")
            for row in rows
        ]
        return div(
            ul(*lis, className="toast-list") if lis else None,
            id=self.id,
            className="toasts",
            aria_live="polite",
        )

    @action(caps=())
    def push(self, message: str = "Saved", **kwargs):
        self._seq = int(self._seq or 0) + 1
        row = {"id": str(self._seq), "message": message}
        self.items = tuple(self.items or ()) + (row,)
        tick(self)
        return update_with(
            self,
            maybe_plan("toast-in", f"#toast-{row['id']}", ms=100),
            extra_ops=[notify(message)],
        )

    @action(caps=())
    def clear(self, **kwargs):
        self.items = ()
        tick(self)
        return update_with(self)


class Palette(Component):
    id = "palette"
    open = MorphState(False)
    query = MorphState("")

    def _hits(self):
        q = str(self.query or "").lower()
        rows = COMMANDS
        if q:
            rows = tuple(c for c in COMMANDS if q in c[0].lower() or q in c[1].lower())
        return rows[:8]

    def render(self):
        if not self.open:
            return div(id=self.id, className="palette", hidden=True, data_open="0")
        hits = []
        for href, label, kind in self._hits():
            if kind == "nav":
                hits.append(
                    li(
                        a(
                            span(label),
                            span(href, className="muted mono"),
                            href=href,
                            className="palette-row",
                        )
                    )
                )
            else:
                hits.append(
                    li(
                        button(
                            span(label),
                            span("intent", className="muted mono"),
                            type="button",
                            className="palette-row",
                            **control("palette.run", verb=href),
                        )
                    )
                )
        return div(
            div(className="palette-scrim", **control("palette.close")),
            div(
                p("Command", className="kicker"),
                h2("Issue an intent", id="palette-title"),
                form(
                    input_(
                        type="search",
                        name="q",
                        value=str(self.query or ""),
                        placeholder="Go, pulse, book, sort…",
                        className="field",
                        autofocus=True,
                        autocomplete="off",
                    ),
                    button("Filter", type="submit", className="sr-only", **control("palette.filter")),
                    className="palette-search",
                    method="post",
                    action="/action/palette.filter",
                    data_ux="1",
                ),
                ul(*hits, className="palette-hits") if hits else p("No matching intent.", className="muted"),
                p("Esc closes. Caps still gate protected verbs.", className="muted tiny"),
                className="palette-panel",
                role="dialog",
                aria_modal="true",
                aria_labelledby="palette-title",
            ),
            id=self.id,
            className="palette",
            data_open="1",
        )

    @action(caps=())
    def toggle(self, **kwargs):
        self.open = not bool(self.open)
        if not self.open:
            self.query = ""
        return update_with(self, maybe_plan("palette", "#palette", ms=160))

    @action(caps=())
    def close(self, **kwargs):
        self.open = False
        self.query = ""
        return update_with(self)

    @action(caps=())
    def filter(self, q: str = "", **kwargs):
        self.query = q
        self.open = True
        return update_with(self)

    @action(caps=())
    def run(self, verb: str = "", **kwargs):
        self.open = False
        HOST.notice = verb
        return update_with(self, extra_ops=[notify(verb or "intent")])


class Banner(Component):
    id = "banner"
    hidden = MorphState(False)

    def render(self):
        if self.hidden:
            return div(id=self.id, hidden=True)
        online = HOST.online
        msg = (
            "Live Caps available. Protected verbs mint authority at the door."
            if online
            else "Offline. Public morphs still run. Caps fail closed."
        )
        return div(
            span("Line", className="kicker"),
            p(msg),
            act("banner.dismiss", "Dismiss", kind="text"),
            id=self.id,
            className="banner" + ("" if online else " is-off"),
            role="status",
        )

    @action(caps=())
    def dismiss(self, **kwargs):
        self.hidden = True
        return update_with(self)


class Ribbon(Component):
    """Live Ops strip — the document naming its own last Results of Ops."""

    id = "ribbon"
    stamp = MorphState("idle")

    def render(self):
        rows = list(HOST.trace or ())[-5:]
        chips = []
        for i, row in enumerate(reversed(rows)):
            chips.append(
                li(
                    span(str(row.get("kind", "morph")), className="ribbon-kind"),
                    span(str(row.get("verb", "")), className="mono"),
                    id=f"rib-{i}",
                    className="ribbon-op",
                )
            )
        return div(
            span("Ops", className="kicker"),
            ul(*chips, className="ribbon-list") if chips else p("Awaiting intent.", className="muted tiny"),
            id=self.id,
            className="ops-ribbon",
            aria_label="Recent Results of Ops",
        )

    @action(caps=())
    def refresh(self, **kwargs):
        tick(self)
        return update_with(self)

