# Put request

import requests as req

r = req.put("https://httpbin.org/put" , data={"a" : 20 , "b" : 30})

print(r.text)
