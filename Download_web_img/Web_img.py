import random
import urllib.request

def Web_img(url):
    name = random.randrange(0,1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

Web_img("https://images7.alphacoders.com/411/thumb-1920-411827.jpg")
print("Image Downloaded")