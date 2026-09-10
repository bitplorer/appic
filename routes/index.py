"""Table — constellation of rooms around an Intent nucleus.

Sight is MorphState (looking is not walking). Walk is Clock A GET.
"""
from __future__ import annotations

from ux_compose import (
    Component,
    MorphState,
    RefState,
    action,
    bind,
    button,
    control,
    div,
    h1,
    h2,
    mark_dirty,
    notify,
    optional_plan,
    p,
    span,
    update_with,
    a,
    section,
)

STARS = (
    ("enter", "/enter", "Door", "Login, OTP, the seal of entry."),
    ("house", "/house", "House", "Eighty-one owned kit rooms."),
    ("atelier", "/atelier", "Atelier", "Market hall. Hero to newsletter."),
    ("commission", "/commission", "Commission", "Questionnaire, stepper, plans, Cap."),
    ("bag", "/bag", "Bag", "Cart. Quantity is RefState."),
    ("forge", "/forge", "Forge", "Glaze, kiln, chart, tree, diff."),
    ("studio", "/studio", "Studio", "Chat log. Feed. Attachments."),
    ("chrome", "/chrome", "Chrome", "Menubar, toolbar, APG holds."),
    ("overlay", "/overlay", "Edge", "OverlayChrome vs anchored family."),
    ("lab", "/lab", "Lab", "Hold an Intent. Spend a Cap."),
    ("author", "/author", "Author", "act, field, status, optional_*."),
    ("docs", "/docs", "Law", "The constitution. Swagger is off."),
)


class Index(Component):
    id = "index"
    sight = MorphState("lab")
    held = MorphState("idle")
    beats = RefState(0)
    dirty = MorphState("idle")

    def render(self):
        sight = str(self.sight or "lab")
        held = str(self.held or "idle")
        beats = int(self.beats or 0)
        stars = []
        for key, href, name, lede in STARS:
            on = key == sight
            stars.append(
                button(
                    span(name, className="star-name"),
                    span(lede, className="star-lede"),
                    type="button",
                    className="star" + (" is-sight" if on else ""),
                    aria_pressed="true" if on else "false",
                    **control("index.sight_star", key=key),
                )
            )
        current = next((s for s in STARS if s[0] == sight), STARS[0])
        return section(
            span("nocturnal foundry os", className="kicker"),
            h1("APPIC", className="display"),
            p(
                "The document is the composition root made visible. "
                "Caps are wax seals. Intent is a nucleus you can hold. "
                "Sight a star, then walk it.",
                className="lede",
            ),
            div(
                div(
                    span("Nucleus", className="kicker"),
                    h2("Intent"),
                    p(f"state · {held}", className="mono"),
                    p(f"beats · {beats}", className="mono"),
                    div(
                        button(
                            "Hold intent" if held != "held" else "Intent held",
                            type="button",
                            className="btn-primary",
                            **bind(self.hold),
                        ),
                        button(
                            "Spend cap",
                            type="button",
                            className="btn-ghost",
                            **control("index.spend"),
                        ),
                        className="row",
                    ),
                    className="nucleus",
                    data_held=held,
                ),
                div(*stars, className="constellation", role="list"),
                className="table-grid",
            ),
            div(
                p(f"Sighted · {current[2]}", className="kicker"),
                h2(current[2]),
                p(current[3], className="lede"),
                a("Walk this room", href=current[1], className="btn-primary"),
                className="sight-card",
            ),
            id=self.id,
            className="page table-page",
        )

    @action(caps=())
    def sight_star(self, key: str = "lab"):
        allowed = {k for k, *_ in STARS}
        self.sight = key if key in allowed else "lab"
        return update_with(self, extra_ops=[notify(f"sight {self.sight}")])

    @action(caps=())
    def hold(self):
        self.held = "held"
        self.beats = int(self.beats or 0) + 1
        mark_dirty(self)
        plan = optional_plan("nucleus-hold", f"#{self.id}", ms=160)
        return update_with(self, plan, extra_ops=[notify("intent held")])

    @action(caps=("orders.place",))
    def spend(self):
        self.held = "spent"
        self.beats = int(self.beats or 0) + 1
        mark_dirty(self)
        return update_with(self, extra_ops=[notify("cap spent")])
