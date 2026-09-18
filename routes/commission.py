"""Page unit — commission a piece. Named steps, Host stock, checkout Cap."""
from __future__ import annotations

from ux_compose import (
    Component,
    MorphState,
    RefState,
    action,
    button,
    control,
    div,
    field,
    fieldset,
    form,
    h1,
    h2,
    legend,
    mark_dirty,
    notify,
    optional_slide,
    p,
    section,
    span,
    update_with,
    a,
)
from store import HOST

CLAYS = (("porcelain", "Porcelain"), ("stoneware", "Stoneware"), ("earthen", "Earthenware"))
GLAZES = (("ash", "Ash"), ("iron", "Iron"), ("celadon", "Celadon"), ("shino", "Shino"))
STEPS = ("clay", "glaze", "fire")


class Commission(Component):
    id = "commission"
    step = MorphState("clay")
    clay = MorphState("porcelain")
    glaze = MorphState("ash")
    dirty = MorphState("idle")
    note = RefState("")
    placed = MorphState(False)

    def render(self):
        step = str(self.step or "clay")
        segs = [
            button(
                label.title(),
                type="button",
                className="seg is-on" if step == key else "seg",
                **control("commission.goto", step=key),
            )
            for key, label in (("clay", "Clay"), ("glaze", "Glaze"), ("fire", "Fire"))
        ]
        if step == "clay":
            body = fieldset(
                legend("Body"),
                *[
                    button(
                        label,
                        type="button",
                        className="choice is-on" if self.clay == key else "choice",
                        **control("commission.pick_clay", key=key),
                    )
                    for key, label in CLAYS
                ],
                className="choices",
            )
        elif step == "glaze":
            body = fieldset(
                legend("Glaze chemistry"),
                *[
                    button(
                        label,
                        type="button",
                        className="choice is-on" if self.glaze == key else "choice",
                        **control("commission.pick_glaze", key=key),
                    )
                    for key, label in GLAZES
                ],
                className="choices",
            )
        else:
            body = div(
                p(
                    f"{self.clay} · {self.glaze}. The kiln will keep it overnight.",
                    className="lede",
                ),
                form(
                    field("note", str(self.note or ""), placeholder="A line for the ledger"),
                    button(
                        "Already fired" if self.placed else "Place the commission",
                        type="submit",
                        className="btn-primary",
                        **control("commission.place"),
                    ),
                    method="post",
                    action="/act/commission.place",
                    data_ux="1",
                    data_target="#commission",
                    className="stack",
                ),
                div(
                    span("", className="seal is-spent" if self.placed else "seal", aria_hidden="true"),
                    span(
                        "Wax spent · orders.place" if self.placed else "Wax intact · mint on place",
                        className="mono",
                    ),
                    a("Walk to the kiln", href="/kiln", className="btn-ghost") if self.placed else span(""),
                    className="cap-row",
                ),
            )
        floor = [
            div(
                span(row.get("clay", ""), className="mono"),
                span(row.get("glaze", ""), className="muted"),
                className="cap-row",
            )
            for row in reversed(HOST.commissions[-5:])
        ] or [p("Nothing commissioned yet.", className="muted")]
        return section(
            span("Commission", className="eyebrow"),
            h1("Make something that stays.", className="display"),
            p("Named steps on MorphState. The note is RefState. Place spends orders.place.", className="lede"),
            div(*segs, className="segs", role="tablist"),
            div(body, id="commission-panel", className="paper"),
            h2("On the floor", className="sub"),
            div(*floor, className="stack"),
            id=self.id,
            className="room",
        )

    @action(caps=())
    def goto(self, step: str = "clay"):
        if step not in STEPS:
            step = "clay"
        self.step = step
        return update_with(self, optional_slide("step", "#commission-panel", direction="next"))

    @action(caps=())
    def pick_clay(self, key: str = "porcelain"):
        if key not in {k for k, _ in CLAYS}:
            key = "porcelain"
        self.clay = key
        return update_with(self, extra_ops=[notify(key)])

    @action(caps=())
    def pick_glaze(self, key: str = "ash"):
        if key not in {k for k, _ in GLAZES}:
            key = "ash"
        self.glaze = key
        return update_with(self, extra_ops=[notify(key)])

    @action(caps=("orders.place",))
    def place(self, note: str = ""):
        self.note = note
        mark_dirty(self)
        glaze = str(self.glaze)
        if HOST.locked_glaze:
            glaze = str(HOST.locked_glaze.get("oxide") or glaze)
        clay = str(self.clay)
        if HOST.wheel_piece:
            clay = f"{clay}·thrown"
        piece = {"clay": clay, "glaze": glaze, "note": note}
        HOST.commissions.append(piece)
        HOST.pending_fire = piece
        HOST.seat(stage="firing", clay=clay, glaze=glaze, note=note)
        HOST.log("commission.place", f"{clay}/{glaze}", "cap")
        HOST.notice = "A piece waits on the kiln shelf."
        self.placed = True
        return update_with(self, extra_ops=[notify("Commission placed")])
