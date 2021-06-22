import argparse
from . import move_and_gen




def add_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument('config_file', nargs='?', default=None)

def run(options: argparse.Namespace) -> int:
    worker = move_and_gen.standard_gen(options.config_file)
    if worker.check() == 1:
        return 0
    worker.do_work()
    print("finish.")
    return 0


