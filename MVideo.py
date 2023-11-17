#Урок 7. Selenium в Python

# Написать программу, которая собирает товары
# «В тренде» с сайта техники mvideo и складывает данные в БД

import pprint
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pymongo import MongoClient


driver = webdriver.Chrome()

driver.get('https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118?from=under_search')
time.sleep(1)

while True:
	wait = WebDriverWait(driver, 20)
	items = wait.until(ec.presence_of_all_elements_located((By.CLASS_NAME, 'product-title__text')))
	count = len(items)
	driver.execute_script("window.scrollBy(0, 2000);")
	time.sleep(2)
	items = driver.find_elements(By.CLASS_NAME, 'product-cards-layout__item')

	if len(items) == count:
		break

def notebooks(name:str,price:str,url:str):
	notebook = {'name': name, 'price': int (''.join(filter(str.isdigit, price))), 'url': url}
	return notebook

mvideo_notebooks =[]
for item in items:
	name = item.find_element(By.CLASS_NAME, 'product-title__text').text
	price = item.find_element(By.CLASS_NAME, 'price__main-value').text
	url = item.find_element(By.CLASS_NAME, 'product-picture-link').get_attribute('href')

	mvideo_notebooks.append(notebooks(name,price,url))


client = MongoClient("localhost", 27017)
mongo_db = client["MVideo"]
mvideo = mongo_db.mvideo


mvideo.insert_many(mvideo_notebooks, ordered=False)
