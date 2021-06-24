import regex
import xmltodict

from src.FMSHProjectGenerator import Converter


class Keil5Converter(Converter):
    # 文件类型定义
    __file_types = {
        '1': 'C',
        '2': 'ASM',
        '3': 'OBJ',
        '4': 'LIB',
        '5': 'TEXT',
        '6': 'CUSTOM',
        '7': 'CPP',
        '8': 'IMAGE',
    }

    # 优化定义(optimize, optimize_hint, keil_use_optimize_hint)
    __optimizes = {
        '0': ('none', 'size', False),
        '1': ('none', 'size', False),
        '2': ('low', 'size', False),
        '3': ('medium', 'size', False),
        '4': ('high', 'size', False),
        '5': ('high', 'speed', True),
        '6': ('high', 'balanced', True),
        '7': ('high', 'size', True),
    }

    # 警告定义
    __warnings = {
        '1': 'no warnings',
        '2': 'all warnings',
        '3': 'ac5-like warnings',
        '4': 'misra compatible',
    }

    __reset_vals = {
        '0': 'normal',
        '1': 'core',
        '2': 'reset pin',
        '3': 'connect under reset',
        '8': 'core and peripheral',
    }

    def __init__(self):
        super().__init__()

    def project_requirement(self):
        # KEIL 5 工程文件字典
        return {'uvprojx': None, 'uvoptx': None}

    def project_analyzer(self, prj_files: dict, target_name: str = '', output_file: str = ''):
        # 检查工程文件配置有效性
        if 'uvprojx' not in prj_files.keys() or prj_files['uvprojx'] is None:
            raise Exception('Keil 5 project file(*.uvprojx) not found')

        if 'uvoptx' not in prj_files.keys() or prj_files['uvoptx'] is None:
            print('Keil 5 project options file(*.uvoptx) not found, relevant settings will remain default!')

        # ---------------- 加载工程描述文件模板 ----------------
        prj_desc = self.load_template(self)

        # ---------------- 加载工程 ----------------
        # 读取工程文件
        f = open(prj_files['uvprojx'], 'r')
        project_xml = f.read()
        f.close()
        project = xmltodict.parse(project_xml, force_list=('Target', 'File'))

        # 读取工程选项文件
        f = open(prj_files['uvoptx'], 'r')
        opt_xml = f.read()
        f.close()
        project_opt = xmltodict.parse(opt_xml, force_list=('Target', 'SetRegEntry'))

        # ---------------- 寻找target对象 ----------------
        # 注意：通过target_name参数指定target，如果target_name为空串，默认选择第一个target
        target_obj = None
        target_obj_opt = None

        if target_name != '':
            for target in project['Project']['Targets']['Target']:
                if target['TargetName'] == target_name:
                    target_obj = target
                    break
            for target in project_opt['ProjectOpt']['Target']:
                if target['TargetName'] == target_name:
                    target_obj_opt = target
                    break
            if target_obj is None:
                print("target " + target_name + " not found")
                exit(1)
            elif target_obj_opt is None:
                print("target " + target_name + " options not found")
                exit(1)
        else:
            if project['Project']['Targets'] is None or \
                    project_opt['ProjectOpt'] is None:
                raise Exception('no target in given project file')
            target_obj = project['Project']['Targets']['Target'][0]
            target_obj_opt = project_opt['ProjectOpt']['Target'][0]
            target_name = target_obj['TargetName']

        # ---------------- 加载芯片配置文件 ----------------
        target_chip_name = target_obj['TargetOption']['TargetCommonOption']['Device']
        target_chip_name = str.upper(target_chip_name)
        target_chip = self.load_chip(target_chip_name)

        # ---------------- 生成工程描述yaml对象 ----------------
        # 工程名称
        prj_desc['name'] = target_name

        # 工程目标
        prj_desc['target'] = target_chip_name

        # 工程选项
        # —— Target: Use MicroLIB
        prj_desc['options']['keil_micro_lib'] = True if target_obj['TargetOption']['TargetArmAds']['ArmAdsMisc'][
                                                            'useUlib'] == '1' else False
        # —— C/C++: C99 Mode
        prj_desc['options']['c_version'] = 'c99' if target_obj['TargetOption']['TargetArmAds']['Cads'][
                                                        'uC99'] == '1' else 'c90'

        # —— C/C++: Optimization
        optimize_lvl = target_obj['TargetOption']['TargetArmAds']['Cads']['Optim']
        prj_desc['options']['optimize'], \
            prj_desc['options']['optimize_hint'], \
            prj_desc['options']['keil_use_optimize_hint'] = self.__optimizes[optimize_lvl]

        # —— C/C++: Warnings
        warning_lvl = target_obj['TargetOption']['TargetArmAds']['Cads']['wLevel']
        if warning_lvl in self.__warnings:
            prj_desc['options']['keil_warning'] = self.__warnings[warning_lvl]

        # 工程高级选项 —— linker script file(*.sct)
        if target_obj['TargetOption']['TargetArmAds']['LDads']['umfTarg'] == '0':
            if 'ScatterFile' in target_obj['TargetOption']['TargetArmAds']['LDads']:
                prj_desc['advanced_options']['keil_linker_cfg'] = \
                    target_obj['TargetOption']['TargetArmAds']['LDads']['ScatterFile']

        # 调试工具
        debug_tool_sel = target_obj_opt['TargetOption']['DebugOpt']['nTsel']
        if debug_tool_sel == '4':
            # JLink
            prj_desc['debug']['tool'] = 'jlink'

            # 获取 JLink 配置
            jlink_opt = None
            for item in target_obj_opt['TargetOption']['TargetDriverDllRegistry']['SetRegEntry']:
                if item['Key'] == 'JL2CM3':
                    jlink_opt = item['Name']
                    break
            if jlink_opt is None:
                print('debug tool not supported, relevant settings will remain default')

            # JLink 接口，连接选项
            jlink_opt_itf = regex.search('-O([0-9]*)', jlink_opt).group(1)
            if int(jlink_opt_itf) & (0b1 << 6) == 0:
                prj_desc['debug']['interface'] = 'JTAG'
            else:
                prj_desc['debug']['interface'] = 'SWD'
            if int(jlink_opt_itf) & (0b11 << 10) == (0b00 << 10):
                prj_desc['debug']['connect'] = 'normal'
            elif int(jlink_opt_itf) & (0b11 << 10) == (0b01 << 10):
                prj_desc['debug']['connect'] = 'with pre-reset'
            elif int(jlink_opt_itf) & (0b11 << 10) == (0b10 << 10):
                prj_desc['debug']['connect'] = 'under reset'
            else:
                print('JLink connect type not supported, relevant settings will remain default')

            # JLink 接口速率
            jlink_opt_spd = regex.search('-ZTIFSpeedSel([0-9]*)', jlink_opt).group(1)
            prj_desc['debug']['speed'] = int(jlink_opt_spd)

            # JLink 接口复位
            jlink_opt_rst = regex.search('-RST([0-9]*)', jlink_opt).group(1)
            if jlink_opt_rst in self.__reset_vals:
                prj_desc['debug']['reset'] = self.__reset_vals[jlink_opt_rst]
            else:
                print('JLink reset type not supported, relevant settings will remain default')

            # 工程高级选项 —— flasher configuration
            jlink_opt_fls = regex.findall(
                '-FF[0-9]([0-9a-zA-Z_]*)(.FLM)? -FS[0-9]([0-9]*) -FL[0-9]([0-9]*)( -FP[0-9]\(\$\$Device:[\S]+\$([\S]+)\))?',
                jlink_opt)

            if jlink_opt_fls is not None:
                for fls_name, fls_ext, fls_base, fls_size, _, fls_path in jlink_opt_fls:
                    fls_algo = dict(name=fls_name + fls_ext, path=fls_path if fls_path != '' else None, base=fls_base,
                                    size=fls_size)
                    if fls_algo not in target_chip['target']['keil_5_flash_algorithms']:
                        if prj_desc['advanced_options']['keil_flasher_cfg'] is None:
                            prj_desc['advanced_options']['keil_flasher_cfg'] = list()
                        prj_desc['advanced_options']['keil_flasher_cfg'].append(fls_algo)

        # 编译器全局定义
        defines = target_obj['TargetOption']['TargetArmAds']['Cads']['VariousControls']['Define']
        define_list = str.split(defines, ",")
        for define in define_list:
            if define in target_chip['fl_driver_defines']:
                define_list.remove(define)
        prj_desc['defines'] = define_list

        # 包含路径
        includes = target_obj['TargetOption']['TargetArmAds']['Cads']['VariousControls']['IncludePath']
        include_list = str.split(includes, ",")
        prj_desc['includePaths'] = include_list

        # 文件组
        prj_desc['groups'] = list()
        groups = target_obj['Groups']['Group']
        for group in groups:
            parent_dir_obj = prj_desc
            group_name = group['GroupName']

            # 确定当前组的父对象（根下的组父对象为根对象）
            if str.find(group['GroupName'], '/') != -1 or str.find(group['GroupName'], '\\') != -1:
                # 该文件组为子文件组
                group_dir = str.replace(group['GroupName'], '\\', '/')
                parent_dir = str.split(group_dir, '/')[:-1]
                group_name = str.split(group_dir, '/')[-1]

                # 寻找父目录对象（不存在则自动添加）
                for p_dir in parent_dir:
                    group_exist_flag = False
                    if parent_dir_obj['groups'] is None:
                        parent_dir_obj['groups'] = list()
                    for project_group in parent_dir_obj['groups']:
                        if project_group['name'] == p_dir:
                            parent_dir_obj = project_group
                            group_exist_flag = True
                            break

                    # 不存在该父目录，进行创建
                    if not group_exist_flag:
                        tmp_group = dict(name=p_dir, files=None, groups=None)
                        if parent_dir_obj['groups'] is None:
                            parent_dir_obj['groups'] = list()
                        parent_dir_obj['groups'].append(tmp_group)
                        parent_dir_obj = tmp_group

            # 创建组
            self_obj = dict(name=group_name, files=None, groups=None)

            # 添加文件到组
            if 'Files' in group and group['Files'] is not None:
                for file in group['Files']['File']:
                    if self_obj['files'] is None:
                        self_obj['files'] = list()
                    self_obj['files'].append(
                        dict(name=file['FileName'], type=self.__file_types[file['FileType']], path=file['FilePath']))

            # 添加组到父对象
            if parent_dir_obj['groups'] is None:
                parent_dir_obj['groups'] = list()
            parent_dir_obj['groups'].append(self_obj)

        # ---------------- 如果output_file不为None, 返回工程描述yaml对象 ----------------
        if output_file != '':
            f = open(output_file, 'w')
            self._yml.dump(prj_desc, f)
            f.close()

        return prj_desc
