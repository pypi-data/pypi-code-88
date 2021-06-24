import argparse

from .decorators import print_port_info, print_wall_info, wall_reset, wall_add, wall_del, print_wsl_info
from .windows_command import WindowsCommandBase, WindowsCommandPort, WindowsCommandFireWall


class WindowsCommandArgParse:
    """
    命令解析类
    """

    def __init__(self):
        """
        初始化命令解析
        """

        self._parser = argparse.ArgumentParser(prog='wslm')
        self._subparsers = self._parser.add_subparsers(title='available commands')
        self._parser.add_argument(
            '-s',
            '--power_shell',
            default=WindowsCommandBase.POWER_SHELL,
            help='PowerShell.exe PATH'
        )
        self._parser.add_argument(
            '-e',
            '--encoding',
            default=WindowsCommandBase.CMD_ENCODING,
            help='Commands Encoding'
        )
        self._parser.set_defaults(func=lambda *args, **kwargs: self._parser.print_help())

    def _parser_cmd_linux(self):
        """
        wsl 相关命令
        :return:
        """
        wsl = self._subparsers.add_parser(
            name='wsl',
            help='WSL2 Commands'
        )
        wsl_subparsers = wsl.add_subparsers(
            help='WSL2 Commands'
        )
        wsl.set_defaults(func=lambda *args, **kwargs: wsl.print_help())

        # # 子系统信息查询
        wsl_info = wsl_subparsers.add_parser('info', help='wsl2 info')
        wsl_info.set_defaults(func=self.wsl_info_callback)

    @print_wsl_info
    def wsl_info_callback(self, namespace, parser, *args, **kwargs):
        """
        查询子系统信息
        :param namespace:
        :param parser:
        :param args:
        :param kwargs:
        :return:
        """

    def _parser_cmd_port(self):
        # windows10 端口转发管理
        port = self._subparsers.add_parser(
            name='port',
            help='connect and listen wsl ports'
        )
        port_subparsers = port.add_subparsers(
            help='connect and listen wsl ports'
        )

        port.set_defaults(func=lambda *args, **kwargs: port.print_help())

        # # 端口信息查询
        port_info = port_subparsers.add_parser('info', help='ports info')
        port_info.set_defaults(func=self.port_info_callback)

        # # 重置所有端口转发
        reset_info = port_subparsers.add_parser('reset', help='reset ports')
        reset_info.add_argument(
            '-w',
            '--wall',
            type=str,
            nargs='*',
            default=WindowsCommandFireWall.FIRE_WALL_RULE_ALL,
            choices=WindowsCommandFireWall.WALL_TYPES,
            help='with firewall'
        )
        reset_info.set_defaults(func=self.port_reset_callback)

        # # 添加端口转发
        port_add = port_subparsers.add_parser('add', help='add ports')
        port_add.add_argument(
            '-p',
            '--port',
            type=int,
            nargs='*',
            help='ports',
            required=True
        )
        port_add.add_argument(
            '-w',
            '--wall',
            type=str,
            nargs='*',
            default=WindowsCommandFireWall.FIRE_WALL_RULE_ALL,
            choices=WindowsCommandFireWall.WALL_TYPES,
            help='with firewall'
        )
        port_add.set_defaults(func=self.port_add_callback)

        # # 删除端口转发
        port_del = port_subparsers.add_parser('del', help='delete ports')
        port_del.add_argument(
            '-p',
            '--port',
            type=int,
            nargs='*',
            help='ports',
            required=True
        )
        port_del.add_argument(
            '-w',
            '--wall',
            type=str,
            nargs='*',
            default=WindowsCommandFireWall.FIRE_WALL_RULE_ALL,
            choices=WindowsCommandFireWall.WALL_TYPES,
            help='with firewall'
        )
        port_del.set_defaults(func=self.port_del_callback)

    @print_wall_info
    @print_port_info
    @wall_add
    def port_add_callback(self, namespace, parser, *args, **kwargs):
        """
        添加端口回调
        :param namespace:
        :param parser:
        :param args:
        :param kwargs:
        :return:
        """

        windows_command_port = WindowsCommandPort(
            encoding=namespace.encoding,
            power_shell=namespace.power_shell
        )
        namespace.port = list(set(namespace.port))
        for port in namespace.port:
            windows_command_port.add(port=port)

    @print_wall_info
    @print_port_info
    @wall_del
    def port_del_callback(self, namespace, parser, *args, **kwargs):
        """
        删除端口回调
        :param namespace:
        :param parser:
        :param args:
        :param kwargs:
        :return:
        """

        windows_command_port = WindowsCommandPort(
            encoding=namespace.encoding,
            power_shell=namespace.power_shell
        )
        namespace.port = list(set(namespace.port))
        for port in namespace.port:
            windows_command_port.delete(port=port)

    @print_wall_info
    @print_port_info
    @wall_reset
    def port_reset_callback(self, namespace, parser, *args, **kwargs):
        """
        重置所有端口转发
        :param namespace:
        :param parser:
        :param args:
        :param kwargs:
        :return:
        """

        windows_command_port = WindowsCommandPort(
            encoding=namespace.encoding,
            power_shell=namespace.power_shell
        )
        windows_command_port.reset()

    @print_wall_info
    @print_port_info
    def port_info_callback(self, namespace, parser, *args, **kwargs):
        """
        查询端口转发信息
        :param namespace:
        :param parser:
        :param args:
        :param kwargs:
        :return:
        """

    def run(self):
        self._parser_cmd_port()
        self._parser_cmd_linux()
        # 解析参数，并执行回调方法
        _args = self._parser.parse_args()
        _func = getattr(_args, 'func', None)
        if _func:
            _func(namespace=_args, parser=self._parser)
        else:
            self._parser.print_help()


def main():
    """
    主方法
    :return:
    """

    windows_command_arg_parse = WindowsCommandArgParse()
    windows_command_arg_parse.run()


if __name__ == '__main__':
    main()
