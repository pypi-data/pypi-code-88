# ============================================================================
# ~/cerebunit/cerebstats/hypothesis_testings/aboutproportions.py
#
# This py-file contains custom score functions initiated by
#
# from cerebstats.hypothesisTesting import XYZ
# ============================================================================

import numpy as np
from scipy.stats import norm
from scipy.stats import binom_test
import quantities as pq


class HtestAboutProportions:
    """
    **Hypothesis Testing (significance testing) about proportions.**


    This is a parameteric test that assumes that individuals in the sample are chosen randomly and experiments equivalent to binomial experiments.


    **1. Verify necessary data conditions.**

    The verification is made based on the sample size requirement (the other condition being random sample or binomial experiment with independent trials; this is assumed).


    ====================  ===========================  ============================
      Statistic name        Single sample test           Double sample test        
    ====================  ===========================  ============================
      sample size           :math:`n` (observation)      :math:`n_1` (observation)
                                                         :math:`n_2` (prediction)
      null value            :math:`p_0` (prediction)     :math:`p_0 = 0`
      proportions with                                   :math:`p_1` (observation)
    trait (succeses)                                     :math:`p_2` (prediction)
    ====================  ===========================  ============================
                    

    Such that,

    * :math:`np_0 \\geq lb \\cap n(1-p_0) \\geq lb`
    * :math:`n_1p_1 \\geq lb \\cap n_1(1-p_1) \\geq lb`
    * :math:`n_2p_2 \\geq lb \\cap n_2(1-p_2) \\geq lb`
    * :math:`lb = 5` (default) alternative value is :math:`lb = 10`

    **2. Defining null and alternate hypotheses.**

    **For single sample test**


    .. table:: Title here

    ================================================== =====================================================================
     Statistic                                          Interpretation                      
    ================================================== =====================================================================
     sample statistic, :math:`\\hat{p}`                 proportion of observation with the characteristic trait (successes)
     null value/population parameter, :math:`p_0`       proportion of prediction taken as the specified value
     null hypothesis, :math:`H_0`                       :math:`\\hat{p} = p_0`      
     alternate hypothesis, :math:`H_a`                  :math:`\\hat{p} \\neq or < or > p_0`
    ================================================== =====================================================================


    *For two sample test*


    ================================================== ===========================================================
     Statistic                                           Interpretation                      
    ================================================== ===========================================================
     sample statistic, :math:`\\hat{p}_1-\\hat{p}_2`     difference between the proportions (observation,1, and
                                                         prediction, 2) with the characteristic trait (successes)
     null value/population parameter, :math:`p_0`        0
     null hypothesis, :math:`H_0`                        :math:`\\hat{p}_1-\\hat{p}_2 = 0`      
     alternate hypothesis, :math:`H_a`                   :math:`\\hat{p}_1-\\hat{p}_2 \\neq or < or > 0`
    ================================================== ===========================================================


    **3. Assuming H0 is true, find p-value.**

    *For single sample test*


    .. table:: Title here

    =============================== ====================================================================
     Statistic                       Interpretation                      
    =============================== ====================================================================
     :math:`n`                       number of observations
     :math:`x`                       number of observations with characteristic trait (successes)
     :math:`\\hat{p}`                sample statistic, :math:`\\hat{p} = \\frac{x}{n}`
     :math:`se_{\\hat{p}}`           standard error that :math:`H_0` is true,
                                     :math:`se_{\\hat{p}} = \\frac{ p_0(1-p_0) }{ n }`
     z_statistic, z                  z = :math:`\\frac{ \\hat{p}-p_0 }{ se_{\\hat{p}} }`
    =============================== ====================================================================


    *For two sample test*


    .. table:: Title here

    ====================================  ==================================================================================================================
     Statistic                              Interpretation                      
    ====================================  ==================================================================================================================
     :math:`n_1`                            number of observations
     :math:`n_2`                            number of predictions
     :math:`x_1`                            number of observations with characteristic trait (successes)
     :math:`x_2`                            number of predictions with characteristic trait (successes)
     :math:`\\hat{p}_1`                     proportion of observation with successes,
                                            :math:`\\hat{p}_1 = \\frac{x_1}{n_1}`
     :math:`\\hat{p}_2`                     proportion of predictions with successes,
                                            :math:`\\hat{p}_2 = \\frac{x_2}{n_2}`
     :math:`\\hat{p}`                       combined proportion assuming that :math:`H_0: p_1 = p_2 = p` is true
                                            :math:`\\hat{p} = \\frac{x_1+x_2}{n_1+n_2}`
     :math:`\\hat{p}_1-\\hat{p}_2`          sample statistic,
     :math:`se_{\\hat{p}_1-\\hat{p}_2}`     standard error that :math:`H_0` is true,
                                            :math:`se_{\\hat{p}_1-\\hat{p}_2}=\\sqrt{\\frac{\\hat{p}(1-\\hat{p})}{n_1}+\\frac{\\hat{p}(1-\\hat{p})}{n_2} }`
     z_statistic, z                         z = :math:`\\frac{\\hat{p}_1-\\hat{p}_2 - p_0}{se_{\\hat{p}_1-\\hat{p}_2}}`
    ====================================  ==================================================================================================================


    *Note:*

    - Using z look up table for standard normal curve which will return its corresponding p.
    - The p-value derived from z-statistic is approximate.
    - For single sample test, exact p-value can be calculated from binomial distribution.
    - The notation :math:`\\hat{p}` in single sample test represents sample statistic but not sample statistic for two sample test.

    **4. Report and Answer the question, based on the p-value is the result (true H0) statistically significant?**

    Answer is not provided by the class but it is up to the person viewing the reported result. The reports are obtained calling the attributes ``.statistics`` and ``.description``. This is illustrated below.

    ::

       ht = HtestAboutProportions( observation, prediction, test_result,
                                   side="less_than" )
       score.description = ht.outcome
       score.statistics = ht.statistics

    **Arguments**

    +----------+------------------------+-----------------------------------------------------+
    | Argument | Representation         | Value type                                          |
    +==========+========================+=====================================================+
    | first    | experiment/observation | dictionary that must have keys;                     |
    |          |                        |**"sample_size"**, **"success_numbers"**,            |
    +----------+------------------------+-----------------------------------------------------+
    | second   | model prediction       | float or dictionary; the later for two sample cases |
    |          |                        |with keys: **"sample_size"**, **"success_numbers"**  |
    +----------+------------------------+-----------------------------------------------------+
    | third    | test result            | dictionary with keywords:                           |
    |(keyword) |                        |**"name"**: string, "proportions_z_test_1pop" or     |
    |          |                        |"proportions_z_test_2pop"                            |
    |          |                        |**"sample_statistic"**: float;                       |
    |          |                        |**"z_statistic"**: float;                            |
    |          |                        |**"side"**: string, "not_equal", "less_than" or      |
    |          |                        |"greater_than";                                      |
    |          |                        |and any additional names that is specific to the test|
    +----------+------------------------+-----------------------------------------------------+

    This constructor method generated :py:attr:`.statistics` and :py:attr:`.outcome` (which is then assigned to :py:attr:`.descirption` within the validation test class where this hypothesis test class is implemented).

    """
    def __init__(self, observation, prediction, test={ "name": "proportions_z_test_1pop",
                                                       "sample_statistic": 0.0,
                                                       "z_statistic": 0.0,
                                                       "side": "not_equal" }):
        """This constructor method generated ``.statistics`` and ``.outcome`` (which is then assigned to ``.descirption`` within the validation test class where this hypothesis test class is implemented).
        """
        self.testname = test["name"]
        self.sample_statistic = test["sample_statistic"]
        self.z_statistic = test["z_statistic"]
        self.side = test["side"]
        self.pvalue_from_z = self._compute_pvalue_from_z()
        if test["name"] == "proportions_z_test_1pop":
            self.get_stats_for_onesample( observation )
            self.specified_value = prediction
            self.pvalue_exact = self._compute_pvalue_exact()
        elif test["name"] == "proportions_z_test_2pop":
            self.get_stats_for_twosamples( observation, prediction )
            self.specified_value = 0
        #
        self.outcome = self.test_outcome()
        #
        self.statistics = self._register_statistics()

    @staticmethod
    def null_hypothesis(symbol_null_value, symbol_sample_statistic):
        "Returns the statement for the null hypothesis, H0."
        return "\nH0: "+ symbol_sample_statistic +" = "+ symbol_null_value

    @staticmethod
    def alternate_hypothesis(side, symbol_null_value, symbol_sample_statistic):
        "Returns the statement for the alternate hypothesis, Ha."
        if side is "less_than":
            return "\nHa: "+ symbol_sample_statistic +" < "+ symbol_null_value
        elif side is "greater_than":
            return "\nHa: "+ symbol_sample_statistic +" > "+ symbol_null_value
        else: #side is "not_equal
            return "\nHa: "+ symbol_sample_statistic +" =/= "+ symbol_null_value

    def _compute_pvalue(self):
        "Returns the p-value."
        if self.side is "less_than":
            return norm.cdf(self.test_statistic)
        elif self.side is "greater_than":
            return norm.sf(self.test_statistic)
        else:  # side is "not_equal"
            return 2 * norm.sf(abs(self.test_statistic))

    def test_outcome(self):
        """Puts together the returned values of :py:meth:`.null_hypothesis`, :py:meth:`.alternate_hypothesis`, and :py:meth:`._compute_pvalue`. Then returns the string value for ``.outcome``.
        """
        #
        symbol_null_value = "p0"
        if self.testname == "proportions_z_test_1pop":
            symbol_sample_statistic = "phat"
            pval_expression = "p-value = "+str(self.pvalue_from_z)
        elif self.testname == "proportions_z_test_2pop":
            symbol_sample_statistic = "p1hat_minus_p2hat"
            pval_expression = \
               "p-value = "+str(self.pvalue_from_z)+", exact p-value = "+str(self.pvalue_exact)
        #
        parameters = ( symbol_null_value +" = "+str(self.specified_value)+", "
                + symbol_sample_statistic+" = "+str(self.sample_statistic)+", "
                + "n = "+str(self.sample_size) )
        outcome = ( self.null_hypothesis(symbol_null_value, symbol_sample_statistic)
             + self.alternate_hypothesis(self.side, symbol_null_value, symbol_sample_statistic)
             + "\nTest statistic: z = "+ str(self.z_statistic)
             + "\nAssuming H0 is true, "+ pval_expression  )
        return parameters+outcome

    def get_stats_for_onesample(self, observation):
        self.sample_size = observation["sample_size"]
        self.successes = observation["success_numbers"]

    def get_stats_for_twosamples(self, observation, prediction):
        self.sample1_size = observation["sample_size"]
        self.sample2_size = prediction["sample_size"]
        self.successes1 = observation["success_numbers"]
        self.successes2 = prediction["success_numbers"]

    def _compute_pvalue_from_z(self):
        "Returns the p-value."
        right_side = norm.sf(self.z_statistic)
        if self.side is "less_than":
            return 1-right_side 
        elif self.side is "greater_than":
            return right_side
        else: #side is "not_equal"
            return 2*( norm.sf(abs(self.z_statistic)) )

    def _compute_pvalue_exact(self):
        "Returns the p-value."
        if self.side is "less_than":
            param = "less"
        elif self.side is "greater_than":
            param = "greater"
        else: #side is "not_equal"
            param = "two-sided"
        return binom_test( self.successes, self.sample_size,
                           self.specified_value, param )

    def _register_statistics(self):
        "Returns dictionary value for the ``.statistics``."
        if self.testname=="proportions_z_test_1pop":
            return { "p0": self.specified_value, "phat": self.sample_statistic,
                     "n": self.sample_size, "x": self.successes,
                     "hypotest": "z-Test for HT about proportions for one sample",
                     "z": self.z_statistic, "p": self.pvalue_from_z,
                     "p_exact": self.pvalue_exact, "side": self.side }
        elif self.testname=="proportions_z_test_2pop":
            return { "p0": self.specified_value, "p1hat_minus_p2hat": self.sample_statistic,
                     "n1": self.sample1_size, "n2": self.sample2_size,
                     "x1": self.successes1, "x2": self.successes2,
                     "hypotest": "z-Test for HT about proportions for two samples",
                     "z": self.z_statistic, "p": self.pvalue_from_z, "side": self.side }
