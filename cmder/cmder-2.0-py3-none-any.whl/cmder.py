#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A shortcut for running shell command.
"""

import subprocess
import os
import sys
import shlex
import tempfile

CMD_LINE_LENGTH = 100
PMT = False

try:
    from loguru import logger
    logger.remove()
    logger.add(sys.stderr, format="<level>{message}</level>", filter=lambda record: record["level"].name == "DEBUG")
    logger.add(sys.stderr, format="<light-green>[{time:HH:mm:ss}]</light-green> <level>{message}</level>", level="INFO")
except ImportError:
    import logging
    logging.basicConfig(format='[%(asctime)s] %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logger = logging.getLogger()


def run(cmd, **kwargs):
    """ Run cmd or raise exception if run fails. """
    def format_cmd(command):
        if isinstance(command, str):
            command = shlex.shlex(command, posix=True, punctuation_chars=True)
            command.whitespace_split = True
            command = list(command)
        elif isinstance(command, (list, tuple)):
            command = [str(c) for c in command]
        else:
            raise TypeError('Command only accepts a string or a list (or tuple) of strings.')
        exe = command[0]
        if len(' '.join(command)) <= CMD_LINE_LENGTH:
            return exe, ' '.join(command)
        command = ' '.join([f'\\\n  {c}' if c.startswith('-') or '<' in c or '>' in c else c for c in command])
        command = command.splitlines()
        commands = []
        for i, c in enumerate(command):
            if i == 0:
                commands.append(c)
            else:
                if len(c) <= 80:
                    commands.append(c)
                else:
                    items = c.strip().replace(' \\', '').split()
                    commands.append(f'  {items[0]} {items[1]} \\')
                    for item in items[2:]:
                        commands.append(' ' * (len(items[0]) + 3) + item + ' \\')
        command = '\n'.join(commands)
        if command.endswith(' \\'):
            command = command[:-2]
        return exe, command
    
    def parse_profile():
        try:
            with open(profile_output) as f:
                t, m = f.read().strip().split()
                t = t.split(".")[0]
                try:
                    hh, mm, ss = t.split(':')
                except ValueError:
                    hh, (mm, ss) = 0, t.split(':')
                t = f'{int(hh):02d}:{int(mm):02d}:{int(ss):02d}'
                m = float(m)
                if m < 1000:
                    m = f'{m:.2f}KB'
                elif m < 1000 * 1000:
                    m = f'{m / 1000:.2f}MB'
                else:
                    m = f'{m / 1000 / 1000:.2f}GB'
                s = f'{t} {m}'
        except FileNotFoundError:
            s = '00:00:00 0.00KB'
        return s
    
    msg, pmt, fmt_cmd = kwargs.pop('msg', ''), kwargs.pop('pmt', False), kwargs.pop('fmt_cmd', True)
    log_cmd = kwargs.pop('log_cmd', True)
    if fmt_cmd:
        program, cmd = format_cmd(cmd)
    else:
        if isinstance(cmd, str):
            program, cmd = cmd.split()[0], cmd
        else:
            program, cmd = cmd[0], ' '.join([str(c) for c in cmd])
    if msg:
        logger.info(msg)
    if log_cmd:
        logger.debug(cmd)
    cwd = kwargs.pop('cwd', None)
    profile_output = tempfile.mktemp(suffix='.txt', prefix='.profile.', dir=cwd)
    try:
        if msg and (pmt or PMT):
            cmd = f'/usr/bin/time -f "%E %M" -o {profile_output} {cmd}'
        process = subprocess.Popen(cmd, universal_newlines=True, shell=True, cwd=cwd,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, **kwargs)
        if process.returncode != 0:
            stdout, stderr = process.communicate()
            logger.error(f'Failed to run {program} (exit code {process.returncode}):\n{stderr or stdout}')
            sys.exit(process.returncode)
        if msg:
            msg = msg.replace(' ...', f' complete.')
            if pmt or PMT:
                msg = f'{msg[:-1]} [{parse_profile()}].' if msg.endswith('.') else f'{msg} [{parse_profile()}].'
            logger.info(msg)
    finally:
        if os.path.isfile(profile_output):
            os.unlink(profile_output)
    return process


if __name__ == '__main__':
    pass
