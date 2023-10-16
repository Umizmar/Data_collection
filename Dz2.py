# Урок 2. Парсинг HTML. BeautifulSoup
import json

# 1 вариант
# Выполнить скрейпинг данных в веб-сайта http://books.toscrape.com/
# и извлечь информацию о всех книгах на сайте во всех категориях:
# название, цену, количество товара в наличии (In stock (19 available)) в формате integer, описание.

# Затем сохранить эту информацию в JSON-файле.

import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = "http://books.toscrape.com/"
headers = {"User-Agent":
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
            'AppleWebKit/537.36 (KHTML, like Gecko)'
            'Chrome/117.0.0.0 Safari/537.36'}

session = requests.session()
books = []
page = 1

def book_info(href):
    book = {}

    response = session.get(url + f"/catalogue/{href}", headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    book_rows = soup.find('article', {'class': 'product_page'})

    book['title'] = book_rows.find('h1').getText()
    book['price'] = float(book_rows.find('p', {'class': 'price_color'}).getText()[2:])
    book['available'] = int(book_rows.find('p',
            {'class': 'instock availability'}).getText().split('(', 1)[1].split(' ')[0])
    try:
        book['description'] = book_rows.find('p', {'class': ''}).getText()
    except:
        book['description'] = 'None'

    books.append(book)


while True:
    response = session.get(url + f"/catalogue/page-{page}.html", headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.find_all('li', {'class': 'col-xs-6'})
    if not rows:
        break

    for row in rows:
        href = row.find('h3').find('a').get('href')
        book_info(href)
    print(f'Обработка {page} страницы')
    page += 1

books_json = json.dumps(books, indent=4)
with open("dz2.json", "w") as outfile:
    outfile.write(books_json)



