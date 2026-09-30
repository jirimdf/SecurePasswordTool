import sqlite3

import pytest

import main


def test_hash_format():
    parts = main.make_hash("secret", iterations=1000).split("@")
    assert parts[0] == "sha256"
    assert parts[1] == "1000"
    assert len(parts[2]) == 32
    assert len(parts) == 4


def test_verify_correct_password():
    hashed = main.make_hash("secret", iterations=1000)
    assert main.verify_hash("secret", hashed)


def test_verify_wrong_password():
    hashed = main.make_hash("secret", iterations=1000)
    assert not main.verify_hash("wrong", hashed)


def test_salt_is_random():
    assert main.make_hash("secret", iterations=1000) != main.make_hash("secret", iterations=1000)


def test_pepper_is_required_for_verification():
    hashed = main.make_hash("secret", iterations=1000, pepper="pep")
    assert main.verify_hash("secret", hashed, pepper="pep")
    assert not main.verify_hash("secret", hashed)


@pytest.mark.parametrize("hash_type", ["sha256", "sha512"])
def test_hash_types(hash_type):
    hashed = main.make_hash("secret", hash_type=hash_type, iterations=1000)
    assert hashed.startswith(hash_type + "@")
    assert main.verify_hash("secret", hashed)


def test_database_insert_and_delete(tmp_path, monkeypatch):
    db = tmp_path / "passwords.db"
    monkeypatch.setattr(main, "DATABASE_FILE", str(db))
    main.create_database()
    main.insert_password("sha256@1000@salt@hash")

    with sqlite3.connect(db) as conn:
        rows = conn.execute("SELECT id, hashed_password FROM passwords").fetchall()
    assert rows == [(1, "sha256@1000@salt@hash")]

    main.delete_password(1)
    with sqlite3.connect(db) as conn:
        assert conn.execute("SELECT COUNT(*) FROM passwords").fetchone()[0] == 0
