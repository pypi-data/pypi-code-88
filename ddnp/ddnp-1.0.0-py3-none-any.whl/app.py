'''
COPYRIGHT:
Copyright (c) 2015-2019, California Institute of Technology ("Caltech").
U.S. Government sponsorship acknowledged.
All rights reserved.

LICENSE:
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
- Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.
- Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.
- Neither the name of Caltech nor its operating division, the Jet
Propulsion Laboratory, nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior
written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.

NTR:
'''

import ddnp.env
import ddnp.vol
import flask

THIS = flask.Flask(__name__)

@THIS.route ('/env', methods=['GET', 'PUT'])
def env()->str:
    '''endpoint /env'''
    try:
        if flask.request.method == 'GET':
            return ddnp.env.get(flask.request.args)
        if flask.request.method == 'PUT':
            return ddnp.env.put(flask.request.args)
    except KeyError: flask.abort (422)
    return 'method was neither GET nor PUT'

@THIS.route ('/file', methods=['GET', 'PUT'])
def file()->str:
    '''endpoint /file'''
    try:
        if flask.request.method == 'GET':
            return ddnp.vol.get(flask.request.args)
        if flask.request.method == 'PUT':
            return ddnp.vol.put(flask.request.files, flask.request.args)
    except FileNotFoundError: flask.abort (404)
    except KeyError: flask.abort (422)
    return 'method was neither GET nor PUT'

@THIS.route ('/ids', methods=['GET'])
def ids()->str:
    '''endpoint /ids'''
    if flask.request.method == 'GET': return ddnp.vol.ids(flask.request.args)
    return 'method was not a GET'

def run (debug:bool, hostname:str, port:int)->None:
    '''run the server'''
    THIS.run (debug=debug, host=hostname, port=port)
    return

@THIS.route ('/tar', methods=['GET', 'PUT'])
def tar()->str:
    '''endpoint /tar'''
    try:
        if flask.request.method == 'GET':
            return ddnp.vol.tar(flask.request.args)
        if flask.request.method == 'PUT':
            return ddnp.vol.untar(flask.request.files,flask.request.args)
    except KeyError: flask.abort (422)
    return 'method was neither GET nor PUT'
