# -*- coding: utf-8 -*-
# incenp.click_shell - A shell extension for Click
# Copyright © 2015 Clark Perkins
# Copyright © 2021 Damien Goutte-Gattat
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
#
# * Neither the name of click-shell nor the names of its contributors
#   may be used to endorse or promote products derived from this
#   software without specific prior permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import logging
import shlex
import traceback
from functools import update_wrapper
from logging import NullHandler
import types

import click

from ._cmd import ClickCmd
from ._compat import get_choices

logger = logging.getLogger(__name__)
logger.addHandler(NullHandler())


def get_invoke(command):
    """Get the Cmd main method from the click command.

    :param command: the click Command object
    :return: the do_* method for Cmd
    :rtype: function
    """

    assert isinstance(command, click.Command)

    def invoke_(self, arg):  # pylint: disable=unused-argument
        try:
            command.main(args=shlex.split(arg),
                         prog_name=command.name,
                         standalone_mode=False,
                         parent=self.ctx)
        except click.ClickException as e:
            e.show()
        except click.Abort:
            # We got an EOF or Keyboard interrupt.  Just silence it
            pass
        except SystemExit:
            # Catch this an return the code instead. All of click's
            # help commands do a sys.exit(), and that's not ideal when
            # running in a shell.
            pass
        except Exception as e:
            traceback.print_exception(type(e), e, None)
            logger.warning(traceback.format_exc())

        # Always return False so the shell doesn't exit
        return False

    invoke_ = update_wrapper(invoke_, command.callback)
    invoke_.__name__ = 'do_%s' % command.name
    return invoke_


def get_help(command):
    """Get the Cmd help function from the click command.

    :param command: the click Command object
    :return: the help_* method for Cmd
    :rtype: function
    """

    assert isinstance(command, click.Command)

    def help_(self):
        extra = {}
        for key, value in command.context_settings.items():
            if key not in extra:
                extra[key] = value

        # Print click's help message
        with click.Context(command, info_name=command.name, parent=self.ctx,
                           **extra) as ctx:
            click.echo(ctx.get_help(), color=ctx.color)

    help_.__name__ = 'help_{}'.format(command.name)
    return help_


def get_complete(command):
    """Get the Cmd complete function for the click command.

    :param command: the click Command object
    :return: the complete_* method for Cmd
    :rtype: function
    """

    assert isinstance(command, click.Command)

    def complete_(self, text, line, begidx, _):
        # Parse the args
        args = shlex.split(line[:begidx])
        # Strip of the first item which is the name of the command
        args = args[1:]

        # Then pass them on to the get_choices method that click uses
        # for completion
        return [choice[0] if isinstance(choice, tuple) else choice
                for choice in get_choices(command, command.name, args, text)]

    complete_.__name__ = 'complete_{}'.format(command.name)
    return complete_


class ClickShell(ClickCmd):

    def add_command(self, cmd, name):
        # Use the MethodType to add these as bound methods to our
        # current instance
        setattr(self, 'do_{}'.format(name),
                types.MethodType(get_invoke(cmd), self))
        setattr(self, 'help_{}'.format(name),
                types.MethodType(get_help(cmd), self))
        setattr(self, 'complete_{}'.format(name),
                types.MethodType(get_complete(cmd), self))


def make_click_shell(ctx, prompt=None, intro=None, hist_file=None):
    assert isinstance(ctx, click.Context)
    assert isinstance(ctx.command, click.MultiCommand)

    # Set this to None so that it doesn't get printed out in usage messages
    ctx.info_name = None

    # Create our shell object
    shell = ClickShell(ctx=ctx, hist_file=hist_file)

    if prompt is not None:
        shell.prompt = prompt

    if intro is not None:
        shell.intro = intro

    for name in ctx.command.list_commands(ctx):
        command = ctx.command.get_command(ctx, name)
        shell.add_command(command, name)

    return shell


class Shell(click.Group):

    def __init__(self, prompt=None, intro=None, hist_file=None,
                 on_finished=None, **attrs):
        attrs['invoke_without_command'] = True
        super().__init__(**attrs)

        # Make our shell
        self.shell = ClickShell(hist_file=hist_file, on_finished=on_finished)
        if prompt:
            self.shell.prompt = prompt
        self.shell.intro = intro

    def add_command(self, cmd, name=None):
        super().add_command(cmd, name)
        name = name or cmd.name
        self.shell.add_command(cmd, name)

    def invoke(self, ctx):
        # Call super() first.  This ensures that we call the method body
        # of our instance first, in case it's something other than `pass`
        ret = super().invoke(ctx)

        if not ctx.protected_args and not ctx.invoked_subcommand:
            # Set this to None so that it doesn't get printed out in
            # usage messages
            ctx.info_name = None

            self.shell.ctx = ctx

            return self.shell.cmdloop()

        return ret


def shell(name=None, **attrs):
    """Creates a new :class:`Shell` with a function as callback.

    This works otherwise the same as :func:`command` just that the `cls`
    parameter is set to :class:`Shell`.
    """

    attrs.setdefault('cls', Shell)
    return click.command(name, **attrs)
