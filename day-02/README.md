
# Day 02 — Mini Contact Book (CLI)

A simple command-line contact manager with in-memory CRUD and **optional JSON persistence** via `--db`.

## Why this exercise?
- Practice lists/dicts and basic CRUD logic
- Learn `argparse` subcommands
- Start writing tests for both functions and CLI flows

## Usage
```
python day-02/contacts.py <command> [options]
```

### Add
```
python day-02/contacts.py --db day-02/contacts.json add --name "Ada Lovelace" --phone "+44 1234" --email ada@example.com --tags pioneer math
```
Output:
```
Added contact #1: Ada Lovelace
```

### List
```
python day-02/contacts.py --db day-02/contacts.json list --sort-by name
```

### Find
```
python day-02/contacts.py --db day-02/contacts.json find --q Ada
```

### Delete
```
python day-02/contacts.py --db day-02/contacts.json delete --id 1
```

> Tip: If you omit `--db`, the actions happen in-memory for that invocation only (useful for quick tests).

## Exit codes
- `0` success
- `1` not found (e.g., delete missing id)
- `2` invalid input/usage

## Tests
Run all tests (requires `pytest`):
```
pytest -q day-02/tests/test_contacts.py
```

## What to commit today
- [x] `day-02/contacts.py`
- [x] `day-02/README.md`
- [x] `day-02/tests/test_contacts.py`

## Git commands
From your repo root:
```
git add day-02/
git commit -m "Day 02: Mini Contact Book CLI with JSON persistence and tests"
git push
```
