B """
Day 02 — Mini Contact Book (CLI)

Features
- In-memory CRUD with optional JSON persistence via --db <path>
- Commands: add, list, find, delete
- Input validation and clear exit codes

Exit codes
  0: success
  1: not found (e.g., delete missing id)
  2: invalid input / usage error
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional

DB_DEFAULT = {"next_id": 1, "contacts": []}

# ---------------- Core functions ----------------

def load_db(path: Optional[str]) -> Dict:
    if not path:
        # in-memory session only
        return {"next_id": 1, "contacts": []}
    p = Path(path)
    if p.exists():
        try:
            return json.loads(p.read_text(encoding='utf-8'))
        except json.JSONDecodeError:
            # Corrupt file → start fresh but don't overwrite yet
            return {"next_id": 1, "contacts": []}
    else:
        return {"next_id": 1, "contacts": []}


def save_db(path: Optional[str], db: Dict) -> None:
    if not path:
        return
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding='utf-8')


def add_contact(db: Dict, name: str, phone: str, email: Optional[str] = None, tags: Optional[List[str]] = None) -> Dict:
    if not name or not phone:
        raise ValueError("'name' and 'phone' are required.")
    tags = tags or []
    cid = db["next_id"]
    contact = {"id": cid, "name": name.strip(), "phone": phone.strip(), "email": (email or '').strip(), "tags": tags}
    db["contacts"].append(contact)
    db["next_id"] = cid + 1
    return contact


def list_contacts(db: Dict, sort_by: str = 'name', reverse: bool = False) -> List[Dict]:
    valid = {"name", "id"}
    key = sort_by if sort_by in valid else 'name'
    return sorted(db["contacts"], key=lambda c: (c.get(key) or ''), reverse=reverse)


def find_contacts(db: Dict, query: str) -> List[Dict]:
    q = (query or '').strip().lower()
    if not q:
        return []
    hits = []
    for c in db["contacts"]:
        hay = ' '.join([
            str(c.get('name','')),
            str(c.get('phone','')),
            str(c.get('email','')),
            ' '.join(c.get('tags', []))
        ]).lower()
        if q in hay:
            hits.append(c)
    return hits


def delete_contact(db: Dict, cid: int) -> bool:
    for i, c in enumerate(db["contacts"]):
        if int(c.get('id')) == int(cid):
            del db["contacts"][i]
            return True
    return False

# ---------------- CLI helpers ----------------

def _fmt_table(rows: List[Dict]) -> str:
    if not rows:
        return "(no contacts)"
    headers = ["ID", "Name", "Phone", "Email", "Tags"]
    cols = list(zip(*[
        [str(r.get('id','')), r.get('name',''), r.get('phone',''), r.get('email',''), ','.join(r.get('tags', []))]
        for r in rows
    ]))
    widths = [max(len(h), max(len(v) for v in col)) for h, col in zip(headers, cols)]
    def fmt_row(values):
        return " | ".join(v.ljust(w) for v, w in zip(values, widths))
    line = "-+-".join('-'*w for w in widths)

    out = [fmt_row(headers), line]
    for r in rows:
        out.append(fmt_row([
            str(r.get('id','')),
            r.get('name',''),
            r.get('phone',''),
            r.get('email',''),
            ','.join(r.get('tags', []))
        ]))
    out.append(f"\nTotal: {len(rows)}")
    return "\n".join(out)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Mini Contact Book: add, list, find, delete")
    p.add_argument('--db', help='Optional path to JSON DB for persistence')

    sub = p.add_subparsers(dest='cmd', required=True)

    pa = sub.add_parser('add', help='Add a new contact')
    pa.add_argument('--name', required=True)
    pa.add_argument('--phone', required=True)
    pa.add_argument('--email')
    pa.add_argument('--tags', nargs='*', default=[], help='Space-separated tags')

    pl = sub.add_parser('list', help='List contacts')
    pl.add_argument('--sort-by', choices=['name','id'], default='name')
    pl.add_argument('--reverse', action='store_true')

    pf = sub.add_parser('find', help='Find contacts by substring across fields')
    pf.add_argument('--q', required=True, help='Query substring')

    pd = sub.add_parser('delete', help='Delete a contact by ID')
    pd.add_argument('--id', type=int, required=True)

    return p


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    db = load_db(args.db)

    if args.cmd == 'add':
        try:
            c = add_contact(db, args.name, args.phone, args.email, args.tags)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 2
        save_db(args.db, db)
        print(f"Added contact #{c['id']}: {c['name']}")
        return 0

    if args.cmd == 'list':
        rows = list_contacts(db, sort_by=args.sort_by, reverse=args.reverse)
        print(_fmt_table(rows))
        return 0

    if args.cmd == 'find':
        rows = find_contacts(db, args.q)
        if not rows:
            print("No contacts found.")
            return 0
        print(_fmt_table(rows))
        return 0

    if args.cmd == 'delete':
        ok = delete_contact(db, args.id)
        if not ok:
            print(f"Error: contact id {args.id} not found.", file=sys.stderr)
            return 1
        save_db(args.db, db)
        print(f"Deleted contact id {args.id}")
        return 0

    # Should not happen
    return 2


if __name__ == '__main__':
    raise SystemExit(main())
