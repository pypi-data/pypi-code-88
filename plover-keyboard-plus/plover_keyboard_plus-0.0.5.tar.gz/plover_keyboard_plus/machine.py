from plover import _
from plover.machine import keyboard
from plover.oslayer import keyboardcontrol
from plover.oslayer.config import PLUGINS_PLATFORM as PLATFORM

KEYBOARDPLUS_NOT_FOUND_FOR_OS = 'Keyboard Plus does not support platform: %s' % PLATFORM

PLUS_SUPPORTED_KEYS = '\n        F13 F14 F15 F16  F17 F18 F19 F20  F21 F22 F23 F24'

X_KEYCODE_TO_KEY = {
    191: "F13",
    192: "F14",
    193: "F15",
    194: "F16",
    195: "F17",
    196: "F18",
    197: "F19",
    198: "F20",
    199: "F21",
    200: "F22",
    201: "F23",
    202: "F24",
}

if PLATFORM in {'linux', 'bsd'}:
    from plover.oslayer import xkeyboardcontrol

    xkeyboardcontrol.KEYCODE_TO_KEY.update(X_KEYCODE_TO_KEY)
    KEYCODE_TO_KEY = xkeyboardcontrol.KEYCODE_TO_KEY
    xkeyboardcontrol.KEY_TO_KEYCODE = dict(
        zip(KEYCODE_TO_KEY.values(), KEYCODE_TO_KEY.keys()))

    class KeyboardPlusCapture(xkeyboardcontrol.KeyboardCapture):
        SUPPORTED_KEYS_LAYOUT = keyboardcontrol.KeyboardCapture.SUPPORTED_KEYS_LAYOUT.replace(
            'F12', 'F12' + PLUS_SUPPORTED_KEYS, 1)
        SUPPORTED_KEYS = tuple(SUPPORTED_KEYS_LAYOUT.split())
else:
    raise Exception(KEYBOARDPLUS_NOT_FOUND_FOR_OS)

# i18n: Machine name.
_._('Keyboard Plus')


class KeyboardPlus(keyboard.Keyboard):
    KEYS_LAYOUT = KeyboardPlusCapture.SUPPORTED_KEYS_LAYOUT
    ACTIONS = ('arpeggiate', )
    # Ordinarily, we would fall back on Keyboard here
    # Due to the way the fallback code in plover.config::system_keymap_option::build_keymap
    #   works, this will remove all of the extra keys prodided above.
    # KEYMAP_MACHINE_TYPE = 'Keyboard'

    def __init__(self, params):
        super().__init__(params)

    def start_capture(self):
        self._initializing()
        try:
            self._keyboard_capture = KeyboardPlusCapture()
            self._keyboard_capture.key_down = self._key_down
            self._keyboard_capture.key_up = self._key_up
            self._suppress()
            self._keyboard_capture.start()
        except:
            self._error()
            raise
        self._ready()
