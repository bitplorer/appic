"""Page unit — glaze.py → GET /glaze. Named oxide; load is RefState; lock is a Cap."""
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
    rect,
    section,
    span,
    svg,
    update_with,
    a,
)
from store import HOST

OXIDES = (
    ("ash", "Ash", "#c9c3b4", 18),
    ("iron", "Iron", "#8a4a32", 42),
    ("copper", "Copper", "#3d6b5a", 28),
    ("cobalt", "Cobalt", "#2c3d66", 12),
    ("tin", "Tin", "#ede8dc", 36),
    ("celadon", "Celadon", "#7d9b76", 24),
)


class Glaze(Component):
    id = "glaze"
    oxide = MorphState("ash")
    load = RefState(24)
    dirty = MorphState("idle")
    locked = MorphState(False)

    def _load(self) -> int:
        try:
            return max(4, min(80, int(self.load or 24)))
        except (TypeError, ValueError):
            return 24

    def _row(self):
        key = str(self.oxide or "ash")
        for row in OXIDES:
            if row[0] == key:
                return row
        return OXIDES[0]

    def render(self):
        row = self._row()
        key, title, hexv, typical = row
        n = self._load()
        chips = [
            button(
                span("", className=f"swatch-dot oxide-{ox}"),
                span(label, className="star-name"),
                type="button",
                className="choice is-on" if self.oxide == ox else "choice",
                **control("glaze.pick", oxide=ox),
            )
            for ox, label, color, _typ in OXIDES
        ]
        bars = [
            svg(
                rect(x="0", y=str(40 - int(val / 2)), width="28", height=str(int(val / 2) + 8), rx="4", className="chart-bar is-on" if ox == key else "chart-bar"),
                viewBox="0 0 28 48",
                width="28",
                height="48",
                aria_label=f"{label} typical {val}",
            )
            for ox, label, _c, val in OXIDES
        ]
        loads = [
            button(
                lab,
                type="button",
                className="choice is-on" if n == val else "choice",
                **control("glaze.dose", load=str(val)),
            )
            for val, lab in ((12, "Thin"), (24, "Even"), (40, "Fat"), (64, "Drip"))
        ]
        return section(
            span("Glaze", className="eyebrow"),
            h1("Mix a chemistry that stays.", className="display"),
            p(
                "The oxide is a named key. The load is RefState. "
                "Locking a recipe spends glaze.lock — a wax seal, once.",
                className="lede",
            ),
            div(
                div(
                    span("batch", className="eyebrow"),
                    div("", className=f"glaze-pool oxide-{key}", id="pool", aria_hidden="true"),
                    p(title, className="hearth-piece"),
                    p(f"{n}% load", className="stat"),
                    p("Typical for this oxide is " + str(typical) + "%.", className="muted"),
                    className="hearth",
                    data_oxide=key,
                ),
                div(
                    span("oxides", className="eyebrow"),
                    h2(title, className="sight-title"),
                    p("Named swatches. Hex is not the identity — the key is.", className="sight-law"),
                    div(*chips, className="choices", role="radiogroup", aria_label="Oxide"),
                    label("Load", className="eyebrow"),
                    div(*loads, className="choices", role="radiogroup", aria_label="Glaze load"),
                    div(*bars, className="chart-row", role="img", aria_label="Typical loads"),
                    div(
                        span("", className="seal is-spent" if self.locked else "seal", aria_hidden="true"),
                        span(
                            "Wax spent · glaze.lock" if self.locked else "Wax intact · mint on lock",
                            className="mono",
                        ),
                        className="cap-row",
                    ),
                    div(
                        button(
                            "Already locked" if self.locked else "Lock this recipe",
                            type="button",
                            className="btn-primary",
                            **control("glaze.lock"),
                        ),
                        a("Walk to make", href="/commission", className="btn-ghost"),
                        className="hero-actions",
                    ),
                    className="paper",
                    id="glaze-card",
                ),
                className="kiln-split",
            ),
            id=self.id,
            className="room",
        )

    @action(caps=())
    def pick(self, oxide: str = "ash"):
        keys = {row[0] for row in OXIDES}
        self.oxide = oxide if oxide in keys else "ash"
        row = self._row()
        self.load = int(row[3])
        mark_dirty(self)
        HOST.log("glaze.oxide", str(self.oxide))
        return update_with(self, optional_plan("pool", "#pool"), extra_ops=[notify(str(self.oxide))])

    @action(caps=())
    def dose(self, load: str = "24"):
        try:
            n = max(4, min(80, int(load)))
        except (TypeError, ValueError):
            n = 24
        self.load = n
        mark_dirty(self)
        return update_with(self, extra_ops=[notify(f"{n}%")])

    @action(caps=("glaze.lock",))
    def lock(self):
        recipe = {"oxide": str(self.oxide), "load": self._load()}
        HOST.recipes.append(recipe)
        HOST.locked_glaze = recipe
        HOST.log("glaze.lock", f"{self.oxide}/{self.load}", "cap")
        HOST.notice = "A recipe is sealed. Walk it to Make."
        self.locked = True
        mark_dirty(self)
        return update_with(self, extra_ops=[notify("recipe locked")])
