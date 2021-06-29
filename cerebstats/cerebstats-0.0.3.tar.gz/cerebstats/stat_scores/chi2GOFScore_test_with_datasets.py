# ~/cerebstats/cerebstats/stat_scores/chi2_gof_Score_test_with_datasets.py
import unittest
import quantities as pq
import numpy as np

from chi2GOFScore import Chi2GOFScore as Chi2Score

from pdb import set_trace as breakpoint

class Chi2GOFScoreTest(unittest.TestCase):

    def setUp(self):
        # for 2 x 2 case
        self.penn_three_digit_lottery_experiment_for1stdigit = {
            # Are the probabilities for selecting one of each digit the same as
            # those given by pediction?
            "sample_size": 500, # 500 lottery days
            "observed_freq": [47,50,55,46,53,39,55,55,44,56]} # its sum = sample size
        self.penn_three_digit_lottery_prediction_for1stdigit_type1 = {
            # Are the probabilities for selecting one of each digit the same as
            # those given by prediction?
            # probability of selecting one for each of the 10 possible digits
            "expected": [50,50,50,50,50,50,50,50,50,50]} # list length = observed_freq
        self.penn_three_digit_lottery_prediction_for1stdigit_type2 = {
            # Are the probabilities for selecting one of each digit the same as
            # those given by prediction?
            # probability of selecting one for each of the 10 possible digits
            "probabilities": [.1,.1,.1,.1,.1,.1,.1,.1,.1,.1]} # length = observed_freq
        self.mNm_colors_experiment = {
            "sample_size": 6918, # number of milk chocolate M&Ms
            # brown, red, yellow, blue, orange, green
            "observed_freq": [1911, 1072, 1308, 804, 821, 1002]}
        self.mNm_colors_prediction = {
            "probabilities": [.3, .2, .2, .1, .1, .1]}

    #@unittest.skip("reason for skipping")
    def test_1_penn_three_digit_lottery_type1(self):
        # for k categories of a categorical variable its probabilities are
        # p_1 to p_k
        # H0: p1, p2, ..., pk are the correct probabilities
        # Ha: not all specified probabilities are correct
        x = Chi2Score.compute(
               self.penn_three_digit_lottery_experiment_for1stdigit,
               self.penn_three_digit_lottery_prediction_for1stdigit_type1 )
        #
        self.assertEqual(
             [round(x["test_statistic"], 2), round(x["p_value"],3), x["df"]],
             [6.04, 0.736, 9] )

    #@unittest.skip("reason for skipping")
    def test_2_penn_three_digit_lottery_type2(self):
        # for k categories of a categorical variable its probabilities are
        # p_1 to p_k
        # H0: p1, p2, ..., pk are the correct probabilities
        # Ha: not all specified probabilities are correct
        x = Chi2Score.compute(
               self.penn_three_digit_lottery_experiment_for1stdigit,
               self.penn_three_digit_lottery_prediction_for1stdigit_type2 )
        #
        self.assertEqual(
             [round(x["test_statistic"], 2), round(x["p_value"],3), x["df"]],
             [6.04, 0.736, 9] )

    #@unittest.skip("reason for skipping")
    def test_3_mNm_colors(self):
        # for k categories of a categorical variable its probabilities are
        # p_1 to p_k
        # H0: p1, p2, ..., pk are the correct probabilities
        # Ha: not all specified probabilities are correct
        x = Chi2Score.compute( self.mNm_colors_experiment,
                               self.mNm_colors_prediction )
        #
        self.assertEqual(
             [round(x["test_statistic"], 2), round(x["p_value"],5), x["df"]],
             [268.75, 0, 5] )

if __name__ == "__main__":
    unittest.main()
