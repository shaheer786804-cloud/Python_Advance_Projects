while True:

    print("Chooes an option")
    print("1 :Continue")
    print("2 : end")
    choice = int(input("Enter your Choice :"))
    if choice == 2:
        break
    elif choice != 1:
        print("Print from given choices")
        continue       
    try:
        a = int(input("Enter numinator :" ,))
        b = int(input("Enter denominator :" ,))
        c = a / b
        print("Result =" ,c) 

    except Exception as e:
        print("An error occur :" , e)
        print("Check your value and try again") 
    finally:
        print("Choose options of starting or ending program")
          

