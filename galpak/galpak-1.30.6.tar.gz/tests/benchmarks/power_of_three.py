import benchmark
import numpy as np

#Benchmark Report
#================
#
#BenchmarkPowerOfThree
#---------------------
#
#                   name | rank |  runs |      mean |        sd | timesBaseline
#------------------------|------|-------|-----------|-----------|--------------
#explicit multiplication |    1 | 1e+04 | 0.0002208 | 4.511e-05 |           1.0
#            numpy power |    2 | 1e+04 |  0.003243 | 0.0002166 | 14.6868697001
#       double asterisks |    3 | 1e+04 |  0.003244 | 0.0002177 |  14.692235388
#
#Each of the above 30000 runs were run in random, non-consecutive order by
#`benchmark` v0.1.5 (http://jspi.es/benchmark) with Python 2.7.5+
#Linux-3.11.0-12-generic-x86_64 on 2014-02-13 14:45:30.


class BenchmarkPowerOfThree(benchmark.Benchmark):

    each = 10000  # configure number of runs

    def setUp(self):
        # Can also specify tearDown, eachSetUp, and eachTearDown
        self.a = np.random.rand(32, 32, 32)

    def test_explicit_multiplication(self):
        b = self.a * self.a * self.a

    def test_double_asterisks(self):
        b = self.a ** 3

    def test_numpy_power(self):
        b = np.power(self.a, 3)


if __name__ == '__main__':
    benchmark.main(format="markdown", numberFormat="%.4g")

