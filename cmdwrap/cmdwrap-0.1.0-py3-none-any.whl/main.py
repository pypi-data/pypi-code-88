import sys
from subprocess import run
import piest.dict as pdict
import piest.list as plist

def _route(d, args):
    head, rest = plist.head_rest(args)

    if head in d.keys():
        v, vt = pdict.value_type(d, head)

        if vt == str:
            args[0] = v
        elif vt == dict:
            args[1:] = _route(v, rest)
        elif vt == tuple:
            args[0], new_d = v
            args[1:] = _route(new_d, rest)
        elif callable(vt):
            v(*rest)
            sys.exit(0)

    return args

def _get_args_options():
    return plist.divide(sys.argv[1:], '--')

def main(routing, cmd = None):
    args, (option, *_) = _get_args_options()
    args = _route(routing, args)
    args = plist.flat_splits(args)

    if cmd:
        run([*cmd.split(), *args])
    elif len(args) > 0:
        run([*args])

