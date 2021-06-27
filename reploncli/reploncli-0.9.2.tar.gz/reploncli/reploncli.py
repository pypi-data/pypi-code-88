import sys
import os
import shlex
import traceback
from cmd import Cmd


class Repl(Cmd):
    def __init__(self, cli_function, prompt="", help=None):
        super().__init__()
        self.cli_function = cli_function
        self.help = help
        self.prompt = str(prompt)
        self._prompt = prompt
        self._update_prompt()

    def _update_prompt(self):
        if callable(self._prompt):
            self.prompt = str(self._prompt())

    def do_help(self, inp):
        if isinstance(self.help, str):
            print(self.help)
        elif callable(self.help):
            self.help()
        self._update_prompt()

    def do_EOF(self, inp):
        print("^D")
        return True

    def emptyline(self):
        self._update_prompt()

    def default(self, inp):
        if inp.startswith(".") and len(inp) > 1:
            os.system(inp[1:])
            self._update_prompt()
            return False
        try:
            self.cli_function(shlex.split(inp))
        except KeyboardInterrupt:
            print("^C")
        except EOFError:
            print("^D")
            return True
        except:
            traceback.print_exc()
        self._update_prompt()
        return False


def reploncli(cli_function, repl_mode=None, help=None, prompt=""):
    if not callable(cli_function):
        raise TypeError("cli_function: callable expected")
    if repl_mode is True:
        repl = Repl(cli_function, prompt, help)
        nothing_worse_than_keyboardinterrupt = True
        while nothing_worse_than_keyboardinterrupt:
            nothing_worse_than_keyboardinterrupt = False
            try:
                repl.cmdloop()
            except KeyboardInterrupt:
                sys.stderr.write("^C\n")
                nothing_worse_than_keyboardinterrupt = True
    else:
        try:
            cli_function()
        except (KeyboardInterrupt, EOFError):
            print()
