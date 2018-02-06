import requests, sys, webbrowser, bs4
print('Googling...')
res = requests.get('https://www.google.com/search?q='+'education')
#res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
linkElems = soup.select('.r  a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('https://www.google.com' + linkElems[i].get('href'))