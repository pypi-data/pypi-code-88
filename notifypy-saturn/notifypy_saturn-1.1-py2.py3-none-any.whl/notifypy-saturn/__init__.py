import requests

URL = "not.acumendev.xyz"
BASE_URL = "https://not.acumendev.xyz"

class Notify:

    def __init__(self, secret, tls):

        self.secret = secret
        self.tls = tls

    #method to create a new document
    def create_doc(self, name):
        # defining a params dict for the parameters to be sent to the API
        DATA = {'name':name}
        HEADERS = {'content-type': 'application/json', 'x-api-key': self.secret}
        
        # sending post request and saving the response as response object
        r = requests.post(url = BASE_URL+"/api/v1/document", data=DATA, headers=HEADERS)
        
        # extracting data in json format
        data = r.json()

        #return data
        return data
    
    #method to create a new conversation
    def create_convo(self, name, sender_id, receiver_id, receiver_name, secret):
        # defining a params dict for the parameters to be sent to the API
        DATA = {'sender_name':name, 'sender_id': sender_id, 'receiver_id': receiver_id, 'receiver_name': receiver_name}
        HEADERS = {'content-type': 'application/json', 'x-api-key': self.secret}
        
        # sending post request and saving the response as response object
        r = requests.post(url = BASE_URL+"/api/v1/conversation", data=DATA, headers=HEADERS)
        
        # extracting data in json format
        data = r.json()

        #return data
        return data

    #method to get a document
    def get_doc(self, name, secret):
        # defining a params dict for the parameters to be sent to the API
        HEADERS = {'content-type': 'application/json', 'x-api-key': self.secret}
        
        # sending get request and saving the response as response object
        r = requests.get(url = BASE_URL+"/api/v1/document"+name, headers=HEADERS)
        
        # extracting data in json format
        data = r.json()

        #return data
        return data
    
    #method to get a document
    def get_convo_messages(self, id, secret):
        # defining a params dict for the parameters to be sent to the API
        HEADERS = {'content-type': 'application/json', 'x-api-key': self.secret}
        
        # sending get request and saving the response as response object
        r = requests.get(url = BASE_URL+"/api/v1/conversation/messages/"+id, headers=HEADERS)
        
        # extracting data in json format
        data = r.json()

        #return data
        return data



    
  
