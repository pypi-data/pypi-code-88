#Import JSON elements to encode/decode Python data structures
import json
#Import file manipulation function
import codecs
#Import ID creation function
import uuid
#Import pathlib
from pathlib import Path
#Import custom Python file (in the same directory)
from Preprocessing import *


"""
Overall input format

Functions take the folowwing JSON for obtaining topics:

{
    "date": "",
    "turns": [
        {
            "mode": "chat",
            "speaker": "<SPEAKER NAME>",
            "end_time": "<TIMESTAMP>",
            "turn_no": "<TURN NUMBER>",
            "dialog_act": "<DIALOGUE ACT LABEL>",
            "comm_act_type": "<COMMAND ACT LABEL>",
            "link_to": "",
            "pos": "",
            "pos_count": "",
            "pos_origin": "",
            "topic": "",
            "polarity": "<SENTIMENT>",
            "text": "<CURRENT TEXT TURN>"
        },	
	...
    ]
}
"""


"""
Create a json file that includes each dialogue turn and the previuos text-history associated.
It is also returned the current dialogue history

Input: string (JSON filename)
ouput: dictionary (dialogue history)

{
    "turns": [
        {
            "turn": "<T1 CURRENT TURN TEXT>",
            "history": {}
        },
        {
            "turn": "<T2 CURRENT TURN TEXT>",
            "history": {
                "T1": {
                    "turn": "<T1 TURN TEXT>",
                    "topics": [<TOPICS INSTRODUCED IN THE TURN>]
                }
            }
        },
     ...
   ]  
}	
"""
def TopicHistoryFile(jsonFile):
    outputJson={}
    try:
        #Open JSON file
        with codecs.open(jsonFile) as file:
            jsonData = json.load(file)
        outputJson["turns"]=[]
        history=[]
        #Concatenate all utterances into a single list
        cleanUtterances=concatenateCleanUtterances(jsonData["turns"])
        uterrances=concatenateUtterances(jsonData["turns"])  
        #Get all the topics related to each turn
        topics=NounPosTagsStanford(cleanUtterances)
        #Iterate over obtained topics to compile the dialogue history
        for turn, topics in zip(uterrances,topics):
            temp={}
            temp["turn"]=turn
            counter=0
            temp["history"]={}    
            for utterance in history:
                    counter+=1
                    temp["history"]["T"+str(counter)]={}
                    temp["history"]["T"+str(counter)]["turn"]=utterance[0]
                    temp["history"]["T"+str(counter)]["topics"]=utterance[1]
            history.append((turn,topics))
            outputJson["turns"].append(temp)        
        #Save file in the appropriate format (using the same input file name)
        fileName=jsonFile.split(".")
        with codecs.open(fileName[0]+"History"+".json", 'w') as file:
                json.dump(outputJson, file, indent=4)
        return outputJson        
    except Exception as e:
        outputJson={}
        return outputJson



"""
Obtain current topics as well as previous ones associated to each dialogue turn
#Input: dictionary (turn history)

{
  "turn": "<CURRENT TURN TEXT>",
  "history": {
    "T1": {
            "turn": "<PREVIOUS TURN TEXT>",
            "topics": [<TOPICS INSTRODUCED IN THE TURN>]
          }
      ...    
  }
}

#ouput: dictionary (topics detected)
{
    "topics":
    {
 	"T1": [<TOPICS INSTRODUCED IN THE TURN>],
 	"T2": [<TOPICS INSTRODUCED IN THE TURN>] 
 	"T3": [<TOPICS INSTRODUCED IN THE TURN>] 
 	...
    }
}    
"""

def topicHistory(turnHistory):
    outputJson={}
    try:
        outputJson["topics"]={}
        #Obtain current turn topics
        currentTopics=NounPosTagsStanford([normalize(turnHistory["turn"])])
        turnNumber=len(turnHistory["history"])
        #Obtain and compile past turns
        if turnHistory["history"]:
            #Compile past turns-topics (history) in the appropriate format
            for turn in turnHistory["history"]:
                    outputJson["topics"][turn]=turnHistory["history"][turn]["topics"]
        #Compile current turn-topics in the appropriate format            
        outputJson["topics"]["T"+str(turnNumber+1)]=currentTopics[0]
        return outputJson
    except Exception as e:
        outputJson["topics"]={}
        return outputJson

