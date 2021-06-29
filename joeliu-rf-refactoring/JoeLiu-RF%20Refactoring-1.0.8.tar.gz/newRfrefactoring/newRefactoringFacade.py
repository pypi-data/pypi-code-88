from .builder.testModelBuilder import TestModelBuilder
from .keywords.keywordFinder import KeywordFinder
from .checker.fileChecker import FileChecker
from .helper.lineKeywordsHelper import LineKeywordsHelper
from .keywords.keywordCreator import KeywordCreator
from .common.utility import *


class NewRefactoringFacade:

    def __init__(self):
        self.builder = TestModelBuilder()
        self.finder = KeywordFinder()
        self.checker = FileChecker()
        self.lineKwsHelper = LineKeywordsHelper()
        self.creator = None

    def build_project_models(self, projectPath):
        allModels = self.builder.get_all_models_in_directory(projectPath)
        self.creator = KeywordCreator(allModels)
        return allModels

    def build_file_model(self, filePath):
        return self.builder.build(filePath)

    def get_steps_that_will_be_wraped(self, fromModel, startLine, endLine):
        self.finder.find_keywords_by_lines(fromModel, startLine, endLine)
        return self.finder.get_lines_keywords()

    def get_same_keywords_with_steps(self, allModels, steps):
        self.checker.find_models_with_same_keywords(allModels, steps)
        return self.checker.get_models_with_same_keywords()

    def build_tokens_of_arguments_in_new_keyword(self, newArgs):
        return self.creator.build_tokens_of_new_keyword_arguments(newArgs)

    def get_new_keyword_body_with_steps_and_new_arguments(self, steps, newArgsTokens):
        return self.lineKwsHelper.get_new_keyword_body_from_line_keywords_and_arguments_tokens(steps, newArgsTokens)

    def create_new_keyword_for_file(self, filePath, newKeywordName, newKeywordBody):
        self.creator.create_new_keyword_for_file(filePath, newKeywordName, newKeywordBody)

    def replace_steps_with_keyword_and_get_models_with_replacing(self, keywordName, keywordArgs, steps):
        newKeywordDict = {'keywordName': keywordName, 'arguments': keywordArgs}
        self.creator.replace_old_steps_with_keyword_for_same_keywords(newKeywordDict, steps)
        return steps[0]['model']

    def present_same_steps(self, sameStepsBlock):
        return self.lineKwsHelper.get_same_keywords_block_text(sameStepsBlock)

    def get_models_without_importing_new_resource_from_models_with_replacement(self, newKeywordName, modelsWithReplacement, newKeywordPath):
        return self.creator.mover.get_models_without_import_new_resource_from_models_with_replacement(newKeywordName, modelsWithReplacement, newKeywordPath)

    def import_new_resource_for_model_without_importing(self, model, resourceValue):
        self.creator.mover.import_new_resource_for_model(model, resourceValue)

    def get_moved_keyword_node_from_model(self, model, keywordName, keywordLine):
        return self.creator.mover.find_moved_keyword_node(model, keywordName, keywordLine)

    def remove_defined_keyword(self, model, keywordNode):
        self.creator.mover.remove_old_keyword_defined(model, keywordNode)

    def insert_defined_keyword(self, model, keywordNode):
        self.creator.mover.insert_new_keyword_defined(model, keywordNode)

    def get_models_using_keyword(self, pathOfKeywordDefined, keywordName):
        return self.creator.mover.get_models_using_keyword(pathOfKeywordDefined, keywordName)

    def get_models_without_import_target_resource(self, movedKeywordName, fromFilePath, targetFilePath):
        return self.creator.mover.get_models_without_import_new_resource(movedKeywordName, fromFilePath, targetFilePath)

    def save_models(self, models):
        recovery_models(models)

    def get_variables_not_defined_in_steps(self, steps):
        localVariables = self.lineKwsHelper.get_local_variables_in_line_keywords(steps)
        return self.lineKwsHelper.get_variables_not_defined_in_lineKeywords(steps, localVariables)