# ~/cerebstats/cerebstats/stat_scores/chi2Score_test_with_datasets.py
import unittest
import quantities as pq
import numpy as np

from chi2Score import Chi2Score

from pdb import set_trace as breakpoint

class Chi2ScoreTest(unittest.TestCase):

    def setUp(self):
        # for 2 x 2 case
        self.gender_drunk_driving_male_group = {
            # Oklahoma road survey to estimate proportion of male and female drunk
            # drivers unders 20yrs old.
            "sample_size": 481, # total male drivers < 20yrs
            "success_numbers": 77} # male drives drank w/in past 2hrs
        self.gender_drunk_driving_female_group = {
            # Oklahoma road survey to estimate proportion of male and female drunk
            # drivers unders 20yrs old.
            "sample_size": 138, # total fmale drivers < 20yrs
            "success_numbers": 16} # female drives drank w/in past 2hrs
        #
        self.tension_headaches_18to29_group = {
            # In the previous year what was the relationship of women's age and
            # episodic tension-type headache
            "sample_size": 1600, # total number of women in this age group
            "success_numbers": 653} # number with tension headaches
        self.tension_headaches_30to39_group = {
            # In the previous year what was the relationship of women's age and
            # episodic tension-type headache
            "sample_size": 2122, # total number of women in this age group
            "success_numbers": 995} # number with tension headaches
        #
        # for 2 x K case
        #
        self.easiest_friendships_gendertype_female_group = {
            # does gender type influence making friends?
            "sample_size": 137, # number of females who responded
            "success_numbers": [58, 16, 63]} # number for [opposite, same, no-difference]
        self.easiest_friendships_gendertype_male_group = {
            # does gender type influence making friends?
            "sample_size": 68, # number of males who responded
            "success_numbers": [15, 13, 40]} # number of [opposite, same, no-difference]
        #
        # For cases like
        # Group (3)        No infection   Yes infection
        # Original question: does taking xylitol sweetener prevent ear infection?
        # Since in cerebunit the score classes accept only experimental observation and
        # model prediction, one may consider the No column as a group, say, observation
        # the the Yes column as the prediction group
        # Modified question: are ear infections prevented with xylitol sweetener?
        self.ear_infection_xylitol_infect_group = {
            # reversing letter orders "S" and "Q", tendency to pick first choice?
            "sample_size": 117, # number of people with ear infection
            "success_numbers": [49, 29, 39]} # infection for placebo, xyl-gum, xyl-lozenge
        self.ear_infection_xylitol_healthy_group = {
            # do fewer than 20% experience medication side effects
            "sample_size": 416, # number of people without ear infection
            "success_numbers": [129, 150, 137]} # healthy for placebo, xyl-gum, xyl-lozenge
        #
        # For two 2 x 2 tables with different sample sizes
        # Is there a relationship between genders in the car (not just driving) and
        # car accident?
        self.car_accident_gendertype_smallsample_female_group = {
            "sample_size": 34, # number of females
            "success_numbers": 18} # number of females experienced car accident
        self.car_accident_gendertype_smallsample_male_group = {
            "sample_size": 23, # number of males
            "success_numbers": 16} # number of males experienced car accident
        self.car_accident_gendertype_largesample_female_group = {
            "sample_size": 136, # number of females
            "success_numbers": 72} # number of females experienced car accident
        self.car_accident_gendertype_largesample_male_group = {
            "sample_size": 92, # number of males
            "success_numbers": 64} # number of males experienced car accident

    #@unittest.skip("reason for skipping")
    def test_1_gender_drunk_driving_2by2(self):
        # Oklahoma road survey to estimate proportion of male and female drunk
        # drivers unders 20yrs old.
        # p1: proportions of male drunk drivers
        # p2: proportions of female drunk drivers
        # H0: p1 = p2 and Ha: p1, p2 are not all the same (i.e, has relationship)
        x = Chi2Score.compute( self.gender_drunk_driving_male_group,
                               self.gender_drunk_driving_female_group )
        # scipy.stat.chi2_contingency does not return values equal to the those
        # using the shortcut formula
        self.assertEqual(
             [np.floor(round(x["test_statistic"], 2)), np.floor(x["p_value"])],
             [np.floor(1.637), np.floor(0.201)] )

    #@unittest.skip("reason for skipping")
    def test_2_tension_headaches_and_age_2by2(self):
        # In the previous year what was the relationship of women's age and
        # episodic tension-type headache
        # p1: proportions of 18-29 women with headaches
        # p2: proportions of 30-39 women with headaches
        # H0: p1 = p2 and Ha: p1 != p2 (i.e, has relationship)
        x = Chi2Score.compute( self.tension_headaches_18to29_group,
                               self.tension_headaches_30to39_group )
        # scipy.stat.chi2_contingency does not return values equal to the those
        # using the shortcut formula
        self.assertEqual( [round(x["test_statistic"], 0), round(x["p_value"], 3)],
                          [np.floor(13.66), 0.000] )

    #@unittest.skip("reason for skipping")
    def test_3_easiest_friendships_gendertype_2by3(self):
        # does gender type influence making friends?
        # p1: proportions of female with no gender difference with friendship
        # p2: proportions of male with no gender difference with friendship
        # H0: p1 = p2 and Ha: p1 != p2 (i.e, related to sex)
        x = Chi2Score.compute( self.easiest_friendships_gendertype_female_group,
                               self.easiest_friendships_gendertype_male_group )
        p_interval = x["p_value"] < 0.25 and x["p_value"] > 0.01
        self.assertEqual( [round(x["test_statistic"], 3), x["df"], p_interval],
                          [8.515, 2, True] )

    #@unittest.skip("reason for skipping")
    def test_4_ear_infection_xylitol_2by3(self):
        # Modified question: are ear infections prevented with xylitol sweetener?
        # p1: proportions of infections taking placebo gum
        # p2: proportions of infections taking xylitol gum
        # H0: p1 = p2 and Ha: p1 != p2 (related)
        x = Chi2Score.compute( self.ear_infection_xylitol_infect_group,
                               self.ear_infection_xylitol_healthy_group )
        #print(x)
        p_interval = x["p_value"] < 0.05 and x["p_value"] > 0.025
        self.assertEqual( [round(x["test_statistic"], 2), x["df"], p_interval],
                          [6.69, 2, True] )
        # Notice that for (3 x 2 version, no compatible with cerebunit)
        # Original question: does taking xylitol sweetener prevent ear infection?
        # p1: proportions of placebo gum intake getting ear infection
        # p2: proportions of xylitol gum intake getting ear infection
        # p3: proportions of xylitol lozenge intake getting ear infection
        # H0: p1 = p2 = p3 and Ha: p1, p1, p3 are not the same
        # Therefore, although for this particular question the three proportions in
        # the hypothesis testing is more descriptive the test statistic and its
        # p-value remain the same.

    #@unittest.skip("reason for skipping")
    def test_5_car_accident_gendertype_female_group_2by2(self):
        x1 = Chi2Score.compute(
                self.car_accident_gendertype_smallsample_female_group,
                self.car_accident_gendertype_smallsample_male_group )
        x2 = Chi2Score.compute(
                self.car_accident_gendertype_largesample_female_group,
                self.car_accident_gendertype_largesample_male_group )
        #print(x1)
        #print(x2)
        a = x1["p_value"] != x2["p_value"]
        self.assertEqual( a, True )
        # Lesson: statistical significance of a fixed difference is
        # affected by the sample size.

if __name__ == "__main__":
    unittest.main()
