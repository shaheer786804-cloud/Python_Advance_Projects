import requests as req

def random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    responce = req.get(url)
    Information = responce.json()

    if Information["success"] and "data" in Information:
        user_data = Information["data"]
        user_name = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return user_name, country
    
    else:
        raise Exception ("Fail to Fetch userdata")

def main():
    try:
        user_name, country = random_user()
        print(f"User_Name : {user_name} \n Country : {country}")

    except Exception as e:
        print("An error occur :", e)

if __name__ == "__main__":
    main()    