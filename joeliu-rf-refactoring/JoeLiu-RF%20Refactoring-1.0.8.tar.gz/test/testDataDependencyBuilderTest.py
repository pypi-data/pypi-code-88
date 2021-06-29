import unittest
from os import path
from robot304.parsing.model import ResourceFile, TestData
from python_package.rfrefactoring.testDataDependencyBuilder import TestDataDependencyBuilder
from python_package.rfrefactoring.testDataVisitor import TestDataVisitor, FindVisitor
from init import test_data, ezScrum_test_data
class TestDataDependencyBuilderTest(unittest.TestCase):
    def setUp(self):
        self.suite = TestData(source=test_data)
        self.resource = ResourceFile(source=test_data+'/ezScrum.txt').populate()

    def test_builder(self):
        source = path.normpath(test_data+'/testResource.txt')
        builder = TestDataDependencyBuilder() 
        result = builder.build(self.suite)
        self.assertIsNotNone(FindVisitor(result, source).get_result()[0])
        self.assertEqual(3,len(result.childs))
        ez_scrum_dependency = FindVisitor(result, self.resource.source).get_result()[0]
        self.assertEqual(4,len(ez_scrum_dependency.childs))
        test_resource_dependency = FindVisitor(result, source).get_result()[0]
        self.assertIsNotNone(FindVisitor(ez_scrum_dependency, source).get_result()[0])
        self.assertIsNotNone(FindVisitor(result, source).get_result()[0])
        self.assertEquals(1, len(test_resource_dependency.childs))