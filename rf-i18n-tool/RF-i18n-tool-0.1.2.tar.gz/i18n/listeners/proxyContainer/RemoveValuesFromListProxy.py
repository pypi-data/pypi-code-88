from .Proxy import Proxy
from robot.libraries.BuiltIn import BuiltIn
import sys
from robot.libraries.Screenshot import Screenshot
from robot.api import logger
import I18nListener as i18n
import ManyTranslations as ui

class RemoveValuesFromListProxy(Proxy):
    def __init__(self, arg_format):
        arg_format[repr(['list_', 'values'])] = self
        # 移除list中符合values的值 ，若values不存在list中，忽略
    def i18n_Proxy(self, func):
        def proxy(self, list_, *values):
            #創出該呼叫的參數紀錄
            full_args = [str(list_), str(values)]            

            #翻譯
            list_trans = i18n.I18nListener.MAP.values(list_, full_args)
            list_have_multi_trans  = False
            for lt in list_trans:
                if len(lt) >1:
                    list_have_multi_trans  = True

            values_trans = i18n.I18nListener.MAP.values(values, full_args)
            values_have_multi_trans = False
            for lt in values_trans:
                if len(lt) >1:
                    values_have_multi_trans = True
                    break
            
            if list_have_multi_trans or values_have_multi_trans:
                RemoveValuesFromListProxy.show_warning(self, list_, values, full_args) #show warning
                #此case也沒有fail的問題，因為遇到value不在list的話會自動忽略

                # 對預計開啟的UI做一些準備
                i18n.I18nListener.Is_Multi_Trans = True
                
                for i, lt in enumerate(list_trans):
                    if len(lt)>1 and str(full_args)+list_[i] not in ui.UI.unique_log: #FIXME dict keys是否要在這邊判斷
                        multi_trans_word = [list_[i]]                                # 還是要移交add_trans_info處理
                        ui.UI.origin_xpaths_or_arguments.append(full_args)
                        ui.UI.add_trans_info(self, multi_trans_word, lt, full_args, func.__name__)
                for i, lt in enumerate(values_trans):
                        if len(lt) > 1 and str(full_args)+values[i] not in ui.UI.unique_log:
                            multi_trans_word = [values[i]]     
                            ui.UI.origin_xpaths_or_arguments.append(full_args)
                            ui.UI.add_trans_info(self, multi_trans_word, lt, full_args, func.__name__) #將翻譯詞加進等等UI會用到的dictionary中
            #將處理好的翻譯回傳給robot原生keyword
            #參考listSelectionShouldBeProxy
            # 將'list_的翻譯值' 賦予給 '原本的list_'，
            # 否則之後並不會實際刪除list內的values
            # 並且將list包list格式化成只有一層list
            
            # 將翻譯後的list_整理成只有唯一翻譯
            for i,lt in enumerate(list_trans):
                list_[i] = lt[0]
            
            #若value_trans中有翻譯在list_中，則將value_trans[i]設為此值，以利回傳
            for i,vt in enumerate(values_trans):
                for j in range(len(vt)):
                    if vt[j] in list_:
                        values_trans[i] = vt[j]
                        break;
            
            return func(self, list_, *tuple(values_trans))
        return proxy

    def show_warning(self, list_, values, full_args):
        language = 'i18n in %s:\n ' %i18n.I18nListener.LOCALE
        test_name = ('Test Name: %s') %BuiltIn().get_variable_value("${TEST NAME}") + '=> Exist multiple translations of the word' + '\n'
        message_for_list = Proxy().deal_warning_message_for_list(list_, full_args, 'LIST')
        message_for_values = Proxy().deal_warning_message_for_list(values, full_args, 'VALUES')
        if message_for_list or message_for_values:
            message = language + test_name + message_for_list + '\n' + \
            message_for_values + '\n' + 'You should verify translation is correct!'
            logger.warn(message)