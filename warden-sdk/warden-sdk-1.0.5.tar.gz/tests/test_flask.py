import json
import pytest
import logging

from io import BytesIO

flask = pytest.importorskip("flask")

from flask import Flask, Response, request, abort, stream_with_context

from warden_sdk import Hub
from warden_sdk.integrations.logging import LoggingIntegration
import warden_sdk.integrations.flask as flask_sentry

BASE_URL = "https://localhost"

@pytest.fixture
def app():
   app = Flask(__name__)
   app.config["TESTING"] = True
   app.secret_key = "haha"

   @app.route("/message")
   def hi():
      Hub.current.client.capture_message("hi")
      return "ok"

   @app.route("/err")
   def err():
      div = 1 / 0
      return "ok"

   return app


def test_has_context(warden_inited, app, capture_events):
   warden_inited()
   events = capture_events()

   client = app.test_client()
   # try:
   response = client.get("/message", base_url=BASE_URL)
   # except Exception as e:
   #    pass

   (event,) = events
   assert event['exception']['values'][0]['value'] == "bad_request"


def test_error(warden_inited, app, capture_events):
   warden_inited()
   events = capture_events()

   client = app.test_client()
   response = client.get("/err", base_url=BASE_URL)

   (event,) = events
   assert event['exception']['values'][0]['value'] == "bad_request"
