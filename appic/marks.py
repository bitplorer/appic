"""Sparse monochrome SVG marks — no emoji."""
from __future__ import annotations

from appic.tags import circle, path, rect, svg


def mark(kind: str):
    common = dict(viewBox="0 0 64 64", width="56", height="56", aria_hidden="true")
    stroke = dict(fill="none", stroke="currentColor", stroke_width="1.5")
    if kind == "cup":
        return svg(
            path(d="M20 18h22v22a10 10 0 0 1-10 10H30A10 10 0 0 1 20 40z", **stroke),
            path(d="M42 24h8a6 6 0 0 1 0 12h-8", **stroke),
            **common,
        )
    if kind == "iron":
        return svg(
            path(d="M14 46h36M18 46V22h8l6 10h8l6-10h8v24", **stroke),
            **common,
        )
    if kind == "linen":
        return svg(
            rect(x="16", y="12", width="32", height="40", rx="2", **stroke),
            path(d="M16 22h32M16 42h32", **stroke),
            **common,
        )
    if kind == "stool":
        return svg(
            path(d="M20 28h24M22 28v22M42 28v22M24 18h16l4 10H20z", **stroke),
            **common,
        )
    if kind == "spoon":
        return svg(
            path(d="M24 14a8 8 0 1 1 8 12L30 52", **stroke),
            **common,
        )
    # shade
    return svg(
        path(d="M12 28l20-14 20 14v6H12z", **stroke),
        path(d="M32 34v16", **stroke),
        circle(cx="32", cy="52", r="3", **stroke),
        **common,
    )


def logo():
    return svg(
        rect(x="8", y="10", width="48", height="44", rx="6", fill="none", stroke="currentColor", stroke_width="1.5"),
        path(d="M22 42V22l10 14 10-14v20", fill="none", stroke="currentColor", stroke_width="1.6"),
        viewBox="0 0 64 64",
        width="28",
        height="28",
        aria_hidden="true",
        className="brand-mark",
    )
