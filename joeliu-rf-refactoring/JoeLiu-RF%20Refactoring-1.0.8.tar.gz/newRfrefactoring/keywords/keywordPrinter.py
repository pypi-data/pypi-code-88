from ..common.utility import is_ForLoop, is_Keyword_tag, is_KeywordCall, normalize
from prettytable import PrettyTable

class KeywordPrinter():

    def print_keywordCall_for_linesKeywords(self, keywordNode):
        keywordCallStr = PrettyTable()

        fields = ['Line', 'Keyword name']
        keywordData = [keywordNode.lineno, keywordNode.keyword]
        for i, arg in enumerate(keywordNode.args):
            fields.append('Argument' + str(i+1))
            keywordData.append(arg)
        keywordCallStr.field_names = fields
        keywordCallStr.add_row(keywordData)
        print(keywordCallStr)

    def print_for_loop_information(self, loopDict):
        loopStr = PrettyTable()
        fields = []
        loopData = []

        for i, variable in enumerate(loopDict['node'].variables):
            fields.append('Variable' + str(i+1))
            loopData.append(variable)

        fields.append('Flavor')
        loopData.append(loopDict['node'].flavor)

        for i, value in enumerate(loopDict['node'].values):
            fields.append('Values' + str(i+1))
            loopData.append(value)

        loopStr.field_names = fields
        loopStr.add_row(loopData)
        print(loopStr)

    def print_loop_for_linesKeywords(self, loopDict):

        self.print_for_loop_information(loopDict)

        for keyword in loopDict['body']:
            if is_KeywordCall(keyword):
                self.print_keywordCall_for_linesKeywords(keyword)

    def print_keyword_for_tag_keyword(self, keyword):
        keywordStr = PrettyTable()
        fields = []
        keywordData = []
        fields = ['Line', 'Kind', 'Keyword name']

        keywordData.append(keyword.lineno)
        keywordData.append(keyword.__class__.__name__)
        keywordData.append(keyword.name)
        for i, arg in enumerate(keyword.args):
            fields.append('Argument' + str(i+1))
            keywordData.append(arg)
        keywordStr.field_names = fields
        keywordStr.add_row(keywordData)
        print(keywordStr)

    def print_kind_line(self, nodeDict):
        keywordStr = PrettyTable()
        fields = []
        keywordData = []
        fields = ['Line', 'Kind', 'Keyword name']

        keywordData.append(nodeDict['node'].lineno)
        keywordData.append(nodeDict['node'].__class__.__name__)
        keywordData.append(nodeDict['node'].name)
        keywordStr.field_names = fields
        keywordStr.add_row(keywordData)
        print(keywordStr)

    def print_run_keywords_for_linesKeywords(self, runKeywordsDict):

        if len(runKeywordsDict['body']) == 0:
            self.print_keyword_for_tag_keyword(runKeywordsDict['node'])
        else:
            self.print_kind_line(runKeywordsDict)
            for keyword in runKeywordsDict['body']:
                self.print_keyword_for_run_keywords_body(keyword)

    def print_keyword_for_run_keywords_body(self, keyword):
        keywordStr = PrettyTable()
        fields = ['Line', 'Keyword name']
        keywordData = [keyword['keywordName'].lineno,
                       keyword['keywordName'].value]
        for i, arg in enumerate(keyword['arguments']):
            fields.append('Argument' + str(i+1))
            keywordData.append(arg.value)
        keywordStr.field_names = fields
        keywordStr.add_row(keywordData)
        print(keywordStr)

    def print_all_lines_keywords(self, lineKeywords):
        for lineKeyword in lineKeywords:
            if is_KeywordCall(lineKeyword['node']):
                self.print_keywordCall_for_linesKeywords(lineKeyword['node'])
            elif is_ForLoop(lineKeyword['node']):
                self.print_loop_for_linesKeywords(lineKeyword)
            elif is_Keyword_tag(lineKeyword['node']):
                self.print_run_keywords_for_linesKeywords(lineKeyword)

    def print_line_keyword(self, lineKeyword):
        if is_KeywordCall(lineKeyword):
            self.print_keywordCall_for_linesKeywords(lineKeyword)
        elif is_Keyword_tag(lineKeyword):
            self.print_keyword_for_tag_keyword(lineKeyword)
        else:
            self.print_keyword_for_run_keywords_body(lineKeyword)
    
    def print_model_with_same_keywords(self, modelWithSameKeywords):
        pathTable = PrettyTable()

        pathTable.field_names = ['Path of model']
        pathTable.add_row([modelWithSameKeywords[0]['model'].source])
        print(pathTable)
        printNodeList = []
        for sameKeyword in modelWithSameKeywords:
            if is_KeywordCall(sameKeyword['node']):
                self.print_keywordCall_for_linesKeywords(sameKeyword['node'])
            elif is_ForLoop(sameKeyword['node']):
                if not(sameKeyword['node'] in printNodeList):
                    printNodeList.append(sameKeyword['node'])
                    self.print_for_loop_information(sameKeyword)
                if is_KeywordCall(sameKeyword['keyword']):
                    self.print_keywordCall_for_linesKeywords(sameKeyword['keyword'])
            elif is_Keyword_tag(sameKeyword['node']):
                if normalize(sameKeyword['node'].name) == normalize('Run Keywords'):
                    if not(sameKeyword['node'] in printNodeList):
                        printNodeList.append(sameKeyword['node'])
                        self.print_kind_line(sameKeyword)
                    self.print_keyword_for_run_keywords_body(sameKeyword['keyword'])
                else:
                    self.print_keyword_for_tag_keyword(sameKeyword['node'])