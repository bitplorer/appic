"""Live App handle for page units that compose owned kit instances.

Isolation Law: never import ux_channel. Kits are registered via App.add.
"""
from __future__ import annotations

from typing import Any

_APP: Any = None


def bind(app: Any) -> None:
    global _APP
    _APP = app


def app():
    return _APP


def unit(sid: str):
    handle = _APP
    if handle is None:
        return None
    behavior = getattr(handle, "behavior", None) or getattr(handle, "_behavior", None)
    if behavior is not None and hasattr(behavior, "components"):
        try:
            found = dict(behavior.components()).get(sid)
            if found is not None:
                return found
        except Exception:
            pass
    reg = getattr(handle, "_kit_registry", {}) or {}
    return reg.get(sid)


def kit_tree(sid: str):
    inst = unit(sid)
    if inst is None:
        from ux_compose import p

        return p(f"Kit {sid} is not mounted.", className="text-sm text-stone-500")
    render = getattr(inst, "render", None)
    if not callable(render):
        from ux_compose import p

        return p(f"Kit {sid} has no render.", className="text-sm text-stone-500")
    try:
        return render(shell=False)
    except TypeError:
        return render()
