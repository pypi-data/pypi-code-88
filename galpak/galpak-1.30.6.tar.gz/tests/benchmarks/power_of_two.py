import benchmark
import numpy as np

#Benchmark Report
#================
#
#BenchmarkPowerOfTwo
#-------------------
#
#                   name | rank |  runs |      mean |        sd | timesBaseline
#------------------------|------|-------|-----------|-----------|--------------
#       double asterisks |    1 | 1e+05 | 3.889e-05 |  4.66e-06 |           1.0
#explicit multiplication |    2 | 1e+05 | 4.024e-05 | 9.693e-06 | 1.03474171064
#            numpy power |    3 | 1e+05 | 0.0004267 | 2.959e-05 | 10.9717454015
#
#Each of the above 300000 runs were run in random, non-consecutive order by
#`benchmark` v0.1.5 (http://jspi.es/benchmark) with Python 2.7.5+
#Linux-3.11.0-12-generic-x86_64 on 2014-02-13 13:26:33.


class BenchmarkPowerOfTwo(benchmark.Benchmark):

    each = 10000  # configure number of runs

    def setUp(self):
        # Can also specify tearDown, eachSetUp, and eachTearDown
        self.a = np.random.rand(32, 32, 32)

    def test_explicit_multiplication(self):
        b = self.a * self.a

    def test_double_asterisks(self):
        b = self.a ** 2

    def test_numpy_power(self):
        b = np.power(self.a, 2)


if __name__ == '__main__':
    benchmark.main(format="markdown", numberFormat="%.4g")

