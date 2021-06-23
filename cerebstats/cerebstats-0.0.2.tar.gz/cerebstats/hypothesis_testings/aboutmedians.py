# ============================================================================
# ~/cerebunit/cerebstats/hypothesis_testings/aboutmedians.py
#
# This py-file contains custom score functions initiated by
#
# from cerebstats.hypothesisTesting import XYZ
# ============================================================================

import numpy as np
from scipy.stats import norm
import quantities as pq


class HtestAboutMedians:
    """
    **Hypothesis Testing (significance testing) about medians.**


    This is a nonparameteric test that does not assume specific type of distribution and hence **robust** (valid over broad range of circumstances) and **resistant** (to influence of outliers) test.


    **1. Verify necessary data conditions.**

    +----------------------+---------------------------------------------------+
    | Statistic            | Interpretation                                    |
    +======================+===================================================+
    | data                 | experiment/observed data array :math:`^{\dagger}` |
    +----------------------+---------------------------------------------------+

    - :math:`^{\dagger}`
    * :math:`\\overrightarrow{x} =` experimental data for one sample testing
    * :math:`\\overrightarrow{x} =` (experimental - prediction) data for paired data testing
    * thus :math:`\\eta =` median of :math:`\\overrightarrow{x}`

    **2. Defining null and alternate hypotheses.**

    .. table:: Title here

    ================================================== =================================================
     Statistic                                          Interpretation                      
    ================================================== =================================================
     sample statistic, :math:`\\eta`                    experiment/observed median :math:`^{\dagger}`
     null value/population parameter, :math:`\\eta_0`   prediction (specified value) :math:`^{\dagger}`
     null hypothesis, :math:`H_0`                       :math:`\\eta = \\eta_0`      
     alternate hypothesis, :math:`H_a`                  :math:`\\eta \\neq or < or > \\eta_0`
    ================================================== =================================================

    Depending on whether testing is for a single sample or for paired data :math:`^{\dagger}`,

    .. table:: Title here

    ===============  ============================ ===================================
    Statistic         single sample                paired data
    ===============  ============================ ===================================
    :math:`\\eta`     experiment/observed median   median of (experiment - observed)
    :math:`\\eta_0`   model prediction             0
    ===============  ============================ ===================================

    Two-sided hypothesis (default)
        :math:`H_0`: :math:`\\eta = \\eta_0` and :math:`H_a`: :math:`\\eta \\neq \\eta_0`

    One-side hypothesis (left-sided)
        :math:`H_0`: :math:`\\eta = \\eta_0` and :math:`H_a`: :math:`\\eta < \\eta_0`

    One-side hypothesis (right-sided)
        :math:`H_0`: :math:`\\eta = \\eta_0` and :math:`H_a`: :math:`\\eta > \\eta_0`

    **3. Assuming H0 is true, find p-value.**

    *If the data is skewed, the non-parametric z-score is computed for Sign test.*

    .. table:: Title here

    =============================== ====================================================================
     Statistic                       Interpretation                      
    =============================== ====================================================================
     :math:`s_{+}`                   number of values in sample :math:`> \\eta_0`   
     :math:`s_{-}`                   number of values in sample :math:`< \\eta_0`   
     :math:`n_U = s_{+} + s_{-}`     number of values in sample :math:`\\neq \\eta_0` 
     z_statistic, z                  z = :math:`\\frac{s_{+} - \\frac{n_U}{2}}{\\sqrt{\\frac{n_U}{4}}}`
    =============================== ====================================================================

    *If the data is not skewed, the non-parametric z-score is computed for Signed-rank test (Wilcoxon signed-rank test* **not** *Wilcoxon rank-sum test).*

    .. table:: Title here

    =============================== =======================================================================
     Statistic                       Interpretation                      
    =============================== =======================================================================
     :math:`\\overrightarrow{x}`     data :math:`^{\dagger}`
     :math:`|x_i-\eta_0|`            absolute difference between data values and null value
     :math:`T`                       ranks of the computed difference (excluding difference = 0 )
     :math:`T^+`                     sum of ranks :math:`\eta_0`; Wilcoxon signed-rank statistic
     :math:`n_U`                     number of values in data not equal to :math:`\\eta_0`
    z_statistic, z                  z = :math:`\\frac{T^+ - [n_U(n_U+1)/4]}{\\sqrt{n_U(n_U+1)(2n_U+1)/24}}`
    =============================== =======================================================================

    Using z look up table for standard normal curve which will return its corresponding p.

    **4. Report and Answer the question, based on the p-value is the result (true H0) statistically significant?**

    Answer is not provided by the class but it is up to the person viewing the reported result. The reports are obtained calling the attributes ``.statistics`` and ``.description``. This is illustrated below.

    ::

       ht = HtestAboutMedians( observation, prediction, score,
                               side="less_than" ) # side is optional
       score.description = ht.outcome
       score.statistics = ht.statistics

    **Arguments**

    +----------+------------------------+---------------------------------+
    | Argument | Representation         | Value type                      |
    +==========+========================+=================================+
    | first    | experiment/observation | dictionary that must have keys; |
    |          |                        |"median","sample_size","raw_data"|
    +----------+------------------------+---------------------------------+
    | second   | model prediction       | float or `Quantity array`       |
    +----------+------------------------+---------------------------------+
    | third    | about test             | dictionary with keywords:       |
    |(keyword) |                        | "name": string ("sign_test",    |
    |          |                        |"signed_rank_test");             |
    |          |                        | "z_statistic": float;           |
    |          |                        | "side": string ("not_equal",    |
    |          |                        |"less_than", "greater_than");    |
    |          |                        | and any additional names that is|
    |          |                        | specific to the test            |   
    +----------+------------------------+---------------------------------+

    This constructor method generated :py:attr:`.statistics` and :py:attr:`.outcome` (which is then assigned to :py:attr:`.descirption` within the validation test class where this hypothesis test class is implemented).

    """
    def __init__(self, observation, prediction, test={ "name": "sign_test",
                                                       "z_statistic": 0.0,
                                                       "side": "not_equal" }):
        """This constructor method generated ``.statistics`` and ``.outcome`` (which is then assigned to ``.descirption`` within the validation test class where this hypothesis test class is implemented).
        """
        self.sample_size = observation["sample_size"]
        if np.array( prediction ).shape is (): # single sample
            data = observation["raw_data"]
            self.specified_value = prediction
        else: # paired data => paired difference
            data = observation["raw_data"] - prediction
            self.specified_value = 0 * prediction.units
        #self.sample_statistic = observation["median"] # quantities.Quantity
        #self.specified_value = prediction # quantities.Quantity
        self.sample_statistic = np.median( data )
        self.testname = test["name"]
        self.z_statistic = test["z_statistic"]
        self.side = test["side"]
        #
        self.outcome = self.test_outcome()
        #
        #self.get_below_equal_above(np.array(observation["raw_data"]))
        if self.testname=="sign_test":
            self.get_below_equal_above( data )
        elif self.testname=="signed_rank_test":
            self.get_stats_for_Wilcoxon_signed_rank( test )
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
            return norm.cdf(self.z_statistic)
        elif self.side is "greater_than":
            return norm.sf(self.z_statistic)
        else:  # side is "not_equal"
            return 2 * norm.sf(abs(self.z_statistic))

    def test_outcome(self):
        """Puts together the returned values of :py:meth:`.null_hypothesis`, :py:meth:`.alternate_hypothesis`, and :py:meth:`._compute_pvalue`. Then returns the string value for ``.outcome``.
        """
        self.pvalue = self._compute_pvalue()
        #
        symbol_null_value = "eta0"
        symbol_sample_statistic = "eta"
        parameters = ( symbol_null_value +" = "+str(self.specified_value)+", "
                + symbol_sample_statistic+" = "+str(self.sample_statistic)+", "
                + "n = "+str(self.sample_size) )
        outcome = ( self.null_hypothesis(symbol_null_value, symbol_sample_statistic)
             + self.alternate_hypothesis(self.side, symbol_null_value, symbol_sample_statistic)
             + "\nTest statistic: z = "+ str(self.z_statistic)
             + "\nAssuming H0 is true, p-value = "+ str(self.pvalue) )
        return parameters+outcome

    def get_below_equal_above(self, data):
        "Set values for the attributes ``.below``, ``.equal``, and ``.above`` the null value, :math:`\\eta_0` = ``.specified_value``."
        self.below = (data < self.specified_value).sum()
        self.equal = (data == self.specified_value).sum()
        self.above = (data > self.specified_value).sum()

    def get_stats_for_Wilcoxon_signed_rank(self, test):
        self.Tplus = test["Tplus"]
        self.n_U = test["n_U"]
        self.muTplus = test["muTplus"]
        self.sdTplus = test["sdTplus"]

    def _register_statistics(self):
        "Returns dictionary value for the ``.statistics``."
        if self.testname=="sign_test":
            return { "eta0": self.specified_value, "eta": self.sample_statistic,
                     "n": self.sample_size, "hypotest": "Sign Test for HT about medians",
                     "below": self.below, "equal": self.equal, "above": self.above,
                     "z": self.z_statistic, "p": self.pvalue, "side": self.side }
        elif self.testname=="signed_rank_test":
            return { "eta0": self.specified_value, "eta": self.sample_statistic,
                     "n": self.sample_size, "hypotest": "Signed-Rank Test for HT about medians",
                     "n_U": self.n_U, "T^+": self.Tplus, "muTplus": self.muTplus,
                     "sdTplus": self.sdTplus,
                     "z": self.z_statistic, "p": self.pvalue, "side": self.side }
