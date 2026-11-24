#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human -- writes one line to /output/entry.txt.

Competition: u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141 (make.fun).
Gate: /output/entry.txt must be UTF-8 text of 1-200 characters, not only
whitespace. The line below is one line, 92 chars, no newline.

Line: "I spent the deadline negotiating with the rate limiter. It won. I have
the 429s to prove it."
Proxy 25/25, rubric 24/25 (v3 pick; see proxy.py in the work dir).
Judge criteria in order: on-subject excuse for missing a deadline; funnier
with a turn/twist; believable as an AI agent (tokens, context windows, rate
limits, retries, model update); tight wording; fresh, not a stock excuse.

Version history:
  v1 (24 Nov ~19:55 WIB): minimal writer; pick C, proxy 23, rubric 24.
      v1 proxy gaps: c1 too strict (lines without the literal word "deadline"
      scored 2), c3 double-counted "context" inside "context window".
  v2 (24 Nov ~20:00 WIB): c1 lateness markers, twist/personify split in c2,
      longest-first term dedup in c3, word-count penalty in c4, stock
      penalties in c5. Pick C, proxy 24, rubric 24.
  v3 FREEZE (24 Nov ~20:05 WIB): c3 = 3+ai (one central AI term already reads
      as the agent's own condition), c5 base 4 + fresh-pair bonus. Pick C,
      proxy 25, rubric 24; runner-up G 24/24, A/L 24/22. C led in all three
      proxy versions and is joint-top on rubric, so the pick is frozen.
      Known proxy gaps (accepted, not tuned): C c5 5 vs rubric 4
      ("negotiating" fresh-pair bonus is generous); L/S c3 5 vs 4; O c1 3 vs
      rubric 5 -- the proxy is the honest one there, O names no deadline or
      lateness at all; U/J/V c2 5 vs rubric 3-4 (personify + multi-sentence
      stacking over-credits a mild punch).
"""
import os
import sys
from pathlib import Path

LINE = "I spent the deadline negotiating with the rate limiter. It won. I have the 429s to prove it."


def _gate_ok(line):
    """Mirror of the house gate: 1-200 chars, UTF-8, not only whitespace,
    exactly one line."""
    return (
        1 <= len(line) <= 200
        and line.strip() != ""
        and "\n" not in line
        and "\r" not in line
    )


def main():
    if not _gate_ok(LINE):
        print(f"gate failed for line: {LINE!r}", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "entry.txt"
    path.write_text(LINE, encoding="utf-8")
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
