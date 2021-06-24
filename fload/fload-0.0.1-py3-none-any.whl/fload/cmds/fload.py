import argparse
import logging
import json
import pkg_resources
import sys
import types

from fload.log import setup_logging

logger = logging.getLogger(__name__)


def load_module(module_name):
    import fload.stream as base_module

    module_class = None
    if hasattr(base_module, module_name):
        module_class = getattr(base_module, module_name)

    if not module_class:
        module_class = load_external_module(module_name)

    if not module_class:
        return None

    module_instance = module_class()
    return module_instance


def load_external_module(module_name):
    for entrypoint in pkg_resources.iter_entry_points('fload_modules'):
        module = entrypoint.load()
        if hasattr(module, module_name):
            module_class = getattr(module, module_name)
            return module_class


def _pop_module_name(argv):
    i = 0
    for arg in argv[1:]:
        if not arg.startswith('-'):
            del argv[i]
            return arg
        i += 1


def main():
    from fload import __version__ as version
    argv = sys.argv

    usage = '%(prog)s module [options]\r\n'
    parser = argparse.ArgumentParser('fload', usage=usage)
    parser.add_argument('-V', '--version', action='version', default=False,
                    version='%(prog)s {version}'.format(version=version))
    # parser.add_argument('module')
    module_name = _pop_module_name(argv)
    # ops = parser.parse_args()
    

    if module_name is None:
        ops = parser.parse_args()
        if not module_name and ops.version:
            print('fload %s' % version)
            sys.exit(0)

        print('Please specify module.')
        parser.print_help()
        sys.exit(1)

    mod = load_module(module_name)
    if mod is None:
        parser.error("module %s not found." % module_name)

    if hasattr(mod, 'add_arguments'):
        getattr(mod, 'add_arguments')(parser)

    parser.usage = f'fload {module_name}'
    ops = parser.parse_args()
    
    if hasattr(mod, 'init'):
        getattr(mod, 'init')(ops)

    setup_logging()

    if hasattr(mod, 'start'):
        for item in run_start(mod):
            print(json.dumps(item))

    if hasattr(mod, 'process'):
        try:
            for line in sys.stdin:
                item = json.loads(line)
                ret = mod.process(item)
                if ret:
                    print(json.dumps(ret))

        except Exception as ex:
            logger.error('Error when processing item %s', item, exc_info=ex)
            sys.exit(1)


def run_start(mod):
    ret = mod.start()
    if not isinstance(ret, types.GeneratorType):
        ret = [ret]
    
    for item in ret:
        yield item


if __name__ == '__main__':
    main()

