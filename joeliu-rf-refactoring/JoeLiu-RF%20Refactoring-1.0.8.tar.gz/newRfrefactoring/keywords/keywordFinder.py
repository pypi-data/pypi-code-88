import ast
from robot.api import Token
from ..common.utility import normalize, get_keywords_for_run_keywords, is_KeywordCall, is_ForLoop


class KeywordFinder(ast.NodeVisitor):

    def __init__(self):
        self.keywordCallList = []
        self.keywordDefList = []
        self.linesKeywords = []
        self.model = None
        self.targetKeyword = None
        self.byKeywordName = False
        self.byLines = False

    def visit_SuiteSetup(self, node):
        """
            Visit all keyword's call in suite_setup to do something.
        """
        if self.byKeywordName:
            self.append_keywordCall_of_multiple_keywords_into_list(node)
        elif self.byLines:
            self.append_keyword_by_lines_for_run_keywords(node)

    def visit_SuiteTeardown(self, node):
        """
            Visit all keyword's call in suite_teardown to do something.
        """
        if self.byKeywordName:
            self.append_keywordCall_of_multiple_keywords_into_list(node)
        elif self.byLines:
            self.append_keyword_by_lines_for_run_keywords(node)

    def visit_TestSetup(self, node):
        """
            Visit all keyword's call in test_setup to do something.
        """
        if self.byKeywordName:
            self.append_keywordCall_of_multiple_keywords_into_list(node)
        elif self.byLines:
            self.append_keyword_by_lines_for_run_keywords(node)

    def visit_TestTeardown(self, node):
        """
            Visit all keyword's call in test_teardown to do something.
        """
        if self.byKeywordName:
            self.append_keywordCall_of_multiple_keywords_into_list(node)
        elif self.byLines:
            self.append_keyword_by_lines_for_run_keywords(node)

    def visit_Setup(self, node):
        """
            Visit keyword calls in test cases to get keywordDef and keywordCalled
        """
        if self.byKeywordName:
            self.append_keywordCall_of_multiple_keywords_into_list(node)
        elif self.byLines:
            self.append_keyword_by_lines_for_run_keywords(node)

    def visit_Teardown(self, node):
        """
            Visit keyword calls in test cases to get keywordDef and keywordCalled
        """
        if self.byKeywordName:
            self.append_keywordCall_of_multiple_keywords_into_list(node)
        elif self.byLines:
            self.append_keyword_by_lines_for_run_keywords(node)

    def visit_TestTemplate(self, node):
        """
            Visit all keyword's call in test_template to get keywordDef and keywordCalled
        """
        if self.byKeywordName:
            self.append_keywordCall_into_list(node.value, node.get_token(Token.NAME))
        elif self.byLines:
            self.append_keyword_by_lines(node)

    def visit_Template(self, node):
        """
            Visit keyword calls in test cases to get keywordDef and keywordCalled
        """
        if self.byKeywordName:
            self.append_keywordCall_into_list(node.value, node.get_token(Token.NAME))
        elif self.byLines:
            self.append_keyword_by_lines(node)

    def visit_ForLoop(self, node):
        if self.byLines:
            self.append_keyword_by_lines_for_forloop(node)

    def visit_KeywordCall(self, node):
        """
            Visit keyword calls in test cases to get keywordDef and keywordCalled
        """
        if self.byKeywordName:
            self.append_keywordCall_into_list(node.keyword, node.get_token(Token.KEYWORD))
        elif self.byLines:
            self.append_keyword_by_lines(node)

    def visit_Keyword(self, node):
        """ 
            Visit keyword table to get keywordDef and keywordCalled
        """
        if self.byKeywordName:
            keywordDef = node.header.get_value(Token.KEYWORD_NAME)
            self.append_keywordDef_into_list(keywordDef, node)
            
            for token in node.body:
                if is_KeywordCall(token):
                    self.append_keywordCall_into_list(token.get_value(Token.KEYWORD), token.get_token(Token.KEYWORD))
                elif(token.__class__.__name__ == 'Teardown'):
                    self.append_keywordCall_of_multiple_keywords_into_list(token)
        elif self.byLines:
            for bodyMember in node.body:
                if is_KeywordCall(bodyMember):
                    self.append_keyword_by_lines(bodyMember)
                elif is_ForLoop(bodyMember):
                    self.append_keyword_by_lines_for_forloop(bodyMember)
                elif(bodyMember.__class__.__name__ == 'Teardown'):
                    self.append_keyword_by_lines_for_run_keywords(bodyMember)

    def find_keywords_by_lines(self, model, startLine, endLine):
        self.byLines = True
        self.startLine = startLine
        self.endLine = endLine
        self.model = model
        self.visit(model)
        self.byLines = False

    def append_keyword_by_lines(self, node):
        if(node.lineno >= self.startLine and node.lineno <= self.endLine):
            nodeDict = {'model': self.model, 'node': node}
            self.linesKeywords.append(nodeDict)

    def append_keyword_by_lines_for_forloop(self, loopNode):
        nodeDict = {'containFor': False, 'model': self.model, 'node': loopNode, 'body': list(loopNode.body)}
        if loopNode.lineno >= self.startLine and loopNode.lineno <= self.endLine:
            nodeDict['containFor'] = True
        for loopBodyMember in loopNode.body:
            if(loopBodyMember.lineno < self.startLine or loopBodyMember.lineno > self.endLine):
                nodeDict['body'].remove(loopBodyMember)
        if len(nodeDict['body']) != 0:
            self.linesKeywords.append(nodeDict)

    def append_keyword_by_lines_for_run_keywords(self, node):
        keyword = normalize(node.name)
        if(keyword == normalize('Run Keywords')):
            runKeywordsBody = get_keywords_for_run_keywords(node.get_tokens(Token.ARGUMENT))
            for keywordDict in list(runKeywordsBody):
                if (keywordDict['keywordName'].lineno < self.startLine or keywordDict['keywordName'].lineno > self.endLine):
                    runKeywordsBody.remove(keywordDict)
            nodeDict = {'containTag': False, 'model': self.model, 'node': node, 'body': runKeywordsBody}
            if node.lineno >= self.startLine and node.lineno <= self.endLine:
                nodeDict['containTag'] = True
            if len(nodeDict['body']) != 0:
                self.linesKeywords.append(nodeDict)
        elif(node.lineno >= self.startLine and node.lineno <= self.endLine):
            nodeDict = {'model': self.model, 'node': node, 'body':[]}
            self.linesKeywords.append(nodeDict)

    def visit_model_for_finding_keyword(self, model, keyword):
        """ 
            Start visiting model.
        """
        self.byKeywordName = True
        self.targetKeyword = normalize(keyword)
        self.model = model
        self.visit(model)
        self.byKeywordName = False

    def visit_models_for_finding_keyword(self, models, keyword):
        """ 
            Start visiting every models.
        """
        for model in models:
            if isinstance(model, list):
                self.visit_models_for_finding_keyword(model, keyword)
            else:
                self.visit_model_for_finding_keyword(model, keyword)

    def append_keywordCall_into_list(self, actualKeywordName, keywordToken, nodes=[]):
        if normalize(actualKeywordName) == self.targetKeyword:
            nodeDict = {'model': self.model, 'nodes': nodes, 'token': keywordToken}
            self.keywordCallList.append(nodeDict)

    def append_keywordCall_of_multiple_keywords_into_list(self, node):
        keywordCall = normalize(node.get_value(Token.NAME))
        if(keywordCall == normalize('Run Keywords')):
            for keywordToken in node.get_tokens(Token.ARGUMENT):
                self.append_keywordCall_into_list(keywordToken.value, keywordToken, node)
        else:
            self.append_keywordCall_into_list(keywordCall, node.get_token(Token.NAME))

    def append_keywordDef_into_list(self, actualKeywordName, keywordNode):
        if normalize(actualKeywordName) == self.targetKeyword:
            nodeDict = {'model': self.model, 'keywordNode': keywordNode}
            self.keywordDefList.append(nodeDict)

    def clear_keyword_calls(self):
        self.keywordCallList = []

    def clear_keyword_defs(self):
        self.keywordDefList = []

    def clear_lines_keywords(self):
        self.linesKeywords = []

    def get_keyword_calls(self):
        return self.keywordCallList

    def get_keyword_defs(self):
        return self.keywordDefList

    def get_lines_keywords(self):
        returnList = list(self.linesKeywords)
        self.clear_lines_keywords()
        return returnList

    def get_moved_keyword(self, keywordLine):
        definedKeyword = self.get_keyword_defs
        for keyword in definedKeyword:
            if keyword['keywordNode'].lineno == keywordLine:
                return keyword
        return None