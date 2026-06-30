# multigenerator

A simple tool that creates strong, random passwords for you.

---

## What is this?

multigenerator is a small Python program that runs in your terminal and generates secure passwords. Just pick a length, and it gives you a password ready to use.


---

## Requirements

- Python 3.6 or later — [Download here](https://www.python.org/downloads/)
- Nothing else to install

---

## How to run it

**1. Download the project**
```bash
git clone https://github.com/MultiRight/multigenerator.git
cd multigenerator
```

**2. Run the script**
```bash
python multigenerator.py
```

---

## How to use it

1. Press **Enter** to start
2. Type a number between **16 and 32** (your password length)
3. Your password appears on screen — copy it and save it somewhere safe
4. Press **r** to generate another one, or **q** to quit

---

## How strong are the passwords?

multigenerator mixes uppercase letters, lowercase letters, numbers, and symbols all together, so the password does not look like any real word or pattern.

The passwords are also picked completely at random every single time, so no two passwords will ever be the same.

---

## Something went wrong?

The program will always tell you what went wrong and let you try again. Here is what each message means:

| Message | What it means | What to do |
|---|---|---|
| err101 | You typed letters instead of a number | Type a number like `20` |
| err102 | The number is too small or too big | Pick a number between 16 and 32 |
| err103 | You typed something other than r or q | Type exactly `r` or `q` |


---
## License

This project is licensed under the **[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html)** 

---

## Author

MultiRight : https://github.com/MultiRight

---
## 🐱 Special Thanks

A special thanks to mimi — the legendary, the great, the gentle cat.
