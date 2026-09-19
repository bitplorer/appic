"""Page unit — provenance.py → GET /provenance.

Wax genealogy. Each Cap spend is a seal. Parent is the previous seal.
PROVENANCE-1. Not /timeline. Host stock, never MorphState(list).
"""
from __future__ import annotations

from ux_compose import (
    Component,
    MorphState,
    a,
    action,
    button,
    circle,
    control,
    div,
    h1,
    h2,
    li,
    mark_dirty,
    notify,
    p,
    path,
    section,
    span,
    svg,
    ul,
    update_with,
    optional_plan,
)
from store import HOST


class Provenance(Component):
    id = "provenance"
    intent = MorphState("hold")
    dirty = MorphState("idle")

    def render(self):
        HOST.occupy("provenance")
        seals = list(HOST.seals[-12:])
        kids = [
            path(
                d="M16 24 L16 200",
                fill="none",
                stroke="currentColor",
                stroke_width="1.1",
                className="seal-spine",
            )
        ]
        nodes = []
        for i, row in enumerate(seals):
            y = 24 + i * 28
            kids.append(circle(cx="16", cy=str(y), r="5", fill="currentColor", className="seal-dot", id=f"seal-{row.get('id')}"))
            nodes.append(
                li(
                    span(str(row.get("id") or ""), className="hand-line-verb"),
                    span(str(row.get("cap") or ""), className="chip"),
                    span(f"{row.get('parent')} → {row.get('verb')}", className="hand-line"),
                    id=f"prov-{row.get('id')}",
                    className="hand-line",
                )
            )
        if not nodes:
            nodes = [li("No wax yet. Press a seal.", className="hand-line", id="prov-empty")]
        intents = (
            ("hold", "Hold"),
            ("fire", "Fire"),
            ("mend", "Mend"),
            ("gift", "Gift"),
        )
        segs = [
            button(
                label,
                type="button",
                className="seg is-on" if str(self.intent) == key else "seg",
                **control("provenance.name", intent=key),
            )
            for key, label in intents
        ]
        return section(
            span("Provenance", className="eyebrow"),
            h1("Wax remembers the hand.", className="display"),
            p(
                "A seal is one-shot Host stock. Parent is the previous seal — a chain, "
                "not a bus. Press spends wax.press. This is not /timeline. The lattice "
                "already owns that stem.",
                className="lede",
            ),
            div(
                div(
                    span("chain", className="eyebrow"),
                    svg(
                        *kids,
                        viewBox="0 0 32 220",
                        className="seal-chain",
                        id="seal-chain",
                        role="img",
                        aria_label=f"{len(HOST.seals)} seals",
                    ),
                    p(f"{HOST.seal_n} presses. Last parent is the living hinge.", className="muted"),
                    className="paper",
                    id="prov-card",
                ),
                div(
                    span("intent", className="eyebrow"),
                    h2(str(self.intent or "hold"), className="sight-title"),
                    p("Name the intent, then press. Caps are wax seals. Empty type is not a seal.", className="sight-law"),
                    div(*segs, className="segs", role="radiogroup", aria_label="Named intent"),
                    div(
                        button("Press the wax", type="button", className="btn-primary", **control("provenance.press")),
                        a("Walk the charge", href="/charge", className="btn-ghost"),
                        a("Walk the threshold", href="/threshold", className="btn-ghost"),
                        className="hero-actions",
                    ),
                    ul(*nodes, className="hands-log", role="log", aria_label="Seal chain"),
                    className="paper",
                ),
                className="kiln-split",
            ),
            id=self.id,
            className="room provenance-room",
        )

    @action(caps=())
    def name(self, intent: str = "hold"):
        allowed = ("hold", "fire", "mend", "gift")
        self.intent = intent if intent in allowed else "hold"
        mark_dirty(self)
        return update_with(self, extra_ops=[notify(str(self.intent))])

    @action(caps=())
    def press(self):
        row = HOST.press_seal(f"provenance.{self.intent}", "wax.press")
        HOST.notice = f"Seal {row['id']} holds {self.intent}."
        HOST.score_write("provenance.press", "provenance", "B")
        mark_dirty(self)
        return update_with(
            self,
            optional_plan("press", "#prov-card"),
            extra_ops=[notify(str(row["id"]))],
        )
