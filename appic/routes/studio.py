"""Page unit: studio.py → Studio — chat, presence, inbox, timeline, moderate Cap."""
from __future__ import annotations

from appic.store import HOST
from appic.ux import (
    Component,
    MorphState,
    RefState,
    action,
    act,
    article,
    button,
    control,
    div,
    form,
    h1,
    h2,
    input_,
    li,
    maybe_plan,
    notify,
    p,
    section,
    span,
    tick,
    ul,
    update_with,
)


class Studio(Component):
    id = "studio"
    tab = MorphState("chat")
    stamp = MorphState("idle")

    def render(self):
        tab = str(self.tab or "chat")
        tabs = [
            act("studio.set_tab", lab, kind="chip-on" if tab == key else "chip", key=key)
            for key, lab in (("chat", "Chat"), ("inbox", "Inbox"), ("presence", "Presence"), ("feed", "Feed"))
        ]
        return section(
            div(
                h1("Studio"),
                p("Typing is MorphState. Lines silent. Moderate is a Cap.", className="muted"),
                className="section-head",
            ),
            div(*tabs, className="chip-row"),
            self._body(tab),
            id=self.id,
            className="page",
        )

    def _body(self, tab: str):
        if tab == "chat":
            lis = [li(x, className="hit") for x in HOST.chat[-8:]]
            return div(
                ul(*lis, className="hit-list"),
                p("Foundry is typing…", className="muted") if HOST.typing else None,
                form(
                    input_(type="text", name="text", placeholder="Write a line", className="field"),
                    button("Send", type="submit", className="btn btn-primary", **control("studio.send")),
                    className="row",
                    method="post",
                    action="/action/studio.send",
                    data_ux="1",
                ),
                div(
                    act("studio.peer_type", "Peer types", kind="ghost"),
                    act("studio.peer_done", "Peer sends", kind="ghost"),
                    className="row",
                ),
                className="card stack",
            )
        if tab == "inbox":
            n = int(HOST.unread or 0)
            items = [li(x) for x in HOST.inbox]
            return div(
                div(
                    span(f"{n} unread", className="chip"),
                    act("studio.mark_read", "Mark read", kind="text"),
                    className="spread",
                ),
                ul(*items, className="hit-list"),
                className="card stack",
            )
        if tab == "presence":
            peers = [li(span(name, className="peer")) for name in HOST.peers]
            return div(
                h2("On the floor"),
                ul(*peers, className="hit-list"),
                p("Self is named. Peers are a silent list.", className="muted tiny"),
                className="card stack",
            )
        feed = [
            ("08:10", "Shade stretched"),
            ("09:40", "Graphite cups into reduction"),
            ("11:02", "Iron bookend mill scale left raw"),
            ("14:18", "Stool oil curing"),
        ]
        return div(
            article(
                h2("Timeline"),
                ul(
                    *[
                        li(span(t, className="mono muted"), span(lab))
                        for t, lab in feed
                    ],
                    className="timeline",
                ),
                className="card stack",
            ),
            article(
                h2("Comment"),
                p("Public note. Hide is a Cap (moderate)."),
                act("studio.moderate", "Hide last note", kind="danger"),
                className="card stack",
            ),
        )

    @action(caps=())
    def set_tab(self, key: str = "chat", **kwargs):
        if key in ("chat", "inbox", "presence", "feed"):
            self.tab = key
        return update_with(self)

    @action(caps=())
    def send(self, text: str = "", **kwargs):
        text = (text or "").strip() or "…"
        HOST.chat.append(f"You: {text}")
        HOST.typing = False
        tick(self)
        return update_with(self, maybe_plan("chat", "#studio", ms=100), extra_ops=[notify("sent")])

    @action(caps=())
    def peer_type(self, **kwargs):
        HOST.typing = True
        return update_with(self)

    @action(caps=())
    def peer_done(self, **kwargs):
        HOST.typing = False
        HOST.chat.append("Foundry: held until you place.")
        tick(self)
        return update_with(self)

    @action(caps=())
    def mark_read(self, **kwargs):
        HOST.unread = 0
        tick(self)
        return update_with(self)

    @action(caps=("comments.moderate",))
    def moderate(self, **kwargs):
        if HOST.chat:
            HOST.chat = HOST.chat[:-1]
        tick(self)
        return update_with(self, extra_ops=[notify("Hidden")])
