import random,os, bs4,requests,webbrowser
import urllib.request
from bs4 import BeautifulSoup

def download_web_image(img_url):
    name = random.randrange(1,1000)
    full_name = str (name)+".jpg"
    urllib.request.urlretrieve(img_url,full_name)

#download_web_image("http://www.firstpost.com/wp-content/uploads/2014/07/DANUSH_VIP.gif")


url = 'https://www.flickr.com/search/?text='+'animals'
#print('enter you search here:')
#search = input()
#url = url + search
print('Googling...')
#webbrowser.open(url)
#res = requests.get(url)
soup = BeautifulSoup(url)
#img_url = soup.find('div', {'class': 'view photo-list-photo-view requiredToShowOnServer awake'  'background-image: url(//c1.staticflickr.com/9/8519/8620325735_5cb816e47d_m.jpg)'})
img_url = soup.findAll("a", {"class":"image"})
for img_link in img_url:
    print(img_link.img['src'])
#download_web_image(img_url)

