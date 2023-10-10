# Урок 1. Основы клиент-серверного взаимодействия. Парсинг API
# Данные с ozon.ru

import requests

url = ("https://api-seller.ozon.ru/v1/description-category/tree")

headers = {'Client-Id': '', 'Api-Key': ''}

resp = requests.post(url, headers=headers).json()

catalog = []
for categories in resp.get('result'):
    catalog.append(categories.get("category_name"))

print('\n'.join(catalog))
print()
user_select = input('Выберите категорию из списка сверху - ')

user_cat = []
if user_select in catalog:
    for select_categories in resp.get('result'):
        if select_categories.get("category_name") == user_select:
            for cat_list in select_categories.get('children'):
                user_cat.append(cat_list.get("category_name"))
else:
    print()
    print('Такого товара нет')

print()
print('\n'.join(user_cat))