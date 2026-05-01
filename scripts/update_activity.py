#!/usr/bin/env python3
"""Append a small daily activity update for the scheduled workflow."""

from __future__ import annotations

import random
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ACTIVITY_LOG = ROOT / "activity-log.md"
ENTRY_TEMPLATES = (
    "Refreshed repository activity dashboard metadata.",
    "Recorded scheduled maintenance heartbeat.",
    "Updated automated project activity notes.",
    "Captured daily repository status checkpoint.",
    "Logged routine repository activity summary.",
)


def main() -> None:
    now = datetime.now(timezone.utc)
    entry_count = random.randint(1, 3)
    entries = random.sample(ENTRY_TEMPLATES, k=entry_count)

    lines = [
        "",
        f"## {now:%Y-%m-%d %H:%M:%S UTC}",
        "",
    ]
    lines.extend(f"- {entry}" for entry in entries)
    lines.append("")

    with ACTIVITY_LOG.open("a", encoding="utf-8") as activity_log:
        activity_log.write("\n".join(lines))


if __name__ == "__main__":
    main()
