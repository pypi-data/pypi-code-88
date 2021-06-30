import ast
from robot.parsing.model import Statement
from robot.api import Token
from ..common.utility import normalize, get_file_name_from_path, save_model_and_update_old_models
from ..checker.fileChecker import FileChecker
from ..keywords.keywordFinder import KeywordFinder


class KeywordMoveHelper(ast.NodeTransformer):

    def __init__(self, modelsInDir=[]):
        self.finder = KeywordFinder()
        self.checker = FileChecker()
        self.modelsInDir = modelsInDir
        self.movedKeywordNode = None
        self.importedResource = None
        self.removeOldKeywordDefined = False
        self.insertKeywordDefined = False
        self.importResource = False

    def visit_SettingSection(self, node):
        if(self.importResource):
            newResource = Statement.from_tokens([
                Token(Token.RESOURCE, 'Resource'),
                Token(Token.SEPARATOR, '    '),
                Token(Token.NAME, self.importedResource),
                Token(Token.EOL, '\n')
            ])
            node.body.insert(0, newResource)
        return self.generic_visit(node)

    def visit_KeywordSection(self, node):
        """
            Visit all keyword's define to do something.
        """
        if(self.insertKeywordDefined):
            if node.body[-1].body[-1].__class__.__name__ != 'EmptyLine':
                empty_line = Statement.from_tokens([Token(Token.EOL, '\n'), Token(Token.EOL, '\n')])
                node.body[-1].body.append(empty_line)
            node.body.append(self.movedKeywordNode)
            return self.generic_visit(node)
        elif(self.removeOldKeywordDefined):
            for index, keyword in  enumerate(node.body):
                if(keyword == self.movedKeywordNode):
                    del(node.body[index])
                    return node
        return node

    def find_moved_keyword_node(self, fromFileModel, movedKeywordName, keywordLine):
        self.finder.visit_model_for_finding_keyword(fromFileModel, movedKeywordName)
        definedKeywords = self.finder.get_keyword_defs()
        if(len(definedKeywords) != 0):
            for keyword in definedKeywords:
                if keyword['keywordNode'].lineno == keywordLine:
                    return keyword['keywordNode']
        return None

    def remove_old_keyword_defined(self, model, removedKeywordNode=None):
        if(removedKeywordNode):
            self.movedKeywordNode = removedKeywordNode
        self.removeOldKeywordDefined = True
        self.visit(model)
        save_model_and_update_old_models(model, self.modelsInDir)
        self.removeOldKeywordDefined = False

    def insert_new_keyword_defined(self, model, insertedKeywordNode=None):
        if(insertedKeywordNode):
            self.movedKeywordNode = insertedKeywordNode
        self.insertKeywordDefined = True
        self.visit(model)
        save_model_and_update_old_models(model, self.modelsInDir)
        self.insertKeywordDefined = False

    def split_models_without_import(self, allModels, modelsWithImport):
            for model in modelsWithImport:
                if(model in allModels):
                    allModels.remove(model)
            return allModels

    def get_models_using_keyword(self, pathOfKeywordDefined, keywordName):
        fileNameKeywordDefined = get_file_name_from_path(pathOfKeywordDefined)
        self.checker.visit_models_to_check_keyword_and_resource(self.modelsInDir, keywordName, fileNameKeywordDefined)
        modelsUsingKeyword = self.checker.get_models_with_resource_and_keyword()
        self.checker.clear_models_with_resource_and_keyword()
        return modelsUsingKeyword


    def get_models_without_import_new_resource(self, movedKeywordName, oldImportedResourcePath, newImportedResourcePath):
        modelsUsingKeyword = self.get_models_using_keyword(oldImportedResourcePath, movedKeywordName)

        newImportedResourceName = get_file_name_from_path(newImportedResourcePath)
        self.checker.visit_models_to_check_keyword_and_resource(modelsUsingKeyword, movedKeywordName, newImportedResourceName)
        modelsWithImportNewResource = self.checker.get_models_with_resource_and_keyword()
        self.checker.clear_models_with_resource_and_keyword()

        return self.split_models_without_import(modelsUsingKeyword, modelsWithImportNewResource)

    def get_models_without_import_new_resource_from_models_with_replacement(self, newKeywordName, modelsWithReplacement, newImportedResourcePath):
        newImportedResourceName = get_file_name_from_path(newImportedResourcePath)
        self.checker.visit_models_to_check_keyword_and_resource(modelsWithReplacement, newKeywordName, newImportedResourceName)
        modelsWithImportNewResource = self.checker.get_models_with_resource_and_keyword()
        self.checker.clear_models_with_resource_and_keyword()

        return self.split_models_without_import(modelsWithReplacement, modelsWithImportNewResource)

    def import_new_resource_for_model(self, modelWithoutImport, importedResourceValue):
        self.importedResource = importedResourceValue
        self.importResource = True
        self.visit(modelWithoutImport)
        save_model_and_update_old_models(modelWithoutImport, self.modelsInDir)
        self.importResource = False
    
    def get_models_after_moving(self):
        return self.modelsInDir
    
    def move_keyword_defined_to_file(self, movedKeywordName, fromFileModel, targetFileModel, keywordLine, newImportedResource=None):

        self.movedKeywordNode = self.find_moved_keyword_node(fromFileModel, movedKeywordName, keywordLine)
        self.remove_old_keyword_defined(fromFileModel)
        self.insert_new_keyword_defined(targetFileModel)
        if(newImportedResource):
            self.importedResource = newImportedResource
            modelsWithoutImport = self.get_models_without_import_new_resource(movedKeywordName, fromFileModel.source, targetFileModel.source)
            for model in modelsWithoutImport:
                self.import_new_resource_for_model(model, newImportedResource)