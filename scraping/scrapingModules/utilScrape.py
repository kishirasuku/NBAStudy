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

def parseRankDataBefore2015(trs,pop_lst):
    returnData = []

    for tr in trs:
        csv_data = []

        # 1行ごとにtd, tr要素のデータを取得してCSVに書き込み
        for cell in tr.findAll(['td', 'th']):
            csv_data.append(cell.get_text())

        if not "Division" in csv_data[0]:
            for i in sorted(pop_lst,reverse=True):
                csv_data.pop(i)

            returnData.append(csv_data)

    return returnData

def csvRankWriterForWestAndEastInfo(East_data,West_data,csv_write):
    #ヘッダーを除く全カンファレンスデータの作成
    allRankData = East_data[1:] + West_data[1:]

    #strをfloatに変換
    for i,d in enumerate(allRankData):
        allRankData[i][1] =float(d[1])

    #順位計算処理
    for i,data in enumerate(sorted(allRankData,reverse=True,key=lambda x:x[1])):
        data.append(i+1)

    #ヘッダーを追加
    East_data[0].append("win%")
    allRankData.insert(0,East_data[0])

    #csvに記述
    for rank in allRankData:
        csv_write.writerow(rank)
