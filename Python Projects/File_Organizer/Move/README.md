# File Mover Utility

A practical, interactive Python command-line utility built to relocate (move) and rename files on your system. It features automated directory creation and safe file transferring paths.

## Features

* **Interactive Relocation:** Prompts users for the target file, its new name, and the destination folder path.
* **On-the-Fly Folder Creation:** Uses Python's `os` module to automatically check for and construct missing folder paths before executing a transfer.
* **Master Loop Structure:** Employs a persistent `while True` block so you can move or rename multiple files back-to-back without having to rerun the script.
* **Defensive Exception Handling:** Implements `try-except` wrappers around high-level file operations to cleanly trap issues like missing source files or invalid system paths.

## How It Works

1. **Path Assembling:** Utilizing `os.path.join()`, it merges the folder location and the new file name into a single clean destination path.
2. **File Transfer:** Executes `shutil.move()` (aliased as `s.move`), which effectively handles cutting and pasting files across directories or simply renaming them in place.
3. **Loop Control Evaluation:** Safely ends the runtime execution if the user answers anything other than `yes` or `y` at the end-of-operation prompt.

## Requirements

* Python 3.x
* Built entirely with standard libraries (`os`, `shutil`) — no external packages required.

## How to Run

1. Open your terminal or VS Code environment.
2. Execute the script:
   ```bash
   python your_script_name.py