import os

# Exactly one letter: A for coffee. No word, no explanation,
# no punctuation — the whole entry is this single character.
LINE = "A"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
