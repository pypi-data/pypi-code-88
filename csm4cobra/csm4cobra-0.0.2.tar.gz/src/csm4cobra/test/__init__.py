import unittest as _unittest


available_tests = ['test_umfinder']

def create_test_suite():
    """create a unittest.TestSuite with available tests"""
    loader = _unittest.TestLoader()
    suite = _unittest.TestSuite()
    for test_name in available_tests:
        exec("from . import " + test_name)
        suite.addTests(loader.loadTestsFromModule(eval(test_name)))
    return suite

suite = create_test_suite()


def test_all():
    """###running unit tests on cobra py###"""
    status = not _unittest.TextTestRunner(verbosity=2).run(
        create_test_suite()
    ).wasSuccessful()
    return status
