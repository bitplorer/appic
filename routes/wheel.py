"""Page unit — wheel.py → GET /wheel. Throwing is a named stage; rpm is RefState."""
from __future__ import annotations

from ux_compose import (
    Component,
    MorphState,
    RefState,
    action,
    button,
    control,
    div,
    h1,
    h2,
    label,
    mark_dirty,
    notify,
    optional_plan,
    p,
    progress,
    section,
    span,
    svg,
    circle,
    path,
    update_with,
    a,
)
from store import HOST

STAGES = ("center", "open", "raise", "collar", "trim")
STAGE_COPY = {
    "center": "The clay is a lump. Find the middle. Speed stays low.",
    "open": "Thumbs in. The well appears. Keep the floor even.",
    "raise": "Walls climb. The speed is honest or the wall folds.",
    "collar": "A neck. Do not collapse the shoulder.",
    "trim": "The foot learns to sit. When it stays, walk it to glaze.",
}
STAGE_LABEL = {
    "center": "Center",
    "open": "Open",
    "raise": "Raise",
    "collar": "Collar",
    "trim": "Trim",
}


class Wheel(Component):
    id = "wheel"
    stage = MorphState("center")
    rpm = RefState(18)
    wet = MorphState(True)
    dirty = MorphState("idle")
    thrown = MorphState(False)

    def _rpm(self) -> int:
        try:
            return max(0, min(120, int(self.rpm or 0)))
        except (TypeError, ValueError):
            return 0

    def render(self):
        stage = str(self.stage or "center")
        if stage not in STAGES:
            stage = "center"
        n = self._rpm()
        pct = int((STAGES.index(stage) / (len(STAGES) - 1)) * 100)
        segs = [
            button(
                STAGE_LABEL[key],
                type="button",
                className="seg is-on" if stage == key else "seg",
                **control("wheel.goto", stage=key),
            )
            for key in STAGES
        ]
        speeds = [
            button(
                label,
                type="button",
                className="choice is-on" if n == val else "choice",
                **control("wheel.spin", rpm=str(val)),
            )
            for val, label in ((12, "Slow"), (36, "Throw"), (72, "Rise"), (108, "Fast"))
        ]
        clay = HOST.wheel_piece or {}
        return section(
            span("Wheel", className="eyebrow"),
            h1("Throw something that holds.", className="display"),
            p(
                "The stage is MorphState. Revolutions are RefState. "
                "Wet is a boolean on the session plane. The thrown body lives on the Host.",
                className="lede",
            ),
            div(
                div(
                    span("bat", className="eyebrow"),
                    div(
                        svg(
                            circle(cx="80", cy="80", r="74", fill="none", stroke="currentColor", stroke_width="1.2", className="wheel-rim"),
                            circle(cx="80", cy="80", r="48", fill="none", stroke="currentColor", stroke_width="0.8", className="wheel-ring"),
                            path(d="M80 18 L80 36 M80 124 L80 142 M18 80 L36 80 M124 80 L142 80", fill="none", stroke="currentColor", stroke_width="1"),
                            circle(cx="80", cy="80", r="22", className="wheel-clay"),
                            viewBox="0 0 160 160",
                            width="220",
                            height="220",
                            className="wheel-svg",
                            aria_hidden="true",
                        ),
                        className="wheel-pad",
                        data_rpm=str(n),
                        data_stage=stage,
                        id="bat",
                    ),
                    p(f"{n} rpm", className="stat", aria_live="polite"),
                    p(STAGE_COPY[stage], className="muted"),
                    className=f"hearth band-{stage}",
                ),
                div(
                    span("hands", className="eyebrow"),
                    h2(STAGE_LABEL[stage], className="sight-title"),
                    p(STAGE_COPY[stage], className="sight-law"),
                    div(*segs, className="segs", role="tablist", aria_label="Throwing stage"),
                    progress(
                        value=str(pct),
                        max="100",
                        className="fire-bar",
                        role="progressbar",
                        aria_valuemin="0",
                        aria_valuemax="100",
                        aria_valuenow=str(pct),
                        aria_label="Throwing progress",
                    ),
                    label("Revolutions", className="eyebrow"),
                    div(*speeds, className="choices", role="radiogroup", aria_label="Wheel speed"),
                    div(
                        button(
                            "Sponge off" if self.wet else "Keep it wet",
                            type="button",
                            className="btn-ghost",
                            **control("wheel.sponge"),
                        ),
                        button(
                            "Already thrown" if self.thrown else "Lift from the bat",
                            type="button",
                            className="btn-primary",
                            **control("wheel.lift"),
                        ),
                        className="hero-actions",
                    ),
                    p(
                        f"{clay.get('stage', stage)} · {n} rpm"
                        if clay
                        else "Nothing on the bat yet.",
                        className="mono",
                    ),
                    a("Walk to glaze", href="/glaze", className="btn-ghost") if self.thrown else span(""),
                    className="paper",
                    id="wheel-card",
                ),
                className="kiln-split",
            ),
            id=self.id,
            className="room",
            data_stage=stage,
        )

    @action(caps=())
    def goto(self, stage: str = "center"):
        if stage not in STAGES:
            stage = "center"
        self.stage = stage
        HOST.log("wheel.stage", stage)
        return update_with(self, optional_plan("bat", "#bat"), extra_ops=[notify(stage)])

    @action(caps=())
    def spin(self, rpm: str = "18"):
        try:
            n = max(0, min(120, int(rpm)))
        except (TypeError, ValueError):
            n = 18
        self.rpm = n
        mark_dirty(self)
        HOST.log("wheel.rpm", str(n))
        return update_with(self, extra_ops=[notify(f"{n} rpm")])

    @action(caps=())
    def sponge(self):
        self.wet = not bool(self.wet)
        HOST.notice = "The sponge is on the rim." if not self.wet else "The clay is wet again."
        return update_with(self, extra_ops=[notify("wet" if self.wet else "dry")])

    @action(caps=())
    def lift(self):
        piece = {
            "stage": str(self.stage),
            "rpm": self._rpm(),
            "wet": bool(self.wet),
        }
        HOST.thrown.append(piece)
        HOST.wheel_piece = piece
        HOST.seat(stage="thrown", clay=str(self.stage))
        HOST.log("wheel.lift", str(self.stage))
        HOST.notice = "A body waits for glaze."
        self.thrown = True
        mark_dirty(self)
        return update_with(self, extra_ops=[notify("lifted")])
