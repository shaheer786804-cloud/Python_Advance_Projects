while True:

    import os
    import shutil as s
    print("\nEnter Your Choice")
    print("1 to continue")
    print("2 to exit")
    select = (input("Enter your choice :"))

    if select == "2":
        
        print("Exiting the file Organizer")
        break
    if select != "1":
        print("Please enter correct choice")
        continue

    print("\nEnter Your Choice")
    print("\n\n1.to copy data")
    print("2.to move data")
    choice = input("Enter Your Choice :" )
    if choice == "1":
        import Copy.copy   
    
    if choice == "2":
        import Move.move
        