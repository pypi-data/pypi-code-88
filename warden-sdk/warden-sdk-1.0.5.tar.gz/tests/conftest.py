import os
import json

import pytest

import warden_sdk
from warden_sdk.transport import Transport
from warden_sdk.debug import capture_internal_exceptions
from warden_sdk.utils import reraise, string_types, iteritems

from tests import _warning_recorder, _warning_recorder_mgr

try:
   import pytest_benchmark
except ImportError:

   @pytest.fixture
   def benchmark():
      return lambda x: x()


@pytest.fixture(autouse=True)
def internal_exceptions(request, monkeypatch):
   errors = []
   if "tests_internal_exceptions" in request.keywords:
      return

   def _capture_internal_exception(self, exc_info):
      errors.append(exc_info)

   @request.addfinalizer
   def _():
      # rerasise the errors so that this just acts as a pass-through (that
      # happens to keep track of the errors which pass through it)
      for e in errors:
         reraise(*e)

   monkeypatch.setattr(warden_sdk.Hub, "_capture_internal_exception",
                       _capture_internal_exception)

   return errors


@pytest.fixture
def capture_events(monkeypatch):

   def inner():
      events = []
      test_client = warden_sdk.Hub.current.client
      old_capture_event = test_client.capture_event

      def append_event(event, hint, scope):
         events.append(event)
         # return old_capture_event(event)

      monkeypatch.setattr(test_client, "capture_event", append_event)
      return events

   return inner


class TestTransport(Transport):

   def __init__(self, capture_event_callback, capture_envelope_callback):
      Transport.__init__(self)
      self.capture_event = capture_event_callback
      self.capture_envelope = capture_envelope_callback
      self._queue = None


@pytest.fixture
def monkeypatch_test_transport(monkeypatch):

   def check_event(event):

      def check_string_keys(map):
         for key, value in iteritems(map):
            assert isinstance(key, string_types)
            if isinstance(value, dict):
               check_string_keys(value)

      with capture_internal_exceptions():
         check_string_keys(event)

   def check_envelope(envelope):
      with capture_internal_exceptions():
         # Assert error events are sent without envelope to server, for compat.
         # This does not apply if any item in the envelope is an attachment.
         if not any(x.type == "attachment" for x in envelope.items):
            assert not any(
                item.data_category == "error" for item in envelope.items)
            assert not any(
                item.get_event() is not None for item in envelope.items)

   def inner(client):
      monkeypatch.setattr(client, "transport",
                          TestTransport(check_event, check_envelope))

   return inner


@pytest.fixture
def warden_init(monkeypatch_test_transport, request):

   def inner(*a, **kw):
      hub = warden_sdk.Hub.current
      client = warden_sdk.Client(*a, **kw)
      hub.bind_client(client)
      if "transport" not in kw:
         monkeypatch_test_transport(warden_sdk.Hub.current.client)

   if request.node.get_closest_marker("forked"):
      # Do not run isolation if the test is already running in
      # ultimate isolation (seems to be required for celery tests that
      # fork)
      yield inner
   else:
      with warden_sdk.Hub(None):
         yield inner


@pytest.fixture
def warden_inited(monkeypatch_test_transport, request):

   def inner():
      hub = warden_sdk.Hub.current
      client = warden_sdk.Client(
          creds={
              'client_id':
                  'X05EgrYLsnLVJDePaR6DoMorykZZaKst',
              'client_secret':
                  'h5i1grbTKz60PiG65S96s9XZVzBMvwZaYVdy9XTSxwae2HKX1qrKFmadZg0'
          },
          service='warden',
          api='sdk',
          scopes=[
              "clerk.datastore.assets", "clerk.datastore.assets.readonly",
              "clerk.datastore.lifeword", "clerk.datastore.lifeword.readonly",
              "clerk.datastore.surveys", "clerk.datastore.surveys.readonly",
              "clerk.datastore.scores", "clerk.datastore.scores.readonly"
          ])
      hub.bind_client(client)
      # if "transport" not in _DEFAULT_INIT_ARGS:
      monkeypatch_test_transport(warden_sdk.Hub.current.client)

   if request.node.get_closest_marker("forked"):
      # Do not run isolation if the test is already running in
      # ultimate isolation (seems to be required for celery tests that
      # fork)
      yield inner
   else:
      with warden_sdk.Hub(None):
         yield inner
