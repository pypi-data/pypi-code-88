import sys
PzqwR=object
PzqwT=staticmethod
Pzqwo=False
Pzqwy=Exception
Pzqwk=None
PzqwU=input
Pzqwa=list
import json
import logging
import getpass
from localstack.config import CONFIG_FILE_PATH,load_config_file
from localstack.constants import API_ENDPOINT
from localstack.utils.common import to_str,safe_requests,save_file,load_file
LOG=logging.getLogger(__name__)
class AuthProvider(PzqwR):
 @PzqwT
 def name():
  raise
 def get_or_create_token(self,username,password,headers):
  pass
 def get_user_for_token(self,token):
  pass
 @PzqwT
 def providers():
  return{c.name():c for c in AuthProvider.__subclasses__()}
 @PzqwT
 def get(provider,raise_error=Pzqwo):
  provider_class=AuthProvider.providers().get(provider)
  if not provider_class:
   msg='Unable to find auth provider class "%s"'%provider
   LOG.warning(msg)
   if raise_error:
    raise Pzqwy(msg)
   return Pzqwk
  return provider_class()
class AuthProviderInternal(AuthProvider):
 @PzqwT
 def name():
  return 'internal'
 def get_or_create_token(self,username,password,headers):
  data={'username':username,'password':password}
  response=safe_requests.post('%s/user/signin'%API_ENDPOINT,json.dumps(data),headers=headers)
  if response.status_code>=400:
   return
  try:
   result=json.loads(to_str(response.content or '{}'))
   return result['token']
  except Pzqwy:
   pass
 def read_credentials(self,username):
  print('Please provide your login credentials below')
  if not username:
   sys.stdout.write('Username: ')
   sys.stdout.flush()
   username=PzqwU()
  password=getpass.getpass()
  return username,password,{}
 def get_user_for_token(self,token):
  raise Pzqwy('Not implemented')
def login(provider,username=Pzqwk):
 auth_provider=AuthProvider.get(provider)
 if not auth_provider:
  providers=Pzqwa(AuthProvider.providers().keys())
  raise Pzqwy('Unknown provider "%s", should be one of %s'%(provider,providers))
 username,password,headers=auth_provider.read_credentials(username)
 print('Verifying credentials ... (this may take a few moments)')
 token=auth_provider.get_or_create_token(username,password,headers)
 if not token:
  raise Pzqwy('Unable to verify login credentials - please try again')
 configs=load_config_file()
 configs['login']={'provider':provider,'username':username,'token':token}
 save_file(CONFIG_FILE_PATH,json.dumps(configs))
def logout():
 configs=json_loads(load_file(CONFIG_FILE_PATH,default='{}'))
 configs['login']={}
 save_file(CONFIG_FILE_PATH,json.dumps(configs))
def json_loads(s):
 return json.loads(to_str(s))
# Created by pyminifier (https://github.com/liftoff/pyminifier)
