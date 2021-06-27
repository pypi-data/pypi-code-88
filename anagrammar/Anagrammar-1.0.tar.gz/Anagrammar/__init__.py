import random
import math

class AngrammarError(Exception):
    pass

def anagram(Chars):
    BigList = []
    while True:
        CharsList = []
        CharsIndexesStr = ""
        if type(Chars) == list:
            CharsList = Chars
        elif type(Chars) == str:
            for i in Chars:
                CharsList.append(i)
        else:
            AngrammarError("Only str & list are supported")

        CharsLen = len(CharsList)
        while True:
            Index = random.randint(0,CharsLen-1)
            if str(Index) not in CharsIndexesStr:
                CharsIndexesStr += str(Index)
            if len(CharsIndexesStr) == CharsLen:
                break
        TempStr = ""
        for i in CharsIndexesStr:
            TempStr += CharsList[int(i)]
        if TempStr not in BigList:
            BigList.append(TempStr)
        if len(BigList) == math.factorial(len(CharsList)):
            break
    BigList.sort()
    return BigList
