import rankScrape
import statsScrape
import os

year = input("作成するデータの年 : ")
dirname = "./dataFile/" + year

if not os.path.isdir(dirname):
    os.makedirs(dirname)

rankScrape.scrapeAllRank(year)
statsScrape.scrapeALLstats(year)