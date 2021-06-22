# SPDX-License-Identifier: GPL-3.0-or-later

# Copyright (C) 2020 Michał Góral.

from i3ipc.aio import Connection
from i3ipc import Event

import sys
import asyncio
import signal
import collections
import functools
import argparse
import subprocess
import logging as log
import re

from i3a._version import version

DEFAULT_PARENTS = ['kitty', 'alacritty', 'st', 'XTerm', 'foot']

Window = collections.namedtuple('Window', ('pid', 'ppid', 'winid', 'pwinid'))


def prepare_args():
    parser = argparse.ArgumentParser(
        description='i3a-swallow - automatic swallowing of child windows')

    parser.add_argument('-e', '--exclude-class', action='append', dest='excluded',
        help='class/app_ids of windows which shouldn\'t trigger swallowing of '
             'their parents. Empty by default, can be given more than once')
    parser.add_argument('-p', '--parent', action='append', dest='parents',
        help='class/app_ids of parent windows whose children should be '
            'swallowed; By default contains some popular terminals. Can be '
            'given more than once')
    parser.add_argument('--debug', action='store_true')

    return parser.parse_args()


def compile_re(patterns):
    return [re.compile(pat) for pat in patterns]


def class_or_app_id(cont):
    return cont.app_id if cont.app_id else cont.window_class


def has_any_class(cont, classes):
    app_id_or_class = class_or_app_id(cont)
    if not app_id_or_class:
        log.warning('Window {} (winid: {}): no app_id/class'.format(
            cont.window_title, cont.id))
        return False

    return any(c.search(app_id_or_class) for c in classes)

def ps_ppid(pid):
    cmd = ['ps', '-q', str(pid), '-o', 'ppid=']
    cp = subprocess.run(cmd, text=True, capture_output=True)
    if cp.returncode != 0:
        return None
    return int(cp.stdout.strip())

def ps_ppids(pid):
    '''Finds all parents of a given PID, in case there's intermediate parent
    (e.g. a shell running in WM-managed terminal window)'''
    ppids = []

    curr = pid
    while curr and curr != 1:
        curr = ps_ppid(curr)
        if curr and curr != 1:
            ppids.append(curr)

    return ppids


def xprop_pid(xwin_id):
    cmd = ['xprop', '-id', str(xwin_id), '_NET_WM_PID']
    cp = subprocess.run(cmd, text=True, capture_output=True)
    if cp.returncode != 0:
        return None
    _, _, pid = cp.stdout.partition('=')
    return int(pid.strip())


def get_pid(cont):
    if hasattr(cont, 'pid') and cont.pid:  # sway
        return cont.pid
    return xprop_pid(cont.window)  # i3


class Swallower:
    def __init__(self, args):
        self.args = args
        self.managed = {}

    async def win_new(self, i3, e):
        if has_any_class(e.container, self.args.excluded):
            log.debug('excluded swallow of {} parent'.format(class_or_app_id(e.container)))
            return

        pid = get_pid(e.container)
        if not pid:
            log.error('couldn\'t get PID for window {}'.format(e.container.id))
            return

        tree = await self.i3.get_tree()
        for ppid in ps_ppids(pid):
            parents = tree.find_by_pid(ppid)

            if not parents:
                continue

            # TODO: under what circumstances can there be 2 or more parents
            # with the same PPID? (mg, 2021-06-21)
            parent = parents[0]
            if not has_any_class(parent, self.args.parents):
                log.debug('excluded swallow of {}'.format(class_or_app_id(parent)))
                return

            self.managed[e.container.id] = parent.id
            log.debug('swallowed {} ({})'.format(class_or_app_id(parent), parent.id))
            await parent.command('move scratchpad')
            return

    async def win_close(self, i3, e):
        parent_id = self.managed.pop(e.container.id, None)
        if not parent_id:
            return

        tree = await self.i3.get_tree()
        pwin = tree.find_by_id(parent_id)
        if pwin:
            scratchpad = pwin.scratchpad()
            if pwin.workspace() == pwin.scratchpad():
                log.debug('unswallowed: {}'.format(parent_id))
                await pwin.command('scratchpad show; floating toggle')
            else:
                log.debug('cannot unswallow win_id={}, which isn\'t on scratchpad'.format(parent_id))

    async def run(self):
        self.i3 = await Connection(auto_reconnect=True).connect()
        self.i3.on(Event.WINDOW_CLOSE, self.win_close)
        self.i3.on(Event.WINDOW_NEW, self.win_new)
        log.debug('i3a-swallow is ready')
        await self.i3.main()


def sigint_handler(sig):
    sys.exit(int(sig))


def main():
    args = prepare_args()

    loglevel = log.DEBUG if args.debug else log.INFO
    log.basicConfig(format='%(message)s', level=loglevel)

    if not args.parents:
        args.parents = DEFAULT_PARENTS

    if not args.excluded:
        args.excluded = []

    log.debug('excluded: {}'.format(', '.join(args.excluded)))
    log.debug('parents: {}'.format(', '.join(args.parents)))

    args.excluded = compile_re(args.excluded)
    args.parents = compile_re(args.parents)

    swallower = Swallower(args)
    loop = asyncio.get_event_loop()
    loop.add_signal_handler(
        signal.SIGINT, functools.partial(sigint_handler, signal.SIGINT))
    loop.run_until_complete(swallower.run())
    return 0
