import random,os, bs4,requests,webbrowser
import urllib.request
from bs4 import BeautifulSoup

def download_web_image(img_url):
    name = random.randrange(1,1000)
    full_name = str (name)+".jpg"
    urllib.request.urlretrieve(img_url,full_name)

download_web_image("https://www.flickr.com/photos/cheishichiyo/6131747939/")