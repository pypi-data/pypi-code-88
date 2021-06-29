"""Transport module sends all of the queued data in `warden_sdk`.

TODO(MP): document
"""
from __future__ import print_function

import io
# import urllib3  # type: ignore
import gzip
import requests

from datetime import datetime, timedelta

from warden_sdk.utils import logger, json_dumps
from warden_sdk.debug import capture_internal_exceptions
from warden_sdk.consts import WARDEN_LOGGING_API_LINK, VERSION
# from warden_sdk.worker import BackgroundWorker
# from warden_sdk.envelope import Envelope

from typing import (Dict, Optional, Any)


class Transport(object):
   """Baseclass for all transports.

   A transport is used to send an event to warden_sdk.
   """

   def __init__(self, options=None):
      self.options = options

   def flush(
       self,
       events,
       timeout: Optional[float] = None,
       callback: Optional[Any] = None,
   ) -> None:
      """Wait `timeout` seconds for the current events to be sent out."""
      pass


class HttpTransport(Transport):
   """The default HTTP transport."""

   def __init__(self, options):
      Transport.__init__(self, options)
      self.options = options

      from warden_sdk import Hub

      self.hub_cls = Hub

   def _send_request(
       self,
       body: bytes,
       headers: Dict[str, str],
       endpoint_type="store",
   ) -> None:
      # TODO(MP): add authentication headers to logging
      headers.update({
          "User-Agent":
              str("warden.python/%s" % VERSION),
          "X-Warden-Auth":
              f"Warden warden_client={self.options['creds']['client_id']}, warden_secret={self.options['creds']['client_secret']}",
      })
      try:
         response = requests.post(
             WARDEN_LOGGING_API_LINK,
             data=body,
             headers=headers,
         )
      except Exception as e:
         raise

      # try:
      #    response = requests.post(
      #        WARDEN_LOGGING_API_LINK,
      #        body=body,
      #        headers=headers,
      #    )
      # except Exception:
      #    self.on_dropped_event("network")
      #    raise

      # try:
      #    self._update_rate_limits(response)

      #    if response.status == 429:
      #       # if we hit a 429.  Something was rate limited but we already
      #       # acted on this in `self._update_rate_limits`.
      #       self.on_dropped_event("status_429")
      #       pass

      #    elif response.status >= 300 or response.status < 200:
      #       logger.error(
      #           "Unexpected status code: %s (body: %s)",
      #           response.status,
      #           response.data,
      #       )
      #       self.on_dropped_event("status_{}".format(response.status))
      # finally:
      #    response.close()

   def _send_event(
       self,
       event  # type: Event
   ) -> None:
      body = io.BytesIO()
      with gzip.GzipFile(fileobj=body, mode="w") as f:
         f.write(json_dumps(event))

      # assert self.parsed_dsn is not None
      # logger.debug(
      #     "Sending event, type:%s level:%s event_id:%s project:%s host:%s" % (
      #         event.get("type") or "null",
      #         event.get("level") or "null",
      #         event.get("event_id") or "null",
      #         self.parsed_dsn.project_id,
      #         self.parsed_dsn.host,
      #     ))
      self._send_request(
          body.getvalue(),
          headers={
              "Content-Type": "application/json",
              "Content-Encoding": "gzip"
          },
      )
      return None

   def capture_event(self, event) -> None:
      hub = self.hub_cls.current
      with hub:
         with capture_internal_exceptions():
            self._send_event(event)

   def flush(
       self,
       events,
       timeout: Optional[float] = None,
       callback: Optional[Any] = None,
   ) -> None:
      logger.debug("Flushing HTTP transport")
      for event in events:
         self.capture_event(event)
      logger.debug("Flushed HTTP transport")


def make_transport(options) -> Transport:
   # ref_transport = options["transport"] # This will be none for now!

   # if ref_transport is None:
   transport_cls = HttpTransport

   if options['creds']['client_id'] and options['creds']['client_secret']:
      return transport_cls(options)

   return None