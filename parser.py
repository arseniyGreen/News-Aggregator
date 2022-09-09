from bs4 import BeautifulSoup
import requests
import sqlite3

headers = {
        'user agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/103.0.5060.134 Safari/537.36"}

# Get all news from ria.ru and return then as a dictionary [title:link]
def parse():

    news_dict = {}

    url = 'https://ria.ru'
    html = requests.get(url, headers)

    soup = BeautifulSoup(html.text, 'html.parser')

    for span in soup.find_all('span', {'class' : 'cell-list__item-title'}):
        #print(span.text)
        #print(span.parent.parent.get('href'),'\n')

        news_dict[span.text] = span.parent.parent.get('href')

    return news_dict

