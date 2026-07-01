# Password Strength Checker

A simple, interactive Python script that evaluates the strength of a user-provided password based on its length and character diversity.

## Features

- **Length Validation:** Ensures passwords are between 8 and 20 characters long.
- **Character Diversity Checks:** Scans for lowercase letters, uppercase letters, numbers, and special characters.
- **Granular Strength Ratings:** Categorizes passwords into four distinct strength levels:
  - 💪 **Very Strong:** Contains all 4 character types.
  - 👍 **Strong Enough:** Contains any 3 character types.
  - ⚠️ **Not Strong Enough:** Contains any 2 character types.
  - ❌ **Too Weak:** Contains only 1 character type.

---

## Prerequisites

Before running the script, make sure you have Python installed on your system:
- Python 3.x

The script uses the standard library `time` module, so no external package installations (`pip`) are required.

---

## How to Run

1. **Clone or Download the Repository:**
   Save the script file as `password_checker.py`.

2. **Open your Terminal or Command Prompt and run:**
   ```bash
   python password_checker.py