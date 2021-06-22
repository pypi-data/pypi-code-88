#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random, sys

import numpy
from scipy import stats
import scipy
import numpy as np
import pandas as pd
import seaborn as sns
import argparse
import time
import logging
import coloredlogs
import collections
import matplotlib.pyplot as plt

from numpy.random import Generator, PCG64
from randomgen.aes import AESCounter
from rtt_data_gen.base import InputSlicer, get_int_reader


logger = logging.getLogger(__name__)
coloredlogs.install(level=logging.INFO)


class Visualizer:
    def main(self):
        rng = Generator(AESCounter(mode='sequence'))

        parser = argparse.ArgumentParser(description='Data spreader - for moduli functions')
        parser.add_argument('--debug', dest='debug', action='store_const', const=True,
                            help='enables debug mode')
        parser.add_argument('--ib', dest='isize', type=int,
                            help='Input block size in bits')
        parser.add_argument('--bins', dest='bins', type=int,
                            help='Input block size in bits')

        args = parser.parse_args()

        islicer = InputSlicer(isize=args.isize, stream=sys.stdin.buffer)
        int_reader = get_int_reader(islicer)

        bins = args.bins or 100_000
        binwidth = 2**args.isize // bins

        ctrr = collections.Counter()
        for x in range(bins):
            ctrr[x*binwidth] = 0

        acc = list(int_reader())
        for val in acc:
            binname = int((val // binwidth) * binwidth)
            ctrr[binname] += 1

        logger.info('Read %s elements, bins: %s' % (len(acc), bins))
        logger.info('c1 c2: %s %s %s' % (acc[0], acc[1], type(acc[0])))

        # hist = numpy.histogram(acc, bins=bins)

        hist_vals = [x[1] for x in sorted(ctrr.items())]
        # print(hist_vals, ctrr.keys())

        plt.figure(figsize=(16, 12))
        sns.lineplot(x=list(range(len(hist_vals))), y=hist_vals)
        plt.savefig('res.png')
        # plt.show()
        print('Graph generated', time.time())


def main():
    br = Visualizer()
    return br.main()


if __name__ == '__main__':
    main()
