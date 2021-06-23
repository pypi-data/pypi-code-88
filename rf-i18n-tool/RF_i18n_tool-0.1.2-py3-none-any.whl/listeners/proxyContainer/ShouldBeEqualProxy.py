from .Proxy import Proxy
from robot.libraries.BuiltIn import BuiltIn
import sys
from robot.libraries.Screenshot import Screenshot
from robot.api import logger
import I18nListener as i18n
import ManyTranslations as ui

class ShouldBeEqualProxy(Proxy):
    def __init__(self, arg_format):
        arg_format[repr(['first', 'second', 'msg=None', 'values=True', 'ignore_case=False', 'formatter=\'str\'' ])] = self
    
    def i18n_Proxy(self, func):
        def proxy(self, first, second, msg=None, values=True, ignore_case=False, formatter='str'):
            # logger.warn("ShouldBeEqual")
            if 'not' in func.__name__:
                compare = lambda x,y:True if x != y else False
            else:
                compare = lambda x,y:True if x == y else False

            #創出該呼叫的參數紀錄
            full_args = [first, second]

            #翻譯
            first_trans = i18n.I18nListener.MAP.value(first, full_args)
            second_trans = i18n.I18nListener.MAP.value(second, full_args)

            #遭遇一詞多譯
            if len(first_trans) >1 or len(second_trans) > 1 : 
                # logger.warn("have multi trans")
                ShouldBeEqualProxy.show_warning(self, first, second, full_args)  

                ##判斷case會過還是fail 
                
                for ft in first_trans:
                    for st in second_trans:
                        if compare(ft,st): #
                            # FIXME 現在會fail的話不顯示UI(但會過的話會把"所有"翻譯詞顯示在UI上)(參考下面實作)
                            # 並且也會把完整xpath或arguments顯示在UI上
                            i18n.I18nListener.Is_Multi_Trans = True

                            if len(first_trans) > 1 and str(full_args)+first not in ui.UI.unique_log:
                                multiple_translation_word = []     
                                multiple_translation_word.append(first) #將expected word包裝成list格式
                                ui.UI.origin_xpaths_or_arguments.append(full_args)
                                ui.UI.add_trans_info(self, multiple_translation_word, first_trans, full_args, func.__name__) #將翻譯詞加進等等UI會用到的dictionary中

                            if len(second_trans) > 1 and str(full_args)+second not in ui.UI.unique_log:
                                multiple_translation_word = []     
                                multiple_translation_word.append(second) #將expected word包裝成list格式
                                ui.UI.origin_xpaths_or_arguments.append(full_args)
                                ui.UI.add_trans_info(self, multiple_translation_word, second_trans, full_args, func.__name__) #將翻譯詞加進等等UI會用到的dictionary中
                            return func(self, ft, st, msg, values, ignore_case, formatter)
            return func(self, first_trans[0], second_trans[0], msg, values, ignore_case, formatter) 
            #執行到這行可能有兩種情況: 1.沒有一詞多譯(回傳第一組翻譯，也就是原本的翻譯) 2.一詞多譯的翻譯詞找不到會讓case過的(回傳第一組翻譯)
        return proxy
    
    def deal_translate_message(self, value, full_args, message_title):
        translation = i18n.I18nListener.MAP.value(value, full_args)[0]
        if value != translation:
            message = ('%s argument evaluates to' + ' ' + '\'%s\'' + ' is translated to: ' + '\'%s\'') %(message_title, value, translation)  + '\n'
        else:
            message = ('%s argument evaluates to' + ' ' + '\'%s\'') %(message_title, value)  + '\n'
        return message

    def show_warning(self, first, second, full_args): 
        language = 'i18n in %s:\n ' %i18n.I18nListener.LOCALE
        test_name = ('Test Name: %s') %BuiltIn().get_variable_value("${TEST NAME}") + '=> Exist multiple translations of the word' + '\n'
        message_for_first = Proxy().deal_warning_message_for_one_word(first, full_args,  'First')
        message_for_second = Proxy().deal_warning_message_for_one_word(second, full_args, 'Second')
        message = language + test_name + message_for_first + ' '*3 + '\n' +  message_for_second + '\n' + 'You should verify translation is correct!'
        if message_for_first or message_for_second:
            logger.warn(message)
        else:
            message_for_first = ShouldBeEqualProxy.deal_translate_message(self, first, full_args,'First')
            message_for_second = ShouldBeEqualProxy.deal_translate_message(self, second, full_args,'Second')
            message = language +' ' + message_for_first + ' '*2 +  message_for_second
            logger.info(message)
