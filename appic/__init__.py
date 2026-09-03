"""APPIC — a foundry OS authored in ux-compose. Isolation-safe product package."""

from __future__ import annotations

__version__ = "0.2.0"


def _install_tag_shim() -> None:
    """Python 3.10 sandbox: ux-dom prefers ≥3.14. Kit copies call ux_compose tags.

    Populate the public tag names so owned ``components/*.py`` stay valid without
    rewriting every stem onto a second tag world.
    """
    try:
        import ux_compose
        import ux_compose.dom as dom
        from appic.tags import (
            a,
            article,
            aside,
            body,
            button,
            circle,
            div,
            footer,
            form,
            h1,
            h2,
            h3,
            head,
            header,
            html,
            input_,
            label,
            li,
            link,
            main,
            meta,
            nav,
            p,
            path,
            raw,
            rect,
            script,
            section,
            span,
            style,
            svg,
            title,
            ul,
        )
    except Exception:
        return
    names = {
        "a": a,
        "article": article,
        "aside": aside,
        "body": body,
        "button": button,
        "circle": circle,
        "div": div,
        "footer": footer,
        "form": form,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "head": head,
        "header": header,
        "html": html,
        "input_": input_,
        "label": label,
        "li": li,
        "link": link,
        "main": main,
        "meta": meta,
        "nav": nav,
        "p": p,
        "path": path,
        "raw": raw,
        "rect": rect,
        "script": script,
        "section": section,
        "span": span,
        "style": style,
        "svg": svg,
        "title": title,
        "ul": ul,
    }
    for mod in (ux_compose, dom):
        for name, fn in names.items():
            if getattr(mod, name, None) is None:
                setattr(mod, name, fn)


_install_tag_shim()
