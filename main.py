import requests
from bs4 import BeautifulSoup

import argparse


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
            stateData[data[1].text] = {'total' : data[2].text, 'active' : data[3].text, 'cured' : data[4].text, 'deaths' : data[5].text}
    return stateData

def formatTotalData(data):
    msg = "Active cases: {0}\nDischarged:   {1}\nDeaths:       {2}\nVaccinations: {3}".format(data['Active'], data['Discharged'], data['Deaths'], data['Vaccination'])
    return msg

def formatStateData(data):
    msg = ""
    msg += "{:=<95}\n".format('=')
    msg += "{:^40}{:>15}{:>16}{:>12}{:>12}\n".format('State', 'Confirmed Cases', 'Active Cases', 'Cured', 'Deaths')
    msg += "{:=<95}\n".format('=')
    for state in data:
        tmp = "{:<40}{:>15}{:>16}{:>12}{:>12}\n".format(state, data[state]['total'], data[state]['active'], data[state]['cured'], data[state]['deaths'])
        msg += tmp
        if(state != 'West Bengal'):
            msg += "{:-<95}\n".format('-')
    msg += "{:=<95}".format('=')
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
    # print(msg_TotalData)
    msg_StateData = formatStateData(stateData)
    # print(msg_StateData)

    parser = argparse.ArgumentParser(description= 'Enter twilio credentials to send message')
    parser.add_argument('sid', help= 'Twilio account sid')
    parser.add_argument('auth', help= 'Twilio account auth_token')
    parser.add_argument('numbers', nargs='*', help= 'Receiving phone numbers')
    args = parser.parse_args()
    # print(args.auth, args.sid, args.numbers, sep='\n')

    print('__End')