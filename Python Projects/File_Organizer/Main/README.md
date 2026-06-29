# File Organizer Utility

An interactive command-line interface (CLI) application built in Python that provides a menu-driven system for managing, copying, and moving files. 

## Features

* **Menu-Driven Navigation:** Uses clear numeric choices (`1` or `2`) to guide the user through continuing, exiting, or choosing between file actions.
* **Master Control Loop:** Implements a `while True` loop structure to keep the program open, allowing for seamless multiple file operations without needing to restart the script.
* **Input Validation:** Protects against unexpected entries by alerting users if they enter an invalid option and restarting the prompt using the `continue` statement.

## How It Works

1. **Session Gatekeeping:** The program begins by asking if you want to continue (`1`) or exit (`2`). This acts as an initial gateway to capture user intent immediately.
2. **Action Selection:** Once inside, a sub-menu presents the choice to either copy or move data.
3. **Loop Integrity:** Choosing to exit breaks the loop cleanly with a goodbye message.

## Code Improvement Note 💡

To make the copy and move choices functional, the shell utilities module (`shutil`) should be used directly instead of importing `copy` or `move` as separate packages. 

For the final implementation, update the action blocks to call the functions directly:
* For **Copy**: Use `s.copy(source, destination)`
* For **Move**: Use `s.move(source, destination)`

## Requirements

* Python 3.x
* Uses built-in standard libraries (`os`, `shutil`).