# -*- coding: utf-8 -*-
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from scrapingModules.utilScrape import takeSoup,parseData

def scrapeAllRank(year):
    #beautifulSoupでhtml情報をもってくる
    soup = takeSoup(year)

    tableEast = soup.findAll("table", {"id":"confs_standings_E"})[0]
    trsEast = tableEast.findAll("tr")

    tableWest = soup.findAll("table", {"id":"confs_standings_W"})[0]
    trsWest = tableWest.findAll("tr")

    # ファイルオープン
    csv_file = open("./dataFile/"+year+"/"+year+"レギュラーシーズン順位.csv", 'wt', newline = '', encoding = 'utf-8')
    csv_write = csv.writer(csv_file)

    #いらない要素番号
    pop_lst = [1,2,4,5,6,7]

    #データをリストにして取得
    West_data = parseData(trsWest,pop_lst)
    East_data = parseData(trsEast,pop_lst)

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


    #ファイルクローズド
    csv_file.close()