"""
Obtain topics related to each dialogue turn without considering the distance among them

Input: string (JSON name)
ouput: dictionary (topics detected)
{
    "topics":
    {
 	"T1": [<TOPICS INSTRODUCED IN THE TURN>],
 	"T2": [<TOPICS INSTRODUCED IN THE TURN>] 
 	"T3": [<TOPICS INSTRODUCED IN THE TURN>] 
 	...
    }
} 

"""

def topicDetection(jsonFile):
    outputJson={}
    outputJson["topics"]={}
    try:
        #Open JSON file
        with codecs.open(jsonFile) as file:
            jsonData = json.load(file)
        #Concatenate all utterances into a single list
        cleanUtterances=concatenateCleanUtterances(jsonData["turns"])
        #Get all the topics related to each turn
        topics=NounPosTagsStanford(cleanUtterances)
        #Output topics in a concrete format
        turnNumber=0
        for topicList in topics:
            #Save all topics related to each turn
            turnNumber+=1
            outputJson["topics"]["T"+str(turnNumber)]=topicList
        #Return topic list    
        return outputJson   
    except Exception as e:
        outputJson={}
        outputJson["topics"]={}
        return outputJson


"""
Obtain topics related to each dialogue turn considering the distance among them

Input: string (JSON name)
Input: integer (allowed distance among topics)
ouput: dictionary (topics detected)
{
    "topics":
    {
 	"T1": [<TOPICS INSTRODUCED IN THE TURN WITH AN ID>],
 	"T2": [<TOPICS INSTRODUCED IN THE TURN WITH AN ID>] 
 	"T3": [<TOPICS INSTRODUCED IN THE TURN WITH AN ID>] 
 	...
    }
} 

"""

def topicDistance(jsonFile,threshold):
    outputJson={}
    outputJson["topics"]={}
    try:
        distance={}
        #Open JSON file
        with codecs.open(jsonFile) as file:
            jsonData = json.load(file)
        #Concatenate all utterances into a single list
        cleanUtterances=concatenateCleanUtterances(jsonData["turns"])
        #Get all the topics related to each turn
        topicsList=NounPosTagsStanford(cleanUtterances)
        turnNumber=0
        #Iterate topic list to check distance
        for topics in topicsList:
            turnNumber+=1
            for topic in topics:
                if topic not in distance:
                    #Topic first occurrence
                    topicId=uuid.uuid4().hex[:4]
                    distance[topic]=[(turnNumber,topicId)]
                else:
                    #Multiple topic occurences
                    lastTopicOcurrence=distance[topic][-1][0]
                    topicSeparation=abs(turnNumber-lastTopicOcurrence)
                    #Topic in range to the same topic in a previous turn so they are the same
                    if topicSeparation > 0 and topicSeparation <= threshold:
                        lastTopicOcurrenceId=distance[topic][-1][1]
                        distance[topic].append((turnNumber,lastTopicOcurrenceId))
                    #Topic is not in range to the same topic in a previous turn    
                    elif topicSeparation > 0:
                        topicId=uuid.uuid4().hex[:4]
                        distance[topic].append((turnNumber,topicId))                
        #Save topics in the appropiate format
        turnNumber=0                    
        for topics in topicsList:
            turnNumber+=1
            currentTurn="T"+str(turnNumber)
            outputJson["topics"][currentTurn]=[]
            for topic in topics:
                topicElement=[item for item in distance[topic] if item[0] == turnNumber]
                outputJson["topics"][currentTurn].append((topic,topicElement[0][1]))
        #Return topics (distance included)        
        return outputJson        
    except Exception as e:
        outputJson={}
        outputJson["topics"]={}
        return outputJson        

"""
#Testing purposes
#Test TopicHistoryFile and topicHistory functions
testFile=TopicHistoryFile("test1.json")
print(topicHistory(testFile["turns"][9]))
#Test topicDetection function
print(topicDetection("test1.json"))
#Test topicDistance function
print(topicDetection("test2.json"))
"""






