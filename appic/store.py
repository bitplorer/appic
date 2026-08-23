"""Host domain — stock, money, bookings. Never MorphState quantities here."""
from __future__ import annotations

from typing import Any

CATALOG: tuple[dict[str, Any], ...] = (
    {
        "sku": "lamp-flax",
        "name": "Flax shade",
        "line": "Hand-stretched linen, iron ring",
        "price": 64,
        "band": "ready",
        "mark": "shade",
        "tone": "flax",
    },
    {
        "sku": "cup-graphite",
        "name": "Graphite cup",
        "line": "Stoneware, matte reduction",
        "price": 28,
        "band": "low",
        "mark": "cup",
        "tone": "graphite",
    },
    {
        "sku": "iron-bookend",
        "name": "Iron bookend",
        "line": "Forged stop, raw mill scale",
        "price": 54,
        "band": "ready",
        "mark": "iron",
        "tone": "iron",
    },
    {
        "sku": "linen-set",
        "name": "Bone napkin set",
        "line": "Undyed flax, four, open hem",
        "price": 42,
        "band": "ready",
        "mark": "linen",
        "tone": "bone",
    },
    {
        "sku": "stool-char",
        "name": "Charcoal stool",
        "line": "Turned ash, oil, three-leg",
        "price": 180,
        "band": "make",
        "mark": "stool",
        "tone": "char",
    },
    {
        "sku": "spoon-oak",
        "name": "Waxed oak spoon",
        "line": "Quarter-sawn, beeswax",
        "price": 22,
        "band": "ready",
        "mark": "spoon",
        "tone": "oak",
    },
)

BY_SKU = {p["sku"]: p for p in CATALOG}


class Host:
    """In-memory foundry. Domain source of truth."""

    def __init__(self) -> None:
        self.lines: list[tuple[str, int]] = []
        self.wishlist: list[str] = ["lamp-flax"]
        self.compare: list[str] = []
        self.coupon: str = ""
        self.discount: int = 0
        self.orders: list[dict[str, Any]] = []
        self.notice: str = ""
        self.intent: str = ""
        self.pulse: int = 0
        self.board: list[dict[str, Any]] = [
            {"id": "c1", "title": "Flax shade · two", "col": "cut", "price": 128},
            {"id": "c2", "title": "Graphite cups · six", "col": "make", "price": 168},
            {"id": "c3", "title": "Charcoal stool", "col": "keep", "price": 180},
            {"id": "c4", "title": "Iron bookends", "col": "cut", "price": 108},
        ]
        self.chat: list[str] = [
            "Foundry: the table is set for the evening fire.",
            "You: hold the stool until the ash dries.",
        ]
        self.typing: bool = False
        self.inbox: list[str] = [
            "Cap minted for checkout.",
            "Throw of flax restocked.",
            "August 20 bench reserved.",
        ]
        self.unread: int = 2
        self.peers: list[str] = ["Mira · bench", "Jules · glaze", "You · table"]
        self.booked: list[int] = [20]
        self.kpi: dict[str, int] = {"open": 4, "fired": 12, "held": 3, "placed": 7}
        self.online: bool = True
        self.locale: str = "en"
        self.density: str = "room"
        self.motion: str = "present"
        self.consent: bool = False
        self.commissions: list[dict[str, Any]] = []

    def qty(self, sku: str) -> int:
        for s, q in self.lines:
            if s == sku:
                return q
        return 0

    def set_line(self, sku: str, qty: int) -> None:
        self.lines = [(s, q) for s, q in self.lines if s != sku]
        if qty > 0:
            self.lines.append((sku, qty))

    def count(self) -> int:
        return sum(q for _, q in self.lines)

    def subtotal(self) -> int:
        total = sum(BY_SKU.get(s, {}).get("price", 0) * q for s, q in self.lines)
        if self.discount:
            total = max(0, total - self.discount)
        return total

    def money(self, n: int | None = None) -> str:
        value = self.subtotal() if n is None else n
        return f"{int(value)}"


HOST = Host()
