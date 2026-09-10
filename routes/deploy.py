"""Ship — prepare_deploy six providers."""
from __future__ import annotations

from pathlib import Path

from ux_compose import Component, h1, li, p, section, span, ul
from ux_compose.deploy import prepare_deploy, format_deploy_result
from ux_compose.tunnel import parse_provider, provider_available


class Deploy(Component):
    id = "deploy"

    def render(self):
        root = Path(__file__).resolve().parents[1]
        providers = ("docker", "fly", "render", "railway", "vps", "checklist")
        rows = [li(name) for name in providers]
        tunnels = []
        for name in ("none", "ngrok", "cloudflare", "cf"):
            parsed = parse_provider(name)
            tunnels.append(li(f"tunnel {name} → {parsed} available={provider_available(parsed)}"))
        result = prepare_deploy(provider="checklist", cwd=root, force=False)
        text = format_deploy_result(result)
        return section(
            span("Ship", className="eyebrow"),
            h1("Six ways out. None of them are Vite.", className="display"),
            p("prepare_deploy writes configs. Deploy runs raw uvicorn, not serve.", className="lede"),
            ul(*rows, className="mono-list"),
            ul(*tunnels, className="mono-list"),
            p(text, className="mono muted"),
            id=self.id,
            className="room",
        )
