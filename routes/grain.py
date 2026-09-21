"""Page unit — grain.py → GET /grain.

Clay body climate. Named grain. data-grain on GET chrome.
Texture of the house, not a ThemeSwitch. GRAIN-1. Not Pulse.
"""
from __future__ import annotations

from ux_compose import (
    Component,
    MorphState,
    a,
    action,
    bind,
    button,
    circle,
    div,
    h1,
    h2,
    mark_dirty,
    notify,
    optional_plan,
    p,
    path,
    section,
    span,
    svg,
    update_with,
)
from store import GRAINS, HOST, grain_d

GRAIN_COPY = {
    "fine": "Porcelain skin. Specular still from the top. Grain is almost air.",
    "grog": "Stoneware bite. The body of the house takes a tooth.",
    "grog-heavy": "The cloth is gritted. Occupancy reads as weft through grog.",
}


class Grain(Component):
    id = "grain"
    body = MorphState("fine")
    dirty = MorphState("idle")

    def render(self):
        HOST.occupy("grain")
        body = str(self.body or HOST.grain or "fine")
        if body not in GRAINS:
            body = "fine"
        HOST.grain = body
        segs = [
            button(
                key,
                type="button",
                className="seg is-on" if body == key else "seg",
                **bind(self.name, body=key),
            )
            for key in GRAINS
        ]
        speckle = []
        n = {"fine": 5, "grog": 11, "grog-heavy": 19}[body]
        for i in range(n):
            x = 18 + (i * 37) % 84
            y = 22 + (i * 23) % 76
            r = 1.2 if body == "fine" else (2.1 if body == "grog" else 2.8)
            speckle.append(
                circle(
                    cx=str(x),
                    cy=str(y),
                    r=str(r),
                    fill="currentColor",
                    className="grain-speck",
                    id=f"speck-{i}",
                )
            )
        return section(
            span("Grain", className="eyebrow"),
            h1("Name the body.", className="display"),
            p(
                "Sky is lumen. Tide is water. Grain is clay. Naming a body turns auto off. "
                "GET chrome carries data-grain. Texture lives on the body, never as wallpaper. "
                "Not ThemeSwitch. Not Pulse.",
                className="lede",
            ),
            div(
                div(
                    span("body", className="eyebrow"),
                    svg(
                        *speckle,
                        path(
                            d=grain_d(body),
                            fill="none",
                            stroke="currentColor",
                            stroke_width="1.3",
                            stroke_linecap="round",
                            className="wave-path",
                        ),
                        viewBox="0 0 120 120",
                        className="eclipse-svg grain-svg",
                        id="grain-disk",
                        role="img",
                        aria_label=f"{body} grain",
                    ),
                    p(body, className="stat"),
                    p(f"auto {'on' if HOST.auto_grain else 'held'}.", className="muted"),
                    className=f"paper eclipse-chamber grain-{body}",
                    id="grain-card",
                ),
                div(
                    span("climate", className="eyebrow"),
                    h2(body, className="sight-title"),
                    p(GRAIN_COPY[body], className="sight-law"),
                    div(*segs, className="segs", role="radiogroup", aria_label="Grain body"),
                    div(
                        button("Hold grog", type="button", className="btn-primary", **bind(self.name, body="grog")),
                        button("Release auto", type="button", className="btn-ghost", **bind(self.release)),
                        a("Rake the ash", href="/ash", className="btn-ghost"),
                        className="hero-actions",
                    ),
                    className="paper",
                ),
                className="kiln-split",
            ),
            id=self.id,
            className="room grain-room",
            data_grain=body,
        )

    @action(caps=())
    def name(self, body: str = "grog"):
        named = HOST.name_grain(body)
        self.body = named
        mark_dirty(self)
        return update_with(self, optional_plan("grain", "#grain-card"), extra_ops=[notify(named)])

    @action(caps=())
    def release(self):
        HOST.auto_grain = True
        named = HOST.sync_grain()
        self.body = named
        mark_dirty(self)
        HOST.notice = "The grain follows the clay in the cradle."
        return update_with(self, optional_plan("grain-auto", "#grain-card"), extra_ops=[notify(named)])
