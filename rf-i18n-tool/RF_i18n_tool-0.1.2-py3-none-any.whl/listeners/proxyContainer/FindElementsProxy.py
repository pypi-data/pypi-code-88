from .Proxy import Proxy
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.remote.webelement import WebElement
from robot.libraries.Screenshot import Screenshot
from robot.api import logger
import I18nListener as i18n
import sys
import ManyTranslations as ui

class FindElementsProxy(Proxy):
    def __init__(self, arg_format):
        arg_format[repr(['by=\'id\'', 'value=None'])] = self
        # 'Page Should Contain Element' 會呼叫此proxy
        # value是要找的element的locator , by(是"xpath:")
    def i18n_Proxy(self, func):
        def proxy(self, by='id', value=None):
            if isinstance(value, WebElement):  #檢查機制
                return func(self, by, value)
            
            #創出該次呼叫的參數紀錄
            full_args = [value]

            #翻譯 ， 針對xpath中需要被翻譯的部分(屬性)
            BuiltIn().import_library('SeleniumLibrary')
            locator = i18n.I18nListener.MAP.locator(BuiltIn().replace_variables(value), full_args) 
                #會呼叫i18nMap的locator(),內部會翻譯xpath內需要翻譯的文字部分，
                #並會設定multiple_translation_words，讓下一行get_multiple_translation_words()取用
            multiple_translation_words = i18n.I18nListener.MAP.get_multiple_translation_words() 

            is_actual = False
            xpath = ''
            #遭遇一詞多譯
            if len(locator) > 1:
                FindElementsProxy.show_warning(self, value, multiple_translation_words, full_args)

                #判斷case會過或fail
                for i, translation_locator in enumerate(locator):
                    #把每種trans_locator用 '|' 串起來， 此種作法之後可以refactor
                    xpath += '|' + translation_locator.replace('xpath:', '') if i != 0 else translation_locator.replace('xpath:', '')
                    #如果畫面上有該翻譯
                    is_actual = BuiltIn().run_keyword_and_return_status('Get WebElement', translation_locator) 
                    if is_actual:
                        break
                    
                if is_actual: #pass
                    # 對預計開啟的UI做一些準備
                    i18n.I18nListener.Is_Multi_Trans = True
                    
                    if str(full_args)+multiple_translation_words[0] not in ui.UI.unique_log:#FIXME
                        word_translation = i18n.I18nListener.MAP.values(multiple_translation_words, full_args)
                        ui.UI.origin_xpaths_or_arguments.append(full_args)
                        ui.UI.add_trans_info(self, multiple_translation_words, word_translation, full_args, func.__name__)
                        
                    actual_locator_message = "System use the locator:'%s' to run!\n" %translation_locator
                    logger.info(actual_locator_message)
                        
            else:# 沒有遭遇一詞多譯的情況
                xpath = locator[0] #直接選第一個當xpath。否則一詞多譯的xpath是一串由 or 組成的string
            return func(self, by, BuiltIn().replace_variables(xpath))
        return proxy

    def show_warning(self, locator, multiple_translation_words, full_args):
        language = 'i18n in %s:\n ' %i18n.I18nListener.LOCALE
        test_name = BuiltIn().get_variable_value("${TEST NAME}")
        message_for_words = Proxy().deal_warning_message_for_list(multiple_translation_words, full_args,  'MULTI_TRANS_WORDS')
        message = language + 'Test Name: ' + test_name + '\n' + 'locator: ' + locator +'\n'+ \
              message_for_words + '\n' + 'You should verify translation is correct!'
        if message_for_words:
            logger.warn(message)
            # Screenshot().take_screenshot(width=700)