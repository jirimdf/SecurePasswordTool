# Secure Password Tool

[![Tests](https://github.com/jirimdf/SecurePasswordTool/actions/workflows/tests.yml/badge.svg)](https://github.com/jirimdf/SecurePasswordTool/actions/workflows/tests.yml)

A command-line tool for hashing and verifying passwords in Python. It generates salted hashes using PBKDF2, supports an optional pepper, and stores the results in a local SQLite database.

## Features

- Generate salted password hashes
- Verify a plaintext password against a stored hash
- Choose the hash algorithm (default: `sha256`)
- Configure the number of iterations (default: `100000`)
- Optional pepper for extra security
- Store and delete hashes in a local SQLite database (`passwords.db`)

## Tech stack

- Python 3 (standard library only: `hashlib`, `secrets`, `sqlite3`, `argparse`)

## Installation

No external dependencies are required.

```bash
git clone https://github.com/jirimdf/SecurePasswordTool.git
cd SecurePasswordTool
```

## Usage

| Command | Description |
|---|---|
| `python main.py --make <plaintext>` | Generate a salted hash |
| `python main.py --verify <plaintext> <hash_info>` | Verify a password against a hash |
| `python main.py --make <plaintext> --hash-type <type>` | Use a specific algorithm, e.g. `sha512` |
| `python main.py --make <plaintext> --iterations <n>` | Use a custom number of iterations |
| `python main.py --make <plaintext> --pepper <pepper>` | Add a pepper value |
| `python main.py --delete <password_id>` | Delete a stored hash by ID |
| `python main.py --help` | Show help |

### Examples

```bash
python main.py --make mypassword
python main.py --make mypassword --hash-type sha512 --iterations 200000
python main.py --verify mypassword "sha256@100000@303bb288988c281d9b199e240f2b6385@9d0563c55a5e713c1140e0d007bf6244f6d99f449cc5e6adb74ba962f4b9f2d7"
python main.py --delete 2
```

The hash info has the format `hash_type@iterations@salt@hash`. Wrap it in quotes when passing it on the command line.

## Tests

```bash
pip install pytest
python -m pytest
```

Tests run automatically on every push via GitHub Actions.

## Screenshots

### Linux
![linux](https://github.com/jirimdf/SecurePasswordTool/assets/163419314/6d5f9120-7b80-43d8-ba86-404ee16aca1b)

### Windows
![windows](https://github.com/jirimdf/SecurePasswordTool/assets/163419314/9930a448-10c0-428d-b49e-a4f74cc07d5e)

## License

This project is licensed under the [MIT License](LICENSE).
