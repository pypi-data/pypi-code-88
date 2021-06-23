# ~/cerebstats/cerebstats/stat_scores/fisherExactScore_test_with_datasets.py
import unittest
import quantities as pq
import numpy as np

from fisherExactScore import FisherExactScore as FExScore

from pdb import set_trace as breakpoint

class FisherExactScoreTest(unittest.TestCase):

    def setUp(self):
        self.herb_vs_cold_herb_group = {
            # reversing letter orders "S" and "Q", tendency to pick first choice?
            "sample_size": 10, # number of people taking echinacea herb
            "success_numbers": 1} # number of people getting cold after taking it
        self.herb_vs_cold_placebo_group = {
            # do fewer than 20% experience medication side effects
            "sample_size": 10, # number of people taking placebo
            "success_numbers": 4} # number of people with cold
        self.butterflyformat_vs_mistakes_butterfly_group = {
            # if feet don't match, is right more likely to be longer or shorter?
            "sample_size": 55, # number of voters using butterfly format ballot paper
            "success_numbers": 4} # number of people choosing wrong candidate
        self.butterflyformat_vs_mistakes_onecolumn_group = {
            # experiment of sender trying to transmit image to receiver via ESP
            "sample_size": 52, # number of voters using single column paper
            "success_numbers": 0} # number of people choosing wrong candidate

    #@unittest.skip("reason for skipping")
    def test_1_herb_vs_cold_rightsided(self):
        # what is the probability that only
        # self.herb_vs_cold_herb_group["success_numbers"] or fewer with cold
        # will be in the herb group by chance?
        x = FExScore.compute( self.herb_vs_cold_placebo_group,
                              self.herb_vs_cold_herb_group, "greater_than" )
        #
        self.assertEqual( [x["test_statistic"], round(x["p_value"], 3)],
                          [0.1, 0.152] )

    #@unittest.skip("reason for skipping")
    def test_2_ballotformat_vs_wrongcandidate_leftsided(self):
        # what is the probability that all
        # self.butterflyformat_vs_mistakes_butterfly_group["success_numbers"]
        # were randomly selected to use the butterfly ballot paper?
        x = FExScore.compute( self.butterflyformat_vs_mistakes_onecolumn_group,
                              self.butterflyformat_vs_mistakes_butterfly_group,
                              "less_than" )
        #
        self.assertEqual( [x["test_statistic"], round(x["p_value"], 4)],
                          [4./55, 0.0661] )

if __name__ == "__main__":
    unittest.main()
