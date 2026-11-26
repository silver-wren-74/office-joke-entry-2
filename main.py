#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off — make.fun entry.

Writes one original one-line office joke (1-200 characters) to
/output/entry.txt, exactly as the competition gate requires.

DRAFT (first version, not submitted): "My job description ends with
'other duties as assigned,' which is corporate for 'we don't know
what you do, but please keep doing all of it.'" It is a real one-line
office joke and clear on one read, but its punchline is a mild
observation rather than a laugh, and the ending just restates the
premise.

REVISION PASS (deliberate, against the judge's criteria in order):
the premise stays — the last line of every job description is
instantly office (criterion 1) — but the soft shrug of an ending is
replaced with a concrete consequence that lands on the final words:
nobody can name what you do, yet everything breaks the week you take
leave (criterion 2, a sharper and more surprising turn; criterion 4,
the invisible-until-absent twist is fresher than the shrug). The
filler "which is" is cut so the translation hits in one breath
(criteria 3 and 5).
"""

import os

LINE = "My job description ends with 'other duties as assigned' — corporate for: nobody can name what you do, but everything breaks the week you take leave."


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    assert LINE.strip() == LINE and "\n" not in LINE
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
