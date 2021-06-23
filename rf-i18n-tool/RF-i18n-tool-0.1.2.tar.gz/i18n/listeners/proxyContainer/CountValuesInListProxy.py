from .Proxy import Proxy
from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.Screenshot import Screenshot
from robot.api import logger
import I18nListener as i18n
import sys
import ManyTranslations as ui

class CountValuesInListProxy(Proxy):
    def __init__(self, arg_format):
        arg_format[repr(['list_', 'value', 'start=0', 'end=None'])] = self
        # 計算list中的指定value之個數
    def i18n_Proxy(self, func):
        def proxy(self, list_, value, start=0, end=None):
            if not list_ or not value:  #檢查機制(可有可無)
                return func(self, list_, value, start, end)
            
            #創出該次呼叫的參數紀錄
            full_args = [str(list_), value] #這邊list要轉str，方便之後資料讀寫

            #翻譯看看
            list_trans = i18n.I18nListener.MAP.values(list_, full_args)
            list_have_multi_trans = False
            for lt in list_trans:
                if len(lt)>1:
                    list_have_multi_trans = True 
                    break
            value_trans = i18n.I18nListener.MAP.value(value, full_args)            

            #遭遇一詞多譯
            if list_have_multi_trans or len(value_trans)>1:
                CountValuesInListProxy.show_warning(self, list_, value, full_args) #show warning
                # 此proxy因為是計算數量，所以沒有case fail的問題
                # 對預計開啟的UI做一些準備
                i18n.I18nListener.Is_Multi_Trans = True  
                
                for i, lt in enumerate(list_trans):
                    if len(lt)>1 and str(full_args)+list_[i] not in ui.UI.unique_log: #FIXME dict keys是否要在這邊判斷
                        multi_trans_word = [list_[i]]                                # 還是要移交add_trans_info處理
                        ui.UI.origin_xpaths_or_arguments.append(full_args)
                        ui.UI.add_trans_info(self, multi_trans_word, lt, full_args, func.__name__)
                if len(value_trans) > 1 and str(full_args)+value not in ui.UI.unique_log:
                    ui.UI.origin_xpaths_or_arguments.append(full_args)
                    multi_trans_word = [value]
                    ui.UI.add_trans_info(self, multi_trans_word, value_trans,full_args, func.__name__)
            #將處理好的翻譯回傳給robot原生keyword
            #為避免畫面上抓取的list[支援], 參數support被翻譯為[支援, 支援服務],
            #不會被count的問題:
            for i, lt in enumerate(list_trans):
                if lt[0] in value_trans:
                    list_trans[i] = value_trans
            return func(self, list_trans, value_trans, start, end)
        return proxy   
    
    def show_warning(self, list_, value, full_args):
        language = 'i18n in %s:\n ' %i18n.I18nListener.LOCALE
        test_name = ('Test Name: %s') %BuiltIn().get_variable_value("${TEST NAME}") + '=> Exist multiple translations of the word' + '\n'
        message_for_list = Proxy().deal_warning_message_for_list(list_, full_args, 'LIST')
        message_for_value = Proxy().deal_warning_message_for_one_word(value, full_args, 'VALUE')
        message = language + test_name + message_for_list + ' '*3 + '\n' + message_for_value + '\n' + 'You should verify translation is correct!' 
        if message_for_list != '' or message_for_value != '':
            logger.warn(message)                        
