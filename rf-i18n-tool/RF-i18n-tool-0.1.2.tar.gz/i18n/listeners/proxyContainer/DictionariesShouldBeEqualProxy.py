from .Proxy import Proxy
from robot.libraries.BuiltIn import BuiltIn
import sys
from robot.libraries.Screenshot import Screenshot
from robot.api import logger
import I18nListener as i18n
import ManyTranslations as ui
from robot.libraries.Collections import _Dictionary

class DictionariesShouldBeEqualProxy(Proxy):
    def __init__(self, arg_format):
        arg_format[repr(['dict1', 'dict2', 'msg=None', 'values=True'])] = self
        # DictionariesShouldBeEqual 和 DictionaryShouldContainSubDictionary 都會呼叫此proxy
    def i18n_Proxy(self, func):
        def proxy(self, dict1, dict2, msg=None, values=True):
            #定義'比較'的邏輯
            compare = lambda x,y:True if x == y else False
            #創出該次呼叫的參數紀錄
            full_args = [str(dict1), str(dict2)] #將dictionary轉str, 方便之後資料讀寫

            #翻譯
            #因為dictionary無法直接翻譯，所以拆成keys和values去分別翻譯，回傳值是list
            dict1_keys_trans = i18n.I18nListener.MAP.values(list(dict1.keys()), full_args)
            dict1_values_trans = i18n.I18nListener.MAP.values(list(dict1.values()), full_args)
            dict2_keys_trans = i18n.I18nListener.MAP.values(list(dict2.keys()), full_args)
            dict2_values_trans = i18n.I18nListener.MAP.values(list(dict2.values()), full_args)
            whole_trans = []  # 將所有翻譯結果放在一起，用來判斷是否有包含一詞多譯
            whole_trans.append(dict1_keys_trans)
            whole_trans.append(dict1_values_trans)
            whole_trans.append(dict2_keys_trans)
            whole_trans.append(dict2_values_trans)
            dict_have_multi_trans = False
            for i in range(4):
                for dt in whole_trans[i]: 
                    # logger.warn(dt)
                    if len(dt)>1:
                        dict_have_multi_trans = True 
                        break

            #FIXME
            new_dict1 = {}
            new_dict2 = {}
            new_dict2=dict(zip(list(dict2.keys()), dict2_values_trans))

            #遭遇一詞多譯
            if dict_have_multi_trans:
                DictionariesShouldBeEqualProxy.show_warning(self, dict1, dict2, full_args) #show warning
                #檢查case會pass or fail(使用原生library的function)
                if 'contain_sub' in func.__name__: #呼叫此proxy的是DictionaryShouldContainSubDictionary
                    keys = self.get_dictionary_keys(dict2)
                    contain_key = True  
                    for k in keys:
                        if k not in dict1:
                            contain_key = False
                            break
                    if contain_key and not list(_Dictionary._yield_dict_diffs(self, keys, dict1, dict2)):
                        diffs = False
                    else:
                        diffs = True
                elif 'equal' in func.__name__: #呼叫此proxy的是DictionaryShouldBeEqual
                    try:
                        keys = _Dictionary._keys_should_be_equal(self, dict1, dict2, msg, values)
                        diffs = list(_Dictionary._yield_dict_diffs(self, keys, dict1, dict2))
                        for k in keys:
                            if dict1[k] in dict2_values_trans[0]:
                                diffs = False
                    except:
                    # 為了避免{['軟體']:['支援']}、{['軟體']:['支援', '支援服務']}
                    # 被系統判定為不相等的情形: #FIXME
                        for dict1_key in dict1.keys():
                            for dict2_key in new_dict2.keys():
                                if [dict1_key] in dict2_keys_trans and dict1[dict1_key] in new_dict2[dict2_key][0]:
                                    new_dict1[dict2_key] = new_dict2[dict2_key]
                                    diffs = False 
                                else:
                                    diffs = True
                                    break
                if not diffs:  # pass
                    # 對預計開啟的UI做一些準備
                    # logger.warn("有一詞多譯，並且pass")
                    i18n.I18nListener.Is_Multi_Trans = True

                    for i, dt in enumerate(dict1_keys_trans):
                        if len(dt)>1 and str(full_args)+list(dict1.keys())[i] not in ui.UI.unique_log: #FIXME dict keys是否要在這邊判斷
                            ui.UI.origin_xpaths_or_arguments.append(full_args)
                            multi_trans_word = [list(dict1.keys())[i]]                                # 還是要移交add_trans_info處理
                            ui.UI.add_trans_info(self, multi_trans_word, dt, full_args, func.__name__)
                    for i, dt in enumerate(dict1_values_trans):
                        if len(dt)>1 and str(full_args)+list(dict1.values())[i] not in ui.UI.unique_log: #FIXME dict keys是否要在這邊判斷
                            ui.UI.origin_xpaths_or_arguments.append(full_args)
                            multi_trans_word = [list(dict1.values())[i]]                                # 還是要移交add_trans_info處理
                            ui.UI.add_trans_info(self, multi_trans_word, dt, full_args, func.__name__)                    
                    for i, dt in enumerate(dict2_keys_trans):
                        if len(dt)>1 and str(full_args)+list(dict2.keys())[i] not in ui.UI.unique_log: #FIXME dict keys是否要在這邊判斷
                            ui.UI.origin_xpaths_or_arguments.append(full_args)
                            multi_trans_word = [list(dict2.keys())[i]]                                # 還是要移交add_trans_info處理
                            ui.UI.add_trans_info(self, multi_trans_word, dt, full_args, func.__name__)                    
                    for i, dt in enumerate(dict2_values_trans):
                        if len(dt)>1 and str(full_args)+list(dict2.values())[i] not in ui.UI.unique_log: #FIXME dict keys是否要在這邊判斷
                            ui.UI.origin_xpaths_or_arguments.append(full_args)
                            multi_trans_word = [list(dict2.values())[i]]                                # 還是要移交add_trans_info處理
                            ui.UI.add_trans_info(self, multi_trans_word, dt, full_args, func.__name__)  
            #以下不管(pass, fail) (有無一詞多譯)都要做 
            #將dict1、dict2的 翻譯過後的key,value合併 
            # 這邊會出錯，因為key要是唯一值， 暫時用原先的key代替
            dict1 = dict(zip(list(dict1.keys()), dict1_values_trans)) 
            dict2 = dict(zip(list(dict2.keys()), dict2_values_trans))
            #將處理好的翻譯回傳給robot原生keyword
            
            #FIXME
            for dict1_key in dict1.keys():
                for dict2_key in dict2.keys():
                    if [dict1_key] in dict2_keys_trans and dict1[dict1_key]== dict2[dict2_key]:
                        dict1.pop(dict1_key, None)
                        dict1[dict2_key] = dict2[dict2_key]
                        return func(self, dict1, dict2)
                    elif dict1_key== dict2_key and dict1[dict1_key][0] in dict2[dict2_key]:
                        dict1[dict1_key] = dict2[dict2_key] 
            if new_dict1:
                return func(self, new_dict1, new_dict2, msg, values)     
                
            else:           
                return func(self, dict1, dict2, msg, values)                              
        return proxy

    def show_warning(self, dict1, dict2, full_args):
        language = 'i18n in %s:\n ' %i18n.I18nListener.LOCALE
        test_name = ('Test Name: %s') %BuiltIn().get_variable_value("${TEST NAME}") + '=> Exist multiple translations of the word' + '\n'
        message_for_dict1_key = Proxy().deal_warning_message_for_list(dict1.keys(), full_args, 'Dict1KEY')
        message_for_dict1_value = Proxy().deal_warning_message_for_list(dict1.values(), full_args, 'Dict1VALUE')
        message_for_dict2_key = Proxy().deal_warning_message_for_list(dict2.keys(), full_args, 'Dict2KEY')
        message_for_dict2_value = Proxy().deal_warning_message_for_list(dict2.values(), full_args, 'Dict2VALUE')
        message = language + test_name + message_for_dict1_key + '\n' + message_for_dict1_value + '\n' \
        + message_for_dict2_key + '\n' + message_for_dict2_value + '\n' + 'You should verify translation is correct!'
        if message_for_dict1_key or message_for_dict1_value or message_for_dict2_key or message_for_dict2_value:
            logger.warn(message)