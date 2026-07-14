# 📊 Command-Line Expense Tracker with CSV Export

A lightweight, interactive command-line application written in Python to help you track, manage, and export your daily expenses. This program runs directly in your terminal and saves your logged transactions into a standard CSV file format for easy opening in Excel, Google Sheets, or any other data editor.

---

## ✨ Features

- **➕ Add Expenses:** Log purchases with an item name, dollar cost, and custom tags/categories.
- **🔍 View Expenses:** View a cleanly indexed table showing your entire logged history.
- **❌ Delete Expenses:** Selectively remove specific transactions by entering their index number.
- **💾 Export to CSV:** Export your tracked memory block seamlessly into a cleanly formatted `expenses.csv` spreadsheet.
- **🛡️ Error Resilience:** Prevents crashes from invalid price inputs (e.g., text instead of numbers) or empty file exports.

---

## 🛠️ How It Works (The Code Blueprint)

The program maintains your logging session in an active list of dictionaries in Python's memory:
```python
expense = {
    "name": "Coffee", 
    "amount": 4.50, 
    "category": "Food"
}
```

When writing to a spreadsheet, it relies on Python's built-in `csv.DictWriter` to automatically map your in-memory dictionaries straight into a table structured with headers:
```csv
category,name,amount
Food,Coffee,4.5
```

---

## 🚀 Getting Started

### Prerequisites
- Make sure you have **Python 3.x** installed on your operating system.

### Running the Program
1. Save the code into a file named `tracker.py`.
2. Open your terminal or command prompt.
3. Navigate to the directory containing your file.
4. Run the program using the following command:
   ```bash
   python tracker.py
   ```

---

## 📖 Usage Guide

When you launch the program, you will be greeted with an interactive terminal interface:

```text
------------------------------
   Welcome to Expense Tracker   
------------------------------
1. To add expense
2. To check your expenses
3. To delete an expense
4. To export expenses to CSV
5. To exit
------------------------------
Enter your choice: 
```

### 1. Adding an Expense
Type `1` and press **Enter**. Enter the details when prompted:
- **What did you buy?** (e.g., `Mechanical Keyboard`)
- **How much did it cost?** (e.g., `89.99`)
- **Enter category:** (e.g., `Tech`)

### 2. Checking Your Expenses
Type `2` and press **Enter** to see all items currently in memory:
```text
--- Your Expenses ---
1. Mechanical Keyboard | $89.99 | [Tech]
2. Avocado Toast | $12.50 | [Food]
```

### 3. Deleting an Expense
Type `3` and press **Enter**. The application will list your current entries and ask for the specific number you want to delete. Inputting `2` in the example above would delete the `Avocado Toast`.

### 4. Exporting to CSV
Type `4` and press **Enter** to output all currently tracked expenses directly into `expenses.csv` inside the same directory.
