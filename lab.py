from typing import List
import pandas as pd
import csv
import codecs
import operator
import time
import os
import math

def readStatsFile(fileName):
    """[csvファイルからスタッツデータを取得してスタッツリストを返す]

    Args:
        fileName ([String]): [ファイル名]

    Returns:
        [list]: [各チームのデータ]
    """
    with codecs.open(fileName, "r", "Shift-JIS", "ignore") as file:
        df = pd.read_table(file, delimiter=",")

    return df.values.tolist()

def readRankFile(fileName):
    """[csvファイルから順位データを取得して順位リストを返す]

    Args:
        fileName ([String]): [ファイル名]

    Returns:
        [list]: [各チームのデータ]
    """
    with codecs.open(fileName, "r", "Shift-JIS", "ignore") as file:
        df = pd.read_table(file, delimiter=",")

    return df.values.tolist()

def calculateALL(T,dataList,rankList):
    """[全ての重みパターンで計算し、一番実際の順位に近いおもみリストを返す]

    Args:
        T ([String,int]): [チーム名,チームの評価点]
        W ([list]): [おもみリスト]
        dataList ([list]): [各チームのスタッツデータ]

    Returns:
        [list]: [実際の準備に一番近いおもみリスト]
    """
    omomi = 6
    bestW = [None,10000]

    #5^8通りの重みで試算
    for a in range(1,omomi):
        for b in range(1,omomi):
            for c in range(1,omomi):
                for d in range(1,omomi):
                    for e in range(1,omomi):
                        for f in range(1,omomi):
                            for g in range(1,omomi):
                                for h in range(1,omomi):
                                        W = [a,b,c,d,e,f,g,h]

                                        #Tを作成
                                        arrangeData(T,W,dataList)

                                        #3位までの評価点数結果を出力
                                        #print3rdResult(T)
                                        #print()

                                        #Tと実際の順位を比較しスコアを計算(scoreが小さいほど順位が近い)
                                        score = compareRanking(T,rankList)

                                        if bestW[1] > score:
                                            bestW[0] = W
                                            bestW[1] = score

                                        T = []

    return bestW

def calculateALLByDaviation(T,dataList,rankList):
    """[全ての重みパターンで計算し、一番実際の順位に近いおもみリストを返す]

    Args:
        T ([String,int]): [チーム名,チームの評価点]
        W ([list]): [おもみリスト]
        dataList ([list]): [各チームのスタッツデータ]

    Returns:
        [list]: [実際の準備に一番近いおもみリスト]
    """
    omomi = 6
    bestW = [None,10000]

    #5^8通りの重みで試算
    for a in range(1,omomi):
        for b in range(1,omomi):
            for c in range(1,omomi):
                for d in range(1,omomi):
                    for e in range(1,omomi):
                        for f in range(1,omomi):
                            for g in range(1,omomi):
                                for h in range(1,omomi):
                                        W = [a,b,c,d,e,f,g,h]

                                        #Tを作成
                                        arrangeDataByDaviation(T,W,dataList)

                                        #3位までの評価点数結果を出力
                                        print3rdResult(T)
                                        print()

                                        #Tと実際の順位を比較しスコアを計算(scoreが小さいほど順位が近い)
                                        score = compareRanking(T,rankList)

                                        if bestW[1] > score:
                                            bestW[0] = W
                                            bestW[1] = score

                                        T = []

    return bestW


def arrangeData(T,W,dataList):
    """[評価点リスト[T]を作り上げる]

    Args:
        T ([String,int]): [チーム名,各チームの総合評価点]
        W ([int]): [重みリスト]
        dataList ([int]): [各チームスタッツの順位]
    """
    for i in range(1,9):
        dataList = sorted(dataList, key=operator.itemgetter(i))

        for idx,elm in enumerate(dataList):
            elm[i] = idx+1


    for i in range(30):
        element = ["team",0]
        element[0] = dataList[i][0]
        for j in range(1,9):
            element[1] += W[j-1]*dataList[i][j]
        T.append(element)

