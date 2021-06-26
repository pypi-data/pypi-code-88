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
#Import mathematical functions
import numpy as np
import math

class NetworkCentrality(object):

    """
    One measure of Network Centrality is the Communication Links Measure (CLM) which calclates a degree of
    Network Centrality for a speaker by coutning the utterances that are addressed to this speaker as a percentage
    of all utterances in a discourse. This excludes utterances addressed to everyone. A spekaer with a higher CLM
    score has a higher degree of Network Centrality.

    CommunicationLinksMeasure = #speakerCommunicationLinks/#allCommunicationLinks
    """
    #ouput: List
    def CommunicationLinksMeasure(self):
        result=[]
        communicationLinks = []
        communicationLinksUsers = {value["speaker"]: [] for value in self.jsonData["turns"]}

        for turn in self.jsonData['turns']:
            # if citing a specific user (we ignore "all-users" and "")
            linkTo = turn["link_to"]
            if linkTo != "all-users" and linkTo != "":
                citedUsers = linkTo.split(":")[0] if ":" in linkTo else linkTo
                citedUsers = citedUsers.split("+") if "+" in citedUsers else [citedUsers]

                communicationLinks.append(turn["text"])

                for citedUser in citedUsers:
                    if citedUser not in communicationLinksUsers:
                        continue
                    communicationLinksUsers[citedUser].append(turn["text"])

        # for each user, calculate communication links measure
        for user in communicationLinksUsers:
            if len(communicationLinks) == 0:
                result.append((user,str(0.0)))
            else:
                result.append((user,str(round(len(communicationLinksUsers[user])*1.0/len(communicationLinks),3))))
        return result   

    """
    One measure of Network Centrality is the Citation Rate Index (CRI) which calculates the degree of Network
    Centrality for a speaker by counting the number of times that the local topics introduced by this speaker are
    cited by other speakers. Unlike SMT of Topic Control, CRI is calculated by normalizing the citation count by
    the log number of topics introduced by the speaker. Speakers with higher CRI scores have a higher degree of
    Network Centrality.

    CitationRateIndex = (#speakerTopicMentions/log(#speakerTopics + 1)) / (#allTopicMentions/log(#allTopics + 1))
    """
    #output: List
    def CitationRateIndex(self):
        result=[]

        userTopics={}
        topicMentions = {}
        subsequentMentions = 0
        allMentions = 0

        for turn, topics in zip(self.jsonData['turns'],self.topics):
            if turn["text"] == "": continue

            if turn["speaker"] not in userTopics:
                userTopics[turn["speaker"]] = []
            
            for topic in topics:
                allMentions += 1
                if topic not in topicMentions:
                    topicMentions[topic] = 0
                    userTopics[turn["speaker"]].append(topic)
                elif topic not in userTopics[turn["speaker"]]:
                    topicMentions[topic] += 1
                    subsequentMentions += 1

        # for each user, calculated the citation rate index
        for user in userTopics:
            mentions = sum([topicMentions[topic] for topic in userTopics[user]])
            try:
                normalized = mentions/(math.log(len(userTopics[user])+1))
                cri = normalized/(subsequentMentions/(math.log(len(topicMentions)+1)))
                result.append((user,str(round(cri*1.0,3))))
            except:
                result.append((user,str(0.0)))
        return result

    """
    One measure of Network Centrality is Meso Topic Introduction (MTI) which is a variant of the LTI measure of
    Topic Control but is only applied to meso-topics rather than all local topics. Meso-topics are the most persistent
    local topics and are widely cited in long stretches of discourse. Speakers who introduce more meso-topics have
    a higher degree of Network Centrality because these topics are widely cited by others. The MTI score for a speaker
    is calculated as a percentage of meso-topics introduced by this speaker to all meso-topics in a discourse.

    MesoTopicIntroduction = #speakerMesoTopicsIntroduced/#allMesoTopics
    """
    #output: List
    def MesoTopicIntroduction(self):
        result=[]

        mesoTopicsUsers = {}
        usedTopics = {}
        # loop through the dialogue
        for turn,topics in zip(self.jsonData['turns'],self.nouns):
            # create entry for each user
            if turn["speaker"] not in mesoTopicsUsers:
                mesoTopicsUsers[turn["speaker"]] = []
            for topic in topics:
                # if the user used the mesotopic, add it to their list
                if topic in self.mesoTopics and topic not in usedTopics:
                    mesoTopicsUsers[turn["speaker"]].append(topic)
                    usedTopics[topic] = 1

        # for each user, calculate the meso topic introduction
        for user in mesoTopicsUsers:
            result.append((user,str(round(len(mesoTopicsUsers[user])*1.0/len(self.mesoTopics),3))))
        return result    

    # Creates combined scores from all network centrality functions and weights
    def NetworkCentralityFunctions(self,weights=[1,1,1]):
        result={"speakers":{},"error":{"CommunicationLinksMeasure":"",
                                    "MesoTopicIntroduction":"",
                                    "CitationRateIndex":"",
                                    "NetworkCentralityFunctions":""}}
        try:
            #Get list of speakers
            speakers=list(set([value["speaker"] for value in self.jsonData["turns"]]))
            #Adequate result structure to the number of speakers
            for speaker in speakers: result["speakers"][speaker]={}


            #Call all the network centrality functions
            try:
                CLM=self.CommunicationLinksMeasure()
            except Exception as e:
                result["error"]["CommunicationLinksMeasure"]=str(e)
                #Default value for Communication Links Measure function
                CLM=[(x,'0.0') for x in speakers]
            try:
                CRI=self.CitationRateIndex()
            except Exception as e:
                result["error"]["CitationRateIndex"]=str(e)
                #Default value for Citation Rate Index function
                CRI=[(x,'0.0') for x in speakers]
            try:
                MTI=self.MesoTopicIntroduction()
            except Exception as e:
                result["error"]["MesoTopicIntroduction"]=str(e)
                #Default value for Meso Topic Introduction function
                MTI=[(x,'0.0') for x in speakers]
            
            #Storage the results of the network centrality for each speaker 
            for x,y,z in zip(CLM,CRI,MTI):
                #Storage the functions results
                result["speakers"][x[0]]["CommunicationLinksMeasure"]=x[1]
                result["speakers"][y[0]]["CitationRateIndex"]=y[1]
                result["speakers"][z[0]]["MesoTopicIntroduction"]=z[1]

            #Calculate the network centrality average for each speaker
            for speaker in result["speakers"]:
                functions=[function for function in result["speakers"][speaker]]
                average = round(np.average([float(result["speakers"][speaker][function]) for function in functions], 
                    weights=weights),3)
                #Storage the average network centrality
                result["speakers"][speaker]["averageNetworkCentrality"]=str(average)
            #Return the JSON response              
            return result
        except Exception as e:
            #Handle overall exception
            result["error"]["NetworkCentralityFunctions"]=str(e)
            #Return the JSON response
            return result