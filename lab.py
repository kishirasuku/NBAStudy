from typing import List
import pandas as pd
import csv
import codecs
import operator
import time

def readFile(fileName):
    with codecs.open(fileName, "r", "Shift-JIS", "ignore") as file:
        df = pd.read_table(file, delimiter=",")

    return df.values.tolist()

def calculateALL(T,W,dataList):
    for a in range(1,11):
        for b in range(1,11):
            for c in range(1,11):
                for d in range(1,11):
                    for e in range(1,11):
                        for f in range(1,11):
                            for g in range(1,11):
                                for h in range(1,11):
                                        W = [a,b,c,d,e,f,g,h]

                                        arrangeData(T,W,dataList)

                                        print3rdResult(T)
                                        print()

                                        T = []


def arrangeData(T,W,dataList):
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

def printResult(T):
    for i,elm in enumerate(sorted(T,key=operator.itemgetter(1),reverse=True)):
        print(i+1,"位",elm[0],":",elm[1],"点")

def print3rdResult(T):
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

calculateALL(T,W,dataList)

end = time.time()

print("Time : ",end-start)