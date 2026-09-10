"""Studio — chat, feed, attachment as presence."""
from __future__ import annotations
from ux_compose import Component, a, div, h1, p, section, span

class Studio(Component):
    id = "studio"
    def render(self):
        return section(
            span("Studio", className="eyebrow"),
            h1("Talk is a log, not a socket toy.", className="display"),
            p("Chat is role=log. Feed is APG articles. Files are names on RefState.", className="lede"),
            div(
                a("Chat", href="/chat", className="map-card"),
                a("Feed", href="/feed", className="map-card"),
                a("Attachment", href="/attachment", className="map-card"),
                a("File upload", href="/fileupload", className="map-card"),
                a("Tags", href="/tagsinput", className="map-card"),
                a("Search", href="/searchbar", className="map-card"),
                className="map-grid",
            ),
            id=self.id, className="room",
        )
