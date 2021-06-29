import os
import h5py
from argparse import ArgumentParser

from .utils import check_magic, get_version, VERSION_NA


def _print_msg(msg):
    print(' ', msg)


def _check_report(h5_grp):
    if 'data' not in h5_grp:
        _print_msg('Missing dataset "data": ✗')
        data_ds = None
    else:
        data_ds = h5_grp['data']

    mapping_grp = None
    if 'mapping' not in h5_grp:
        _print_msg('Missing group "mapping": ✗')
        mapping_grp = None
    else:
        mapping_grp = h5_grp['mapping']

    if data_ds is None or mapping_grp is None:
        n_elements = data_ds.shape[1]
        n_steps = data_ds.shape[0]

        # Check mapping



    pass


def is_output_valid(h5_path):
    print('Checking {}'.format(h5_path))

    if not os.path.exists(h5_path) or not h5py.is_hdf5(h5_path):
        print('  ✗  Not a valid hdf5 file, skipping')
        return False

    h5 = h5py.File(h5_path)
    ver = get_version(h5)

    _print_msg('Contains "version" attribute: {} {}'.format('✓', '(' + ver + ')' if ver != VERSION_NA else '✗', ''))
    _print_msg('Contains "magic" attribute: {}'.format('✓' if  check_magic(h5) else '✗'))
    print()

    if 'report' in h5:
        for pop_name, pop_grp in h5['report'].items():
            if isinstance(pop_grp, h5py.Group):
                print('  Found element report for "{}"'.format(pop_name))
                _check_report(pop_grp)
                # print(pop_name, pop_grp)



if __name__ == '__main__':
    parser = ArgumentParser(description='Validate bmtk input and output files')
    parser.add_argument('files', metavar='files', type=str, nargs='+')

    args = parser.parse_args()
    for f in args.files:
        is_output_valid(f)

    # print(args.files)
    # print('HERE')
