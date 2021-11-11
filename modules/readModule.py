import codecs
import pandas as pd

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
