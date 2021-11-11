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

def printScore(W):

    print("総合ポイント:",W[1])
    print("1チーム当たりの平均誤差",W[1]/30)
