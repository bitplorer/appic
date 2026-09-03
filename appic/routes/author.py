"""Page unit: author.py → Author.

The one author door (ADR 0004). Official helpers from ux_compose.author —
act, field, status, tick, maybe_plan / maybe_fade / maybe_slide — made visible.
Isolation: no ux_channel.
"""
from __future__ import annotations

from ux_compose import (
    Component,
    MorphState,
    RefState,
    action,
    attach_notes,
    field,
    maybe_fade,
    maybe_plan,
    maybe_slide,
    notify,
    status,
    tick,
    update_with,
    act,
)

from appic.ux import (
    div,
    h1,
    h2,
    p,
    section,
    span,
    article,
    form,
    button,
    control,
)

from appic.store import HOST


def _slide_dist() -> float:
    try:
        from ux_motion import tokens as _tok

        return float(_tok.dist("md"))
    except Exception:
        return 24.0


class Author(Component):
    id = "author"
    note = MorphState("The author door is one.")
    query = MorphState("")
    stamp = MorphState("idle")
    kind = MorphState("plan")

    def render(self):
        q = str(self.query or "")
        kind = str(self.kind or "plan")
        notes = []
        try:
            for item in attach_notes()[:6]:
                notes.append(
                    article(
                        span(item.door, className="kicker"),
                        p(f"wanted {item.wanted} · kept L{item.level_kept}", className="mono tiny"),
                        p(item.reason, className="muted tiny"),
                        className="card",
                    )
                )
        except Exception:
            notes = [p("No attach notes yet.", className="muted")]
        return section(
            span("one author door · ADR 0004 · ux_compose.author", className="eyebrow"),
            h1("Author"),
            p(
                "Public helpers live on ux_compose. act, field, status, tick, maybe_*. "
                "examples/_common.py re-exports the same objects. There is no second helper world.",
                className="lede",
            ),
            form(
                field("q", q, placeholder="Name a presence…"),
                button("Hold", type="submit", className="btn btn-primary", **control("author.hold")),
                className="intent-row",
                method="post",
                action="/action/author.hold",
                data_ux="1",
            ),
            status(str(self.note), kind="note"),
            div(
                article(
                    span("act()", className="kicker"),
                    h2("Intent as a POST form"),
                    p("Official act() posts /act/{action}. APPIC aliases it onto /action/{name}.", className="muted"),
                    act("author.pulse", "Pulse via act()", kind="primary", target="#author"),
                    className="card",
                ),
                article(
                    span("tick()", className="kicker"),
                    h2("Stamp flip"),
                    p(f"stamp = {self.stamp}. RefState-only mutations need a qualitative tick to morph.", className="muted"),
                    act("author.flip", "Flip stamp", kind="secondary", target="#author"),
                    className="card",
                ),
                article(
                    span("maybe_*", className="kicker"),
                    h2("Plans degrade"),
                    p("maybe_plan / maybe_fade / maybe_slide return None when ux-motion is absent.", className="muted"),
                    div(
                        act("author.play", "Rise", kind="secondary", target="#author", recipe="plan"),
                        act("author.play", "Fade", kind="secondary", target="#author", recipe="fade"),
                        act("author.play", "Slide", kind="secondary", target="#author", recipe="slide"),
                        className="row",
                    ),
                    p(f"last recipe · {kind} · slide dist {_slide_dist()}", className="mono tiny"),
                    className="card",
                ),
                className="law-grid",
            ),
            div(
                article(
                    span("act(..., on=)", className="kicker"),
                    h2("Channel grammar on the form"),
                    p("on= stamps data-channel-on. One demonstration. The door is still /act/{action}.", className="muted"),
                    act("author.pulse", "Pulse on longpress", kind="secondary", target="#author", on="longpress"),
                    p("data-channel-on=\"longpress\"", className="mono tiny"),
                    className="card",
                ),
                article(
                    span("maybe_slide dist", className="kicker"),
                    h2("Motion tokens"),
                    p("ux_motion.tokens.dist(\"md\") else 24.0. prev → −dist, next → +dist.", className="muted"),
                    p(str(_slide_dist()), className="mono", id="author-dist"),
                    className="card",
                ),
                className="split",
            ),
            div(
                h2("Attach notes"),
                p("Silence was the defect. Step-downs are visible, per-App.", className="muted tiny"),
                div(*notes, className="law-grid") if notes else p("Clean attach.", className="muted"),
                className="stack",
            ),
            id=self.id,
            className="page",
            data_stamp=str(self.stamp),
        )

    @action(caps=())
    def hold(self, q: str = "", **kwargs):
        self.query = (q or "").strip()
        self.note = f"Held · {self.query}" if self.query else "Cleared"
        HOST.intent = str(self.query)
        tick(self)
        return update_with(self, extra_ops=[notify(self.note)])

    @action(caps=())
    def pulse(self, **kwargs):
        HOST.pulse = int(HOST.pulse or 0) + 1
        self.note = f"Pulse {HOST.pulse} via act()"
        tick(self)
        return update_with(
            self,
            maybe_plan("author-pulse", "#author", ms=140),
            extra_ops=[notify(self.note)],
        )

    @action(caps=())
    def flip(self, **kwargs):
        tick(self)
        self.note = f"stamp · {self.stamp}"
        return update_with(self, extra_ops=[notify(self.note)])

    @action(caps=())
    def play(self, recipe: str = "plan", **kwargs):
        self.kind = recipe or "plan"
        tick(self)
        plan = None
        if self.kind == "fade":
            plan = maybe_fade("author-fade", "#author", ms=160)
        elif self.kind == "slide":
            plan = maybe_slide("author-slide", "#author", direction="next", ms=180)
        else:
            plan = maybe_plan("author-rise", "#author", ms=140)
        self.note = f"recipe · {self.kind}"
        return update_with(self, plan, extra_ops=[notify(self.note)])
