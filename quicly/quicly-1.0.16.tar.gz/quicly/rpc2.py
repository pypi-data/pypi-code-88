from typing import *

import threading
import re
import functools
from quicly.inspectutils import QxInspectUtils
from quicly.patterns import *

from collections import OrderedDict


class QxRequest(object):
  def __init__(self):
    pass


class QxResponse(object):
  def __init__(self):
    pass


class QxServerHandler(object):
  def __init__(self, func: Optional[Callable] = None):
    self._func = func
    self._args = OrderedDict()
    self._meta = OrderedDict()

  def __call__(self, *al, **kw) -> Any:
    ret = None
    if callable(self._func):
      ret = self._func(*al, **kw)
    return ret


class QxServerHandlers(object):
  _lock = threading.Lock()
  _inst = dict()

  def __new__(cls, server_name: Optional[str] = None, *a, **kw):
    inst = cls._inst.get(server_name)
    if not isinstance(inst, cls):
      with cls._lock:
        inst = cls._inst.get(server_name)
        if not isinstance(inst, cls):
          inst = super().__new__(cls)
          cls._inst[server_name] = inst
    return inst

  def __init__(self, server_name: Optional[str] = None, *a, **kw):
    self._server_name = server_name

    self._handler_cls_inst_table = dict()
    self._handler_cls_inst_table_lock = threading.Lock()

    self._handlers = dict()
    self._patterns = set()

  @property
  def server_name(self) -> Optional[str]:
    return self._server_name

  def _get_handler_cls_inst(self, handler_cls: Type) -> Any:
    assert isinstance(handler_cls, type)
    handler_cls_inst = self._handler_cls_inst_table.get(handler_cls)
    if not isinstance(handler_cls_inst, handler_cls):
      with self._handler_cls_inst_table_lock:
        handler_cls_inst = self._handler_cls_inst_table.get(handler_cls)
        if not isinstance(handler_cls_inst, handler_cls):
          handler_cls_inst = handler_cls()
          self._handler_cls_inst_table[handler_cls] = handler_cls_inst
    return handler_cls_inst

  def _process_method_handler(self, handler: Callable):
    if QxInspectUtils.is_inst_method(handler):
      handler_cls = QxInspectUtils.get_method_class(handler)
      if isinstance(handler_cls, type):
        handler_cls_inst = self._get_handler_cls_inst(handler_cls)
        handler = functools.partial(handler, handler_cls_inst)
    return handler

  def find_handler(self, name: str) -> Optional[Callable]:
    ret = None

    if name in self._handlers:
      ret = self._handlers.get(name)
    else:
      for pattern in self._patterns:  # type: re.Pattern
        if pattern.fullmatch(name):
          ret = self._handlers.get(pattern.pattern)
          break

    return ret

  @staticmethod
  def parse_name(name: str, default_pattern: str = None) -> Dict:
    default_pattern = default_pattern if isinstance(default_pattern, str) else '[^/]*'
    matches = list(re.finditer(r'\{[_\dA-Z]+(:[^}]*)?\}', name, re.I))

    if len(matches):
      def __get_part_str__(_name: str, _i: int = 0, _j: int = None):
        return _name[_i:_j] if isinstance(_j, int) else _name[_i:]

      def __add_part_str__(_parts: dict, _name: str, _i: int = 0, _j: int = None):
        _part = __get_part_str__(_name, _i, _j)
        if isinstance(_part, str) and len(_part):
          _part_pattern = _part.replace('.', '\\.')
          _parts[_part] = _part_pattern, None

      def __add_part_var__(_parts: dict, _name: str, _i: int = 0, _j: int = None):
        _part = __get_part_str__(_name, _i, _j)
        if isinstance(_part, str) and len(_part):
          _part_t = _part[1:-1].split(':', maxsplit=1)
          _part_var = _part_t[0].strip()
          _part_pattern = _part_t[1].strip() if len(_part_t) == 2 else default_pattern
          _parts[_part] = _part_pattern, _part_var

      parts = OrderedDict()

      i = 0
      for m in matches:
        span = m.span()
        __add_part_str__(parts, name, i, span[0])
        __add_part_var__(parts, name, span[0], span[1])
        i = span[1]

      __add_part_str__(parts, name, i)

      ret = parts
    else:
      ret = name

    return ret

  @staticmethod
  def process_name(name: str, default_pattern: Optional[str] = None) -> Union[str, re.Pattern]:
    name_t = QxServerHandlers.parse_name(name, default_pattern)

    if isinstance(name_t, dict):
      ret = re.compile(''.join(x[0] for x in name_t.values()))
    else:
      ret = name_t

    return ret

  def register_handler(self, handler: Callable, alias: Optional[Union[str, List[str]]] = None):
    names = list()

    for name in (getattr(handler, '__qualname__', None), getattr(handler, '__name__', None), str(handler)):
      if isinstance(name, str) and len(name):
        names.append(name)
        break

    if isinstance(alias, str):
      alias = [alias]
    elif isinstance(alias, (list, tuple, set)):
      alias = list(alias)
    else:
      alias = list()

    for name in alias:
      if isinstance(name, str) and len(name):
        names.append(name)

    handler = self._process_method_handler(handler)

    for name in names:
      name_t = self.process_name(name)

      if isinstance(name_t, str):
        self._handlers[name_t] = handler
      elif isinstance(name_t, re.Pattern):
        self._handlers[name_t.pattern] = handler
        self._patterns.add(name_t)


QxServerHandlers.parse_name('Hello.aaa')
QxServerHandlers.parse_name('/user/{user:\\d+}/friend/{friend}')


class Hello(object):
  @staticmethod
  def aaa(*al, **kw):
    print('aaa', al, kw)

  @classmethod
  def bbb(cls, *al, **kw):
    print('bbb', cls, al, kw)

  def ccc(self, *al, **kw):
    print('ccc', self, al, kw)


handlers = QxServerHandlers()
handlers.register_handler(Hello.aaa, '/aaa/x/{x}/y/{y}')
handlers.register_handler(Hello.bbb, '/bbb/x/{x}/y/{y}')
handlers.register_handler(Hello.ccc, '/ccc/x/{x}/y/{y}')

handlers.find_handler('Hello.bbb')()
handlers.find_handler('/ccc/x/1/y/2')()
