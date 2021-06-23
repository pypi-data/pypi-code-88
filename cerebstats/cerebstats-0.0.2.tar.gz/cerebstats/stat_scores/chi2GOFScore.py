# ============================================================================
# ~/cerebstats/cerebstats/stat_scores/chi2GOFScore.py
#
# This py-file contains custum score functions initiated by
#
# from cerebstats import scoreScores
# from cerebstats.scoreScores import ABCScore
# ============================================================================

import numpy as np
from scipy.stats import chisquare
import sciunit


# ==============================Chi2GOFScore==================================
class Chi2GOFScore(sciunit.Score):
    """
    Compute chi2-statistic for chi-squared goodness-of-fit Test of proportions.

    One may think of this as a **one-way contingency table.**


    +--------------+-------------------------------------------------------------+
    | sample size  | :math:`k` categories of a categorial variable of interest   |
    +              +--------------+--------------+----------------+--------------+
    | :math:`n`    | :math:`x_1`  | :math:`x_2`  | :math:`\\ldots` | :math:`x_k`  |
    +==============+==============+==============+================+==============+
    | observations | :math:`O_1`  | :math:`O_2`  | :math:`\\ldots` | :math:`O_k`  |
    +--------------+--------------+--------------+----------------+--------------+
    | probabilities| :math:`p_1`  | :math:`p_2`  | :math:`\\ldots` | :math:`p_k`  |
    +--------------+--------------+--------------+----------------+--------------+
    | expected     | :math:`np_1` | :math:`np_2` | :math:`\\ldots` | :math:`np_k` |
    +--------------+--------------+--------------+----------------+--------------+


    Notice that for probabilities of *k* categories :math:`\\sum_{\\forall i} p_i = 1`. The expected counts for each category can be derived from it (or already given) such that :math:`\\sum_{\\forall i} np_i = n`.

    .. table:: Title here

    ==================== ==============================================================================
      Definitions          Interpretation                    
    ==================== ==============================================================================
     :math:`n`             sample size; total number of experiments done
     :math:`k`             number of categorical variables
     :math:`O_i`           observed count (frequency) for :math:`i^{th}` variable
     :math:`p_i`           probability for :math:`i^{th}` category such that
                           :math:`\\sum_{\\forall i} p_i = 1`
     :math:`E_i`           expected count for  :math:`i^{th}` category such that
                           :math:`E_i = n p_i`
     test-statistic        :math:`\\chi^2 = \\sum_{\\forall i} \\frac{(O_i - E_i)^2}{E_i}`
     :math:`df`            degrees of freedom, :math:`df = k-1`
    ==================== ==============================================================================



    *Note* the modification made when compared with a two-way :math:`\\chi^2` test is

    - the calculation of expected counts :math:`E_i = n p_i`
    - the degree of freedom :math:`df = k-1`


    This class uses `scipy.stats.chisquare <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chisquare.html>`_.

    **Use Case:**

    ::

      x = Chi2GOFScoreForProportionChi2GOFTest.compute( observation, prediction )
      score = Chi2GOFScoreForProportionChi2GOFTest(x)

    *Note*: As part of the `SciUnit <http://scidash.github.io/sciunit.html>`_ framework this custom :py:class:`.TScore` should have the following methods,

    * :py:meth:`.compute` (class method)
    * :py:meth:`.sort_key` (property)
    * :py:meth:`.__str__`

    """
    #_allowed_types = (float,)
    _description = ( "ZScoreForSignTest gives the z-statistic applied to medians. "
                   + "The experimental data (observation) is taken as the sample. "
                   + "The sample statistic is 'median' or computed median form 'raw_data'. "
                   + "The null-value is the 'some' specified value whic is taken to be the predicted value generated from running the model. " )

    @classmethod
    def compute(cls, observation, prediction):
        """
        +---------------------+-----------------------------------------------------------------------+
        | Argument            | Value type                                                            |
        +=====================+=======================================================================+
        | first argument      |dictionary; observation/experimental data must have keys "sample_size" |
        |                     |with a number as its value and "observed_freq" whose value is an array |
        +---------------------+-----------------------------------------------------------------------+
        | second argument     |dictionary; model prediction must have either "probabilities" or       |
        |                     |"expected" whose value is an array (same length as "observed_freq")    |
        +---------------------+-----------------------------------------------------------------------+

        *Note:*

        * chi squared tests (for goodness-of-fit or contingency table) by nature are two-sided so there is not option for one-sidedness.

        """
        name = "chi2_goodness_of_fit_test_for_proportions"
        if "probabilities" in prediction:
            probabilities = np.array( prediction["probabilities"] )
            expected_counts = observation["sample_size"] * probabilities
        elif "expected" in prediction:
            expected_counts = np.array( prediction["expected"] )
            probabilities = expected_counts / observation["sample_size"]
        #
        k_categories = expected_counts.size
        score, pvalue = chisquare( observation["observed_freq"], f_exp = expected_counts )
        #return self.score # chi2_statistic
        return {"name": name, "sample_statistic": probabilities, "expected_values": expected_counts,
                "test_statistic": score, "df": k_categories-1, "p_value": pvalue}

    @property
    def sort_key(self):
        return self.score

    def __str__(self):
        return "ChiSqGOFScore is " + str(self.score)
# ============================================================================
