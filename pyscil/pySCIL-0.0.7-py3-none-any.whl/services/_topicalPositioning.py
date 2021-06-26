#Import Json elements to encode Python data structures
import json
#Import functions to deal with text
import re, string, unicodedata
#Import nartural language processing functions
import nltk
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize, sent_tokenize
#Import mathematical functions
import numpy as np

#Import pathlib
from pathlib import Path

import pickle

def get_wordnet_pos(word):
    #Map POS tag to first character lemmatize() accepts
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)

#Remove punctuation from list of tokenized words
def removeAscii(words):
    return [re.sub(r'[^\w\s]','',word) for word in words if word != ""]

# get cited polarity based on the maximum of multiple cited polarities
def getCitedPolarity(citedPolarities):
    citedPolarity = ""
    positiveCount = 0
    negativeCount = 0
    neutralCount = 0
    
    for p in citedPolarities:
        if p == "positive" or p == "":
            positiveCount += 1
        elif p == "negative":
            negativeCount += 1
        elif p == "neutral":
            neutralCount += 1
    if positiveCount >= negativeCount and positiveCount >= neutralCount:
        citedPolarity = "positive"
    elif negativeCount > positiveCount and negativeCount > neutralCount:
        citedPolarity = "negative"
    else:
        citedPolarity = "neutral"
    return citedPolarity

# get polarity based on ANEW
def getPolarity(text, topic, anew, lemmatizer):
    polarity = ""

    # separate the text into separate words
    words = text.lower().replace(" '","'").split(" ")
    words = list(filter(None,removeAscii(words)))

    # find indices where the topic appears in the turn
    npWords = np.array(words)
    indices = np.flatnonzero(np.core.defchararray.find(npWords,topic)!=-1)

    reverse_polarity = False
    negative = []
    positive = []
    visited = [] # keep track of visited indices
    # get 10 word wind for each index
    for index in indices:
        # get window of (maximum) 10 words around the target topic
        turnlen = len(words)
        before = list(range(max(0,index-5), index))
        after = list(range(index+1,min(turnlen,index+6)))
        window = [(word,index) for word,index in zip(words[max(0,index-5):index],before) if index not in visited] +\
            [(word,index) for word,index in zip(words[index+1:min(turnlen,index+6)],after) if index not in visited]
        visited += before + after

        # if "not" or "no" is within the 10 word window, we reverse the resulting polarity
        if ("not" in window or "no" in window):
            reverse_polarity = True

        for word in window:
            if word[0] not in stopwords.words('english'):
                # lemmatize the word
                lematized = lemmatizer.lemmatize(word[0], get_wordnet_pos(word[0]))
                if lematized in anew:
                    if anew[lematized] >= 5:
                        positive.append(lematized)
                    else:
                        negative.append(lematized)

    if len(negative) > len(positive):
        polarity = "negative"
    else:
        polarity = "positive"

    # reverse polarity if flag set to true
    if reverse_polarity:
        if polarity == "positive":
            polarity = "negative"
        else:
            polarity = "positive"
    return polarity

#! not currently being used
def getAdjPhrases(pos):
    count = 0
    half_chunk = ""
    # 0 looking for adverb or adjective
    # 1 adverb found looking for adverb or adjective
    # 2 adjective found looking for adjective or noun
    # 3 noun found looking for more
    # if a stage fails, it returns to stage 0
    temp = ""
    stage = 0
    for word, tag in pos:
        failedStage = False
        if (stage == 0):
            if (tag == "RB"):
                stage = 1
                count += 1
            elif (tag == "JJ"):
                stage = 2
                count += 1
            else:
                failedStage = True
        elif (stage == 1):
            if (tag == "RB"):
                count += 1
            elif (tag == "JJ"):
                stage = 2
                count += 1
            else:
                failedStage = True
        elif (stage == 2):
            if (tag == "JJ"):
                count += 1
            elif (re.match(r"NNP?S?", tag)):
                stage = 3
                count += 1
            else:
                failedStage = True
        elif (stage == 3):
            if not (re.match(r"NNP?S?", tag)):
                failedStage = True

        if failedStage:
            if (stage == 3):
                half_chunk += temp + "---"
            else:
                half_chunk += "---"
            count = 0
            stage = 0
            temp = ""
        else:
            temp += word + " "
    half_chunk = re.sub(r"-+","?",half_chunk).split("?")
    half_chunk = [x.strip() for x in half_chunk if x!=""]
    return half_chunk

