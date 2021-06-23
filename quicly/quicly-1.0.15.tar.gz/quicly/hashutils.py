from typing import *

import os
import hashlib


class QxHash(object):
  def __init__(self, algorithm: str):
    self._hash_o = getattr(hashlib, algorithm)
    assert callable(self._hash_o)

  def hash_s(self, s: Union[str, bytes]) -> str:
    if isinstance(s, str):
      s = s.encode('utf-8')
    h = self._hash_o()
    h.update(s)
    return h.hexdigest().lower()

  def hash_f(self, f: str) -> str:
    ret = None
    if os.path.isfile(f):
      with open(f, 'rb') as fo:
        ret = self.hash_s(fo.read())
    elif os.path.isdir(f):
      lines = []
      for item in sorted(os.listdir(f)):
        pathname = os.path.join(f, item)
        lines.append('{}:{}'.format(item, self.hash_f(pathname)))
      ret = self.hash_s('\n'.join(lines))
    return ret
