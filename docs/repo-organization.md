# Repo Organization

A structural map of the `fraglag` repository.

## Top-level layout

```
fraglag/
├── Bamboo.md            # Operational policy layer
├── README.md            # Human-facing documentation
├── AGENT.md             # Cold-start router and Session Identity
├── pyproject.toml       # Package metadata and dependencies
├── behavior/            # Bamboo behavior files (discipline canon)
│   ├── ctx-rules.md     # Hard operational rules
│   ├── ctx-lexicon.md   # System terms (Knobs, PLTRF)
│   └── persona-layer.md # Persona boundaries
├── docs/                # Operational memory mapping
│   ├── repo-organization.md  # ← this file. The map.
│   └── ctx-orientation.md    # Log of Knobs
├── fraglog/             # Python package source code
│   ├── cli.py           # CLI entry point and commands
│   ├── parser.py        # Log parser implementation
│   ├── patterns.py      # Regex rules for parsing
│   ├── models.py        # Structured log objects
│   └── export.py        # JSON/CSV/Table exports
├── examples/            # Example log files
│   └── match.txt        # Sample FPS game log
└── tests/               # Unit testing suite
    └── test_parser.py   # Tests for the parser and statistics
```

---

## Maintenance rules

- New folders or file movements require updating this map in the same commit.
- Every concept has exactly one canonical home (PLTRF).
- Broken links or missing references are considered build failures.
