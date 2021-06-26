#Import Json elements to encode Python data structures
import json
#Import functions to deal with text
import re, string, unicodedata
#Import nartural language processing functions
import nltk
from nltk import word_tokenize, sent_tokenize
#Import mathematical functions
import numpy as np

class SocialPositioning(object):
    
    """
    One measure of Social Positioning is the Offer-Commit Index (OCI) which looks at commitments on the part of the
    speaker to some future action. We count the number of Offer-Commit dialogue acts in the utterances made by each
    speaker as a proportion of all Offer-Commit utterances in the discourse.

    OfferCommitIndex = #speakerOfferCommits/#allOfferCommits
    """
    #output: List
    def OfferCommitIndex(self):
        result = []
        offerCommit = []
        offerCommitUsers = {}

        for turn in self.jsonData['turns']:
            if turn["speaker"] not in offerCommitUsers:
                offerCommitUsers[turn["speaker"]] = []
            #MAKE SURE THIS EXISTS
            tag = turn["tag"]
            if tag == "offer-commit":
                offerCommit.append(turn["text"])
                offerCommitUsers[turn["speaker"]].append(turn["text"])

        for user in offerCommitUsers:
            if len(offerCommit) == 0:
                result.append((user,str(0.0)))
            else:
                result.append((user,str(round(len(offerCommitUsers[user])*1.0/len(offerCommit),3))))
        return result

    """
    One measure of Social Positioning is the Confirmation-Request Index (CRI) which looks at speakers making
    confirmation requests. We count the number of Confirmation-Request dialogue acts in the utterances made by each
    speaker as a proportion of all Confirmation-Request utterances in the discourse.

    ConfirmationRequestIndex = #speakerConfirmationRequests/#allConfirmationRequests
    """
    #output: List
    def ConfirmationRequestIndex(self):
        result = []
        confirmationRequest = []
        confirmationRequestUsers = {}

        for turn in self.jsonData['turns']:
            if turn["speaker"] not in confirmationRequestUsers:
                confirmationRequestUsers[turn["speaker"]] = []

            tag = turn["tag"]
            if tag == "confirmation-request":
                confirmationRequest.append(turn["text"])
                confirmationRequestUsers[turn["speaker"]].append(turn["text"])

        for user in confirmationRequestUsers:
            if len(confirmationRequest) == 0:
                result.append((user,str(0.0)))
            else:
                result.append((user,str(round(len(confirmationRequestUsers[user])*1.0/len(confirmationRequest),3))))
        return result

    # Creates combined scores from all social positioning functions and weights
    def SocialPositioningFunctions(self,weights=[1,1]):
        result={"speakers":{},"error":{"OfferCommitIndex":"",
                                        "ConfirmationRequestIndex":"",
                                        "SocialPositioningFunctions":""}}
        try:
            #Get list of speakers
            speakers=list(set([value["speaker"] for value in self.jsonData["turns"]]))
            #Adequate result structure to the number of speakers
            for speaker in speakers: result["speakers"][speaker]={}

            #Call all the social positioning functions
            try:
                OCI=self.OfferCommitIndex()
            except Exception as e:
                result["error"]["OfferCommitIndex"]=str(e)
                #Default value for Offer Commit Index function
                OCI=[(x,'0.0') for x in  speakers]

            try:
                CRI=self.ConfirmationRequestIndex()
            except Exception as e:
                result["error"]["ConfirmationRequestIndex"]=str(e)
                #Default value for Confirmation Request Index function
                CRI=[(x,'0.0') for x in  speakers]

            
            #Storage the results of the social positioning for each speaker 
            for y,z in zip(OCI,CRI):
                #Storage the functions results
                result["speakers"][y[0]]["OfferCommitIndex"]=y[1]
                result["speakers"][z[0]]["ConfirmationRequestIndex"]=z[1]

            #Calculate the social positioning average for each speaker
            for speaker in result["speakers"]:
                functions=[function for function in result["speakers"][speaker]]
                average = round(np.average([float(result["speakers"][speaker][function]) for function in functions], 
                    weights=weights),3)
                #Storage the average social positioning
                result["speakers"][speaker]["averageSocialPositioning"]=str(average)
            #Return the JSON response              
            return result
        except Exception as e:
            #Handle overall exception
            result["error"]["SocialPositioningFunctions"]=str(e)
            #Return the JSON response
            return result