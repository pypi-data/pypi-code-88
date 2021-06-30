from . import plt
from .parameters import my_dpi

__all__ = ['save_figures']


def save_figures(id_figures=None, directories=None, formats=None):
    if id_figures is None:
        id_figures = plt.get_fignums()
    n_figures = len(id_figures)

    if directories is None:
        directories = [str(d) for d in id_figures]
    else:
        if not (isinstance(directories, list) or
                isinstance(directories, tuple)):
            directories = [directories]

        n_directories = len(directories)
        if n_figures != n_directories:
            raise ValueError('n_figures and n_directories must be equal.\n'
                             'Now, n_figures = {} and n_directories = {}'.format(n_figures, n_directories))

    if formats is None:
        formats = ['svg']

    # my_dpi = 100
    n_formats = len(formats)
    for i in range(n_figures):

        plt.figure(id_figures[i])

        for j in range(n_formats):
            # plt.subplots_adjust(hspace=hspace)
            directory_i_j = '.'.join([directories[i], formats[j]])
            plt.savefig(directory_i_j, format=formats[j], dpi=my_dpi)
