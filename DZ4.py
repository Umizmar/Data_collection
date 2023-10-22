import requests
from lxml import html
import csv

# Урок 4. Парсинг HTML. XPath
# Написать приложение, которое собирает основные новости с сайта news.mail.ru
# Для парсинга использовать XPath. Структура данных должна содержать:
# * название источника;
# * наименование новости;
# * ссылку на новость;
# * дата публикации.
#
# Сохраните извлеченные данные в CSV-файл с помощью модуля csv.
#
# Ваш код должен включать следующее:
#
# Строку агента пользователя в заголовке HTTP-запроса,
# чтобы имитировать веб-браузер и избежать блокировки сервером.
# Выражения XPath для выбора элементов данных таблицы и извлечения их содержимого.
# Обработка ошибок для случаев, когда данные не имеют ожидаемого формата.
# Комментарии для объяснения цели и логики кода.
#
# Примечание: Пожалуйста, не забывайте соблюдать этические и юридические нормы при веб-скреппинге.

url = "https://news.mail.ru/"
headers = {"User-Agent":
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
            'AppleWebKit/537.36 (KHTML, like Gecko)'
            'Chrome/117.0.0.0 Safari/537.36'}

responce = requests.get(url=url, headers=headers)                  #запрос на сайт
                                                                       # и
dom = html.fromstring(responce.text)                                # создание xpath

news_list =[]

def data_info(link):                                                      #достаем информацию
    responce = requests.get(url=link)                                   #из конкретной  новости
    dom_ = html.fromstring(responce.text)
    try:
        source = dom_.xpath("//span[@class='link__text']/text()")[0]     #источник
    except:
        source='None'
    try:
        name = str(*dom_.xpath("//h1/text()"))                          #название
    except:
        name='None'
    try:
        date = str(*dom_.xpath("//span//@datetime"))                    #дату создания
    except:
        date='None'

    news_list.append(f' Новость: {name}')                            #добавляем в список
    news_list.append(f' Источник: {source}')                            #для последующей записи в CSV файл
    news_list.append(f' Дата создания: {date}')

    return news_list

news = dom.xpath("//ul[@data-module='TrackBlocks']//@href")   #достаем конкретную ссылку на новость

for link in news:
    news_list.append(f'Ссылка: {link}')

    data_info(link)                                           #функция добавления Новости, Источника и Даты

with open('dz4.csv', 'a', newline = '') as f:                 #запись в CSV файл
    writer = csv.writer(f, delimiter=(';'))
    [writer.writerow(news_list[i : i + 4]) for i in range(0, len(news_list), 4)]

