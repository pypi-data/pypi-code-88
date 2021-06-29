import sys
from os import path
p = path.normpath(path.dirname(path.abspath(__file__))+"/../..")
sys.path.append(p)
from python_package.newRfrefactoring.common.threadWithReturn import BuildingModelThread
from python_package.newRfrefactoring.builder.testModelBuilder import TestModelBuilder
from python_package.newRfrefactoring.keywords.keywordFinder import KeywordFinder
from python_package.newRfrefactoring.checker.fileChecker import FileChecker
from python_package.newRfrefactoring.keywords.keywordCreator import KeywordCreator
from python_package.newRfrefactoring.keywords.keywordPrinter import KeywordPrinter
from python_package.newRfrefactoring.keywords.keywordMoveHelper import KeywordMoveHelper
from python_package.newRfrefactoring.helper.lineKeywordsHelper import LineKeywordsHelper
from python_package.newRfrefactoring.common.utility import *
from prettytable import PrettyTable

builder = TestModelBuilder()
finder = KeywordFinder()
checker = FileChecker()
creator = None
lineKwsHelper = LineKeywordsHelper()
kwPrinter = KeywordPrinter()
mover = None

def get_arguments_of_new_keyword_from_user(lineKeywords):
    newKeywordArgs = []
    while True:
        clear_screen()
        print('According to your data we found the following information and we will wrap these keywords as a new keyword.')
        kwPrinter.print_all_lines_keywords(lineKeywords)
        if len(newKeywordArgs) == 0:
            print('\nNew keyword without arguments now.')
        else:
            print_arugments_for_string_list(newKeywordArgs)
            print('')
        arg = input('If you want to add a new argument for new keyword, please input argument content.\nIf you don\'t want to add a new argument, please input \'Exit\'.\n\nNew argument' + str(len(newKeywordArgs) + 1) + ':')
        if normalize(arg) == normalize('Exit'):
            break
        else:
            newKeywordArgs.append(arg)
    return newKeywordArgs

def print_arugments_for_string_list(args):
    print('\nThe following information is new keyword\'s arguments now.')
    argsTable = PrettyTable()
    argsTable.field_names = ['Number', 'Argument']
    for index, arg in enumerate(args):
        argsTable.add_row([index + 1, arg])
    print(argsTable)

def is_arguemnts_changed_from_user(arg, isFirst):
    isChangeArgument = ''
    while(normalize(isChangeArgument) != normalize('Y') and normalize(isChangeArgument) != normalize('N')):
        if isFirst:
            isChangeArgument = input('\nDo you want to change keywords\' arguments with new argument \"'+ arg +'\"?(Y\\N):')
        else:
            isChangeArgument = input('Do you want to change other keywords\' arguments with new argument \"'+ arg +'\"?(Y\\N):')

    return normalize(isChangeArgument) == normalize('Y')

def is_anwser_yes(text):
    isReplace = ''
    while(normalize(isReplace) != normalize('Y') and normalize(isReplace) != normalize('N')):
        isReplace = input(text)

    return normalize(isReplace) == normalize('Y')

def update_keywords_arguments(lineKeywords, newKeywordArgs):
    newKeywordArgsTokens = []
    for arg in newKeywordArgs:
        clear_screen()
        print_arugments_for_string_list(newKeywordArgs)
        isFirst = True
        while is_arguemnts_changed_from_user(arg, isFirst):
            clear_screen()
            kwPrinter.print_all_lines_keywords(lineKeywords)
            line = int(get_number_from_user('Please input line that you want to change.\nLine:'))
            keywordWithLine = lineKwsHelper.get_line_keyword_from_line_keywords(lineKeywords, line)
            clear_screen()
            if keywordWithLine:
                print('This is the keyword\'s information now.')
                kwPrinter.print_line_keyword(keywordWithLine['node'])
                argNum = int(get_number_from_user('Please input the argument number which you want to replace with \"' + arg + '\"\n(Ex:1)\nArgument number:'))
                lineKeywordArgs = lineKwsHelper.get_arguments_for_line_keyword(keywordWithLine)
                while not(argNum > 0 and argNum <= len(lineKeywordArgs)):
                    print('Please input correct argument number.')
                    argNum = int(get_number_from_user('Please input the argument number which you want to replace with \"' + arg + '\"\n(Ex:1)\nArgument number:'))
                updatedData = {'lineKeyword': keywordWithLine, 'updateArg': lineKeywordArgs[int(argNum) - 1], 'newArg': arg}
                lineKwsHelper.update_arguments_of_line_keyword(lineKeywords, updatedData)
                clear_screen()
            else:
                print('There is not keyword in line that you input.')
            isFirst = False

