import requests
from bs4 import BeautifulSoup


def getSoupObject(url):
    return BeautifulSoup(requests.get(url).content, 'html.parser')

def getTotalData(soup):
    dataList = soup.find('div', class_ = 'col-xs-8 site-stats-count').findAll('li')
    dataDict = dict()
    for li in dataList:
        tmp = li.text.strip().split()
        dataDict[tmp[0]] = tmp[1]
    vaccineData = soup.find('div', class_ = 'fullbol').text.strip().split()
    dataDict[vaccineData[1]] = "".join(vaccineData[3].split(','))
    return dataDict

def getStateData(soup):
    table = soup.find('table', class_ = 'table table-striped table-bordered').find('tbody')
    stateData = dict()
    for row in table.findAll('tr'):
        data = row.findAll('td')
        if data != []:
            stateData[data[1].text] = {'Total confirmed cases' : data[2].text, 'Active cases' : data[3].text, 'Cured/Discharged' : data[4].text, 'Deaths' : data[5].text}
    return stateData

def formatTotalData(data):
    msg = "Active cases: {0}\nDischarged:   {1}\nDeaths:       {2}\nVaccinations: {3}".format(data['Active'], data['Discharged'], data['Deaths'], data['Vaccination'])
    return msg

if __name__ == '__main__':
    print('__Start')
    totalCovidStatsURL = 'https://www.mohfw.gov.in/'
    stateCovidStatsURL = 'https://prsindia.org/covid-19/cases'
    soup = getSoupObject(totalCovidStatsURL)
    totalData = getTotalData(soup)
    soup = getSoupObject(stateCovidStatsURL)
    stateData = getStateData(soup)
    # print(totalData)
    # print('********************')
    # print(stateData)

    msg_TotalData = formatTotalData(totalData)
    print(msg_TotalData)

    print('__End')