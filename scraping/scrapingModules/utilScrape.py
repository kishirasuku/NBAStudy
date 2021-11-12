from bs4 import BeautifulSoup
from urllib.request import urlopen

def takeSoup(year):
    html = urlopen("https://www.basketball-reference.com/leagues/NBA_"+year+".html")
    soup = BeautifulSoup(html, "html.parser")

    return soup

def parseData(trs,pop_lst):
    returnData = []

    for tr in trs:
        csv_data = []

        # 1行ごとにtd, tr要素のデータを取得してCSVに書き込み
        for cell in tr.findAll(['td', 'th']):
            csv_data.append(cell.get_text())

        for i in sorted(pop_lst,reverse=True):
            csv_data.pop(i)

        returnData.append(csv_data)

    return returnData
