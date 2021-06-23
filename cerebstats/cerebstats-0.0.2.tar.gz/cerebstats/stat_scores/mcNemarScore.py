# ============================================================================
# ~/cerebstats/cerebstats/stat_scores/mcNemarScore.py
#
# This py-file contains custum score functions initiated by
#
# from cerebstats import scoreScores
# from cerebstats.scoreScores import ABCScore
# ============================================================================

import numpy as np
import sciunit


# ===========================McNemarScore======================================
class McNemarScore(sciunit.Score):
    """
    Compute test-statistic for McNemar's Test of proportions for change/difference in paired data (discordant pairs).

    **Two DEPENDENT samples**, such that they disagree. Hence, there are two types of disagreement; sample-1 agrees but not sample-2 and, sample-2 agrees but not sample-1.

    .. table:: Title here

    ==================== =============================================================================
      Definitions         Interpretation                    
    ==================== =============================================================================
     :math:`b`            proportion of one type of disagreement
     :math:`c`            proportion of other type of disagreement
     :math:`n`            sample size of discordant pairs; :math:`n = b + c`
     :math:`p_0`          some specified value; 0.5 for McNemar testing
     test-statistic       :math:`b` for one disagreement type and, :math:`c` for other disagreement
    ==================== =============================================================================

    *Note:*

    - :py:meth:`.compute` takes two argument
    - it returns proportions (discordant) in the second argument
    - therefore, for the proportion of disagreement of interest pass it as the second argument
    - to compute *p-value* using `scipy.stats.binom_test <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom_test.html>`_ the arguments passed for number of successes is the test-statistic, number of trials is the number of discordant pairs and null value is 0.5

    **Use Case:**

    ::

      x = McNemarScoreForMcNemarTest.compute( observation, prediction )
      score = McNemarScoreForMcNemarTest(x)

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
        | first argument             | dictionary; sample-1 (dependent sample) with   |
        |                            | "discordant_half"                              |
        +----------------------------+------------------------------------------------+
        | second argument            | dictionary; sample-2 (dependent sample) with   |
        |                            | "discordant_half"                              |
        +----------------------------+------------------------------------------------+

        *Note:*

        * observation **must** have the key "raw_data" whose value is the list of numbers

        """
        name = "proportions_discordant_data_test"
        # one possible type of disagreement between observation and prediction
        b = prediction["discordant_half"] # previous success but not failure OR
                                          # prediction satisfies criteria but not observation
        # other possible type of disagreement between observation and prediction
        c = observation["discordant_half"] # previously failed but now successful OR
                                           # observation satisfies criteria but not prediction
        sample_size = b+c # number of discordant pairs
        # for diagreement type: prediction satisfies but not observation
        score = b # proportion of this type of diagreement
        #return self.score # z_statistic
        return {"name": name, "sample_size": sample_size, "test_statistic": score}

    @property
    def sort_key(self):
        return self.score

    def __str__(self):
        return "McNemarScore is " + str(self.score)
# ============================================================================
