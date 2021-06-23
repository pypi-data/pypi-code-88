# ============================================================================
# ~/cerebstats/cerebstats/stat_scores/zPropScore.py
#
# This py-file contains custum score functions initiated by
#
# from cerebstats import scoreScores
# from cerebstats.scoreScores import ABCScore
# ============================================================================

import numpy as np
import sciunit


# ==========================ZScoreForProportionZTest==================================
class ZScoreForProportionZTest(sciunit.Score):
    """
    Compute z-statistic for z-Test of proportions.

    **For single population.**

    .. table:: Title here

    ==================== =============================================================================
      Definitions         Interpretation                    
    ==================== =============================================================================
     :math:`n`            sample size
     :math:`p_0`          some specified value
     :math:`\\hat{p}`     sample proportion (with characteristic of interest), i.e, sample statistic
     :math:`se_{H_0}`     standard error of :math:`\\hat{p}` if :math:`p_0` is the true value of p
                          :math:`se_{H_0} = \\sqrt{\\frac{p_0(1-p_0)}{n}}`
     z-statistic, z       z = :math:`\\frac{ \\hat{p} - p_0 }{ \\sqrt{\\frac{p_0(1-p_0)}{n}} }`
    ==================== =============================================================================


    **For two populations.**


    .. table:: Title here

    ===============================  ========================================================================================================
      Definitions                     Interpretation
    ===============================  ========================================================================================================
     :math:`n_1`                      sample size for first population (experimental data)
     :math:`n_2`                      sample size for second population (prediction data)
     :math:`x_1`                      numbers in first population's sample having the trait in question
     :math:`x_2`                      numbers in second population's sample having the trait in question
     :math:`p_0`                      0
     :math:`\\hat{p_1}`               sample 1 proportion:math:`\\hat{p_1} = \\frac{x_1}{n}`
     :math:`\\hat{p_2}`               sample 2 proportion:math:`\\hat{p_2} = \\frac{x_2}{n}`
     :math:`\\hat{p_1}-\\hat{p_2}`     sample statistic (with characterisic of interest)
     :math:`\\hat{p}`                 estimate of common population proportion; if :math:`H_0` is true
                                      :math:`p_1 = p_2 = p` and estimate :math:`\\hat{p}` is
                                      :math:`\\hat{p} = \\frac{n_1\\hat{p_1} + n_2\\hat{p_2}}{n_1 + n_2}`
                                      :math:`\\hat{p} = \\frac{x_1 + x_2}{n_1 + n_2}`
     :math:`se_{H_0}`                 standard error of :math:`\\hat{p_1}-\\hat{p_2}` if :math:`H_0` is true
                                      :math:`se_{H_0} = \\sqrt{\\frac{\\hat{p}(1-\\hat{p})}{n_1} + \\frac{\\hat{p}(1-\\hat{p})}{n_2}}`
     z-statistic, z                   z = :math:`\\frac{ \\hat{p_1} - \\hat{p_2} - p_0 }{ se_{H_0} }`
    ===============================  ========================================================================================================


    **Use Case:**

    ::

      x = ZScoreForProportionZTest.compute( observation, prediction )
      score = ZScoreForProportionZTest(x)

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
        +----------------------------+------------------------------------------------+
        | Argument                   | Value type                                     |
        +============================+================================================+
        | first argument             | dictionary; observation/experimental data      |
        |                            | must have keys "sample_size" and "phat"        |
        +----------------------------+------------------------------------------------+
        | second argument            | floating number or array                       |
        +----------------------------+------------------------------------------------+

        *Note:*

        * observation **must** have the key "raw_data" whose value is the list of numbers

        """
        try: # two sample test
            name = "proportions_z_test_2pop"
            n1 = observation["sample_size"]
            n2 = prediction["sample_size"]
            x1 = observation["success_numbers"]
            x2 = prediction["success_numbers"]
            p0 = 0 #*prediction.units
            p1hat = x1/n1
            p2hat = x2/n2
            sample_statistic = p1hat - p2hat
            phat = (x1+x2)/(n1+n2) # combined proportion NOT sample statisic
            se_H0 = np.sqrt( phat*(1-phat)*( (1/n1) + (1/n2) ) )
        except: # single sample test
            name = "proportions_z_test_1pop"
            n = observation["sample_size"]
            x = observation["success_numbers"]
            p0 = prediction
            sample_statistic = x/n # phat
            se_H0 = np.sqrt( (p0*(1-p0))/ n )
        #
        score = (sample_statistic - p0) / se_H0
        #return self.score # z_statistic
        return {"name": name, "sample_statistic": sample_statistic, "z_statistic": score}

    @property
    def sort_key(self):
        return self.score

    def __str__(self):
        return "ZScore is " + str(self.score)
# ============================================================================
