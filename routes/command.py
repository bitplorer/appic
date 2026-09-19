"""Page unit — command.py → Command. Owned kit, shell=False. House destinations."""
from __future__ import annotations

from components.command import Command as CommandCard

from store import HOST


class Command(CommandCard):
    COMMANDS = (
        ("go-table", "The table", "House"),
        ("go-now", "The instrument", "House"),
        ("go-vessel", "The vessel", "House"),
        ("go-score", "The score", "House"),
        ("go-chorus", "The chorus", "House"),
        ("go-eclipse", "The eclipse", "House"),
        ("go-duet", "The duet", "House"),
        ("go-provenance", "The seals", "House"),
        ("go-threshold", "The doors", "House"),
        ("go-watch", "The night watch", "House"),
        ("go-kiln", "The kiln", "House"),
        ("go-wheel", "The wheel", "House"),
        ("go-vitrine", "The vitrine", "House"),
        ("go-kintsugi", "Kintsugi", "House"),
        ("go-gift", "The gift", "House"),
        ("go-lineage", "Lineage", "House"),
        ("go-air", "The air", "House"),
        ("go-law", "The written law", "House"),
        ("shift-noon", "Name noon", "Sky"),
        ("shift-night", "Name night", "Sky"),
        ("veil-full", "Name a full eclipse", "Sky"),
        ("unveil", "Lift the umbra", "Sky"),
        ("ring-bell", "Ring the bell", "Watch"),
        ("sign-out", "Sign out", "Session"),
    )

    def on_run(self, key: str) -> str:
        HOST.log("command.run", key, "morph")
        dest = {
            "go-table": "table",
            "go-now": "now",
            "go-vessel": "vessel",
            "go-score": "score",
            "go-chorus": "chorus",
            "go-eclipse": "eclipse",
            "go-duet": "duet",
            "go-provenance": "provenance",
            "go-threshold": "threshold",
            "go-watch": "watch",
            "go-kiln": "kiln",
            "go-wheel": "wheel",
            "go-vitrine": "vitrine",
            "go-kintsugi": "kintsugi",
            "go-gift": "gift",
            "go-lineage": "lineage",
            "go-air": "air",
            "go-law": "law",
        }
        if key in dest:
            HOST.occupy(dest[key])
            HOST.notice = f"Command named {dest[key]}."
            return f"Walk to {dest[key]}"
        if key == "shift-noon":
            HOST.auto_sky = False
            HOST.sky_band = "noon"
            HOST.notice = "The house is named noon."
            return "noon"
        if key == "shift-night":
            HOST.auto_sky = False
            HOST.sky_band = "night"
            HOST.notice = "The house is named night."
            return "night"
        if key == "veil-full":
            HOST.veil("full")
            return "full"
        if key == "unveil":
            HOST.unveil()
            return "clear"
        if key == "ring-bell":
            HOST.watch_bells.append("bell · command")
            HOST.notice = "A bell crossed the house."
            return "bell"
        return f"Ran {key}"

    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
