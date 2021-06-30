import ast
from robot.api import Token
from robot.parsing.model import Keyword, Statement
from ..builder.testModelBuilder import TestModelBuilder
from ..keywords.keywordMoveHelper import KeywordMoveHelper
from ..common.utility import save_model_and_update_old_models, normalize, get_keywords_for_run_keywords, is_Keyword_tag, is_ForLoop, is_KeywordCall


class KeywordCreator(ast.NodeTransformer):

    def __init__(self, allModels=[]):
        self.allModels = allModels
        self.mover = KeywordMoveHelper(self.allModels)
        self.removedDict = None
        self.replacedDict = None
        self.newNode = None
        self.isRemoveNode = False

    def visit_SuiteSetup(self, node):
        """
            Visit all keyword's call in suite_setup to do somethings.
        """
        if self.isRemoveNode:
            return self.is_node_equal_for_run_keywords(node, self.removedDict)
        if self.replacedDict['node'] == node:
            return self.generic_visit(self.newNode)
        return node

    def visit_SuiteTeardown(self, node):
        """
            Visit all keyword's call in suite_teardown to do somethings.
        """
        if self.isRemoveNode:
            return self.is_node_equal_for_run_keywords(node, self.removedDict)
        if self.replacedDict['node'] == node:
            return self.generic_visit(self.newNode)
        return node

    def visit_TestSetup(self, node):
        """
            Visit all keyword's call in test_setup to do somethings.
        """
        if self.isRemoveNode:
            return self.is_node_equal_for_run_keywords(node, self.removedDict)
        if self.replacedDict['node'] == node:
            return self.generic_visit(self.newNode)
        return node

    def visit_TestTeardown(self, node):
        """
            Visit all keyword's call in test_teardown to do somethings.
        """
        if self.isRemoveNode:
            return self.is_node_equal_for_run_keywords(node, self.removedDict)
        if self.replacedDict['node'] == node:
            return self.generic_visit(self.newNode)
        return node

    def visit_Setup(self, node):
        """
            Visit all keyword's call in setup to do somethings.
        """
        if self.isRemoveNode:
            return self.is_node_equal_for_run_keywords(node, self.removedDict)
        if self.replacedDict['node'] == node:
            return self.generic_visit(self.newNode)
        return node

    def visit_Teardown(self, node):
        """
            Visit all keyword's call in teardown to do somethings.
        """
        if self.isRemoveNode:
            return self.is_node_equal_for_run_keywords(node, self.removedDict)
        if self.replacedDict['node'] == node:
            return self.generic_visit(self.newNode)
        return node

    def visit_TestTemplate(self, node):
        """
            Visit all keyword's call in test_template to do somethings.
        """
        if self.isRemoveNode:
            return self.is_node_equal_for_one_keyword(node, self.removedDict['node'])
        if self.replacedDict['node'] == node:
            return self.generic_visit(self.newNode)
        return node

    def visit_Template(self, node):
        """
            Visit all keyword's call in template to do somethings.
        """
        if self.isRemoveNode:
            return self.is_node_equal_for_one_keyword(node, self.removedDict['node'])
        if self.replacedDict['node'] == node:
            return self.generic_visit(self.newNode)
        return node

    def visit_ForLoop(self, node):
        """
            Visit all keyword's call to do somethings.
        """
        if self.isRemoveNode:
            if self.removedDict['node'] == node:
                for loopBodyMemeber in list(node.body):
                    if loopBodyMemeber == self.removedDict['keyword']:
                        node.body.remove(loopBodyMemeber)
                        if len(node.body) == 0:
                            return None
                        else:
                            return self.generic_visit(node)
            return node
        elif self.isReplaceLastKeyword:
            if self.replacedDict['node'] == node:
                return self.generic_visit(self.newNode)
            return node

    def visit_KeywordCall(self, node):
        """
            Visit all keyword's call to do somethings.
        """
        if self.isRemoveNode:
            return self.is_node_equal_for_one_keyword(node, self.removedDict['node'])
        elif self.isReplaceLastKeyword:
            if self.replacedDict['node'] == node:
                return self.generic_visit(self.newNode)
            return node

    def create_new_keyword_for_file(self, _path, keywordName, keywordBody):

        targetFileModel = TestModelBuilder().build(_path)

        header = Statement.from_tokens([
            Token(Token.NAME, keywordName),
            Token(Token.EOL, '\n')
        ])

        keywordNode = Keyword(header, keywordBody)

        self.mover.insert_new_keyword_defined(targetFileModel, keywordNode)

    def build_tokens_of_new_keyword_arguments(self, args):
        argsTokens = [
            Token(Token.SEPARATOR, '    '),
            Token(Token.ARGUMENTS, '[Arguments]')
        ]
        for arg in args:
            argsTokens.append(Token(Token.SEPARATOR, '    '))
            argsTokens.append(Token(Token.ARGUMENT, arg))
        argsTokens.append(Token(Token.EOL, '\n'))

        return argsTokens

    def is_node_equal_for_one_keyword(self, node, keywordNode):
        if keywordNode == node:
            return None
        return node

    def is_node_equal_for_run_keywords(self, node, removedDict):
        def get_arguments_value_from_arguments_tokens(argsTokens):
            argsValues = []
            for argToken in argsTokens:
                argsValues.append(argToken.value)
            return argsValues

            removedDict['keyword']['arguments']
        
        if node == removedDict['node']:
            if normalize(node.name) == normalize('Run Keywords'):
                runKeywordsArgs = node.get_tokens(Token.ARGUMENT)
                copyRunKeywordsArgs = list(runKeywordsArgs)
                for index, runKeywordsArg in enumerate(copyRunKeywordsArgs):
                    removedArgsValues = get_arguments_value_from_arguments_tokens(removedDict['keyword']['arguments'])
                    if runKeywordsArg.value == removedDict['keyword']['keywordName'].value or runKeywordsArg.value in removedArgsValues:
                        removedIndex = runKeywordsArgs.index(runKeywordsArg)
                        del(runKeywordsArgs[removedIndex])
                        if runKeywordsArg.value in removedArgsValues:
                            removedArgsValues.remove(runKeywordsArg.value)
                        if len(runKeywordsArgs) != removedIndex and runKeywordsArgs[removedIndex].value == 'AND':
                            del(runKeywordsArgs[removedIndex])
                        if len(removedArgsValues) == 0:
                            break
                if len(copyRunKeywordsArgs) != len(runKeywordsArgs):
                    if len(runKeywordsArgs) != 0:
                        runKeywordsDict = get_keywords_for_run_keywords(runKeywordsArgs)
                        runKeywordsNode = self.build_tag_keywords_for_run_keywords(node.__class__.__name__, runKeywordsDict)
                        self.removedDict['node'] = runKeywordsNode
                        return self.generic_visit(runKeywordsNode)
                    else:
                        return None
        return node

    def build_tag_keywords_for_run_keywords(self, tagClass, keywords):
        def build_tokens_of_run_keywords(keywordsTokens, keywords):
            isFirst = True
            if len(keywords) > 1:
                for keyword in keywords:
                    if isFirst:
                        if isinstance(keyword['keywordName'], Token):
                            keywordsTokens.append(Token(Token.ARGUMENT, keyword['keywordName'].value))
                        else:
                            keywordsTokens.append(Token(Token.ARGUMENT, keyword['keywordName']))
                        isFirst = False
                    else:
                        keywordsTokens.append(Token(Token.EOL, '\n'))
                        keywordsTokens.append(Token(Token.SEPARATOR, '    '))
                        keywordsTokens.append(Token(Token.CONTINUATION, '...'))
                        keywordsTokens.append(Token(Token.SEPARATOR, '                    '))
                        keywordsTokens.append(Token(Token.ARGUMENT, 'AND'))
                        keywordsTokens.append(Token(Token.SEPARATOR, '    '))
                        if isinstance(keyword['keywordName'], Token):
                            keywordsTokens.append(Token(Token.ARGUMENT, keyword['keywordName'].value))
                        else:
                            keywordsTokens.append(Token(Token.ARGUMENT, keyword['keywordName']))
                    for arg in keyword['arguments']:
                        keywordsTokens.append(Token(Token.SEPARATOR, '    '))
                        if isinstance(keyword['keywordName'], Token):
                            keywordsTokens.append(Token(Token.ARGUMENT, arg.value))
                        else:
                            keywordsTokens.append(Token(Token.ARGUMENT, arg))
            else:
                if isinstance(keywords[0]['keywordName'], Token):
                    keywordsTokens.append(Token(Token.NAME, keywords[0]['keywordName'].value))
                else:
                    keywordsTokens.append(Token(Token.NAME, keywords[0]['keywordName']))
                for arg in keywords[0]['arguments']:
                    keywordsTokens.append(Token(Token.SEPARATOR, '    '))
                    if isinstance(arg, Token):
                        keywordsTokens.append(Token(Token.ARGUMENT, arg.value))
                    else:
                        keywordsTokens.append(Token(Token.ARGUMENT, arg))
            keywordsTokens.append(Token(Token.EOL, '\n'))

        def get_token_type_from_tag_class(tagClass):
            if tagClass == 'SuiteSetup':
                return [Token(Token.SUITE_SETUP, 'Suite Setup')]
            elif tagClass == 'SuiteTeardown':
                return [Token(Token.SUITE_TEARDOWN, 'Suite Teardown')]
            elif tagClass == 'TestSetup':
                return [Token(Token.TEST_SETUP, 'Test Setup')]
            elif tagClass == 'TestTeardown':
                return [Token(Token.TEST_TEARDOWN, 'Test Teardown')]
            elif tagClass == 'Setup':
                return [Token(Token.SEPARATOR, '    '), Token(Token.SETUP, '[Setup]')]
            elif tagClass == 'Teardown':
                return [Token(Token.SEPARATOR, '    '), Token(Token.TEARDOWN, '[Teardown]')]
            
        keywordsTokens = []
        keywordsTokens = get_token_type_from_tag_class(tagClass)
        keywordsTokens.append(Token(Token.SEPARATOR, '    '))
        if len(keywords) > 1:
            keywordsTokens.append(Token(Token.NAME, 'Run Keywords'))
            keywordsTokens.append(Token(Token.SEPARATOR, '    '))

        build_tokens_of_run_keywords(keywordsTokens, keywords)
        return Statement.from_tokens(keywordsTokens)

    def replace_old_steps_with_keyword_for_same_keywords(self, newKeywordDict, sameKeywords):
        def remove_node_for_same_keywords(sameKeywordDict, allModels):
            self.isRemoveNode = True
            self.removedDict = sameKeywordDict
            self.visit(sameKeywordDict['model'])
            save_model_and_update_old_models(sameKeywordDict['model'], allModels)
            self.isRemoveNode = False

        def build_forLoop(lastSameKeyword, newKeywordName, arguments):
            newKeywordNode = TestModelBuilder().build_keywordCall('        ', newKeywordName, arguments)
            for index, loopBodyMember in enumerate(lastSameKeyword['node'].body):
                if loopBodyMember == lastSameKeyword['keyword']:
                    lastSameKeyword['node'].body[index] = newKeywordNode
                    break
            return lastSameKeyword['node']

        def build_tag_keywords(lastSameKeyword, newKeywordDict):
            if normalize(lastSameKeyword['node'].name) == normalize('Run Keywords'):
                runKeywordsArgs = lastSameKeyword['node'].get_tokens(Token.ARGUMENT)
                runKeywordsDict = get_keywords_for_run_keywords(runKeywordsArgs)
                runKeywordsDict[-1] = newKeywordDict
                return self.build_tag_keywords_for_run_keywords(lastSameKeyword['node'].__class__.__name__, runKeywordsDict)
            else:
                return self.build_tag_keywords_for_run_keywords(lastSameKeyword['node'].__class__.__name__, [newKeywordDict])

        def build_replaced_node(newKeywordDict, sameKeywords):
            if is_KeywordCall(sameKeywords[0]['node']) or (is_ForLoop(sameKeywords[0]['node']) and sameKeywords[0]['containFor']):
                return TestModelBuilder().build_keywordCall('    ', newKeywordDict['keywordName'], newKeywordDict['arguments'])
            elif is_ForLoop(sameKeywords[0]['node']) and not(sameKeywords[0]['containFor']):
                return build_forLoop(sameKeywords[-1], newKeywordDict['keywordName'], newKeywordDict['arguments'])
            elif is_Keyword_tag(sameKeywords[0]['node']):
                return build_tag_keywords(sameKeywords[-1], newKeywordDict)

        def replace_last_keyword_with_new_keyword(newKeywordDict, sameKeywords, allModels):
            self.isReplaceLastKeyword = True
            self.newNode = build_replaced_node(newKeywordDict, sameKeywords)
            self.replacedDict = sameKeywords[-1]
            self.visit(sameKeywords[-1]['model'])
            save_model_and_update_old_models(sameKeywords[-1]['model'], allModels)
            self.isReplaceLastKeyword = False

        tagKeywords = []
        updatedNode = None
        for sameKeyword in sameKeywords:
            if is_Keyword_tag(sameKeyword['node']):
                if not(sameKeyword['node'] in tagKeywords):
                    tagKeywords.append(sameKeyword['node'])
                else:
                    sameKeyword['node'] = updatedNode
            if sameKeyword != sameKeywords[-1]:
                remove_node_for_same_keywords(sameKeyword, self.allModels)
                if is_Keyword_tag(sameKeyword['node']):
                    updatedNode = sameKeyword['node']
            else:
                replace_last_keyword_with_new_keyword(newKeywordDict, sameKeywords, self.allModels)