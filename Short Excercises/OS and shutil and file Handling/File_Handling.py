with open ("file.txt" , "w") as file:
    file.write("This is a text file")

with open ("file.txt" , "a") as file:
    file.write("\nMore data is added to this file")

with open ("file.txt" , "r") as file:
    data = file.read()
print(data)