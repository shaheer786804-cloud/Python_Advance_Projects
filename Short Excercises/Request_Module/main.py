import requests as req

r = req.get("https://www.google.com")
print(r)

with open("index.htm" , "w") as f:
    f.write(r.text)