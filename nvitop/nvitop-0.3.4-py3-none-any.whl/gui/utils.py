# This file is part of nvitop, the interactive NVIDIA-GPU process viewer.
# License: GNU GPL version 3.

# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
# pylint: disable=disallowed-name,invalid-name

import sys

from ..core import NA


try:
    if not sys.stdout.isatty():
        raise ImportError
    from termcolor import colored  # pylint: disable=unused-import
except ImportError:
    def colored(text, color=None, on_color=None, attrs=None):  # pylint: disable=unused-argument
        return text


def cut_string(s, maxlen, padstr='...', align='left'):
    assert align in ('left', 'right')

    if not isinstance(s, str):
        s = str(s)

    if len(s) <= maxlen:
        return s
    if align == 'left':
        return s[:maxlen - len(padstr)] + padstr
    return padstr + s[-(maxlen - len(padstr)):]


BLOCK_CHARS = ' ▏▎▍▌▋▊▉'


def make_bar(prefix, percent, width):
    bar = '{}: '.format(prefix)
    if percent != NA:
        if isinstance(percent, str) and percent.endswith('%'):
            percent = percent[:-1]
            percent = float(percent) if '.' in percent else int(percent)
        percentage = float(percent) / 100.0
        quotient, remainder = divmod(max(1, round(8 * (width - len(bar) - 4) * percentage)), 8)
        bar += '█' * quotient
        if remainder > 0:
            bar += BLOCK_CHARS[remainder]
        if isinstance(percent, float) and len('{} {:.1f}%'.format(bar, percent)) <= width:
            bar += ' {:.1f}%'.format(percent)
        else:
            bar += ' {:d}%'.format(int(percent)).replace('100%', 'MAX')
    else:
        bar += '░' * (width - len(bar) - 4) + ' N/A'
    return bar.ljust(width)
