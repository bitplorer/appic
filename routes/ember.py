"""Page unit — ember.py → GET /ember.

Last coal. Named coal. Remaining heat as a single ember path.
Instrument fragment in GET chrome. EMBER-3.
Not Watch. Not Pulse. Not the kiln.
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
    optional_fade,
    p,
    path,
    section,
    span,
    svg,
    update_with,
)
from store import COALS, HOST, ember_d

COAL_COPY = {
    "live": "A coal still named. The instrument reads it. Heat is a path.",
    "dark": "The coal is held. Specular from the top still holds.",
    "ash": "The last coal is spent. Ash is Host stock. The hearth is quiet.",
}


class Ember(Component):
    id = "ember"
    coal = MorphState("live")
    dirty = MorphState("idle")

    def render(self):
        HOST.occupy("ember")
        coal = str(HOST.coal or self.coal or "live")
        if coal not in COALS:
            coal = "live"
        self.coal = coal
        heat = int(HOST.heat_remain or 0)
        segs = [
            button(
                key,
                type="button",
                className="seg is-on" if coal == key else "seg",
                **bind(self.name, coal=key),
            )
            for key in COALS
        ]
        return section(
            span("Ember", className="eyebrow"),
            h1("Name the last coal.", className="display"),
            p(
                "Coal is MorphState. Remaining heat is Host stock — the same hearth "
                "Kiln and Watch keep. The instrument in GET chrome carries the coal. "
                "This is not Watch. This is not Pulse. EMBER-3.",
                className="lede",
            ),
            div(
                div(
                    span("coal", className="eyebrow"),
                    svg(
                        circle(cx="60", cy="60", r="28", fill="none", stroke="currentColor", stroke_width="1.4", className="ember-ring"),
                        circle(cx="60", cy="60", r="8", fill="currentColor", className="ember-core"),
                        path(
                            d=ember_d(coal),
                            fill="none",
                            stroke="currentColor",
                            stroke_width="1.5",
                            stroke_linecap="round",
                            className="wave-path",
                            transform="translate(0 70)",
                        ),
                        viewBox="0 0 120 120",
                        className="ember-svg",
                        id="ember-disk",
                        role="img",
                        aria_label=f"{coal} coal",
                    ),
                    p(f"{heat}h remaining on the hearth.", className="stat"),
                    className=f"paper ember-chamber coal-{coal}",
                    id="ember-card",
                ),
                div(
                    span("name", className="eyebrow"),
                    h2(coal, className="sight-title"),
                    p(COAL_COPY[coal], className="sight-law"),
                    div(*segs, className="segs", role="radiogroup", aria_label="Coal"),
                    div(
                        button("Name a live coal", type="button", className="btn-primary", **bind(self.name, coal="live")),
                        button("Let it ash", type="button", className="btn-ghost", **bind(self.name, coal="ash")),
                        a("Keep the watch", href="/watch", className="btn-ghost"),
                        className="hero-actions",
                    ),
                    className="paper",
                ),
                className="kiln-split",
            ),
            id=self.id,
            className="room ember-room",
            data_coal=coal,
        )

    @action(caps=())
    def name(self, coal: str = "live"):
        named = HOST.name_coal(coal)
        self.coal = named
        mark_dirty(self)
        return update_with(self, optional_fade("ember", "#ember-card"), extra_ops=[notify(named)])
