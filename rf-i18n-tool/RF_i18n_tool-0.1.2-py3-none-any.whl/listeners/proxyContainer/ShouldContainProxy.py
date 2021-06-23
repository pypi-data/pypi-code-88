from .Proxy import Proxy
from robot.libraries.BuiltIn import BuiltIn
import sys
from robot.libraries.Screenshot import Screenshot
from robot.api import logger
import I18nListener as i18n
import ManyTranslations as ui
from robot.utils import is_string, is_list_like

class ShouldContainProxy(Proxy):   #container要包含item才算pass
    def __init__(self, arg_format):
        arg_format[repr(['container', 'item', 'msg=None', 'values=True', 'ignore_case=False'])] = self
                        # container:可能是string或list,  item:通常是string
                        # ShouldNotContain也會呼叫此keyword
    def i18n_Proxy(self, func):
        def proxy(self, container, item, msg=None, values=True, ignore_case=False):
            #創出該呼叫的參數紀錄
            full_args = [str(container), item] #container有機會是list，轉str，方便之後資料讀寫
            # logger.warn(container)

            #翻譯
            container_trans = i18n.I18nListener.MAP.values(container, full_args)
            item_trans = i18n.I18nListener.MAP.value(item, full_args)
            # logger.warn(item_trans)
            # logger.warn(container_trans)

            container_have_multi_trans = False
            if is_list_like(container):
                for lt in container_trans:
                    if len(lt) >1:
                        container_have_multi_trans  = True
                        break 
            elif is_string(container):
                if len(container_trans)>1:
                    container_have_multi_trans = True

            #遭遇一詞多譯
            if container_have_multi_trans or len(item_trans)>1:
                ShouldContainProxy.show_warning(self, container, item, full_args) #show warning
                #檢查case會pass or fail
                #FIXME 因為container有可能是抓畫面上翻譯過網頁的值，所以這邊的判斷
                #      要考慮container和item不是同語言的情形
                is_pass = False
                if 'not' in func.__name__ :
                    if is_string(container):
                        container = container.lower()
                        if item not in container and (index not in container for index in item_trans):
                            is_pass=True
                    elif is_list_like(container):
                        # 若不同語言的情況下，item不在container內，有可能同語言下卻會包含
                        # 所以要考慮item和item_trans，皆不在container中
                        if item not in container and (index not in container for index in item_trans):
                            is_pass = True
                else:
                    if is_string(container):
                        container = container.lower()
                        if item in container or (index in container for index in item_trans):
                            is_pass = True
                    elif is_list_like(container):
                        if item in container or (index in container for index in item_trans):
                            is_pass = True

                if is_pass: #pass
                    # 對預計開啟的UI做一些準備
                    i18n.I18nListener.Is_Multi_Trans = True

                    if is_list_like(container):
                        for i, lt in enumerate(container_trans):
                            # logger.warn(container)
                            # logger.warn(container[i])
                            if len(lt)>1 and str(full_args)+container[i] not in ui.UI.unique_log: #FIXME dict keys是否要在這邊判斷
                                multi_trans_word = [container[i]]                            # 還是要移交add_trans_info處理
                                ui.UI.origin_xpaths_or_arguments.append(full_args)
                                ui.UI.add_trans_info(self, multi_trans_word, lt, full_args, func.__name__)
                    elif is_string(container):
                        if len(container_trans)>1 and str(full_args)+container not in ui.UI.unique_log:
                            multiple_translation_word = [container]     
                            ui.UI.origin_xpaths_or_arguments.append(full_args)
                            ui.UI.add_trans_info(self, multiple_translation_word, container_trans, full_args, func.__name__) #將翻譯詞加進等等UI會用到的dictionary中
                    if len(item_trans)>1 and str(full_args)+item not in ui.UI.unique_log:
                        multiple_translation_word = [item]     
                        ui.UI.origin_xpaths_or_arguments.append(full_args)
                        ui.UI.add_trans_info(self, multiple_translation_word, item_trans, full_args, func.__name__) #將翻譯詞加進等等UI會用到的dictionary中

            #將處理好的翻譯回傳給robot原生keyword
            #  原本預期會pass,因為有可能container是抓畫面上翻譯過網頁的值，
            #  所以item_trans在一詞多譯的情況下，可能不會包含於container內，
            #  而導致case出錯，目前是打算在proxy先測試過再做回傳
            if 'not' not in func.__name__ :
                if is_list_like(item_trans):
                    for it in item_trans: #把item_trans一詞多譯換成會過的那個
                        if [it] in container_trans:
                            item_trans = [it]
                            break
            #FIXME should not contain還未定義，未來有機率出錯
            return func(self, container_trans, item_trans, msg)
        return proxy                        
    
    def show_warning(self, container, item, full_args):
        language = 'i18n in %s:\n ' %i18n.I18nListener.LOCALE
        test_name = ('Test Name: %s') %BuiltIn().get_variable_value("${TEST NAME}") + '=> Exist multiple translations of the word' + '\n'
        message_for_container = Proxy().deal_warning_message_for_list(container, full_args, 'CONTAINER')
        message_for_item = Proxy().deal_warning_message_for_one_word(item, full_args, 'Expected Contain')
        if message_for_container or message_for_item :
            message = language + test_name + message_for_container + '\n' +  message_for_item + '\n' + 'You should verify translation is correct!'
            logger.warn(message)