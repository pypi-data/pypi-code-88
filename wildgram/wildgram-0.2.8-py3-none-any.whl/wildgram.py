import regex as re
import string
import os
import numpy as np

STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you',
"you(\'?)re", "you(\'?)ve", "you(\'?)ll", "you(\'?)d", 'your', 'yours', 'yourself', 'yourselves',
'he', 'him', 'his', 'himself', 'she', "she(\'?)s", 'her', 'hers', 'herself', 'it',
"it(\'?)s", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those',
'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if',
'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with',
'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after',
'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over',
'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where',
'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other',
'some', 'such', 'only', 'own', 'same', 'so', 'than', 'too', 'very','can', 'just',
'should', "should(\'?)ve", 'now']

punc = "!|\"|\#|\$|\%|\&|\'|\(|\)|\*|\+|\,|\-|\.|\/|\:|\;|\<|\=|\>|\?|\@|\[|\\|\]|\^|\_|\`|\{|\||\}|\~"

TOPICWORDS = [{"token": "no", "tokenType": "negation"},{"token": "negative", "tokenType": "negation"},
{"token": "not", "tokenType": "negation"},{"token": "nor", "tokenType": "negation"},
{"token": "ain(\'?)t", "tokenType": "negation"},{"token": "aren(\'?)t", "tokenType": "negation"},
{"token": "couldn(\'?)t", "tokenType": "negation"},{"token": "didn(\'?)t", "tokenType": "negation"},
{"token": "doesn(\'?)t", "tokenType": "negation"},{"token": "hadn(\'?)t", "tokenType": "negation"},
{"token": "hasn(\'?)t", "tokenType": "negation"},{"token": "haven(\'?)t", "tokenType": "negation"},
{"token": "isn(\'?)t", "tokenType": "negation"},{"token": "mightn(\'?)t", "tokenType": "negation"},
{"token": "mustn(\'?)t", "tokenType": "negation"},{"token": "needn(\'?)t", "tokenType": "negation"},
{"token": "shan(\'?)t", "tokenType": "negation"},{"token": "shouldn(\'?)t", "tokenType": "negation"},
{"token": "wasn(\'?)t", "tokenType": "negation"},{"token": "weren(\'?)t", "tokenType": "negation"},
{"token": "won(\'?)t", "tokenType": "negation"},{"token": "don(\'?)t", "tokenType": "negation"},
{"token": "wouldn(\'?)t", "tokenType": "negation"},{"token": "denies", "tokenType": "negation"},
{"token": "denied", "tokenType": "negation"},{"token": "\d+\.\d+", "tokenType": "numeric", "suffix": "[^\s\d-]+"},
{"token": "\d+", "tokenType": "numeric","suffix": "[^\s\d-]+"},"([A-Za-z]("+punc+")?){1,2}[A-Za-z]",
{"token": "\d+\.\d+", "tokenType": "numeric"},{"token": "\d+", "tokenType": "numeric"},
{"token": "one", "tokenType": "numeric"},{"token": "two", "tokenType": "numeric"},
{"token": "three", "tokenType": "numeric"},{"token": "four", "tokenType": "numeric"},
{"token": "will", "tokenType": "future"}, "reveal", "revealed"]

JOINERWORDS = ["of", "in", "to", "on","than","at"]

def pullOutJoiners(merged, text, joinerwords):
    if len(joinerwords) == 0:
        return []
    ret = []
    joiners = "|".join(["(\s|^)"+stop+"(\s|$)" for stop in joinerwords])
    for i in range(len(merged)):
        match = merged[i]
        start = 0
        end = len(text)
        if not re.search("("+joiners+")", text[match[0]:match[1]]):
            continue
        if i > 0:
            start = merged[i-1][0]
        if i < len(merged)-1:
            end = merged[i+1][1]
        if start != merged[i][0] and end != merged[i][1]:
            ret.append((start,end, 'token'))
    return ret

def pullOutNoise(pattern, text, leftovers):
    matches = [(match.start(), match.end(), "noise") for match in pattern.finditer(text.lower(),overlapped=True)]
    matches = sorted(matches, key=lambda x: (x[0], x[1]))
    prev = 0
    noise = []
    for i in range(len(matches)-1):
        if matches[i][1] < matches[i+1][0]:
            leftovers, noise = checkAndRemoveLeftovers(leftovers,matches[prev][0],matches[i][1],noise,"noise" )
            prev = i+1
    if prev < len(matches):
        leftovers, noise = checkAndRemoveLeftovers(leftovers,matches[prev][0],matches[-1][1],noise,"noise" )
    return noise, leftovers

def pullOutTokens(indexes, type="token"):
    indexes = list(indexes)
    if len(indexes) == 0:
        return []
    indexes = sorted(indexes)
    prev = indexes[0]
    ret = []
    for i in range(len(indexes)-1):
        if indexes[i]+1 != indexes[i+1]:
            ret.append((prev,indexes[i]+1,type))
            prev = indexes[i+1]
    ret.append((prev, indexes[-1]+1,type))

    return ret

