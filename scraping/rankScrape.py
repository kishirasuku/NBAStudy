# -*- coding: utf-8 -*-
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from scrapingModules.utilScrape import *

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

    #EastとWestのデータでcsvファイルに記述する
    csvRankWriterForWestAndEastInfo(East_data,West_data,csv_write)

    #ファイルクローズド
    csv_file.close()

def scrapeAllRankBefore2015(year):
    #beautifulSoupでhtml情報をもってくる
    soup = takeSoup(year)

    tableEast = soup.findAll("table", {"id":"divs_standings_E"})[0]
    trsEast = tableEast.findAll("tr")

    tableWest = soup.findAll("table", {"id":"divs_standings_W"})[0]
    trsWest = tableWest.findAll("tr")

    # ファイルオープン
    csv_file = open("./dataFile/"+year+"/"+year+"レギュラーシーズン順位.csv", 'wt', newline = '', encoding = 'utf-8')
    csv_write = csv.writer(csv_file)

    #いらない要素番号
    pop_lst = [1,2,4,5,6,7]

    #データをリストにして取得
    West_data = parseRankDataBefore2015(trsWest,pop_lst)
    East_data = parseRankDataBefore2015(trsEast,pop_lst)

    #EastとWestのデータでcsvファイルに記述する
    csvRankWriterForWestAndEastInfo(East_data,West_data,csv_write)

    #ファイルクローズド
    csv_file.close()

