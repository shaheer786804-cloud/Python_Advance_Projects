import os 

if(not os.path.exists("Tutorials")):
     os.mkdir("Tutorials")
for i in range(0 , 5):
     os.mkdir(f"Tutorials\ Tutorial {i+1}")
 




