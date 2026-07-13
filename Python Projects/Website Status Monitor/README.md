# Website Status Monitor

A lightweight Python automation tool that reads a list of URLs from a text file, tests their connectivity via HTTP requests, logs the results in real-time, and exports the data into both CSV and JSON formats. 

This project is perfect for monitoring uptime or verifying a batch of links quickly.

## Features
* **Batch Processing:** Reads multiple URLs from a plain text file (`urls.txt`).
* **Real-Time Logging:** Outputs detailed logs simultaneously to the terminal and a local log file (`monitor.log`).
* **Robust Error Handling:** Catches timeouts, invalid URLs, and network drops without crashing the script.
* **Dual-Format Export:** Automatically generates structured `urls_result.csv` and `urls_result.json` reports after completion.

---

## Skills Learned & Applied
* **`requests`**: Handling HTTP requests, status codes, and timeouts.
* **File I/O**: Reading data from text files and writing to structured file formats.
* **`logging`**: Implementing professional multi-handler logging (file + console streams) with timestamps.
* **Data Serialization**: Formatting Python dictionaries into JSON arrays and rows of CSV data.

---

## Getting Started

### Prerequisites
Make sure you have Python installed on your system. You will also need the `requests` library. You can install it via pip:

```bash
pip install requests