# TODO: generally improve accuracy 
def getTopicUtterances(jsonData, allTags, mts):
    #turns containing each topic
    topicTurns = {topic: [] for topic in mts}
    infoRequestTurns = {topic: [] for topic in mts}
    responseTurns = []
    agreeTurns = []
    disagreeTurns = []

    anew = {}
    path = str(Path(__file__).parent.parent)
    
    with open(path + '/anew.pickle', 'rb') as handle:
        anew = pickle.load(handle)

    topicalPolarityUsers = {}

    lemmatizer = WordNetLemmatizer()
    
    # pass 1
    # narrow down the search
    for turn, pos in zip(jsonData['turns'],allTags):
        tag = turn["tag"]
        if turn['speaker'] not in topicalPolarityUsers:
            topicalPolarityUsers[turn['speaker']] = {topic: [] for topic in mts}
        
        if tag == "response-answer":
            responseTurns.append(turn)
        elif tag == "agree-accept":
            agreeTurns.append(turn)
        elif tag == "disagree-reject":
            disagreeTurns.append(turn)

        for topic in mts:
            if topic in turn['text']:
                topicTurns[topic].append((turn,pos))
                if tag == "information-request":
                    infoRequestTurns[topic].append(turn["turn_no"])
    
    # pass 2
    for topic in topicTurns:
        for turn, pos in topicTurns[topic]:
            tag = turn["tag"]
            polarity = getPolarity(turn["text"], topic, anew, lemmatizer)

            #! Just add all for now
            '''
            # 1st, check if there is response-answer or assertion-opinion
            if (tag == "response-answer" or tag == "assertion-opinion"):
                topicalPolarityUsers[turn["speaker"]][topic].append((turn["turn_no"],polarity))
                continue
            
            # TODO: improve, check for verb phrases as well
            # 2nd, check if there is adjective/adverb phrase
            phrases = getAdjPhrases(pos)
            if phrases: #if there are adjective/adverb phrases
                topicalPolarityUsers[turn["speaker"]][topic].append((turn["turn_no"],polarity))
                continue
            '''
            topicalPolarityUsers[turn["speaker"]][topic].append((turn["turn_no"],polarity))


    # pass 3
    # check all response turns, if they respond to an infoRequestTurn, include them
    for turn in responseTurns:            
        linkTo = turn["link_to"]
        if linkTo != "all-users" and linkTo != "":
            citedTurn = linkTo.split(":")[1] if ":" in linkTo else None
            for topic in infoRequestTurns:
                if citedTurn in infoRequestTurns[topic]:
                    # assume blank polarity to be positive
                    polarity = turn["polarity"] or "positive"
                    topicalPolarityUsers[turn["speaker"]][topic].append((turn["turn_no"],polarity))
                    break

    # pass 4
    # check all agree/disagree responses to the above
    # TODO: Potentially too many utterances happen in these cases? unsure
    for turn in agreeTurns:
        linkTo = turn["link_to"]
        if linkTo != "all-users" and linkTo != "":
            citedUser,citedTurn = linkTo.split(":") if ":" in linkTo else (None,None)
            if citedUser:
                for topic in topicalPolarityUsers[citedUser]:
                    citedPolarities = ','.join([x[1] for x in topicalPolarityUsers[citedUser][topic] if x[0] == citedTurn])
                    citedPolarities = citedPolarities.split(",") # split on comma if multiple matches
                    
                    #get cited polarity from the majority of the 3 possibilities
                    citedPolarity = getCitedPolarity(citedPolarities)
                    
                    topicalPolarityUsers[turn["speaker"]][topic].append((turn["turn_no"],citedPolarity))
    for turn in disagreeTurns:
        linkTo = turn["link_to"]
        if linkTo != "all-users" and linkTo != "":
            citedUser,citedTurn = linkTo.split(":") if ":" in linkTo else (None,None)
            if citedUser:
                for topic in topicalPolarityUsers[citedUser]:
                    citedPolarities = ','.join([x[1] for x in topicalPolarityUsers[citedUser][topic] if x[0] == citedTurn])
                    citedPolarities = citedPolarities.split(",") # split on comma if multiple matches
                    
                    #get cited polarity from the majority of the 3 possibilities
                    citedPolarity = getCitedPolarity(citedPolarities)
                    if citedPolarity == "neutral":
                        polarity = turn["polarity"] or "positive"
                    elif citedPolarity == "positive":
                        polarity = "negative"
                    elif citedPolarity == "negative":
                        polarity = "positive"
                    topicalPolarityUsers[turn["speaker"]][topic].append((turn["turn_no"],polarity))                        
    return topicalPolarityUsers

