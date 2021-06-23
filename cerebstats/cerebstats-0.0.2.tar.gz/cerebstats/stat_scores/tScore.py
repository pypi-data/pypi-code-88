# ============================================================================
# ~/cerebstats/cerebstats/stat_scores/tScore.py
#
# This py-file contains custom score functions initiated by
#
# from cerebstats import scoreScores
# from cerebstats.scoreScores import ABCScore
# ============================================================================

import sciunit


# ==========================TScore=======================================
class TScore(sciunit.Score):
    """
    Compute t-statistic as the standardized statistic as

    .. table:: Title here

    ================================== ===========================================
      Definitions                       Interpretation                            
    ================================== ===========================================
      sample_mean, :math:`\\bar{x}`     observation["mean"]                       
      null_value, :math:`\\mu_0`        model prediction                          
      standard_error, se                observation["standard_error"]             
      t-statistic, t                    t = :math:`\\frac{\\bar{x} - \\mu_0}{se}` 
    ================================== ===========================================

    Note: se = :math:`\\frac{s}{\\sqrt{n}}`, where n is the sample size and s is the standard deviation.
    
    **Use Case**

    ::

      x = TScore.compute( observation, prediction )
      score = TScore(x)

    *Note*: As part of the `SciUnit <http://scidash.github.io/sciunit.html>`_ framework this custom :py:class:`.TScore` should have the following methods,

    * :py:meth:`.compute` (class method)
    * :py:meth:`.sort_key` (property)
    * :py:meth:`.__str__`

    """
    #_allowed_types = (float,)
    _description = ( "TScore gives the student-t as the standardized statistic applied to means. "
                   + "The experimental data (observation) is taken as the sample. "
                   + "The sample statisic is 'mean' and s.e is the 'standard_error' of this sample. "
                   + "The population parameter or null-value is the the predicted value generated from running the model. " )

    @classmethod
    def compute(self, observation, prediction):
        """
        *Note:*

        * observation (sample) is in dictionary form with keys mean and
        * standard_error whose value has magnitude and python quantity
        * the populations parameter is the predicted value

        """
        self.score = ((observation["mean"] - prediction)/observation["standard_error"])
        return self.score # t_statistic

    @property
    def sort_key(self):
        return self.score

    def __str__(self):
        return "TScore is " + str(self.score)
# ============================================================================
