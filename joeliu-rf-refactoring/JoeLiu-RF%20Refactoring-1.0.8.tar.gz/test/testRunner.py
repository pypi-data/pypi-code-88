import unittest
from os import path
import sys
p = path.normpath(path.dirname(path.abspath(__file__))+"/../..")
sys.path.append(p)
from referencesFinderTest import KeywordReferenceFinderTest, VariableReferenceFinderTest
from testDataDependencyBuilderTest import TestDataDependencyBuilderTest
from referencesMethodsTest import ReferencesMethodsTest
from refactoringFacadeTest import RefactoringFacadeTest
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(KeywordReferenceFinderTest)
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(VariableReferenceFinderTest))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestDataDependencyBuilderTest))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ReferencesMethodsTest))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RefactoringFacadeTest))
    unittest.TextTestRunner(verbosity=2).run(suite)