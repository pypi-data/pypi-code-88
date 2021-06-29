# =============================================================================
# ~/cerebunit/cerebstats/data_conditions/forHTmeans.py
#
# create 3 July 2019 Lungsi
#
# =============================================================================

from scipy.stats import normaltest, skew

class NecessaryForHTMeans(object):
    """
    **Checks for situations for which Hypothesis Testing About Means is valid, i.e, is t-Test (or standard z-score) valid?**


    **Situation-1**

    For large sample sizes and randomly collected individuals one may assume that the population of the measurements (of interest) is normal. Thus condition for hypothesis testing about means is valid.

    **Situation-2**

    Hypothesis testing about means is also valid when there is not evidence of extreme outliers or skewed population shape. This is usually the case for population of the measurements that are approximately normal.

    **Implementation**

    +-------------------------------------+--------------------------------+
    | Method name                         | Arguments                      |
    +=====================================+================================+
    | :py:meth:`.ask`                     | experimental_data              |
    +-------------------------------------+--------------------------------+
    | :py:meth:`.check_normal_population` | experimental_data              |
    +-------------------------------------+--------------------------------+
    | :py:meth:`.check_skew_population`   | experimental_data              |
    +-------------------------------------+--------------------------------+

    """
    @staticmethod
    def check_normal_population(data):
        """Tests if sample is from a normal distribution.

        Algorithm to check if population is normal

        --------

        | **Given:** data                                     
        | **Parameter:** :math:`\\alpha = 0.001`              
        | **Compute:** p :math:`\\leftarrow` normaltest(data) 
        | **if** p < :math:`\\alpha`                          
        |        "data is normal"                             
        | **else**                                            
        |        "data is not normal"                         

        --------

        *Note:*

        * :math:`\\alpha` is an arbitrarily small value, here taken as equal to 0.001
        * `scipy.stats.normaltest <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.normaltest.html>`_ is based on `D'Agostino <https://doi.org/10.1093/biomet/58.2.341>`_ & `Pearson's <https://doi.org/10.1093/biomet/60.3.613>`_ omnibus test of normality.
        * "data is normal" => `True` and "data is not normal" => `False`

        """
        alpha = 0.001 # an arbitrarily small alpha value
        k2, p = normaltest(data)
        if p < alpha: # null hypothesis: sample comes from normal distribution
            return True
        else:
            return False

    @staticmethod
    def check_skew_population(data):
        """Tests if the data is symmetric (not skewed).

        Algorithm to check if population is not skewed

        --------

        | **Given:** data                                     
        | **Parameter:** :math:`\\beta = 0.001`              
        | **Compute:** s :math:`\\leftarrow` skew(data) 
        | **if** s > :math:`\\beta`                          
        |        "data is skewed"                             
        | **else**                                            
        |        "data is not skewed"                         

        --------

        *Note:*

        * :math:`\\beta` is an arbitrarily small value, here taken as equal to 0.001
        * `scipy.stats.skew <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.skew.html>`_ is based on *Zwillinger, D. and Kokoska, S. (2000). CRC Standard Probability and Statistics Tables and Formulae. Chapman & Hall: New York. 2000. Section 2.2.24.1.* `ISBN: ISBN 9780849300264 <https://www.crcpress.com/CRC-Standard-Probability-and-Statistics-Tables-and-Formulae-Student-Edition/Kokoska-Zwillinger/p/book/9780849300264>`_ that uses `Fisher-Pearson coefficient of skewness <https://en.wikipedia.org/wiki/Skewness>`_.
        * by default `scipy.stats.skew` is computed for `bias = True`. Fisher-Pearson standardized moment coefficient is the computed value for the corrected bias, i.e, `bias = False`.
        * "data is skewed" => `True` and "data is not skewed" => `False`

        """
        beta = 0.001 # an arbitrarily small beta value
        if skew(data) < beta:
            return True
        else:
            return False

    @classmethod
    def ask(cls, question, experimental_data):
        """Depending on the question asked (`normal?` or `skew?`) this function checks if the distribution of the raw data is normal or skewed.

        Algorithm that asks if the distribution of an experimental data is normal.

       `question = normal?`

        --------

        |  **Given:** experimental_data
        |  **get** sample_size :math:`\\leftarrow` number of experimental data elements
        |  *invoke* :py:meth:`.check_normal_population`

        --------

       Algorithm that asks if the distribution is skewed (a data may not be bell-shaped but symmetric).

       `question = skew?`

        --------

        |  **Given:** experimental_data
        |  *invoke* :py:meth:`.check_skew_population`

        --------

        *Note:*

        * boolean return (`True` or `False`)
        * `True` if it is normal
        * `True` if it is skewed

        """
        if question=="normal?":
            try:
                return cls.check_normal_population( experimental_data )
            except:
                return False
        elif question=="skew?":
            try:
                return cls.check_skew_population( experimental_data )
            except:
                return False
        else:
            raise ValueError("question must be normal? or skew?")
