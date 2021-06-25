# Copyright (c) 2021 Renata Hodovan, Akos Kiss.
#
# Licensed under the BSD 3-Clause License
# <LICENSE.rst or https://opensource.org/licenses/BSD-3-Clause>.
# This file may not be copied, modified, or distributed except
# according to those terms.

import pytest

from inators import arg as inators_arg

from common_arg import _test_add_argument, MockArgumentParserExit


@pytest.mark.parametrize('func_args, func_kwargs, sys_argv, exp', [
    (['0.0.0'], {}, [], {}),
    (['0.0.0'], {}, ['--version'], MockArgumentParserExit),
    (['0.0.0'], {'short_alias': '-V'}, ['-V'], MockArgumentParserExit),
    (['0.0.0'], {'long_alias': '--revision'}, ['--revision'], MockArgumentParserExit),
])
def test_add_version_argument(func_args, func_kwargs, sys_argv, exp):
    _test_add_argument(inators_arg.add_version_argument, func_args, func_kwargs, sys_argv, exp)
