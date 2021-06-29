"""Client class that controls everything in `warden_sdk`.

Client class is in-charge of bringing all of the components of the `warden_sdk` together; considered the engine. Use this module to call and instantiate a Client class when required such as when initializing a new thread for asyncio or multithreading. Otherwise, there's no need to instantiate a new Client class again.

  Typical usage example:

  from warden_sdk.client import Client
  client = Client(*args, **kwargs)

Code reference:
- [sentry_sdk](https://github.com/getsentry/sentry-python/blob/master/sentry_sdk/client.py)
"""
import atexit
from datetime import datetime

from warden_sdk.integrations import setup_integrations
from warden_sdk.utils import iteritems, text_type, string_types
from warden_sdk.debug import (
    capture_internal_exceptions, handle_in_app, current_stacktrace,
    logger)  # TODO(MP): add this function where necessary. Consult Sentry_SDK
from warden_sdk.transport import make_transport
from warden_sdk.consts import DEFAULT_OPTIONS, SDK_INFO
from warden_sdk.serializer import serialize
from warden_sdk.auth import verify_client


def _get_options(*args, **kwargs):
   """Gets options from the arguments.

   Retrieves the options from the arguments passed to the function and verifies if they are the allowed options based on the `DEFAULT_OPTIONS` class in the `const.py` file.

   Args:
      *args
      **kwargs

   Returns:
      A dict mapping keys to the corresponding args data fetched. Each option points of the corresponding argument passed For example:

      {
         'creds': {'client_id': '','client_secret': ''},
         'service': 'clerk',
         'api': 'datastore',
         'scopes': ['scope.1'],
         'integrations': [FlaskIntegration()]
      }

   Raises:
      TypeError: Unknown option was passed.
   """
   rv = dict(DEFAULT_OPTIONS)
   options = dict(*args, **kwargs)

   for key, value in iteritems(options):
      if key not in rv:
         raise TypeError("Unknown option %r" % (key,))
      rv[key] = value

   return rv


class _Client(object):
   """Client class controls all actions of `warden_sdk`.

   Client class setups the authentication to verify whether the API is registered correctly with a point-of-contact to 'blame' and refer to for information (project manager). Also setups up required integrations for logging such as `LoggingIntegration', 'ExcepthookIntegration', and 'FlaskIntegration'.

   This class also has a `self.captured` variable where all captured events are 'queued' and once the program exits, it runs `self.flush` in order to submit all captured events.

   Attributes:
      options: A dictionary containing all of the data when initialized to be used to verify and log events.
    """

   captured = []

   def __init__(self, *args, **kwargs) -> None:
      self.options = _get_options(*args, **kwargs)
      self._init_impl()

   def __getstate__(self):
      return {"options": self.options}

   def __setstate__(self, state):
      self.options = state["options"]
      self._init_impl()

   def _init_impl(self):
      # verify_client(self.options)
      self.transport = make_transport(self.options)
      self.integrations = setup_integrations(self.options["integrations"])

      atexit.register(self.close)  # Run flush when the program ends

   def capture_event(
       self,
       event,  # type: Event
       hint=None,  # type: Optional[Hint]
       scope=None,  # type: Optional[Scope]
   ):
      event_opt = self._prepare_event(event, hint, scope)

      self.captured.append(event_opt)

   def get_captured(self):
      return self.captured

   def _prepare_event(
       self,
       event,  # type: Event
       hint,  # type: Hint
       scope,  # type: Optional[Scope]
   ):
      # type: (...) -> Optional[Event]

      if event.get("timestamp") is None:
         event["timestamp"] = datetime.utcnow()

      if scope is not None:
         event_ = scope.apply_to_event(event, hint)
         if event_ is None:
            return None
         event = event_

      if (self.options["attach_stacktrace"] and "exception" not in event and
          "stacktrace" not in event and "threads" not in event):
         with capture_internal_exceptions():
            event["threads"] = {
                "values": [{
                    "stacktrace":
                        current_stacktrace(self.options["with_locals"]),
                    "crashed":
                        False,
                    "current":
                        True,
                }]
            }

      for key in "release", "environment", "server_name", "dist":
         if event.get(key) is None and self.options[key] is not None:
            event[key] = text_type(self.options[key]).strip()
      if event.get("sdk") is None:
         sdk_info = dict(SDK_INFO)
         sdk_info["integrations"] = sorted(self.integrations.keys())
         event["sdk"] = sdk_info

      if event.get("platform") is None:
         event["platform"] = "python"

      event = handle_in_app(event, self.options["in_app_exclude"],
                            self.options["in_app_include"])

      # Postprocess the event here so that annotated types do
      # generally not surface in before_send
      if event is not None:
         event = serialize(
             event,
             smart_transaction_trimming=self.options["_experiments"].get(
                 "smart_transaction_trimming"),
         )

      before_send = self.options["before_send"]
      if before_send is not None and event.get("type") != "transaction":
         new_event = None
         with capture_internal_exceptions():
            new_event = before_send(event, hint or {})
         if new_event is None:
            logger.info("before send dropped event (%s)", event)
         event = new_event  # type: ignore

      return event

   # def __iter__(self):
   #    return iter(self.captured)

   def close(self) -> None:
      """Close the client and shut down the transport. Flush out the system, by sending all of the data collected throughout the process."""
      self.flush()
      # if self.transport is not None:
      #    self.transport.kill()
      #    self.transport = None

   def flush(self) -> None:
      """Send the final results collected."""
      # print(
      #     'hi', self.captured
      # )  # TODO(Michael Podsiadly) add transport flush here here send all of the captured events.
      if self.transport is not None:
         self.transport.flush(self.captured)

   def __enter__(self):
      return self

   def __exit__(self, exc_type, exc_value, tb):
      self.close()


Client = (lambda: _Client)()