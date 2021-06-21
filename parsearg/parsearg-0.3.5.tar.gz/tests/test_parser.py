import pytest
from parsearg.parser import (
    ParseArg,
)
from parsearg.utils import (
    underline,
)

def test_ParseArg(get_a_aa_dict):
    # create the parser from the dict (flat tree)
    parser = ParseArg(d=get_a_aa_dict, root_name='root')

    def do_it(node):
        def _do_it(args):
            # generate the argparse.Namespace by parsing the arguments:
            ns     = parser.parse_args(args)

            # perform the associated callback:
            result = ns.callback(ns)

            # display the result:
            print('{}\n{}'.format(underline(f'{args!r}'), result))

        print(underline(f'\n\nNODE :: {node!r}'))
        with pytest.raises(SystemExit):
            _do_it(f'{node} -h')
        print('\n')

        _do_it(f'{node}')
        _do_it(f'{node} -v')
        _do_it(f'{node} -c')
        _do_it(f'{node} -v -c')

    nodes = [
        'A',
        'A B',
        'A BB',
        'A BB C',
        'A BB CC',
        'A BB CCC',
        'AA',
        'AA B',
        'AA BB',
        'AA BB C',
        'AA BB CC',
        'AA BB CCC',
    ]
    list(map(lambda node: do_it(node), nodes))

