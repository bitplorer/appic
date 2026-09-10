"""Forge — workbench kit."""
from __future__ import annotations
from ux_compose import Component, a, div, h1, p, section, span

class Forge(Component):
    id = "forge"
    def render(self):
        cards = (
            ("/chart", "Chart", "Named SVG bars. Heights RefState. role=img."),
            ("/tree", "Tree", "APG treeview. add treeview aliases here."),
            ("/diff", "Diff", "Named before/after. Radiogroup."),
            ("/mockup", "Mockup", "Named device frame."),
            ("/colorpicker", "Glaze", "Named swatches. Hex is RefState."),
            ("/countdown", "Kiln", "role=timer. Remaining RefState."),
            ("/progress", "Fire", "progressbar. Magnitude RefState."),
            ("/attachment", "Files", "Names on RefState."),
            ("/feed", "Feed", "APG feed of articles."),
            ("/resizable", "Split", "Named split. Radiogroup + labelled separator."),
            ("/scrollarea", "Pane", "Labelled overflow. Named jump."),
            ("/fab", "Dial", "Menu id stays in the tree, hidden when closed."),
        )
        return section(
            span("Forge", className="eyebrow"),
            h1("The workbench keeps time.", className="display"),
            p("Magnitudes stay on RefState. Named keys stay on MorphState.", className="lede"),
            div(*[a(span(t, className="card-title"), span(l, className="muted"), href=h, className="map-card") for h,t,l in cards], className="map-grid"),
            id=self.id, className="room",
        )
