# ~/cerebstats/cerebstats/stat_scores/zSignScoreTest.py
import unittest
import quantities as pq
import numpy as np
from scipy.stats import norm

from zSignScore import ZScoreForSignTest as ZScore

from pdb import set_trace as breakpoint

class ZScoreForSignTest_Test(unittest.TestCase):

    def setUp(self):
        # for one sample testing
        self.onesample_data = {"raw_data": pq.Quantity( # observation
                           [97.4, 97.8, 98.2, 98.2, 98.2, 98.2, 98.6, 98.6, 99.0,
                            97.1, 97.6, 98.0, 98.4, 98.4, 99.2, 99.7, 97.15, 98.5],
                           units = pq.degF )}
        self.onesample_eta0 = 98.6 * pq.degF # prediction
        # for paired data
        self.sons = {"raw_data": pq.Quantity( # observation
                        [69.  , 72.  , 69.  , 74.  , 72.  , 70.  , 71.  , 68.  , 71.  ,
                         69.  , 69.  , 68.  , 68.  , 72.  , 64.  , 76.  , 68.  , 68.  ,
                         70.  , 69.  , 67.  , 76.5 , 72.  , 64.  , 70.  , 68.  , 73.  ,
                         76.5 , 64.  , 71.  , 73.  , 72.  , 71.  , 65.  , 69.  , 66.  ,
                         68.  , 67.  , 70.  , 70.  , 65.  , 70.  , 72.  , 70.  , 71.  ,
                         71.  , 72.  , 70.  , 68.  , 71.  , 72.  , 63.  , 69.  , 72.  ,
                         67.75, 70.  , 67.  , 74.  , 73.  , 66.  , 74.  , 70.  , 72.  ,
                         70.  , 75.  , 74.  , 70.  , 74.  , 72.  , 72.  , 73.  , 72.  ,
                         73.  , 74.  , 68.  , 63.  ], units = pq.inch )}
        self.fathers = pq.Quantity( # prediction
                       [68. , 69. , 69. , 76. , 72. , 74. , 73. , 73. , 67. , 64. , 65. ,
                        65. , 67. , 71. , 64. , 78. , 65. , 69. , 69. , 32. , 70. , 73.5,
                        68. , 63. , 70. , 68. , 72. , 72. , 60. , 70. , 67. , 72. , 65. ,
                        65. , 72. , 64. , 65. , 65. , 72. , 68. , 68. , 69. , 70. , 71. ,
                        67. , 68. , 64. , 67. , 73. , 73. , 67. , 63. , 65. , 75. , 66. ,
                        73. , 65. , 72. , 74. , 71. , 72. , 71. , 69. , 73. , 76. , 74. ,
                        68. , 65. , 69. , 72. , 69. , 68. , 67. , 74. , 66. , 66. ],
                        units = pq.inch )
        self.paired_data_eta0 = 0

    #@unittest.skip("reason for skipping")
    def test_1_onesample_data(self):
        x = ZScore.compute(self.onesample_data, self.onesample_eta0)
        below = (self.onesample_data["raw_data"] < self.onesample_eta0).sum()
        equal = (self.onesample_data["raw_data"] == self.onesample_eta0).sum()
        above = (self.onesample_data["raw_data"] > self.onesample_eta0).sum()
        eta = np.median( self.onesample_data["raw_data"] )
        n = len( self.onesample_data["raw_data"] )
        p_value = 1 - norm.sf( x["z_statistic"] ) # eta < eta0
        #print(x, below, equal, above, eta, n, p_value)
        # Check answer
        self.assertEqual( [below, equal, above, eta, n],
                          [13, 2, 3, 98.2, 18] ) # p=0.0106 exact?

    #@unittest.skip("reason for skipping")
    def test_2_paired_data(self):
        x = ZScore.compute(self.sons, self.fathers)
        data = self.sons["raw_data"] - self.fathers
        below = (data < self.paired_data_eta0).sum()
        equal = (data == self.paired_data_eta0).sum()
        above = (data > self.paired_data_eta0).sum()
        eta = np.median( data )
        p_value = norm.sf( x["z_statistic"] ) # eta > eta0
        #print(below, equal, above, eta, x["z_statistic"], p_value)
        # Check answer
        self.assertEqual(
          [below, equal, above, eta, round(x["z_statistic"], 2), round(p_value, 4)],
          [21, 11, 44, 1.0, 2.85, 0.0022] )

if __name__ == "__main__":
    unittest.main()
