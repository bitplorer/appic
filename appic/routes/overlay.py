"""Page unit: overlay.py → Overlay.

OverlayChrome owns edge-overlay ids, dismiss grammar, and the open plan.
Dialog / Sheet / ActionSheet take chrome from the primitive. Markup stays
on the widget. Isolation: no ux_channel.
"""
from __future__ import annotations

from components.overlay import OverlayChrome, overlay as overlay_chrome

from ux_compose import (
    Component,
    MorphState,
    action,
    notify,
    tick,
    update_with,
    maybe_plan,
)

from appic.ux import (
    act,
    div,
    h1,
    h2,
    p,
    section,
    span,
    article,
    ul,
    li,
)

from appic.rooms import cards


class Overlay(Component):
    id = "overlay"
    stamp = MorphState("idle")
    kind = MorphState("dialog")

    def render(self):
        kinds = (
            ("dialog", "center", "Keep it · click swipe.down"),
            ("sheet", "right", "Close · click swipe.right"),
            ("actionsheet", "bottom", "Handle · click swipe.down swipe.vertical"),
        )
        rows = []
        for kind, edge, grammar in kinds:
            chrome = overlay_chrome(kind, kind=kind)
            plan = chrome.open_plan()
            rows.append(
                article(
                    span(kind, className="kicker"),
                    h2(chrome.edge),
                    ul(
                        li(f"scrim  #{chrome.scrim_id}", className="mono tiny"),
                        li(f"panel  #{chrome.panel_id}", className="mono tiny"),
                        li(f"dismiss  #{chrome.dismiss_id}", className="mono tiny"),
                        li(f"dismiss swipe  {chrome.swipe_on_dismiss()}", className="mono tiny"),
                        li(f"handle swipe  {chrome.swipe_on_handle()}", className="mono tiny"),
                        li(
                            "open plan  " + ("selectors only" if plan is not None else "None (motion absent)"),
                            className="mono tiny",
                        ),
                        className="cap-list",
                    ),
                    p(grammar, className="muted"),
                    className="card" + (" is-on" if self.kind == kind else ""),
                    id=f"chrome-{kind}",
                )
            )
        live = overlay_chrome(str(self.kind or "dialog"), kind=str(self.kind or "dialog"))
        return section(
            span("OverlayChrome · one primitive · swipe never on the root", className="eyebrow"),
            h1("Chrome"),
            p(
                "Dialog, Sheet, and ActionSheet take ids, dismiss grammar, and the open plan "
                "from OverlayChrome. Anchored popovers and Command are a different family — "
                "they do not copy these ids. Close is morph-only: after apply the panel is gone.",
                className="lede",
            ),
            div(
                act("overlay.pick", "Dialog", kind="chip-on" if self.kind == "dialog" else "chip", which="dialog"),
                act("overlay.pick", "Sheet", kind="chip-on" if self.kind == "sheet" else "chip", which="sheet"),
                act("overlay.pick", "Action sheet", kind="chip-on" if self.kind == "actionsheet" else "chip", which="actionsheet"),
                className="row",
            ),
            p(
                f"live · #{live.panel_id} · {live.swipe_on_dismiss()}",
                className="mono tiny",
            ),
            div(*rows, className="law-grid"),
            h2("Owned cards"),
            p("The widgets sit in the house. Chrome is shared. Tailwind stays on the copy.", className="muted tiny"),
            div(*cards("dialog", "sheet", "actionsheet"), className="kit-grid"),
            id=self.id,
            className="page",
        )

    @action(caps=())
    def pick(self, which: str = "dialog", **kwargs):
        if which not in {"dialog", "sheet", "actionsheet"}:
            which = "dialog"
        self.kind = which
        tick(self)
        chrome = overlay_chrome(which, kind=which)
        plan = chrome.open_plan() or maybe_plan("overlay-pick", f"#chrome-{which}", ms=140)
        return update_with(self, plan, extra_ops=[notify(f"chrome · {which}")])
