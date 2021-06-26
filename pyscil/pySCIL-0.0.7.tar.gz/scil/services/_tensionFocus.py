#Import Json elements to encode Python data structures
import json
#Import functions to deal with text
import re, string, unicodedata
#Import nartural language processing functions
import nltk
#Import mathematical functions
import numpy as np

class TensionFocus(object):

    """
    One measure of tension focus is the Disagree-Reject Target Index (DRT) which is the 
    proportion of disagree-reject and confirmation-request turns in discourse that directed 
    at a particular speaker. According to this measure, a speaker at whom more utterances of 
    disagreement, disapproval, or rejection are directed by other speakers or whose statements are 
    questioned by others is considered to have a higher degree of tension focus. We calculate the 
    proportion of utterances of disagreement, disapproval and rejection, as well as confirmation 
    requests in the discourse that are directed at each speaker as a percentage of all such 
    utterances by all speakers in discourse.

    #DisagreeRejectTargetIndex = #speakerTargetedDisagreements/#allTargetedDisagreements
    """
    #ouput: List
    def DisagreeRejectTargetIndex(self):
        result=[]

        disagreeTargets = []
        disagreeTargetsUsers = {value["speaker"]: [] for value in self.jsonData["turns"]}

        for turn in self.jsonData['turns']:
            # check if tagged as disagree-reject or confirmation-request
            tag = turn["tag"]
            linkTo = turn["link_to"]
            if tag == "disagree-reject" or tag == "confirmation-request":        
                # if citing a specific user (we ignore "all-users" and "")
                if linkTo != "all-users" and linkTo != "":
                    citedUsers = linkTo.split(":")[0] if ":" in linkTo else linkTo
                    citedUsers = citedUsers.split("+") if "+" in citedUsers else [citedUsers]

                    disagreeTargets.append(turn["text"])

                    for citedUser in citedUsers:
                        # ignore self references
                        if citedUser == turn["speaker"]: continue

                        if citedUser not in disagreeTargetsUsers:
                            continue
                        disagreeTargetsUsers[citedUser].append(turn["text"])


        # for each user, calculate disagree reject target index
        for user in disagreeTargetsUsers:
            if len(disagreeTargets) == 0:
                result.append((user,str(0.0)))
            else:
                result.append((user,str(round(len(disagreeTargetsUsers[user])*1.0/len(disagreeTargets),3))))
        return result   

    """
    One measure of Tension Focus is the Topical Disagreement Target Index (TDT) which captures the differential between
    two (or more) speakers' attitudes or sentiments towards a topic. For the purpose of this measure, we shall count
    all unmarked statements by a speaker where there is an earlier (the most recent) statement by another speaker on
    the same topic but with opposite polarity. Here, "unmarked" refers to a statement not explicitly marked as
    Disagree-Reject or otherwise counted under the DRT measure. The value of TDT for each speaker is the proportion
    of topical disagreement turns directed at this speaker by all other speakers to the sum of such statements made by
    all speakers in a discourse. 
    """
    #ouput: List
    def TopicalDisagreementTargetIndex(self):
        result=[]

        topicalDisagreementTarget = []
        topicalDisagreementTargetUsers = {value["speaker"]: [] for value in self.jsonData["turns"]}
        #0 neutral/unknown, 1 = positive, -1 = negative
        topics = {}
        #6 is link to 7 is polarity 8 is topic

        for turn in self.jsonData['turns']:
            citedUsers = []

            # if citing a specific user (we ignore "all-users" and "")
            linkTo = turn["link_to"]
            if linkTo != "all-users" and linkTo != "":
                citedUsers = linkTo.split(":")[0] if ":" in linkTo else linkTo
                citedUsers = citedUsers.split("+") if "+" in citedUsers else [citedUsers]

            topic = turn["topic"]
            if topic not in topics:
                #"" is default person
                topics[topic] = ["", 0]

            changePolar = False
            
            newPolarity = 0

            polarity = turn["polarity"]
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
                topicalDisagreementTarget.append(turn["text"])
                for citedUser in citedUsers:
                    if citedUser == turn["speaker"]: continue

                    topicalDisagreementTargetUsers[citedUser].append(turn["text"])

        # for each user, calculate disagree reject target index
        for user in topicalDisagreementTargetUsers:
            if len(topicalDisagreementTarget) == 0:
                result.append((user,str(0.0)))
            else:
                result.append((user,str(round(len(topicalDisagreementTargetUsers[user])*1.0/len(topicalDisagreementTarget),3))))

        return result  

    # Creates combined scores from all tension focus functions and weights
    def TensionFocusFunctions(self,weights=[1,1]):
        result={"speakers":{},"error":{"DisagreeRejectTargetIndex":"",
                                        "TopicalDisagreementTargetIndex":"",
                                        "TensionFocusFunctions":""}}
        try:
            #Get list of speakers
            speakers=list(set([value["speaker"] for value in self.jsonData["turns"]]))
            #Adequate result structure to the number of speakers
            for speaker in speakers: result["speakers"][speaker]={}

            #Call all the tension focus functions
            try:
                DRT=self.DisagreeRejectTargetIndex()
            except Exception as e:
                result["error"]["DisagreeRejectTargetIndex"]=str(e)
                #Default value for Disagree-Reject Target Index function
                DRT=[(x,'0.0') for x in  speakers]

            try:
                TDT=self.TopicalDisagreementTargetIndex()
            except Exception as e:
                result["error"]["TopicalDisagreementTargetIndex"]=str(e)
                #Default value for Topical Disagreement Target Index function
                TDT=[(x,'0.0') for x in  speakers]

            
            #Storage the results of the tension focus for each speaker 
            for y,z in zip(DRT,TDT):
                #Storage the functions results
                result["speakers"][y[0]]["DisagreeRejectTargetIndex"]=y[1]
                result["speakers"][z[0]]["TopicalDisagreementTargetIndex"]=z[1]

            #Calculate the tension focus average for each speaker
            for speaker in result["speakers"]:
                functions=[function for function in result["speakers"][speaker]]
                average = round(np.average([float(result["speakers"][speaker][function]) for function in functions], 
                    weights=weights),3)
                #Storage the average tension focus
                result["speakers"][speaker]["averageTensionFocus"]=str(average)
            #Return the JSON response              
            return result 
        except Exception as e:
            #Handle overall exception
            result["error"]["TensionFocusFunctions"]=str(e)
            #Return the JSON response
            return result
