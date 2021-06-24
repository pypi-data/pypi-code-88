import re
import subprocess
from platform import system as platform_system

from prettytable import PrettyTable

from .util import Color


class WindowsCommandBase:
    """
    命令基类
    """

    CMD_ENCODING = 'gbk'

    POWER_SHELL = r'PowerShell.exe'

    BASH_EXE = r'bash.exe'

    WSL_EXE = r'wsl.exe'

    def __init__(
            self,
            encoding=CMD_ENCODING,
            power_shell: str = POWER_SHELL,
            bash_exe: str = BASH_EXE,
            wsl_exe: str = WSL_EXE,
            **kwargs
    ):
        self._cmd_encoding = encoding
        self._power_shell = power_shell
        self._bash_exe = bash_exe
        self._wsl_exe = wsl_exe
        self._settings = kwargs

    def run_cmd(self, cmd: str, run=True) -> str:
        """
        执行命令，并返回结果
        :param run:
        :param cmd:
        :return:
        """
        if not run:
            return cmd
        pre_str = Color.red('Exec')
        cmd_str = Color.yellow(cmd)
        print(f'{pre_str} : {cmd_str}')
        _result = subprocess.Popen(
            cmd,
            shell=True,
            stderr=subprocess.STDOUT,
            stdout=subprocess.PIPE,
            bufsize=-1,
            encoding=self._cmd_encoding
        )
        _result.wait()
        try:
            data = _result.stdout.read()
        except UnicodeDecodeError:
            data = ''
        return data


class WindowsCommandLinux(WindowsCommandBase):
    """
    linux子系统
    """

    IPV4_PATTERN = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

    def get_wsl_ip(self, run=True) -> str:
        """
        获取WSL的IP
        :return:
        """

        wsl_cmd = "ifconfig eth0 | grep 'inet '"
        if platform_system().lower() == 'windows':
            wsl_cmd = f'{self._bash_exe} -c "{wsl_cmd}"'
        if not run:
            return wsl_cmd
        _result = self.run_cmd(cmd=wsl_cmd, run=run)
        wsl_ip = re.search(self.IPV4_PATTERN, _result).group(0)
        return wsl_ip

    def shutdown_wsl(self, run=True) -> str:
        """
        立即终止所有正在运行的分发和 WSL 2 轻型工具虚拟机
        :param run:
        :return:
        """
        cmd = f'{self._wsl_exe} --shutdown'
        return self.run_cmd(cmd=cmd, run=run)

    def info_table(self):
        """
        获取子系统信息，以 PrettyTable 格式返回
        :return:
        """
        wsl_info = self.info()
        wsl_info_table = self.wsl_info_to_table(port_info_list=wsl_info)
        return wsl_info_table

    def info(self):
        """
        获取子系统信息
        :return:
        """
        cmd = self.get_cmd_wsl_info()
        result_string = self.run_cmd(cmd).splitlines()
        return self.wsl_info_to_list(wsl_info_result=result_string)

    def get_cmd_wsl_info(self):
        return f'{self._wsl_exe} -l -v'

    @staticmethod
    def wsl_info_to_list(wsl_info_result):
        _result = []
        for i, v in enumerate(wsl_info_result):
            if i == 0:
                continue
            v = v.replace(b'\x00'.decode(), '').strip()
            if not v:
                continue
            v = v.split()
            if len(v) == 3:
                v.insert(0, '')
            _result.append({
                "name": v[1],
                "state": v[2],
                "version": v[3],
                "is_default": v[0] == '*',
            })
        return _result

    @staticmethod
    def wsl_info_to_table(port_info_list):
        """
        准换为PrettyTable
        :return:
        """
        wsl_info_table = PrettyTable(
            field_names=['name', 'state', 'version', 'is_default'],
            min_table_width=72,
        )
        for item in port_info_list:
            wsl_info_table.add_row([v for k, v in item.items()])
        return wsl_info_table


