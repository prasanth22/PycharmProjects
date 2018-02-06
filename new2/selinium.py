import re
import requests
from bs4 import BeautifulSoup

site = 'https://www.flickr.com/search/?text=animals'

response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all("div", {"background-image":"url"})


#urls = [img['src'] for img in img_tags]
print(img_tags)


#for url in urls:
 #  with open(filename.group(1), 'wb') as f:
  #         # sometimes an image source can be relative
            # if it is provide the base url which also happens
            # to be the site variable atm.
   #         url = '{}{}'.format(site, url)
    #    response = requests.get(url)
     #   f.write(response.content)