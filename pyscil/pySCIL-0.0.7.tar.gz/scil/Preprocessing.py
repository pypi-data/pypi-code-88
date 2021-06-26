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

#Get and keep certain part of speech tags
#Input: list of lists
#ouput: list of lists
def NounPosTagsNLTK(wordList): 
  tags=['NN', 'NNS', 'NNP', 'NNPS']
  wordList=[word for word in [words for words in wordList] if word]
  wordList=[nltk.pos_tag(word) for word in [words for words in wordList]]
  return [[word[0] for word in words if word[1] in tags] for words in wordList]

#Get and keep certain part of speech tags using the stanford lib
#Input: list of lists
#ouput: list of lists
def NounPosTagsStanford(wordList):
  #get the flask script path
  appPath=str(Path(__file__).parent)
  # Add jar and model via their path (instead of setting environment)
  jar=appPath+"/stanford-postagger-full-2015-04-20/stanford-postagger.jar"
  model=appPath+"/stanford-postagger-full-2015-04-20/models/english-left3words-distsim.tagger"
  #Set up PoS tagger
  posTagger = StanfordPOSTagger(model, jar, encoding='utf8')
  #Select noun tags only (topics)
  tags=['NN', 'NNS', 'NNP', 'NNPS']
  wordTags=posTagger.tag_sents(wordList)
  return [[word[0] for word in elements if word[1] in tags] for elements in wordTags]

#Concatenate preprocess dialogue utterances
#Input: list
#ouput: list
def concatenateCleanUtterances(dialogueTurns):
    return [normalize(turn["text"]) for turn in dialogueTurns]


#Concatenate dialogue utterances
#Input: list
#ouput: list
def concatenateUtterances(dialogueTurns):
    return [turn["text"] for turn in dialogueTurns]

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
