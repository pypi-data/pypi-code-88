#Import Json elements to encode Python data structures
import json
#Import functions to deal with text
import re, string, unicodedata
#Import nartural language processing functions
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
nltk.download('stopwords')
#Import mathematical functions
import numpy as np

#Import string for removing punctuation
import string

class ArgumentDiversity(object):

    """
    One measure of argument diversity is the rate at which different speakers size of 
    vocabulary for a single user. Speakers who introduce more new words have a greater 
    Argument Diversity. All content words are counted, but lexical variants are 
    considered as instances of the same word. VRI is calculated as distinct words 
    used by this speaker as a percentage of all distinct words in discourse

    VocabularyRangeIndex = #speakerVocabulary/#allVocabulary
    """
    #output: List
    def VocabularyRangeIndex(self):
        result = []
        #Holds all vocab everyone uses
        vocabulary = set()
        vocabularyUsers = {}

        #Initiate Lemmatizer so same lexical variants are ignored
        lemmatizer = WordNetLemmatizer() 

        for turn in self.jsonData["turns"]:
            if turn["speaker"] not in vocabularyUsers:
                vocabularyUsers[turn["speaker"]] = set()

            #Currently only ignores punctuation
            words = [word for word in turn["text"].split(" ") if word.lower() not in string.punctuation]

            for word in words:

                tempWord = lemmatizer.lemmatize(word)
                if tempWord not in vocabularyUsers[turn["speaker"]]:
                        vocabularyUsers[turn["speaker"]].add(tempWord)
                if tempWord not in vocabulary:
                    vocabulary.add(tempWord)

        for user in vocabularyUsers:
            #Each user value is the percentage of unique words used in relation to all words in the conversation
            result.append((user, str(round(len(vocabularyUsers[user])*1.0/len(vocabulary),3))))

        return result

    """
    One measure of argument diversity is the rate at which different speakers introduce new words 
    into the conversation. Speakers who introduce more new words have a greater Argument Diversity.
    All content words are counted, including emoticons and other textese, but not the stop-words 
    (i.e., prepositions, articles, etc.), and lexical variants are considered as instances of the 
    same word. VIM is calculated as a proportion of new content words introduced by each speaker 
    to all distinct content words in discourse.

    VocabularyIntroductionMeasure = #speakerVocabulary/#allVocabulary
    """
    #output: List
    def VocabularyIntroductionMeasure(self):
        result = []
        vocabulary = set()
        vocabularyUsers = {}

        # getting set of stopwords
        stopWords = set(stopwords.words('english'))

        for turn in self.jsonData["turns"]:
            if turn["speaker"] not in vocabularyUsers:
                vocabularyUsers[turn["speaker"]] = set()
            
            # lemmatizer for eliminating simple lexical variants
            lemmatizer = WordNetLemmatizer() 

            # splits turn utterance into words, filtering out stopwords and punctuation
            words = [word for word in turn["text"].split(" ") if word.lower() not in stopWords
                and word.lower() not in string.punctuation]

            for word in words:
                # lemmatizing word
                tempWord = lemmatizer.lemmatize(word)
                if tempWord not in vocabulary:
                    vocabulary.add(tempWord)
                if tempWord not in vocabularyUsers[turn["speaker"]]:
                    vocabularyUsers[turn["speaker"]].add(tempWord)

        for user in vocabularyUsers:
            result.append((user, str(round(len(vocabularyUsers[user])*1.0/len(vocabulary),3))))

        return result

    # Creates combined scores from all argument diversity functions and weights
    def ArgumentDiversityFunctions(self,weights=[1,1]):
        result={"speakers":{},"error":{"VocabularyRangeIndex":"",
                                    "VocabularyIntroductionMeasure":"",
                                    "ArgumentDiversityFunctions":""}}
        try:
            #Get list of speakers
            speakers=list(set([value["speaker"] for value in self.jsonData["turns"]]))
            #Adequate result structure to the number of speakers
            for speaker in speakers: result["speakers"][speaker]={}

            #Call all the argument diversity functions
            try:
                VRI = self.VocabularyRangeIndex()
            except Exception as e:
                result["error"]["VocabularyRangeIndex"]=str(e)
                #Default value for Vocabulary Range Index function
                VRI=[(x,'0.0') for x in  speakers]

            try:    
                VIM = self.VocabularyIntroductionMeasure()
            except Exception as e:
                result["error"]["VocabularyIntroductionMeasure"]=str(e)
                #Default value for Vocabulary Introduction Measure function
                VIM=[(x,'0.0') for x in  speakers]
            

            #Store the results of the argument diversity for each speaker
            for x,z in zip(VRI,VIM):
                #Store the functions results
                result["speakers"][x[0]]["VocabularyRangeIndex"]=x[1]
                result["speakers"][z[0]]["VocabularyIntroductionMeasure"]=z[1]
            
            #Calculate the argument diversity average for each speaker
            for speaker in result["speakers"]:
                functions = [function for function in result["speakers"][speaker]]
                average = round(np.average([float(result["speakers"][speaker][function]) for function in functions], 
                    weights=weights),3)
                #Store the average argument diversity
                result["speakers"][speaker]["averageArgumentDiversity"]=str(average)

            #Return the JSON response
            return result
        except Exception as e:
            #Handle overall exception
            result["error"]["ArgumentDiversityFunctions"]=str(e)
            #Return the JSON response
            return result
