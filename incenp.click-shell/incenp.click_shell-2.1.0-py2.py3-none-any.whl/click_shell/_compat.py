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

# pylint: disable=unused-import

import click

# Handle changes in Click's shell completion code
try:
    # Click >= 6.4, Click < 8.0
    from click._bashcomplete import get_choices
except ImportError:
    try:
        # Click < 6.4
        from click._bashcomplete import resolve_ctx
    except ImportError:
        # Click >= 8.0
        from click.shell_completion import _resolve_context

        def resolve_ctx(cli, prog_name, args):
            return _resolve_context(cli, {}, prog_name, args)

    # The click._bashcomplete:get_choices function from Click 6.4 to 8.0
    def get_choices(cli, prog_name, args, incomplete):
        ctx = resolve_ctx(cli, prog_name, args)

        if ctx is None:
            return

        choices = []
        if incomplete and not incomplete[:1].isalnum():
            for param in ctx.command.params:
                if not isinstance(param, click.Option):
                    continue
                choices.extend(param.opts)
                choices.extend(param.secondary_opts)
        elif isinstance(ctx.command, click.MultiCommand):
            choices.extend(ctx.command.list_commands(ctx))

        for item in choices:
            if item.startswith(incomplete):
                yield item
