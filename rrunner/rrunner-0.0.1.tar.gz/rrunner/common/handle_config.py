from configparser import ConfigParser
from rrunner.common.handle_path import CONFIG_DIR, DATA_DIR
import os
# 封装读/写config.ini中的数据
class Config(ConfigParser):
    def __init__(self, file_name, encoding="utf-8-sig"):
        # 调用父类的init方法
        super().__init__()
        self.read(file_name, encoding=encoding)
        self.file_name = file_name
        self.encoding = encoding

    # 往配置文件config.init中写数据
    def write_data(self, section, option, value):
        self.set(section, option, value)
        self.write(fp=open(self.file_name, "w", encoding=self.encoding))


# 创建一个对象读取config.ini中的数据
#config = Config(os.path.join(CONFIG_DIR, "config.ini"))
config = Config(os.path.join(os.getcwd(), "config.ini"))
# 创建一个对象读取test_data.ini中的数据
configtestdata = Config(os.path.join(DATA_DIR, "test_data.ini"))
