from typing import List
import pandas as pd
import csv
import codecs
import operator
import time

def readFile(fileName):
    """[csvファイルからデータを取得してリストを返す]

    Args:
        fileName ([String]): [ファイル名]

    Returns:
        [list]: [各チームのデータ]
    """
    with codecs.open(fileName, "r", "Shift-JIS", "ignore") as file:
        df = pd.read_table(file, delimiter=",")

    return df.values.tolist()

def calculateALL(T,W,dataList):
    """[全ての重みパターンで計算し、一番実際の順位に近いおもみリストを返す]

    Args:
        T ([String,int]): [チーム名,チームの評価点]
        W ([list]): [おもみリスト]
        dataList ([list]): [各チームのスタッツデータ]

    Returns:
        [list]: [実際の準備に一番近いおもみリスト]
    """
    bestW = [W,10]

    for a in range(1,6):
        for b in range(1,6):
            for c in range(1,6):
                for d in range(1,6):
                    for e in range(1,6):
                        for f in range(1,6):
                            for g in range(1,6):
                                for h in range(1,6):
                                        W = [a,b,c,d,e,f,g,h]

                                        arrangeData(T,W,dataList)

                                        score = compareRanking(T)

                                        if bestW[1] < score:
                                            bestW[0] = W
                                            bestW[1] = score

                                        print3rdResult(T)
                                        print()

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

def compareRanking(T):
    score = 0
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


df = None
dataList = None
T = []
W = [5,5,5,5,5,5,5,5]
fileName="2021レギュラーシーズン.csv"

dataList = readFile(fileName)
        
#arrangeData(T,W,dataList)

#printResult(T)

start = time.time()

bestW = calculateALL(T,W,dataList)

end = time.time()

print("Time : ",end-start)