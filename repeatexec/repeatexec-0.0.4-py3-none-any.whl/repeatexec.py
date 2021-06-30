import sys
import time
import os


def option_check():
    if len(sys.argv) < 3:
        print("Usage: repeatexec -n 10 -e ls")
        print("will run 'ls' command every 10 seconds")
        return False
    if '-n' not in sys.argv:
        print('no option -n')
        return False
    if '-e' not in sys.argv:
        print('no option -e')
        return False

    if sys.argv.index('-n') > sys.argv.index('-e'):
        print('-n must before -e')
        return False
    try:
        sec_i = sys.argv.index('-n') + 1
        int(sys.argv[sec_i])
    except:
        print('ivalid number after -n')
    return True


def run_command(_command):
    os.system(_command)


def repeate_exec():
    if not option_check():
        return
    sec_i = sys.argv.index('-n') + 1
    cmd_i = sys.argv.index('-e') + 1
    sleep_seconds = int(sys.argv[sec_i])
    command = sys.argv[cmd_i:]
    command = ' '.join(command)
    print('commands:', command)
    print(f'interval: {sleep_seconds}s')
    while True:
        run_command(command)
        time.sleep(sleep_seconds)


if __name__ == '__main__':
    repeate_exec()
