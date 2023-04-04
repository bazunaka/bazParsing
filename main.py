import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    h3 = soup.find(
        'div',
        {"class": "td-post-content tagdiv-type"}
    ).find('h3').text
    return h3


def get_multiple_data(html):
    soup = BeautifulSoup(html, "lxml")
    h3 = soup.findAll('h3')[3]
    h3_text = h3.findAllNext('a')
    return h3_text


def main():
    url = 'https://pumpmuscles.ru/bodibilding/anatomiya-myishts-cheloveka-bodibildera.html#Трапеции'
    print(get_multiple_data(get_html(url)))


if __name__ == '__main__':
    main()
