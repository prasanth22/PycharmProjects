import requests
from bs4 import BeautifulSoup
def web_page(max_page):
    page = 2
    while page < max_page:
        url = 'http://hannenorak.com/catalogue/page/'+str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for h2 in soup.find_all('h2',{'class':'woocommerce-loop-product__title'}):
            book_names = h2.string
            print(book_names)
        page+=1
web_page(3)


