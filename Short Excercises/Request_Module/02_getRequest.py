import requests as req

r = req.get("https://httpbin.org/get")

print(r.text)