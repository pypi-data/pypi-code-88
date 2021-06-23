from .Proxy import Proxy
from robot.libraries.BuiltIn import BuiltIn
import sys
from robot.libraries.Screenshot import Screenshot
from robot.api import logger
import I18nListener as i18n
import ManyTranslations as ui

class ElementTextShouldBeProxy(Proxy): #FIXME 此proxy還有待refactor
    def __init__(self, arg_format):
        arg_format[repr(['locator', 'expected', 'message=None', 'ignore_case=False'])] = self
    
    def i18n_Proxy(self, func):
        def proxy(self, locator, expected, message=None, ignore_case=False): #locator://*[@text='支援'](locator有時並不需要翻譯) expected:support
            
            #創出該呼叫的參數紀錄
            full_args = [locator, expected]

            #翻譯
            possible_translations = i18n.I18nListener.MAP.value(expected, full_args) #support可能map成支援/支援服務

            actual_text = ''
            #遭遇一詞多譯
            if len(possible_translations) > 1:
                ElementTextShouldBeProxy.show_warning(self, expected, full_args)

                #判斷原本case會過還是fail 

                #pass
                i18n.I18nListener.Is_Multi_Trans = True

                if str(full_args)+expected not in ui.UI.unique_log:
                    multiple_translation_words = []
                    multiple_translation_words.append(expected) #將expected word包裝成list格式
                    ui.UI.origin_xpaths_or_arguments.append(full_args)
                    ui.UI.add_trans_info(self, multiple_translation_words, possible_translations, full_args, func.__name__)

                BuiltIn().import_library('SeleniumLibrary')
                actual_text = BuiltIn().run_keyword('Get Text', locator) #有多種翻譯，取得locator的字當作actual text #FIXME 此作法不是很好
            
            else:# 沒有遭遇一詞多譯 或者 有一詞多譯但case會fail
                actual_text = possible_translations[0]
            
            actual_text_message = "'%s'is currently resolved as'%s'\n" %(expected, actual_text)
            logger.info(actual_text_message)
            return func(self, BuiltIn().replace_variables(locator), actual_text, message, ignore_case) if actual_text in possible_translations else func(self, BuiltIn().replace_variables(locator), expected, message, ignore_case)
                                #locator://*[@text='支援'] , expected(support)以修正過後的actual text(支援)代替
        return proxy
    
    def show_warning(self, expected, full_args):
        language = 'i18n in %s:\n ' %i18n.I18nListener.LOCALE
        test_name = ('Test Name: %s') %BuiltIn().get_variable_value("${TEST NAME}") + '=> Exist multiple translations of the word' + '\n'
        message_for_expected = Proxy().deal_warning_message_for_one_word(expected, full_args, 'Expected')
        if message_for_expected :
            if expected not in i18n.I18nListener.Not_SHOW_WARNING_WORDS:   
                message = language + test_name + message_for_expected + ' '*3 + '\n' + 'You should verify translation is correct!'
                logger.warn(message)
            else:
                message = 'Detail Information\n' + language + message_for_expected + ' '*3  + '\nYou had resolved the multiple translations of the word: \'%s\'' %(expected)
                logger.info(message)