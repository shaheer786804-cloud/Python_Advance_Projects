import os
import shutil as s

while True:
    file = input("Enter the name of file (with extension, e.g., document.txt): ")
    file_new_name = input("Enter the new name of the file (e.g., moved_file.txt): ")
    folder_location = input("Enter the folder path where you want to save it(leave empty to save in same folder): ")
    
    try:
        if folder_location == "":
            destination_path = file_new_name 

        else: 
            not os.path.exists(folder_location)
            os.makedirs(folder_location)
            print(f"Created new directory: {folder_location}")

        destination_path = os.path.join(folder_location, file_new_name)
        
        s.move(file, destination_path)
        print(f"Successfully moved and saved to its destination")
        
    except Exception as e:
        print("An error occurred:", e)
        print("Please check your file name and folder path, then try again.")
    
    print("-" * 30)

    choice = input("Do you want to move another file? (yes/no): ").lower()
    if choice not in ['yes', 'y']:
        print("Exiting system. Goodbye!")
        break
    