# Repo Organization

A structural map of the `fraglag` repository.

## Top-level layout

```
fraglag/
├── Bamboo.md            # Operational policy layer
├── README.md            # Human-facing documentation
├── AGENT.md             # Cold-start router and Session Identity
├── demo.py              # Runnable parser demo (inline sample log)
├── behavior/            # Bamboo behavior files (discipline canon)
│   ├── ctx-rules.md         # Hard operational rules + Knob format
│   ├── ctx-lexicon.md       # System terms (Knob, PLTRF, Hot/Warm/Cold)
│   ├── ctx-entropy.md       # Preservation discipline (LTIP/STIP)
│   ├── ctx-token-limits.md  # Token economy and 1–10 scoring
│   ├── ctx-utility.md       # Utility surfaces
│   ├── ctx-window.md        # Context-window management
│   ├── persona-layer.md     # Persona placement boundary
│   └── user-model.md        # How the agent reads and models the user
├── docs/                # Operational memory mapping
│   ├── repo-organization.md  # ← this file. The map.
│   └── ctx-orientation.md    # The running log of Knobs (single home)
├── fraglag/             # Python package source code
│   ├── __init__.py      # Package marker
│   ├── cli.py           # CLI entry point (argparse → JSON)
│   ├── parser.py        # parse_line / parse_text
│   └── patterns.py      # XPTitle enum + regex EVENT_PATTERNS
├── examples/            # Example log files
│   └── match.txt        # Sample FPS match log
└── .github/
    └── workflows/
        └── pltrf-check.yml  # CI: package-name + map-integrity check
```

---

## Maintenance rules

- New folders or file movements require updating this map in the same commit.
- Every concept has exactly one canonical home (PLTRF). The Knob log lives only
  at `docs/ctx-orientation.md` — there is no second orientation file.
- Broken links or missing references are build failures, enforced by
  `.github/workflows/pltrf-check.yml`.

## Not yet built (planned, intentionally absent)

These were named in the original bootstrap scaffold but never built. Listed here
so the intent stays on record without leaving phantom entries in the map above:
`fraglag/models.py` (structured log objects), `fraglag/export.py` (JSON/CSV/table
exports), `pyproject.toml` (packaging), `tests/test_parser.py` (parser suite).