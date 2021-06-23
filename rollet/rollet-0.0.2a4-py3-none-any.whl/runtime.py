"""
Rollet runtime console script
"""
import argparse
import pandas as pd
from time import sleep
from tqdm import tqdm
from datetime import datetime

from rollet import get_content


def extract_col(link, fields, timesleep = 0, **kwargs):
    try:
        content = get_content(link, **kwargs)
    except:
        content = {
            'title': 'failed',
            'date': datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}
    finally:
        content = [content.get(k) for k in fields]
    return pd.Series(content)


def extract_csv(
    path, link_col,
    fields, **kwargs
):
    path_out = f'{path[:-4]}-output.csv' if not kwargs.get('outfile') else kwargs['outfile']
    start = kwargs.get('start', 0)
    size = None if kwargs.get('size', -1) < 0 else kwargs.get('size', 100)
    timesleep = kwargs.get('timesleep', 0)
    df = pd.read_csv(path, nrows = size, skiprows = lambda x: x>1 and x<=start)
    tqdm.pandas()
    df[fields] = df[link_col].progress_apply(
        extract_col,
        args = (fields, timesleep,),
        blacklist = kwargs.get('blacklist', True),
        timeout = kwargs.get('timeout', 1)
    )
    df.to_csv(path_out, index = False)


def rollet_extract():
    parser = argparse.ArgumentParser(prog = 'rollet')
    parser.add_argument(
        'extract',
        choices = ['extract-txt', 'extract-csv', 'extract-json'],
        help = 'Choose file type option extraction')
    parser.add_argument('path', help = 'file path')
    parser.add_argument(
        '-o', '--outfile', nargs = '?',
        help = 'output file path')
    parser.add_argument(
        '-l', '--link', nargs = '?',
        help = 'link field if csv or json')
    parser.add_argument(
        '-f', '--fields', nargs = '?',
        default = "status,title,abstract,lang,content_type,date",
        help = 'fields to keep separated by comma')
    parser.add_argument(
        '--start', nargs = '?', default = 0, type = int,
        help = 'number of rows to skip')
    parser.add_argument(
        '--size', nargs = '?', default = -1, type = int,
        help = 'max number of rows to keep')
    parser.add_argument(
        '-t', '--timesleep', nargs = '?', default = 0,
        help = 'sleep time in seconds between two pulling')
    parser.add_argument(
        '--timeout', nargs = '?', default = 1.0, type = float,
        help = 'Max GET request timeout in second')
    parser.add_argument(
        '--blacklist', nargs = '?', default = '1',
        help = '0 (do not use), 1 (use), path (one column domain blacklist file)'
    )

    args = parser.parse_args()
    args.timesleep = float(args.timesleep)
    args.fields = args.fields.split(',')
    if (args.extract != 'extract-txt') and not args.link:
        raise ValueError(
            """The --links field name must be filled in
            if the data is not a text column extract-txt""")
    if args.blacklist.isdigit():
        blacklist = bool(int(args.blacklist))
    else:
        with open(args.blacklist, errors = 'ignore') as f:
            blacklist = list(map(lambda x:x.strip(), f.readlines()))

    if args.extract == "extract-csv":
        extract_csv(
            args.path, args.link, args.fields,
            start = args.start,
            size = args.size,
            outfile = args.outfile,
            timesleep = args.timesleep,
            blacklist = blacklist,
            timeout = float(args.timeout)
        )
    
    else:
        raise NotImplementedError('other extraction format is not supported yet')