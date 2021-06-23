from .Proxy import Proxy
from robot.libraries.BuiltIn import BuiltIn
import sys
from robot.libraries.Screenshot import Screenshot
from robot.api import logger
import I18nListener as i18n
import ManyTranslations as ui

class DictionaryShouldContainItemProxy(Proxy):
    def __init__(self, arg_format):
        arg_format[repr(['dictionary', 'key', 'value', 'msg=None'])] = self
        # Dictionary應該包含Item(key : value)
        # 這邊的 dict key 和 key 都交由內層呼叫 dictionaryshouldcontainkey 再做處理
        # 也就是說: 此proxy只會先做'dict value'和'value'部分的翻譯
        #FIXME 目前USER對於key的翻譯要選擇兩次才會自動選，原因是內層呼叫的full_args不同了
    def i18n_Proxy(self, func):
        def proxy(self, dictionary, key ,value, msg=None):            
            #創出該次呼叫的參數紀錄
            full_args = [str(dictionary), key, value] #將dictionary轉str, 方便之後資料讀寫

            #翻譯
            #因為dictionary無法直接翻譯，所以拆成keys和values去分別翻譯，回傳值是list
            dict_values_trans = i18n.I18nListener.MAP.values(list(dictionary.values()), full_args)            
            dict_have_multi_trans = False 
            for dt in dict_values_trans:
                if len(dt) >1:
                    dict_have_multi_trans  = True
            value_trans = i18n.I18nListener.MAP.value(value, full_args)
            
            #遭遇一詞多譯
            if len(value_trans)>1 or dict_have_multi_trans:
                DictionaryShouldContainItemProxy.show_warning(self, dictionary, value, full_args) #show warning
                #檢查case會pass or fail
                if key in dictionary.keys() and dictionary[key] == value: #pass
                    # 對預計開啟的UI做一些準備
                    i18n.I18nListener.Is_Multi_Trans = True
                    
                    for i, dt in enumerate(dict_values_trans):
                        if len(dt)>1 and str(full_args)+list(dictionary.values())[i] not in ui.UI.unique_log: #FIXME dict keys是否要在這邊判斷
                            multi_trans_word = [list(dictionary.values())[i]]                                # 還是要移交add_trans_info處理
                            ui.UI.origin_xpaths_or_arguments.append(full_args)
                            ui.UI.add_trans_info(self, multi_trans_word, dt, full_args, func.__name__)
                    if len(value_trans) > 1 and str(full_args)+value not in ui.UI.unique_log:
                        multiple_translation_word = [value]     
                        ui.UI.origin_xpaths_or_arguments.append(full_args)
                        ui.UI.add_trans_info(self, multiple_translation_word, value_trans, full_args, func.__name__) #將翻譯詞加進等等UI會用到的dictionary中
            #將dictionary 翻譯過後的key,value合併 
            # 這邊會出錯，因為key要是唯一值， 暫時用原先的key代替
            dictionary = dict(zip(list(dictionary.keys()), dict_values_trans))         
            #將處理好的翻譯回傳給robot原生keyword
            #key的部分不用擔心，因為裡面還會再呼叫一次DictionaryShouldContainKeyProxy，交給後面去處理
            return func(self, dictionary, key, value_trans,msg)
        return proxy

    def show_warning(self, dictionary, value, full_args):
        language = 'i18n in %s:\n ' %i18n.I18nListener.LOCALE
        test_name = ('Test Name: %s') %BuiltIn().get_variable_value("${TEST NAME}") + '=> Exist multiple translations of the word' + '\n'
        message_for_dict_value = Proxy().deal_warning_message_for_list(dictionary.values(),full_args, 'DICT_VALUE')
        message_for_value = Proxy().deal_warning_message_for_one_word(value, full_args,  'VALUE')
        if message_for_dict_value or message_for_value:
            message = language + test_name + message_for_dict_value + '\n' + \
                        message_for_value + '\n' +\
                        'You should verify translation is correct!'
            logger.warn(message)