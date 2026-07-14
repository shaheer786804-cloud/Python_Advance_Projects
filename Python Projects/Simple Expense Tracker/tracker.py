expenses = []

def add_expense():
    name = input("What did you buy? ").strip()
    try:
        amount = float(input("How much did it cost? $"))
        category = input("Enter category (e.g., Food, Tech): ").strip()
        
        expense = {
            "name": name, 
            "amount": amount, 
            "category": category
        }
        
        expenses.append(expense)
        print(f"✅ Added: {name} (${amount})")
        
    except ValueError:
        print("❌ Error: Please enter a valid number for the price.")

def view_expenses():
    if not expenses:
        print("\n📭 No expenses recorded yet.")
        return False 
    
    print("\n--- Your Expenses ---")
    count = 1  
    for exp in expenses:
        item_name = exp["name"]
        item_price = exp["amount"]
        item_tag = exp["category"]
        
        print(count, ".", item_name, "| $", item_price, "| [", item_tag, "]")
        count = count + 1  
    return True 

def delete_expense():
    view_expenses() 
    
    if not expenses:
        print("No expenses to delete!")
        return

    choice = input("Enter the number to delete: ")
    
    try:
        index_to_remove = int(choice) - 1
        
        if 0 <= index_to_remove < len(expenses):

            removed_item = expenses.pop(index_to_remove)
            print(f"Deleted '{removed_item}' successfully!")
        else:
            print("Invalid number. That item isn't on the list.")
            
    except ValueError:
        # This catches inputs like "abc", "", or symbols
        print("Please enter a valid whole number.")


def simple_expense_tracker():
    print("\n" + "-" * 30)
    print("   Welcome to Expense Tracker   ")
    print("-" * 30)
    print("1. To add expense")
    print("2. To check your expenses")
    print("3. To delete an expense") # New option!
    print("4. To exit")
    print("-" * 30)
    
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        delete_expense()
    elif choice == '4':
        print("\nGoodbye!")
        exit()
    else:
        print("Invalid value entered")

while True:
    simple_expense_tracker()