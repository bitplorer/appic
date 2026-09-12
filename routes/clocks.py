"""Clocks — Clock A GET vs Clock B action."""
from __future__ import annotations
from ux_compose import Component, a, div, h1, p, section, span, dl, dt, dd, article

class Clocks(Component):
    id = "clocks"
    def render(self):
        return section(
            span("Clocks", className="eyebrow"),
            h1("Two clocks, one sky.", className="display"),
            p("Payload type picks media type — not Accept. HTML is daylight. JSON is a pulse. A generator is a stream of light.", className="lede"),
            div(
                article(h1("Clock A"), p("GET wrap. Brand lives here. Morph HTML has brand=0."), a("Health JSON", href="/health", className="btn-ghost"), className="paper"),
                article(h1("Clock B"), p("Action. Intent → Cap → Result. hello.pulse is fail-closed."), a("Hello", href="/hello", className="btn-ghost"), className="paper"),
                article(h1("Stream"), p("render() yields. Host picks StreamingResponse."), a("Pulse stream", href="/pulse", className="btn-ghost"), className="paper"),
                className="split-3",
            ),
            dl(
                dt("Serve dev"),
                dd("origin + ui + channel + CSS watch"),
                dt("Serve prod"),
                dd("clocks hard off"),
                dt("restart-channel"),
                dd("one-shot Channel RAM drop"),
                dt("Forbidden argv"),
                dd("development · production · restart_channel"),
                dt("Tunnel"),
                dd("starts after origin health is green"),
                dt("Cut C"),
                dd("empty Content-Type → bad_request"),
                className="facts",
            ),
            id=self.id, className="room",
        )
