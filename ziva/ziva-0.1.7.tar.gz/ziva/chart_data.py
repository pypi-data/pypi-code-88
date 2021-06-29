import os
import sys

import dateutil.parser
from parser import ParserError
from datetime import datetime


def get_plotly_data(filepaths, parse_filename=True):
    """Get data for plotly from filepaths
    :param parse_filename: Parse filename to device and channel. Use full filename if false
    """

    traces = []
    for file in filepaths:
        if file.endswith('dJ'):
            traces += dj_to_plotly(file)
        if file.endswith('txt') or file.endswith('dtv'):
            traces += dtv_to_plotly(file, parse_filename=parse_filename)
    return traces


def dtv_to_plotly(filepath, parse_filename=True) -> list:
    """ Get plotly ready data from the file of type dtv (can also be txt)"""

    if not filepath:
        raise AttributeError('File is invalid')

    with open(filepath, 'r') as f:
        lines = f.readlines()

    if not filepath.endswith('dtv') and not filepath.endswith('txt'):
        raise AttributeError('File is invalid')

    # Split filepath by `_`. First arg is device, last is channel
    dev_id_split = os.path.splitext(os.path.basename(filepath))[0].split('_')
    if len(dev_id_split) >= 2 or not parse_filename:
        dev_id = f"{dev_id_split[0]}_{dev_id_split[-1]}"
    else:
        dev_id = "".join(dev_id_split)

    data = []
    for line in lines:
        if len(line.split(',')) == 2:
            ts = line.split(',')[0].strip()
            val = line.split(',')[1].strip()
            try:
                dt = datetime.strptime(ts, "%d/%m/%Y %H:%M:%S")
            except ValueError:
                # Invalid datetime string
                continue
            data.append((str(dt), val))

    # Order data by timestamp in ascending order
    data = sorted(data, key=lambda t: t[0])

    # Prepare traces for plotly
    traces = []
    x, y = zip(*data)
    traces = [{
        'x': x,
        'y': y,
        'name': dev_id,
        'type': 'scatter',
        'mode': 'lines+points',
    }]

    return traces


def dj_to_plotly(filepath) -> list:
    """Get plotly ready data from the file of type `dJ`"""

    if not filepath:
        raise AttributeError('File is invalid')

    with open(filepath, 'r') as f:
        lines = f.readlines()

    if not filepath.endswith('dJ'):
        raise AttributeError('File is invalid')

    header = {}
    for line in lines:
        if line.find('=') > -1:
            header[line.split('=')[0]] = line.split('=')[1].strip()
        elif line.strip() == '$DATA':
            break

    data = {}
    for line in lines:
        if len(line.split(',')) >= 2:
            ts = line.split(',')[0]
            values = line.split(',')[1:]
            try:
                dt = dateutil.parser.parse(ts)
            except ParserError:
                # Invalid datetime string
                continue
            for i, val in enumerate(values):
                try:
                    val = val.strip()
                    val = eval(val)
                except (NameError, SyntaxError):
                    # Invalid val
                    continue
                if f'CHAN_NAME{i}' not in data:
                    data[f'CHAN_NAME{i}'] = []
                data[f'CHAN_NAME{i}'].append((str(dt), val))

    # Order data by timestamp in ascending order
    for key, val in data.items():
        data[key] = sorted(val, key=lambda t: t[0])

    # Prepare data for plotly
    traces = []
    for key, val in data.items():
        x, y = zip(*val)
        traces.append({
            'x': x,
            'y': y,
            'name': header[key],
            'type': 'scatter',
            'mode': 'lines+points',
        })
    return traces


if __name__ == '__main__':
    file = sys.argv[1]
    print(get_plotly_data([file]))
