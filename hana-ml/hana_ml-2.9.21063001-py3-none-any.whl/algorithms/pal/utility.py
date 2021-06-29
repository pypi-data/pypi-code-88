"""
This module contains Python API of utility functions.
"""
from collections import defaultdict
try:
    import configparser
except ImportError:
    import ConfigParser as configparser
import logging

#pylint: disable=bare-except, line-too-long, invalid-name

def version_compare(pkg_version, version):
    """
    If pkg's version is greater than the specified version, it returns True. Otherwise, it returns False.
    """
    pkg_ver_list = pkg_version.split(".")
    ver_list = version.split(".")
    if int(pkg_ver_list[0]) > int(ver_list[0]):
        return True
    if int(pkg_ver_list[0]) == int(ver_list[0]):
        if int(pkg_ver_list[1]) > int(ver_list[1]):
            return True
        if int(pkg_ver_list[1]) == int(ver_list[1]):
            if int(pkg_ver_list[2]) >= int(ver_list[2]):
                return True
    return False

class Settings:
    """
    Configuration of logging level
    """
    settings = None
    user = None
    @staticmethod
    def load_config(config_file):
        """
        Load HANA credentials.
        """
        Settings.settings = configparser.ConfigParser()
        Settings.settings.read(config_file)
        try:
            url = Settings.settings.get("hana", "url")
        except:
            url = ""
        try:
            port = Settings.settings.getint("hana", "port")
        except:
            port = 0
        try:
            pwd = Settings.settings.get("hana", "passwd")
        except:
            pwd = ''
        try:
            Settings.user = Settings.settings.get("hana", "user")
        except:
            Settings.user = ""
        Settings._init_logger()
        return url, port, Settings.user, pwd

    @staticmethod
    def _set_log_level(logger, level):
        if level == 'info':
            logger.setLevel(logging.INFO)
        else:
            if level == 'warn':
                logger.setLevel(logging.WARN)
            else:
                if level == 'debug':
                    logger.setLevel(logging.DEBUG)
                else:
                    logger.setLevel(logging.ERROR)

    @staticmethod
    def _init_logger():
        logging.basicConfig()
        for module in ["hana_ml.ml_base", 'hana_ml.dataframe', 'hana_ml.algorithms.pal']:
            try:
                level = Settings.settings.get("logging", module)
            except:
                level = "error"
            logger = logging.getLogger(module)
            Settings._set_log_level(logger, level.lower())

    @staticmethod
    def set_log_level(level='info'):
        """
        Set logging level.

        Parameters
        ----------

        level : {'info', 'warn', 'debug', 'error'}
        """
        logging.basicConfig()
        for module in ["hana_ml.ml_base", 'hana_ml.dataframe', 'hana_ml.algorithms.pal']:
            logger = logging.getLogger(module)
            Settings._set_log_level(logger, level)

def _toposort(edges):
    """
    Topologysort to compute pipeline. For Python 3.9, graphlib.TopologicalSorter can replace this function.
    """
    def _toposort_recur(graph, v, visited, stack):
        visited[v] = True
        for i in graph[v]:
            if visited[i] is False:
                _toposort_recur(graph, i, visited, stack)
        stack.insert(0, v)

    graph = defaultdict(list)
    nodes = set()
    for edge in edges:
        graph[edge[0]].append(edge[1])
        nodes.add(edge[0])
        nodes.add(edge[1])
    visited = {}
    for i in nodes:
        visited[i] = False
    stack = []
    for i in nodes:
        if visited[i] is False:
            _toposort_recur(graph, i, visited, stack)
    return stack
