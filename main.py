"""Write the family-scene entry for the make.fun competition.

The entry text is a constant below — nothing is read, fetched, or
generated at run time, so the output is the same on every run. The
writer honours the competition gate exactly: 1-280 UTF-8 characters,
not whitespace-only, and no trailing newline (the gate counts the
file's characters, so a stray newline would be a wasted character
and a needless difference between runs). The em dash in the text is
written as the escape \u2014 so this source file stays plain ASCII.
"""

import os

LINE = "My parents never once said 'we're proud of you' out loud. They said it in packed lunches, in lifts at 2 a.m., in a spare key cut the week I moved out \u2014 and I heard every word, mostly second-hand from the neighbours."

assert 1 <= len(LINE) <= 280, f"entry is {len(LINE)} chars, must be 1-280"
assert LINE.strip(), "entry must not be whitespace-only"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
