import logging
import os
import re
import shutil
import stat
import sys
import tempfile
from datetime import datetime

import colorama

import urllib.request
from typing import List, Iterable, Tuple, Any, Callable, Optional

from semantic_version import Version

import configparser
import pmakeup as pm


class CorePMakeupPlugin(pm.AbstractPmakeupPlugin):
    """
    Contains all the commands available for the user in a PMakeupfile.py file
    """

    def _setup_plugin(self):
        pass

    def _teardown_plugin(self):
        pass

    def _get_dependencies(self) -> Iterable[type]:
        return []

    @pm.register_command.add("core")
    def require_pmakeup_plugins(self, *pmakeup_plugin_names: str):
        """Tells pmakeup that, in order to run the script, you required a sequence of pmakeup plugins correctly
        installed (the version does not matter)

        Pmakeup will then arrange itself in installing dependencies and the correct order of the plugins

        :param pmakeup_plugin_names: the plugins that are requierd to be present in order for the script to work.
            Dependencies are automatically added
        """
        # TODO implement
        raise NotImplementedError()

    @pm.register_command.add("core")
    def vars(self) -> "pm.AttrDict":
        """
        Get a dictioanry containing all the variables setup up to this point.
        You can use thi dictionary to gain access to a variable in a more pythonic way (e.g., vars.foo rather
        than get_variable("foo")

        :raises PMakeupException: if the variable is not found
        """
        return self._model._eval_globals.variables

    @pm.register_command.add("core")
    def log_command(self, message: str):
        """
        reserved. Useful to log the action performed by the user

        :param message: message to log
        """

        if not self.get_variable_or_set_it("disable_log_command", False):
            logging.info(message)

    @pm.register_command.add("core")
    def get_all_registered_plugins(self) -> Iterable[str]:
        """
        get all the registered pmakeup plugins at this moment
        """
        return map(lambda p: p.get_plugin_name(), self.get_plugins())

    @pm.register_command.add("core")
    def get_all_available_command_names(self) -> Iterable[str]:
        """
        Get all the commands you can execute right now
        """
        yield from self._model._eval_globals

    @pm.register_command.add("core")
    def get_latest_path_with_architecture(self, current_path: str, architecture: int) -> pm.path:
        """
        get the latest path on the system with the specified archietcture

        :param current_path: nominal path name
        :param architecture: either 32 or 64
        :return: the first path compliant with this path name
        """
        max_x = None
        for x in filter(lambda x: x.architecture == architecture, self._model._eval_globals.pmakeup_interesting_paths[current_path]):
            if max_x is None:
                max_x = x
            elif x.version > max_x.version:
                max_x = x

        return max_x.path

    @pm.register_command.add("core")
    def ensure_condition(self, condition: Callable[[], bool], message: str = "") -> None:
        """
        Perform a check. If the condition is **not** satisfied, we raise exception

        :param condition: the condition to check. generate exception if the result is False
        :param message: the message to show if the exception needs to be generated
        """

        if not condition():
            raise pm.AssertionPMakeupException(f"pmakeup needs to generate a custom exception: {message}")

    @pm.register_command.add("core")
    def ensure_has_variable(self, name: str) -> None:
        """
        Ensure the user has passed a variable in the registry.
        If not, an exception is generated

        :param name: the variable name to check

        """
        return self.ensure_condition(
            lambda: name in self.get_shared_variables(),
            message=f"""No variable in registry named "{name}"."""
        )

    @pm.register_command.add("core")
    def ensure_has_cli_variable(self, name: str) -> None:
        """
        Ensure the user has passed a variable via "--variable" CLI utils.
        If not, an exception is generated

        :param name: the variable name to check

        """
        self.log_command(f"Checking if the user has passed the variable from CLI \"{name}\"...")
        return self.ensure_condition(
            lambda: name in self.get_registry().pmakeup_cli_variables,
            message=f"""No variable passed with "--variable" named "{name}"."""
        )

    @pm.register_command.add("core")
    def ensure_has_cli_variable_is_one_of(self, name: str, *allowed_values) -> None:
        """
        Ensure that a variable has been passed from the command line and has a value among the one passed

        :param name: variable name
        :param allowed_values: set of values we check against the variable calue
        """
        self.log_command(f"Checking if the variable passed by the user from CLI \"{name}\" has one of the values {', '.join(map(str, allowed_values))}...")
        self.ensure_condition(
            lambda: name in self.get_registry().pmakeup_cli_variables,
            message=f"""No variable passed with "--variable" named "{name}"."""
        )
        val = self.get_registry().pmakeup_cli_variables[name]
        self.ensure_condition(
            lambda: val in allowed_values,
            message=f"""variable {name} (with value {val}) passed with "--variable" has not a value among {', '.join(map(str, allowed_values))}."""
        )



    @pm.register_command.add("core")
    def semantic_version_2_only_core(self, filename: str) -> Version:
        """
        A function that can be used within ::get_latest_version_in_folder

        :param filename: the absolute path of a file that contains a version
        :return: the version
        """
        regex = r"\d+\.\d+\.\d+"
        b = os.path.basename(filename)
        m = re.search(regex, b)
        logging.debug(f"checking if \"{filename}\" satisfies \"{regex}\"")
        if m is None:
            raise pm.PMakeupException(f"Cannot find the regex {regex} within file \"{b}\"!")
        logging.debug(f"yes: \"{m.group(0)}\"")
        return Version(m.group(0))

    @pm.register_command.add("core")
    def quasi_semantic_version_2_only_core(self, filename: str) -> Version:
        """
        A function that can be used within ::get_latest_version_in_folder.
        It accepts values like "1.0.0", but also "1.0" and "1"

        :param filename: the absolute path of a file that contains a version
        :return: the version
        """
        regex = r"\d+(?:\.\d+(?:\.\d+)?)?"
        b = os.path.basename(filename)
        m = re.search(regex, b)
        if m is None:
            raise pm.PMakeupException(f"Cannot find the regex {regex} within file \"{b}\"!")
        result = m.group(0)
        if len(result.split(".")) == 2:
            result += ".0"
        if len(result.split(".")) == 1:
            result += ".0.0"
        return Version(result)

    @pm.register_command.add("core")
    def get_latest_version_in_folder(self, folder: pm.path = None, should_consider: Callable[[pm.path], bool] = None, version_fetcher: Callable[[str], Version] = None) -> Tuple[Version, List[pm.path]]:
        """
        Scan the subfiles and subfolder of a given directory. We assume each file or folder has a version withint it.
        Then fetches the latest version.
        This command is useful in dierctories where all releases of a given software are placed. if we need to fetch
        the latest one,
        this function is perfect for the task.

        :param folder: the folder to consider. If unspecified, it is the current working directory
        :param should_consider: a function that allows you to determine if we need to consider or
            not a subfile/subfolder. The input isan absolute path. If no function is given, we accept all the
            sub files
        :param version_fetcher: a function that extract a version from the filename. If left unspecified, we will
            use ::semantic_version_2_only_core
        :return: the latest version in the folder. The second element of the tuple is a collection of all the filenames
            that specify the latest version
        """

        def default_should_consider(x) -> bool:
            return True

        if folder is None:
            folder = self.get_cwd()
        if should_consider is None:
            should_consider = default_should_consider
        if version_fetcher is None:
            version_fetcher = self.quasi_semantic_version_2_only_core
        p = self.paths.abs_path(folder)

        result_version = None
        result_list = []
        for file in self.platform.ls(p, generate_absolute_path=True):
            logging.debug(f"Shuld we consider {file} for fetching the latest version?")
            if not should_consider(file):
                continue
            # find the version
            v = version_fetcher(file)
            logging.debug(f"fetched version {v}. Latest version detected up until now is {result_version}")
            if result_version is None:
                result_version = v
                result_list = [file]
                logging.debug(f"update version with {result_version}. Files are {' '.join(result_list)}")
            elif v > result_version:
                result_version = v
                result_list = [file]
                logging.debug(f"update version with {result_version}. Files are {' '.join(result_list)}")
            elif v == result_version:
                result_list.append(file)
                logging.debug(f"update version with {result_version}. Files are {' '.join(result_list)}")

        return result_version, result_list

    def _truncate_string(self, string: str, width: int, ndots: int = 3) -> str:
        if len(string) > (width - ndots):
            return string[:(width-ndots)] + "."*ndots
        else:
            return string

    @pm.register_command.add("core")
    def get_starting_cwd(self) -> pm.path:
        """
        :return: absolute path of where you have called pmakeup
        """
        return self._model.starting_cwd

    @pm.register_command.add("core")
    def path_wrt_starting_cwd(self, *folder: str) -> pm.path:
        """
        Compute path relative to the starting cwd

        :param folder: other sections of the path
        :return: path relative to the absolute path of where you have called pmakeup
        """
        return os.path.abspath(os.path.join(self._model.starting_cwd, *folder))

    @pm.register_command.add("core")
    def get_pmakeupfile_path(self) -> pm.path:
        """
        :return: absolute path of the main PMakeupfile path
        """
        return self._model.input_file

    @pm.register_command.add("core")
    def get_pmakeupfile_dir(self) -> pm.path:
        """
        The directory where the analyzed pmakeupfile is located

        :return: absolute ptha of the directory of the path under analysis
        """
        return os.path.dirname(self._model.input_file)

    @pm.register_command.add("core")
    def path_wrt_pmakeupfile(self, *folder: str) -> pm.path:
        """
        Compute path relative to the file where PMakeupfile is located

        :param folder: other sections of the path
        :return: path relative to the absolute path of where PMakeupfile is located
        """
        return os.path.abspath(os.path.join(os.path.dirname(self._model.input_file), *folder))

    @pm.register_command.add("core")
    def get_pmakeupfile_dirpath(self) -> pm.path:
        """
        :return: absolute path of the folder containing the main PMakeupfile path
        """
        return os.path.dirname(self._model.input_file)

    @pm.register_command.add("core")
    def require_pmakeup_version(self, lowerbound: str) -> None:
        """
        Check if the current version of pmakeup is greater or equal than the given one.
        If the current version of pmakeup is not compliant with this constraint, an error is generated

        :param lowerbound: the minimum version this script is compliant with
        """
        system_version = Version(pm.version.VERSION)
        script_version = Version(lowerbound)
        self._log_command(f"Checking if script minimum pmakeup version {script_version} >= {system_version}")
        if script_version > system_version:
            raise pm.PMakeupException(f"The script requires at least version {script_version} to be installed. Current version is {system_version}")

    @pm.register_command.add("core")
    def get_command_line_string(self) -> str:
        """
        Get the command line string from the user

        :return: argv
        """
        return " ".join(sys.argv)

    @pm.register_command.add("core")
    def read_variables_from_properties(self, file: pm.path, encoding: str = "utf-8") -> None:
        """
        Read a set of easy variables from a property file. All the read variables will be available in the "variables"
        value. If some variable name preexists, it will not be overriden
        :see: https://docs.oracle.com/cd/E23095_01/Platform.93/ATGProgGuide/html/s0204propertiesfileformat01.html

        :param file: the file to read
        :param encoding: encoding of the file. If left missing, we will use utf-8
        """

        p = self.paths.abs_path(file)
        self._log_command(f"Reading variables from property file {p}")
        config = configparser.ConfigParser()
        # see https://stackoverflow.com/a/19359720/1887602
        config.optionxform = str
        with open(p, "r", encoding=encoding) as f:
            config.read_string("[config]\n" + f.read())

        for k, v in config["config"].items():
            if k in self.get_shared_variables():
                logging.warning(f"Ignoring variable \"{k}\" from file {p}, since it alrady exist within the ambient")
                continue
            self._log_command(f"Adding variable \"{k}\" to {v}")
            self.get_shared_variables()[k] = v

    @pm.register_command.add("core")
    def include_string(self, string: str) -> None:
        """
        Include and execute the code within the given string

        :param string: the commands to execute
        """
        self._log_command(f"Include and execute string \"{string}\"")
        self._model.execute_string(string)

    @pm.register_command.add("core")
    def include_file(self, *file: pm.path) -> None:
        """
        Replace the include directive with the content fo the included file. Fails if there is no such path

        :param file: the external file to include in the script
        """

        p = self.paths.abs_path(*file)
        self._log_command(f"include file content \"{p}\"")
        self._model.execute_file(p)

    @pm.register_command.add("core")
    def get_variable(self, name: str) -> Any:
        """
        Ensure the user has passed a variable.
        If not, raises an exception

        :param name: the variable name to check
        :raises PMakeupException: if the variable is not found
        """
        if name not in self.get_shared_variables():
            raise pm.PMakeupException(f"Variable {name} not found")
        return self.get_shared_variables()[name]

    @pm.register_command.add("core")
    def set_variable(self, name: str, value: Any) -> None:
        """
        Set the variable in the current model. If the variable did not exist, we create one one.
        Otherwise, the value is overridden

        :param name: name of the variable to programmatically set
        :param value: value to set
        """
        self.get_shared_variables()[name] = value


CorePMakeupPlugin.autoregister()
