# This file is for general preprocessing to be done on dialogues such as
# Part of Speech extraction or any high-cost processing that we want
# to perform only once.

# TODO: Implement new ways of discovering topics. This is using the naive method
# TODO: of noun detection in order to compare results to the previous web-based version.

# TODO: add customization to topic and mesotopic criteria

#Import Json elements to encode Python data structures
import json
#Import functions to deal with text
import re, string, unicodedata
#Import nartural language processing functions
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize, sent_tokenize
#Import stanford PoS tagger
from nltk.tag import StanfordPOSTagger
#Import file manipulation function
import codecs

#Import pathlib
from pathlib import Path

#Function that Break texts into words
#Input: string
#ouput: list
def tokenize(text):
    return nltk.word_tokenize(text.lower())

#Function that removes non-ASCII characters from list of tokenized words
#Input: list
#ouput: list
def removeNonAscii(words):
    return [unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore') for word in words]

#Remove empty elements after some preprocessing
#Input: list
#ouput: list
def removeEmptyElements(text):
    return [word.replace('\n', '') for word in text if word != ""]

#Remove punctuation from list of tokenized words
def removeAscii(words):
    return [re.sub(r'[^\w\s]','',word) for word in words if word != ""]

#Function that removes English stopWords from a text
#Input: list
#ouput: list
def removeStopWords(words):
    return [word for word in words if word not in stopwords.words('english')]


#Clean text based in other functions
#Input: string
#ouput: list
def normalize(text): 
    words=tokenize(text)
    words=removeNonAscii(words)
    words=removeAscii(words)
    words=removeEmptyElements(words)
    words=removeStopWords(words)
    return words

def normMinusStop(text): 
    words=tokenize(text)
    words=removeNonAscii(words)
    words=removeAscii(words)
    words=removeEmptyElements(words)
    return words

#Concatenate dialogue utterances  
def concatenateUtterances(dialogueTurns):
    return [normalize(turn["text"]) for turn in dialogueTurns]

#Concatenate dialogue utterances  
def concatenateUtterancesMinusStop(dialogueTurns):
    return [normMinusStop(turn["text"]) for turn in dialogueTurns]

# returns all words with noun tags in each turn
def NounPosTags(posTags):
    tags=['NN','NNS','NNP','NNPS']
    return [[word[0] for word in elements if word[1] in tags] for elements in posTags]
    
# returns all nouns with at least n occurrences in each turn 
def Topics(turns, n):
    allTopics = []
    wordOccurences = {}
    for turn in turns:
        temp = []
        for word in turn:
            if word not in wordOccurences:
                wordOccurences[word] = 0
            wordOccurences[word] += 1
            temp.append(word)
        allTopics.append(temp)
    return [[word for word in turn if wordOccurences[word] >= n] for turn in allTopics]

# returns a dictionary of mesoTopics based on the mesoTopicThreshold, n
def MesoTopics(dialogue, turns, n):
    topicDict = {}
    for turn, topics in zip(dialogue,turns):
        # ignore turns with no dialogue
        if turn["text"] == "": continue

        for topic in topics:
            # if topic is a new topic, create an entry
            if topic not in topicDict:
                topicDict[topic] = []
            topicDict[topic].append(turn)
    
    mesoTopics = {topic: [float(turn["turn_no"]) for turn in topicDict[topic]] for topic in topicDict if len(topicDict[topic]) >= n}
    return mesoTopics

class Preprocessing(object):
    #Get PoS tags for words in dialogue using Stanford
    def stanfordPoSTagger(self):
        try:
            #Concatenate all utterances into a single list
            fullList=concatenateUtterancesMinusStop(self.jsonData["turns"])
            wordList=concatenateUtterances(self.jsonData["turns"])
            
            #get path
            path = str(Path(__file__).parent.parent)

            # Add jar and model via their path (instead of setting environment) 
            jar=path+"/stanford-postagger-full-2015-04-20/stanford-postagger.jar"
            model=path+"/stanford-postagger-full-2015-04-20/models/english-left3words-distsim.tagger"
            #Set up PoS tagger
            posTagger = StanfordPOSTagger(model, jar, encoding='utf8')
            self.posTags=posTagger.tag_sents(wordList)
            self.allTags=posTagger.tag_sents(fullList)
        except Exception as e:
            print("EXCEPTION:", e)

    #Get nouns, topics, mesotopics using Stanford
    def NounPosTagsStanford(self, n, mesoTopicThreshold):
        try:
            if (self.posTags):
                self.nouns = NounPosTags(self.posTags)
                self.topics = Topics(self.nouns, n)
                self.mesoTopics = MesoTopics(self.jsonData['turns'], self.nouns, mesoTopicThreshold)
        except Exception as e:
            print("EXCEPTION:", e)

    #Get PoS tags for words in dialogue using NLTK
    def NLTKPoSTagger(self):
        try:
            #Concatenate all utterances into a single list
            fullList=concatenateUtterancesMinusStop(self.jsonData["turns"])
            wordList=concatenateUtterances(self.jsonData["turns"])
            self.posTags=[nltk.pos_tag(word) for word in [words for words in wordList]]
            self.allTags=[nltk.pos_tag(word) for word in [words for words in fullList]]
        except Exception as e:
            print("EXCEPTION:", e)

    #Get nouns, topics, mesotopics using NLTK
    def NounPosTagsNLTK(self, n, mesoTopicThreshold):
        try:    
            if (self.posTags):
                self.nouns = NounPosTags(self.posTags)
                self.topics = Topics(self.nouns, n)
                self.mesoTopics = MesoTopics(self.jsonData['turns'], self.nouns, mesoTopicThreshold)
        except Exception as e:
            print("EXCEPTION:", e)

