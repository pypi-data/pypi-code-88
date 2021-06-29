import re
from robot304.parsing.model import ForLoop, Step, Variable
from robot304.parsing.settings import Arguments, Setting, _Import
"""
This func is used to search the variable name from a given string.
variableName: string of variable name.
targetStr: the target string to be search.
return: the search result.
"""
def get_variable_match_result(variableName, targetStr):
    return re.findall(r"[\$\@\&]\{%s(?:\[[\S]*\])?\}" %variableName[2:-1], targetStr, flags=re.IGNORECASE)
"""
This func is used to search keyword name from a given string.
keywordName: string of keyword name.
targetStr: the target string to be search.
return: whether the targetStr is keyword.
"""
def is_keyword_match(keywordName, targetStr):
    return keywordName.lower() == targetStr.lower()
"""
This func is used to get the replace method.
replaceKind: kind of replace method which is variable or keyword.
"""
def get_replace_str_method(replaceKind):
    """
    This func is used to get the replace keyword result of a given string.
    targetStr: the origin string.
    old: the string need to be replaced.
    new: the new string to replace.
    return: the targetStr after replacing old to new.
    """
    def get_keyword_replace_str(targetStr, old, new):
        return targetStr.replace(old, new) if is_keyword_match(old, targetStr) else targetStr
    """
    This func is used to get the replace variable result of a given string.
    targetStr: the origin string.
    old: the string need to be replaced.
    new: the new string to replace.
    return: the targetStr after replacing old to new.
    """
    def get_variable_replace_str(targetStr, old, new):
        match_result = get_variable_match_result(old, targetStr)
        replace_result =  targetStr
        for matchStr in match_result:
            #get the '[' index in variable reference.
            var_name_end_index = matchStr.find('[')
            #get the variable name without symbol.EX:${test}=>test.
            var_name_target = matchStr[matchStr.find("{")+1:var_name_end_index if var_name_end_index!=-1 else matchStr.find("}")]
            #replace the name with the new one in variable.EX:${test}=>${newName}
            replace_str = matchStr.replace(var_name_target, new, 1)
            #replace the whole variable in targetStr.EX:Log    ${test}=>Log    ${newName}
            replace_result = replace_result.replace(matchStr, replace_str, 1)
        return replace_result
    return {'variable':get_variable_replace_str, 'keyword':get_keyword_replace_str}[replaceKind]

"""
This func is used to wrapped the 'get_replace_str_method'.
"""
def get_variable_replace_str(targetStr, old, new):
    return get_replace_str_method('variable')(targetStr, old, new)

"""
This func is used to get the present func of `setting` object.
"""
def get_setting_object_present_method():
    def func(setting):
        present_str = ""
        for data in setting.as_list():
            present_str+=data+"    "
        return present_str.strip()
    return func
"""
This func is used to get the present func of `step` object.
"""
def get_step_object_present_method():
    def func(step):
        present_str = ""
        for data in step.as_list():
            present_str+=data+"    "
        return present_str.strip()
    return func
"""
This func is used to get the present func of `forLoop` object.
"""
def get_for_loop_object_present_method():
    def get_for_loop_str(forLoop):
        step_present_method = get_step_object_present_method()
        present_str = ""
        for data in forLoop.as_list():
            present_str+=data+"    "
        present_str = present_str.strip()
        for step in forLoop:
            present_str+="\n\\    "+step_present_method(step)
        return present_str
    return get_for_loop_str    
"""
This func is used to get the present func of `variable` object.
"""
def get_variable_object_present_method():
    def func(variable):
        present_str = ""
        for data in variable.as_list():
            present_str+=data+"    "
        return present_str.strip()
    return func
"""
This func is used to get the present func of `keyword` object.
"""
def get_keyword_object_present_method():
    def func(keyword):
        return keyword.name
    return func
"""
This func is used to get the replace func of `setting` object.
"""
def get_setting_object_replace_method(replaceKind):
    get_replace_str = get_replace_str_method(replaceKind)
    def replace_setting(setting, old, new):
        datas_after_replace = [get_replace_str(item, old, new) for item in setting.as_list()]
        setting._set_initial_value()
        setting._populate(datas_after_replace[1:])
    return replace_setting
"""
This func is used to get the replace func of `import` object.
"""
def get_import_object_replace_method(replaceKind):
    get_replace_str = get_replace_str_method(replaceKind)
    def replace_import(_import, old, new):
        _import.name = get_replace_str(_import.name, old, new)
        for index, arg in enumerate(_import.args):
            _import.args[index] = get_replace_str(arg, old, new)
    return replace_import
"""
This func is used to get the replace func of `step` object.
"""
def get_step_object_replace_method(replaceKind):
    get_replace_str = get_replace_str_method(replaceKind)
    def replace_variable(step, old, new):
        datas_after_replace = [get_replace_str(item, old, new) for item in step.as_list()]
        step.__init__(datas_after_replace)
    return replace_variable
"""
This func is used to get the replace func of `forLoop` object.
"""
def get_for_loop_object_replace_method(replaceKind):
    replace_method = get_step_object_replace_method(replaceKind)
    def replace_variable(forLoop, old, new):
        for index, item in enumerate(forLoop.items):
            forLoop.items[index] = get_variable_replace_str(item, old, new)
        for step in forLoop:
            replace_method(step, old, new)
    def replace_keyword(forLoop, old, new):
        for step in forLoop:
            replace_method(step, old, new)
    return {'variable':replace_variable, 'keyword':replace_keyword}[replaceKind]
"""
This func is used to get the replace func of `variable` object.
"""
def get_variable_object_replace_method():
    def func(variable, old, new):
        variable.name = get_variable_replace_str(variable.name, old, new)
        for index, value in enumerate(variable.value):
            variable.value[index] = get_variable_replace_str(value, old, new)
    return func
"""
This func is used to get the replace func of `keyword` object.
"""
def get_keyword_object_replace_method():
    def func(keyword, old, new):
        replace_method = get_replace_str_method('keyword')
        keyword.name = replace_method(keyword.name, old, new)
    return func
"""
This func is used to get the `present` func according to the object type.
"""
def get_present_method(instance):
    if isinstance(instance, Setting):
        return get_setting_object_present_method()
    elif isinstance(instance, ForLoop):
        return get_for_loop_object_present_method()
    elif isinstance(instance, Step):
        return get_step_object_present_method()
"""
This func is used to get the `replace` func according to the object type.
"""
def get_replace_method(instance, replaceKind):
    if isinstance(instance, _Import):
        return get_import_object_replace_method(replaceKind)
    if isinstance(instance, Setting):
        return get_setting_object_replace_method(replaceKind)
    elif isinstance(instance, ForLoop):
        return get_for_loop_object_replace_method(replaceKind)
    elif isinstance(instance, Step):
        return get_step_object_replace_method(replaceKind)