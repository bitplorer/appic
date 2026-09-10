"""Rail — APG chrome. Caps off chrome."""
from __future__ import annotations
from ux_compose import Component, a, div, h1, p, section, span

class Rail(Component):
    id = "rail"
    def render(self):
        cards = (
            ("/menubar", "Menubar", "Submenu ids stay in the tree with hidden."),
            ("/toolbar", "Toolbar", "Last command aria-current, not pressed."),
            ("/togglegroup", "Toggles", "Exclusive radiogroup. Not Tabs."),
            ("/spinbutton", "Spin", "Magnitude RefState. Not Stepper."),
            ("/themeswitch", "Theme", "light/dark/system. Not a boolean switch."),
            ("/filterbar", "Filter", "Labeled query + named filter radiogroup."),
            ("/navbar", "Navbar", "Desktop and mobile are two trees."),
            ("/bottomnav", "Bottom", "Mobile sections. aria-current."),
            ("/sidebar", "Sidebar", "Collapsible rail. Active key MorphState."),
            ("/breadcrumb", "Trail", "Walking back is public."),
            ("/tabs", "Tabs", "{id}-tab-{k} / {id}-p-{k}. Inactive stay hidden."),
            ("/accordion", "Fold", "Open ids MorphState tuple."),
        )
        return section(
            span("Rail", className="eyebrow"),
            h1("Chrome is not authority.", className="display"),
            p("APG holds. Caps stay off chrome. Toolbar last command is aria-current.", className="lede"),
            div(*[a(span(t, className="card-title"), span(l, className="muted"), href=h, className="map-card") for h,t,l in cards], className="map-grid"),
            id=self.id, className="room",
        )
