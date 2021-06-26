#Import Json elements to encode Python data structures
import json
#Import functions to deal with text
import re, string, unicodedata
#Import nartural language processing functions
import nltk
from nltk import word_tokenize, sent_tokenize
#Import mathematical functions
import numpy as np

class Disagreement(object):

    """
    One measure of disagreement is the Disagree-Reject Index (DRX) which is the proportion of disagree and/or reject turns 
    produced by a speaker that are directed at any other participants in the discourse. According to this measure, a 
    speaker who makes more utterances of disagreement, disapproval, or rejection is considered to produce a higher degree 
    of disagreement in discourse. We calculate the proportion of utterances of disagreement, disapproval and rejection in 
    the discourse that are made by each speaker as a percentage of all such utterances by all speakers in discourse.

    DisagreeRejectIndex = #speakerDisagreeRejects/#allDisagreeRejects
    """
    #output: List
    def DisagreeRejectIndex(self):
        result = []
        disagreeRejects = []
        disagreeRejectsUsers = {}

        for turn in self.jsonData['turns']:
            if turn["speaker"] not in disagreeRejectsUsers:
                disagreeRejectsUsers[turn["speaker"]] = []

            tag = turn["tag"]
            if tag == "disagree-reject":
                disagreeRejects.append(turn["text"])
                disagreeRejectsUsers[turn["speaker"]].append(turn["text"])

        for user in disagreeRejectsUsers:
            if len(disagreeRejects) == 0:
                result.append((user,str(0.0)))
            else:
                result.append((user,str(round(len(disagreeRejectsUsers[user])*1.0/len(disagreeRejects),3))))
        return result

    """
    One measure of disagreement is the Topical Disagreement Index (TDX) which captures the differential between two
    (or more) speakers' attitudes or sentiments towards a topic. The value of TDX for each speaker is the proportion
    of topical disagreement turns made by this speaker to the sum of such statements made by all speakers in a discourse.
    Utterances that (1) make either positive for negative statements about a topic and (2) offer either supportive or
    unsupportive information about this topic are taken into account to calculate TDX.

    TopicalDisagreementIndex = #speakerTopicalDisagreement/#allTopicalDisagreement 
    """
    #output: List
    def TopicalDisagreementIndex(self):
        result=[]

        topicalDisagreement = []
        topicalDisagreementUsers = {}
        #0 neutral/unknown, 1 = positive, -1 = negative
        topics = {}
        #6 is link to 7 is polarity 8 is topic

        for turn in self.jsonData['turns']:
            # create entry for each user
            if turn["speaker"] not in topicalDisagreementUsers:
                topicalDisagreementUsers[turn["speaker"]] = []

            topic, polarity = turn["topic"], turn["polarity"]

            if topic not in topics:
                #"" is default person
                topics[topic] = ["", 0]

            changePolar = False
            
            newPolarity = 0

            if polarity == "" or polarity == "neutral":
                newPolarity = 0

            elif polarity == "positive":
                newPolarity = 1

            elif polarity == "negative":
                newPolarity = -1

            if topics[topic][0] != "" and topics[topic][0] != turn["text"] and topics[topic][1] != 0 and topics[topic][1] == -newPolarity:
                changePolar = True

            topics[topic][0] = turn["text"]
            topics[topic][1] = newPolarity

            tag = turn["tag"]
            if tag != "disagree-reject" and changePolar:
                topicalDisagreement.append(turn["text"])

                topicalDisagreementUsers[turn["speaker"]].append(turn["text"])

        # for each user, calculate disagree reject index
        for user in topicalDisagreementUsers:
            if len(topicalDisagreement) == 0:
                result.append((user,str(0.0)))
            else:
                result.append((user,str(round(len(topicalDisagreementUsers[user])*1.0/len(topicalDisagreement),3))))

        return result   

    # Creates combined scores from all disagreement functions and weights
    def DisagreementFunctions(self,weights=[1,1]):
        result={"speakers":{},"error":{"DisagreeRejectIndex":"",
                                    "TopicalDisagreementIndex":"",
                                    "DisagreementFunctions":""}}
        try:
            #Get list of speakers
            speakers=list(set([value["speaker"] for value in self.jsonData["turns"]]))
            #Adequate result structure to the number of speakers
            for speaker in speakers: result["speakers"][speaker]={}

            #Call all the agreement functions
            try:
                DRX = self.DisagreeRejectIndex()
            except Exception as e:
                result["error"]["DisagreeRejectIndex"]=str(e)
                #Default value for Disagree Reject Index function
                DRX=[(x,'0.0') for x in  speakers]

            try:    
                TDX = self.TopicalDisagreementIndex()
            except Exception as e:
                result["error"]["TopicalDisagreementIndex"]=str(e)
                #Default value for Topical Disagreement Index function
                TDX=[(x,'0.0') for x in  speakers]


            #Store the results of the disagreement for each speaker
            for x,z in zip(DRX,TDX):
                #Store the functions results
                result["speakers"][x[0]]["DisagreeRejectIndex"]=x[1]
                result["speakers"][z[0]]["TopicalDisagreementIndex"]=z[1]

            #Calculate the disagreement average for each speaker
            for speaker in result["speakers"]:
                functions = [function for function in result["speakers"][speaker]]
                average = round(np.average([float(result["speakers"][speaker][function]) for function in functions], 
                    weights=weights),3)
                #Store the average disagreement
                result["speakers"][speaker]["averageDisagreement"]=str(average)
            #Return the JSON response
            return result
        except Exception as e:
            #Handle overall exception
            result["error"]["DisagreementFunctions"]=str(e)
            #Return the JSON response
            return result

