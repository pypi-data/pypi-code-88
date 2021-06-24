from functools import wraps

from .util import Color, get_fire_wall_rule_args
from .windows_command import WindowsCommandPort, WindowsCommandFireWall, WindowsCommandLinux


def __print_port_info(namespace, parser, *args, **kwargs):
    """
    输出端口转发信息到控制台
    :param args:
    :param kwargs:
    :return:
    """

    port_info_table = WindowsCommandPort(
        encoding=namespace.encoding,
        power_shell=namespace.power_shell
    ).info_table()
    print(Color.cyan('Ports Info:'))
    print(Color.green(port_info_table))


def __print_wall_info(namespace, parser, *args, **kwargs):
    """
    输出防火墙信息到控制台
    :param args:
    :param kwargs:
    :return:
    """

    wall_info_table = WindowsCommandFireWall(
        encoding=namespace.encoding,
        power_shell=namespace.power_shell
    ).info_table()
    print(Color.cyan('NetFireWallRules Info:'))
    print(Color.green(wall_info_table))


def __reset_wall(namespace, parser, *args, **kwargs):
    """
    重置防火墙
    :param namespace:
    :param parser:
    :param args:
    :param kwargs:
    :return:
    """
    namespace.wall = get_fire_wall_rule_args(namespace.wall)
    if namespace.wall is not None:
        WindowsCommandFireWall(
            encoding=namespace.encoding,
            power_shell=namespace.power_shell
        ).reset()


def __add_wall(namespace, parser, *args, **kwargs):
    """
    添加防火墙
    :param namespace:
    :param parser:
    :param args:
    :param kwargs:
    :return:
    """

    namespace.port = list(set(namespace.port))
    namespace.wall = get_fire_wall_rule_args(namespace.wall)
    if namespace.wall is not None:
        windows_command_fire_wall = WindowsCommandFireWall(
            encoding=namespace.encoding,
            power_shell=namespace.power_shell
        )
        if windows_command_fire_wall.FIRE_WALL_RULE_OUT in namespace.wall:
            return list(map(lambda port: windows_command_fire_wall.add_out(port=port), namespace.port))
        elif windows_command_fire_wall.FIRE_WALL_RULE_IN in namespace.wall:
            return list(map(lambda port: windows_command_fire_wall.add_in(port=port), namespace.port))
        else:
            return list(map(lambda port: windows_command_fire_wall.add(port=port), namespace.port))


def __del_wall(namespace, parser, *args, **kwargs):
    """
    删除防火墙
    :param namespace:
    :param parser:
    :param args:
    :param kwargs:
    :return:
    """

    namespace.port = list(set(namespace.port))
    namespace.wall = get_fire_wall_rule_args(namespace.wall)
    if namespace.wall is not None:
        windows_command_fire_wall = WindowsCommandFireWall(
            encoding=namespace.encoding,
            power_shell=namespace.power_shell
        )
        if windows_command_fire_wall.FIRE_WALL_RULE_OUT in namespace.wall:
            return list(map(lambda port: windows_command_fire_wall.delete_out(port=port), namespace.port))
        elif windows_command_fire_wall.FIRE_WALL_RULE_IN in namespace.wall:
            return list(map(lambda port: windows_command_fire_wall.delete_in(port=port), namespace.port))
        else:
            return list(map(lambda port: windows_command_fire_wall.delete(port=port), namespace.port))


def __print_wsl_info(namespace, parser, *args, **kwargs):
    """
    输出子系统信息到控制台
    :param args:
    :param kwargs:
    :return:
    """

    wsl_info_table = WindowsCommandLinux(
        encoding=namespace.encoding,
        power_shell=namespace.power_shell
    ).info_table()
    print(Color.cyan('WSL2 Info:'))
    print(Color.green(wsl_info_table))


def print_wsl_info(func):
    """
    输出端口转发信息到控制台
    :param func:
    :return:
    """

    @wraps(func)
    def __wraps(*args, **kwargs):
        _result = func(*args, **kwargs)
        __print_wsl_info(**kwargs)
        return _result

    return __wraps


def print_port_info(func):
    """
    输出端口转发信息到控制台
    :param func:
    :return:
    """

    @wraps(func)
    def __wraps(*args, **kwargs):
        _result = func(*args, **kwargs)
        __print_port_info(**kwargs)
        return _result

    return __wraps


def print_wall_info(func):
    """
    输出防火墙信息到控制台
    :param func:
    :return:
    """

    @wraps(func)
    def __wraps(*args, **kwargs):
        _result = func(*args, **kwargs)
        __print_wall_info(**kwargs)
        return _result

    return __wraps


def wall_reset(func):
    """
    重置防火墙
    :param func:
    :return:
    """

    @wraps(func)
    def __wraps(*args, **kwargs):
        _result = func(*args, **kwargs)
        __reset_wall(**kwargs)
        return _result

    return __wraps


def wall_add(func):
    """
    添加防火墙
    :param func:
    :return:
    """

    @wraps(func)
    def __wraps(*args, **kwargs):
        _result = func(*args, **kwargs)
        __add_wall(**kwargs)
        return _result

    return __wraps


def wall_del(func):
    """
    删除防火墙
    :param func:
    :return:
    """

    @wraps(func)
    def __wraps(*args, **kwargs):
        _result = func(*args, **kwargs)
        __del_wall(**kwargs)
        return _result

    return __wraps
