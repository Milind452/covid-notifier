import requests
from bs4 import BeautifulSoup


def getSoupObject(url):
    return BeautifulSoup(requests.get(url).content, 'html.parser')

def getGeneralData(soup):
    dataList = soup.find('div', class_ = 'col-xs-8 site-stats-count').findAll('li')
    dataDict = dict()
    for li in dataList:
        tmp = li.text.strip().split()
        dataDict[tmp[0]] = tmp[1]
    vaccineData = soup.find('div', class_ = 'fullbol').text.strip().split()
    dataDict[vaccineData[1]] = "".join(vaccineData[3].split(','))
    print(dataDict)

if __name__ == '__main__':
    print('__Start')
    url = 'https://www.mohfw.gov.in/'
    soup = getSoupObject(url)
    getGeneralData(soup)
    print('__End')