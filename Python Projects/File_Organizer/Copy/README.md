# File Cloner Utility

A lightweight, interactive Python command-line utility designed to easily duplicate and back up files. It supports copying files within the same directory or automatically creating new destination folders if they do not exist.

## Features

* **Interactive CLI:** Prompts the user step-by-step for the source file name, target name, and target directory.
* **Smart Directory Creation:** Automatically detects if a target folder is missing and creates it on the fly using the `os` module.
* **Persistent Execution:** Built with a master control loop (`while True`) that remains open, allowing you to copy multiple files in a single session without restarting the script.
* **Robust Error Handling:** Uses `try-except` blocks to gracefully catch issues like missing source files or invalid paths, preventing crashes and offering helpful suggestions.

## How It Works

1. **Imports:** Utilizes the built-in `os` module for path management and safe aliases `shutil` as `s` for high-level file operations.
2. **Path Resolution:** If the folder input is left empty, it safely copies the file into the current working directory. If a path is provided, it uses `os.path.join` to cleanly assemble the destination route.
3. **Loop Control:** Evaluates user intent at the end of each operation, safely exiting only when the user types something other than `yes` or `y`.

## Requirements

* Python 3.x
* No external dependencies required (uses standard built-in libraries).

## How to Run

1. Open your terminal or VS Code workbench.
2. Run the script using:
   ```bash
   python your_script_name.py