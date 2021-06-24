import json
import os

from jinja2 import Environment, FileSystemLoader, select_autoescape
from ruamel.yaml import YAML


class Converter:
    def __init__(self):
        # ruamel.yaml实例
        self._yml = YAML(typ='rt')

        # 将None输出设定为null
        def represent_none(self, data):
            return self.represent_scalar('tag:yaml.org,2002:null', 'null')

        self._yml.representer.add_representer(type(None), represent_none)

        # 设定ruamel.yaml流格式
        self._yml.default_flow_style = False

    # 获取工程模板文件路径
    @staticmethod
    def load_template(self):
        f = open(os.path.join(os.path.dirname(__file__), 'assets', 'project_template.yaml'))
        tmp = self._yml.load(f)
        f.close()
        return tmp

    @staticmethod
    def load_chip(chip_name: str):
        chip = None
        if chip_name is not None:
            chip_file = os.path.join(os.path.dirname(__file__), 'chips', chip_name + '.json')
            if os.path.exists(chip_file):
                if os.access(chip_file, os.R_OK):
                    f = open(chip_file, 'r')
                    chip = json.load(fp=f)
                    f.close()
        if chip is None:
            raise Exception("chip configuration file not found: " + chip_name)
        return chip

    # 获取工程文件需求抽象接口
    def project_requirement(self) -> dict:
        pass

    # 分析工程抽象接口
    def project_analyzer(self, prj_files: dict, target_name: str = '', output_file: str = ''):
        pass


class Generator:
    # 生成工程抽象接口
    def project_generator(self, prj_info, target_info, prj_path):
        pass


class ProjectGenerator:
    def __init__(self):
        # Jinja2环境
        self.__env = Environment(
            loader=FileSystemLoader("converters/templates"),
            autoescape=select_autoescape(),
            trim_blocks=True,
            lstrip_blocks=True,
        )

        # ruamel.yaml对象
        self.__yaml = YAML(typ='rt')

        # 工程对象
        self.__prj_desc = None

    def convert(self, src_prj_path, converter: Converter, output_file: str = ''):
        # 获取转换器所需工程文件
        req = converter.project_requirement()

        # 查找工程文件
        for root, dirs, files in os.walk(src_prj_path, topdown=False):
            for name in files:
                ext_name = name.split('.')[-1]
                if ext_name in req.keys():
                    req[ext_name] = os.path.join(root, name)

        # 转换并保存工程对象
        self.__prj_desc = converter.project_analyzer(req, output_file=output_file)

    def generate(self, dest_prj_path, generator: Generator, input_file: str = ''):
        # 加载工程描述文件
        if input_file != '':
            f = open(input_file, 'r')
            self.__prj_desc = self.__yaml.load(f)
            f.close()
        if self.__prj_desc is None:
            raise Exception('failed to load project!')

        # 检查芯片型号是否正确，并加载芯片配置
        chip = None
        if self.__prj_desc['target'] is not None:
            chip_file = os.path.join(os.path.dirname(__file__), 'chips', str.upper(self.__prj_desc['target']) + '.json')
            if os.path.exists(chip_file):
                if os.access(chip_file, os.R_OK):
                    f = open(chip_file, 'r')
                    chip = json.load(fp=f)
                    f.close()
        if chip is None:
            raise Exception("Configuration file not found for chip " + self.__prj_desc['target'])

        # 添加芯片的工程相关参数到工程
        # 全局定义
        self.__prj_desc['defines'] = chip['fl_driver_defines'] + self.__prj_desc['defines']

        # TODO:
        '''
        # 生成工程前，需要检查是否工程已经存在。如果存在，需要对工程进行合并（主要是合并defines, includePaths 和 groups，其他配置替换）
        # groups合并主要是考虑到用户自己新建的group的问题，工具首先保证yaml文件中描述的组和文件全部存在，在此基础上添加原有的文件
        # 合并可以选择使能/禁止
        # 合并功能调用函数对于不同IDE有不同调用方法，实现合并到下方生成工程的枚举中。
        '''

        # 生成工程
        generator.project_generator(self.__prj_desc, chip['target'], dest_prj_path)
