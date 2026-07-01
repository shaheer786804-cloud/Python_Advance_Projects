from time import sleep
alphabets = (
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
)
alphabets_upper = (
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
)
numbers = (
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
)
special_characters = (
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", 
    "+", "[", "]", "{", "}", ";", ":", "'", '"', ",", "<", ".", ">", 
    "/", "?", "|"
)

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
        print("It must contain at most 16 characters.")
        return

    print("Let's check the strength of your Password...")
    sleep(1.5)
    # 2. Check character categories
    has_lower = any(char in alphabets for char in Password)
    has_upper = any(char in alphabets_upper for char in Password)
    has_num = any(char in numbers for char in Password)
    has_special = any(char in special_characters for char in Password)

    # 3. Strength Logic (Flipped from Strongest to Weakest)
    
    # LEVEL 4: Very Strong (Checks all 4 categories)
    if (has_lower and has_upper and has_num and has_special) and (8 <= len(Password) <= 20):
        print("Your Password is very strong! Excellent.")

    # LEVEL 3: Strong Enough (Checks groups of 3 categories)
    elif ((has_lower and has_upper and has_num) or 
          (has_lower and has_upper and has_special) or 
          (has_lower and has_num and has_special) or 
          (has_upper and has_num and has_special)) and (8 <= len(Password) <= 20):
        print("Your Password is strong enough!")

    # LEVEL 2: Not Strong Enough (Checks pairs of 2 categories)
    elif ((has_lower and has_upper) or (has_lower and has_num) or 
          (has_lower and has_special) or (has_upper and has_num) or 
          (has_upper and has_special) or (has_num and has_special)) and (8 <= len(Password) <= 20):
        print("Your Password is not strong enough!")

    # LEVEL 1: Too Weak (Only matching 1 category total)
    elif (has_lower or has_upper or has_num or has_special) and (8 <= len(Password) <= 20):
        print("Your Password is too weak!")
        
    else:
        print("Your Password Should contains character between 8-20")

Password_strength_Checker()
