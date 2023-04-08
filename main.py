import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    ul = soup.find(
        'ul',
        {"class": "ez-toc-list ez-toc-list-level-1"}
    )
    li = ul.find_all('li')

    for a in li:
        name = a.find_next('a').text
        print(name)


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
    # url = 'https://pumpmuscles.ru/bodibilding/anatomiya-myishts-cheloveka-bodibildera.html#Трапеции'
    # print(get_multiple_data(get_html(url)))
    # url = 'https://dailyfit.ru/katalog-uprazhnenij/?tax_celevye_myshcy%5B%5D=44&tax_vid_uprazhnenija%5B%5D=18' грудь
    url = 'https://dailyfit.ru/katalog-uprazhnenij/?tax_celevye_myshcy%5B%5D=31&tax_vid_uprazhnenija%5B%5D=18'
    print(get_workouts(get_html(url)))


if __name__ == '__main__':
    main()
