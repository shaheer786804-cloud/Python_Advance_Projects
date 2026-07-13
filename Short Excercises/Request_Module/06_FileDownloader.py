import requests as req

url = "https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-723.exe"
r = req.get(url)

fp = open("winrar.exe" , "wb")
fp.write(r.content)
fp.close
