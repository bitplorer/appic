"""Market hall — marketing kit as a real storefront."""
from __future__ import annotations
from ux_compose import Component, a, div, h1, p, section, span

class Market(Component):
    id = "market"
    def render(self):
        cards = [
            (href, title, law)
            for href, title, law in (
                ("/hero", "Hero", "Landing band. CTA is chrome, not a Cap."),
                ("/pricingsection", "Pricing", "Choose binds the button, not the row."),
                ("/logocloud", "Marks", "Named marks with alt. Selected aria-pressed."),
                ("/testimonials", "Voices", "which is a key, not a quantity."),
                ("/newsletter", "Letter", "Subscribe spends list.subscribe."),
                ("/cta", "Call", "Titled action. Demo act public."),
                ("/featuregrid", "Promises", "Named tiles. Active key MorphState."),
                ("/footer", "Colophon", "contentinfo. aria-current."),
            )
        ]
        return section(
            span("Hall", className="eyebrow"),
            h1("The market is a hall, not a gallery.", className="display"),
            p("Hero, pricing, marks, voices, the letter. Same Component at L1 and L3.", className="lede"),
            div(*[a(span(t, className="card-title"), span(l, className="muted"), href=h, className="map-card") for h,t,l in cards], className="map-grid"),
            id=self.id, className="room",
        )