class WindowsCommandPort(WindowsCommandBase):
    """
    端口转发
    """

    CMD_PORT_PRE = '{power_shell} netsh interface portprox'

    CMD_PORT_ADD = '{pre} add v4tov4 listenport={port} listenaddress={addr} connectport={port} connectaddress={ip}'

    CMD_PORT_DEL = '{pre} delete v4tov4 listenport={port} listenaddress={addr}'

    CMD_PORT_INFO = '{pre} show all'

    CMD_PORT_RESET = '{pre} reset'

    def info_table(self):
        """
        获取端口转发信息，以 PrettyTable 格式返回
        :return:
        """

        port_info = self.info()
        port_info_table = self.port_info_to_table(port_info_list=port_info)
        return port_info_table

    def info(self):
        """
        获取端口转发信息
        :return:
        """

        cmd = self.get_cmd_port_info()
        result_string = self.run_cmd(cmd).splitlines()
        return self.port_info_to_list(port_info_result=result_string)

    def add(self, port: int, addr: str = '0.0.0.0', ip: str = ''):
        """
        添加端口
        :param port:
        :param addr:
        :param ip:
        :return:
        """

        cmd = self.get_cmd_port_add(port=port, addr=addr, ip=ip)
        return self.run_cmd(cmd)

    def delete(self, port: int, addr: str = '0.0.0.0'):
        """
        删除端口
        :param port:
        :param addr:
        :return:
        """

        cmd = self.get_cmd_port_del(port=port, addr=addr)
        return self.run_cmd(cmd)

    def reset(self):
        """
        清除所有的端口转发
        :return:
        """
        cmd = self.get_cmd_port_reset()
        return self.run_cmd(cmd)

    def __get_cmd_port_pre(self) -> str:
        cmd = self.CMD_PORT_PRE.format(
            power_shell=self._power_shell
        )
        return cmd

    def get_cmd_port_add(self, port: int, addr: str = '0.0.0.0', ip: str = '') -> str:
        """
        获取添加端口转发的命令字符串
        :param port: 要转发的端口
        :param addr: 监听地址
        :param ip: 监听IP，为空时自动获取wsl的ip
        :return:
        """

        ip = ip if ip else WindowsCommandLinux(
            encoding=self._cmd_encoding,
            power_shell=self._power_shell,
            bash_exe=self._bash_exe,
            **self._settings
        ).get_wsl_ip()
        cmd = self.CMD_PORT_ADD.format(
            pre=self.__get_cmd_port_pre(),
            port=port,
            addr=addr,
            ip=ip
        )
        return cmd

    def get_cmd_port_del(self, port: int, addr: str = '0.0.0.0') -> str:
        """
        获取删除端口转发的命令字符串
        :param port: 要转发的端口
        :param addr: 监听地址
        :return:
        """

        cmd = self.CMD_PORT_DEL.format(
            pre=self.__get_cmd_port_pre(),
            port=port,
            addr=addr,
        )
        return cmd

    def get_cmd_port_reset(self):
        """
        获取清除端口转发的命令字符串
        :return:
        """
        cmd = self.CMD_PORT_RESET.format(pre=self.__get_cmd_port_pre())
        return cmd

    def get_cmd_port_info(self):
        """
        获取端口转发信息的命令字符串
        :return:
        """
        cmd = self.CMD_PORT_INFO.format(pre=self.__get_cmd_port_pre())
        return cmd

    @staticmethod
    def port_info_to_list(port_info_result):
        _result = []
        for key, line in enumerate(port_info_result):
            if key < 5:
                continue
            line = line.strip().split()
            if len(line) == 4:
                _result.append({
                    'listen_address': line[0],
                    'listen_port': int(line[1]),
                    'connect_address': line[2],
                    'connect_port': int(line[3]),
                })
        return _result

    @staticmethod
    def port_info_to_table(port_info_list):
        """
        准换为PrettyTable
        :return:
        """
        port_info_table = PrettyTable(
            field_names=['ListenAddress', 'ListenPort', 'ConnectAddress', 'ConnectPort'],
            min_table_width=72,
        )
        for item in port_info_list:
            port_info_table.add_row([v for k, v in item.items()])
        return port_info_table


