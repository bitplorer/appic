"""Page unit — House. Anchored family map, not OverlayChrome."""
from __future__ import annotations

from ux_compose import Component, a, div, h1, h2, li, p, section, span, ul


ROOMS = (
    ("/typeahead", "Typeahead", "Hits morph #typeahead-hits only. delay:300."),
    ("/combobox", "Combobox", "Type then pick. Ids follow {id}-form / {id}-opt-n."),
    ("/select", "Select", "Grouped options. Label for ↔ trigger."),
    ("/dropdown", "Dropdown", "Menu is presence. Value is a named key."),
    ("/popover", "Popover", "Non-modal, anchored. Escape dismisses."),
    ("/tooltip", "Tooltip", "role=tooltip described-by. Not a modal."),
    ("/hovercard", "HoverCard", "Non-modal preview. Anchored family."),
    ("/navmenu", "NavMenu", "Disclosure of named destinations."),
    ("/usermenu", "UserMenu", "Sign-out spends auth.logout."),
    ("/contextmenu", "ContextMenu", "Click or longpress. aria-controls."),
    ("/carousel", "Carousel", "Named slides. Overlay chevrons. Coalescing pip."),
    ("/table", "Table", "Sort MorphState, selection RefState. Bind the checkbox."),
    ("/pagination", "Pagination", "Opaque keys. Windowed numbers."),
    ("/sheet", "Sheet", "Right edge. Close/Done swipe.right. No root swipe."),
    ("/actionsheet", "ActionSheet", "Bottom. Handle swipe-down threshold:48."),
)


class House(Component):
    id = "house"

    def render(self):
        cards = [
            a(
                span(title, className="card-title"),
                span(law, className="muted"),
                href=href,
                className="map-card",
            )
            for href, title, law in ROOMS
        ]
        return section(
            span("House", className="eyebrow"),
            h1("Anchored things stay.", className="display"),
            p(
                "Do not force Dropdown, Combobox, Select, Popover, Tooltip, HoverCard, "
                "UserMenu, or NavMenu through OverlayChrome. That family is the edge.",
                className="lede",
            ),
            div(*cards, className="map-grid"),
            id=self.id,
            className="room",
        )
