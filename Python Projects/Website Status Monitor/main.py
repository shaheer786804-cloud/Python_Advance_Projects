# Website Status Monitor
# Reads URLs from a file, sends HTTP requests, logs response codes, saves CSV/JSON results, and alerts if a site is down.
# Skills learned: requests, files, logging, automation.

import csv
import json
import logging
import requests as req


def website_status_monitor():
    # --- 1. SETUP LOGGING ---
    # This configures logging to save messages to 'monitor.log' AND print them to the terminal.
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("monitor.log", encoding='utf-8'),
            logging.StreamHandler()  # This keeps the terminal outputs visible
        ]
    )
    print("-" * 15)
    print("Enter your choice")
    print("-" * 15)

    print("1.Take URL from the text file urls.txt")
    print("2.You want to enter the url")
    print("3.To Exit")
    choice = input("Enter your choice: ")

    if choice == '1':

        # 2. Load the URLs from your text file
        try:
            with open("urls.txt", "r") as file:
                urls = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            logging.error("The file 'urls.txt' does not exist. Please check the filepath.")
            urls = []

        # 3. Process URLs and save results if we actually found URLs
        if urls:
            json_results = []

            # Open the CSV file for writing
            with open('urls_result.csv', 'w', newline='', encoding='utf-8') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(['URL', 'Status Code', 'Result']) 
                
                # Loop through every URL loaded from the file
                for url in urls:
                    logging.info(f"Testing connection to: {url}")
                    
                    try:
                        # Send the HTTP GET request
                        response = req.get(url, timeout=5)
                        status = response.status_code
                        
                        if status == 200:
                            result_msg = "Success! The website is up and running."
                            logging.info(f"{url} - Status: {status} - {result_msg}")
                        else:
                            result_msg = f"Website returned an issue. Status: {status}"
                            logging.warning(f"{url} - Status: {status} - {result_msg}")
                            
                    except req.exceptions.RequestException as e:
                        status = "ERROR"
                        result_msg = f"Network error: {str(e)}"
                        logging.error(f"Could not connect to {url}. Error details: {e}")
                        
                    # A. Write the data into the CSV row
                    csv_writer.writerow([url, status, result_msg])
                    
                    # B. Create a dictionary for this URL and append it to our JSON list
                    url_data = {
                        "url": url,
                        "status_code": status,
                        "result": result_msg
                    }
                    json_results.append(url_data)

            # 4. Save all collected data into a JSON file
            with open('urls_result.json', 'w', encoding='utf-8') as json_file:
                json.dump(json_results, json_file, indent=4)

            logging.info("Processing complete!")
            logging.info("-> Results saved to 'urls_result.csv'")
            logging.info("-> Results saved to 'urls_result.json'")
        else:
            logging.warning("No URLs to process.")




    elif choice == '2' :
        url = input("Enter the URL: ").strip()

        if url:
            json_results = []
            
            # Open the CSV file for writing
            with open('urls_result.csv', 'w', newline='', encoding='utf-8') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(['URL', 'Status Code', 'Result']) 
                
                logging.info(f"Testing connection to: {url}")
                try:
                    # Send the HTTP GET request
                    response = req.get(url, timeout=5)
                    status = response.status_code
                    
                    if status == 200:
                        result_msg = "Success! The website is up and running."
                        logging.info(f"{url} - Status: {status} - {result_msg}")
                    else:
                        result_msg = f"Website returned an issue. Status: {status}"
                        logging.warning(f"{url} - Status: {status} - {result_msg}")
                        
                except req.exceptions.RequestException as e:
                    status = "ERROR"
                    result_msg = f"Network error: {str(e)}"
                    logging.error(f"Could not connect to {url}. Error details: {e}")
                    
                # A. Write the data into the CSV row
                csv_writer.writerow([url, status, result_msg])
                
                # B. Create a dictionary for this URL and append it to our JSON list
                url_data = {
                    "url": url,
                    "status_code": status,
                    "result": result_msg
                }
                json_results.append(url_data)

            # 4. Save all collected data into a JSON file
            with open('urls_result.json', 'w', encoding='utf-8') as json_file:
                json.dump(json_results, json_file, indent=4)

            logging.info("Processing complete!")
            logging.info("-> Results saved to 'urls_result.csv'")
            logging.info("-> Results saved to 'urls_result.json'")
        else:
            logging.warning("No URL was entered.")
            
    elif choice == '3':
        print("Exiting the Website status monitor")
        print("-" * 15)
        print("Good Bye")
        print("-" * 15)
        exit() 

    else :
        print("-" * 15)
        print("Invalid Choice")
        print("-" * 15)
        

while True:        
    website_status_monitor()