#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function

import os
import json
import time
import argparse
import traceback
from datetime import datetime

import websocket
try:
    import thread
except ImportError:
    import _thread as thread


class AstralBot():
    """
        An AstralBot engine connector.
    """
    def __init__(self, url, options, task_function=None):
        self.remote = "ws://" + url;
        self.task_function = task_function
        self.last_engine_data = None
        self.last_game_data = None
        self.settings = {
          "verbose": True
        }

        if options:
          if options.get("verbose"):
            self.settings["verbose"] = options["verbose"];

    def _encode_message(self, message):
        """
        Encode a json object to a string message.
        """
        return json.dumps(message)


    def _decode_message(self, data):
        """
        Decode a message string in json object.
        """
        return json.loads(data)


    def run(self):
        """
        Start and maintain the communication process (will wait for a connection)
        """
        exit_requested = False
        websocket.enableTrace(False)
        ws = websocket.WebSocketApp(self.remote,
                                  subprotocols = ['astral-protocol-v1'],
                                  on_open = lambda ws: self.on_open(ws),
                                  on_message = lambda ws, msg: self.on_message(ws, msg),
                                  on_error = lambda ws, error: self.on_error(ws, error),
                                  on_close =  lambda ws: self.on_close(ws))
        while not exit_requested:
            try:
                print("Trying to connect to: {}".format(self.remote))
                ws.run_forever() # This should return a value depending of the exit reason but it does not... so let's improvise :(
                time.sleep(1)
            except KeyboardInterrupt as ki:
                exit_requested = True

# ==================== Handle websocket callbacks ==============================
    def on_error(self, connection, error):
        print("WebSocket Connection Error:", error)

    def on_close(self, connection):
        print("WebSocket Connection Closed")

    def on_open(self, connection):
        print("AstralBot Connected")

    def on_message(self, connection, message):
        execute_task = False
        msg = self._decode_message(message)
        print("WebSocket message", msg)
