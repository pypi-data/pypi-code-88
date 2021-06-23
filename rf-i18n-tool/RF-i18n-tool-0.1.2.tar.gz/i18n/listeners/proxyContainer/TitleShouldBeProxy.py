from .Proxy import Proxy
from robot.libraries.BuiltIn import BuiltIn
import sys
from robot.libraries.Screenshot import Screenshot
from robot.api import logger
import I18nListener as i18n
import ManyTranslations as ui

class TitleShouldBeProxy(Proxy):
    def __init__(self, arg_format):
        arg_format[repr(['title', 'message=None'])] = self
        # 會和網頁視窗的title比較是否相同
    
    def i18n_Proxy(self, func):
        def proxy(self, title, message=None):
            #創出該呼叫的參數紀錄
            full_args = [title]

            #翻譯，如果有一詞多譯的話要藉由判斷，找出正確的翻詞回傳
            title_trans = i18n.I18nListener.MAP.value(title, full_args)
            # logger.warn(title_trans)

            #遭遇一詞多譯
            if len(title_trans)>1:
                TitleShouldBeProxy.show_warning(self, title, full_args) #show warning
                #檢查case會pass or fail
                is_pass = False
                actual = self.get_title()
                for tt in title_trans:
                    if tt == actual:
                        is_pass = True
                        break
                if is_pass: #pass
                    # 對預計開啟的UI做一些準備
                    i18n.I18nListener.Is_Multi_Trans = True

                    if len(title_trans) > 1 and str(full_args)+title not in ui.UI.unique_log:
                        multiple_translation_word = [title]     
                        ui.UI.origin_xpaths_or_arguments.append(full_args)
                        ui.UI.add_trans_info(self, multiple_translation_word, title_trans, full_args, func.__name__) #將翻譯詞加進等等UI會用到的dictionary中
            #將處理好的翻譯回傳給robot原生keyword
            #因為畫面上的title是唯一值，如果直接將title_trans回傳，有可能發生錯誤
            #所以要先做過濾的動作
            actual = self.get_title()
            for tt in title_trans:
                if tt == actual:
                    title_trans = tt
            return func(self, title_trans, message)
        return proxy

    def show_warning(self, title, full_args):
        language = 'i18n in %s:\n ' %i18n.I18nListener.LOCALE
        test_name = ('Test Name: %s') %BuiltIn().get_variable_value("${TEST NAME}") + '=> Exist multiple translations of the word' + '\n'
        message_for_title = Proxy().deal_warning_message_for_one_word(title, full_args, 'TITLE')
        if message_for_title :
            message = language + test_name + message_for_title + '\n' + 'You should verify translation is correct!'
            logger.warn(message)