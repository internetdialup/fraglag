# fraglag/parser.py

from fraglag.patterns import COMPILED_EVENT_PATTERNS, ANNOUNCER_TITLES


def parse_line(line: str) -> list[dict]:
    matched_events = []

    for event_type, patterns in COMPILED_EVENT_PATTERNS.items():
        for pattern in patterns:
            match = pattern.search(line)

            if match:
                matched_events.append({
                    "event": event_type.value if hasattr(event_type, "value") else event_type,
                   "title": ANNOUNCER_TITLES.get(event_type, str(event_type).replace("_", " ").title()),
                    "matched_text": match.group(0),
                    "source": line.strip(),
                })

    return matched_events


def parse_text(text: str) -> list[dict]:
    events = []

    for line in text.splitlines():
        events.extend(parse_line(line))

    return events