def replace_steps_with_a_new_keyword(modelsWithSameKeywords, allModels, newKeywordName, newKeywordArgs):
    replacedStepsModels = []
    if len(modelsWithSameKeywords) != 0 and is_anwser_yes('The steps are same in '+ str(len(modelsWithSameKeywords)) +' places\nDo you want to replace same steps in other files with new keyword?(Y\\N):'):
        for modelWithSameKeywords in modelsWithSameKeywords:
            replacedStepsModels.append(modelWithSameKeywords[0]['model'])
            clear_screen()
            kwPrinter.print_model_with_same_keywords(modelWithSameKeywords)
            if is_anwser_yes('Do you want to replace the steps with new keyword?(Y\\N):'):
                clear_screen()
                keywordArgs = []
                for index, newArg in enumerate(newKeywordArgs):
                    print_arugments_for_string_list(newKeywordArgs)
                    arg = input('Please input \"'+ newArg +'\" content.\nIf you finish inputting argument, please input \'Exit\'.\n\nArgument' + str(index + 1)+'('+ newArg + '):')
                    if normalize(arg) == normalize('Exit'):
                        break
                    else:
                        keywordArgs.append(arg)
                    clear_screen()
                newKeywordDict = {'keywordName': newKeywordName, 'arguments': keywordArgs}
                creator.replace_old_steps_with_keyword_for_same_keywords(newKeywordDict, modelWithSameKeywords)
    return replacedStepsModels


def import_resource_where_new_keyword(newKeywordName, modelsWithReplacement, newKeywordPath):
    modelsWithoutImport = mover.get_models_without_import_new_resource_from_models_with_replacement(newKeywordName, modelsWithReplacement, newKeywordPath)
    if len(modelsWithoutImport) != 0:
        pathWithoutImportTable = PrettyTable()
        pathOfNewKeywordTable = PrettyTable()
        pathWithoutImportTable.field_names = ['Path without importing resource of new keyword']
        pathOfNewKeywordTable.field_names = ['Path of resource where new keyword is']
        for model in modelsWithoutImport:
            pathWithoutImportTable.add_row([model.source])
        print('The Following path(s) don\'t import resource of new keyword.')
        print(pathWithoutImportTable)
        if is_anwser_yes('Do you want to import resource for them(it)?(Y\\N):'):
            for model in modelsWithoutImport:
                clear_screen()
                pathWithoutImportTable.clear_rows()
                pathOfNewKeywordTable.clear_rows()
                pathWithoutImportTable.add_row([model.source])
                pathOfNewKeywordTable.add_row([newKeywordPath])
                print(pathWithoutImportTable)
                print(pathOfNewKeywordTable)
                resourceStr = input('Please input resource value that you want to import for it.\nResource value:')
                mover.import_new_resource_for_model(model, resourceStr)

def import_resource_where_moved_keyword(movedKeywordName, fromFilePath, targetFilePath):
    modelsWithoutImport = mover.get_models_without_import_new_resource(movedKeywordName, fromFilePath, targetFilePath)
    if len(modelsWithoutImport) != 0:
        pathWithoutImportTable = PrettyTable()
        pathOfTargetFileTable = PrettyTable()
        pathWithoutImportTable.field_names = ['Path without importing target file']
        pathOfTargetFileTable.field_names = ['Path of target file']
        for model in modelsWithoutImport:
            pathWithoutImportTable.add_row([model.source])
        print('The Following path(s) don\'t import target file.')
        print(pathWithoutImportTable)
        if is_anwser_yes('Do you want to import resource for them(it)?(Y\\N):'):
            for model in modelsWithoutImport:
                clear_screen()
                pathWithoutImportTable.clear_rows()
                pathOfTargetFileTable.clear_rows()
                pathWithoutImportTable.add_row([model.source])
                pathOfTargetFileTable.add_row([targetFilePath])
                print(pathWithoutImportTable)
                print(pathOfTargetFileTable)
                resourceStr = input('Please input resource value that you want to import for it.\nResource value:')
                mover.import_new_resource_for_model(model, resourceStr)

