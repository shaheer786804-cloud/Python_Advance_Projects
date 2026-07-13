import requests as req

def stock():
    url = "https://api.freeapi.app/api/v1/public/stocks/INFY"
    response = req.get(url)
    information = response.json()

    if information["success"] and "data" in information:
        stock_information = information["data"]
        name = stock_information["Name"]
        Symbol = stock_information["Symbol"]
        return name , Symbol
    
def main():
    try:
        name , Symbol = stock()
        print(f"Stock Name : {name} \n Symbol :{Symbol}")

    except Exception as e:
        print("An error Occur :" , e)
    
if __name__ == "__main__":
    main()

    