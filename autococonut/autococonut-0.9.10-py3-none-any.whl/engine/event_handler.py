"""
The AutoCoconut Project - Module 'event_handler'
===============================================================================
The event_handler module uses pynput to record the key and mouse actions
(events), provide a basic interpretation and sorting and returning a dictionary
of these events.

Created by Lukáš Růžička (lruzicka@redhat.com), 2020 and provided under the
General Public License v3.
"""
from . import interpreter
from . import screenshot_grabber as camera
import glob
import json
import os
import time
import signal
from pynput.keyboard import KeyCode
from pynput.keyboard import Listener as KeyListener
from pynput.mouse import Listener as MouseListener

class Handler:
    """ The Handler class processes the mouse and keyboard events, interprets them,
    creates a dictionary of events and returns it for further analysis. """
    def __init__(self, stop_key="f10", time_offset=1):
        """ Innitiates the variables.

        The ${stop_key} defines a special key that will terminate the listeners
        and finish the script. The ${time_offset} defines the divergence of the
        "corrected" screenshot from the event timestamp. It should be a positive,
        non-zero value."""
        # The $stop_key switches on the recording and quits the script.
        self.stop_key = stop_key
        # If self.started is False no events are recorded. After pressing the
        # stop key, this will change to true and the script will record events.
        self.started = False
        # The $time_offset sets the delay with which a "corrected" needle is
        # taken. By default it is 1 second.
        self.time_offset = time_offset
        # All the captured events are stored in the $self.events which is returned
        # at the end.
        self.events = {}
        # These keys are the so called modifiers:
        self.modifiers = [
                        'alt',
                        'ctrl',
                        'ctrl_r',
                        'cmd',
                        'shift'
        ]
        # These keys are the so called special (non-alphanumeric) keys:
        self.specials = [
                        'menu',
                        'esc',
                        'enter',
                        'backspace',
                        'insert',
                        'home',
                        'page_up',
                        'page_down',
                        'end',
                        'delete',
                        'print_screen',
                        'scroll_lock',
                        'caps_lock',
                        'pause',
                        'up',
                        'down',
                        'right',
                        'left',
                        'f1',
                        'f2',
                        'f3',
                        'f4',
                        'f5',
                        'f6',
                        'f7',
                        'f8',
                        'f9',
                        'f10',
                        'f11',
                        'f12'
        ]

        # When scrolling the mouse, each single step is sent from pynput.
        # This would case the script to take a high number of screenshots,
        # therefore we only take a screenshot after a certain number
        # of scroll steps. This is controlled by these variables.
        self.scrollstep = 0
        self.scrollscreen = None
        self.needlefiles = []
        # Start the screenshot_grabber.py in the background for taking screenshots.
        camera.start()

    def name_shot(self, timestamp):
        """ Create the shot name.

        Takes the $(timestamp) and returns the $(timestamp).png. """
        return f"{timestamp}.png"

    def record_wheel_scroll(self, point_x, point_y, delta_x, delta_y, timestamp):
        """ Records a mouse scroll in vertical (dy) and horizontal (dx) direction.

        Note, that the horizontal direction is not available on the standard mouse."""
        if self.scrollscreen:
            shot = self.scrollscreen[0]
            cshot = self.scrollscreen[1]
        # For scrolls, take a screenshot after each 10 steps.
        if self.scrollstep == 0 or self.scrollstep > 10:
            camera.save_screenshot(timestamp, self.time_offset)
            shot = self.name_shot(timestamp)
            cshot = self.name_shot(timestamp + self.time_offset)
            self.scrollscreen = [shot, cshot]
            self.scrollstep = 1
        else:
            self.scrollstep += 1
        # Create the event
        report = {
            'type': 'mouse',
            'action': 'scroll',
            'coordinates': (point_x, point_y),
            'horizontal': delta_x,
            'vertical': delta_y,
            'screens': [shot, cshot]
        }
        self.events[timestamp] = report
        return report

    def record_mouse_click(self, point_x, point_y, button, timestamp, release=False):
        """ Records the mouse click of the 'button' at the given position 'x' and 'y'.

        It takes the $button, $point_x, $point_y from the event collector, including
        the $timestamp and $release to recognize whether the button was pressed or
        released in this event.

        The corrected screenshot, in this case, is taken prior (not after) the timestamp
        screenshot, because often, when the mouse hovers over a gui element, this one
        changes, highlights and this would cause problems with OpenQA recognition."""
        shot = cshot = None
        button = str(button).split('.')[1]
        if not release:
            action = 'click'
            # For a mouse click, especially for the purposes of OpenQA,
            # it is crucial to take a clicking needle when there are no
            # changes to the standard screen, such as changes in colour,
            # or shapes, when the mouse cursor hovers over the button.
            # Therefore, we will take a screenshot that precedes the
            # actual action instead.
            offset = self.time_offset * -1
            camera.save_screenshot(timestamp, offset)
            shot = self.name_shot(timestamp)
            cshot = self.name_shot(timestamp + offset)
        else:
            action = 'release'
        # Create the event
        report = {
            'type': 'mouse',
            'action': action,
            'button': button,
            'coordinates': (point_x, point_y),
            'screens': [shot, cshot]
        }
        self.events[timestamp] = report
        return report

    def record_mouse_move(self, point_x, point_y, timestamp):
        """ Records the mouse moves.

        Takes the $point_x and $point_y coordinates where the mouse has moved
        and the $timestamp of the event. """
        # Moving the mouse is not so much important, but we need it to interpret
        # some of the "superevents", such as dragging the mouse. Therefore,
        # we still want to record it.
        report = {
            'type': 'mouse',
            'action': 'move',
            'coordinates': (point_x, point_y)
        }
        self.events[timestamp] = report
        return report

    def record_key_press(self, key, timestamp, release=False):
        """ Records the key events (presses and releases) and divides them into several groups.

        Takes the $key (str), the $timestamp and $release (bool) to distinguis between presses
        and releases."""
        shot = cshot = None
        if not release:
            action = 'press'
            # We do not want to take screenshots for alphanumeric keys, because
            # that would require a lot of screenshots to be taken as, when typing,
            # many keys are used without any effects on the screen. We only
            # take a screenshots for special keys, modifiers, and the tab key.
            if key in self.specials or key in self.modifiers or key == "tab" or key == self.stop_key:
                camera.save_screenshot(timestamp, self.time_offset)
                shot = self.name_shot(timestamp)
                cshot = self.name_shot(timestamp + self.time_offset)
        if release:
            action = 'release'
            # Sometimes, when a modifier is pressed, it can take some time to press
            # all the necessary keys in the combination and, especially, it the offset
            # is set too short, the corrected shot to display the result of the action,
            # could actually come prior to that. Therefore, we also take a screenshot,
            # when the modifiers are released.
            if key in self.modifiers:
                camera.save_screenshot(timestamp, self.time_offset)
                shot = self.name_shot(timestamp)
                cshot = self.name_shot(timestamp + self.time_offset)
        # We want to divide key actions into several groups.
        if key is None:
            tipe = 'non-mapped'
            key = 'silent'
        elif key == self.stop_key:
            tipe = 'stop'
        elif key in self.modifiers:
            tipe = 'modifier'
        elif key in self.specials:
            tipe = 'special'
        else:
            tipe = 'alphanumeric'

        report = {
            'type': 'key',
            'subtype' : tipe,
            'action': action,
            'key': key,
            'screens': [shot, cshot]
        }
        self.events[timestamp] = report
        return report

    def clean_recording(self):
        self.events = {}

