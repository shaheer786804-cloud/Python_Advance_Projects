import requests as req

r = req.post("https://httpbin.org/post" , data= {"Subject" : "Math"})

print(r.text)
