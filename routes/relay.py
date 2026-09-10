"""Relay — HMR / tunnel / serve clocks. Delivery, not a Document API."""
from __future__ import annotations

from ux_compose import Component, dl, dd, dt, h1, p, section, span
from ux_compose.hmr import HMR_PATH
from ux_compose.tunnel import local_probe_host


class Relay(Component):
    id = "relay"

    def render(self):
        host = local_probe_host("0.0.0.0")
        return section(
            span("Relay", className="eyebrow"),
            h1("HMR is delivery.", className="display"),
            p("location.reload() is the fallback only. Tunnel starts after origin health is green.", className="lede"),
            dl(
                dt("HMR path"),
                dd(str(HMR_PATH)),
                dt("probe host"),
                dd(str(host)),
                dt("serve dev"),
                dd("origin + ui + channel + CSS watch"),
                dt("restart-channel"),
                dd("one-shot Channel RAM drop"),
                className="facts",
            ),
            id=self.id,
            className="room",
        )
