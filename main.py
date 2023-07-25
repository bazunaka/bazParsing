import requests
from bs4 import BeautifulSoup

import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}


def get_html(url):
    r = requests.get(url, headers=headers)
    return r


def get_data(html):
    time.sleep(10)
    if get_html(html).status_code == 200:
        soup = BeautifulSoup(get_html(html).content, 'html.parser')
        main_a = soup.find('div', attrs={'class': '_9330de7794--cards--pA5SE'})
        div_list = main_a.find_all('div', attrs={'data-name': 'ResidentialComplexCardWrapper'})
        for i in range(len(div_list)):
            print(div_list[i].get_text())
        print(div_list)


def get_classes(html):
    classes = []
    if get_html(html).status_code == 200:
        soup = BeautifulSoup(get_html(html).content, 'html.parser')
        for element in soup.find_all('div', class_=True):
            classes.extend(element["class"])
        for i in range(len(classes)-1):
            classes[i].s
    print(classes)


def main():
    url = 'https://www.cian.ru/zastroishchik-pik-9/?apartmentsWithDecoration=true&minPrice=3500000&maxPrice=5350000&deadline=2024#projects'
    print(get_data(url))
    # get_classes(url)


if __name__ == '__main__':
    main()
