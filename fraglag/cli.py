 # fraglag/cli.py

import argparse
import json

from fraglag.parser import parse_text


def main():
    parser = argparse.ArgumentParser(
        description="Parse FPS-style match logs into structured JSON events."
    )

    parser.add_argument(
        "file",
        help="Path to a match log text file."
    )

    args = parser.parse_args()

    with open(args.file, "r", encoding="utf-8") as file:
        text = file.read()

    events = parse_text(text)

    print(json.dumps(events, indent=2))


if __name__ == "__main__":
    main()