# ~/cerebstats/cerebstats/stat_scores/zPropScore_test_with_datasets.py
import unittest
import quantities as pq
import numpy as np
from scipy.stats import norm
from scipy.stats import binom_test

from zPropScore import ZScoreForProportionZTest as ZScore

from pdb import set_trace as breakpoint

class ZScoreForProportionZTest_Test(unittest.TestCase):

    def setUp(self):
        # for one sample testing
        self.order_in_voting_letters = {
            # reversing letter orders "S" and "Q", tendency to pick first choice?
            "sample_size": 190, # number of students
            "success_numbers": 114, # number of students picking the first choice letter
            #"phat": 0.60, # 114/190
            "p0": 0.50 }
        self.side_effect_less_20pc = {
            # do fewer than 20% experience medication side effects
            "sample_size": 400, # number of patients
            "success_numbers": 68, # number of patients with side effects
            #"phat": 0.17, # 68/400
            "p0": 0.20 }
        self.right_vs_left_feet_lengths = {
            # if feet don't match, is right more likely to be longer or shorter?
            "sample_size": 112, # number of people with unequal measurements
            "success_numbers": 63, # number of people reporting longer right foot
            #"phat": 0.5625, # 63/112
            "p0": 0.5 }
        self.is_esp_possible = {
            # experiment of sender trying to transmit image to receiver via ESP
            "sample_size": 164, # number of trials
            "success_numbers": 45, # number of reported successes
            #"phat": 0.2744, # 45/164
            "p0": 0.25 } # 0.25 => random guessing
        self.do_men_looks_over_personality = {
            # students asked if men care more for looks over personality
            "sample_size": 61, # number of men in class
            "success_numbers": 26, # number of yeses
            #"phat": 0.4262, # 26/61
            "p0": 0.5 }
        self.prevent_ear_infection_placebo = {
            # hypothesis that regular sue of sweetener xylitol to prevent ear infection in pre-school children
            "sample_size": 165, # number of children w/ 5x doses placebo syrup
            "success_numbers": 68, # number of children w/ ear infection in 3 months
            }
        self.prevent_ear_infection_xylitol = {
            # hypothesis that regular sue of sweetener xylitol to prevent ear infection in pre-school children
            "sample_size": 159, # number of children w/ 5x doses xylitol syrup
            "success_numbers": 46, # number of children w/ ear infection in 3 months
            }

    #@unittest.skip("reason for skipping")
    def test_1_onesample_data_voting_letter_order_rightsided(self):
        x = ZScore.compute( self.order_in_voting_letters,
                            self.order_in_voting_letters["p0"] )
        # APPROXIMATE p-value
        p_value = norm.sf( x["z_statistic"] ) # p > p0, default
        #p_value = 1 - norm.sf( x["z_statistic"] ) # p < p0
        #print(x, p_value, 1-p_value)
        # Check answer Ha: p > p0
        self.assertEqual( [round(x["sample_statistic"], 2),
                           round(x["z_statistic"],2), round(p_value, 3)],
                          [0.60, 2.76, 0.003] )

    #@unittest.skip("reason for skipping")
    def test_2_onesample_side_effect_less_20pc_leftsided(self):
        x = ZScore.compute( self.side_effect_less_20pc,
                            self.side_effect_less_20pc["p0"] )
        # APPROXIMATE p-value
        #p_value = norm.sf( x["z_statistic"] ) # p > p0, default
        p_value = 1 - norm.sf( x["z_statistic"] ) # p < p0
        #print(x, p_value, 1-p_value)
        # Check answer Ha: p < p0
        self.assertEqual( [round(x["sample_statistic"], 2),
                           round(x["z_statistic"],1), round(p_value, 3)],
                          [0.17, -1.5, 0.067] )

    #@unittest.skip("reason for skipping")
    def test_3_onesample_right_vs_left_feet_lengths_twosided(self):
        x = ZScore.compute( self.right_vs_left_feet_lengths,
                            self.right_vs_left_feet_lengths["p0"] )
        # APPROXIMATE p-value
        #p_value = norm.sf( x["z_statistic"] ) # p > p0, default
        p_value = 2*norm.sf( abs(x["z_statistic"]) ) # p =/= p0
        #print(x, p_value, 1-p_value)
        # Check answer Ha: p < p0
        self.assertEqual( [round(x["sample_statistic"], 4),
                           round(x["z_statistic"],2), round(p_value, 3)],
                          [0.5625, 1.32, 0.186] )

    #@unittest.skip("reason for skipping")
    def test_4_onesample_is_esp_possible_rightsided(self):
        x = ZScore.compute( self.is_esp_possible,
                            self.is_esp_possible["p0"] )
        #p_value = norm.sf( x["z_statistic"] ) # p > p0, default
        #p_value = norm.sf( x["z_statistic"] ) # p > p0
        # EXACT p-value
        p_value = binom_test( self.is_esp_possible["success_numbers"],
                              self.is_esp_possible["sample_size"],
                              self.is_esp_possible["p0"],
                              "greater" ) # better than random (p0 = 0.25)
        #print(x, p_value, 1-p_value, binom_test(45,164,0.25,"greater"))
        # Check answer Ha: p > p0
        self.assertEqual( [round(x["sample_statistic"], 4), round(p_value, 3)],
                          [0.2744, 0.261] )

    #@unittest.skip("reason for skipping")
    def test_5_onesample_do_men_looks_over_personality_leftsided(self):
        x = ZScore.compute( self.do_men_looks_over_personality,
                            self.do_men_looks_over_personality["p0"] )
        # EXACT p-value
        p_value = binom_test( self.do_men_looks_over_personality["success_numbers"],
                              self.do_men_looks_over_personality["sample_size"],
                              self.do_men_looks_over_personality["p0"],
                              "less" )
        #print(x, p_value)
        # Check answer Ha: p < p0
        self.assertEqual( [round(x["sample_statistic"], 4), round(p_value, 3)],
                          [0.4262, 0.153] )

    #@unittest.skip("reason for skipping")
    def test_6_twosample_prevent_ear_infection_rightsided(self):
        x = ZScore.compute( self.prevent_ear_infection_placebo,
                            self.prevent_ear_infection_xylitol )
        p_value = norm.sf( x["z_statistic"] ) # eta > eta0
        #print(below, equal, above, eta, x["z_statistic"], p_value)
        # Check answer
        self.assertEqual( [round(x["sample_statistic"], 3),
                           round(x["z_statistic"], 2), round(p_value, 2)],
                          [0.123, 2.31, 0.01] )

if __name__ == "__main__":
    unittest.main()
