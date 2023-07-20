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
        #span_list = main_a.find_all('span', attrs={'class': 'styles__BulkFloor-j8px38-3 haaSuT'})
        span_list = main_a.find_all('div', attrs={'class': r'[styles__\*]'})
        for i in range(3):
            print(span_list[i].get_text())



def get_workouts(html):
    soup = BeautifulSoup(html, "lxml")
    div = soup.find(
        'div',
        {"class": "ui two stackable cards"}
    )
    a = div.findAll(
        'div',
        {"class": "content"}
    )
    for aq in a:
        name = aq.find_next('a').text
        print(name)


def get_multiple_data(html):
    soup = BeautifulSoup(html, "lxml")
    h3 = soup.findAll('li')
    # h3_text = h3.findAllNext('li')
    return dir(h3)


def main():
    url = 'https://www.pik.ru/search/bd'
    print(get_data(url))


if __name__ == '__main__':
    main()
