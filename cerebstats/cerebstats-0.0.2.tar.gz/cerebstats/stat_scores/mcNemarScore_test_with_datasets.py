# ~/cerebstats/cerebstats/stat_scores/mcNemarScore_test_with_datasets.py
import unittest
import quantities as pq
import numpy as np

from mcNemarScore import McNemarScore

from scipy.stats import binom_test

from pdb import set_trace as breakpoint

class McNemarScoreTest(unittest.TestCase):

    def setUp(self):
        self.satisfied_partner_couple_husband_not_wife = {
            # study of marital satisfaction
            "sample_size": 100, # number of husbands (200 couples)
            "discordant_half": 15} # number of statisfied husbands but not wife
        self.satisfied_partner_couple_wife_not_husband = {
            # study of marital satisfaction
            "sample_size": 100, # number of wives (200 couples)
            "discordant_half": 5} # number of statisfied wives but not husbands
        self.asthma_prevalence_at13_not_20 = {
            # do fewer than 20% experience medication side effects
            "sample_size": 72, # number of people taking placebo
            "discordant_half": 22} # number of people with cold
        self.asthma_prevalence_at20_not_13 = {
            # if feet don't match, is right more likely to be longer or shorter?
            "sample_size": 428, # number of voters using butterfly format ballot paper
            "discordant_half": 8} # number of people choosing wrong candidate

    #@unittest.skip("reason for skipping")
    def test_1_partner_satisfaction_leftsided(self):
        # what is the probability that only
        # self.herb_vs_cold_herb_group["success_numbers"] or fewer with cold
        # will be in the herb group by chance?
        # Ha: p < p0
        x = McNemarScore.compute(
               self.satisfied_partner_couple_husband_not_wife,
               self.satisfied_partner_couple_wife_not_husband )
        # p-value
        p_value = binom_test( x["test_statistic"],
                              x["sample_size"],
                              0.5, # general p0 for McNemar testing
                              "greater" )
        self.assertEqual( [x["test_statistic"], round(p_value, 3)],
                          [5, 0.994] )

    #@unittest.skip("reason for skipping")
    def test_2_asthma_prevalence_rightsided(self):
        # what is the probability that all
        # self.butterflyformat_vs_mistakes_butterfly_group["success_numbers"]
        # were randomly selected to use the butterfly ballot paper?
        #Ha: p > p0
        x = McNemarScore.compute(
               self.asthma_prevalence_at13_not_20,
               self.asthma_prevalence_at20_not_13 )
        # p-value
        p_value = binom_test( x["test_statistic"],
                              x["sample_size"],
                              0.5, # general p0 for McNemar testing
                              "less" )
        self.assertEqual( [x["test_statistic"], round(p_value, 3)],
                          [8, 0.008] )
        # Note that if samples were WRONGLY taken as independent samples
        # and perform z-test, the resultant p-value = 0.094

if __name__ == "__main__":
    unittest.main()
