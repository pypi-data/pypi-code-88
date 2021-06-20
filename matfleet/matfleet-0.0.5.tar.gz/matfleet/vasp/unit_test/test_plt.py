#   coding:utf-8
#   This file is part of Alkemiems.
#
#   Alkemiems is free software: you can redistribute it and/or modify
#   it under the terms of the MIT License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = '2020/11/10 21:16:09'

import numpy as np
import matplotlib.pyplot as plt
import argparse


def plot_band(fn, k_point, ylim, outputfn=''):

    data = np.loadtxt(fn, dtype=np.float)
    x = data[:, 0]
    y = data[:, 1:]
    plt.figure(1, (15, 8))
    plt.plot(x, y, color='b')
    
    for k in [int(i) for i in k_point.split(',')]:
        plt.plot([x[k]]*100, np.linspace(-1, 1, 100), c='r')
        plt.plot(np.linspace(0, np.max(x), 100), [0]*100, c='r')

    plt.xlim(0, np.max(x))
    assert isinstance(ylim, (tuple, list))
    plt.ylim(ylim)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.98)
    if outputfn:
        plt.savefig(outputfn)
    plt.show()


def run_plot(tmpargs=None):
    from dancingcell.utility.auxbool_argparse import str2list
    m_description = """test plt band"""
    usage = """
        快速绘制band图
    """
    parser = argparse.ArgumentParser(description=m_description, usage=usage)
    parser.add_argument('-f', '--fn', type=str, default='band_data_up.dcdat', help='PORCAR name Default:PROCAR')
    parser.add_argument('-k', '--k_path', type=str, default=None, help='0, 12, 24, 36 ..., split by ","')
    parser.add_argument('-y', '--ylim', type=str2list, default=[-1, 1], help='[-1, 1]')
    parser.add_argument('-o', '--outputfn', type=str, default='', help='output filename')
    args, unparsed = parser.parse_known_args(tmpargs)
    plot_band(fn=args.fn, k_point=args.k_path, ylim=args.ylim, outputfn=args.outputfn)
    
    
if __name__ == '__main__':
    ff = 'band_data_up.dcdat'
    k_index = '0, 27, 54, 92, 138, 175, -1'
    # plot_band(ff, k_index, [-1, 1])
    cmd = ['-f', ff, '-k', k_index, '-y', '[-1, 1]']
    run_plot(cmd)
