import requests
from bs4 import BeautifulSoup


def getSoupObject(url):
    return BeautifulSoup(requests.get(url).content, 'html.parser')

if __name__ == '__main__':
    print('__Start')
    url = 'https://www.github.com'
    soup = getSoupObject(url)
    print(soup.title)
    print('__End')