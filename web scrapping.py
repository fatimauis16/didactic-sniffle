import requests
from bs4 import BeautifulSoup as bs

url=https://www.neweggbusiness.com/product/product.aspx?item=9siv1w18cc7026

page=requests.get(url)

pp=str(page.content)

soup=bs(page.contebt, 'html.parser')

title=soup.find_all('h1',attrs={'class':'product-title'})[0].get_text()

price=soup.find_all('div',attrs={'class':'price-currency'})[0].get text()

print(price)
