from robot.api import Token
from robot.parsing.model import Statement
from ..common.utility import is_ForLoop, is_Keyword_tag, is_KeywordCall, normalize
from ..builder.testModelBuilder import TestModelBuilder

class LineKeywordsHelper():

    def get_line_keyword_from_line_keywords(self, lineKeywords, line):
        for lineKeyword in lineKeywords:
            if is_KeywordCall(lineKeyword['node']):
                if lineKeyword['node'].lineno == line:
                    return {'belong': lineKeyword, 'node': lineKeyword['node']}
            elif is_ForLoop(lineKeyword['node']):
                for loopBodyMember in lineKeyword['body']:
                    if loopBodyMember.lineno == line:
                        return {'belong': lineKeyword, 'node': loopBodyMember}
            elif is_Keyword_tag(lineKeyword['node']):
                if len(lineKeyword['body']) != 0:
                    for keyword in lineKeyword['body']:
                        if keyword['keywordName'].lineno == line:
                            return {'belong': lineKeyword, 'node': keyword}
                elif lineKeyword['node'].lineno == line:
                    return {'belong': lineKeyword, 'node': lineKeyword['node']}
        return None

    def get_arguments_for_line_keyword(self, keywordWithLine):
        if is_KeywordCall(keywordWithLine['belong']['node']):
            return keywordWithLine['node'].args
        elif is_ForLoop(keywordWithLine['belong']['node']):
            return keywordWithLine['node'].args
        elif is_Keyword_tag(keywordWithLine['belong']['node']):
            if len(keywordWithLine['belong']['body']) != 0:
                return keywordWithLine['node']['arguments']
            else:
                return keywordWithLine['node'].args

    def update_arguments_of_line_keyword(self, lineKeywordsList, updatedArgData):
        isUpdated = False

        for lineKeyword in lineKeywordsList:
            if isUpdated:
                break
            if lineKeyword == updatedArgData['lineKeyword']['belong']:
                if(is_KeywordCall(lineKeyword['node']) and lineKeyword['node'] == updatedArgData['lineKeyword']['node']):
                    keywordArgsTokens = lineKeyword['node'].get_tokens(Token.ARGUMENT)
                    for arg in keywordArgsTokens:
                        if str(arg.value) == str(updatedArgData['updateArg']):
                            arg.value = updatedArgData['newArg']
                            isUpdated = True
                            break
                elif is_ForLoop(lineKeyword['node']):
                    for member in lineKeyword['body']:
                        if member == updatedArgData['lineKeyword']['node']:
                            keywordArgsTokens = member.get_tokens(Token.ARGUMENT)
                            for arg in keywordArgsTokens:
                                if str(arg.value) == str(updatedArgData['updateArg']):
                                    arg.value = updatedArgData['newArg']
                                    isUpdated = True
                                    break
                elif is_Keyword_tag(lineKeyword['node']):
                    if len(lineKeyword['body']) != 0:
                        for keyword in lineKeyword['body']:
                            if keyword == updatedArgData['lineKeyword']['node']:
                                for arg in keyword['arguments']:
                                    if str(arg.value) == str(updatedArgData['updateArg']):
                                        arg.value = updatedArgData['newArg']
                                        isUpdated = True
                                        break
                    elif lineKeyword['node'] == updatedArgData['lineKeyword']['node']:
                        keywordArgsTokens = lineKeyword['node'].get_tokens(Token.ARGUMENT)
                        for arg in keywordArgsTokens:
                            if str(arg.value) == str(updatedArgData['updateArg']):
                                arg.value = updatedArgData['newArg']
                                isUpdated = True
                                break

    def get_new_keyword_body_from_line_keywords_and_arguments_tokens(self, lineKeywords, argsTokens):
        keywordsBody = []
        if len(argsTokens) != 0:
            arguments = Statement.from_tokens(argsTokens)
            keywordsBody.append(arguments)
        for index, lineKeyword in enumerate(lineKeywords):
            if is_ForLoop(lineKeyword['node']):
                if lineKeyword['containFor']:
                    keywordsBody.append(lineKeyword['node'])
                else:
                    for loopBodyMember in lineKeyword['body']:
                        keywordsBody.append(loopBodyMember)
            elif is_Keyword_tag(lineKeyword['node']):
                if lineKeyword['containTag'] and index != 0:
                    keywordsBody.append(lineKeyword['node'])
                else:
                    for keyword in lineKeyword['body']:
                        argumentsValues = []
                        for arg in keyword['arguments']:
                            argumentsValues.append(arg.value)
                        keywordCall = TestModelBuilder().build_keywordCall('    ', keyword['keywordName'].value, argumentsValues)
                        keywordsBody.append(keywordCall)
            else:
                keywordsBody.append(lineKeyword['node'])
        return keywordsBody

    def get_same_keywords_block_text(self, sameStepsBlock):
            def get_keywordCall_text(node):
                text = node.keyword
                for arg in node.args:
                    text += ('    ' + arg)
                text += '\n'
                return text
            
            def get_loop_info_text(node):
                text = 'For'
                for variable in node.variables:
                    text += (' ' + variable)
                text += ( ' ' + node.flavor)
                for value in node.values:
                    text += (' ' + value)
                text += "\n"
                return text

            def get_tag_keyword_text(node):
                text = ('    [' + node.__class__.__name__ + ']')
                text += ('    ' + node.name)
                if normalize(sameStep['node'].name) != normalize('Run Keywords'):
                    for arg in node.args:
                        text += ('    ' + arg)
                return text

            def get_run_keywords_body_text(body):
                text = ('    ' + body['keywordName'].value)
                for arg in body['arguments']:
                    text += ('    ' + arg.value)
                text += '\n'
                return text


            present_result = ''
            loopFirst = True
            runKeywordsFirst = True
            for sameStep in sameStepsBlock:
                if is_KeywordCall(sameStep['node']):
                    if not(loopFirst):
                        present_result += 'END'
                    loopFirst = True
                    runKeywordsFirst = True
                    present_result += get_keywordCall_text(sameStep['node'])
                elif is_ForLoop(sameStep['node']):
                    runKeywordsFirst = True
                    if loopFirst:
                        present_result += get_loop_info_text(sameStep['node'])
                        if is_KeywordCall(sameStep['keyword']):
                            present_result += ('    ' + get_keywordCall_text(sameStep['keyword']))
                        loopFirst = False
                    else:
                        if is_KeywordCall(sameStep['keyword']):
                            present_result += ('    ' + get_keywordCall_text(sameStep['keyword']))
                elif is_Keyword_tag(sameStep['node']):
                    if not(loopFirst):
                        present_result += 'END\n'
                    loopFirst = True
                    if normalize(sameStep['node'].name) != normalize('Run Keywords'):
                            present_result += get_tag_keyword_text(sameStep['node']) + '\n'
                    else:
                        if runKeywordsFirst:
                            runKeywordsFirst = False
                            present_result += get_tag_keyword_text(sameStep['node'])
                            present_result += get_run_keywords_body_text(sameStep['keyword'])
                        else:
                            present_result += ('    ...    AND' + get_run_keywords_body_text(sameStep['keyword']))

            return present_result
    
    def get_local_variables_in_line_keywords(self, lineKeywords):
        localVariables = []
        for lineKeyword in lineKeywords:
            if is_KeywordCall(lineKeyword['node']):
                for variable in lineKeyword['node'].assign:
                    if normalize(variable) != normalize(''):
                        localVariables.append(variable)
            elif is_ForLoop(lineKeyword['node']):
                for variable in lineKeyword['node'].variables:
                    if not(variable in localVariables):
                        localVariables.append(variable)
                for keyword in lineKeyword['body']:
                    if is_KeywordCall(keyword):
                        for variable in keyword.assign:
                            if normalize(variable) != normalize(''):
                                localVariables.append(variable)
        for index, localVariable in enumerate(localVariables):
            localVariables[index] = localVariable.replace(' ','').replace('=','')
        return list(set(localVariables))

    def get_variables_not_defined_in_lineKeywords(self, lineKeywords, localVariables):
        variablesNotDefined = []
        prefixVariable = ['@{', '${', '&{']
        for lineKeyword in lineKeywords:
            if is_KeywordCall(lineKeyword['node']):
                for arg in lineKeyword['node'].args:
                    for prefix in prefixVariable:
                        if arg.find(prefix) == 0 and not(arg in localVariables):
                            variablesNotDefined.append(arg)
                            break
            elif is_ForLoop(lineKeyword['node']):
                for value in lineKeyword['node'].values:
                    for prefix in prefixVariable:
                        if value.find(prefix) == 0 and not(value in localVariables):
                            variablesNotDefined.append(value)
                            break
                for keyword in lineKeyword['body']:
                    if is_KeywordCall(keyword):
                        for arg in keyword.args:
                            for prefix in prefixVariable:
                                if arg.find(prefix) == 0 and not(arg in localVariables):
                                    variablesNotDefined.append(arg)
                                    break
            elif is_Keyword_tag(lineKeyword['node']):
                if normalize(lineKeyword['node'].name) != normalize('Run Keywords'):
                    for arg in lineKeyword['node'].args:
                        for prefix in prefixVariable:
                            if arg.find(prefix) == 0 and not(arg in localVariables):
                                variablesNotDefined.append(arg)
                                break
                else:
                    for keyword in lineKeyword['body']:
                        for arg in keyword['arguments']:
                            for prefix in prefixVariable:
                                if arg.value.find(prefix) == 0 and not(arg.value in localVariables):
                                    variablesNotDefined.append(arg.value)
                                    break
        return list(set(variablesNotDefined))
