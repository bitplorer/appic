"""Skin — WebAssets."""
from __future__ import annotations
from ux_compose import Component, WebAssets, h1, p, section, span, dl, dt, dd
from settings import webassets, OUTPUT_CSS, ASSETS_DIR

class Skin(Component):
    id = "skin"
    def render(self):
        href = getattr(webassets, "css_href", f"/css/{OUTPUT_CSS}")
        return section(
            span("Skin", className="eyebrow"),
            h1("The skin is a folder with an ETag.", className="display"),
            p("WebAssets.emit must send ETag / Last-Modified. dual_copy is the leftover alias.", className="lede"),
            dl(
                dt("css href"), dd(str(href)),
                dt("assets"), dd(str(ASSETS_DIR)),
                dt("output"), dd(OUTPUT_CSS),
                dt("class"), dd(WebAssets.__name__),
                className="facts",
            ),
            id=self.id, className="room",
        )
