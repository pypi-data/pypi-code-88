from pynput import keyboard
from typing import List, Tuple, Set
import logging
import threading

class InputState():
    def __init__(self):
        self.keyboard_state = {}
        self.keys_pressed_events = set()
        self.keys_released_events = set()

        self.last_state = {}
        self.current_state = {}

        self._lock = threading.Lock()
        listener = keyboard.Listener(
            on_press=self._on_press,
            on_release=self._on_release)
        listener.start()

    @property
    def pressed_keys(self):
        with self._lock:
            return [k for k, v in self.keyboard_state.items() if v == 1]

    def _on_press(self, key):
        try:
            key_val = str(key.char)
            logging.debug(('alphanumeric key {0} pressed'.format(key_val)))
        except AttributeError:
            key_val = str(key)
            logging.debug('special key {0} pressed'.format(key_val))

        with self._lock:
            if self.keyboard_state.get(key_val, 0) == 0:
                self.keys_pressed_events.add(key_val)
            self.keyboard_state[key_val] = 1


    def _on_release(self, key):
        with self._lock:
            try:
                key_val = str(key.char)
                logging.debug(('alphanumeric key {0} released'.format(key_val)))
            except AttributeError:
                key_val = str(key)
                logging.debug('special key {0} released'.format(key_val))

            self.keyboard_state[key_val] = 0
            self.keys_released_events.add(key_val)

    def is_pressed(self, keys):
        pressed = self.pressed_keys.copy()
        return self._check_if_all_are_pressed(pressed, keys)

    @staticmethod
    def _check_if_all_are_pressed(pressed, keys):
        if type(keys) in [List, tuple, set]:
            ret = all(x in pressed for x in keys)
        else:
            ret = keys in pressed
        logging.debug(f"Checking {keys} in {pressed} --> {ret}")
        return ret

    def clear_events(self):
        with self._lock:
            self.keys_pressed_events.clear()
            self.keys_released_events.clear()


