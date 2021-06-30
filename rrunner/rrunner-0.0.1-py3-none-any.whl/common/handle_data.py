import re
from rrunner.common.handle_config import configtestdata


class CaseData:
    """这个类专门用来保存，执行执行过程中提取出来给其他用例用的数据"""
    pass


"""替换excel中用#xxx#表示的参数，传入的是类名和参数值"""
def replace_data(cls, data):
    r1 = r"#(.+?)#"
    # 根据是否匹配到要替换的数据，来决定要不要进入循环
    while re.search(r1, data):
        # 匹配一个需要替换的内容
        item = re.search("#(.+?)#", data)
        # 获取待替换的内容
        rep_data = item.group()
        # 获取需要替换的字段
        key = item.group(1)
        try:
            # 根据要替换的字典，去配置文件中找到对应的数据，进行替换
            value = configtestdata.get("test_data", key)
        except:
            # 如果配置文件中找不到，报错了，则去CaseData的属性中找对应的值进行替换
            value = getattr(cls, key)
        data = data.replace(rep_data, str(value))
    return data


def assert_dict_item(dic1, dic2):
    """
    断言dic1中的所有元素时dic2中的成员，成立返回True，不成立引发断言错误
    :param dic1:
    :param dic2:
    :return:
    """
    for item in dic1.items():
        print(item)
        print(dic2.items())
        if item not in dic2.items():
            raise AssertionError("{}items not in {}".format(dic1, dic2))