def pullOutTopics(topics, text, leftovers, noise):
    ret = []
    punc = [x for x in string.punctuation]
    allindexes = set()
    potentialphrases = []
    for topic in topics:
        token = topic
        tokenType = "token"
        suffix = ""
        suffixType = "token"
        if isinstance(topic, dict):
            token = topic["token"]
            tokenType = topic["tokenType"]
            if "suffix" in topic:
                suffix = topic["suffix"]

        ## find all relevant matches
        for match in re.finditer("(\s|"+"|\\".join(punc)+"|^)"+token+suffix+"(\s|"+"|\\".join(punc)+"\s|$)", text.lower(),overlapped=True):
            topicmatches = re.finditer(token, text[match.start():match.end()].lower())
            allindexes = allindexes.union(range(match.start(), match.end()))
            for top in topicmatches:
                potentialphrases.append((match.start()+ top.start(),match.start()+ top.end(), tokenType))
                if suffix == "":
                    continue
                suffixes = re.finditer(suffix, text[match.start()+top.end():match.end()].lower())
                for suff in suffixes:
                    if suff.start() == suff.end():
                        continue
                    potentialphrases.append((match.start()+ top.end()+suff.start(),match.start()+ top.end()+suff.end(), "token"))

    for potential in potentialphrases:
        leftovers, ret = checkAndRemoveLeftovers(leftovers, potential[0], potential[1], ret, potential[2])

    ## what's left is noise
    allindexes = leftovers.intersection(allindexes)
    noise = pullOutTokens(allindexes, "noise") + noise
    leftovers = leftovers.difference(allindexes)

    return ret, leftovers,noise

def isInLeftovers(leftovers, r):
    return len(leftovers.intersection(set(r))) == len(r)

def checkAndRemoveLeftovers(leftovers, start, end, ret, tokenType):
    r = range(start, end)
    if not isInLeftovers(leftovers, r):
        return leftovers, ret
    ret.append((start, end, tokenType))
    leftovers = leftovers.difference(r)
    return leftovers, ret


def figureOutRegex(stopwords, size=2):
    punc = [x for x in string.punctuation]
    regex = '[\s' + "|\\".join(punc)+ ']{'+ str(size)+',}|\n|[\s' + "|\\".join(punc)+ ']+$'
    stops = "|".join(["(\s|^)"+stop+"(\s|$)" for stop in stopwords])
    if len(stops) != 0:
        regex = stops+'|'+regex
    prog = re.compile("("+regex+")")
    return prog

def filterAndSort(matches, returnNoise):
    ret = {}
    for match in matches:
        if match[0] not in ret:
            ret[match[0]] = {}
        if match[1] not in ret[match[0]]:
            ret[match[0]][match[1]] = match[2]
            continue
        curState = ret[match[0]][match[1]]
        ## this allows non tokens to override tokens if they are duplicates
        if match[2] == "token" and curState != "token":
            continue
        ret[match[0]][match[1]] = match[2]
    res = []
    for key in ret:
        for k in ret[key]:
            if not returnNoise and ret[key][k] == "noise":
                continue
            res.append((key, k, ret[key][k]))

    return sorted(res,key=lambda x: (x[0], x[1]) )

def createRangesFromProg(prog, topics, text, joinerwords,ranges=[],leftover=[]):
    newnoise, leftover = pullOutNoise(prog, text, leftover)
    topics, leftover, newnoise = pullOutTopics(topics, text, leftover, newnoise)
    tokens = pullOutTokens(leftover)
    merged = sorted(tokens + topics + newnoise, key=lambda x: (x[0], x[1]))
    ranges = ranges + pullOutJoiners(merged, text, joinerwords) + tokens + topics + newnoise
    return ranges, leftover

def createToken(start, end, type, text, index):
    return {"startIndex": start, "endIndex":end, "token":text[start:end], "tokenType": type, "index": index}

def wildgram(text, stopwords=STOPWORDS, topicwords=TOPICWORDS, include1gram=True, joinerwords=JOINERWORDS, returnNoise=True, includeParent=False):
    # corner case for inappropriate input
    if not isinstance(text, str):
        raise Exception("What you just gave wildgram isn't a string, mate.")
    if not returnNoise and includeParent:
        raise Exception("Parent is based on noise index, you need to set returnNoise to True in order to have includeParent be True. Otherwise set both to False.")

    prog = figureOutRegex(stopwords)
    ranges = []
    leftover = set(range(len(text))) # what characters haven't been marked previously
    ranges, leftover = createRangesFromProg(prog, topicwords, text, joinerwords,ranges, leftover)
    if include1gram:
        prog1gram = figureOutRegex(stopwords, 1)
        ranges, leftover = createRangesFromProg(prog1gram, [], text, joinerwords,ranges, leftover)

    ranges =filterAndSort(ranges, returnNoise)
    ret = []
    for r in ranges:
        app = createToken(r[0], r[1], r[2], text,len(ret))
        ret.append(app)

    return ret
