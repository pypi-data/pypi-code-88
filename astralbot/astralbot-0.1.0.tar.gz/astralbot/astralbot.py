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
          "verbose": True,
          "saveScreen": False,
          "saveScreenDir": "./screenshots",
          "sessionToken": None
        }
        self.auth = {
          "handlerToken": None,
          "sessionToken": None,
          "version": None,
          "name": None
        }
        if options:
          if options.get("verbose"):
            self.settings["verbose"] = options["verbose"];


    def set_auth(self, name, version, sessionToken):
        """
        Add authentication informations to connect a protected astral engine.
        """
        self.auth["name"] = name
        self.auth["version"] = version
        self.auth["sessionToken"] = sessionToken
        self.auth["handlerToken"] = None


    def enable_screen_saving(self, dir=None):
        """
        Enable screenshot automatic saving and optionnally set the output folder (each screenshot will be saved).
        """
        self.settings["saveScreen"] = True
        if dir:
            self.settings["saveScreenDir"] = dir

        if not os.path.exists(self.settings["saveScreenDir"]):
            os.makedirs(self.settings["saveScreenDir"])


    def screen_to_file(self):
        """
        Save the latest screenshot in the disk.
        """
        screen_data = self.last_game_data.get("screen").get("data")
        screen_counter = self.last_game_data.get("screen").get("counter", 0)
        if screen_data:
            screen_path = os.path.join(self.settings["saveScreenDir"], "screenshot_{}.png".format(screen_counter))
        with open(screen_path, "wb") as f:
            f.write(bytes(bytearray(screen_data.get("data"))))


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


    def _forge_command_data(self, command):
        """
        Returns the base object to send a message.
        """
        if self.settings["verbose"]:
            print("DEBUG: _forge_command_data()", command)

        data = {
            "timestamp": str(datetime.now()),
            "command": command,
            "args": {}
        }
        return data


    def _send_command_data(self, connection, data, checkLock=False):
        """
        Send the message to the astralBot.
        """
        if checkLock:
            if self.lastState.get("protected", False):
                if self.auth.get("handlerToken") == None:
                    print("ERROR: _send_command_data()", data.command, "command locked")
                    return
                else:
                    data.handlerToken = self.auth.get("handlerToken")
        connection.send(self._encode_message(data))


    def _set_session_token(self, connection, coreToken, newSessionToken):
        """
        Forge and send a setSessionToken messsage to the specified connection.
        Use the coreToken to set the session token used to get the handler token.
        """
        data = self._forge_command_data("setSessionToken")
        data.args = {
          "newSessionToken": newSessionToken,
          "coreToken": coreToken
        }
        self._send_command_data(connection, data)


    def _ping(self, connection):
        """
        Forge and send a ping messsage to the specified connection.
        """
        data = self._forge_command_data("ping")
        self._send_command_data(connection, data)


    def _register_handler(self, connection):
        """
        Request the current handler token with the session token.
        """
        if self.auth.get("sessionToken") and self.auth.get("name") and self.auth.get("version"):
            data = self._forge_command_data("registerHandler");
            data.args = {
                "sessionToken": self.auth.sessionToken,
                "version": self.auth.version,
                "name": self.auth.name
            }
            self._send_command_data(connection, data)
        else:
            print("ERROR _register_handler(): auth informations are not defined");


    def _start(self, connection, name):
        """
        Forge and send a start messsage to the specified connection.
        """
        data = self._forge_command_data("start")
        data["args"] = {
            "name": name
        }
        self._send_command_data(connection, data)


    def _click_at(self, connection, x, y):
        """
        Forge and send a clickAt messsage to the specified connection.
        """
        data = self._forge_command_data("clickAt")
        data["args"] = {
            "x": x,
            "y": y
        }
        self._send_command_data(connection, data)


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
        self.auth["handlerToken"] = None
        self.auth["sessionToken"] = None

    def on_open(self, connection):
        print("AstralBot Connected")
        if self.auth.get("sessionToken") != None:
            self._register_handler(connection)
        self._ping(connection)

    def on_message(self, connection, message):
        execute_task = False
        msg = self._decode_message(message)
        # print("WebSocket message", msg)
        event = msg.get("event")
        payload = msg.get("payload")
        if event in ["GameEngine.engineData", "GameEngine.gameData"]:
            execute_task = True
            if event == "GameEngine.engineData":
                self.last_engine_data = payload
            if event == "GameEngine.gameData":
                self.last_game_data = payload
                if self.settings.get("saveScreen") == True:
                    self.screen_to_file()
        elif event in ["error", "refused"]:
            print("ERROR: {} {}".format(event, payload))
        elif event in ["registered"]:
            print("INFO: {}".format(event))
            self.auth["handlerToken"] = payload.get("handlerToken")
        else:
            print("ERROR: unknown event {}".format(event))

        if self.task_function and execute_task:
            if self.settings.get("verbose"):
                print("DEBUG: Calling taskFunction() ...")
            try:
                action = self.task_function(self.last_engine_data, self.last_game_data)
            except:
                print("ERROR in task_function:")
                traceback.print_exc()
            if self.settings.get("verbose"):
                print("DEBUG: Action from taskFunction() {}".format(action))

            # NOTE: handle action if there is a specified command:
            # TODO: check action type and content
            if action.get("command"):
                if action.get("command") == "clickAt":
                    self._click_at(connection, action.get("args").get("x"), action.get("args").get("y"))
                if action.get("command") == "start":
                    self._start(connection, action.get("args").get("name"))
