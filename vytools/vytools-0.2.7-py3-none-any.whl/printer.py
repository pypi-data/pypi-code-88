from termcolor import cprint
import os
INFOCOLOR = 'cyan'
SUCCESSCOLOR = 'green'
FAILCOLOR = 'red'
WARNCOLOR = 'yellow'

BUFFER = None
def set_buffer(buffer):
  global BUFFER
  BUFFER = buffer

def printer__(strng, color=None, attrs=None, fp=None):
  if attrs is None: attrs = []
  if fp:
    fp.write(strng+os.linesep)

  if BUFFER is not None:
    BUFFER.append(strng)
  if color or attrs:
    cprint(strng, color=color, attrs=attrs)
  else:
    print(strng)

def print_def(strng, attrs=None, fp=None):
  printer__(strng, attrs=attrs, fp=fp)

def print_plus(strng, fp=None):
  color = WARNCOLOR if strng.endswith('+') else SUCCESSCOLOR
  printer__(strng, color=color, fp=fp)

def print_warn(*argv):
  printer__(' '.join(argv),color=WARNCOLOR)

def print_info(*argv):
  printer__(' '.join(argv),color=INFOCOLOR)

def print_success(*argv):
  printer__(' '.join(argv),color=SUCCESSCOLOR)

def print_fail(*argv):
  printer__(' '.join(argv),color=FAILCOLOR)
