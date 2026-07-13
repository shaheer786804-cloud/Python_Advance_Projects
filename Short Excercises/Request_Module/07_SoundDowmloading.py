import requests as req

url = "https://cdn.pixabay.com/download/audio/2025/03/22/audio_033f72065b.mp3?filename=kave_msri-cinematic-hit-3-317170.mp3"
r = req.get(url)

fp = open("sound.mp3" , "wb")
fp.write(r.content)
fp.close
