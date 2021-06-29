# ============================================================================
# ~/cerebunit/cerebstats/stat_scores/zSignScore.py
#
# This py-file contains custum score functions initiated by
#
# from cerebstats import scoreScores
# from cerebstats.scoreScores import ABCScore
# ============================================================================

import numpy as np
import sciunit


# ==========================ZScoreForSignTest==================================
class ZScoreForSignTest(sciunit.Score):
    """
    Compute z-statistic for Sign Test.

    .. table:: Title here

    ================= =============================================================================
      Definitions      Interpretation                    
    ================= =============================================================================
     :math:`\eta_0`    some specified value :math:`^{\dagger}`
     :math:`S^{+}`     number of values in sample :math:`> \eta_0`
     :math:`S^{-}`     number of values in sample :math:`< \eta_0`
     :math:`n_u`       number of values in sample :math:`\\neq \eta_0`, i.e., :math:`S^{+} + S^{-}`
     z-statistic, z    z = :math:`\\frac{ S^{+} - \\frac{n_u}{2} }{ \\sqrt{\\frac{n_u}{4}} }`
    ================= =============================================================================

    :math:`^{\dagger} \eta_0`, null value is

    * the model prediction for one sample testing
    * 0 for testing with paired data (observation - prediction)
    
    **Use Case:**

    ::

      x = ZScoreForSignTest.compute( observation, prediction )
      score = ZScoreForSignTest(x)

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
        +----------------------------+------------------------------------------------+
        | second argument            | floating number or array                       |
        +----------------------------+------------------------------------------------+

        *Note:*

        * observation **must** have the key "raw_data" whose value is the list of numbers

        """
        if np.array( prediction ).shape is (): # single sample test
            data = observation["raw_data"]
            eta0 = prediction
        else: # paired difference test
            data = observation["raw_data"] - prediction
            eta0 = 0 #*prediction.units
        splus = ( data > eta0 ).sum()
        n_U = (data != eta0 ).sum()
        score = (splus - (n_U/2)) / np.sqrt(n_U/4)
        #return self.score # z_statistic
        return {"name": "sign_test", "z_statistic": score}

    @property
    def sort_key(self):
        return self.score

    def __str__(self):
        return "ZScore is " + str(self.score)
# ============================================================================