class Collector:
    """ Collects the events from mouse and keyboard.

    This class controls the keyboard and mouse pynput listeners to gather information
    on various events. """

    def __init__(self, stop_key="f10", time_offset=1, queue=None):
        """ Initates the class variables and starts the listeners.

        Take $stop_key (str) which is used to stop the listeners at the end."""
        # Initiates the Handler class
        self.handler = Handler(stop_key, time_offset)
        self.stop_key = stop_key
        self.powered = False
        if stop_key == "gui":
            self.powered = True
        self.interrupt = False
        if queue:
            self.queue = queue
        else:
            self.queue = None
        # Start the key and mouse listeners to listen to events. Events will be
        # dropped until $self.powered becomes True.

    def start(self):
        if self.stop_key == "gui":
            self.powered = True
        self.handler.clean_recording()
        with MouseListener(on_move=self.on_mouse_move,
                           on_click=self.on_mouse_click,
                           on_scroll=self.on_mouse_scroll) as self.mlistener, \
             KeyListener(on_press=self.on_key_press,
                         on_release=self.on_key_release) as self.klistener:
            self.mlistener.join()
            self.klistener.join()

    def stop(self):
        """ Stop everything and return output. """
        self.powered = False
        self.mlistener.stop()
        self.klistener.stop()
        self.handler.record_key_press(self.stop_key, time.time())
        time.sleep(1) # To let the screenshotter finish its job.

    def get_key_name(self, key):
        """ Convert the Key into a string.

        While with special key, we want to record their exact names, with normal keys
        we prefer the single characters.
        Takes the key object from returned by the keyboard listener. """
        if isinstance(key, KeyCode):
            key_name = key.char
        else:
            key_name = str(key).split('.')[1]
        return key_name

    def return_report(self, beautiful=False):
        """ Returns the final report dictionary.

        If $beautiful is set, the json will be formatted."""
        raw = self.handler.events
        if beautiful:
            report = json.dumps(raw, indent=4, ensure_ascii=False)
            if self.queue:
                self.queue.put(report)
        else:
            report = raw
            if self.queue:
                self.queue.put(report)
        return report

    def on_mouse_move(self, point_x, point_y):
        """ Define actions in case the mouse moves. """
        if self.powered:
            self.handler.record_mouse_move(point_x, point_y, time.time())

    def on_mouse_click(self, point_x, point_y, button, pressed):
        """ Define actions in case someone uses the mouse buttons. """
        if self.powered:
            if pressed:
                self.handler.record_mouse_click(point_x, point_y, button, time.time())
            else:
                self.handler.record_mouse_click(point_x, point_y, button, time.time(), release=True)

    def on_mouse_scroll(self, point_x, point_y, delta_x, delta_y):
        """ Define actions in case someone scrolls the mouse. """
        if self.powered:
            self.handler.record_wheel_scroll(point_x, point_y, delta_x, delta_y, time.time())

    def on_key_press(self, key):
        """ Define actions when a key is pressed. """
        key = self.get_key_name(key)
        if self.powered:
            self.handler.record_key_press(key, time.time())

    def on_key_release(self, key):
        """ Define actions when a key is released. """
        key = self.get_key_name(key)
        if key == self.stop_key and self.powered:
            #self.mlistener.stop()
            #self.klistener.stop()
            self.stop()
            print("Event recording has stopped. You are safe now.")
        elif key == self.stop_key and not self.powered:
            self.powered = True
            print("Event recording has started. Watch your steps.")
        elif self.powered:
            self.handler.record_key_press(key, time.time(), release=True)



#================================================================================

def signal_handler(signum, frame):
    """ Override the SIGINT to block the CTRL-C combination from terminating the script. """
    print("The Ctrl-C combination has been recorded, but its function blocked.")
    print("To end the event tracker, hit the stop key (F10 by default).")

def main():
    """ Main method of event_handler. For running independently. """
    # Fix handling the Ctrl_C SIGINT
    signal.signal(signal.SIGINT, signal_handler)
    # Invoke the Handler class and do starting routines.
    magicbox = Handler("f10", gui=False)
    # Invoke the Collector class
    events = Collector(magicbox)
    # Return the recorded raw report
    report = events.return_report()
    # Interpret the report into something more readable
    i = interpreter.Interpreter(report)
    print(report)

if __name__ == '__main__':
    main()
