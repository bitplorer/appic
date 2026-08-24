"""Page unit: home.py → Home."""
from __future__ import annotations

from appic.store import HOST
from appic.ux import (
    Component,
    MorphState,
    RefState,
    a,
    action,
    act,
    article,
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
    notify,
    p,
    section,
    span,
    tick,
    ul,
    update_with,
)


class Home(Component):
    id = "home"
    greeting = MorphState("The table is lit")
    stamp = MorphState("idle")
    query = MorphState("")

    def render(self):
        n = int(HOST.pulse or 0)
        k = HOST.kpi
        q = str(self.query or HOST.intent or "")
        return section(
            div(
                span("page unit · App.mount · progressive L3", className="eyebrow"),
                h1(
                    span(str(self.greeting), className="display"),
                    span("APPIC", className="wordmark"),
                    className="hero-title",
                ),
                p(
                    "A foundry OS authored as legal Results of Ops. "
                    "You issue intent. The document morphs. Caps gate the verbs that charge.",
                    className="lede",
                ),
                div(
                    button(
                        f"Pulse · {n}",
                        type="button",
                        className="btn btn-primary",
                        **control("home.beat"),
                    ),
                    a("Open atelier", href="/atelier", className="btn btn-ghost"),
                    button(
                        "Command",
                        type="button",
                        className="btn btn-text",
                        **control("palette.toggle"),
                    ),
                    className="hero-actions",
                ),
                form(
                    input_(
                        type="search",
                        name="q",
                        value=q,
                        placeholder="Name an intent — flax, iron, stool…",
                        className="field field-lg",
                        autocomplete="off",
                    ),
                    button("Hold", type="submit", className="btn btn-primary", **control("home.intend")),
                    className="intent-row",
                    method="post",
                    action="/action/home.intend",
                    data_ux="1",
                ),
                className="hero",
            ),
            div(
                article(
                    h3("Path law"),
                    p("URL is filesystem. Class name never leaks into the path."),
                    className="card",
                ),
                article(
                    h3("Two clocks"),
                    p("MorphState names the pose. RefState holds magnitude. Stamp dirties."),
                    className="card",
                ),
                article(
                    h3("Cap law"),
                    p("Checkout, book, redeem, wipe, verify — fail closed without a Cap."),
                    className="card",
                ),
                className="law-grid",
            ),
            div(
                div(
                    h2("House"),
                    p("KPI values live on the Host. Stamp is the only dirty tick.", className="muted"),
                    className="section-head",
                ),
                div(
                    _kpi("Open", k["open"]),
                    _kpi("Fired", k["fired"]),
                    _kpi("Held", k["held"]),
                    _kpi("Placed", k["placed"]),
                    className="kpi-row",
                ),
                className="house",
            ),
            div(
                h2("Presence"),
                p("Peers are Host memory. You are named, not counted.", className="muted tiny"),
                ul(*[li(x, className="peer") for x in HOST.peers], className="hit-list"),
                className="card",
            ),
            id=self.id,
            className="page",
        )

    @action(caps=())
    def beat(self, **kwargs):
        HOST.pulse = int(HOST.pulse or 0) + 1
        self.greeting = "Still here" if HOST.pulse > 3 else "The table is lit"
        tick(self)
        return update_with(
            self,
            maybe_plan("pulse", "#home", ms=140),
            extra_ops=[notify(f"pulse={HOST.pulse}")],
        )

    @action(caps=())
    def intend(self, q: str = "", **kwargs):
        HOST.intent = (q or "").strip()
        self.query = HOST.intent
        tick(self)
        msg = f"Intent held · {HOST.intent}" if HOST.intent else "Intent cleared"
        return update_with(self, extra_ops=[notify(msg)])


def _kpi(label: str, n: int):
    return div(
        span(str(n), className="kpi-n"),
        span(label, className="kpi-l"),
        className="kpi",
    )
