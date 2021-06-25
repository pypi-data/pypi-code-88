import numpy as np
import benchmark

#Benchmark Report
#================
#
#Benchmark numpy nan to num
#--------------------------
#
#       name | rank |  runs |      mean |        sd | timesBaseline
#------------|------|-------|-----------|-----------|--------------
#key mapping |    1 | 1e+04 | 0.0001705 |  1.39e-05 |           1.0
# nan to num |    2 | 1e+04 |  0.000952 | 0.0002365 | 5.58281984443
#
#Each of the above 20000 runs were run in random, non-consecutive order by
#`benchmark` v0.1.5 (http://jspi.es/benchmark) with Python 2.7.5+
#Linux-3.11.0-12-generic-x86_64 on 2014-01-27 10:33:55.


class Benchmark_numpy_nan_to_num(benchmark.Benchmark):

    each = 10000  # configure number of runs

    def setUp(self):
        # Can also specify tearDown, eachSetUp, and eachTearDown
        self.input = np.random.rand(32, 32, 32)

    def eachSetUp(self):
        self.a = self.input.copy()

    def test_nan_to_num(self):
        self.a = np.nan_to_num(self.a)

    def test_key_mapping(self):
        self.a[np.isnan(self.a)] = 0


if __name__ == '__main__':
    benchmark.main(format="markdown", numberFormat="%.4g")

