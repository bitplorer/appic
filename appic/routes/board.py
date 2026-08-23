"""Page unit: board.py → Board — kanban, table bulk, undo, optimistic."""
from __future__ import annotations

from appic.store import HOST
from appic.ux import (
    Component,
    MorphState,
    RefState,
    action,
    act,
    div,
    h1,
    h2,
    h3,
    li,
    maybe_plan,
    notify,
    p,
    section,
    span,
    table,
    tbody,
    td,
    th,
    thead,
    tick,
    tr,
    ul,
    update_with,
)

COLS = (("cut", "Cut"), ("make", "Make"), ("keep", "Keep"))


class Board(Component):
    id = "board"
    view = MorphState("kanban")
    sort = MorphState("title")
    selected = RefState(())
    undo = RefState(())
    pending = RefState("")
    stamp = MorphState("idle")

    def render(self):
        view = str(self.view or "kanban")
        body = self._kanban() if view == "kanban" else self._table()
        return section(
            div(
                div(
                    h1("Board"),
                    p("Move is public. Archive would take a Cap. Optimistic paint, then Host.", className="muted"),
                ),
                div(
                    act("board.set_view", "Kanban", kind="chip-on" if view == "kanban" else "chip", key="kanban"),
                    act("board.set_view", "Table", kind="chip-on" if view == "table" else "chip", key="table"),
                    act("board.undo_move", "Undo", kind="ghost") if HOST.board else None,
                    className="row",
                ),
                className="section-head spread",
            ),
            body,
            id=self.id,
            className="page",
        )

    def _kanban(self):
        cols = []
        for key, lab in COLS:
            cards = [c for c in HOST.board if c["col"] == key]
            lis = []
            for c in cards:
                pending = self.pending == c["id"]
                lis.append(
                    li(
                        h3(c["title"]),
                        p(HOST.money(c["price"]), className="price"),
                        div(
                            *[
                                act("board.move", dest, kind="text", cid=c["id"], col=dest)
                                for dest, _ in COLS
                                if dest != key
                            ],
                            className="row",
                        ),
                        className="kanban-card" + (" is-pending" if pending else ""),
                        id=f"card-{c['id']}",
                    )
                )
            cols.append(
                div(
                    span(f"{lab} · {len(cards)}", className="kicker"),
                    ul(*lis, className="kanban-list") if lis else p("Empty column.", className="muted tiny"),
                    className="kanban-col",
                    id=f"col-{key}",
                )
            )
        return div(*cols, className="kanban")

    def _table(self):
        idx = {"title": "title", "stage": "col", "price": "price"}.get(str(self.sort or "title"), "title")
        rows = sorted(HOST.board, key=lambda r: str(r.get(idx, "")))
        sel = set(self.selected or ())
        body_rows = []
        for r in rows:
            on = r["id"] in sel
            body_rows.append(
                tr(
                    td(act("board.toggle", "On" if on else "Sel", kind="chip-on" if on else "chip", cid=r["id"])),
                    td(r["title"]),
                    td(r["col"]),
                    td(HOST.money(r["price"]), className="mono"),
                    className="is-on" if on else "",
                )
            )
        return div(
            div(
                act("board.sort", "Title", kind="chip-on" if self.sort == "title" else "chip", key="title"),
                act("board.sort", "Stage", kind="chip-on" if self.sort == "stage" else "chip", key="stage"),
                act("board.sort", "Price", kind="chip-on" if self.sort == "price" else "chip", key="price"),
                act("board.bulk_keep", "Move selected to keep", kind="ghost"),
                className="chip-row",
            ),
            table(
                thead(tr(th(""), th("Commission"), th("Stage"), th("Hold"))),
                tbody(*body_rows),
                className="data",
            ),
            className="stack",
        )

    @action(caps=())
    def set_view(self, key: str = "kanban", **kwargs):
        if key in ("kanban", "table"):
            self.view = key
        return update_with(self)

    @action(caps=())
    def sort(self, key: str = "title", **kwargs):
        self.sort = key
        return update_with(self)

    @action(caps=())
    def move(self, cid: str = "", col: str = "make", **kwargs):
        prev = None
        for c in HOST.board:
            if c["id"] == cid:
                prev = c["col"]
                c["col"] = col
                break
        self.undo = tuple(self.undo or ()) + ((cid, prev),)
        self.pending = ""
        tick(self)
        return update_with(self, maybe_plan("card", f"#card-{cid}", ms=120), extra_ops=[notify(f"→ {col}")])

    @action(caps=())
    def undo_move(self, **kwargs):
        stack = list(self.undo or ())
        if not stack:
            return update_with(self, extra_ops=[notify("Nothing to undo")])
        cid, col = stack.pop()
        self.undo = tuple(stack)
        for c in HOST.board:
            if c["id"] == cid and col:
                c["col"] = col
        tick(self)
        return update_with(self, extra_ops=[notify("Undone")])

    @action(caps=())
    def toggle(self, cid: str = "", **kwargs):
        have = set(self.selected or ())
        if cid in have:
            have.remove(cid)
        else:
            have.add(cid)
        self.selected = tuple(sorted(have))
        tick(self)
        return update_with(self)

    @action(caps=())
    def bulk_keep(self, **kwargs):
        for c in HOST.board:
            if c["id"] in set(self.selected or ()):
                c["col"] = "keep"
        self.selected = ()
        tick(self)
        return update_with(self, extra_ops=[notify("Moved to keep")])
