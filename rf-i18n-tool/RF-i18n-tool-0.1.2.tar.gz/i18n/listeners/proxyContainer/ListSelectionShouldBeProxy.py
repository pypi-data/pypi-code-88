from .Proxy import Proxy
from robot.libraries.BuiltIn import BuiltIn
import sys
from robot.libraries.Screenshot import Screenshot
from robot.api import logger
import I18nListener as i18n
import ManyTranslations as ui
from SeleniumLibrary.keywords.selectelement import SelectElementKeywords

class ListSelectionShouldBeProxy(Proxy):
    def __init__(self, arg_format):
        arg_format[repr(['locator', 'expected'])] = self
        # 驗證 selection list `locator` 的 expected選項有被選擇起來
        # selection list 在網頁中: <select>

    def i18n_Proxy(self, func):
        def proxy(self, locator, *expected):
            # logger.warn(type(locator))
            #創出該呼叫的參數紀錄
            full_args = [locator, str(expected)] #expected型別是tuple，轉成str方便之後讀寫

            BuiltIn().import_library('SeleniumLibrary')
            #翻譯， 會翻譯xpath內有需要被翻譯的屬性(邏輯定義在i18nMap)，翻譯完需要屬性後會回傳整條xpath，
            #並會設定multiple_translation_words，讓下一行get_multiple_translation_words()取用
            locator_trans = i18n.I18nListener.MAP.locator(BuiltIn().replace_variables(locator), full_args)
            # logger.warn(locator_trans)
            multiple_translation_words = i18n.I18nListener.MAP.get_multiple_translation_words()
            words_trans = i18n.I18nListener.MAP.values(multiple_translation_words, full_args)

            expected_trans = i18n.I18nListener.MAP.values(expected, full_args)
            # logger.warn(expected)
            # logger.warn(expected_trans)
            expected_have_multi_trans = False
            for lt in expected_trans:
                if len(lt) >1:
                    expected_have_multi_trans = True
                    break
            
            xpath = ""
            #遭遇一詞多譯
            if len(locator_trans)>1 or expected_have_multi_trans:
                ListSelectionShouldBeProxy.show_warning(self, multiple_translation_words,expected, full_args) #show warning
                #對翻譯過後可能的多種xpath做串接
                for i, lt in enumerate(locator_trans):
                    xpath += '|' + lt.replace('xpath', '') if i!=0 else lt.replace('xpath', '')
                #判斷case會過還是fail (使用原生library)
                options = SelectElementKeywords._get_selected_options(self, locator)
                labels = SelectElementKeywords._get_labels(self, options)
                is_pass = False
                for lt in expected_trans:
                    for single_tran in lt:
                        if single_tran in labels:
                            is_pass = True
                            break
                
                if is_pass: # pass
                    # 對預計開啟的UI做一些準備
                    i18n.I18nListener.Is_Multi_Trans = True
                    
                    for i, word_trans in enumerate(words_trans):
                        if len(word_trans)>1 and str(full_args)+multiple_translation_words[i] not in ui.UI.unique_log:
                            multi_trans_word = [multiple_translation_words[i]]              
                            ui.UI.origin_xpaths_or_arguments.append(full_args)                  
                            ui.UI.add_trans_info(self, multi_trans_word, word_trans, full_args, func.__name__)
                    for i, lt in enumerate(expected_trans):
                        if len(lt) > 1 and str(full_args)+expected[i] not in ui.UI.unique_log:
                            multi_trans_word = [expected[i]]     
                            ui.UI.origin_xpaths_or_arguments.append(full_args)
                            ui.UI.add_trans_info(self, multi_trans_word, lt, full_args, func.__name__) #將翻譯詞加進等等UI會用到的dictionary中
            else: #沒有一詞多譯
                xpath = locator_trans[0]
            #將處理好的翻譯回傳給robot原生keyword
            #這邊expected是tuple可以用'*' unpack argument，但expected_trans內部item還是list
            #為了下面回傳時好處理，此處必須把list包list的一詞多譯壓縮成一個string
            
            # 若有翻譯會使case過，則用其置換labels_trans中的翻譯 #FIXME 可優化
            all_options = SelectElementKeywords._get_options(self, locator)
            all_labels = SelectElementKeywords._get_labels(self, all_options)
            for i, lt in enumerate(expected_trans): 
                    for single_tran in lt:
                        if single_tran in all_labels:
                            expected_trans[i] = single_tran
                            break

            return func(self, BuiltIn().replace_variables(xpath), *tuple(expected_trans))
        return proxy

    def show_warning(self, multi_trans_words, expected, full_args):
        language = 'i18n in %s:\n ' %i18n.I18nListener.LOCALE
        test_name = ('Test Name: %s') %BuiltIn().get_variable_value("${TEST NAME}") + '=> Exist multiple translations of the word' + '\n'
        message_for_words = Proxy().deal_warning_message_for_list(multi_trans_words,full_args, 'MULTI_TRANS_WORDS')
        message_for_expected = Proxy().deal_warning_message_for_list(expected,full_args, 'EXPECTED')
        if message_for_words or message_for_expected:
            message = language + test_name + message_for_words + '\n' + \
                message_for_expected + '\n' +'You should verify translation is correct!'
            logger.warn(message)