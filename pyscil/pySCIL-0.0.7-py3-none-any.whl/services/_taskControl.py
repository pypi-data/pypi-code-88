#Import Json elements to encode Python data structures
import json
#Import functions to deal with text
import re, string, unicodedata
#Import nartural language processing functions
import nltk
#Import mathematical functions
import numpy as np

class TaskControl(object):

    """
    One measure of task control is the number of directives (done as statements or questions) made by 
    each participant as a percentage of all directives in discourse.

    DirectiveIndex = #speakerDirectives/#allDirectives
    """
    #output: List
    def DirectiveIndex(self):
        result = []
        directives = []
        directivesUsers = {}

        for turn in self.jsonData['turns']:
            if turn["speaker"] not in directivesUsers:
                directivesUsers[turn["speaker"]] = []
            
            # if tag is "action-directive" or "offer-commit" or "information-request"
            tag = turn["tag"]
            if tag == "action-directive" or tag == "offer-commit" or tag == "information-request":
                directives.append(turn["text"])

                #Save all directives for each user
                directivesUsers[turn["speaker"]].append(turn["text"])

        # for each user, calculate their DI
        for user in directivesUsers:
            # if there are no directives in the dialogue, set DI 0
            if len(directives) != 0:
                result.append((user,str(round(len(directivesUsers[user])*1.0/len(directives),3))))
            else:
                result.append((user,str(0.0)))

        return result

    """
    Another measure of task control is the total number of turns a participant
    explicitly address the problem solving process or the procedure of how to go about solving the task.
    Such participant attemps to control the way that the group is performing the task.

    ProcessManagementIndex = AmountProcessManagementUtteranceForUser/TotalAmountProcessManagementUtterance
    """
    #output: List
    def ProcessManagementIndex(self):
        result = []
        #Counts how many process management utterances in whole dialog
        totalCount = 0
        processManagementUsers = {}

        for turn in self.jsonData['turns']:
            if turn["speaker"] not in processManagementUsers:
                processManagementUsers[turn["speaker"]] = 0

            #if metaTag "task-mgmt" or "prcs-mgmt"
            metaTag = turn["metaTag"]
            if metaTag == "task-mgmt" or metaTag == "prcs-mgmt":
                totalCount += 1
            
                #Increase process management utterance for given user
                processManagementUsers[turn["speaker"]] += 1

        #Likely just get number for each person
        #Also add 1 to total
        #Return the percentage value

        for user in processManagementUsers:
            #Each user value is the percentage of unique words used in relation to all words in the conversation
            if totalCount == 0:
                result.append((user,str(0.0)))
            else:
                result.append((user,str(round(processManagementUsers[user]*1.0/totalCount,3))))

        return result

    """
    Another measure of task control measures the success of a speaker's directives, offers, and process
    management utterances. A speaker with utterances mostly met by consent or approval by other participants
    has a high degree of task control while one whos suggestions, directives, and offers tend to be
    rejected or dismissed by others have a low degree of task control in the discourse.

    ProcessManagementSuccessIndex = PMI score +1 for each consent or approval and -1 for each rejection or disapproval/#ProcessManagementUterrances
    """
    #output: List
    def ProcessManagementSuccessIndex(self):
        result = []

        totalCount = 0
        processManagementSuccessUsers = {}

        pm_turns = []

        for turn in self.jsonData['turns']:
            if turn["speaker"] not in processManagementSuccessUsers:
                processManagementSuccessUsers[turn["speaker"]] = 0

            # CALCULATE PMI
            # if metaTag "task-mgmt" or "prcs-mgmt" AND tag "assertion-opinion" or "action-directive" or "offer-commit"
            tag = turn["tag"]
            metaTag = turn["metaTag"]
            if ((metaTag == "task-mgmt" or metaTag == "prcs-mgmt") and (tag == "assertion-opinion" or\
                tag == "action-directive" or tag == "offer-commit")):

                # add 1 for being a PM task
                totalCount += 1
                processManagementSuccessUsers[turn["speaker"]] += 1

                # add turn text to pm_turns []
                pm_turns.append(turn)

            # if metaTag "task-mgmt" or "prcs-mgmt"
            if metaTag == "task-mgmt" or metaTag == "prcs-mgmt":
                linkTo = turn["link_to"]
                if linkTo != "all-users" and linkTo != "":
                    citedTurn = linkTo.split(":")[1] if ":" in linkTo else None
                
                    if citedTurn != None:
                        for pm_turn in pm_turns:
                            # if pm_turn matches cited turn
                            if pm_turn["turn_no"] == citedTurn:
                                # add 1 if agree-accept or acknowledge
                                # sub 1 if disagree-reject
                                
                                if tag == "agree-accept" or tag == "acknowledge":
                                    processManagementSuccessUsers[pm_turn["speaker"]] += 1
                                elif tag == "disagree-reject":
                                    processManagementSuccessUsers[pm_turn["speaker"]] -= 1
                        
        # for each speaker calculate pmsi
        for user in processManagementSuccessUsers:
            if totalCount == 0:
                result.append((user,str(0.0)))
            else:
                result.append((user, str(round(processManagementSuccessUsers[user]*1.0/totalCount,3))))
        return result

    # Creates combined scores from all task control functions and weights
    def TaskControlFunctions(self,weights=[1,1,1]):
        result={"speakers":{},"error":{"DirectiveIndex":"",
                                    "ProcessManagementIndex":"",
                                    "ProcessManagementSuccessIndex":"",
                                    "TaskControlFunctions":""}}

        try:
            #Get list of speakers
            speakers=list(set([value["speaker"] for value in self.jsonData["turns"]]))
            #Adequate result structure to the number of speakers
            for speaker in speakers: result["speakers"][speaker]={}

            #Call all the task control functions
            try:
                DI = self.DirectiveIndex()
            except Exception as e:
                result["error"]["DirectiveIndex"]=str(e)
                #Default value for Directive Index function
                DI=[(x,'0.0') for x in  speakers]

            try:    
                PMI = self.ProcessManagementIndex()
            except Exception as e:
                result["error"]["ProcessManagementIndex"]=str(e)
                #Default value for Process Management Index function
                PMI=[(x,'0.0') for x in  speakers]
            
            try:
                PMSI = self.ProcessManagementSuccessIndex()
            except Exception as e:
                result["error"]["ProcessManagementSuccessIndex"]=str(e)
                #Default value for Process Management Success Index function
                PMSI=[(x,'0.0') for x in  speakers]

            #Store the results of the task control for each speaker
            for x,y,z in zip(DI, PMI, PMSI):
                #Store the functions results
                result["speakers"][x[0]]["DirectiveIndex"]=x[1]
                result["speakers"][y[0]]["ProcessManagementIndex"]=y[1]
                result["speakers"][z[0]]["ProcessManagementSuccessIndex"]=z[1]

            #Calculate the task control average for each speaker
            for speaker in result["speakers"]:
                functions = [function for function in result["speakers"][speaker]]
                average = round(np.average([float(result["speakers"][speaker][function]) for function in functions], 
                    weights=weights),3)
                # Store the average task control
                result["speakers"][speaker]["averageTaskControl"]=str(average)
            #Return the JSON response
            return result
        except Exception as e:
            #Handle overall exception
            result["error"]["TaskControlFunctions"]=str(e)
            #Return the JSON response
            return result