import requests as req
import tqdm
try:
    url = "https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-723.exe"
    r = req.get(url , stream= True)

    totalExpectedBytes = int(r.headers["Content-Length"])
    print(totalExpectedBytes)
    BytesReceived = 0
    Progress_bar = tqdm.tqdm(total=totalExpectedBytes , unit="iB" , unit_scale=True)
    with open("winrar.exe", 'wb') as fd:
        for chunk in r.iter_content(chunk_size=1000):
            # print(f"{BytesReceived} received out of {totalExpectedBytes}")
            Progress_bar.update(1000)
            fd.write(chunk)
            BytesReceived += 1000

    Progress_bar.close
except Exception as e:
    print(e)