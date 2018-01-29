import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1,1000)
    full_name = str (name)+".jpg"
    urllib.request.urlretrieve(url,full_name)

download_web_image("http://www.firstpost.com/wp-content/uploads/2014/07/DANUSH_VIP.gif")