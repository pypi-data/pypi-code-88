import os

# 获取当前文件目录的根目录
DIR = os.path.dirname(os.path.dirname(__file__))
# 定义测试数据的存放目录
DATA_DIR = os.path.join(DIR, 'data')
# 定义用例存放的根目录
CASE_DIR = os.path.join(os.getcwd(), "testcases")
# 定义报告存放的根目录
REPORT_DIR = os.path.join(os.getcwd(), 'reports')
# 定义配置文件存放的根目录
CONFIG_DIR = os.path.join(DIR, 'config')
# 测试文件目录
TESTS_DIR = os.path.join(os.getcwd(), "testcases")
