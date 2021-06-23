# ============================================================================
# ~/cerebunit/cerebstats/hypothesis_testings/tTest.py
#
# This py-file contains custom score functions initiated by
#
# from cerebstats.hypothesisTesting import XYZ
# ============================================================================

from scipy.stats import norm
from scipy.stats import t as student_t
import quantities as pq


class HtestAboutMeans:
    """
    **Hypothesis Testing (significance testing) about means.**


    **1. Verify necessary data conditions.**

    +-------------------------------------+-------------------------------------+
    | Statistic                           | Interpretation                      |
    +=====================================+=====================================+
    | sample size, n                      | experiment/observed n               |
    +-------------------------------------+-------------------------------------+
    | optionally: raw data                | experiment/observed data array      |
    +-------------------------------------+-------------------------------------+

    Is :math:`n \\geq 30`?

    If not, check if data is from normal distribution.

    If both returns NO, you can't perform hypothesis testing about means.
    Instead use sign test.

    If either of the above two question returns YES continue below.

    **2. Defining null and alternate hypotheses.**

    .. table:: Title here

    ================================================ =====================================
      Statistic                                       Interpretation                      
    ================================================ =====================================
     sample statistic, :math:`\\mu`                   experiment/observed mean         
     null value/population parameter, :math:`\\mu_0`  model prediction                  
     null hypothesis, :math:`H_0`                     :math:`\\mu = \\mu_0`             
     alternate hypothesis, :math:`H_a`                :math:`\\mu \\neq or < or > \\mu_0`
    ================================================ =====================================

    Two-sided hypothesis (default)
        :math:`H_0`: :math:`\\mu = \\mu_0` and :math:`H_a`: :math:`\\mu \\neq \\mu_0`

    One-side hypothesis (left-sided)
        :math:`H_0`: :math:`\\mu = \\mu_0` and :math:`H_a`: :math:`\\mu < \\mu_0`

    One-side hypothesis (right-sided)
        :math:`H_0`: :math:`\\mu = \\mu_0` and :math:`H_a`: :math:`\\mu > \\mu_0`

    **3. Assuming H0 is true, find p-value.**

    .. table:: Title here

    ====================================== ========================================================
      Statistic                             Interpretation                      
    ====================================== ========================================================
      sample size, n                        experiment/observed n               
      standard error, SE                    experiment/observed SE = :math:`\\frac{SD}{\\sqrt{n}}`
      or                                    or                                  
      standard deviation, SD                experiment/observed SD              
      t-statistic, t                        test score, :math:`t = \\frac{\\mu - \\mu_0}{SE}`
      degree of freedom, df                 :math:`df = n - 1`
      z-statistic, z (standard)             test score, :math:`z = \\frac{\\mu - \\mu_0}{SD}`
    ====================================== ========================================================

    Using t and df look up table for t-distrubution which will return its corresponding p. If the denominator is ``SD`` then value of z is seen in a normal distribution to return its corresponding p.

    **4. Report and Answer the question, based on the p-value is the result (true H0) statistically significant?**

    Answer is not provided by the class but its is up to the person viewing the reported result. The results are obtained calling the attributed ``.statistics`` and ``.description``. This is illustrated below.

    ::

       ht = HtestAboutMeans( observation, prediction, score,
                             side="less_than" ) # side is optional
       score.description = ht.outcome
       score.statistics = ht.statistics

    **Arguments**

    +----------+-----------------------------+---------------------------------+
    | Argument | Representation              | Value type                      |
    +==========+=============================+=================================+
    | first    | experiment/observation      | dictionary that must have keys; |
    |          |                             | "mean" and "sample_size"        |
    +----------+-----------------------------+---------------------------------+
    | second   | model prediction            | float                           |
    +----------+-----------------------------+---------------------------------+
    | third    | test score/z or t-statistic | dictionary with key; "z" or "t" |
    +----------+-----------------------------+---------------------------------+
    | fourth   | sidedness of test           | string; "not_equal" (default)   |
    |          |                             | or "less_than", "greater_than"  |
    +----------+-----------------------------+---------------------------------+

    The constructor method generates :py:attr:`.statistics` and  :py:attr:`.outcome` (which is then assigned to :py:attr:`.description` within the validation test class where this hypothesis test class is implemented).

    """
    def __init__(self, observation, prediction, test_statistic, side="not_equal"):
        """This constructor method generates ``.statistics`` and ``.outcome`` (which is then assigned to ``.description`` within the validation test class where this hypothesis test class is implemented).
        """
        self.sample_statistic = observation["mean"] # quantities.Quantity
        self.sample_size = observation["sample_size"]
        self.popul_parameter = prediction # quantities.Quantity
        self.test_statistic = list( test_statistic.values() )[0]
        self.test_statistic_name = list( test_statistic.keys() )[0]
        if "t" in test_statistic:
            self.deg_of_freedom = self.sample_size - 1
            self.standard_error = observation["standard_error"]
        elif "z" in test_statistic:
            self.standard_deviation = observation["SD"]
        self.side = side
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
        if self.test_statistic_name == "t":
            if self.side is "less_than":
                return student_t.cdf(self.test_statistic, self.deg_of_freedom)
            elif self.side is "greater_than":
                return student_t.sf(self.test_statistic, self.deg_of_freedom)
            else: #side is "not_equal"
                return 2 * student_t.sf(abs(self.test_statistic), self.deg_of_freedom)
        elif self.test_statistic_name == "z":
            if self.side is "less_than":
                return norm.cdf(self.test_statistic)
            elif self.side is "greater_than":
                return norm.sf(self.test_statistic)
            else: #side is "not_equal"
                return 2 * norm.sf(abs(self.test_statistic))

    def test_outcome(self):
        """Puts together the returned values of :py:meth:`.null_hypothesis`, :py:meth:`.alternate_hypothesis`, and :py:meth:`._compute_pvalue`. Then returns the string value for ``.outcome``.
        """
        self.pvalue = self._compute_pvalue()
        #symbol_null_value = unichr(0x3bc).encode('utf-8') + "0" # mu_0; chr for Python3
        #symbol_sample_statistic = unichr(0x3bc).encode('utf-8') # mu
        symbol_null_value = "u0"
        symbol_sample_statistic = "u"
        parameters = ( symbol_null_value +" = "+str(self.popul_parameter)+", "
                + symbol_sample_statistic+" = "+str(self.sample_statistic)+", "
                + "n = "+str(self.sample_size) )
        string_for_test_statistic = self.test_statistic_name +" = "+ str(self.test_statistic)
        outcome = ( self.null_hypothesis(symbol_null_value, symbol_sample_statistic)
             + self.alternate_hypothesis(self.side, symbol_null_value, symbol_sample_statistic)
             + "\nTest statistic: "+ string_for_test_statistic
             + "\nAssuming H0 is true, p-value = "+ str(self.pvalue) )
        return parameters+outcome

    def _register_statistics(self):
        "Returns dictionary value for the ``.statistics``."
        x = { "u0": self.popul_parameter, "u": self.sample_statistic,
              "hypotest": self.test_statistic_name+"-Test for HT about means",
              "n": self.sample_size,
              self.test_statistic_name: self.test_statistic }
        if self.test_statistic_name=="t":
            x.update( {"se": self.standard_error,
                       "df": self.deg_of_freedom} )
        elif self.test_statistic_name=="z":
            x.update( {"sd": self.standard_deviation} )
        return x
