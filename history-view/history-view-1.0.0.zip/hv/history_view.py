import argparse
import os
import sys
import pdb
import subprocess
import re
import pyperclip

from .renderer import HistoryRenderer
from .interactions import HistoryInteractor, InteractionResult, INTERACTION

# abstraction layer where console detection needs to kick in and return a list of the console history
# prototype only supports powershell
#  - most recent first
#  - all of it
def get_console_history(search):
    if os.name == "nt":
        with open(
            "{userhome}/AppData/Roaming/Microsoft/Windows/PowerShell/PSReadline/ConsoleHost_history.txt".format(
                userhome=os.environ["USERPROFILE"]
            ),
            "r",
            encoding="utf-8",
        ) as history:
            data = history.readlines()
            data.reverse()
    else:
        raise NotImplementedError("Unsupported combination of shell and OS.")

    if search:
        return [command for command in data if re.search(search, command)]
    else:
        return data


def set_clipboard(command):
    pyperclip.copy(command)


def add_console_history(command):
    if os.name == "nt":
        with open(
            "{userhome}/AppData/Roaming/Microsoft/Windows/PowerShell/PSReadline/ConsoleHost_history.txt".format(
                userhome=os.environ["USERPROFILE"]
            ),
            "a",
            encoding="utf-8",
        ) as history:
            history.write(command + "\r")
    else:
        raise NotImplementedError("Unsupported combination of shell and OS.")


def return_or_exit(command, renderer, copy_to_clip):
    print(os.linesep)

    if copy_to_clip:
        set_clipboard(command)
        sys.exit(0)
    else:
        add_console_history(command)
        result = subprocess.run(command, shell=True, cwd=os.getcwd())
        sys.exit(result.returncode)


def console_loop(renderer, copy_to_clip):
    """
    This loop is the primary driver of the UI experience. Its primary purpose is to
    provide the input <-> renderer interaction loop.
    """
    i_handler = HistoryInteractor()

    while True:
        output = renderer.render_current_frame()
        sys.stdout.write(output)
        sys.stdout.flush()

        input_result = i_handler.wait_for_input()

        if input_result.result is INTERACTION.FRAME_BACK:
            renderer.increment_frame()

        if input_result.result is INTERACTION.FRAME_FORWARD:
            renderer.decrement_frame()

        if input_result.result is INTERACTION.ITEM_SELECTED:
            idx = (
                renderer.selected_index
                if input_result.value == None
                else input_result.result
            )
            command = renderer.get_command(idx)
            return_or_exit(command, renderer, copy_to_clip)

        if input_result.result is INTERACTION.EXIT:
            sys.exit(0)

        if input_result.result is INTERACTION.UNKNOWN:
            print("Unrecognized interaction. Exiting.")
            sys.exit(1)


def console_entry():
    parser = argparse.ArgumentParser(description="Traverse your console history.")

    parser.add_argument("-s", "--search", dest="search", default=None)
    parser.add_argument("--parrot", dest="parrotfy", action="store_true", default=False)
    parser.add_argument("--c", dest="copy_to_clip", action="store_true", default=False)

    args = parser.parse_args()

    data = get_console_history(args.search)
    renderer = HistoryRenderer(data, parrot_mode=args.parrotfy)
    console_loop(renderer, args.copy_to_clip)
