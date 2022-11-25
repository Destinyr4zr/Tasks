from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

HEADERS = {
    'User-Agent': 'insert_agent',
    'Accept': '*/*',
    'Accept-encoding': 'gzip, deflate, br',
    'Accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
    }


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    r.encoding = 'utf-8'
    return r


def get_data_from_labirint():
    URL = "some_url"

    html = get_html(URL)

    soup = BeautifulSoup(html.text, 'html.parser')

    items = soup.find_all('div', class_='products-row-outer responsive-cards')
    items = items[2]
    items = items.find_all('div', class_='card-column card-column_gutter col-xs-6 col-sm-3 col-md-1-5 col-xl-2')

    books = []

    for item in items:
        old_price = item.find('span', class_='price-old')
        if old_price:
            old_price = int(''.join(re.findall(r'\d+', old_price.get_text())))
        else:
            old_price = 'No data'

        authors = item.find('div', class_='product-author')
        if authors:
            authors = authors.find_all('a')
            authors = [x.get('title') for x in authors]
            authors = ', '.join(authors)
        else:
            authors = 'No data'

        try:
            books.append({
                'Название': item.find('span', class_='product-title').get_text(),
                'Автор': authors,
                'Цена сейчас': int(''.join(re.findall(r'\d+',item.find('span', class_='price-val').get_text()))),
                'Цена раньше': old_price,
                'Жанр': item.find('div', class_='product need-watch').get('data-first-genre-name'),
                'Раздел': item.find('div', class_='product need-watch').get('data-maingenre-name'),
                'Ссылка на книгу': URL + item.find('a', class_='cover').get('href'),
                'Магазин': 'Лабиринт'
            })

        except:
            continue

    books = pd.DataFrame(books)
    books['Скидка %'] = 0
    mask = books['Цена раньше'] != 'No data'
    books.loc[mask, 'Скидка %'] = (1 - (books.loc[mask, 'Цена сейчас'] / books.loc[mask, 'Цена раньше'])) * 100
    books['Скидка %'] = books['Скидка %'].astype(int)
    books = books[['Название', 'Автор', 'Цена сейчас', 'Цена раньше', 'Скидка %', 'Жанр', 'Раздел', 'Ссылка на продукт', 'Магазин']]

    return books


def get_data_from_chitai_gorod():
    URL = "some_other_url"

    html = get_html(URL)
    soup = BeautifulSoup(html.text, 'html.parser')
    sections = soup.find_all('div', class_='best-sales__block best-sales__block_14')

    books = []

    for section in sections:
        items = section.find_all('div', class_='product-card js_product js__product_card js__slider_item')

        for item in items:
            author = item.find('div', class_='product-card__author').get_text().replace('\t', '')
            author = author.replace('\n', '')
            old_price = item.find('span', class_='old-price')
            if old_price:
                old_price = int(''.join(re.findall(r'\d+', old_price.get_text())))
            else:
                old_price = 'No data'

            try:
                books.append({
                    'Название': item.get('data-chg-book-name'),
                    'Автор': author,
                    'Цена сейчас': int(''.join(re.findall(r'\d+',item.find('span',class_='product-price__value').get_text()))),
                    'Цена раньше': old_price,
                    'Раздел': section.find('div', class_='best-sales__block__title').get_text(),
                    'Ссылка на продукт': URL + item.find('a',class_='product-card__img js-analytic-productlink').get('href'),
                    'Магазин': 'Читай город'
                })

            except:
                continue

    books = pd.DataFrame(books)
    books['Скидка %'] = 0
    mask = books['Цена раньше'] != 'No data'
    books.loc[mask, 'Скидка %'] = (1 - (books.loc[mask, 'Цена сейчас'] / books.loc[mask, 'Цена раньше'])) * 100
    books['Скидка %'] = books['Скидка %'].astype(int)
    books = books[['Название', 'Автор', 'Цена сейчас', 'Цена раньше', 'Скидка %', 'Раздел', 'Ссылка на продукт', 'Магазин']]

    return books


def merge_products(products_1, products_2):
    return pd.concat([products_1, products_2], ignore_index=True)


if __name__ == '__main__':
    products_1 = get_data_from_labirint()

    products_2 = get_data_from_chitai_gorod()

    all_books = merge_products(products_1, products_2)

    products_1.to_csv('name1.csv', index=False)
    products_2.to_csv('name2.csv', index=False)
    all_books.to_csv('whole_proj.csv', index=False)
