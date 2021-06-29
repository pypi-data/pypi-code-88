# =============================================================================
# ~/cerebunit/cerebstats/data_conditions/forHTproportions.py
#
# create 18 October 2019 Lungsi
#
# =============================================================================

import numpy as np

class NecessaryForHTProportions(object):
    """
    **Checks for situations (sample size requirements) for which Hypothesis Testing About Proportions is valid, i.e, is t-Test (or standard z-score) valid? and also for Hypothesis Testing About proportions by** :math:`\\chi^2` **-test.**

    **1. For z-test**

    **Situation-1**

    With respect to distributions condition for hypothesis testing about proportions is valid if

    - random sample (from population)
    - data from `binomial experiment <https://en.wikipedia.org/wiki/Binomial_distribution>`_ **with independent trials**.

    Below are some rule-of-thumbs guide to check if an experiment if binomial:

    - it is repeated a fixed number of times

    - trials are independent

    - trial outcomes are either success or failure

    - probability of success is the same for all trials.


    **Situation-2**

    Hypothesis testing about proportions is also valid when **both** the quantities :math:`np` **and** :math:`n(1 - p_0)` are *at least* :math:`5^{\dagger}`. Note that, :math:`n` is the sample size and :math:`p_0` is the null value. Some consider :math:`10^{\ddagger}` (instead of 5) as the lower bound.

    - Ott, R.L. (1998). An Introduction to Statistical Methods and Data Analysis. (p.370) :math:`^{\dagger}`
    - Utts, J.M, Heckard, R.F. (2010). Mind on Statistics. (p.465) :math:`^{\ddagger}`

    **2. For** :math:`\\chi^2` **-test**

    **Situation-1**

    Dito as above.

    **Situation-2**

    The guidelines for *large sample* are

    - expected values in all the cell of the two-way contingency table should be greater than 1
    - number of cells with expected values greater than 5 should be **at least** :math:`80\\%` of the total number of cells

    Note that, :math:`\\chi^2`-test may be performed even if the above large sample guidelines are violated but the results *may not* be valid. :math:`^{\dagger\dagger}`

    - Utts, J.M, Heckard, R.F. (2010). Mind on Statistics. (p.588) :math:`^{\dagger\dagger}`

    **Implementation**

    +-------------------------------------+--------------------------------+
    | Method name                         | Arguments                      |
    +=====================================+================================+
    | :py:meth:`.ask_for_ztest`           | n, p0, lb (optional)           |
    +-------------------------------------+--------------------------------+
    | :py:meth:`.ask_for_chi2test`        | expected valued two-way table  |
    +-------------------------------------+--------------------------------+

    """
    @staticmethod
    def ask_for_ztest(n, p0, lb=5):
        """This function checks if the sample size requirement for running hypothesis testing for proportions using z-test.

        +------------+-------------------------------+
        | Arguments  | Meaning                       |
        +============+===============================+
        | first, n   | sample size                   |
        +------------+-------------------------------+
        | second, p0 | null value                    |
        +------------+-------------------------------+
        | third, lb  | lower bound (5 (default))     |
        +------------+-------------------------------+

        Algorithm that asks if the distribution of an experimental data is normal.

        --------

        |  **Given:** :math:`n, p_0, lb`
        |  **Compute** result1 :math:`\\leftarrow` :math:`np_0`
        |  **Compute** result2 :math:`\\leftarrow` :math:`n(1-p_0)`
        |  **if** result1 :math:`\\cap` result2 :math:`\\geq lb`
        |         "sample size requirement is satisfied"
        |  **else**
        |         "sample size requirement is not satisfied"

        --------

        *Note:*

        * boolean return (`True` or `False`)
        * `True` if sample size requirement is satisfied
        * `False` if sample size requirement is **not** satisfied
        * for two sample tests pass :math:`n_i` and :math:`p_i` in place of :math:`n` and :math:`p_0` respectively for :math:`i^{th}` sample.

        """
        #    raise ValueError("question must be normal? or skew?")
        np0_check = lambda n,p0,lb: True if n*p0 >= lb else False
        n1minusp0_check = lambda n,p0,lb: True if ( n*(1-p0) ) >= lb else False
        if ( np0_check(n, p0, lb) and n1minusp0_check(n, p0, lb) is True ):
            return True
        else:
            return False

    @staticmethod
    def ask_for_chi2test(expected_values):
        """This function checks if the sample size requirement for running hypothesis testing for proportions using :math:`\\chi^2`-test.

        The argument is the expected values table of the 2 x K two-way contingency table.

        +-------------------+------------------------------------------------------+
        | Definition        | Meaning                                              |
        +===================+======================================================+
        | :math:`n`         | total number of cells in a two-way contingency table |
        +-------------------+------------------------------------------------------+
        | :math:`n_1`       | number of expectation values < 1                     |
        +-------------------+------------------------------------------------------+
        | :math:`n_5`       | number of expectation values > 5                     |
        +-------------------+------------------------------------------------------+
        | :math:`lb_{80\\%}` | :math:`80\\%` of the cells                            |
        +-------------------+------------------------------------------------------+

        Algorithm that asks if the distribution of an experimental data is normal.

        --------

        |  **Given:** ex; expected values table
        |  **Get** :math:`n \\leftarrow ex.size`
        |  **Get** :math:`n_1 \\leftarrow ex[ex<1].size`
        |  **Get** :math:`n_5 \\leftarrow ex[ex>1].size`
        |  **Compute** :math:`lb_{80\\%} \\leftarrow ex[ex>1].size`
        |  **Compute** result2 :math:`\\leftarrow` 0.8 \\times n`
        |  **if** :math:`n_1 < 0 \\cap n_5 \\geq lb_{80\\%}`
        |         "sample size requirement is satisfied"
        |  **else**
        |         "sample size requirement is not satisfied"

        --------

        *Note:*

        * boolean return (`True` or `False`)
        * `True` if sample size requirement is satisfied
        * `False` if sample size requirement is **not** satisfied

        """
        #    raise ValueError("question must be normal? or skew?")
        number_of_expected_counts = expected_values.size
        number_of_expected_counts_lessthan1 = \
                    expected_values[ expected_values < 1. ].size
        number_of_expected_counts_largerthan5 = \
                    expected_values[ expected_values > 5. ].size
        lowerbound_80percent = 0.8*number_of_expected_counts
        #
        if ( (number_of_expected_counts_lessthan1 < 1) and
             (number_of_expected_counts_largerthan5 >= lowebound_80percent)
             is True ):
            return True
        else:
            return False
