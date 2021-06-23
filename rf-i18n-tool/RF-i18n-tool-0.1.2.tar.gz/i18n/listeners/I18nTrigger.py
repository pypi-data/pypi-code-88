import SeleniumLibrary
import re
import os
import inspect
import json
import sys
from glob import glob
import SeleniumLibrary
from selenium import webdriver
from robot.libraries.Collections import Collections
from SeleniumLibrary.base import keyword
from robot.libraries.BuiltIn import BuiltIn

class I18nTrigger:

    def __init__(self):
        self.arg_format = {}
        self.new_proxy_instance()
        self.set_proxy_func_to_library_class_func(Collections)
        self.set_proxy_func_to_library_class_func(webdriver.Chrome)
        self.set_proxy_func_to_library_class_func(BuiltIn)
        self.set_proxy_func_to_SeleniumLibrary()

    def get_module_name(self, path):
        file = re.findall('[_A-Za-z]+.py', path)   # file是含有['']的檔名 , file[0]為檔名
        file_name = re.findall('[_A-Za-z]+', file[0]) #filename是將檔名和py分開的串列
        module_name = file_name[0]      #filename[0]是不含.py的檔名
        return module_name

    def get_class_name(self, text):
        m = re.search('class[ A-Za-z]+', text)
        class_define =  m.group(0)   #class_define是class+class名稱
        m = re.findall('[a-zA-Z]+', class_define)
        class_name = m[1] # Fisrst is 'Class' Second is Class name
        return class_name

    def new_proxy_instance(self):
        module_names = []
        class_names = []
        for f in glob('%s\proxyContainer\*.py' % (os.path.dirname(os.path.abspath(__file__)))):
            with open(f, 'r', encoding='UTF-8') as sub_proxy:
                text = sub_proxy.read()     #text是.py檔的檔名+內容
                module_name =  self.get_module_name(sub_proxy.name) #sub_proxy.name是包含路徑的檔名
                if text and module_name != '__init__'and module_name != 'Proxy': # 不處理父類別
                    module_names.append(module_name)   #將檔名append在一起
                    class_names.append(self.get_class_name(text))   #將class名append在一起

        zipped = zip ( module_names , class_names )  #將兩者打包起來
        for arg in zipped:
            inport_text = 'from proxyContainer import %s' %(arg[0]) # from proxyContainer import 模組名
            exec(inport_text) #動態執行
            instance_text = '%s.%s(self.arg_format)' %(arg[0], arg[1]) # x.x(self.arg_format)
            eval(instance_text)  #計算instance_text

    #get proxy
    def get_func_proxy(self, func): #重要!用來判斷該keyword是否有代理keyword存在
        args_declaration = self.get_argument_declaration(func) #得出該func的參數宣告部分
        if repr(args_declaration) in list(self.arg_format.keys()):  #***如果參數宣告在arg_format這個dict的keys中
            return self.arg_format[repr(args_declaration)].i18n_Proxy(func)  #回傳arg_format中value(是proxy的類別名).i18n_Proxy(func)
        return func #否則回傳原本的func屬性值

    def get_argument_declaration(self, func):
        args = inspect.getfullargspec(func).args[1:]  # [0] is self, get出該func的參數部分去掉self
        defaults = inspect.getfullargspec(func).defaults #get出該func參數的default部分
        varargs = inspect.getfullargspec(func).varargs
        keywords = inspect.getargspec(func).keywords
        if defaults:            # 幫args加上default值，如果有的話
            defaults = ['=' + repr(default) for default in defaults]
            defaults = [''] * (len(args) - len(defaults)) + defaults
            args = list(arg[0] + arg[1] for arg in zip(args, defaults))
        if varargs:
            args.append(varargs)
        if keywords:
            args.append(keywords)
        return args

    def set_proxy_func_to_library_class_func(self, library):
        for str_method in dir(library):  # dir(library)是library的全部屬性
            func = getattr(library, str_method) #func是該屬性的屬性值
            if repr(type(func)) == "<class 'function'>":  #如果屬性值是 function
                setattr(library, str_method, self.get_func_proxy(func))

    # provide a surrogate of selenium keywords and functions so that they can test i18n
    ## SeleniumLibrary
    def set_proxy_func_to_SeleniumLibrary(self):
        import SeleniumLibrary
        keywords = [keyword.replace(' ', '_').lower() for keyword in SeleniumLibrary.SeleniumLibrary().keywords] #把seleniumlibrary內的keyword資訊格式化成只顯示其keyword名稱
        for str_keywords_class in dir(SeleniumLibrary): #Seleniumlibrary內的各種class
            keywords_class = getattr(locals().get(SeleniumLibrary.__name__), str_keywords_class) #得出class在seleniumlibrary內的呼叫路徑
            for str_method in dir(keywords_class): #dir(keywords_class)是該class內的各種method
                if str_method.replace(' ', '_').lower() in keywords: #若method名稱出現在keywords list內(和keyword同名)
                    func = getattr(keywords_class, str_method)
                    if repr(type(func)) == "<class 'function'>":#如果屬性值是 function
                        setattr(keywords_class, str_method, keyword(self.get_func_proxy(func)))

I18nTrigger() #import I18nTrigger that it will run this line.