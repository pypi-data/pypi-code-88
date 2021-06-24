import sys
WnVFM=object
WnVFz=staticmethod
WnVFm=False
WnVFJ=Exception
WnVFH=None
WnVFK=input
WnVFh=list
import json
import logging
import getpass
from localstack.config import CONFIG_FILE_PATH,load_config_file
from localstack.constants import API_ENDPOINT
from localstack.utils.common import to_str,safe_requests,save_file,load_file
LOG=logging.getLogger(__name__)
class AuthProvider(WnVFM):
 @WnVFz
 def name():
  raise
 def get_or_create_token(self,username,password,headers):
  pass
 def get_user_for_token(self,token):
  pass
 @WnVFz
 def providers():
  return{c.name():c for c in AuthProvider.__subclasses__()}
 @WnVFz
 def get(provider,raise_error=WnVFm):
  provider_class=AuthProvider.providers().get(provider)
  if not provider_class:
   msg='Unable to find auth provider class "%s"'%provider
   LOG.warning(msg)
   if raise_error:
    raise WnVFJ(msg)
   return WnVFH
  return provider_class()
class AuthProviderInternal(AuthProvider):
 @WnVFz
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
  except WnVFJ:
   pass
 def read_credentials(self,username):
  print('Please provide your login credentials below')
  if not username:
   sys.stdout.write('Username: ')
   sys.stdout.flush()
   username=WnVFK()
  password=getpass.getpass()
  return username,password,{}
 def get_user_for_token(self,token):
  raise WnVFJ('Not implemented')
def login(provider,username=WnVFH):
 auth_provider=AuthProvider.get(provider)
 if not auth_provider:
  providers=WnVFh(AuthProvider.providers().keys())
  raise WnVFJ('Unknown provider "%s", should be one of %s'%(provider,providers))
 username,password,headers=auth_provider.read_credentials(username)
 print('Verifying credentials ... (this may take a few moments)')
 token=auth_provider.get_or_create_token(username,password,headers)
 if not token:
  raise WnVFJ('Unable to verify login credentials - please try again')
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
