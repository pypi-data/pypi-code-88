# ~/cerebstats/cerebstats/stat_scores/zTwoSampleRankSumScore_test_with_datasets.py
import unittest
import quantities as pq
import numpy as np
from scipy.stats import norm

from zTwoSampleRankSumScore import ZScoreForTwoSampleRankSumTest as ZScore

from pdb import set_trace as breakpoint

class ZScoreForTwoSampleRankSumTest_Test(unittest.TestCase):

    def setUp(self):
        self.sample_usa = {"raw_data": [2, 30, 35, 70, 100, 120, 135, 150, 190, 200]}
        self.sample_aus = {"raw_data": [8, 12, 16, 29, 35, 40, 45, 46, 95]}

    #@unittest.skip("reason for skipping")
    def test_1_orderdata_ranks(self):
        ordered_data, all_ranks = ZScore.orderdata_ranks(self.sample_usa, self.sample_aus)
        a = ( list(ordered_data) == 
                [2, 8, 12, 16, 29, 30, 35, 35, 40, 45, 46, 70, 95, 100,
                 120, 135, 150, 190, 200] )
        b = ( all_ranks ==
                [1, 2, 3,   4,  5,  6,7.5,7.5,  9, 10, 11, 12,  13, 14,
                  15,  16,  17,  18,  19] )
        self.assertTrue( a and b is True )

    #@unittest.skip("reason for skipping")
    def test_2_sample1_ranks(self):
        ranks_for_sample1 = ZScore.get_observation_rank(self.sample_usa, self.sample_aus)
        #print(ranks_for_sample1)
        self.assertEqual( list(ranks_for_sample1),
                          [ 1, 6, 7.5, 12, 14, 15, 16, 17, 18, 19] )

    #@unittest.skip("reason for skipping")
    def test_3_twosample_data(self):
        x = ZScore.compute(self.sample_usa, self.sample_aus)
        p_value = norm.sf( x["z_statistic"] ) # eta > eta0
        #print(x, p_value)
        # Check answer
        self.assertEqual( [ x["W"], x["mu_W"], round(x["sd_W"], 2),
                            round(x["z_statistic"], 2), round(p_value, 2) ],
                          [125.5, 100, 12.25, 2.08, 0.02] )

if __name__ == "__main__":
    unittest.main()
