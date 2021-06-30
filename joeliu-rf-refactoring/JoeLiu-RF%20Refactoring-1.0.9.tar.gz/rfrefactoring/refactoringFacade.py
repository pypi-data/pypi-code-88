import sys
from os import path
from robot304.api import TestData
from robot304.parsing.model import Step
from .testDataDependencyBuilder import TestDataDependencyBuilder
from .testDataVisitor import TestDataVisitor, FindVisitor
from .referencesFinder import KeywordReferenceFinder, VariableReferenceFinder
from .refactorHelper import KeywordRefactorHelper, VariableRefactorHelper
from robot304.parsing.model import ResourceFile
from .referencesMethods import get_keyword_object_replace_method, get_variable_object_replace_method, get_present_method
"""
    This class is for plugin usage.
"""
class RefactoringFacade:
    """
    This func is used for get the keyword,variable,setting object.
    instanceName is the name of keyword,variable,setting.
    table is the table object in test suite or resourcefile.
    """
    def get_instance_from_testData(self, instanceName, table):
        return next((instance for instance in table if instance.name.upper() == instanceName.upper()),None)
    """
    This func is used for parsing and classify all testdatas under given path.
    path: path which contain testdatas
    return: the root of tree.
    """
    def build(self, path):
        suite = TestData(source=path)
        builder = TestDataDependencyBuilder()
        root = builder.build(suite)
        return root
    """
    This func is used to find a testdata node from the given tree.
    root: the root of tree.
    source: the path of an testdata.
    return: a node which contain the testdata.
    """
    def get_testData_node(self, root, source):
        find_visitor = FindVisitor(root, source)
        return find_visitor.get_result()[0] if find_visitor.has_result() else None
    """
    This func is used to find keyword from a testdata file in tree.
    root: the root of tree.
    kwName: the name of keyword.
    source: the path of testdata.
    return: a keyword object 
    """
    def get_keyword_obj_from_file(self, root, kwName, source):
        testData = self.get_testData_node(root, source).get_data()
        return self.get_instance_from_testData(kwName, testData.keyword_table)
    """
    This func is used to find variable from a testdata file in tree.
    root: the root of tree.
    varName: the name of variable.
    source: the path of testdata.
    return: a variable object 
    """
    def get_variable_obj_from_file(self, root, varName, source):
        testData = self.get_testData_node(root, source).get_data()
        return self.get_instance_from_testData(varName, testData.variable_table)
    """
    This func is used to find all references of a given keyword.
    root: the root of tree.
    keyword: the keyword object.
    return: all references separate by testdata.
    """
    def get_keyword_references(self, root, keyword):
        source = keyword.source
        finder = KeywordReferenceFinder()
        node = self.get_testData_node(root, source)
        references = {}
        def visit(node):
            node_source = node.get_data().source
            #filter the duplicated testdata.
            if node_source not in references.keys():
                references[node_source] = finder.find_references_from_testdataFile(keyword.name, node.get_data())
            return True
        node.accept(TestDataVisitor(visit))
        return [reference for reference in references.values() if len(reference['references']) > 0 ]
    """
    This func is used to find all references of a given golbal variable.
    root: the root of tree.
    variable: the variable object.
    return: all references separate by testdata.
    """
    def get_variable_references(self, root, variable):
        source = variable.parent.parent.source
        finder = VariableReferenceFinder()
        node = self.get_testData_node(root, source)
        references = {}
        def visit(node):
            node_source = node.get_data().source
            if node_source not in references.keys():
                references[node_source] = finder.find_global_variable_references_from_testdata_file(variable, node.get_data())
            return True
        node.accept(TestDataVisitor(visit))
        return [reference for reference in references.values() if len(reference['references']) > 0 ]
    """
    This func is used to find all references of a given local variable.
    testcaseObj: the testcase or resourcefile object.
    variable: the variable object.
    return: all references.
    """
    def get_local_variable_references(self,testCaseObj, variable):
        finder = VariableReferenceFinder()
        return finder.find_local_variable_references_from_test_case_obj(variable, testCaseObj)
    """
    This func is used to rename variable from the given references.
    references: the variable references.
    oldVariableName: the origin variable name.
    newVariableName: the new variable name.
    """
    def rename_variable_references(self, references, oldVariableName, newVariableName):
        VariableRefactorHelper().rename_variable(references, oldVariableName, newVariableName)
    """
    This func is used to rename keyword from the given references.
    references: the variable references.
    oldKeywordName: the origin keyword name.
    newKeywordName: the new keyword name.
    """
    def rename_keyword_references(self, references, oldKeywordName, newKeywordName):
        KeywordRefactorHelper().rename_keyword(references, oldKeywordName, newKeywordName)
    """
    This func is used to rename the given keyword object.
    keyword: the keyword object.
    newName: the new keyword name.
    """
    def rename_keyword_def(self, keyword, newName):
        replace_method = get_keyword_object_replace_method()
        replace_method(keyword, keyword.name, newName)
    """
    This func is used to rename the given variable object.
    variable: the variable object.
    newName: the new variable name.
    """
    def rename_variable_def(self, variable, newName):
        replace_method = get_variable_object_replace_method()
        replace_method(variable, variable.name, newName)
    """
    This func is used to modify a given reference to a new value.
    reference: a reference object.
    referenceValue: string value of a reference.
    Note: it can not support for the ForLoop object yet.
    """
    def modify_reference(self, reference, referenceValue):
        replace_value = referenceValue.split("    ")
        reference_obj = reference.reference
        if isinstance(reference_obj, Step):
            reference_obj.__init__(replace_value)
        else:
            reference_obj._set_initial_value()
            reference_obj._populate(replace_value[1:])
    """
    This func is used for save multiple testdata.
    testDataFiles: the given testData objects.
    """
    def save_test_data_files(self, testDataFiles):
        for testData in testDataFiles:
            self.save(testData)

    def save(self, testData):
        testData.save()
    """
    This func is used for present keyword.
    keyword: the keyword object.
    return: the string use to present the keyword.
    """
    def present_keyword(self, keyword):
        present_result = keyword.name+"\n"
        for attr in keyword:
            present_method = get_present_method(attr)
            present_result += "    "+present_method(attr)+"\n"
        return present_result