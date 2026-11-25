"""Roast Your Fridge — one-line entry (program/v1, python3.13).

Writes the roast to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR when set).
The entry is a fixed original line; the program is deterministic.
"""
import os

ENTRY = "My fridge's butter compartment has never once held butter \u2014 it's a witness-protection programme for one very lonely garlic clove."

def main():
    # Gate self-check (revision edit): the sealed gate wants 1-200 chars, non-blank.
    assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry fails the 1-200 char gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
