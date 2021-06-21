from parsearg import ParseArg
from parsearg.utils import underline
from parsearg.example_trees import a_dict


view = a_dict()

def main():
    # create the parser from the dict (flat tree)
    parser = ParseArg(d=view, root_name='root')

    def do_it(node):
        def _do_it(args):
            # generate the argparse.Namespace by parsing the arguments:
            ns     = parser.parse_args(args)

            # perform the associated callback:
            result = ns.callback(ns)

            # display the result:
            print('{}\n{}'.format(underline(f'{args!r}'), result))

        print(underline(f'\n\nNODE :: {node!r}'))
        try:
            _do_it(f'{node} -h')
        except SystemExit as e:
            pass
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
    ]
    list(map(lambda node: do_it(node), nodes))


if __name__ == '__main__':
    main()
