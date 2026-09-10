"""Ownable copy of ux_compose.kit.drawer — edit freely.

Copied by ``uxcompose add drawer``. Regenerate with ``uxcompose add drawer --force``.

Drawer is a Sheet alias — same Host, right-edge panel.

Not a second Host. ``kind=drawer`` on OverlayChrome maps to the same
right edge as Sheet. MorphState / Caps / a11y: see ``Sheet``.

Copied by ``uxcompose add drawer`` also lands ``sheet.py`` (sibling rewrite).
"""

from __future__ import annotations

from .sheet import Sheet as Drawer

__all__ = ["Drawer"]
