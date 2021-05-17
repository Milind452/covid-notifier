import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    print('__Start')
    url = 'https://www.github.com'
    page = requests.get(url).content
    soup = BeautifulSoup(page, 'html.parser')
    print(soup.title)
    print('__End')