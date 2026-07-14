# Website Status Monitor & Expense Tracker

A collection of lightweight, interactive Python command-line interface (CLI) tools designed to automate everyday tasks. This repository currently features a **Simple Expense Tracker** and a **Website Status Monitor** to demonstrate foundational concepts in file handling, data serialization, and network programming.

---

## 🛠️ Features

### 1. Simple Expense Tracker
Manage your daily spending straight from the terminal. 
* **Add Expenses:** Log an item name, cost, and category.
* **Input Validation:** Automatically handles invalid price formatting gracefully.
* **View & Delete:** Review your structured expense list and delete items dynamically by their list number.
* **CSV Export:** Instantly exports your logs to `expenses.csv` using Python's native `csv.DictWriter`.

### 2. Website Status Monitor
An automated helper to check if your favorite sites or projects are online.
* **Flexible Inputs:** Load multiple target URLs from a `urls.txt` file or input a single URL on the fly.
* **Robust Logging:** Outputs status logs to both the terminal and a local `monitor.log` file.
* **Structured Data Export:** Automatically generates both a `urls_result.csv` report and a structured `urls_result.json` payload.

---

## 📂 Project Structure

```text
├── monitor.py              # Website status checking script
├── urls.txt                # (Optional) Text file containing URLs to monitor
├── README.md               # Project documentation