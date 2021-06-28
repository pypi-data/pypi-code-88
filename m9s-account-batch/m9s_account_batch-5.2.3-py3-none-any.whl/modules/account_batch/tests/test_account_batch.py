# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import doctest
from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite
from trytond.tests.test_tryton import doctest_setup, doctest_teardown, \
    doctest_checker


class AccountBatchTestCase(ModuleTestCase):
    'Test Account Batch module'
    module = 'account_batch'


def suite():
    suite = test_suite()
    suite.addTests(doctest.DocFileSuite(
            'scenario_account_batch.rst',
            setUp=doctest_setup, tearDown=doctest_teardown, encoding='utf-8',
            checker=doctest_checker,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE))
    # Run this test after the scenario, because the scenario needs a fresh
    # database. SQLite doesn't seem to properly rollback the transaction.
    # s. a. https://bugs.tryton.org/issue9133
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            AccountBatchTestCase))
    return suite
