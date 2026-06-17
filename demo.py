# demo.py

import json
from fraglag.parser import parse_text

sample = """
BeastBoy got First Blood
BeastBoy Double Kill
BeastBoy hit a triple kill
BeastBoy is Godlike
"""

events = parse_text(sample)

print(json.dumps(events, indent=2))