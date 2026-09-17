"""Foundry Host memory. Domain stock lives here — never on MorphState.

Isolation: no ux_channel. Quantity is RefState on Components; this module
is the Host DB for commissions, bag, ledger, notices, kiln queue, thrown
bodies, locked recipes, vitrine, briefs, the studio floor, sky band, and
the shared hearth heat the Night Watch keeps.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%H:%M:%S")


@dataclass
class Host:
    notice: str = ""
    intent: str = "hold the table"
    pulse: int = 0
    bag: list[str] = field(default_factory=list)
    ledger: list[dict[str, Any]] = field(default_factory=list)
    commissions: list[dict[str, Any]] = field(default_factory=list)
    pending_fire: dict[str, Any] | None = None
    last_firing: dict[str, Any] | None = None
    authed: str = ""
    thrown: list[dict[str, Any]] = field(default_factory=list)
    wheel_piece: dict[str, Any] | None = None
    recipes: list[dict[str, Any]] = field(default_factory=list)
    locked_glaze: dict[str, Any] | None = None
    vitrine: list[dict[str, Any]] = field(default_factory=list)
    ratings: dict[str, str] = field(default_factory=dict)
    briefs: list[dict[str, Any]] = field(default_factory=list)
    last_brief: dict[str, Any] | None = None
    hands: list[str] = field(default_factory=list)
    sky_band: str = "night"
    firing: bool = False
    heat_remain: int = 0
    watch_bells: list[str] = field(default_factory=list)
    _piece_n: int = 0

    def log(self, verb: str, detail: str = "", kind: str = "morph") -> None:
        self.ledger.append(
            {"at": _now(), "verb": verb, "detail": detail, "kind": kind}
        )
        self.ledger = self.ledger[-48:]
        self.pulse += 1

    def next_id(self) -> str:
        self._piece_n += 1
        return f"p{self._piece_n:03d}"

    def draw(self, piece: dict[str, Any] | None) -> dict[str, Any]:
        row = dict(piece or {})
        row.setdefault("id", self.next_id())
        row.setdefault("band", "done")
        self.vitrine.append(row)
        self.vitrine = self.vitrine[-24:]
        return row

    def light(self, piece: dict[str, Any] | None) -> None:
        self.firing = True
        self.heat_remain = 12
        self.last_firing = dict(piece or {})
        self.pending_fire = None

    def tick_heat(self) -> str:
        """Advance shared hearth heat. Returns the kiln band name."""
        if not self.firing:
            return "idle"
        self.heat_remain = max(0, int(self.heat_remain) - 1)
        if self.heat_remain <= 0:
            self.firing = False
            self.heat_remain = 0
            self.notice = "Drawn from the kiln."
            self.log("kiln.drawn", str((self.last_firing or {}).get("clay", "")), "cap")
            self.draw(
                {
                    "clay": (self.last_firing or {}).get("clay", "clay"),
                    "glaze": (self.last_firing or {}).get("glaze", "glaze"),
                    "note": (self.last_firing or {}).get("note", ""),
                    "band": "done",
                }
            )
            return "done"
        if self.heat_remain <= 2:
            return "cool"
        if self.heat_remain <= 5:
            return "peak"
        if self.heat_remain <= 8:
            return "soak"
        return "warm"

    def kpi(self) -> dict[str, int]:
        return {
            "pulse": self.pulse,
            "bag": len(self.bag),
            "seals": sum(1 for row in self.ledger if row.get("kind") == "cap"),
            "commissions": len(self.commissions),
            "thrown": len(self.thrown),
            "drawn": len(self.vitrine),
            "heat": int(self.heat_remain),
        }


HOST = Host()
