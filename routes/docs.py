"""Page unit — GET /docs. Product constitution. FastAPI Swagger stays off."""
from __future__ import annotations

from ux_compose import Component, a, article, div, h1, h2, li, p, section, span, ul, __version__


class Docs(Component):
    id = "docs"

    def render(self):
        laws = (
            "The document is the composition root made visible.",
            "Caps are wax seals that break when spent.",
            "Intent is a nucleus you can hold.",
            "GET is Clock A. Action is Clock B.",
            "Payload type picks media type.",
            "Brand lives on wrap=, never inside render().",
            "Quantity is RefState. Named things are MorphState.",
            "81 stems, one house. OverlayChrome is the edge primitive.",
            "AlertDialog is interrupting. Escape does not dismiss it.",
            "Typeahead morphs the hits slot, never the field being typed.",
            "HMR is delivery, not a Document API.",
            "Channel owns FileStateStore. Compose keeps lifecycle.",
            "Kit Cut 1: render(*, shell=False, **slots). apply_slots / kit_shell.",
            "Doctor scan_store_clone fails closed on a cloned store class.",
            "Channel Cut C: empty Content-Type on /action is bad_request.",
            "Cap door is Channel.boot. Redis wins over sqlite. Do not export both.",
            "Frozen serve verbs: dev / prod / restart-channel.",
            "cli.py is argv only. serve_dev.py starts CSS watch + tunnel.",
            "Compose has no FEATURES.md — ARCHITECTURE + OWNERSHIP are the encyclopedia.",
            "Morph fragments prefer ux-dom extract_by_id. Homemade walker is escape. No fragment.py.",
            "Specular on glass arrives from 90 degrees. Nested radius = parent minus padding.",
            "The kiln is a named band. Remaining heat is RefState. Sighting the sky is MorphState.",
            "Noon is a named sky band. The clock is Host stock. Occupancy is a short memory.",
            "The living instrument is GET chrome. Resonance is a path, not a canvas.",
            "Now is a house room. It is not a Pulse room.",
            "Tide is lunar climate. data-tide on GET chrome. New burns hotter.",
            "Fugue hops the warp. Morph-then-Play. XOR: no html= on the plan.",
            "Mirror is the piece looking at itself. Owned Diff, shell=False.",
            "Phantom is ghost occupancy. Unsighted warp fades. Not Pulse.",
            "Wedge is named grain. Folds are RefState. bind() kneads. stagger_in on #fold-*.",
            "Bisque is first fire. Remaining is RefState. Not the glaze kiln.",
            "Raku is sudden quench. morph_play hop. Heat dumps to ash. data-raku on GET chrome.",
            "Ember is the last coal. Instrument fragment. Not Watch. Not Pulse.",
            "Coda closes the loop. Named close. morph_play toward the table.",
        )
        return section(
            span("Law", className="eyebrow"),
            h1("A constitution you can walk.", className="display"),
            p(f"ux-compose {__version__}. FastAPI Swagger is off. This page owns GET /docs.", className="lede"),
            ul(*[li(law) for law in laws], className="law"),
            div(
                a("Trace residuals", href="/trace", className="btn-primary"),
                a("Ownership notes", href="/notes", className="btn-ghost"),
                className="hero-actions",
            ),
            id=self.id,
            className="room",
        )
