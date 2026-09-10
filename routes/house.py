"""Kit house — every owned stem, grouped into wings. Sight then walk."""
from __future__ import annotations

from foundry import kit_tree
from owned import WINGS
from ux_compose import (
    Component,
    MorphState,
    action,
    button,
    control,
    div,
    h1,
    h2,
    notify,
    p,
    section,
    span,
    update_with,
)


class House(Component):
    id = "house"
    wing = MorphState("door")

    def render(self):
        current = str(self.wing or "door")
        if current not in WINGS:
            current = "door"
        title, stems = WINGS[current]
        tabs = [
            button(
                meta[0],
                type="button",
                className="chip" + (" is-on" if key == current else ""),
                **control("house.select", wing=key),
            )
            for key, meta in WINGS.items()
        ]
        rooms = [div(kit_tree(stem), className="paper-slot", data_kit=stem) for stem in stems]
        return section(
            span("eighty-one owned stems", className="kicker"),
            h1("House"),
            p(
                "Copied with uxcompose add. The library keeps the source of truth; "
                "these files are yours. shell=False drops the Atelier kicker. "
                "Ids stay in the tree when closed.",
                className="lede",
            ),
            div(*tabs, className="chip-row", role="tablist"),
            h2(title),
            p(f"{len(stems)} rooms in this wing.", className="muted"),
            div(*rooms, className="kit-grid"),
            id=self.id,
            className="page",
        )

    @action(caps=())
    def select(self, wing: str = "door"):
        self.wing = wing if wing in WINGS else "door"
        return update_with(self, extra_ops=[notify(f"wing {self.wing}")])
