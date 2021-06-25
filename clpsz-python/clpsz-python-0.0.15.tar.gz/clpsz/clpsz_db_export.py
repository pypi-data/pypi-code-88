import os
import errno
import shutil
from multiprocessing import Pool

import pymysql
import click


def read_file_as_list(file_path):
    res = []
    with open(file_path, 'r') as f:
        for line in f:
            if line[-1] == os.linesep:
                line = line[:-1]
            res.append(line)
    return res


def get_column_names(conn, db, table):
    cursor = conn.cursor()
    cursor.execute('USE {}'.format(db))
    cursor.execute('DESC {}'.format(table))
    data = cursor.fetchall()
    cursor.close()
    columns = [e[0] for e in data]
    return columns


def dump_all_wrapper(args):
    dump_all(*args)


def dump_all(conn_param, db_tables, exclude_columns, directory):
    conn = pymysql.connect(
        host=conn_param['host'],
        port=conn_param['port'],
        user=conn_param['user'],
        passwd=conn_param['passwd'],
    )
    for db_table in db_tables:
        db, table = db_table.split('.')
        file_path = '{}/{}-{}_dump.csv'.format(directory, db, table)
        dump(conn, db, table, exclude_columns, file_path)
    conn.close()


def dump(conn, db, table, exclude_columns, path):
    columns = get_column_names(conn, db, table)
    for column in exclude_columns:
        if column in columns:
            columns.remove(column)

    cursor = conn.cursor()
    cursor.execute('USE {}'.format(db))
    cursor.execute('SELECT {} FROM {}'.format(','.join(columns), table))
    data = cursor.fetchall()
    cursor.close()
    with open(path, 'w') as f:
        f.write(','.join(columns) + '\n')
        for row in data:
            f.write(','.join([str(e) for e in row]) + '\n')


def create_dir_if_not_exists(path):
    try:
        if os.path.exists(path):
            shutil.rmtree(path)
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))


@click.command()
@click.option('-d', '--db-config-path', 'db_config_path', required=True, help='database config file path, file in json format')
@click.option('-t', '--table-list-path', 'table_list_path', required=True, help='table list file path, file in json format')
@click.option('-o', '--output-dir', 'output_dir', required=True, help='path to output directory')
@click.option('-e', '--exclude-columns', 'exclude_columns', help='columns to exclude, separate by comma')
@click.option('-c', '--concurrent', 'concurrent', type=int, default=1, help='concurrency')
def main(db_config_path, table_list_path, output_dir, exclude_columns, concurrent):
    if exclude_columns is None:
        exclude_columns = {}
    else:
        exclude_columns = set(exclude_columns.split(','))

    create_dir_if_not_exists(output_dir)

    db_config = read_file_as_list(db_config_path)
    host, port, user, password = db_config[0], db_config[1], db_config[2], db_config[3]
    port = int(port)
    conn_param = dict(
        host=host,
        port=port,
        user=user,
        passwd=password,
    )

    table_list = read_file_as_list(table_list_path)
    if concurrent == 1:
        dump_all(conn_param, table_list, exclude_columns, output_dir)
    else:
        parts = split(table_list, concurrent)
        args = []
        for part in parts:
            args.append((conn_param, part, exclude_columns, output_dir))
        p = Pool(concurrent)
        p.map(dump_all_wrapper, args)


if __name__ == '__main__':
    main()
