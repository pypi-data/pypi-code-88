import os
import sys
import json
import click
from .udatetime import millisecond_timestamp_to_str


@click.command()
def main():
    main1()


def main1():
    k = 0
    try:
        buff = ''
        while True:
            buff += sys.stdin.read(1)
            if buff.endswith(os.linesep):
                line = buff[:-1]
                print(parse_line(line))
                buff = ''
                k = k + 1
    except KeyboardInterrupt:
        sys.stdout.flush()
        pass
    print('processed {} lines'.format(k))


def parse_line(line):
    try:
        data = json.loads(line)
        is_ddl = data['isDdl']
        db = data['database']
        table = data['table']
        _type = data['type']
        ts = data['ts']
        if is_ddl:
            _len = 0
            res = 'ddl {}.{}'.format(db, table)
        else:
            _len = len(data['data'])
            res = '{} | {} rows affected | {} {}.{}'.format(millisecond_timestamp_to_str(int(ts)), _len, _type, db, table)
        return res
    except Exception as e:
        raise Exception(e)


if __name__ == '__main__':
    pass
