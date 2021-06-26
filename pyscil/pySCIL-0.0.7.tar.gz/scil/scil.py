# Defines SCIL class
import json

# import from services
from .services import *

# inherit functions from subclasses
class SCIL(_preprocessing.Preprocessing, _topicControl.TopicControl, _taskControl.TaskControl, 
    _agreement.Agreement, _disagreement.Disagreement, _argumentDiversity.ArgumentDiversity, 
    _involvement.Involvement, _networkCentrality.NetworkCentrality, _emotiveLanguageUse.EmotiveLanguageUse, 
    _sociability.Sociability, _tensionFocus.TensionFocus, _taskFocus.TaskFocus, 
    _topicalPositioning.TopicalPositioning, _socialPositioning.SocialPositioning, _socialRoles.SocialRoles):
    
    def __init__(self, jData, pTags=None, aTags=None, n=None, t=None, mt=None):

        self.jsonData = self.addJsonData(jData)

        self.posTags = pTags
        self.allTags = aTags
        self.nouns = n
        self.topics = t
        self.mesoTopics = mt

    # perform Stanford preprocessing on json
    def preprocessStanford(self, topicThreshold=2, mesoTopicThreshold=10):
        self.stanfordPoSTagger()
        self.NounPosTagsStanford(topicThreshold, mesoTopicThreshold)

    # perform NLTK preprocessing on json
    def preprocessNLTK(self, topicThreshold=2, mesoTopicThreshold=10):
        self.NLTKPoSTagger()
        self.NounPosTagsNLTK(topicThreshold, mesoTopicThreshold)

    # takes a json file and returns a dictionary
    def addJsonData(self, data):
        temp = json.load(data)

        # do some preprocessing on json data
        # to lowercase, removing leading hyphens, etc
        for turn in temp['turns']:
            metaTag, tag = (turn["dialog_act"].split(':') if ":" in turn["dialog_act"] else ("",turn["dialog_act"])) if turn["dialog_act"] != '' else ("","")
            metaTag = metaTag.lower()
            tag = tag.strip('-').lower()
            turn['metaTag'] = metaTag
            turn['tag'] = tag
            turn['speaker'] = turn['speaker'].lower()
            turn['polarity'] = turn['polarity'].lower()
            turn['topic'] = turn['topic'].lower()
            turn['link_to'] = turn['link_to'].lower()
            turn['comm_act_type'] = turn['comm_act_type'].lower()

        return temp

