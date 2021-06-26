# pelion_sage_controller_api.py

# Requirements
import requests
import json
import base64
import uuid
import time

#
# AWS Sagemaker Edge Agent via Pelion controller API
#
class ControllerAPI:
    # Constructor
    def __init__(self, api_key, gw_device_id, api_endpoint = 'api.us-east-1.mbedcloud.com'):
        # To Do: Lets keep the API Key as protected as possible... 
        self.pelion_api_key = api_key

        # We could make the Pelion Edge Sagemaker Edge Agent Device ID variable as well...
        self.pelion_sagemaker_agent_device_id = gw_device_id
        
        # Pelion Edge Sagemaker Edge Agent Device surfaces out these two LWM2M resources
        self.pelion_rpc_request_lwmwm_uri = '/33311/0/5701'
        self.pelion_config_lwm2m_uri = '/33311/0/5702'
        self.pelion_cmd_status_lwm2m_uri = '/33311/0/5702'

        # Standard Pelion Northbound API plumbing with our selected device ID from above...
        self.pelion_api_endpoint = api_endpoint
        self.pelion_request_headers = {'Authorization':'Bearer ' + self.pelion_api_key, 'content-type':'application/json' }
        self.pelion_long_poll_url = 'https://' + self.pelion_api_endpoint + '/v2/notification/pull'
        self.pelion_url = 'https://' + self.pelion_api_endpoint + '/v2/device-requests/' + self.pelion_sagemaker_agent_device_id + '?async-id='

    # Pelion DeviceRequests Dispatch (internal)
    def __pelion_device_request_dispatch(self,req_id, verb, uri, json_data):
        pelion_b64_payload = ''
        if json_data != '':
            pelion_b64_payload = base64.b64encode(json.dumps(json_data).encode('utf-8')).decode('utf-8')

        # Pelion Dispatch Command
        pelion_device_requests_cmd = { "method": verb, "uri": uri }
        if pelion_b64_payload != '':
            pelion_device_requests_cmd["payload-b64"] = pelion_b64_payload

        # Make the call to invoke the command...
        pelion_cmd_response = requests.post(self.pelion_url + req_id, data=json.dumps(pelion_device_requests_cmd), headers=self.pelion_request_headers)
        print('DeviceRequest: ' + self.pelion_url + " Data: " + str(pelion_device_requests_cmd) + " Status Code: " + str(pelion_cmd_response.status_code))

        # Now Long Poll to get the command dispatch response..
        DoPoll = True
        pelion_command_response = {}
        while DoPoll:
            long_poll_responses = requests.get(self.pelion_long_poll_url, headers=self.pelion_request_headers)
            responses_json = json.loads(long_poll_responses.text)
            if 'async-responses' in responses_json:
                for response in responses_json['async-responses']:
                    if response['id'] == req_id:
                        pelion_command_response = ''
                        if 'payload' in response:
                            if response['payload'] != '':
                                pelion_command_response = json.loads(base64.b64decode(response['payload']))
                        DoPoll = False
            time.sleep(1)
        return pelion_command_response

    # Pelion LWM2M Value Request (internal)
    def __pelion_get(self,req_id, uri):
        return self.__pelion_device_request_dispatch(req_id, 'GET', uri, '')

    # Pelion LWM2M POST Execute (internal)
    def __pelion_post(self,req_id, uri, json_data):
        return self.__pelion_device_request_dispatch(req_id, 'POST', uri, json_data)

    # Pelion LWM2M PUT Operation (internal)
    def __pelion_put(self,req_id, uri, json_data):
        return self.__pelion_device_request_dispatch(req_id, 'PUT', uri, json_data)

    # Get the last value of our LWM2M RPC Interface
    def pelion_last_cmd_result(self):
        req_id = str(uuid.uuid4())
        return self.__pelion_get(req_id,self.pelion_rpc_request_lwmwm_uri)

    #
    # Configuration API
    #
    
    # Get Configuration
    def pelion_get_config(self):
        req_id = str(uuid.uuid4())
        return self.__pelion_get(req_id,self.pelion_config_lwm2m_uri)

    # Set Configuration
    def pelion_set_config(self,key,value):
        req_id = str(uuid.uuid4())
        config_update = {"jsonrpc":"2.0","id":req_id,"config":{}}
        config_update['config'][key] = value
        self.__pelion_put(req_id,self.pelion_config_lwm2m_uri,config_update)
        return self.pelion_get_config()

    #
    # Sagemaker Controls
    # These commands need to conform to the JsonRPC format presented in SageMakerEdgeAgentContainer/sagemaker-agent-pt.js
    #
    
    # Is dispatched command running?
    def pelion_cmd_is_running(self,command):
        req_id = str(uuid.uuid4())
        status = self.__pelion_get(req_id,self.pelion_cmd_status_lwm2m_uri)
        print("Command Dict: " + str(status) + " Status: " + status[command])
        if command in status:
            print("command is in status")
            if status[command] == 'running':
                print(" Status: " + status[command] + " is RUNNING")
                return True
        print(" Status: " + status[command] + " is RUNNING")
        return False
    
    # Is dispatch command in error?
    def pelion_cmd_in_error(self,command):
        req_id = str(uuid.uuid4())
        status = self.__pelion_get(req_id,self.pelion_cmd_status_lwm2m_uri)
        print("Command Dict: " + str(status) + " Status: " + status[command])
        if command in status:
            if status[command] == 'error':
                return True
        return False
    
    # ListModels
    def pelion_list_models(self):
        req_id = str(uuid.uuid4())
        self.__pelion_post(req_id, self.pelion_rpc_request_lwmwm_uri, {"jsonrpc":"2.0","id":req_id,"method":"listModels"})
        return self.pelion_last_cmd_result()

    # LoadModel
    def pelion_load_model(self,model_name,s3_filename):
        req_id = str(uuid.uuid4())
        self.__pelion_post(req_id,self.pelion_rpc_request_lwmwm_uri, {"jsonrpc":"2.0","id":req_id,"method":"loadModel","params":{"name":model_name,"s3_filename":s3_filename}})
        return self.pelion_last_cmd_result()

    # UnloadModel
    def pelion_unload_model(self,model_name):
        req_id = str(uuid.uuid4())
        self.__pelion_post(req_id,self.pelion_rpc_request_lwmwm_uri, {"jsonrpc":"2.0","id":req_id,"method":"unloadModel","params":{"name":model_name}})
        return self.pelion_last_cmd_result()
    
    # ReloadModel
    def pelion_reload_model(self,model_name,s3_filename):
        req_id = str(uuid.uuid4())
        self.__pelion_post(req_id,self.pelion_rpc_request_lwmwm_uri, {"jsonrpc":"2.0","id":req_id,"method":"reloadModel","params":{"name":model_name,"s3_filename":s3_filename}})
        return self.pelion_last_cmd_result()

    # Predict
    def pelion_predict(self,model_name,input_data_url,output_url):
        req_id = str(uuid.uuid4())
        self.__pelion_post(req_id,self.pelion_rpc_request_lwmwm_uri,{"jsonrpc":"2.0","id":req_id,"method":"predict","params":{"model_name":model_name,"input_data_url":input_data_url,"output_url":output_url}})
        return self.pelion_last_cmd_result()