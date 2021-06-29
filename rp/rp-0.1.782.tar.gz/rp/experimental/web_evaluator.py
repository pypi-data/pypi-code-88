import socket
import json
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

import rp

DEFAULT_SERVER_PORT = 25893

class Evaluation:
    def __init__(self,code:str):
        self.code=code
        try:
            self.value=eval(self.code)
        except KeyboardInterrupt:
            raise
        except BaseException as error:
            self.error=error
            
    @property
    def failed(self):
        return hasattr(self,'error')
    @property
    def succeeded(self):
        return not self.failed
    
    def encode(self):
        return rp.object_to_bytes(self)
    
    def __repr__(self):
        return '<Evaluation: fail=%s>'%self.failed

class _Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/octet-stream")
        self.end_headers()
        body=self.get_request_body()
        data=json.loads(body)
        code=data['code']
        print("CODE: "+code)
        evaluation=Evaluation(code)
        response=evaluation.encode()
        self.wfile.write(response)
        
    def get_request_body(self):
        length=int(self.headers.get('Content-Length'))
        body = self.rfile.read(length)
        return body

def run_server(server_port=None):
    if server_port is None:
        server_port = DEFAULT_SERVER_PORT

    host_name = "0.0.0.0"
    webServer = HTTPServer((host_name, server_port), _Handler)
    print("Server started at http://%s:%s" % (rp.get_my_local_ip_address(), server_port))

    try:
        webServer.serve_forever()
    finally:
        webServer.server_close()

    print("Server stopped.")

class Client:
    def __init__(self,server_name:str,server_port:int=None):
        #server_name is like "127.0.1.33" or like "glass.local"
        self.server_name=server_name
        self.server_port = DEFAULT_SERVER_PORT if server_port is None else server_port
        self.server_url='http://%s:%i'%(self.server_name,self.server_port)

    def evaluate(self,code:str):
        response=requests.request('GET',self.server_url,json={'code':code})
        result=rp.bytes_to_object(response.content)
        # assert isinstance(result,Evaluation),'Bad response...make sure the server and client are running on the same version of python with the same library versions'
        return result

if __name__=='__main__':
    if rp.input_yes_no("Is this the server or the client? Yes means this is the server."):
        print("Running the server.")
        run_server()
    else:
        print("Running the client.")
        client=Client(input("Enter the server's IP: "))
        while True:
            print(client.evaluate(input(" >>> ")))