def arrangeDataByDaviation(T,W,dataList):
    """[評価点リスト[T]を作り上げる]

    Args:
        T ([String,int]): [チーム名,各チームの総合評価点]
        W ([int]): [重みリスト]
        dataList ([int]): [各チームスタッツの順位]
    """

    for i in range(30):
        element = ["team",0]
        element[0] = dataList[i][0]
        for j in range(1,9):
            element[1] += W[j-1]*dataList[i][j]
        T.append(element)

def toDeviationValue(statsDataList):

    teamDataNum = 30
    averageStats = [0,0,0,0,0,0,0,0]
    standardDeviations = [0,0,0,0,0,0,0,0]

    #各スタッツの平均値(averageStats)を算出
    for statsElm,aveStat in enumerate(averageStats):
        for teamNum in range(teamDataNum):
            aveStat += statsDataList[teamNum][statsElm+1]

        aveStat /= teamDataNum
        averageStats[statsElm] = aveStat

    #各スタッツの標準偏差(standardDeviation)
    for statsElm,standardDeviation in enumerate(standardDeviations):
        for teamNum in range(teamDataNum):
            standardDeviation += (statsDataList[teamNum][statsElm+1] - averageStats[statsElm])**2

        standardDeviation/=float(teamDataNum)
        standardDeviation = math.sqrt(standardDeviation)

        standardDeviations[statsElm] = standardDeviation


    #statsDataList内のデータを偏差値に変換
    for stat in statsDataList:
        for elmNum in range(1,9):
            try:
                stat[elmNum] = (10*(stat[elmNum] - averageStats[elmNum-1]))/standardDeviations[elmNum-1] + 50
            except Exception:
                print("偏差値計算におけるエラー")
                exit()

    return statsDataList

def compareRanking(T,rankList):
    """[実際の順位と比較してスコアを算出する]

    Args:
        T ([String,int]): [チーム名,チームの評価点]
        rankList ([int]): [実際の順位リスト]

    Returns:
        [int]: [スコア]
    """
    #0からスタート、１チームごとの順位の離れ方で計算
    score = 0

    for i,elm in enumerate(sorted(T,key=operator.itemgetter(1),reverse=True)):
        for rank in rankList:
            if elm[0] == rank[0]:
                score += abs(i-rank[2])

    return score

def printResult(T):
    """[データからの全順位を出力]

    Args:
        T ([String,int]): [チーム名,各チームの評価点]
    """
    for i,elm in enumerate(sorted(T,key=operator.itemgetter(1),reverse=True)):
        print(i+1,"位",elm[0],":",elm[1],"点")

def print3rdResult(T):
    """[3位までの結果を出力]

    Args:
        T ([String]): [チーム名,チームの評価点]
    """
    by3rd = sorted(T,key=operator.itemgetter(1),reverse=True)
    by3rd = by3rd[0:3]

    for i,elm in enumerate(by3rd):
        print(i+1,"位",elm[0],":",elm[1],"点",flush=True)

def printW(W):
    """[スタッツを見やすく出力する]

    Args:
        W ([list]): [出力するリスト]
    """
    print("FG%",W[0])
    print("3P%",W[1])
    print("FT%",W[2])
    print("ORB",W[3])
    print("DRB",W[4])
    print("APG",W[5])
    print("SPG",W[6])
    print("BPG",W[7])


df = None
dataList = None
T = []
stats_file = "./dataFile/2021/2021レギュラーシーズンスタッツ.csv"
rank_file = "./dataFile/2021/2021レギュラーシーズン順位.csv"

#データ読み込み
statsDataList = readStatsFile(stats_file)
rankDataList = readRankFile(rank_file)

#スタッツデータを偏差値に変換
statsDataList = toDeviationValue(statsDataList)

#試算開始
start = time.time()

#順位表を使った試算
#bestW = calculateALL(T,statsDataList,rankDataList)

#偏差値を使った試算
bestW = calculateALLByDaviation(T,statsDataList,rankDataList)


end = time.time()

print("Time : ",end-start)

#最良のWを使って順位を算出
T = []

#順位の場合
#arrangeData(T,bestW[0],statsDataList)

#偏差値の場合
arrangeDataByDaviation(T,bestW[0],statsDataList)

#最良順位出力
printResult(T)

#重み出力
printW(bestW[0])

#ポイント出力
print("points:",bestW[1])
