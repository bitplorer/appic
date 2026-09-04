"""Page unit: deploy.py → Deploy.

uxcompose deploy providers made visible. Prepares config — does not upload.
Isolation: no ux_channel. Default ASGI entry is app:asgi.
"""
from __future__ import annotations

from pathlib import Path

from ux_compose.deploy import (
    DeployResult,
    format_deploy_result,
    prepare_deploy,
)
from ux_compose.tunnel import parse_provider as parse_tunnel

from appic.store import HOST
from appic.ux import (
    Component,
    MorphState,
    RefState,
    a,
    action,
    article,
    bind,
    button,
    div,
    h1,
    h2,
    li,
    maybe_plan,
    notify,
    p,
    section,
    span,
    tick,
    ul,
    update_with,
)

PROVIDERS = ("docker", "fly", "render", "railway", "vps", "checklist")
TUNNELS = ("none", "ngrok", "cloudflare")
ROOT = Path(__file__).resolve().parents[2]

_BLURBS = {
    "docker": ("Dockerfile + .dockerignore", "CMD uvicorn app:asgi — CSS compiled before the image."),
    "fly": ("fly.toml", "fly deploy after uxcompose build."),
    "render": ("render.yaml", "Web service, uvicorn app:asgi."),
    "railway": ("railway.json / nixpacks", "PORT from the host."),
    "vps": ("systemd unit", "rsync, venv, enable --now."),
    "checklist": ("no files", "build · doctor · DEBUG=false · uvicorn · TLS."),
}


class Deploy(Component):
    id = "deploy"
    provider = MorphState("checklist")
    tunnel = MorphState("none")
    last = RefState("")
    stamp = MorphState("idle")

    def render(self):
        current = str(self.provider or "checklist")
        if current not in PROVIDERS:
            current = "checklist"
        tun = str(self.tunnel or "none")
        buttons = [
            button(
                name,
                type="button",
                className="chip" + (" is-on" if current == name else ""),
                id=f"provider-{name}",
                **bind(self.choose, provider=name),
            )
            for name in PROVIDERS
        ]
        tunnels = [
            button(
                name,
                type="button",
                className="chip" + (" is-on" if tun == name else ""),
                **bind(self.set_tunnel, tunnel=name),
            )
            for name in TUNNELS
        ]
        preview = _BLURBS.get(current, _BLURBS["checklist"])
        written_hint, note = preview
        return section(
            div(
                span("uxcompose deploy · prepare only · app:asgi", className="kicker"),
                h1("Ship"),
                p(
                    "Six providers. The CLI writes Docker / Fly / Render / Railway / VPS files "
                    "or prints a checklist. It does not upload secrets. Tunnel is a serve-dev "
                    "flag that starts after origin health is green — ngrok or cloudflare, never a Document API.",
                    className="lede",
                ),
                className="hero",
            ),
            article(
                h2("Provider"),
                p("Named MorphState. Choosing is public. Preparing is a Cap.", className="muted tiny"),
                div(*buttons, className="chip-row"),
                className="card",
            ),
            article(
                h2("Tunnel"),
                p("parse_provider aliases off/false/0 → none. Chip on Relay too.", className="muted tiny"),
                div(*tunnels, className="chip-row"),
                className="card",
            ),
            article(
                h2(f"Prepare · {current}"),
                p(note, className="muted"),
                p(written_hint, className="mono tiny"),
                button(
                    "Prepare this provider",
                    type="button",
                    className="btn btn-primary",
                    **bind(self.prepare),
                ),
                p(str(self.last or ""), className="mono tiny") if self.last else None,
                className="card",
            ),
            article(
                h2("ASGI law"),
                p("Deploy starts raw uvicorn, not serve. Default entry is app:asgi.", className="muted"),
                div(
                    span("uvicorn app:asgi --host 0.0.0.0 --port 8080", className="chip is-on"),
                    span("uxcompose serve prod", className="chip"),
                    span("DeployResult", className="chip"),
                    className="chip-row",
                ),
                a("Relay clocks", href="/relay", className="btn btn-text"),
                className="card",
            ),
            id=self.id,
            className="page deploy-page",
            data_provider=current,
            data_tunnel=tun,
        )

    @action(caps=())
    def choose(self, provider: str = "checklist", **kwargs):
        if provider not in PROVIDERS:
            provider = "checklist"
        self.provider = provider
        tick(self)
        HOST.log("deploy.choose", provider, "morph")
        return update_with(
            self,
            maybe_plan("deploy-pick", f"#provider-{provider}", ms=120),
            extra_ops=[notify(f"provider · {provider}")],
        )

    @action(caps=())
    def set_tunnel(self, tunnel: str = "none", **kwargs):
        parsed = parse_tunnel(tunnel)
        self.tunnel = parsed
        tick(self)
        HOST.log("deploy.tunnel", parsed, "morph")
        return update_with(self, extra_ops=[notify(f"tunnel · {parsed}")])

    @action(caps=("ship.deploy",))
    def prepare(self, **kwargs):
        provider = str(self.provider or "checklist")
        if provider not in PROVIDERS:
            provider = "checklist"
        result = prepare_deploy(provider, cwd=ROOT, force=False, app_name="appic")
        self.last = format_deploy_result(result)
        tick(self)
        HOST.log("deploy.prepare", provider, "cap")
        HOST.last_seal = f"ship.deploy:{provider}"
        return update_with(
            self,
            maybe_plan("deploy-prep", "#deploy", ms=160),
            extra_ops=[notify(f"prepared · {provider}")],
        )


def deploy_evidence() -> dict:
    return {
        "providers": list(PROVIDERS),
        "tunnels": list(TUNNELS),
        "result_type": DeployResult.__name__,
        "asgi": "app:asgi",
        "blurbs": dict(_BLURBS),
    }
