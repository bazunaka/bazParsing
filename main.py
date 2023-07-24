import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}


def get_html(url):
    r = requests.get(url, headers=headers)
    return r


def get_data(html):
    if get_html(html).status_code == 200:
        soup = BeautifulSoup(get_html(html).content, 'html.parser')
        main_a = soup.find('a', id='listing_flat')
        # span_list = main_a.find_all('span', attrs={'class': 'styles__BulkFloor-j8px38-3 haaSuT'})
        # span_list = main_a.find_all('div', attrs={'class': r'\bs\w+.*'})
        # for i in range(1):
        #    print(span_list[i].get_text())
        span_list = main_a.find_all('span')
        div_list = main_a.find_all('div')
        for i in range(len(span_list) - 1):
            print(span_list[i].get_text())
        for k in range(len(div_list) - 1):
            print(div_list[k].get_text())
        # print(div_list)


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
    url = 'https://www.pik.ru/search/bd'
    #print(get_data(url))
    get_classes(url)


if __name__ == '__main__':
    main()
