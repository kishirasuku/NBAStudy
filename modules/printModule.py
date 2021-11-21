import operator

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

def printScore(W,teamNum):

    print("総合ポイント:",W[1])
    print("1チーム当たりの平均誤差",W[1]/teamNum)

def printTop10WAverage(top10W):
    averageW = [0,0,0,0,0,0,0,0]

    for wPlusScore in top10W:
        for i in range(8):
            averageW[i] += wPlusScore[0][i]

    for i in range(8):
        averageW[i] = averageW[i]/10.0

    print("---------------TOP10の重み平均値--------------------")
    print("平均FG%",averageW[0])
    print("平均3P%",averageW[1])
    print("平均FT%",averageW[2])
    print("平均ORB",averageW[3])
    print("平均DRB",averageW[4])
    print("平均APG",averageW[5])
    print("平均SPG",averageW[6])
    print("平均BPG",averageW[7])

    averageScore = 0

    for w in top10W:
        averageScore += w[1]

    print("TOP10の平均スコア:",averageScore/10.0)