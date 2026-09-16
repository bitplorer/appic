"""Page unit — brief.py → GET /brief. Named answers. Submit spends form.submit."""
from __future__ import annotations

from ux_compose import (
    Component,
    MorphState,
    RefState,
    action,
    a,
    button,
    control,
    div,
    fieldset,
    form,
    h1,
    legend,
    mark_dirty,
    notify,
    p,
    section,
    span,
    update_with,
)
from store import HOST

QUESTIONS = (
    (
        "use",
        "What should it hold?",
        (("tea", "Tea"), ("grain", "Grain"), ("nothing", "Nothing — a form")),
    ),
    (
        "scale",
        "How large in the hand?",
        (("cup", "A cup"), ("bowl", "A bowl"), ("jar", "A jar")),
    ),
    (
        "fire",
        "How hot should it live?",
        (("cone6", "Cone 6"), ("cone10", "Cone 10"), ("raku", "Raku")),
    ),
)


class Brief(Component):
    id = "brief"
    use = MorphState("tea")
    scale = MorphState("cup")
    fire = MorphState("cone6")
    done = MorphState(False)
    dirty = MorphState("idle")
    note = RefState("")

    def render(self):
        groups = []
        for key, prompt, opts in QUESTIONS:
            current = str(getattr(self, key) or opts[0][0])
            groups.append(
                fieldset(
                    legend(prompt),
                    *[
                        button(
                            lab,
                            type="button",
                            className="choice is-on" if current == opt else "choice",
                            **control("brief.pick", field=key, value=opt),
                        )
                        for opt, lab in opts
                    ],
                    className="choices",
                )
            )
        return section(
            span("Brief", className="eyebrow"),
            h1("Say what it is for.", className="display"),
            p(
                "Each answer is a named key on MorphState. "
                "Submit spends form.submit. The brief feeds Make — it does not place.",
                className="lede",
            ),
            form(
                *groups,
                div(
                    span("", className="seal is-spent" if self.done else "seal", aria_hidden="true"),
                    span(
                        "Wax spent · form.submit" if self.done else "Wax intact · mint on submit",
                        className="mono",
                    ),
                    className="cap-row",
                ),
                div(
                    button(
                        "Brief already filed" if self.done else "File the brief",
                        type="submit",
                        className="btn-primary",
                        **control("brief.submit"),
                    ),
                    a("Walk to the wheel", href="/wheel", className="btn-ghost") if self.done else span(""),
                    className="hero-actions",
                ),
                method="post",
                action="/act/brief.submit",
                data_ux="1",
                data_target="#brief",
                className="paper stack",
                id="brief-card",
            ),
            id=self.id,
            className="room",
        )

    @action(caps=())
    def pick(self, field: str = "use", value: str = ""):
        allowed = {q[0]: {opt for opt, _ in q[2]} for q in QUESTIONS}
        if field not in allowed:
            return update_with(self)
        if value not in allowed[field]:
            value = next(iter(allowed[field]))
        setattr(self, field, value)
        mark_dirty(self)
        return update_with(self, extra_ops=[notify(f"{field}={value}")])

    @action(caps=("form.submit",))
    def submit(self):
        brief = {
            "use": str(self.use),
            "scale": str(self.scale),
            "fire": str(self.fire),
        }
        HOST.briefs.append(brief)
        HOST.last_brief = brief
        HOST.log("brief.submit", f"{self.use}/{self.scale}/{self.fire}", "cap")
        HOST.notice = "A brief is on the table. Throw it."
        self.done = True
        mark_dirty(self)
        return update_with(self, extra_ops=[notify("brief filed")])
