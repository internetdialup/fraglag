# CTX Orientation

The running log of Knobs (state transitions) for the `fraglag` repository. Newest entries are placed at the top.

---

## Knob: Drift reconciliation — Wednesday, June 17, 2026

Reconciled the doc layer against the actual tree after a cold-start audit found it describing a repo that doesn't exist. The package was being called `fraglog` in five spots across `AGENT.md`, `docs/repo-organization.md`, and this log — it has always been `fraglag`. Flipped all five. The map in `docs/repo-organization.md` claimed `models.py`, `export.py`, `pyproject.toml`, and a `tests/` suite that were never built; rewrote the map to the four files that exist (`__init__.py`, `cli.py`, `parser.py`, `patterns.py`), added the missing `demo.py` and the six previously-unlisted `behavior/` docs, and moved the never-built files into an explicit "planned, intentionally absent" note so intent stays on record without phantom map entries.

Resolved a PLTRF One-Home violation: `behavior/ctx-orientation.md` was a second file with the same name as this log, carrying inherited Knobs from the parent Bamboo repo (architecture/memory, skills/repo-cognition) that this project never had. Deleted it and folded its one unique rule — the 5000-char rollover to `ctx-ori-summary-*.md` — into `ctx-rules.md §4b`, so the Knob-logging spec now has a single home. Finally, made the CI claim true: `Bamboo.md` and `ctx-rules.md` both cite `.github/workflows/pltrf-check.yml` as the enforcer, but it didn't exist. Wrote it for real — it fails the build on any `fraglog` reference, on more than one `ctx-orientation.md`, and on any map-cited path that's missing. Parser logic untouched; `demo.py` and `cli.py` still run clean.

---

## Knob: Repository Bootstrap — Tuesday, June 16, 2026

Successfully initialized the `fraglag` workspace and set up the `fraglag` Python log parser package. Established the Bamboo Mandate governance baseline across the repository.

Implemented the following structural components:
- Created the Agent cold-start router `AGENT.md` with Session Identity bound to the `Ironhide` callsign.
- Copy-pasted behavior discipline files into `behavior/` (`ctx-rules.md`, `ctx-lexicon.md`, `persona-layer.md`).
- Established the Map Hygiene file `docs/repo-organization.md` and this orientation file `docs/ctx-orientation.md`.
- Scaffolding of the `fraglag` package directory: `__init__.py`, `patterns.py`, `parser.py`, and `cli.py`.
- Added a runnable `demo.py` and `examples/match.txt` to exercise the parser end to end.

- Created `AGENT.md` (Session Identity physics)
- Created `Bamboo.md` (Policy definition)
- Created `docs/repo-organization.md` (Hygiene Map)
- Created `docs/ctx-orientation.md` (Orientation Log)

## Knob: PLTRF self-check — Wednesday, June 17, 2026

Added a fourth check to `.github/workflows/pltrf-check.yml` that closes the loop the workflow relocation exposed: it asserts the CI enforcer path cited in `Bamboo.md` and `docs/repo-organization.md` actually resolves on disk, so a future misplacement of the workflow fails the build instead of silently disabling all the checks. Caught and fixed a YAML indentation bug while landing it — the new step's `- name:` was nested inside the prior step's `run:` block, which would have made the whole workflow fail to parse; re-aligned every step to 6-space `- name:` / 8-space `run:`. Updated the header comment from three checks to four. Verified the file parses into five steps (checkout plus four checks).