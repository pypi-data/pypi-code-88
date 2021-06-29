"""
Project CLI
"""

import click
import os
import shutil
import codecs


@click.group()
def cli():
    """Project Group"""
    pass


@cli.group()
def project():
    """Manage project, such as create, ..."""
    pass


LANGUAGE_FRAMEWORKS = {
    'python': ['fastapi', 'django', 'flask'],
    'go': ['gin', 'dapr_grpc']
}
VIRTUAL_ENV_NAME = '.venv'


def _get_run_dir():
    """获取当前运行目录"""
    # print('current dir:', os.getcwd())
    return os.getcwd()


def _get_project_folder_name(name, project_type):
    """获取工程文件夹名称"""
    return name + '_' + project_type


def _get_project_path(path, name, project_type):
    """获取工程目录"""
    return os.path.join(path, _get_project_folder_name(name, project_type))


def _check_path(path):
    """检查初始化path"""

    # path 末尾不能以 / 结尾
    if len(path) > 1 and path.endswith('/'):
        path = path[:-1]

    if path.startswith('.'):
        # 当path是'.'开头的确定为相对路径
        path = os.path.abspath(path)
    elif path == '':
        # 当path是''时，使用当前路径
        path = _get_run_dir()
    else:
        path = os.path.abspath(path)

    # 检查path是否有效存在和能读写
    # print('check path:', path)
    if os.path.exists(path):
        # 检查读写权限
        test_file_path = os.path.join(path, 't')
        try:
            f = open(test_file_path, 'w')
            f.close()
        except PermissionError or IOError:
            click.echo(f"Please check {path} directory r/w permission")
            return None
        else:
            # 删除测试文件
            os.remove(test_file_path)
    else:
        try:
            os.makedirs(path)
        except PermissionError or IOError:
            click.echo(f'Make directory {path} permission deny.')
            return None
        except OSError as e:
            click.echo(f'Make directory {path} occurred OS error. {e}')
            return None
    return path


def _check_project_path(path):
    """检查项目path"""

    # 检查是否存在
    if os.path.exists(path):
        file = os.path.split(path)[-1]
        if os.path.isdir(path):
            click.echo(f"same directory({file}) already exists.")
        else:
            click.echo(f"same file name {file} already exists.")
        return False
    else:
        return True


def _get_template_path(lang: str, framework_name: str) -> str:
    """获取模板路径"""
    current_path = os.path.abspath(__file__)
    return os.path.join(os.path.dirname(os.path.dirname(current_path)), 'templates', lang, framework_name)


def _get_framework_list() -> list:

    r = []
    for k, v in LANGUAGE_FRAMEWORKS.items():
        for i in v:
            r.append(k + '-' + i)
    return r

@project.command()
# @click.option(
#     '-l', '--lang', 
#     prompt='Please input language type', 
#     required=True, 
#     type=click.Choice([l['language'] for l in LANGUAGES], case_sensitive=False), 
#     help='project language type'
# )
@click.option(
    '-f', '--framework', 
    prompt=f'Please select develop framework [{" ".join(str(i) + ":" + v for i, v in enumerate(_get_framework_list()))}]', 
    required=True, 
    default=0,
    type=click.IntRange(0, len(_get_framework_list())), 
    help='dev framework'
)
@click.option(
    '-i', 
    '--init_env', 
    prompt='Init virtual env', 
    type=bool, default=True, 
    help='Whether initialize dev environment.'
)
@click.option(
    '-p', 
    '--path', 
    prompt='Project base path', 
    default=_get_run_dir, 
    type=str, 
    help='Specify project path'
)
@click.argument('project')
def create(framework, init_env, path, project):
    """Create project."""

    # print(framework, init_env, path, project)

    # project_type = PROJECT_LANGUAGE_TYPES[type]
    # # print(name, project_type, init_env, path, __file__)

    # 检查path是否有效
    path = _check_path(path)
    if path is None:
        return

    # # 创建工程目录
    # project_name = _get_project_folder_name(name, project_type)
    # project_path = _get_project_path(path, name, project_type)
    project_path = os.path.join(path, project)

    # 检测当前文件夹是否存在同名文件
    if not _check_project_path(project_path):
        return

    # # 创建父级目录
    # os.mkdir(project_path)

    # 获取模板
    lang, framework = _get_framework_list()[framework].split('-')
    template_path = _get_template_path(lang=lang, framework_name=framework)

    # 检查模板是否存在
    if not os.path.exists(template_path):
        click.echo(f"{lang} framework {framework} template not exists.")
        return

    # 创建服务目录
    shutil.copytree(template_path, project_path)

    # 创建虚拟环境
    if init_env:
        import venv

        service_env_path = os.path.join(project_path, VIRTUAL_ENV_NAME)
        venv.create(service_env_path, with_pip=True)

    click.echo('Project created successfully! :-)')
