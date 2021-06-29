"""User class to maintain state and user information.

The User module allows us to collect all of the relevant information for a user and allow the system to access the relevant information about a User that necessary to propagate internally for clear understanding of what's going on with the system.
"""
from warden_sdk.hub import Hub
from warden_sdk.utils import (get_options)

from typing import (Any, Optional)


class _User(object):
   """User class contains all information about the requester.
   """
   fid: Optional[str] = None
   __scope: Optional[list] = None

   def __init__(self) -> None:
      pass

   def setup(self, request: Any) -> None:
      # try:
      try:
         __context = request.environ['serverless.event']['requestContext'][
             'authorizer']
      except:
         __context = request['serverless.event']['requestContext']['authorizer']
      self.fid = __context['fid']
      self.scope = __context['scope']
      # except Exception as err:
      #    raise
      # Exception({
      #        'error': 'invalid_request',
      #        'error_description': str(err)
      #    })

      hub = Hub.current
      client = hub.client
      options = get_options(client.options)

      if options['scopes'] is None:
         raise ValueError('Missing scopes.')

      self.verify_scopes(options['scopes'])

   @property
   def scope(self) -> list:
      return self.__scope

   @scope.setter
   def scope(self, scope):
      self.__scope = scope.split(' ')

   def verify_scopes(self, scopes) -> bool:
      if not any(scope in self.scope for scope in scopes):
         raise Exception({
             'error': 'invalid_request',
             'error_description': 'Invalid scopes.'
         })

      return True


User = (lambda: _User)()