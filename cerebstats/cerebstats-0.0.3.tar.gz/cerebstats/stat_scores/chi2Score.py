# ============================================================================
# ~/cerebstats/cerebstats/stat_scores/chi2Score.py
#
# This py-file contains custum score functions initiated by
#
# from cerebstats import scoreScores
# from cerebstats.scoreScores import ABCScore
# ============================================================================

import numpy as np
from scipy.stats import chi2_contingency as chi2test
import sciunit


# ==================================Chi2Score==================================
class Chi2Score(sciunit.Score):
    """
    Compute chi2-statistic for chi squared Test of proportions.

    **For any two-way contingency tables.**

    +--------------------------------+---------------------------------------------+
    | Possibilities for categorical  |  Possibilities for categorical variable, B  |
    |                                +----------------------+----------------------+
    |  variable, A                   |         Yes          |          No          |
    +================================+======================+======================+
    |            a1                  |    :math:`O_{00}`    |    :math:`O_{01}`    |
    +--------------------------------+----------------------+----------------------+
    |            a2                  |    :math:`O_{10}`    |    :math:`O_{11}`    |
    +--------------------------------+----------------------+----------------------+


    .. table:: Title here

    ==================== ==============================================================================
      Definitions          Interpretation                    
    ==================== ==============================================================================
     :math:`r`             number of row variables
     :math:`c`             number of column variables
     :math:`O_{ij}`        observed count for a cell in :math:`i^{th}` row, :math:`j^{th}` column
     :math:`R_{i}`         total observations in :math:`i^{th}` row,
                           :math:`\\sum_{\\forall j \\in c} O_{ij}`
     :math:`C_{j}`         total observations in :math:`j^{th}` column,
                           :math:`\\sum_{\\forall i \\in r} O_{ij}`
     :math:`n`             total count for entire table :math:`\\sum_{\\forall i \\in r} R_i` or
                           :math:`\\sum_{\\forall j \\in c} C_j`
     :math:`E_{ij}`        expected count for a cell in :math:`i^{th}` row, :math:`j^{th}` column
                           :math:`E_{ij} = \\frac{R_i C_j}{n}`
     test-statistic        :math:`\\chi^2 = \\sum_{\\forall i,j} \\frac{(O_{ij}-E_{ij})^2}{E_{ij}}`
     :math:`df`            degrees of freedom, :math:`df = (r-1)(c-1)`
    ==================== ==============================================================================



    **Special note**. For the case of 2 x 2 table like below


    +--------------------------------+---------------------------------------------+--------------+
    | Possibilities for categorical  |  Possibilities for categorical variable, B  |    Total     |
    |                                +----------------------+----------------------+              |
    |  variable, A                   |       column-1       |       column-2       |              |
    +================================+======================+======================+==============|
    |           row-1                |          A           |          B           | R\ :sub:`1`\ |
    +--------------------------------+----------------------+----------------------+--------------+
    |           row-2                |          C           |          D           | R\ :sub:`2`\ |
    +--------------------------------+----------------------+----------------------+--------------+
    |           Total                |     C\ :sub:`1`\     |     C\ :sub:`2`\     |      N       |
    +--------------------------------+----------------------+----------------------+--------------+


    Notice that for 2 x 2, :math:`df = 1` and its test statictic can calculated with the shortcut formula

    :math:`\\chi^2 = \\frac{ N(AD-BC)^2 }{ R_1 R_2 C_1 C_2 }`


    This class uses `scipy.stats.chi2_contingency <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html>`_. `chi2_contingency` is a special case of `chisquare` as demonstrated below

    ::

      obs = np.array([ [129, 49], [150, 29], [137, 39] ])
      chi2, p, df, expected = scipy.stats.chi2_contingency( obs )
      chi2_, p_ = scipy.stats.chisquare( obs.ravel(), f_exp=expected.ravel(), ddof=obs.size-1-df )
      chi2 == chi2_ == 6.69
      True
      p == p2 == 0.03
      True


    **Use Case:**

    ::

      x = Chi2ScoreForProportionChi2Test.compute( observation, prediction )
      score = Chi2ScoreForProportionChi2Test(x)

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
        +---------------------+--------------------------------------------------+
        | Argument            | Value type                                       |
        +=====================+==================================================+
        | first argument      |dictionary; observation/experimental data must    |
        |                     |must have keys "sample_size" and "success_numbers"|
        +-----------------------+------------------------------------------------+
        | second argument     |dictionary; model prediction must also have keys  |
        |                     |"sample_size" and "success_numbers"               |
        +---------------------+--------------------------------------------------+

        *Note:*

        * for a 2 x 2 table, the value for the key `"success_numbers` is a number for both observation and prediction
        * for a 2 x k table, the values for the keys `"success_numbers"` (both observation and prediction) is either a list or an array.
        * chi squared tests by nature are two-sided so there is not option for one-sidedness.

        """
        if ( isinstance( observation["success_numbers"], list ) or       # and dit for
             isinstance( observation["success_numbers"], np.ndarray ) ): # predictions
            name = cls.get_testname_for_2byK( observation )
            table_2way = np.array( [ observation["success_numbers"],
                                     prediction["success_numbers"] ] )
        else: # its a scalar and hence a 2 x 2 contingency table
            name = "proportions_chi2_test_2by2"
            table_2way = cls.get_contingency_table_2by2(observation, prediction)
        #
        score, pvalue, df, table_expected = chi2test( table_2way )
        #return self.score # chi2_statistic
        return {"name": name, "sample_statistic": table_2way, "expected_values": table_expected,
                "test_statistic": score, "df": df, "p_value": pvalue}

    @property
    def sort_key(self):
        return self.score

    def __str__(self):
        return "ChiSqScore is " + str(self.score)

    @staticmethod
    def get_contingency_table_2by2(obs, pred):
        a00 = obs["success_numbers"]
        a01 = obs["sample_size"] - obs["success_numbers"]
        a10 = pred["success_numbers"]
        a11 = pred["sample_size"] - pred["success_numbers"]
        return np.array( [ [a00, a01], [a10, a11] ] )

    @staticmethod
    def get_testname_for_2byK(obs): # interchangeable with predictions
        try: # if "success_numbers" value is a list
            x = len(obs["success_numbers"])
        except: # if "success_numbers" value is a np.ndarray
            x = obs["success_numbers"].size
        return "proportions_chi2_test_2by"+str(x)
# ============================================================================
