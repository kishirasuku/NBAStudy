# -*- coding: utf-8 -*-
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from scrapingModules.utilScrape import takeSoup,parseData

def scrapeALLstats(year):
    #beautifulSoupでhtml情報をもってくる
    soup = takeSoup(year)

    table = soup.findAll("table", {"id":"per_game-team"})[0]
    trs = table.findAll("tr")

    # ファイルオープン
    csv_file = open("./dataFile/"+year+"/"+year+"レギュラーシーズンスタッツ.csv", 'wt', newline = '', encoding = 'utf-8')
    csv_write = csv.writer(csv_file)

    #いらない要素番号
    pop_lst = [0,2,3,4,5,7,8,10,11,12,13,14,18,22,23,24]

    #データをリストにして取得
    allStatsData = parseData(trs,pop_lst)

    #ヘッダーを作成
    frame = allStatsData[0]

    #ヘッダーを抜きにしたデータ取得
    allStatsData = allStatsData[1:-1]

    #strをfloatに変換
    for i in range(len(allStatsData)):
        for j in range(1,9):
            if 1 <= j and j <= 3:
                allStatsData[i][j] = round(float(allStatsData[i][j])*100,1)
            else:
                allStatsData[i][j] = float(allStatsData[i][j])

    #ヘッダーを追加
    allStatsData.insert(0,frame)

    #csvに記述
    for data in allStatsData:
        csv_write.writerow(data)

    # ファイルクローズド
    csv_file.close()