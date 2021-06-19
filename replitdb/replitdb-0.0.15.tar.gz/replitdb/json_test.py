from replitdb import AsyncClient
import asyncio
import os

def DeprecationWarning(text):
    print(f"\033[1;31mDeprecationWarning: {text}\033[0;0m")

DeprecationWarning("This package has been deprecated please use the official repldb package ( can be found at: https://pypi.org/p/replit ), if you want to keep using it, you can access the clients with _Client.")

import replitdb._async as AsyncHandler
asyncio.run = AsyncHandler.run
class _Client():
    def __init__(self,**args):
        self.client = AsyncClient(args.get('url',os.getenv('REPLIT_DB_URL')))
        self.default = args.get('default','')
        self.args = args

    def __getitem__(self, key):
        return asyncio.run(self.client.view(key))

    def __setitem__(self, key, value):
        return asyncio.run(self.client.set_dict({key:value}))

    def __delitem__(self, key):
        return asyncio.run(self.client.remove(key))

    def __contains__(self, key):
        return key in self.keys()

    def __len__(self):
        return len(self.keys())

    def __repr__(self):
        x = asyncio.run(self.client.all_dict)
        print(x)
        exit()
        return repr(x)
    def __eq__(self,two):
      try:
        x = two.client.url
      except AttributeError:
        return False
      return self.client.url == x
    def __hash__(self):
      return hash(self.client.url)
    def __iter__(self):
      return iter(list(self._dict.keys()))
    def __getstate__(self):
      return {'args':self.args}
    def __setstate__(self, state):
      self.args = state['args']
      self = self.copy()
    @property
    def _dict(self):
      return asyncio.run(self.client.all_dict)
    def __str__(self):
      return str(self._dict)
    def __list__(self):
      return list(self._dict.keys())
    def keys(self):
      return self._dict.keys()
    def values(self):
      return self._dict.values()
    def update(self,dict):
      return asyncio.run(self.client.set_dict(dict))
    def clear(self):
      return asyncio.run(self.client.wipe)
    def copy(self):
      return Client(*self.args)
    def get(self,get):
      return self._dict.get(get)
    def items(self):
      return self._dict.items()
    def pop(self,pop):
      return asyncio.run(self.client.remove(pop))
    def setdefault(self,key,val):
      if(key in self):
        return self[key]
      self[key] = val
      return val