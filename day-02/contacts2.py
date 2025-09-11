import argparse
import json
import sys
from typing import List, Dict
from pathlib import Path

class ContactBook:
    def __init__(self, db_path: str = None):
        self.contacts: List[Dict] = []
        self.next_id = 1
        self.db_path = db_path
        if db_path and Path(db_path).exists():
            self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.db_path, 'r') as f:
                data = json.load(f)
                self.contacts = data.get('contacts', [])
                self.next_id = max((c['id'] for c in self.contacts), default=0) + 1
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in database file: {self.db_path}") from e

    def save_contacts(self):
        if self.db_path:
            # Ensure parent directory exists before writing
            Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)
            with open(self.db_path, 'w') as f:
                json.dump({'contacts': self.contacts}, f, indent=2)

    def add_contact(self, name: str, phone: str, email: str, tags: List[str]) -> int:
        contact = {
            'id': self.next_id,
            'name': name,
            'phone': phone,
            'email': email,
            'tags': tags
        }
        self.contacts.append(contact)
        self.next_id += 1
        self.save_contacts()
        return contact['id']

    def list_contacts(self, sort_by: str) -> List[Dict]:
        if sort_by == 'name':
            return sorted(self.contacts, key=lambda c: c['name'].lower())
        if sort_by == 'id':
            return sorted(self.contacts, key=lambda c: c['id'])
        raise ValueError(f"Invalid sort key: {sort_by}")

    def find_contacts(self, query: str) -> List[Dict]:
        query = query.lower()
        return [c for c in self.contacts if (
            query in c['name'].lower() or
            query in c['phone'].lower() or
            query in c['email'].lower() or
            any(query in tag.lower() for tag in c['tags'])
        )]

    def delete_contact(self, contact_id: int) -> bool:
        initial_len = len(self.contacts)
        self.contacts = [c for c in self.contacts if c['id'] != contact_id]
        if len(self.contacts) < initial_len:
            self.save_contacts()
            return True
        return False

def parse_args():
    parser = argparse.ArgumentParser(description="Contact book CLI")
    parser.add_argument('--db', help="Path to JSON database")
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Add command
    add_parser = subparsers.add_parser('add', help="Add a new contact")
    add_parser.add_argument('--name', required=True)
    add_parser.add_argument('--phone', required=True)
    add_parser.add_argument('--email', required=True)
    add_parser.add_argument('--tags', nargs='*', default=[])

    # List command
    list_parser = subparsers.add_parser('list', help="List contacts")
    list_parser.add_argument('--sort-by', choices=['id', 'name'], default='id')

    # Find command
    find_parser = subparsers.add_parser('find', help="Find contacts")
    find_parser.add_argument('--q', required=True)

    # Delete command
    delete_parser = subparsers.add_parser('delete', help="Delete a contact")
    delete_parser.add_argument('--id', type=int, required=True)

    return parser.parse_args()

def format_contact(contact: Dict) -> str:
    tags = ', '.join(contact['tags'])
    return f"#{contact['id']}: {contact['name']}, {contact['phone']}, {contact['email']}, tags: [{tags}]"


def main():
    args = parse_args()
    try:
        book = ContactBook(args.db)

        if args.command == 'add':
            contact_id = book.add_contact(args.name, args.phone, args.email, args.tags)
            print(f"Added contact #{contact_id}: {args.name}")
            sys.exit(0)

        elif args.command == 'list':
            contacts = book.list_contacts(args.sort_by)
            for contact in contacts:
                print(format_contact(contact))
            sys.exit(0)

        elif args.command == 'find':
            contacts = book.find_contacts(args.q)
            for contact in contacts:
                print(format_contact(contact))
            sys.exit(0)

        elif args.command == 'delete':
            if book.delete_contact(args.id):
                print(f"Deleted contact #{args.id}")
                sys.exit(0)
            else:
                print(f"Contact #{args.id} not found")
                sys.exit(1)
    except ValueError as e:
        print(str(e), file=sys.stderr)
        sys.exit(2)
    except (OSError, IOError) as e:
        print(f"I/O error: {e}", file=sys.stderr)
        sys.exit(2)

if __name__ == '__main__':
    main()