class TopicalPositioning(object):
    topicUtterances = None

    """
    One measure of Topical Positioning is the Topical Polarity Index (TPX) which detects polarity of topical
    positioning on meso-topic T. For each speaker we count:
        (1) All utterances on T using statements with polarity P applied directly to T
        (2) All utterances that offer information with polarity P about topic T
        (3) All responses (as agree/disagree dialogue acts) to other speakers' statements with polarity P applied to T.
    We calculate TPX for each speaker as a proportion of positive, negative and neutral polarity utterances
    made by this speaker about topic T. A speaker whose utterances are overwhelmingly positive (80% or more)
    has a pro-topic positon (TPX = +1) while one who is overwhelmingly negative has an against-topic position
    (TPX = -1) and one who is largely neutral or whose utterances vary in polarity as a neutral/undecided
    position on the topic (TPX = 0) 
    """
    #output: List
    def TopicalPolarityIndex(self):
        # mesoTopics -> self.mesoTopics

        # detect the following
        # (1) all utterances on T with polarity P applied directly to T using adverb or adjective phrases, or when T is the direct object of a verb
        # (2) all utterances that offer information with polarity P about topic T
        # (3) all responses (agree/disagree acts) to other speakers' statement with polarity P applied to T

        # if 80% or more are positive towards T, TPX = +1
        # if 80% or more are negative towards T, TPX = -1
        # else, TPX = 0

        mts = [topic for topic in self.mesoTopics]

        result = []

        # call helper function
        if not self.topicUtterances:
            self.topicUtterances = getTopicUtterances(self.jsonData, self.allTags, mts)

        # calculate TPX
        # TODO: make the threshold customizable
        for user in self.topicUtterances:
            temp = {'topics': {}}
            for topic in self.topicUtterances[user]:
                positive = 0
                negative = 0
                neutral = 0
                for turn in self.topicUtterances[user][topic]:
                    if turn[1] == "positive": 
                        positive += 1
                    elif turn[1] == "negative":
                        negative += 1
                    elif turn[1] == "neutral":
                        neutral += 1
                tot = positive + negative + neutral
                tpx = "0"
                if tot != 0:
                    percentPositive = float(positive) / float(positive + negative + neutral)
                    percentNegative = float(negative) / float(positive + negative + neutral)
                    # print(user,topic,round(percentPositive,3),round(percentNegative,3))
                    if percentPositive >= 0.8:
                        tpx = "1"
                    elif percentNegative >= 0.8:
                        tpx = "-1"
                temp['topics'][topic] = tpx
            result.append((user,temp))

        return result


    """
    One measure of Topical Positioning is the Polarity Strength Index (PSX) which calculated the strength of
    topical positioning. The proportion of utterances on the topic made by each speaker to all utterances made
    on this topic by all speakers in a discourse is calculated. Speakers who make more utterances on a topic
    relative to other speakers takes a stronger position on this topic. PSX is measured on a 5-point scale
    corresponding to the quintiles in normal distribution.
    """
    #output: List
    def PolarityStrengthIndex(self):
        # calculate the proportion of utterances made on T by this speaker to all
        # utterances made on T. PSX is measured on a 5-point scale corresponding
        # to quintiles in the normal distribution.
        # all utterances (made up of the 3 things we are looking in TPX)
        # > 80% -> 5; > 60% -> 4; > 40% -> 3; > 20% -> 2; >= 0% -> 1

        mts = [topic for topic in self.mesoTopics]

        result = []

        # call helper function
        if not self.topicUtterances:
            self.topicUtterances = getTopicUtterances(self.jsonData, self.allTags, mts)

        topicUtterances = {topic: 0 for topic in mts}
        polarityStrengthUsers = {user: {topic: 0 for topic in mts} for user in self.topicUtterances}

        # calculate PSX        
        for topic in mts:
            tot = 0
            for user in self.topicUtterances:
                amt = len(self.topicUtterances[user][topic])
                polarityStrengthUsers[user][topic] = amt
                tot += amt
            topicUtterances[topic] = tot

        for user in polarityStrengthUsers:
            temp = {'topics': {}}
            for topic in polarityStrengthUsers[user]:
                ratio = float(polarityStrengthUsers[user][topic]) / float(topicUtterances[topic])
                percentile = 0
                if ratio <= 0.2:
                    percentile = 1
                elif ratio <= 0.4:
                    percentile = 2
                elif ratio <= 0.6:
                    percentile = 3
                elif ratio <= 0.8:
                    percentile = 4
                else:
                    percentile = 5
                temp['topics'][topic] = str(percentile)
            result.append((user,temp))
        return result

    # Creates combined scores from all topical positioning functions
    def TopicalPositioningFunctions(self):
        result={"speakers":{},"error":{"TopicalPolarityIndex":"",
                                        "PolarityStrengthIndex":"",
                                        "TopicalPositioningFunctions":""}}
        try:
            #Get list of speakers
            speakers=list(set([value["speaker"] for value in self.jsonData["turns"]]))
            #Adequate result structure to the number of speakers
            for speaker in speakers: result["speakers"][speaker]={}

            #Call all the tension focus functions
            try:
                TPX=self.TopicalPolarityIndex()
            except Exception as e:
                result["error"]["TopicalPolarityIndex"]=str(e)
                #Default value for Disagree-Reject Target Index function
                TPX=[(x,'0.0') for x in  speakers]
        
            try:
                PSX=self.PolarityStrengthIndex()
            except Exception as e:
                result["error"]["PolarityStrengthIndex"]=str(e)
                #Default value for Topical Disagreement Target Index function
                PSX=[(x,'0.0') for x in  speakers]

            
            #Storage the results of the tension focus for each speaker 
            for y,z in zip(TPX,PSX):
                #Storage the functions results
                result["speakers"][y[0]]["TopicalPolarityIndex"]=y[1]
                result["speakers"][z[0]]["PolarityStrengthIndex"]=z[1]

            #Return the JSON response              
            return result 
        except Exception as e:
            #Handle overall exception
            result["error"]["TopicalPositioningFunctions"]=str(e)
            #Return the JSON response
            return result

