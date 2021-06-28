# Author: Botao Yu
import argparse
from .tao_runner import TaoRunner


def add_args(argument_parser):
    argument_parser.add_argument('task_file', type=str)
    argument_parser.add_argument('--log-dir', type=str, default='log')
    argument_parser.add_argument('--save-task-log', action='store_true')


def main():
    parser = argparse.ArgumentParser()
    add_args(parser)

    args = parser.parse_args()

    runner = TaoRunner(args.task_file, log_dir=args.log_dir, save_task_log=args.save_task_log)
    runner.run()


if __name__ == '__main__':
    main()
