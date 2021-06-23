from .Proxy import Proxy
from robot.libraries.BuiltIn import BuiltIn
import sys
from robot.libraries.Screenshot import Screenshot
from robot.api import logger
import I18nListener as i18n
import ManyTranslations as ui

class RemoveFromDictionaryProxy(Proxy):
    def __init__(self, arg_format):
        arg_format[repr(['dictionary', 'keys'])] = self
        #Remove given keys from the dictionary. if key not in it, ignore it.
    def i18n_Proxy(self, func):
        def proxy(self, dictionary, *keys):
            #創出該呼叫的參數紀錄
            full_args = [str(dictionary), str(keys)]

            #翻譯
            #因為dictionary無法直接翻譯，所以拆成keys和values去分別翻譯，回傳值是list
            dict_keys_trans = i18n.I18nListener.MAP.values(list(dictionary.keys()), full_args)
            dict_have_multi_trans  = False
            for dt in dict_keys_trans:
                if len(dt) >1:
                    dict_have_multi_trans  = True

            keys_trans = i18n.I18nListener.MAP.values(keys, full_args)
            keys_have_multi_trans = False
            for lt in keys_trans:
                if len(lt) >1:
                    keys_have_multi_trans = True
                    break
            # logger.warn(keys_have_multi_trans)
            # logger.warn(dict_have_multi_trans)
            
            if keys_have_multi_trans or dict_have_multi_trans:
                RemoveFromDictionaryProxy.show_warning(self, dictionary, keys, full_args) #show warning
                #此case也沒有fail的問題，因為遇到key不在dictionary的話會自動忽略

                # 對預計開啟的UI做一些準備
                i18n.I18nListener.Is_Multi_Trans = True
                
                for i, dt in enumerate(dict_keys_trans):
                    if len(dt)>1 and str(full_args)+list(dictionary.keys())[i] not in ui.UI.unique_log: #FIXME dict keys是否要在這邊判斷
                        multi_trans_word = [list(dictionary.keys())[i]]                                # 還是要移交add_trans_info處理
                        ui.UI.origin_xpaths_or_arguments.append(full_args)
                        ui.UI.add_trans_info(self, multi_trans_word, dt, full_args, func.__name__)
                for i, lt in enumerate(keys_trans):
                        if len(lt) > 1 and str(full_args)+keys[i] not in ui.UI.unique_log:
                            multi_trans_word = [keys[i]]     
                            ui.UI.origin_xpaths_or_arguments.append(full_args)
                            ui.UI.add_trans_info(self, multi_trans_word, lt, full_args, func.__name__) #將翻譯詞加進等等UI會用到的dictionary中
            #將dictionary 翻譯過後的 key 合併 
            # 這邊會出錯，因為key要是唯一值， 暫時用原先的key代替
            # dictionary = dict(zip( list(dictionary.keys()), list(dictionary.values()) ) )         
            #將處理好的翻譯回傳給robot原生keyword
            #FIXME 這邊比較麻煩，之後user選擇key的唯一翻譯後，目前還是只會回傳原本的key值
            # logger.warn(dictionary)
            return func(self, dictionary, *keys)
        return proxy

    def show_warning(self, dictionary, keys, full_args):
        language = 'i18n in %s:\n ' %i18n.I18nListener.LOCALE
        test_name = ('Test Name: %s') %BuiltIn().get_variable_value("${TEST NAME}") + '=> Exist multiple translations of the word' + '\n'
        message_for_dict_keys = Proxy().deal_warning_message_for_list(dictionary.keys(), full_args, 'DICT_KEYS')
        message_for_keys = Proxy().deal_warning_message_for_list(keys, full_args, 'KEYS')
        if message_for_keys != '':
            message = language + test_name + message_for_dict_keys + '\n' + \
            message_for_keys + '\n' + 'You should verify translation is correct!'
            logger.warn(message)