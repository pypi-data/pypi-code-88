# ============================================================================
# ~/cerebstats/cerebstats/stat_scores/fisherExactScore.py
#
# This py-file contains custum score functions initiated by
#
# from cerebstats import scoreScores
# from cerebstats.scoreScores import ABCScore
# ============================================================================

import numpy as np
from scipy.stats import fisher_exact
import sciunit


# ==========================FishExactScore=============================
class FisherExactScore(sciunit.Score):
    """
    Compute fisher-statistic for Fisher Exact Test of proportions for **2 x 2** tables. This test should be called when sample size conditions for z-test (for proportions) and chi2-test (for proportions) are violated.

    Consider a generic 2 x 2 table

    +--------------------------------+---------------------------------------------+
    | Possibilities for categorical  |  Possibilities for categorical variable, B  |
    |                                +----------------------+----------------------+
    |  variable, A                   |         Yes          |          No          |
    +================================+======================+======================+
    |            a1                  |          b1          |          b2          |
    +--------------------------------+----------------------+----------------------+
    |            a2                  |          b3          |          b4          |
    +--------------------------------+----------------------+----------------------+

    Then depending on the question of interest, any one of the values (b1 to b4) in the cells will be its corresponding test statistic (i.e, score). The p-value is computed using the probability distribution, `hypergeometric distribution <https://en.wikipedia.org/wiki/Hypergeometric_distribution>`_.

    This class uses `scipy.stats.fisher_exact <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.fisher_exact.html>`_. The `scipy.stats.fisher_exact` returns two values; a ratio of the odds and the p-value.

    Let us take the example

    +----------------+-----------------------------+
    | Groups         |  people getting cold after  |
    |                +--------------+--------------+
    |                |     Yes      |     No       |
    +================+==============+==============+
    | echinacea herb |      1       |     9        |
    +----------------+--------------+--------------+
    | placebo        |      4       |     6        |
    +----------------+--------------+--------------+

    Then the ratio of the odds is :math:`\\frac{1 \\times 6}{4 \\times 9}`. Also, for this scenario if the concern is whether the use of herb prevented acquiring cold then its test statistic is the number of colds acquired in the echinacea group.

    **Use Case:**

    ::

      x = FishExScoreForFisherExactTest( observation, prediction, "greater_than" )
      score = FishExScoreForFisherExactTest(x)

    **what is the probability (pvalue) that only score value or fewer would be in the model group just by chance?** If our null hypothesis would be that it is not by chance but highly probably then the test is right sided (greater).

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
    def compute(cls, observation, prediction, sidedness):
        """
        +---------------------+--------------------------------------------------+
        | Argument            | Value type                                       |
        +=====================+==================================================+
        | first argument      |dictionary; observation/experimental data must    |
        |                     |must have keys "sample_size" and "success_numbers"|
        +-----------------------+------------------------------------------------+
        | second argument     |dictionary; model prediction must also have keys  |
        |                     |"sample_size" and "success_numbers"               |
        +---------------------+--------------------------------------------------+
        | third argument      |string; "not_equal", "greater_than", "less_than"  |
        +---------------------+--------------------------------------------------+

        *Note:*

        * unlike most scores in CerebUnit this one takes in a third argument for side of hypothesis testing; this is because of `scipy.stats.fisher_exact`.

        """
        name = "fisher_exact_test_2by2"
        table_2way = cls.get_contingency_table_2by2(observation, prediction)
        #
        oddsratio, pvalue = fisher_exact( table_2way, cls.format_sidedness_name(sidedness) )
        score = prediction["success_numbers"]/prediction["sample_size"]
        # observation["success_numbers"] which to pick?
        # what is the probability (pvalue) that only prediction["success_numbers"] or fewer
        # would be in the model group just by chance?
        #return self.score # chi2_statistic
        return {"name": name, "sample_statistic": table_2way,
                "test_statistic": score, "p_value": pvalue}

    @property
    def sort_key(self):
        return self.score

    def __str__(self):
        return "FisherExactScore is " + str(self.score)

    @staticmethod
    def get_contingency_table_2by2(obs, pred):
        a00 = obs["success_numbers"]
        a01 = obs["sample_size"] - obs["success_numbers"]
        a10 = pred["success_numbers"]
        a11 = pred["sample_size"] - pred["success_numbers"]
        return np.array( [ [a00, a01], [a10, a11] ] )

    @staticmethod
    def format_sidedness_name(sidedness):
       # this function is used to maintain consitency with CerebUnit
        if sidedness=="not_equal":
            return "two_sided"
        elif sidedness=="less_than":
            return "less"
        elif sidedness=="greater_than":
            return "greater"
# ============================================================================
