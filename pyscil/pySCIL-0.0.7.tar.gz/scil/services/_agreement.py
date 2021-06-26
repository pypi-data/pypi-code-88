#Import Json elements to encode Python data structures
import json
#Import functions to deal with text
import re, string, unicodedata
#Import nartural language processing functions
import nltk
from nltk import word_tokenize, sent_tokenize
#Import mathematical functions
import numpy as np

class Agreement(object):

    """
    One measure of agreement is the Agree-Accept Index (ATX) which is the proportion of agree and/or accept turns 
    produced by a speaker that are directed at any other participants in the discourse. According to this measure, 
    a speaker who makes more utterances of agreement, approval, or acceptance is considered to produce a higher 
    degree of agreement in discourse. We calculate the proportion of utterances of agreement, approval and acceptance 
    in the discourse that are made by each speaker as a percentage of all such utterances by all speakers in discourse. 

    AgreeAcceptIndex = #speakerAgreeAccepts/#allAgreeAccepts
    """
    #output: List
    def AgreeAcceptIndex(self):
        result = []
        agreeAccepts = []
        agreeAcceptsUsers = {}

        for turn in self.jsonData['turns']:
            if turn["speaker"] not in agreeAcceptsUsers:
                agreeAcceptsUsers[turn["speaker"]] = []

            tag = turn["tag"]
            if tag == "agree-accept":
                agreeAccepts.append(turn["text"])
                agreeAcceptsUsers[turn["speaker"]].append(turn["text"])

        for user in agreeAcceptsUsers:
            if len(agreeAccepts) == 0:
                result.append((user,str(0.0)))
            else:
                result.append((user,str(round(len(agreeAcceptsUsers[user])*1.0/len(agreeAccepts),3))))
        return result

    """
    One measure of agreement is the Topical Agreement Index (TAX) which captures the convergence between two
    (or more) speakers' attitudes or sentiments towards a topic. The value of TAX for each speaker is the
    proportion of topical agreement turns made by this speaker to the sum of such statements made by all
    speakers in a discourse. Utterances that (1) make either positive or negative statements about a topic
    and (2) offer either supportive or unsupportive information about a topic are take into account to
    calculate TAX. 

    TopicaAgreementIndex = #speakerTopicalAgreement/#allTopicalAgreement
    """
    #output: List
    def TopicalAgreementIndex(self):
        result=[]

        topicalAgreement = []
        topicalAgreementUsers = {}
        #0 neutral/unknown, 1 = positive, -1 = negative
        topics = {}
        #6 is link to 7 is polarity 8 is topic

        for turn in self.jsonData['turns']:
            # create entry for each user
            if turn["speaker"] not in topicalAgreementUsers:
                topicalAgreementUsers[turn["speaker"]] = []

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
            if tag != "agree-accept" and changePolar:
                topicalAgreement.append(turn["text"])

                topicalAgreementUsers[turn["speaker"]].append(turn["text"])

        # for each user, calculate disagree agreement index
        for user in topicalAgreementUsers:
            if len(topicalAgreement) == 0:
                result.append((user,str(0.0)))
            else:
                result.append((user,str(round(len(topicalAgreementUsers[user])*1.0/len(topicalAgreement),3))))

        return result   

    # Creates combined scores from all agreement functions and weights
    def AgreementFunctions(self,weights=[1,1]):
        result={"speakers":{},"error":{"AgreeAcceptIndex":"",
                                    "TopicalAgreementIndex":"",
                                    "AgreementFunctions":""}}
        try:
            #Get list of speakers
            speakers=list(set([value["speaker"] for value in self.jsonData["turns"]]))
            #Adequate result structure to the number of speakers
            for speaker in speakers: result["speakers"][speaker]={}

            #Call all the agreement functions
            try:
                ATX = self.AgreeAcceptIndex()
            except Exception as e:
                result["error"]["AgreeAcceptIndex"]=str(e)
                #Default value for Agree Accept Index function
                ATX=[(x,'0.0') for x in  speakers]

            try:    
                TAX = self.TopicalAgreementIndex()
            except Exception as e:
                result["error"]["TopicalAgreementIndex"]=str(e)
                #Default value for Topical Agreement Index function
                TAX=[(x,'0.0') for x in  speakers]


            #Store the results of the agreement for each speaker
            for x,z in zip(ATX,TAX):
                #Store the functions results
                result["speakers"][x[0]]["AgreeAcceptIndex"]=x[1]
                result["speakers"][z[0]]["TopicalAgreementIndex"]=z[1]

            #Calculate the agreement average for each speaker
            for speaker in result["speakers"]:
                functions = [function for function in result["speakers"][speaker]]
                average = round(np.average([float(result["speakers"][speaker][function]) for function in functions], 
                    weights=weights),3)
                #Store the average agreement
                result["speakers"][speaker]["averageAgreement"]=str(average)
            #Return the JSON response
            return result
        except Exception as e:
            #Handle overall exception
            result["error"]["AgreementFunctions"]=str(e)
            #Return the JSON response
            return result

