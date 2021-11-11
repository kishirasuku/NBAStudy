from typing import List
import pandas as pd
import csv
import codecs
import operator
import time
import os
import math
from modules.readModule import readStatsFile,readRankFile
from modules.printModule import print3rdResult,printResult,printScore,printW
from modules.arrangeDataModule import arrangeData,arrangeDataByDaviation

def calculateALL(dataList,rankList,maxWeight):
    """[全ての重みパターンで計算し、一番実際の順位に近いおもみリストを返す]

    Args:
        T ([String,int]): [チーム名,チームの評価点]
        W ([list]): [おもみリスト]
        dataList ([list]): [各チームのスタッツデータ]

    Returns:
        [list]: [実際の準備に一番近いおもみリスト]
    """
    T = []
    omomi = maxWeight + 1
    bestW = [None,10000]
    
    under35 = 0
    Waverage = [0,0,0,0,0,0,0,0]

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

                                        if score/30 <= 3.5:
                                            under35 += 1
                                            for i,wElm in enumerate(W):
                                                Waverage[i] += wElm

                                        if bestW[1] > score:
                                            bestW[0] = W
                                            bestW[1] = score

                                        T = []
    
    for i in range(len(Waverage)):
        Waverage[i] /= under35

    print("平均誤差が3.5以下の数:",under35)
    return bestW,Waverage

def calculateALLByDaviation(dataList,rankList,maxWeight):
    """[全ての重みパターンで計算し、一番実際の順位に近いおもみリストを返す]

    Args:
        T ([String,int]): [チーム名,チームの評価点]
        W ([list]): [おもみリスト]
        dataList ([list]): [各チームのスタッツデータ]

    Returns:
        [list]: [実際の準備に一番近いおもみリスト]
    """

    T=[]
    omomi = maxWeight+1
    bestW = [None,10000]

    under35 = 0
    Waverage = [0,0,0,0,0,0,0,0]

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
                                        #print3rdResult(T)
                                        #print()

                                        #Tと実際の順位を比較しスコアを計算(scoreが小さいほど順位が近い)
                                        score = compareRanking(T,rankList)

                                        if score/30 <= 3.5:
                                            under35 += 1
                                            for i,wElm in enumerate(W):
                                                Waverage[i] += wElm

                                        if bestW[1] > score:
                                            bestW[0] = W
                                            bestW[1] = score

                                        T = []


    for i in range(len(Waverage)):
        Waverage[i] /= under35

    print("平均誤差が3.5以下の数:",under35)
    return bestW,Waverage

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
                if abs(i-rank[2]) >= 15:
                    score += 100
                score += abs(i-rank[2])

    return score

def doByStats(stats_file,rank_file,maxWeight):

    print("スタッツ順位による計算を開始")
    print("使用データ年度 :",stats_file[11:15])
    print("重み最大値 : ",maxWeight)

    #データ読み込み
    statsDataList = readStatsFile(stats_file)
    rankDataList = readRankFile(rank_file)

    #試算開始
    start = time.time()

    #順位表を使った試算
    bestW,Waverage = calculateALL(statsDataList,rankDataList,maxWeight)

    end = time.time()

    print("Time : ",end-start)

    #最良のWを使って順位を算出
    T = []

    #順位の場合
    arrangeData(T,bestW[0],statsDataList)
    
    print("--------------------最良順位データ--------------------")

    #最良順位出力
    printResult(T)

    #重み出力
    printW(bestW[0])

    #ポイント出力
    printScore(bestW)
    
    print("-----------------平均誤差3.5以下の重み平均値-----------------")
    printW(Waverage)

def doByDaviation(stats_file,rank_file,maxWeight):

    print("偏差値による計算を開始")
    print("使用データ年度 :",stats_file[11:15])
    print("重み最大値 : ",maxWeight)

    #データ読み込み
    statsDataList = readStatsFile(stats_file)
    rankDataList = readRankFile(rank_file)

    #スタッツデータを偏差値に変換
    statsDataList = toDeviationValue(statsDataList)

    #試算開始
    start = time.time()

    #偏差値を使った試算
    bestW,Waverage = calculateALLByDaviation(statsDataList,rankDataList,maxWeight)

    end = time.time()

    print("Time : ",end-start)

    #最良のWを使って順位を算出
    T = []

    #偏差値の場合
    arrangeDataByDaviation(T,bestW[0],statsDataList)
    
    print("--------------------最良順位データ--------------------")

    #最良順位出力
    printResult(T)

    #重み出力
    printW(bestW[0])

    #ポイント出力
    printScore(bestW)
    
    print("-----------------平均誤差3.5以下の重み平均値-----------------")
    printW(Waverage)


stats_file = "./dataFile/2021/2021レギュラーシーズンスタッツ.csv"
rank_file = "./dataFile/2021/2021レギュラーシーズン順位.csv"
maxWeight = 5 #重みの最大値

#通常計算の場合
doByStats(stats_file,rank_file,maxWeight)

#偏差値計算の場合
doByDaviation(stats_file,rank_file,maxWeight)