from .Proxy import Proxy
from robot.libraries.BuiltIn import BuiltIn
import sys
from robot.libraries.Screenshot import Screenshot
from robot.api import logger
import I18nListener as i18n
import ManyTranslations as ui

class GetMatchCountProxy(Proxy):
    def __init__(self, arg_format):
        arg_format[repr(['list', 'pattern', 'case_insensitive=False', 'whitespace_insensitive=False'])] = self
        # 會回傳list中符合pattern的個數，支援regular expression的方式
        # GetMatchCount是個比較特殊的情況，因為'a*'這種pattern不好去翻譯，
        # 但是如果不做處理的話，以原先的腳本去跑新的多國語言網頁，可能導致錯誤(ex畫面上get到的list是中文)
        # 所以目前的想法是必須 list 和 pattern 的語言要相同(缺陷)
        # FIXME 若遇到list, pattern語言不相同的情形，則可能要有偵測語言機制(不好做)

        #目前應急的做法，是假設兩者語言相同，在報表呈現現在list中的item是被翻譯成什麼
    def i18n_Proxy(self, func):
        def proxy(self, list, pattern, case_insensitive=False, whitespace_insensitive=False):
            if not list or not pattern: # 檢查機制，目前可有可無
                return func(self, list, pattern, case_insensitive, whitespace_insensitive)
            
            #創出該次呼叫的參數紀錄
            full_args = [str(list), pattern] #將list轉str, 方便之後資料讀寫

            #翻譯
            list_trans = i18n.I18nListener.MAP.values(list, full_args)
            list_have_multi_trans = False
            for lt in list_trans:
                if len(lt) >1:
                    list_have_multi_trans = True
                    break
                
            #遭遇一詞多譯
            #此proxy同樣也沒有fail的問題，頂多get出錯誤的值
            if list_have_multi_trans: 
                # 這邊因為內層會呼叫get matches，而get matches也會呼叫此proxy，
                # 所以為了不讓warning show 兩次，條件只讓 get matches去show warning
                if 'matches' in func.__name__:
                    GetMatchCountProxy.show_warning(self, list,full_args) #show warning
                i18n.I18nListener.Is_Multi_Trans = True
                
                for i, lt in enumerate(list_trans):
                    if len(lt)>1 and str(full_args)+list[i] not in ui.UI.unique_log: #FIXME dict keys是否要在這邊判斷
                        multi_trans_word = [list[i]]                                # 還是要移交add_trans_info處理
                        ui.UI.origin_xpaths_or_arguments.append(full_args)
                        ui.UI.add_trans_info(self, multi_trans_word, lt, full_args, func.__name__)
            
            #此處不將翻譯過後的詞回傳，因為可能導致get不到正確的數量
            #僅在報表上會顯示list中會有一詞多譯warning的詞，並跳UI
            return func(self, list, pattern, case_insensitive, whitespace_insensitive)
        return proxy

    def show_warning(self, list, full_args):
        language = 'i18n in %s:\n ' %i18n.I18nListener.LOCALE
        test_name = ('Test Name: %s') %BuiltIn().get_variable_value("${TEST NAME}") + '=> Exist multiple translations of the word' + '\n'
        message_for_list = Proxy().deal_warning_message_for_list(list, full_args, 'LIST')
        if message_for_list :
            message = language + test_name + message_for_list + '\n' + 'You should verify translation is correct!'
            logger.warn(message)