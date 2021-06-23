# ~/cerebstats/cerebstats/stat_scores/zWilcoxSignedRank_test_with_datasets.py
import unittest
import quantities as pq
import numpy as np
from scipy.stats import norm

from zWilcoxSignedRankScore import ZScoreForWilcoxSignedRankTest as ZScore

from pdb import set_trace as breakpoint

class ZScoreForWilcoxSignedRankTest_Test(unittest.TestCase):

    def setUp(self):
        # for one sample testing
        self.onesample_data = {"raw_data": pq.Quantity( # observation
                              [125, 118, 123, 120, 135, 129, 117], units = pq.mmHg )}
        self.onesample_eta0 = 120. * pq.mmHg # prediction
        # for paired data
        self.daughters = {"raw_data": pq.Quantity( # observation
                        [64. , 66. , 63. , 67. , 60. , 68. , 67. , 66. , 67. , 65. , 61. ,
                         64. , 68. , 64. , 65.5, 67. , 67. , 62.5, 62. , 62. , 64. , 66. ,
                         65. , 67. , 64.5, 70. , 63. , 65. , 60. , 69. , 64. , 62. , 63. ,
                         64. , 62. , 72. , 63. , 67. , 68. , 64. , 72. , 59.5, 65. , 68. ,
                         61. , 66. , 62.5, 65. , 65. , 63. , 70. , 64. , 63. , 68. , 63.5,
                         67.5, 66. , 66. , 61. , 63. , 61. , 61. , 66. , 63. , 66. , 66. ,
                         68. , 62. , 66. , 62. , 63. , 66. , 66. , 69. , 68. , 64. , 69. ,
                         62. , 65. , 67. , 66. , 63. , 61. , 67. , 67. , 63.5, 60. , 67. ,
                         61. , 64. , 68. , 63. , 62. , 67. , 60. , 64.5, 60.5, 69.5, 66. ,
                         65. , 65. , 63. , 67. , 68. , 68. , 65. , 63. , 62. , 63. , 71. ,
                         63. , 63. , 62. , 63. , 65. , 63. , 65. , 64. , 68. , 64. , 61. ,
                         62. , 66. , 68. , 65. , 69. , 65. , 64. , 64. , 67. , 68. , 73. ],
                         units = pq.inch )}
        self.mothers = pq.Quantity( # prediction
                        [64. , 61. , 62. , 68. , 60. , 67. , 70. , 60. , 68. , 64. , 64. ,
                         63. , 64. , 63. , 62. , 66. , 69. , 65.5, 61. , 57. , 62. , 66. ,
                         64. , 65. , 66. , 65. , 56. , 64. , 64. , 64. , 63. , 62. , 62. ,
                         69. , 62. , 65. , 60. , 69. , 64. , 67. , 70. , 59. , 70. , 60. ,
                         59. , 64. , 67. , 62. , 63. , 61. , 68. , 64. , 65. , 69. , 64. ,
                         70. , 65. , 63. , 61. , 65. , 60. , 60. , 65. , 61. , 62. , 62. ,
                         63. , 62. , 67. , 60. , 62. , 62. , 65. , 66. , 65. , 65. , 67. ,
                         65. , 63. , 64. , 67. , 62. , 66. , 64. , 63. , 65. , 64. , 65. ,
                         59. , 62. , 67. , 65. , 64. , 66. , 62. , 65.5, 62. , 63. , 64. ,
                         64. , 62. , 60. , 65. , 66. , 62. , 63. , 65. , 60. , 66. , 69. ,
                         63. , 63. , 64. , 61. , 67. , 65. , 64. , 58. , 68. , 63. , 62. ,
                         60. , 62. , 66. , 64. , 65. , 69. , 68. , 64. , 62. , 65. , 68. ],
                        units = pq.inch )
        self.paired_data_eta0 = 0

    #@unittest.skip("readon for skipping")
    def test_1_get_ranks(self):
        data = self.onesample_data["raw_data"]
        absdiff = np.abs( data - self.onesample_eta0 )
        ordered_absdiff = np.sort(absdiff)
        ordered_absdiff_no0 = ordered_absdiff[ ordered_absdiff != 0 ]
        #print(ordered_absdiff)
        #print(ordered_absdiff_no0)
        ranks = ZScore.get_ranks( ordered_absdiff_no0 )
        self.assertEqual( ranks, [1, 2.5, 2.5, 4, 5, 6] )

    #@unittest.skip("reason for skipping")
    def test_2_get_Tplus(self):
        data = self.onesample_data["raw_data"]
        Tplus = ZScore.get_Tplus( data, self.onesample_eta0 )
        self.assertEqual( Tplus, 17.5 )

    #@unittest.skip("reason for skipping")
    def test_3_onesample_data(self):
        x = ZScore.compute(self.onesample_data, self.onesample_eta0)
        #print(x)
        # Check answer
        self.assertEqual( [x["Tplus"], x["n_U"]], [17.5, 6] )

    #@unittest.skip("reason for skipping")
    def test_4_paired_data(self):
        x = ZScore.compute(self.daughters, self.mothers)
        eta = np.median( self.daughters["raw_data"] - self.mothers )
        p_value = norm.sf( x["z_statistic"] ) # eta > eta0
        #print(x, eta, p_value)
        # Check answer
        self.assertEqual( [ x["Tplus"], x["n_U"], eta,
                            round(x["z_statistic"], 2), round(p_value, 4) ],
                          [5021.0, 120, 1.0, 3.64, 0.0001] )

if __name__ == "__main__":
    unittest.main()
