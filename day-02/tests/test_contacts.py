import json
import subprocess
import sys
from pathlib import Path
from day_01_import_helper import import_from_path

# Import module functions for unit testing
mod = import_from_path('contacts', 'day-02/contacts.py')


def run_cli(args, cwd=None):
    cmd = [sys.executable, 'day-02/contacts.py'] + args
    res = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)
    return res.returncode, res.stdout.strip(), res.stderr.strip()


def test_add_and_list_with_db(tmp_path):
    db = tmp_path / 'contacts.json'
    code, out, err = run_cli(['--db', str(db), 'add', '--name', 'Ada', '--phone', '123'])
    assert code == 0 and 'Added contact #1' in out

    code, out, err = run_cli(['--db', str(db), 'add', '--name', 'Bob', '--phone', '456', '--email', 'b@example.com', '--tags', 'sales', 'apac'])
    assert code == 0 and 'Added contact #2' in out

    code, out, err = run_cli(['--db', str(db), 'list'])
    assert code == 0
    assert 'Ada' in out and 'Bob' in out
    assert 'sales,apac' in out


def test_find_and_delete(tmp_path):
    db = tmp_path / 'contacts.json'
    run_cli(['--db', str(db), 'add', '--name', 'Alice', '--phone', '111'])
    run_cli(['--db', str(db), 'add', '--name', 'Alicia', '--phone', '222'])
    run_cli(['--db', str(db), 'add', '--name', 'Charlie', '--phone', '333'])

    code, out, err = run_cli(['--db', str(db), 'find', '--q', 'lic'])
    assert code == 0
    # Should match Alice and Alicia only
    assert 'Alice' in out and 'Alicia' in out and 'Charlie' not in out

    # Delete existing
    code, out, err = run_cli(['--db', str(db), 'delete', '--id', '2'])
    assert code == 0 and 'Deleted contact id 2' in out

    # Delete non-existent
    code, out, err = run_cli(['--db', str(db), 'delete', '--id', '999'])
    assert code == 1 and 'not found' in err


def test_function_add_validation():
    db = {"next_id": 1, "contacts": []}
    try:
        mod.add_contact(db, name='', phone='123')
        assert False, 'Expected ValueError for empty name'
    except ValueError:
        pass
    try:
        mod.add_contact(db, name='Test', phone='')
        assert False, 'Expected ValueError for empty phone'
    except ValueError:
        pass

    c = mod.add_contact(db, name='Zoe', phone='999', email='z@example.com', tags=['se'])
    assert c['id'] == 1 and c['name'] == 'Zoe'
    assert db['next_id'] == 2
