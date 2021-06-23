from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
import I18nListener as i18n
import json
import re
import os
from glob import glob

class I18nMap:

    def __init__(self, translation_file,locale='en-US'):
        self.locale = locale #language
        self.translation_file = translation_file #i18ntranslation dict(在之前已把json格式翻譯檔轉成了python dictionary)
        self.translation_mapping_routes = self.read_translation_mapping_routes() #存入mappingRoutes.json裡面的資料
        self.multiple_translation_words = []
        self.no_need_trans_attirbutes = ["@id", "@class"]

    def read_translation_mapping_routes(self):
        json_path = glob('./mappingRoutes.json')[0]
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f) # json -> python
    
    def is_exist_multiple_translation_words(self, text, full_args):
            # logger.warn(self.value(text, full_args))
            if len(self.value(text, full_args)) > 1 and text not in self.multiple_translation_words: #跑value()，看看翻譯是否多於一種
                # logger.warn("multi_trans word +1~")
                # logger.warn(text)
                self.multiple_translation_words.append(text) 
    
    '''
        new_locate_rule -> key should be the regular expression rule
                           I will use findall to find the word that is needed to translate .
                           so value should be the your match word group position.
    '''
    def locator(self, xpath, full_args, new_locate_rule={}): #會被那些需要翻譯locator的proxy呼叫
        def combine_locate_rule(rule_at, rule_bracket, locate_rule):  
            default_rule = { # 以regular expression制定翻譯規則
                    '(('+ rule_bracket + ')\((text\(\))?\) ?= ?(\'|\")(([0-9a-zA-Z.?&()]| ?)+)(\'|\"))': 4, #這段會get到text()='xxx' 或 normalize-space()='xxx'
                    '(('+ rule_bracket + ')\((text\(\))?\)\ ?, ?(\'|\")(([0-9a-zA-Z.?&()]| ?)+)(\'|\"))': 4, #這段會get到text(), 'xxx' 或 normalize-space(), 'xxx'
                    '(('+ rule_at + ') ?= ?(\'|\")(([0-9a-zA-Z.?&()]| ?)+)(\'|\"))' : 3, #這段會get到@title='xxx'
                    '(('+ rule_at + ') ?, ?(\'|\")(([0-9a-zA-Z.?&()]| ?)+)(\'|\"))' : 3  #這段會get到@title, 'xxx'
                }
            if len(new_locate_rule):
                temp = dict(default_rule.items() + new_locate_rule.items())
                locate_rule = temp
            else:
                locate_rule = default_rule
            return locate_rule

        def find_all_match_word(xpath, locate_rule):  
            all_match_words = {}
            for rule in locate_rule.keys():
                matches = re.findall(rule, xpath)
                all_match_words[rule] = matches # ex: all_match_words={ rule1://*[text()='test'], ...}
            return all_match_words
        #start
        self.multiple_translation_words = []    
        if not isinstance(xpath, str): #測看看xpath是不是string
            return [xpath]
        translated_xpath = [xpath]

        #   利用"負面表列法"改善翻譯邏輯，
        #   不再只根據rule去抓xpath，而是"沒有在no_need_trans_attirbutes"中
        #   的attributes都代表"可能要翻譯的屬性"，需要去檢查

        # 透過一一檢查xpath中的每個attribute，來制定新的翻譯規則
        rule_for_filter = {   #用來過濾出attribute的rule
            "(@[a-z-]*)":"@",
            "([a-z-]*\(\))":"()"
        }
        rule_for_insert_at = ""
        rule_for_insert_bracket = ""
        all_match_attributes = find_all_match_word(xpath, rule_for_filter) #挑出xpath中所有的可能被翻譯attribute
        for rule, matches in all_match_attributes.items():
            for match in matches:
                c = 0
                if match not in self.no_need_trans_attirbutes:
                    if rule_for_filter[rule] == "@":
                        rule_for_insert_at += "|" + match if c!=0 else match
                        c+=1
                    elif rule_for_filter[rule] == "()":
                        match = match.strip("()")
                        rule_for_insert_bracket += "|" + match if c!=0 else match
                        c+=1
        # 把要插入的rule代入，和default的rule結合，創造出一套新的locate_rule
        locate_rule = combine_locate_rule(rule_for_insert_at, rule_for_insert_bracket, new_locate_rule) 
        # 之後再沿用以前的方法去把xpath內需要翻譯的部分做翻譯
        
        # 下面這行會利用rule去實際得 找出符合規則的xpath段落
        all_match_words = find_all_match_word(xpath, locate_rule) #將xpath和rule傳入找所有符合字詞
        # logger.warn(all_match_words)
        for rule, matches in all_match_words.items(): #all_match_words是dict, rule是key, matches是value 
            # logger.warn(matches)
            for match in matches: # 同種rule查找到的match可能不只一筆 ex: text()='xxx' & text()='yyy'
                match_group = locate_rule[rule] #拿到rule的編號
                quot_group = match_group - 1 
                # logger.warn(match)
                # logger.warn(match[match_group])
                self.is_exist_multiple_translation_words(match[match_group], full_args) #檢驗是否有一個以上翻譯
                # match[match_group]是可以被翻譯的word
                #以下實際將xpath翻譯,
                #FIXME 此處translated_xpath會被覆蓋??
                translated_xpath = self.translate(full_args, match=match[match_group], quot=match[quot_group], 
                xpaths=translated_xpath) # group 0 as self, group 4 as match, group 3 as quot 
        if xpath != list(translated_xpath)[0] : # 表示有成功被翻譯(不管個數)，所以長的不一樣了
            self.log_translation_info(xpath, translated_xpath)
        return translated_xpath
    
    def log_translation_info(self, xpath, translated_xpath):
        def is_need_to_show_warning():
            for multiple_translation_word in self.multiple_translation_words:
                if multiple_translation_word in i18n.I18nListener.Not_SHOW_WARNING_WORDS: #circular include 問題
                    return False
            return True   
        
        def deal_translated_xpath_info(translated_xpath):
            translated_xpath_info = ''
            for i,temp_xpath in enumerate(translated_xpath):
                temp = str(i+1) + '. ' + temp_xpath + '\n   '
                translated_xpath_info = translated_xpath_info + temp
            message = 'Detail Information\ni18n in %s :\nOriginal Locator:\n   1. %s\nTranslated Locator:\n   %s' % (self.locale, xpath, translated_xpath_info)
            return message
        
        warning_or_not = is_need_to_show_warning()
        message = deal_translated_xpath_info(translated_xpath)
        if warning_or_not == False:
            words = ', '.join(self.multiple_translation_words)
            message = message + '\nYou had resolved the multiple translations of the word: \'%s\'' %(words)
        logger.info(message)

    def get_multiple_translation_words(self):
        return self.multiple_translation_words

     # Our target is "XXX" if without quot that it will translate the wrong target.
    def translate(self,full_args, match, quot, xpaths):
        origin = quot + match + quot
        translate_list = []
        for translation in self.value(match, full_args):
            value = quot + translation + quot
            for xpath in xpaths:
                translate_list.append(xpath.replace(origin, value))
        return list(set(translate_list))    #最後會把所有可能的翻譯後xpath(s)都裝進list回傳

    #For list should be equal, set should be equal...
    def values(self, values, full_args):
        return [self.value(v, full_args) for v in values]

    def value(self, value, full_args):
        try:
            result = self.get_possible_translation(value, full_args)
            # logger.warn(result)
        except (KeyError):
            return [value]
        return list(set(result))

    def get_possible_translation(self, value, full_args):
        # 先查看setting是否有value的設定檔，若有則以設定檔為主，否則執行翻譯
        #FIXME 此處要加上判斷，看是否能透過對照'腳本名稱'& '該keyword的所有參數'，來判斷是否取用設定檔的翻譯
        result = []
        for i in range(len(i18n.I18nListener.SETTING_KEYS)):
            if i18n.I18nListener.SETTING_KEYS[i] == value and i18n.I18nListener.SETTING_ARGS[i] == full_args:
                result.append(i18n.I18nListener.SETTING_TRANS[i])
                # logger.warn(result)
                break
        if result:    
            return result
        else:
            try:
                for mapping_route in self.translation_mapping_routes[value]:   #用value當key抓出translation_mapping_routes裡的特定values
                    result.append(eval("self.translation_file%s" % mapping_route))
            except (KeyError):
                raise KeyError
            return result