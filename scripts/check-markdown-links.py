#!/usr/bin/env python3
"""Verify relative Markdown links in the repository root (parent of scripts/)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\]\(([^)]+)\)")
SKIP_PREFIX = ("http://", "https://", "mailto:")


def main() -> int:
    failed = False
    for md in sorted(ROOT.rglob("*.md")):
        if ".git" in md.parts:
            continue
        text = md.read_text(encoding="utf-8", errors="replace")
        for match in LINK.finditer(text):
            target = match.group(1).split()[0]
            if target.startswith("#") or target.startswith(SKIP_PREFIX):
                continue
            path = target.split("#")[0]
            if not path:
                continue
            resolved = (md.parent / path).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                # Absolute or outside repo — skip
                continue
            if not resolved.exists():
                rel = md.relative_to(ROOT)
                print(f"BROKEN: {rel} -> {target}")
                failed = True
    if failed:
        print("Markdown link check failed.", file=sys.stderr)
        return 1
    print("Markdown link check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
