from os import path
from robot304.parsing.model import ForLoop
from robot304.parsing.settings import Setting
import re
from .reference import Reference
from .referencesMethods import *

"""
This func is used to check whether a keyword is used in an attribute.
attribute: The decomposition value of step,setting,forloop object.
keyword: name of a keyword.
return: whether a keyword is used in an given attribute.
"""
def is_keyword_use_in_attribute(keyword, attribute):
    return any([is_keyword_use_in_attribute(keyword, step) for step in attribute]) if isinstance(attribute, ForLoop) else any([is_keyword_match(keyword,attr) for attr in attribute.as_list()])

class KeywordReferenceFinder:
    """
    This func is used to create reference object.
    parsedObject: an object which has keyword reference.It could be step,setting,forloop.
    return: a reference object.
    """
    def create_reference(self, parsedObject):
        return Reference(parsedObject, get_present_method(parsedObject), get_replace_method(parsedObject, 'keyword'))
    """
    This func is used to find keyword references from a keyword.
    targetKeyword: name of the keyword to be found.
    sourceKeyword: the keyword to be searched.
    return: a list which contain reference object.
    """
    def find_references_from_keyword(self, targetKeyword, sourceKeyword):
        source = [step for step in sourceKeyword.steps+[sourceKeyword.teardown]]
        return [self.create_reference(step) for step in source if is_keyword_use_in_attribute(targetKeyword, step)]
    """
    This func is used to find keyword references from a testcase.
    targetKeyword: name of the keyword to be found.
    testcase: the testcase to be searched.
    return: a list which contain reference object.
    """
    def find_references_from_testcase(self, targetKeyword, testcase):
        source = [step for step in testcase.steps+[testcase.template, testcase.setup, testcase.teardown]]
        return [self.create_reference(setting) for setting in source if is_keyword_use_in_attribute(targetKeyword, setting)]
    """
    This func is used to find keyword references from setting table.
    targetKeyword: name of the keyword to be found.
    setting: the setting table to be searched.
    return: a list which contain reference object.
    """
    def find_references_from_settings(self, targetKeyword, setting):
        return [self.create_reference(setting) for setting in [setting.suite_setup, setting.suite_teardown,setting.test_setup, setting.test_teardown] if is_keyword_use_in_attribute(targetKeyword, setting)]
    """
    This func is used to find keyword references from a testDataFile.
    targetKeyword: name of the keyword to be found.
    testDataFile: the testDataFile to be searched.which can be ResourceFile or TestCaseFile.
    return: a dict which contain all reference objects and testdata object.
    """
    def find_references_from_testdataFile(self, targetKeyword, testDataFile):
        references = []
        for kw in testDataFile.keyword_table:
            references.extend(self.find_references_from_keyword(targetKeyword,kw))
        for test in testDataFile.testcase_table:
            references.extend(self.find_references_from_testcase(targetKeyword, test))
        references.extend(self.find_references_from_settings(targetKeyword, testDataFile.setting_table))
        return {'testdata':testDataFile,'references':references}

class VariableReferenceFinder:
    """
    This func is used to check whether a string match a given variable.
    variableName: name of a variable which contain symbol of variable.Like ${test}.
    string: a string you want to check.
    return: whether the string match. 
    """
    def is_variable_match(self, variableName, string):
        return len(get_variable_match_result(variableName, string))>0
    """
    This func is used to check whether a variable been assigned in a step.
    EX: The `${test}` variable is assigned in step `${test} =    Set Variable    test123`.
    variable: name of the variable.
    step: the step to be checked.
    return: whether a variable is assign in a step.
    """
    def is_var_assign_in_step(self, variable, step):
        if isinstance(step, ForLoop):
            return any([self.is_var_assign_in_step(variable, loop_step) for loop_step in step]) or any([self.is_variable_match(variable, var) for var in step.vars])
        else:
            for assign_variable in step.assign:
                if self.is_variable_match(variable, assign_variable):
                    return True
            return False
    """
    This func is used to check whether a variable is used in an attribute.
    attribute: The decomposition value of step,setting,forloop object.
    variable: name of a variable.
    return: whether a variable is used in an given attribute.
    """
    def is_var_use_in_attribute(self, variable, attribute):
        if isinstance(attribute, ForLoop):
            return any([self.is_var_use_in_attribute(variable, data) for data in attribute]) or any([self.is_variable_match(variable, data) for data in attribute.items])
        return any([self.is_variable_match(variable, data) for data in attribute.as_list()])
    """
    This func is used to check whether a variable is define in an argument object.
    variable: name of a variable.
    argument: the argument object.
    return: whether the given variable is define in argument. 
    """
    def is_var_def_in_argument(self, variable, argument):
        def is_arg_match(variable, data):
            arg = data.split("=")
            #The argument does not have default value.
            if len(arg) == 1:
                return self.is_variable_match(variable, data)
            #The argument has default value.
            else:
                return len(arg)>1 and self.is_variable_match(variable, arg[0])
        return any([is_arg_match(variable, data) for data in argument.as_list()])
        
    def get_references_from_attribute(self, attribute):
        return Reference(attribute, get_present_method(attribute) ,get_replace_method(attribute, 'variable'))

    def find_global_variable_references_from_testcase_obj(self, variable, testcase):
        testcase_contents = [content for content in testcase]
        # This is used to find the step which assign the variable.
        variable_assign_step = next((step for step in testcase.steps if self.is_var_assign_in_step(variable, step)),None)
        # Calculate the search range.
        # Search before the step which assign the variable. 
        source = [testcase_contents[index] for index in range(testcase_contents.index(variable_assign_step))] if variable_assign_step else testcase_contents
        return [self.get_references_from_attribute(content) for content in source if self.is_var_use_in_attribute(variable, content)]

    def find_global_variable_references_from_keyword(self, variable, keyword):
        return [] if self.is_var_def_in_argument(variable, keyword.args) else self.find_global_variable_references_from_testcase_obj(variable, keyword)

    def find_global_variable_references_from_setting(self, variable, settingTable):
        return [self.get_references_from_attribute(setting) for setting in settingTable if self.is_var_use_in_attribute(variable, setting)]

    def find_global_variable_references_from_testdata_file(self, variable, testData):
        def is_variable_def_in_testData(variable, testData):
            return any(self.is_variable_match(variable, var.name) for var in testData.variable_table)
        source = variable.parent.parent.source
        # This is used to distinguish the variable which has same name but define in different source. 
        if path.normpath(source) != path.normpath(testData.source) and is_variable_def_in_testData(variable.name, testData):
            return {'testdata':testData, 'references':[]}
        references = []
        references.extend(self.find_global_variable_references_from_setting(variable.name, testData.setting_table))
        for keyword in testData.keyword_table:
            references.extend(self.find_global_variable_references_from_keyword(variable.name, keyword))
        for testcase in testData.testcase_table:
            references.extend(self.find_global_variable_references_from_testcase_obj(variable.name, testcase))
        return {'testdata':testData, 'references':references}
    
    def find_local_variable_references_from_test_case_obj(self, variable, testcase):
        return [self.get_references_from_attribute(content) for content in [testcase.doc, testcase.tags, testcase.timeout] + testcase.steps + [testcase.teardown, testcase.return_] if self.is_var_use_in_attribute(variable, content)]