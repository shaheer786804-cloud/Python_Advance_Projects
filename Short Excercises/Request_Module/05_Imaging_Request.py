import requests as req
from io import BytesIO
from PIL import Image

r = req.get("https://static0.cbrimages.com/wordpress/wp-content/uploads/2024/08/sasuke.jpg?w=1200&h=675&fit=crop")
i = Image.open(BytesIO(r.content))

fp = open("Sasuke_Image.jpg" , "wb")
i.save(fp)
fp.close
