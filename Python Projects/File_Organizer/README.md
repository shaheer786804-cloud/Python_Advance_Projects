# Simple File Organizer

A lightweight, interactive command-line utility written in Python to help you easily copy or move files across folders, with automatic directory creation.

---

## Features

*   **Copy Data:** Duplicates a file to a target destination with a new name.
*   **Move Data:** Relocates a file to a new target destination (acts as a move/rename tool).
*   **Smart Folder Creation:** If the destination folder doesn't exist, the script automatically creates it for you.
*   **Interactive Interface:** Easy-to-use menu prompts that let you perform multiple operations in a single run.
*   **Error Handling:** Catches missing files or invalid paths gracefully without crashing the application.

---

## Prerequisites

To run this script, you only need Python installed on your system. It relies entirely on Python's built-in standard libraries (`os` and `shutil`), so no external third-party packages are required.

*   Python 3.x or higher

---

## How to Run

1. Clone or download this repository to your local machine.
2. Open your terminal or command prompt.
3. Navigate to the folder containing the script.
4. Run the script using the following command:

```bash
python main.py