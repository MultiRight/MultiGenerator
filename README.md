# MultiGenerator

A secure, terminal-based password generator written in Python.

---

## Overview

MultiGenerator is a command-line utility that generates cryptographically secure passwords using Python's `secrets` module. It is designed to be lightweight, straightforward, and reliable for everyday use.

---

## Features

- Cryptographically secure password generation via the `secrets` module
- Customizable password length between 16 and 32 characters
- Color-coded terminal interface for improved readability
- Cross-platform support (Linux, macOS, Windows)
- Built-in help page accessible via `--help`
- Clear and consistent error messages

---

## Requirements

- Python 3.6 or higher

No third-party dependencies are required.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/MultiRight/MultiGenerator
cd MultiGenerator
```

---

## Usage

Run the script using Python:

```bash
python MultiGenerator.py
```

If that does not work, try using `python3` explicitly:

```bash
python3 MultiGenerator.py
```

When prompted, enter your desired password length (between 16 and 32 characters). The generator will produce a secure password composed of uppercase and lowercase letters, digits, and special characters.

To access the help page, type `--help` when prompted at startup.

---

## Error Reference

| Code   | Description                                                  |
|--------|--------------------------------------------------------------|
| err101 | Invalid input — letters or symbols were entered instead of a number |
| err102 | Invalid length — the number entered is less than 16 or greater than 32 |
| err103 | Invalid action — the entered choice is not `r` or `q`       |

---

## Character Set

Generated passwords are drawn from the following character set:

```
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789
!@#$%^&*-_=+
```

---

## License

Copyright &copy; 2026 MultiRight &lt;https://github.com/MultiRight&gt;

This project is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html).

---

## 🐱 Special Thanks

A special thanks to mimi — the legendary, the great, the gentle cat.
