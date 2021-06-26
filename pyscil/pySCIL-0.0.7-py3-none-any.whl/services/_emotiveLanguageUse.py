#Import Json elements to encode Python data structures
import json
#Import functions to deal with text
import re, string, unicodedata
#Import nartural language processing functions
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

#Import mathematical functions
import numpy as np

#Import pathlib
from pathlib import Path

import pickle

#Extract the wordnet PoS from a word
#Input: string
#output: wordnet PoS
def get_wordnet_pos(word):
    #Map POS tag to first character lemmatize() accepts
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)

class EmotiveLanguageUse(object):

    """
    One measure of Emotive Language Use is the Emotive Word Index (EWI) which is the proportion 
    of emotionally charged words used by a speaker. The value of EWI is calculated as a 
    percentage of emotional words (including repetitions) used by this speaker in a discourse.
    Emotive words are stored in a pickled dictionary adapted from Tom Drummond's vocabulary of emotions.

    EmotiveWordIndex = #userEmotiveWords/#allEmotiveWords
    """
    #output: List
    def EmotiveWordIndex(self):
        result = []
        emotiveWords = []
        emotiveWordsUsers = {}

        path = str(Path(__file__).parent.parent)

        # open the pickled dictionary of emotive words
        with open(path + '/emotive_words.pickle', 'rb') as handle:
            emotiveWordDict = pickle.load(handle)

            lemmatizer = WordNetLemmatizer()

            for turn in self.jsonData['turns']:
                # store all speakers in the dialogue
                if turn["speaker"] not in emotiveWordsUsers:
                    emotiveWordsUsers[turn["speaker"]] = []

                for word in turn["text"].split(" "):
                    # ignore blank strings
                    if word == "":
                        continue

                    # lemmatize the word
                    word = lemmatizer.lemmatize(word, get_wordnet_pos(word))

                    # if word is in the dictionary add it to our storage
                    if word in emotiveWordDict:
                        emotiveWords.append(word)
                        emotiveWordsUsers[turn["speaker"]].append(word)
                        
        #  for each user, calculate the emotive word index
        for user in emotiveWordsUsers:
            if len(emotiveWords) == 0:
                result.append((user,str(0.0)))
            else:
                result.append((user,str(round(len(emotiveWordsUsers[user])*1.0/len(emotiveWords),3))))
        return result

    # Creates combined scores from all emotive language use functions and weights
    def EmotiveLanguageUseFunctions(self,weights=[1]):
        result={"speakers":{},"error":{"EmotiveWordIndex":"",
                                        "EmotiveLanguageUseFunctions":""}}
        try:
            #Get list of speakers
            speakers=list(set([value["speaker"] for value in self.jsonData["turns"]]))
            #Adequate result structure to the number of speakers
            for speaker in speakers: result["speakers"][speaker]={}

            #Call all the emotive language use functions
            try:
                EWI=self.EmotiveWordIndex()
            except Exception as e:
                result["error"]["EmotiveWordIndex"]=str(e)
                #Default value for Emotive Word Index function
                EWI=[(x,'0.0') for x in speakers]

            #Store the results of the emotive language use for each speaker
            for z in EWI:
                #Store the functions results
                result["speakers"][z[0]]["EmotiveWordIndex"]=z[1]
            
            #Calculate the emotive language use average for each speaker
            for speaker in result["speakers"]:
                functions = [function for function in result["speakers"][speaker]]
                average = round(np.average([float(result["speakers"][speaker][function]) for function in functions], 
                    weights=weights),3)
                #Store the average emotive language use
                result["speakers"][speaker]["averageEmotiveLanguageUse"]=str(average)
            
            #Return the JSON response
            return result
        except Exception as e:
            #Handle overall exception
            result["error"]["EmotiveLanguageUseFunctions"]=str(e)
            #Return the JSON response
            return result