class WindowsCommandFireWall(WindowsCommandBase):
    """
    防火墙管理
    """

    FIRE_WALL_RULE_OUT = 'Outbound'

    FIRE_WALL_RULE_IN = 'Inbound'

    FIRE_WALL_RULE_ALL = 'ALL'

    WALL_TYPES = [
        FIRE_WALL_RULE_IN,
        FIRE_WALL_RULE_OUT
    ]

    WALL_NAME = 'WSL 2 Firewall Unlock'

    CMD_WALL_ADD = "{power_shell} \"New-NetFireWallRule -DisplayName '{name}' -group '{group}' -Direction '{type}' -LocalPort {port} -Action Allow -Protocol TCP\""

    CMD_WALL_DEL = "{power_shell} \"Remove-NetFireWallRule -DisplayName '{name}'\""

    CMD_WALL_INFO = "{power_shell} \"Get-NetFirewallRule -Group '{group}'\""

    CMD_WALL_RESET = "{power_shell} \"Remove-NetFireWallRule -Group '{group}'\""

    def info_table(self, group=WALL_NAME):
        """
        获取防火墙信息，以 PrettyTable 格式返回
        :param group:
        :return:
        """

        wall_info = self.info(group=group)
        wall_info_table = self.wall_info_to_table(wall_info_list=wall_info)
        return wall_info_table

    def info(self, group=WALL_NAME):
        """
        获取防火墙信息
        :param group:
        :return:
        """

        cmd = self.get_cmd_wall_info(group=group)
        result_string = self.run_cmd(cmd).splitlines()
        return self.wall_info_to_list(wall_info_result=result_string)

    def add(self, port: int):
        """
        添加向防火墙
        :param port:
        :return:
        """
        return self.add_in(port=port) + self.add_out(port=port)

    def add_in(self, port: int):
        """
        添加入方向防火墙
        :param port:
        :return:
        """
        cmd = self.get_cmd_wall_inbound_add(port=port)
        return self.run_cmd(cmd)

    def add_out(self, port: int):
        """
        添加出方向防火墙
        :param port:
        :return:
        """
        cmd = self.get_cmd_wall_outbound_add(port=port)
        return self.run_cmd(cmd)

    def delete(self, port: int):
        """
        删除防火墙
        :param port:
        :return:
        """
        return self.delete_in(port=port) + self.delete_out(port=port)

    def delete_in(self, port: int):
        """
        删除入方向防火墙
        :param port:
        :return:
        """
        cmd = self.get_cmd_wall_inbound_del(port=port)
        return self.run_cmd(cmd)

    def delete_out(self, port: int):
        """
        删除出方向防火墙
        :param port:
        :return:
        """
        cmd = self.get_cmd_wall_outbound_del(port=port)
        return self.run_cmd(cmd)

    def reset(self, group=WALL_NAME):
        """
        清除所有的防火墙
        :param group:
        :return:
        """

        cmd = self.get_cmd_wall_reset(group=group)

        return self.run_cmd(cmd)

    def get_cmd_wall_inbound_add(self, port: int) -> str:
        """
        获取添加入方向防火墙命令字符串
        :param port:
        :return:
        """
        return self.get_cmd_wall_add(port=port, wall_type=self.FIRE_WALL_RULE_IN)

    def get_cmd_wall_outbound_add(self, port: int) -> str:
        """
        获取添加出方向防火墙命令字符串
        :param port:
        :return:
        """
        return self.get_cmd_wall_add(port=port, wall_type=self.FIRE_WALL_RULE_OUT)

    def get_cmd_wall_add(self, port: int, wall_type: str) -> str:
        """
        获取添加防火墙命令字符串
        :param port:
        :param wall_type:
        :return:
        """

        cmd = self.CMD_WALL_ADD.format(
            name='{name} {type} {port}'.format(name=self.WALL_NAME, port=port, type=wall_type),
            port=port,
            type=wall_type,
            group=self.WALL_NAME,
            power_shell=self._power_shell,
        )
        return cmd

    def get_cmd_wall_inbound_del(self, port: int) -> str:
        """
        获取删除入方向防火墙命令字符串
        :param port:
        :return:
        """

        return self.get_cmd_wall_del(port=port, wall_type=self.FIRE_WALL_RULE_IN)

    def get_cmd_wall_outbound_del(self, port: int) -> str:
        """
        获取删除出方向防火墙命令字符串
        :param port:
        :return:
        """

        return self.get_cmd_wall_del(port=port, wall_type=self.FIRE_WALL_RULE_OUT)

    def get_cmd_wall_del(self, port: int, wall_type: str) -> str:
        """
        获取删除防火墙命令字符串
        :param port:
        :param wall_type:
        :return:
        """

        cmd = self.CMD_WALL_DEL.format(
            name='{name} {type} {port}'.format(name=self.WALL_NAME, port=port, type=wall_type),
            power_shell=self._power_shell,
        )

        return cmd

    def get_cmd_wall_reset(self, group=WALL_NAME):
        """
        获取清除所有的防火墙令字符串
        :param group:
        :return:
        """
        cmd = self.CMD_WALL_RESET.format(
            group=group,
            power_shell=self._power_shell,
        )
        return cmd

    def get_cmd_wall_info(self, group=WALL_NAME):
        """
        获取防火墙信息令字符串
        :param group:
        :return:
        """
        cmd = self.CMD_WALL_INFO.format(
            group=group,
            power_shell=self._power_shell,
        )
        return cmd

    @staticmethod
    def wall_info_to_list(wall_info_result):
        _result = {}
        cur_name = None
        for key, line in enumerate(wall_info_result):
            line = line.split(':')
            line = [i.strip() for i in line]
            if len(line) != 2:
                continue
            if line[0] == 'Name':
                cur_name = line[1]
                _line = _result.get(line[1], None)
                if not _line:
                    _result[line[1]] = {}
            if cur_name is not None:
                _result[cur_name][line[0]] = line[1]

        return list([v for k, v in _result.items()])

    @staticmethod
    def wall_info_to_table(wall_info_list):
        wall_info_table = PrettyTable(
            field_names=['DisplayName', 'Direction', 'Action', 'Enabled'],
            min_table_width=70,
        )
        for item in wall_info_list:
            wall_info_table.add_row([
                item.get('DisplayName'),
                item.get('Direction'),
                item.get('Action'),
                item.get('Enabled'),
            ])
        return wall_info_table
