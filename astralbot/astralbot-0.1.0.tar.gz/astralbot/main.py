#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function

import os
import json
import argparse
import traceback

from astralbot import AstralBot

class GameBot:
    def __init__(self, supported_game):
        """
        GameBot instance to handle engine updates
        """
        self.supported_game = supported_game
        self.previous_state = None

    def engineStateTransition(self, engine):
        """
        return the new engine status in case of state transition
        """
        state = engine.get("state")
        if state != self.previous_state:
            self.previous_state = state
            return state
        return None

    def loop(self, engine, game):
        """
        will be ran each time the engine state change and should return an action to take.
        """
        action = dict()
        new_state = self.engineStateTransition(engine)
        print(" * Engine data: {}".format(engine))
        print(" * Game data: {}".format(game))

        # click in the first box when transition from started to ready.
        if new_state:
            print(" * State transition detected {}".format(new_state))
            if new_state == "initialized":
                if self.supported_game in engine.get("games", list()):
                    print("Please astralBot, start the game {}".format(self.supported_game))
                    action = {"command": "start", "args": {"name": self.supported_game} }
                else:
                    print("ERROR: the astralBot instance does not support the game {}".format(self.supported_game))
            # Make the first move when the game is ready
            elif new_state == "started":
                print("Please astralBot, click at 20,60")
                action = {"command": "clickAt", "args": {"x": 20, "y":60} }
            else:
                print("Nothing to do")
        return action


def main():
    """
        Used to load a script to interact with an astralbot engine.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, default="localhost:8080", help="Url of astralbot engine (with port <ip>:<port>)")
    args = parser.parse_args()

    try:
        gb = GameBot("minesweeper_beginner")
        ab = AstralBot(args.url, {"verbose": True}, gb.loop)
        # save all received screen in the disk
        # ab.enable_screen_saving()

        # In the case the astral engine is protected you can add authentication informations
        # ab.set_auth("myBot", "v1.0.0", "t0ken")

        # connect and run the bot
        ab.run()
    except Exception as e:
        traceback.print_exc()


if __name__ == "__main__":
    main()
