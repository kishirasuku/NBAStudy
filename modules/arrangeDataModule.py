import operator

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


    for i in range(len(dataList)):
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

    for i in range(len(dataList)):
        element = ["team",0]
        element[0] = dataList[i][0]
        for j in range(1,9):
            element[1] += W[j-1]*dataList[i][j]
        T.append(element)
