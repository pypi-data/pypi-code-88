import pytest
import sys
import subprocess

from textwrap import dedent

from warden_sdk.hub import Hub

# def test_excepthook(warden_inited, capture_events):
#    warden_inited()
#    events = capture_events()

#    (event,) = events
#    print(event)