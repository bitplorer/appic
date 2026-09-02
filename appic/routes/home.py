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
    bind,
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
from ux_compose import HAS_DOM, Level, __version__

BENCHES = (
    ("mira", "Mira", "bench · flax"),
    ("jules", "Jules", "glaze · iron"),
    ("you", "You", "table · intent"),
)


class Home(Component):
    id = "home"
    greeting = MorphState("The table is lit")
    stamp = MorphState("idle")
    query = MorphState("")
    bench = MorphState("you")

    def render(self):
        n = int(HOST.pulse or 0)
        k = HOST.kpi
        q = str(self.query or HOST.intent or "")
        last_ops = list(HOST.trace or ())[-3:]
        op_lis = [
            li(
                span(str(row.get("kind", "morph")), className="chip"),
                span(str(row.get("verb", "")), className="mono"),
                className="cap-row",
            )
            for row in reversed(last_ops)
        ]
        benches = [
            button(
                span(name, className="bench-name"),
                span(role, className="muted tiny"),
                type="button",
                className="bench" + (" is-on" if self.bench == key else ""),
                id=f"bench-{key}",
                **control("home.seat", who=key),
            )
            for key, name, role in BENCHES
        ]
        return section(
            div(
                span("page unit · App.mount · progressive L3 · Morph then Play", className="eyebrow"),
                h1(
                    span(str(self.greeting), className="display"),
                    span("APPIC", className="wordmark"),
                    className="hero-title",
                ),
                p(
                    "A foundry OS authored as legal Results of Ops. "
                    "You issue intent. The document morphs. Caps gate the verbs that charge. "
                    "The kit is a house you own. Signal is a grammar you can feel.",
                    className="lede",
                ),
                div(
                    button(
                        f"Pulse · {n}",
                        type="button",
                        className="btn btn-primary",
                        **bind(self.beat),
                    ),
                    a("Open door", href="/enter", className="btn btn-ghost"),
                    a("Walk the house", href="/house", className="btn btn-ghost"),
                    a("Author door", href="/author", className="btn btn-ghost"),
                    button(
                        "Command",
                        type="button",
                        className="btn btn-text",
                        **control("palette.toggle"),
                    ),
                    className="hero-actions",
                ),
                div(
                    span(f"L{int(Level(HOST.level) if HOST.level else 0)}", className="chip is-on"),
                    span(f"ux-compose {__version__}", className="chip"),
                    span(f"HAS_DOM · {'on' if HAS_DOM else 'shim'}", className="chip"),
                    className="chip-row",
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
                    p("Checkout, book, redeem, wipe, verify, mint — fail closed without a Cap."),
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
                h2("Benches"),
                p("Presence is named, never counted. Seat is MorphState.", className="muted tiny"),
                div(*benches, className="bench-row"),
                className="card",
            ),
            div(
                h2("Last Ops"),
                p("The lattice and Trace read the same Host log.", className="muted tiny"),
                ul(*op_lis, className="cap-list") if op_lis else p("Pulse to write the first Op.", className="muted"),
                a("See the lattice", href="/lattice", className="btn btn-text"),
                className="card",
            ),
            id=self.id,
            className="page",
            data_pulse=str(n),
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

    @action(caps=())
    def seat(self, who: str = "you", **kwargs):
        keys = {k for k, _, _ in BENCHES}
        self.bench = who if who in keys else "you"
        tick(self)
        return update_with(
            self,
            maybe_plan("seat", f"#bench-{self.bench}", ms=120),
            extra_ops=[notify(f"seated · {self.bench}")],
        )


def _kpi(label: str, n: int):
    return div(
        span(str(n), className="kpi-n"),
        span(label, className="kpi-l"),
        className="kpi",
    )
