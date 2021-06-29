"""Global centralized class to manage all instances.

Hub centralizes and manages all Clients that are instantiated. This allows us to globally access Clients and puts the Hub in a ContextVars for easier management across different threads if used in async.

This module also initializes the warden_sdk through th `init()` module.

  Typical usage example:

  import warden_sdk as warden
  warden_sdk.init(...)

Code reference:
- [sentry_sdk](https://github.com/getsentry/sentry-python/blob/master/sentry_sdk/hub.py)
"""

import sys
import logging  # TODO(MP): add this function where necessary. Consult Sentry_SDK

from warden_sdk.client import Client
from warden_sdk.debug import (
    exc_info_from_error,
    event_from_exception,
)
from warden_sdk.utils import (ContextVar, logger)

# Create local and global context to handle the global Hub.
_local = ContextVar("warden_current_hub")


class _InitGuard(object):
   """Protects the initialization by closing the previous client.
   """

   def __init__(self, client) -> None:
      self._client = client

   def __enter__(self):
      # type: () -> _InitGuard
      return self

   def __exit__(self, exc_type, exc_value, tb):
      c = self._client
      if c is not None:
         c.close()


def _init(*args, **kwargs):
   """Initialize `warden_sdk`.

  Setups up the initial Client on the global Hub class.

  Args:
      *args
      **kwargs

  Returns:
      Instantiated class of InitGuard that will close the client when warden is initialized again.
  """
   client = Client(*args, **kwargs)
   Hub.current.bind_client(client)
   rv = _InitGuard(client)
   return rv


init = (lambda: _init)()


def with_metaclass(meta, *bases):
   # type: (Any, *Any) -> Any
   class MetaClass(type):

      def __new__(metacls, name, this_bases, d):
         # type: (Any, Any, Any, Any) -> Any
         return meta(name, bases, d)

   return type.__new__(MetaClass, "temporary_class", (), {})


class HubMeta(type):
   """Base class for Hub to get current/global Hub.
   """

   @property
   def current(cls):
      rv = _local.get(None)
      if rv is None:
         rv = Hub(GLOBAL_HUB)
         _local.set(rv)
      return rv

   @property
   def main(cls):
      return GLOBAL_HUB


class Hub(with_metaclass(HubMeta)):
   """Hub class for global access of all/any Clients within `warden_sdk`.

   TODO(Michael Podsiadly): edit
   Hub class setups a global Hub to be used across the `warden_sdk` as a point of access. From the global Hub, we have access to functions that `capture_` events, messages, and errors . An important feature of this class is the function to capture internal errors, necessary to record errors from within the sdk.

   Attributes:
      client_or_hub: An instantiated Client or Hub.
   """
   _stack = None  # type: Tuple[Optional[Client]]

   def __init__(
       self,
       client_or_hub=None,  # type: Optional[Union[Hub, Client]]
       #  scope=None,  # type: Optional[Any]
   ):
      if isinstance(client_or_hub, Hub):
         hub = client_or_hub
         client = hub._stack[-1]
      else:
         client = client_or_hub

      self._stack = [client]
      self._last_event_id = None  # type: Optional[str]
      self._old_hubs = []  # type: List[Hub]

   def __enter__(self):
      self._old_hubs.append(Hub.current)
      _local.set(self)
      return self

   def __exit__(
       self,
       exc_type,  # type: Optional[type]
       exc_value,  # type: Optional[BaseException]
       tb,  # type: Optional[Any]
   ):
      old = self._old_hubs.pop()
      _local.set(old)

   def run(self, callback):
      """Runs a callback in the context of the hub.  Alternatively the
      with statement can be used on the hub directly.
      """
      with self:
         return callback()

   @property
   def client(self):
      """Returns the current client on the hub."""
      return self._stack[-1]

   def bind_client(
       self,
       new  # type: Optional[Client]
   ):
      """Binds a new client to the hub."""
      # top = self._stack[-1]
      self._stack[-1] = (new)

   def capture_event(
       self,
       event,  # type: Event
       hint=None,  # type: Optional[Hint]
       scope=None,  # type: Optional[Any]
       **scope_args  # type: Any
   ):
      """Captures an event. Alias of :py:meth:`warden_sdk.Client.capture_event`."""
      client = self._stack[-1]
      if client is not None:
         rv = client.capture_event(event, hint, scope)
         if rv is not None:
            self._last_event_id = rv
         return rv
      return None

   def capture_message(
       self,
       message,  # type: str
       level=None,  # type: Optional[str]
       scope=None,  # type: Optional[Any]
       **scope_args  # type: Any
   ):
      # type: (...) -> Optional[str]
      """Captures a message.  The message is just a string.  If no level
      is provided the default level is `info`.

      Returns:
         An `event_id` if the SDK decided to send the event (see :py:meth:`warden_sdk.Client.capture_event`).
      """
      if self.client is None:
         return None
      if level is None:
         level = "info"
      return self.capture_event({
          "message": message,
          "level": level
      },
                                scope=scope,
                                **scope_args)

   def capture_exception(
       self,
       error=None,  # type: Optional[Union[BaseException, ExcInfo]]
       scope=None,  # type: Optional[Any]
       **scope_args  # type: Any
   ):
      # type: (...) -> Optional[str]
      """Captures an exception.

      Args:
         error: An exception to catch. If `None`, `sys.exc_info()` will be used.

      Returns
         An `event_id` if the SDK decided to send the event (see :py:meth:`warden_sdk.Client.capture_event`).
      """
      client = self.client
      if client is None:
         return None
      if error is not None:
         exc_info = exc_info_from_error(error)
      else:
         exc_info = sys.exc_info()

      event, hint = event_from_exception(exc_info,
                                         client_options=client.options)
      try:
         return self.capture_event(event, hint=hint, scope=scope, **scope_args)
      except Exception:
         self._capture_internal_exception(sys.exc_info())

      return None

   def _capture_internal_exception(
       self,
       exc_info  # type: Any
   ):
      # type: (...) -> Any
      """ Capture an exception that is likely caused by a bug in the SDK itself.
      
      These exceptions do not end up in Warden and are just logged instead.
      """
      logger.error("Internal error in warden_sdk", exc_info=exc_info)

   def flush(self):
      client = self.client
      client.close()
      pass

   def get_integration(
       self,
       name_or_class  # type: Union[str, Type[Integration]]
   ):
      # type: (...) -> Any
      """Returns the integration for this hub by name or class.  If there
        is no client bound or the client does not have that integration
        then `None` is returned.
        If the return value is not `None` the hub is guaranteed to have a
        client attached.
        """
      if isinstance(name_or_class, str):
         integration_name = name_or_class
      elif name_or_class.identifier is not None:
         integration_name = name_or_class.identifier
      else:
         raise ValueError("Integration has no name")

      client = self.client
      if client is not None:
         rv = client.integrations.get(integration_name)
         if rv is not None:
            return rv


# Instantiate a Global Hub class and set it into the local ContextVars
GLOBAL_HUB = Hub()
_local.set(GLOBAL_HUB)