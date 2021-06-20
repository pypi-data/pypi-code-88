import os
import sys
import shutil
from lesscli import Application
import re
import json
import random
from arms.utils.wordstyle import replace_dict, replace_all, WordStyle, WordSeed
from arms.utils.common import dump_file_name
from pathlib import Path


def terminal_menu(options, show_func):
    """
    :param options: 选项列表
    :param show_func: 从选项获取描述的函数
    :return: 选中的选项，None表示退出
    """
    page_no = 0
    page_size = 9
    while True:
        opt_slide = options[page_no * page_size: (page_no + 1) * page_size]
        print('\n\n------------------------------------')
        print('--    Welcome to Terminal Menu    --')
        print('------------------------------------')
        for idx, opt_item in enumerate(opt_slide):
            print('[%d] < %s' % (idx + 1, show_func(opt_item)))
        print('')
        print('[q] < Quit.')
        if page_no > 0:
            print('[j] < Previous Page.')
        if (page_no + 1) * page_size < len(options):
            print('[k] < Next Page.')
        print('\nChoice:', end=' ')
        try:
            os.system('/bin/stty raw')
            c = sys.stdin.read(1).lower()
            print(c)
            print('\r')
        finally:
            os.system('/bin/stty cooked')
        if c == 'q':
            return None
        elif '1' <= c <= '9':
            return opt_slide[int(c) - 1]
        elif page_no > 0 and c == 'j':
            page_no -= 1
            continue
        elif (page_no + 1) * page_size < len(options) and c == 'k':
            page_no += 1
            continue
        else:
            print('Exception: Wrong Number, Please Try Again.')
            continue


def makedir(real_path):
    from pathlib import Path
    Path(real_path).mkdir(parents=True, exist_ok=True)


def print_help():
    text = """

    arms init [git_url]         : 项目初始化（直接覆盖）
    arms patch [git_url]        : 项目补丁（保留重名文件）
    arms -h                     : show help information
    arms -v                     : show version


    """
    print(text)


def print_version():
    """
    显示版本
    """
    from arms import __version__
    text = """
    arms version: {}

    """.format(__version__)
    print(text)


def run_process(tpl_name, is_patch=False):
    """
    项目初始化工具
    """
    # [1/7]判断本地有.git目录
    if not os.path.isdir('.git'):
        print('Please change workdir to top! or run "git init" first.')
        exit(1)
    # [2/7]拉取模版项目
    local_path = Path.home() / '.arms_config.json'
    if not local_path.exists():
        print('请先执行arms config [git_url]')
        exit(-1)
    config_json = json.loads(local_path.open(encoding='utf-8').read())
    if tpl_name not in config_json:
        print('模版名称不存在！')
        exit(-1)
    ret = os.system('rm -rf .arms_tpl && git clone %s .arms_tpl' % config_json[tpl_name]['git_url'])
    if ret:
        exit(1)
    # [3/7]生成替换字典
    json_path = Path('.arms_tpl/.arms.json')
    if not json_path.is_file():
        print('No .arms.json found in source project!')
        exit(1)
    index_json = {}
    try:
        index_json.update(json.loads(json_path.open().read()))
    except Exception as e:
        print('.arms.json is not valid JSON format!')
        exit(1)
    # 支持层级选择
    while isinstance(index_json, dict) and '__name__' not in index_json:
        options = [{'key': key, 'value': value} for key, value in index_json.items()]
        opt_choice = terminal_menu(options, lambda x: x['key'].strip())
        if opt_choice is None:
            exit(0)
        index_json = opt_choice['value']
    if not isinstance(index_json, dict):
        print('.arms.json错误: 节点类型错误!')
        exit(1)
    if '__only__' in index_json:
        if '__except__' in index_json:
            print('.arms.json错误: __only__和__except__不能同时定义!')
            exit(1)
        if '__rename__' in index_json:
            print('.arms.json错误: __only__和__rename__不能同时定义!')
            exit(1)
    if '__rename__' in index_json:
        if any(rule.count(':') != 1 for rule in index_json['__rename__']):
            print('.arms.json错误: __rename__不符合规范!')
            exit(1)
    old_proj_name = index_json['__name__']
    new_proj_name = input('请输入项目代号：')
    if not new_proj_name:
        print('项目代码不能为空！')
        exit(1)
    # [4/7]删除无用路径
    if index_json.get('__only__'):
        only_paths = [rule.split(':')[-1] for rule in index_json['__only__']]
        rename_rules = [rule for rule in index_json['__only__'] if ':' in rule]
    else:
        only_paths = ['.']
        rename_rules = index_json.get('__rename__', [])
    except_paths = index_json.get('__except__', [])
    tar_cmd = 'tar %s -czf ../.arms_tpl.tgz --exclude .git %s' % (
        ' '.join(f'--exclude {p}' for p in except_paths), ' '.join(only_paths))
    print(tar_cmd)
    os.system(' && '.join([
        'cd .arms_tpl',
        tar_cmd,
        'cd ..',
        'rm -rf .arms_tpl',
        'mkdir .arms_tpl',
        'cd .arms_tpl',
        'tar -zxf ../.arms_tpl.tgz',
        'rm -f ../.arms_tpl.tgz'
    ]))
    # [5/7]文件重命名
    repl_dict = replace_dict(old_proj_name, new_proj_name)
    # renames = index_json.get('__rename__', [])
    out_abs_path = os.path.abspath('.')
    os.chdir('.arms_tpl')  # 变换工作目录
    for item in rename_rules:
        to_path, from_path = item.split(':', 1)
        if Path(from_path).exists():  # 前面的重命名可能会影响后面的重命名
            os.rename(from_path, to_path)  # os.rename非常强大
    curpath = Path('.')
    for i in range(20):  # 替换路径中的项目代号，最大循环20轮
        touched = False
        renames = []
        for p in curpath.rglob('*'):
            full_path = str(p)
            new_path = replace_all(full_path, repl_dict)
            if new_path != full_path:
                renames.append(f'{new_path}:{full_path}')
        for item in renames:
            to_path, from_path = item.split(':', 1)
            if Path(from_path).exists():  # 前面的重命名可能会影响后面的重命名
                os.rename(from_path, to_path)  # os.rename非常强大
                touched = True
        if not touched:  # 若一轮操作没有产生重命名则退出
            break
    if is_patch:  # 通过重命名，保留重名文件
        midname = str(WordSeed(WordStyle.lower_snake, WordSeed.of(new_proj_name).tokens))
        out_path = Path('..')
        for p in curpath.rglob('*'):
            if p.is_file() and (out_path / p).is_file():
                new_file_name = dump_file_name(p.parts[-1], project=midname)
                p.rename('/'.join(p.parts[:-1] + (new_file_name,)))
    # [6/7]文本替换
    for p in curpath.rglob('*'):
        if p.is_dir() or str(p).startswith(('.git/', '.idea/', 'node_modules/')):
            continue
        try:
            text = p.open().read()
            new_text = replace_all(text, repl_dict)
            if new_text != text:
                with p.open('w') as f:
                    f.write(new_text)
        except Exception as e:
            pass
    # [7/7]git add
    os.system('tar -czvf ../.arms_tpl.tgz .')
    os.chdir(out_abs_path)  # 变换工作目录
    os.system(' && '.join([
        'rm -rf .arms_tpl',
        'tar -zxf .arms_tpl.tgz',
        'rm -f .arms_tpl.tgz'
    ]))
    os.system('git add .')
    if is_patch:
        print('---- arms patch succeed :) ----')
    else:
        print('---- arms init succeed :) ----')