def wrap_steps_as_a_new_keyword():
    global creator
    global mover
    projectPath = get_folder_path_from_user('Please input the folder\'s path which will be scanned.\nEx:D:/test_data\nScanned folder path:')
    clear_screen()
    # projectPath = 'C:/Users/Gene/Desktop/Thesis_For_Refactor/python_package/test_data'
    # projectPath = 'D:/Thesis Local/Thesis_For_Refactor/python_package/test_data'
    # projectPath = 'D:/Project/test_automation'
    projectbuildThread = BuildingModelThread(projectPath)
    projectbuildThread.start()

    fromFilePath = get_file_path_from_user('Please input the file\'s path which has the steps that will be wrapped as a keyword.\nEx:D:/test_data/test_data.robot\nFile path:')
    clear_screen()
    # fromFilePath = 'C:/Users/Gene/Desktop/Thesis_For_Refactor/python_package/test_data/test_data.robot'
    # fromFilePath = 'D:/Thesis Local/Thesis_For_Refactor/python_package/test_data/test_data.robot'
    # fromFilePath = 'D:/Project/test_automation/RobotTests/Feature Tests/Parts Management/TMD-18039 Edit_View Part Instance Detail Page/Keywords/TMD-18137.txt'
    fileBuildThread = BuildingModelThread(fromFilePath)
    fileBuildThread.start()

    startLine = int(get_number_from_user('Please input start line to get steps.\nStart line:'))
    clear_screen()
    endLine = int(get_number_from_user('Please input end line to get steps.\nEnd line:'))
    clear_screen()
    # startLine = 44
    # endLine = 50
    # startLine = 92
    # endLine = 98

    print('Please wait, Models building~')
    allModels = projectbuildThread.join()
    fromModel = fileBuildThread.join()
    creator = KeywordCreator(allModels)
    clear_screen()

    finder.find_keywords_by_lines(fromModel, startLine, endLine)
    lineKeywords = finder.get_lines_keywords()

    checker.find_models_with_same_keywords(allModels, lineKeywords)
    modelsWithSameKeywords = checker.get_models_with_same_keywords()

    newKeywordArgs = get_arguments_of_new_keyword_from_user(lineKeywords)
    # newKeywordArgs = ['${test1}']
    newKeywordArgsTokens = []
    if len(newKeywordArgs) != 0:
        update_keywords_arguments(lineKeywords, newKeywordArgs)
        newKeywordArgsTokens = creator.build_tokens_of_new_keyword_arguments(newKeywordArgs)
    
    newKeywordsBody = lineKwsHelper.get_new_keyword_body_from_line_keywords_and_arguments_tokens(lineKeywords, newKeywordArgsTokens)
    clear_screen()
    kwPrinter.print_all_lines_keywords(lineKeywords)
    newKeywordName = input('Please input name for new keyword.\nKeyword name:')
    # newKeywordName = 'Test123'
    clear_screen()
    newKeywordPath = get_file_path_from_user('Please input the file\'s path where new keyword will insert into.\nFile path:')
    # newKeywordPath = 'C:/Users/Gene/Desktop/Thesis_For_Refactor/python_package/test_data/ezScrum.txt'
    # newKeywordPath = 'D:/Thesis Local/Thesis_For_Refactor/python_package/test_data/ezScrum.txt'
    clear_screen()
    creator.create_new_keyword_for_file(newKeywordPath, newKeywordName, newKeywordsBody)
    #adding
    modelsWithReplacement = replace_steps_with_a_new_keyword(modelsWithSameKeywords, allModels, newKeywordName, newKeywordArgs)
    clear_screen()
    mover = KeywordMoveHelper(allModels)
    import_resource_where_new_keyword(newKeywordName, modelsWithReplacement, newKeywordPath)

def move_defined_keyword_to_another_model():
    global mover
    projectPath = get_folder_path_from_user('Please input the folder\'s path which will be scanned.\nEx:D:/test_data\nScanned folder path:')
    clear_screen()
    projectbuildThread = BuildingModelThread(projectPath)
    projectbuildThread.start()
    movedKeywordName = input('Please input the keyword which you want to move.\nEx:Open The Browser\nMoved keyword\'s name:')
    clear_screen()
    fromFilePath = get_file_path_from_user('Please input the file\'s path where the moved keyword.\nEx:D:/test_data\nFrom file\'s path:')
    fromFilebuildThread = BuildingModelThread(fromFilePath)
    fromFilebuildThread.start()
    clear_screen()
    targetFilePath = get_file_path_from_user('Please input the file\'s path where the moved keyword will be inserted.\nEx:D:/test_data\nTarget file\'s path:')
    targetFilebuildThread = BuildingModelThread(targetFilePath)
    targetFilebuildThread.start()
    clear_screen()
    print('Please wait, Models building~')
    allModels = projectbuildThread.join()
    fromFileModel = fromFilebuildThread.join()
    targetFileModel = targetFilebuildThread.join()
    mover = KeywordMoveHelper(allModels)
    movedKeywordNode = mover.find_moved_keyword_node(fromFileModel, movedKeywordName)
    mover.remove_old_keyword_defined(fromFileModel, movedKeywordNode)
    mover.insert_new_keyword_defined(targetFileModel, movedKeywordNode)
    clear_screen()
    import_resource_where_moved_keyword(movedKeywordName, fromFileModel.source, targetFileModel.source)

if __name__ == '__main__':

    clear_screen()
    print('Please select a mode:')
    print('1. Move defined keyword to another file')
    print('2. Wrap steps as a keyword')
    print('3. Move defined variable to another file')
    print('4. Wrap value as a common variable')
    print('9. Exit system')
    mode = None

    while True:
        mode = input('Mode:')
        clear_screen()
        if(mode == '1.' or mode == '1'):
            move_defined_keyword_to_another_model()
            exit('Thank you for using.')
        elif(mode == '2.' or mode == '2'):
            wrap_steps_as_a_new_keyword()
            exit('Thank you for using.')
        elif(mode == '3.' or mode == '3'):
            exit('Sorry,please waiting we are Developing.')
        elif(mode == '4.' or mode == '4'):
            exit('Sorry,please waiting we are Developing.')
        elif(mode == '9.' or mode == '9'):
            exit('Thank you for using.')
        else:
            print('Please input correct mode')