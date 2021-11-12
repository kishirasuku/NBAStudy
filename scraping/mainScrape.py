import rankScrape
import statsScrape
import os

year = input("作成するデータの年 : ")
dirname = "./dataFile/" + year

#フォルダがなければ作成する
if not os.path.isdir(dirname):
    os.makedirs(dirname)

#2015年以降は順位のスクレイピングの形式が異なる
if int(year) <= 2015:
    rankScrape.scrapeAllRankBefore2015(year)
else:
    rankScrape.scrapeAllRank(year)

statsScrape.scrapeALLstats(year)