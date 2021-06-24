# Python edgegrid module
""" Copyright 2015 Akamai Technologies, Inc. All Rights Reserved.

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.

 You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""
import sys
import os
import requests
import logging
import json
from akamai.edgegrid import EdgeGridAuth, EdgeRc
from .http_calls import EdgeGridHttpCaller
if sys.version_info[0] >= 3:
    # python3
    from urllib import parse
else:
    # python2.7
    import urlparse as parse

logger = logging.getLogger(__name__)

#edgerc = EdgeRc('/Users/apadmana/.edgerc')
section = 'default'
debug = False
verbose = False
#baseurl_prd = 'https://%s' % edgerc.get(section, 'host')
#session = requests.Session()
#session.auth = EdgeGridAuth.from_edgerc(edgerc, section)
#session.headers.update({'User-Agent': "AkamaiCLI"})
#prdHttpCaller = EdgeGridHttpCaller(session, debug, verbose, baseurl_prd)



class AkamaiProperty():
    def __init__(self,edgercLocation,name, accountSwitchKey=None):
        self.name = name
        self.contractId = ''
        self.groupId = ''
        self.propertyId = ''
        self.stagingVersion = 0
        self.productionVersion = 0
        self.accountSwitchKey = ''
        self._edgerc = ''
        self._prdHttpCaller = ''
        self._session = ''
        self._baseurl_prd = ''
        self._host = ''
        self._invalidconfig = False
        self._criteria_stack = []
        self._condition_json = []
        self._condition_json1 = []

        self._edgerc = EdgeRc(edgercLocation)
        self._host = self._edgerc.get(section, 'host')
        self._baseurl_prd = 'https://%s' %self._host
        self._session = requests.Session()
        self._session.auth = EdgeGridAuth.from_edgerc(self._edgerc, section)
        self._session.headers.update({'User-Agent': "AkamaiCLI"})
        self._prdHttpCaller = EdgeGridHttpCaller(self._session, debug, verbose, self._baseurl_prd)

        data = {}
        data['propertyName'] = name
        json_data = json.dumps(data)
        propertyInfoEndPoint = "/papi/v1/search/find-by-value"
        if accountSwitchKey:
            self.accountSwitchKey = accountSwitchKey
            params = {'accountSwitchKey':accountSwitchKey}
            status,prop_info = self._prdHttpCaller.postResult(propertyInfoEndPoint,json_data,params)
        else:
            status,prop_info = self._prdHttpCaller.postResult(propertyInfoEndPoint,json_data)
        if prop_info:
            if 'versions' in prop_info and 'items' in prop_info['versions'] and len(prop_info['versions']['items']) !=0:
                self.propertyId = prop_info['versions']['items'][0]['propertyId']
                self.contractId = prop_info['versions']['items'][0]['contractId']
                self.groupId = prop_info['versions']['items'][0]['groupId']
                for item in prop_info['versions']['items']:
                    if item["productionStatus"] == "ACTIVE":
                        self.productionVersion = item["propertyVersion"]
                    if item["stagingStatus"] == "ACTIVE":
                        self.stagingVersion = item["propertyVersion"]
            else:
                print("No Configuration with {} Found".format(name))
                self._invalidconfig = True
        return None


    def printPropertyInfo(self):
        print("Hello")
        if self._invalidconfig == True:
            print("No Configuration Found")
            return
        print("Property Name:",self.name)
        print("Property Id:",self.propertyId)
        print("Contract Id:",self.contractId)
        print("Group Id:",self.groupId)
        print("Active Staging Version:",self.stagingVersion)
        print("Active Production Version:",self.productionVersion)

    def getStagingVersion(self):
        if self._invalidconfig == True:
            print("No Configuration Found")
            return -1
        return self.stagingVersion

    def getProductionVersion(self):
        if self._invalidconfig == True:
            print("No Configuration Found")
            return -1
        return self.productionVersion

    def getRuleTree(self,version):
        if self._invalidconfig == True:
            print("No Configuration Found")
            return []
        ruleTreeEndPoint = "/papi/v1/properties/" + self.propertyId + "/versions/" +str(version) + "/rules"
        params =    {
                    'validateRules': 'false',
                    'validateMode': 'false',
                    'dryRun': 'true'
                    }
        if self.accountSwitchKey:
            params["accountSwitchKey"] = self.accountSwitchKey

        ruleTree = self._prdHttpCaller.getResult(ruleTreeEndPoint,params)
        return ruleTree

    def updateRuleTree(self,version,jsondata):
        if self._invalidconfig == True:
            print("No Configuration Found")
            return False
        updateRuleTreeEndPoint = '/papi/v1/properties/' + self.propertyId + '/versions/' + str(version) + '/rules'
        params =    {
                    'contractId': self.contractId,
                    'groupId': self.groupId
                    }
        if self.accountSwitchKey:
            params["accountSwitchKey"] = self.accountSwitchKey

        status,updateRuleTree = self._prdHttpCaller.putResult(updateRuleTreeEndPoint,jsondata,params)
        print(status)
        if status == 200:
            return True
        else:
            return False

    def getHostnames(self,version):
        if self._invalidconfig == True:
            print("No Configuration Found")
            return []
        getHostNameEndPoint = '/papi/v1/properties/{property_id}/versions/{new_version}/hostnames'.format(property_id=self.propertyId ,new_version=version)
        params = {}
        params["contractId"] =self.contractId
        params["groupId"] = self.groupId

        if self.accountSwitchKey:
            params["accountSwitchKey"] = self.accountSwitchKey

        getHostnameJson = self._prdHttpCaller.getResult(getHostNameEndPoint,params)
        hostNameList = []
        for hostname in  getHostnameJson["hostnames"]["items"]:
            hostNameList.append(hostname["cnameFrom"])
        return hostNameList


    def createVersion(self,baseVersion):
        if self._invalidconfig == True:
            print("No Configuration Found")
            return -1
        versionCreateEndPoint = '/papi/v1/properties/' + self.propertyId + '/versions/'

        data = {}
        data['createFromVersion'] = str(baseVersion)
        json_data = json.dumps(data)

        if self.accountSwitchKey:
            params = {'accountSwitchKey':self.accountSwitchKey}
            version_info = self._prdHttpCaller.postResult(versionCreateEndPoint,json_data,params)
        else:
            version_info = self._prdHttpCaller.postResult(versionCreateEndPoint,json_data)

        if version_info[0] == 201:
            version_link = version_info['versionLink']
            start_index = version_link.find('/versions')+10
            end_index = version_link.find('?')
            return version_link[start_index:end_index]
        else:
            return 0

    def activateStaging(self,version,notes,email_list):
        if self._invalidconfig == True:
            print("No Configuration Found")
            return False
        activationEndPoint = '/papi/v1/properties/' + self.propertyId + '/activations'

        data = {}
        data['propertyVersion'] = int(version)
        data['network'] = 'STAGING'
        data['note'] = notes
        data['acknowledgeAllWarnings'] = True
        data['notifyEmails'] = email_list
        data['fastPush'] = True
        data['useFastFallback'] = False

        json_data = json.dumps(data)

        if self.accountSwitchKey:
            params = {'accountSwitchKey':self.accountSwitchKey}
            version_info = self._prdHttpCaller.postResult(activationEndPoint,json_data,params)
        else:
            version_info = self._prdHttpCaller.postResult(activationEndPoint,json_data)

        if version_info:
            return True
        else:
            return False

    def activateProduction(self,version,notes,email_list,peer_review_email,customer_email):
        if self._invalidconfig == True:
            print("No Configuration Found")
            return False
        activationEndPoint = '/papi/v1/properties/' + self.propertyId + '/activations'

        data = {}
        data['propertyVersion'] = int(version)
        data['network'] = 'PRODUCTION'
        data['note'] = notes
        data['acknowledgeAllWarnings'] = True
        data['notifyEmails'] = email_list
        data['fastPush'] = True
        data['useFastFallback'] = False

        complianceRecord = {}
        complianceRecord['noncomplianceReason'] = "NONE"
        complianceRecord['peerReviewedBy'] = peer_review_email
        complianceRecord['unitTested'] = True
        complianceRecord['customerEmail'] = customer_email
        data['complianceRecord'] = complianceRecord

        json_data = json.dumps(data)

        if self.accountSwitchKey:
            params = {'accountSwitchKey':self.accountSwitchKey}
            version_info = self._prdHttpCaller.postResult(activationEndPoint,json_data,params)
        else:
            version_info = self._prdHttpCaller.postResult(activationEndPoint,json_data)

        if version_info:
            return True
        else:
            return False

    def __parseChildCriteriaBehaviors(self,rule_list,level=0):
        if len(rule_list) == 0:
            return
        for rule in reversed(rule_list):
            criteria_dict = {}
            criteria_dict['criteria'] = rule['criteria']
            criteria_dict['condition'] = rule['criteriaMustSatisfy']
            self._criteria_stack.append(criteria_dict)
            self.__parseChildCriteriaBehaviors(rule['children'],level+1)
            for behavior in rule['behaviors']:
                condition_dict = {}
                condition_dict['behavior'] = behavior
                condition_dict['criteria'] = self._criteria_stack.copy()
                self._condition_json.insert(0,condition_dict)
            temp = self._criteria_stack.pop()

    def _getBehaviorParsedList(self,version):
        if self._invalidconfig == True:
            print("No Configuration Found")
            return []
        self._criteria_stack = []
        self._condition_json = []
        self._condition_json1 = []

        ruleTree = self.getRuleTree(int(version))

        for default_behaviors in ruleTree['rules']['behaviors']:
            criteria_dict = {}
            criteria_dict['criteria'] = []
            criteria_dict['condition'] = 'all'

            condition_dict1 = {}
            condition_dict1['behavior'] = default_behaviors
            condition_dict1['criteria'] = criteria_dict
            self._condition_json1.append(condition_dict1)

        self.__parseChildCriteriaBehaviors(ruleTree['rules']['children'])

        behaviorParsedList = self._condition_json1 + self._condition_json
        return behaviorParsedList

    
    def getAvailableFeatures(self,version):
        if self._invalidconfig == True:
            print("No Configuration Found")
            return []

        behaviorList = []
        getAvailableFeaturesEndPoint = "/papi/v1/properties/{propertyId}/versions/{propertyVersion}/available-behaviors".format(propertyId=self.propertyId,propertyVersion=version)
        params = {}
        if self.accountSwitchKey:
            params["accountSwitchKey"] = self.accountSwitchKey
            getFeaturesjson = self._prdHttpCaller.getResult(getAvailableFeaturesEndPoint,params)
        else:
            getFeaturesjson = self._prdHttpCaller.getResult(getAvailableFeaturesEndPoint)
        for behaviors in getFeaturesjson["behaviors"]["items"]:
            behaviorList.append(behaviors["name"])
        return behaviorList

    def getUnusedBehaviors(self,version):
        if self._invalidconfig == True:
            print("No Configuration Found")
            return []
        
        availableFeatures = self.getAvailableFeatures(version)
        usedBehaviors = self.getUsedBehaviors(version)
        unusedBehaviors = list(set(availableFeatures) - set(usedBehaviors))
        return unusedBehaviors
    
    def getHostnames(self,version):
        if self._invalidconfig == True:
            print("No Configuration Found")
            return []

        hostnameList = []
        getHostNameEndPoint = "/papi/v1/properties/{propertyId}/versions/{propertyVersion}/hostnames-behaviors".format(propertyId=self.propertyId,propertyVersion=version)
        params = {}
        if self.accountSwitchKey:
            params["accountSwitchKey"] = self.accountSwitchKey
            getHostnameJson = self._prdHttpCaller.getResult(getHostNameEndPoint,params)
        else:
            getHostnameJson = self._prdHttpCaller.getResult(getHostNameEndPoint)
        
        for hostname in getHostnameJson["hostnames"]["items"]:
            hostnameList.append(hostname["cnameType"])
        return hostnameList

    def getSiteShieldMap(self,version):
        if self._invalidconfig == True:
            print("No Configuration Found")
            return []
        behaviorParsedList = self._getBehaviorParsedList(version)
        sslist = []
        for behavior in behaviorParsedList:
            if behavior["behavior"]["name"] == 'siteShield':
                sslist.append(behavior["behavior"]["options"]['ssmap']['value'])
        sslist = list(dict.fromkeys(sslist))
        return sslist


    def getSureRouteCustomMaps(self,version):
        if self._invalidconfig == True:
            print("No Configuration Found")
            return []
        behaviorParsedList = self._getBehaviorParsedList(version)
        srlist = []
        for behavior in behaviorParsedList:
            if behavior["behavior"]["name"] == 'sureRoute':
                if behavior["behavior"]["options"]['type'] == 'CUSTOM_MAP': 
                    srlist.append(behavior["behavior"]["options"]['customMap'])
        srlist = list(dict.fromkeys(srlist))
        return srlist

    def getUsedBehaviors(self,version):
        if self._invalidconfig == True:
            print("No Configuration Found")
            return []
        behaviorParsedList = self._getBehaviorParsedList(version)
        behaviorList = []
        for behavior in behaviorParsedList:
            behaviorList.append(behavior["behavior"]["name"])
        behaviorList = list(dict.fromkeys(behaviorList))
        return behaviorList

    def getOrigins(self,version):
        if self._invalidconfig == True:
            print("No Configuration Found")
            return []
        behaviorParsedList = self._getBehaviorParsedList(version)
        originlist = []
        for behavior in behaviorParsedList:
            if behavior["behavior"]["name"] == 'origin':
                originlist.append(behavior["behavior"]["options"]['hostname'])
        originlist = list(dict.fromkeys(originlist))
        return originlist

    def getCPCodes(self,version):
        if self._invalidconfig == True:
            print("No Configuration Found")
            return []
        behaviorParsedList = self._getBehaviorParsedList(version)
        cpCodeList = []
        for behavior in behaviorParsedList:
            if behavior["behavior"]["name"] == 'cpCode':
                cpCodeList.append(behavior["behavior"]["options"]['value']['id'])
        cpCodeList = list(dict.fromkeys(cpCodeList))
        return cpCodeList


class AkamaiPropertyManager():
    def __init__(self,edgercLocation,accountSwitchKey=None):
        self.accountSwitchKey = ''
        self._edgerc = ''
        self._prdHttpCaller = ''
        self._session = ''
        self._baseurl_prd = ''
        self._host = ''
        self._edgerc = EdgeRc(edgercLocation)
        self._host = self._edgerc.get(section, 'host')
        self._baseurl_prd = 'https://%s' %self._host
        self._session = requests.Session()
        self._session.auth = EdgeGridAuth.from_edgerc(self._edgerc, section)
        self._session.headers.update({'User-Agent': "AkamaiCLI"})
        self._prdHttpCaller = EdgeGridHttpCaller(self._session, debug, verbose, self._baseurl_prd)

    def getGroups(self):
        groupsList = []
        ep = "/papi/v1/groups"
        params = {}
        if self.accountSwitchKey:
            params["accountSwitchKey"] = self.accountSwitchKey
            getgroupJson = self._prdHttpCaller.getResult(ep,params)
        else:
            getgroupJson = self._prdHttpCaller.getResult(ep)
        for items in getgroupJson["groups"]["items"]:
            groupsList.append(items["groupId"])
        return groupsList

    def getContracts(self):
        contractsList = []
        ep = "/papi/v1/contracts"
        params = {}
        if self.accountSwitchKey:
            params["accountSwitchKey"] = self.accountSwitchKey
            getcontractJson = self._prdHttpCaller.getResult(ep,params)
        else:
            getcontractJson = self._prdHttpCaller.getResult(ep)
        for items in getcontractJson["contracts"]["items"]:
            contractsList.append(items["contractId"])
        return contractsList

    def listCPCodes(self,contract_id,group_id):
        cpCodeList = []
        ep = '/papi/v1/cpcodes'
        params = {}
        params['contractId'] = contract_id
        params['groupId'] = group_id
        if self.accountSwitchKey:
            params["accountSwitchKey"] = self.accountSwitchKey

        getcpCodesJson = self._prdHttpCaller.getResult(ep,parameters=params)
        print(getcpCodesJson)
        for items in getcpCodesJson["cpcodes"]["items"]:
            cpCodeList.append(items["cpcodeId"])

    def getPropertiesofGroup(self,contractid,groupid):
        ep = '/papi/v1/properties'
        params = {}
        params['contractId'] = contractid
        params['groupId'] = groupid
        if self.accountSwitchKey:
            params["accountSwitchKey"] = self.accountSwitchKey

        getpropertiesJson = self._prdHttpCaller.getResult(ep,parameters=params)
        
        propList = []
        if len(getpropertiesJson['properties']['items']) != 0:
            for prop in getpropertiesJson['properties']['items']:
                propList.append(prop['propertyName'])

        return propList

    def getallProperties(self):
        propertylist = []
        groupIds = self.getGroups()
        contractIds = self.getContracts()
        for grp in groupIds:
            for ctr in contractIds:
                property_list = self.getPropertiesofGroup(ctr,grp)
                if len(property_list) != 0:
                    for x in propertylist:
                        propertylist.append(x)
        return propertylist