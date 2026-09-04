"""Page unit: skin.py → Skin.

WebAssets made visible. Compose owns the CSS/JS product tree, not ux-dom.
Isolation: no ux_channel. Catalog css: False — no companion CSS per kit card.
"""
from __future__ import annotations

from pathlib import Path

from ux_compose import WebAssets, __version__
from ux_compose.assets import CSS_URL_PREFIX, OUTPUT_CSS_NAME

from appic.store import HOST
from appic.ux import (
    Component,
    MorphState,
    a,
    action,
    article,
    bind,
    button,
    div,
    h1,
    h2,
    h3,
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
from settings import ASSETS_DIR, OUTPUT_CSS, webassets

SWATCHES = (
    ("ink", "#0c0d0b", "field"),
    ("elevated", "#141512", "plane"),
    ("surface", "#1a1b18", "panel"),
    ("bone", "#ebe6d8", "type"),
    ("muted", "#9a9488", "aside"),
    ("cool", "#c8ccd4", "accent"),
)


class Skin(Component):
    id = "skin"
    band = MorphState("tokens")
    stamp = MorphState("idle")

    def render(self):
        wa = webassets
        href = getattr(wa, "css_href", None)
        href = href() if callable(href) else "/css/output.css"
        input_css = getattr(wa, "input_css", None)
        output_css = getattr(wa, "output_css", None)
        input_path = Path(str(input_css)) if input_css is not None else ASSETS_DIR / "css" / "input.css"
        output_path = Path(str(output_css)) if output_css is not None else ASSETS_DIR / "static" / "file" / "css" / OUTPUT_CSS
        etag = ""
        last_mod = ""
        size = 0
        if output_path.is_file():
            st = output_path.stat()
            size = st.st_size
            etag = f'W/"{st.st_mtime_ns}-{st.st_size}"'
            last_mod = str(int(st.st_mtime))
        first_token = ""
        if input_path.is_file():
            head = input_path.read_text(encoding="utf-8", errors="replace")[:80].lstrip()
            first_token = head.split(None, 1)[0] if head else ""
        swatches = [
            article(
                span(label, className="tiny muted"),
                span(hexcode, className="mono"),
                span(role, className="tiny"),
                className="swatch",
                style=f"--swatch:{hexcode}",
                id=f"swatch-{key}",
            )
            for key, hexcode, role, label in (
                (k, h, r, k) for k, h, r in SWATCHES
            )
        ]
        band = str(self.band or "tokens")
        return section(
            div(
                span("WebAssets · compose-owned · not ux-dom", className="kicker"),
                h1("Skin"),
                p(
                    "Tokens live in input.css. uxcompose build minifies to /css/output.css. "
                    "The static door stamps ETag and Last-Modified so CSS watch can HEAD-poll. "
                    "Kit cards ship class_* only — catalog css: False. "
                    "serve=\"webassets\" is a leftover alias; the escape hatch is serve=\"dual_copy\".",
                    className="lede",
                ),
                div(
                    span(f"href {href}", className="chip is-on"),
                    span(f"{CSS_URL_PREFIX}/{OUTPUT_CSS_NAME}", className="chip"),
                    className="chip-row",
                ),
                className="hero",
            ),
            div(
                button(
                    "Tokens",
                    type="button",
                    className="chip" + (" is-on" if band == "tokens" else ""),
                    **bind(self.show, band="tokens"),
                ),
                button(
                    "Compiler",
                    type="button",
                    className="chip" + (" is-on" if band == "compiler" else ""),
                    **bind(self.show, band="compiler"),
                ),
                button(
                    "Leftovers",
                    type="button",
                    className="chip" + (" is-on" if band == "leftovers" else ""),
                    **bind(self.show, band="leftovers"),
                ),
                className="chip-row",
            ),
            div(*swatches, className="swatch-row") if band == "tokens" else None,
            article(
                h2("Disk law"),
                ul(
                    li(span("input", className="chip"), span(str(input_path), className="mono")),
                    li(span("output", className="chip"), span(str(output_path), className="mono")),
                    li(span("exists", className="chip"), span("yes" if output_path.is_file() else "missing", className="mono")),
                    li(span("bytes", className="chip"), span(str(size), className="mono")),
                    li(span("etag", className="chip"), span(etag or "—", className="mono")),
                    li(span("mtime", className="chip"), span(last_mod or "—", className="mono")),
                    li(span("first token", className="chip"), span(first_token or "—", className="mono")),
                    className="cap-list",
                ),
                p(
                    "First token of every .css file must be CSS — never JS export. "
                    "That was a Vite failure mode. The foundry does not compile CSS as JS.",
                    className="muted tiny",
                ),
                className="card",
            ) if band == "compiler" else None,
            article(
                h2("Leftovers expire by teaching"),
                p("Doctor flags these in product trees. It does not fail-close on them.", className="muted"),
                div(
                    span('serve="webassets"', className="chip"),
                    span('serve="dual_copy"', className="chip is-on"),
                    span("host=\"batteries\"", className="chip"),
                    span("DirectoryRouter", className="chip"),
                    className="chip-row",
                ),
                p(
                    "Package-static escape hatch is dual_copy. WebAssets is the product CSS tree. "
                    "They are not the same door.",
                    className="muted tiny",
                ),
                a("See teaching chips on Trace", href="/trace", className="btn btn-text"),
                className="card",
            ) if band == "leftovers" else None,
            id=self.id,
            className="page skin-page",
            data_band=band,
        )

    @action(caps=())
    def show(self, band: str = "tokens", **kwargs):
        if band not in {"tokens", "compiler", "leftovers"}:
            band = "tokens"
        self.band = band
        tick(self)
        HOST.log("skin.show", band, "morph")
        return update_with(
            self,
            maybe_plan("skin-band", "#skin", ms=120),
            extra_ops=[notify(f"skin · {band}")],
        )


def skin_evidence() -> dict:
    wa = webassets
    href = getattr(wa, "css_href", None)
    return {
        "css_href": href() if callable(href) else "/css/output.css",
        "prefix": CSS_URL_PREFIX,
        "output_name": OUTPUT_CSS_NAME,
        "assets_dir": str(ASSETS_DIR),
        "webassets": WebAssets.__name__,
        "leftover_alias": 'serve="webassets"',
        "prefer": 'serve="dual_copy"',
    }
