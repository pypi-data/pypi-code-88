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

import argparse
import configparser
import ddnp.env
import ddnp.vol
import os

def _dir (path:str)->str:
    '''determine if the absolute path exists and that it is a directory'''
    path = os.path.abspath (path)

    if not os.path.exists(path):
        raise ValueError('Path "' + path + '" does not exist.')
    if not os.path.isdir(path):
        raise ValueError('Path "' + path + '" is not a directory.')
    return path

def _env (efn:str)->{}:
    '''convert files to dictionaries'''
    if not os.path.exists(efn):
        raise ValueError('File "' + efn + '" does not exist.')
    if not os.path.isfile(efn):
        raise ValueError('File "' + efn + '" is not a regular file.')

    with open (efn, 'rt') as file: content = file.read()
    result = configparser.ConfigParser()
    result.optionxform = str
    try: result.read_string(content)
    except configparser.MissingSectionHeaderError:
        result.read_string ('[GLOBAL]\n' + content)
        pass
    return result

AP = argparse.ArgumentParser()
AP.add_argument ('-d', '--debug', action='store_true', default=False,
                 help='set the flask server to debug mode')
AP.add_argument ('-e', '--env-file', default=[], nargs='*', type=_env,
                 help=('an environment file as simple as example.txt or as '+
                       'complicated as defined by Python configparser where '+
                       'groups and delimited by ".".'))
AP.add_argument ('-H', '--hostname', default='localhost',
                 help='host name to serve on [%(default)s]')
AP.add_argument ('-N', '--no-run', action='store_true', default=False,
                 help='when set, treat as a dry run')
AP.add_argument ('-p', '--port', default=5000, type=int,
                 help='port number to serve on [%(default)d]')
AP.add_argument ('-v', '--volume', default=[], nargs='*', type=_dir,
                 help='root path for finding files and processing tar files')
ARGS = AP.parse_args()
print (ARGS)
for config in ARGS.env_file:
    for section in config:
        for key in config[section]: ddnp.env.add (section, key,
                                                  config[section][key])
        pass
    pass
for vpath in ARGS.volume: ddnp.vol.add (vpath)

if not ARGS.no_run: ddnp.app.run(ARGS.debug, ARGS.hostname, ARGS.port)
print (ddnp.env.CONTEXT)
print (ddnp.vol.CONTEXT)
