# Regex Password Strength Checker

A highly optimized, interactive Python script that evaluates the strength of a user-provided password using Regular Expressions (Regex) for instant pattern matching.

## Features

- **Length Validation:** Restricts passwords strictly to a healthy range of 8 to 20 characters.
- **Regex-Powered Scanning:** Utilizes Python's native `re` module to instantly detect character categories without messy, memory-heavy lookup lists.
- **Granular Strength Ratings:** Automatically groups findings into four clean categories:
  - 💪 **Very Strong:** Features lowercase, uppercase, numbers, and symbols.
  - 👍 **Strong Enough:** Misses only 1 category.
  - ⚠️ **Not Strong Enough:** Features only 2 categories.
  - ❌ **Too Weak:** Features only 1 single category.

---

## Prerequisites

- Python 3.x

This script depends entirely on built-in standard libraries (`re` and `time`), meaning **no external packages or installations (`pip`) are required**.

---

## How to Run

1. **Save the Code:** 
   Save your script locally as `password_checker.py`.

2. **Run via Terminal/Command Prompt:**
   ```bash
   python password_checker.py