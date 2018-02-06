from bs4 import BeautifulSoup
from urllib2_file import urlaopen
film_id = '0423409'
url = 'http://www.imdb.com/title/tt%s/' % (film_id)
soup = BeautifulSoup(urllib2.urlopen(url).read())
link = soup.find(itemprop="image")
print(link["src"])