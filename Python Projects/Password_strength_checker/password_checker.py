import re
from time import sleep

def Password_strength_Checker():
    Password = input("\nEnter your password (or type 'exit' to quit): ")
    
    if Password.lower() == 'exit':
        return "exit"

    # 1. Length Validations
    if len(Password) < 8:
        print("Password is too short!")
        print("It must contain at least 8 characters.")
        return

    if len(Password) > 20:
        print("Password is too long!")
        print("It must contain at most 20 characters.")  # Fixed: changed from 16 to 20 to match logic
        return

    print("Let's check the strength of your Password...")
    sleep(1.5)

    # 2. Check character categories using Regex
    # re.search() returns a match object if found, which Python evaluates as True
    has_lower = bool(re.search(r'[a-z]', Password))
    has_upper = bool(re.search(r'[A-Z]', Password))
    has_num = bool(re.search(r'[0-9]', Password))
    # This matches any character that IS NOT a letter, number, or whitespace
    has_special = bool(re.search(r'[^a-zA-Z0-9\s]', Password))

    # 3. Strength Logic 
    # Note: We can remove the length checks here since we already filtered out 
    # passwords shorter than 8 or longer than 20 at the beginning of the function.
    
    # LEVEL 4: Very Strong (Checks all 4 categories)
    if has_lower and has_upper and has_num and has_special:
        print("Your Password is very strong! Excellent.")

    # LEVEL 3: Strong Enough (Checks groups of 3 categories)
    elif ((has_lower and has_upper and has_num) or 
          has_lower and has_upper and has_special or 
          has_lower and has_num and has_special or 
          has_upper and has_num and has_special):
        print("Your Password is strong enough!")

    # LEVEL 2: Not Strong Enough (Checks pairs of 2 categories)
    elif ((has_lower and has_upper) or (has_lower and has_num) or 
          (has_lower and has_special) or (has_upper and has_num) or 
          (has_upper and has_special) or (has_num and has_special)):
        print("Your Password is not strong enough!")

    # LEVEL 1: Too Weak (Only matching 1 category total)
    elif has_lower or has_upper or has_num or has_special:
        print("Your Password is too weak!")
        
    else:
        print("Your Password should contain characters between 8-20.")

Password_strength_Checker()