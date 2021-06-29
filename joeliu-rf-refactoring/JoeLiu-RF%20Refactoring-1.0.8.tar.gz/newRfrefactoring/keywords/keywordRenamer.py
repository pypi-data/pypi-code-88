import ast
from robot.api import get_model, Token
from ..common.utility import normalize, is_KeywordCall


class KeywordRenamer(ast.NodeVisitor):

    def __init__(self):
        self.new_name = None
        self.keywordNode = None
        self.keywordToken = None

    def visit_SuiteSetup(self, node):
        """
            Visit all keyword's call in suite_setup to rename keywordCalled.
        """
        self.rename_keyword_from_multiple_keywords(node)

    def visit_SuiteTeardown(self, node):
        """
            Visit all keyword's call in suite_teardown to rename keywordCalled.
        """
        self.rename_keyword_from_multiple_keywords(node)

    def visit_TestSetup(self, node):
        """
            Visit all keyword's call in test_setup to rename keywordCalled.
        """
        self.rename_keyword_from_multiple_keywords(node)

    def visit_TestTeardown(self, node):
        """
            Visit all keyword's call in test_teardown to rename keywordCalled.
        """
        self.rename_keyword_from_multiple_keywords(node)

    def visit_Setup(self, node):
        """
            Visit keyword calls in test cases to rename keywordCalled.
        """
        self.rename_keyword_from_multiple_keywords(node)

    def visit_Teardown(self, node):
        """
            Visit keyword calls in test cases to rename keywordCalled.
        """
        self.rename_keyword_from_multiple_keywords(node)

    def visit_TestTemplate(self, node):
        """
            Visit all keyword's call in test_template to rename keywordCalled.
        """
        token = node.get_token(Token.NAME)
        if(self.keywordToken == token):
            token.value = self.new_name

    def visit_Template(self, node):
        """
            Visit all keyword's call in template to rename keywordCalled.
        """
        token = node.get_token(Token.NAME)
        if(self.keywordToken == token):
            token.value = self.new_name

    def visit_KeywordCall(self, node):
        """
            Visit keyword calls in test cases to rename keywordCalled.
        """
        token = node.get_token(Token.KEYWORD)
        if(self.keywordToken == token):
            token.value = self.new_name

    def visit_Keyword(self, node):
        """ 
            Visit keyword table to rename keywordDef and keywordCalled
        """
        if(self.keywordNode):
            if(self.keywordNode == node):
                token = node.header.get_token(Token.KEYWORD_NAME)
                token.value = self.new_name
        elif(self.keywordToken):
            for token in node.body:
                if is_KeywordCall(token) and self.keywordToken == token.get_token(Token.KEYWORD):
                    token.get_token(Token.KEYWORD).value = self.new_name
                elif(token.__class__.__name__ == 'Teardown'):
                    self.rename_keyword_from_multiple_keywords(token)

    def rename_keyword_from_multiple_keywords(self, node):
        keywordCall = normalize(node.get_value(Token.NAME))
        if(keywordCall == normalize('Run Keywords')):
            for keywordToken in node.get_tokens(Token.ARGUMENT):
                if(self.keywordToken == keywordToken):
                    keywordToken.value = self.new_name
        else:
            token = node.get_token(Token.NAME)
            if(self.keywordToken == token):
                    keywordToken.value = self.new_name

    def rename_keyword_for_nodes(self, new_name, dictsDefined, dictsCalled):
        
        def rename_keyword_defined(keywordDicts):

            for keywordDict in keywordDicts:
                self.keywordNode = keywordDict['keywordNode']
                self.visit(keywordDict['model'])
                keywordDict['model'].save()
            self.keywordNode = None
        
        def rename_keyword_called(keywordDicts):
            
            for keywordDict in keywordDicts:
                self.keywordToken = keywordDict['token']
                self.visit(keywordDict['model'])
                keywordDict['model'].save()
            self.keywordToken = None

        self.new_name = new_name
        rename_keyword_defined(dictsDefined)
        rename_keyword_called(dictsCalled)
        self.new_name = None
