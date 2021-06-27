import click
from yucebio_config import Config
import hashlib

class BaseUploader(object):
    PLATFROM = 'default'
    ALIAS_NAME = []

    def __init__(self) -> None:
        self._config = Config('uploader')

    @property
    def config(self):
        return {}

    def configure(self) -> None:
        """子类需要重载该接口以提供自定义配置能力"""
        click.secho("没有需要配置的内容", fg='yellow')

    def upload(self, local: str, remote: str, recursive: bool = True) -> str:
        """从本地上传文件到远端, 返回远端文件系统的路径

        Args:
            local (str): 本地文件路径
            remote (str): 远端文件路径
            recursive (bool): 自动识别文件或目录
        """
        click.secho(f"{self.__class__.__name__}未实现upload方法!!!", fg='red')
        return remote

    def download(self, remote: str, local: str, recursive: bool = True):
        """从远端下载文件或目录到本地

        Args:
            remote (str): 远端文件或目录
            local (str): 本地文件或目录
            recursive (bool, optional): 自动识别文件或目录. Defaults to True.
        """
        click.secho(f"{self.__class__.__name__}未实现download方法!!!", fg='red')


    def meta(self, remote: str):
        """获取远端文件或目录的meta信息

        Args:
            remote (str): 远端文件或目录
        """
        click.secho(f"{self.__class__.__name__}未实现meta方法!!!", fg='red')

    def md5(self, local_file: str):
        """获取文件md5值

        Args:
            local_file (str): 本地文件
        """
        with open(local_file, 'rb') as r:
            m = hashlib.md5(r.read())
            return m.hexdigest()