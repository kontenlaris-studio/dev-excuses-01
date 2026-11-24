#!/usr/bin/env python3
"""Write one developer excuse to /output/entry.txt. Stdlib only."""
import os

LINE = "The ticket said 'minor change', so I changed one line, and now three services are down and I am Googling my own error message."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote /output/entry.txt ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
