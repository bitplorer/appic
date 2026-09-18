"""Foundry Host memory. Domain stock lives here — never on MorphState.

Isolation: no ux_channel. Quantity is RefState on Components; this module
is the Host DB for commissions, bag, ledger, notices, kiln queue, thrown
bodies, locked recipes, vitrine, briefs, the studio floor, sky climate,
the shared hearth the Night Watch keeps, occupancy, and the circadian clock.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Any

IST = timezone(timedelta(hours=5, minutes=30))

BANDS = ("night", "dawn", "noon", "dusk")


def ist_hour() -> int:
    return datetime.now(IST).hour


def band_for_hour(h: int) -> str:
    h = int(h) % 24
    if 5 <= h < 8:
        return "dawn"
    if 8 <= h < 16:
        return "noon"
    if 16 <= h < 22:
        return "dusk"
    return "night"


def clock_label(h: int) -> str:
    return f"{int(h) % 24:02d}:00"


def _now() -> str:
    return datetime.now(IST).strftime("%H:%M:%S")


def waveform_d(band: str) -> str:
    """Resonance of the hearth. Peak is denser. Idle is a still line."""
    key = str(band or "idle")
    if key in ("peak", "middle"):
        return "M0 18 Q8 2 16 18 T32 18 T48 18 T64 18 T80 18 T96 18 T112 18 T128 18 T144 18 T160 18 T176 18 T192 18 T208 18"
    if key in ("soak", "first", "warm"):
        return "M0 18 Q16 8 32 18 T64 18 T96 18 T128 18 T160 18 T192 18 T224 18"
    if key in ("cool", "last"):
        return "M0 18 Q24 12 48 18 T96 18 T144 18 T192 18"
    if key in ("done",):
        return "M0 18 Q40 14 80 18 T160 18 T240 18"
    return "M0 18 L240 18"


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
    atmosphere: str = "oxidation"
    cone: int = 10
    window: str = "today"
    day: str = "thu"
    remain_h: int = 14
    _piece_n: int = 0
    clock_h: int = field(default_factory=ist_hour)
    auto_sky: bool = True
    occupied: list[str] = field(default_factory=list)
    heat_trace: list[int] = field(default_factory=list)

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
        self.heat_trace.append(12)
        self.heat_trace = self.heat_trace[-24:]

    def tick_heat(self) -> str:
        """Advance shared hearth heat. Returns the kiln band name."""
        if not self.firing:
            return "idle"
        self.heat_remain = max(0, int(self.heat_remain) - 1)
        self.heat_trace.append(int(self.heat_remain))
        self.heat_trace = self.heat_trace[-24:]
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

    def sync_sky(self) -> str:
        if self.auto_sky:
            self.sky_band = band_for_hour(self.clock_h)
        if self.sky_band not in BANDS:
            self.sky_band = "night"
        return self.sky_band

    def tick_clock(self) -> str:
        self.clock_h = (int(self.clock_h) + 1) % 24
        return self.sync_sky()

    def occupy(self, room: str) -> None:
        room = str(room or "").strip()
        if not room:
            return
        self.occupied = [room] + [r for r in self.occupied if r != room]
        self.occupied = self.occupied[:8]

    def kpi(self) -> dict[str, int]:
        return {
            "pulse": self.pulse,
            "bag": len(self.bag),
            "seals": sum(1 for row in self.ledger if row.get("kind") == "cap"),
            "commissions": len(self.commissions),
            "thrown": len(self.thrown),
            "drawn": len(self.vitrine),
            "heat": int(self.heat_remain),
            "present": len(self.occupied),
        }


def _seed(host: Host) -> Host:
    host.sync_sky()
    host.briefs = [
        {"intent": "a bowl that holds night", "at": "05:12:00"},
        {"intent": "a lip thin enough to vanish", "at": "05:40:00"},
    ]
    host.last_brief = host.briefs[-1]
    host.thrown = [
        {"id": "p001", "clay": "porcelain", "stage": "open"},
        {"id": "p002", "clay": "stoneware", "stage": "trim"},
    ]
    host.vitrine = [
        {
            "id": "p000",
            "clay": "porcelain",
            "glaze": "celadon",
            "band": "done",
            "note": "thin lip, still warm in the hand",
        }
    ]
    host.hands = ["the table is lit", "a pulse crossed the cloth"]
    host.occupied = ["table"]
    host.heat_trace = [0, 0, 2, 4, 7, 9, 8, 6, 4, 2, 0]
    host.notice = "The house is listening."
    host.log("house.open", host.sky_band)
    return host


HOST = _seed(Host())