def run_init(*args):
    """
    项目初始化工具
    arms init [name]
    """
    if len(args) != 1:
        print("请输入命令完成项目初始化：arms init [name]")
        exit(1)
    try:
        run_process(tpl_name=args[0], is_patch=False)
    finally:
        os.system('rm -rf .arms_tpl')
        os.system('rm -f .arms_tpl.tgz')


def run_patch(*args):
    """
    项目补丁工具
    arms patch [name]
    """
    if len(args) != 1:
        print("请输入命令完成项目补丁：arms patch [name]")
        print()
        exit(1)
    try:
        run_process(tpl_name=args[0], is_patch=True)
    finally:
        os.system('rm -rf .arms_tpl')
        os.system('rm -f .arms_tpl.tgz')


def run_config(*args):
    """
    arms配置工具
    arms config [git_url]
    """
    if len(args) != 1:
        print("请输入文档访问链接：arms config [git_url]")
        exit(1)
    git_url = args[0]
    # [1/2]拉取模版源
    ret = os.system("git clone %s .arms_tpl_src" % git_url)
    if ret:
        exit(1)
    # [2/2]保存到本地目录
    local_path = Path.home() / '.arms_config.json'
    try:
        with open(local_path, 'w') as f:
            f.write(open('.arms_tpl_src/config.json').read())
        print("更新配置成功.")
    except Exception:
        print(f"无法修改本地配置文件：{local_path}")
    finally:
        shutil.rmtree('.arms_tpl_src')


def run_search(*args):
    """
    项目搜索工具
    arms config [keyword]
    """
    if len(args) != 1:
        print("请输入搜索关键词：arms search [keyword]")
        exit(1)
    keyword = args[0].lower()
    local_path = Path.home() / '.arms_config.json'
    config_json = json.loads(local_path.open(encoding='utf-8').read())
    for name, setting in config_json.items():
        if keyword == name.lower() or keyword in setting['description'].lower() or keyword in setting.get('keywords', '').lower():
            print(f'{name} - {setting["description"]}')


def entrypoint():
    if sys.version_info.major == 2 or sys.version_info.minor < 5:
        print('arms已不再支持python2，请安装python3.5+')
        exit(1)
    Application('armstrong')\
        .add('version', print_version)\
        .add('init', run_init) \
        .add('patch', run_patch) \
        .add('config', run_config) \
        .add('search', run_search) \
        .run()
