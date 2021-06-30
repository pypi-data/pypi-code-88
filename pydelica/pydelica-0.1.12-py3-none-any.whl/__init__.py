import logging

import subprocess
import platform
import pandas
from typing import Any, Dict

from pydelica.solutions import SolutionHandler
from pydelica.compiler import Compiler
from pydelica.model import Model
from pydelica.options import SimulationOptions, Solver
from pydelica.logger import OMLogLevel

import pydelica.exception as pde

import glob
import os


class Session:
    def __init__(self, log_level: OMLogLevel = OMLogLevel.NORMAL):
        """Session object which handles model runs.

        This class is used to initiate model runs, building the models and
        allowing the user to set parameter values etc.

        Parameters
        ----------
        log_level : OMLogLevel, optional
            level of Modelica logging, by default OMLogLevel.NORMAL
        """
        self._solutions = {}
        self._model_parameters = {}
        self._simulation_opts = {}
        self._binaries = {}
        self._logger = logging.getLogger("PyDelica")
        if log_level == OMLogLevel.DEBUG:
            self._logger.setLevel(logging.DEBUG)
        self._compiler = Compiler()
        self._log_level = log_level

    def use_library(self, library_name: str, library_version: str = ""):
        self._compiler._library.use_library(library_name, library_version)

    def build_model(
        self,
        modelica_source_file: str,
        model_addr: str = None,
        extra_models: list = [],
        update_input_paths_to: str = "",
    ):
        self._logger.debug(
            "Building model %sfrom file '%s'",
            model_addr + " " if model_addr else "",
            modelica_source_file,
        )
        _binary_loc = self._compiler.compile(modelica_source_file, model_addr, extra_models)
        _xml_files = glob.glob(os.path.join(_binary_loc, "*.xml"))

        if not _xml_files:
            raise pde.ModelicaFileGenerationError(
                "Failed to retrieve XML files from model compilation"
            )

        self._logger.debug("Parsing generated XML files")
        for xml_file in _xml_files:
            _model_name = os.path.basename(xml_file).split("_init")[0]
            self._model_parameters[_model_name] = Model(
                modelica_source_file, xml_file
            )

            _binary = _model_name

            if platform.system() == "Windows":
                _binary += ".exe"

            self._binaries[_model_name] = os.path.join(
                os.path.abspath(_binary_loc), _binary
            )

            if not os.path.exists(self._binaries[_model_name]):
                raise RuntimeError(
                    f"Compilation of model '{_model_name}' failed, "
                    f"no binary '{self._binaries[_model_name]}' found."
                )

            self._logger.debug(
                "Located compiled binary '%s'", self._binaries[_model_name]
            )

            self._solutions[_model_name] = SolutionHandler(
                os.path.abspath(_binary_loc)
            )

            self._logger.debug(
                "Extracting default simulation options for model '%s' from XML file",
                _model_name,
            )

            self._simulation_opts[_model_name] = SimulationOptions(xml_file)

            # Option to update any variable recognised as an input
            # i.e. .mat/.csv to point to the correct location as an
            # absolute path
            if update_input_paths_to:
                self._set_input_files_directory(
                    _model_name, update_input_paths_to
                )

            # Allows easy creation of a Pandas dataframe for displaying solutions
            self._set_output_to_csv()

    def get_binary_location(self, model_name: str):
        if model_name not in self._binaries:
            raise pde.BinaryNotFoundError(
                f"Failed to retrieve binary for model '{model_name}'"
            )
        return self._binaries[model_name]

    def get_parameters(self, model_name: str = None):
        if model_name:
            if model_name not in self._model_parameters:
                raise pde.UnknownModelError(model_name)

            return self._model_parameters[model_name]
        else:
            _out_params = {}
            for model in self._model_parameters:
                for param in self._model_parameters[model]:
                    if param in _out_params:
                        continue
                    _out_params[param] = self._model_parameters[model][param]
        return _out_params

    def get_parameter(self, param_name: str) -> Any:
        for model in self._model_parameters:
            if param_name in self._model_parameters[model]:
                if isinstance(
                    self._model_parameters[model].get_parameter(param_name),
                    dict,
                ):
                    raise AssertionError(
                        "Expected non-mutable value for requested parameter"
                        f"'{param_name}' but got type 'dict'"
                    )
                return self._model_parameters[model].get_parameter(param_name)
        raise pde.UnknownParameterError(param_name)

    def get_simulation_options(self, model_name: str = None) -> Dict[str, Any]:
        """Retrieve Dictionary of the Simulation Options

        Parameters
        ----------
        model_name : str
            name of model to get simulation options for

        Returns
        -------
        Dict[str, Any]
            dictionary containing all simulation options

        Raises
        ------
        KeyError
            if the given model name is not recognised
        """
        if not model_name:
            model_name = list(self._binaries.keys())[0]
        if not model_name in self._simulation_opts:
            raise pde.UnknownModelError(model_name)
        return self._simulation_opts[model_name]

    def get_simulation_option(
        self, option: str, model_name: str = None
    ) -> Any:
        """Retrieve a single option for a given model.

        Parameters
        ----------
        option : str
            option to search for
        model_name : str, optional
            name of modelica model

        Returns
        -------
        Any
            value for the given option

        Raises
        ------
        KeyError
            if the given model is not recognised
        KeyError
            if the given option name is not recognised
        """
        if not model_name:
            return self._simulation_opts[list(self._binaries.keys())[0]][
                option
            ]
        else:
            return self._simulation_opts[model_name][option]

    def set_parameter(self, param_name: str, value: Any):
        if isinstance(value, dict):
            raise TypeError(
                "Cannot assign a value of type dictionary as a parameter value"
                f" for parameter '{param_name}'"
            )
        self._logger.debug(
            "Searching for parameter '%s' and assigning new value"
        )
        for model in self._model_parameters:
            if param_name in self._model_parameters[model]:
                self._model_parameters[model].set_parameter(param_name, value)
                return
        raise pde.UnknownParameterError(param_name)

    def _set_input_files_directory(
        self, model_name: str, input_dir: str = None
    ):
        if not input_dir:
            input_dir = os.path.dirname(
                self._model_parameters[model_name].get_source_path()
            )

        for param, value in self._model_parameters[model_name].items():
            if not value["value"]:
                continue

            _has_addr_elem = any(
                i in value["value"]
                for i in [os.path.sep, ".mat", ".csv"]
                if value["type"] == str
            )

            if value["type"] == str and _has_addr_elem:
                _addr = os.path.join(input_dir, value["value"])
                self._model_parameters[model_name].set_parameter(param, _addr)

    def simulate(self, model_name: str = None, verbosity=None):
        if not model_name:
            model_name = list(self._binaries.keys())[0]
            self._logger.warning(
                "No model name specified, using first result '%s'", model_name
            )
        if model_name not in self._binaries:
            raise pde.BinaryNotFoundError(
                f"Could not find binary for Model '{model_name}',"
                " did you run 'build_models' on the source file?"
            )

        self._logger.debug("Launching simulation for model '%s'", model_name)

        # Write parameters to the XML file read by the binary
        self._model_parameters[model_name].write_params()

        _current_dir = os.getcwd()
        _binary_dir = os.path.dirname(self._binaries[model_name])
        os.chdir(_binary_dir)

        _args = [
            os.path.join(".", os.path.basename(self._binaries[model_name]))
        ]

        if not os.path.exists(self._binaries[model_name]):
            raise pde.BinaryNotFoundError(
                f"Failed to retrieve binary for model '{model_name}' "
                f"from location '{_binary_dir}'"
            )

        if verbosity and verbosity.value:
            _args += [verbosity.value]
        elif self._log_level.value:
            _args += [self._log_level.value]

        _run_sim = subprocess.run(
            _args,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True,
            shell=False,
        )
        print(_run_sim.stdout)
        pde.parse_error_string_simulate(_run_sim.stdout, _run_sim.stderr)
        os.chdir(_current_dir)
        self._solutions[model_name].retrieve_session_solutions()

    def _set_output_to_csv(self):
        for model in self._simulation_opts:
            self._simulation_opts[model].set_option("outputFormat", "csv")

    def set_solver(self, solver: Solver, model_name: str = None):
        if model_name:
            self._simulation_opts[model_name].set_option(
                "solver", solver.value
            )
        else:
            for model in self._simulation_opts:
                self._simulation_opts[model].set_option("solver", solver.value)

    def set_time_range(
        self,
        start_time: int = None,
        stop_time: int = None,
        model_name: str = None,
    ):
        if model_name:
            if start_time:
                self._simulation_opts[model_name].set_option(
                    "startTime", start_time
                )
            if stop_time:
                self._simulation_opts[model_name].set_option(
                    "stopTime", stop_time
                )
        else:
            for model in self._simulation_opts:
                if start_time:
                    self._simulation_opts[model].set_option(
                        "startTime", start_time
                    )
                if stop_time:
                    self._simulation_opts[model].set_option(
                        "stopTime", stop_time
                    )

    def set_tolerance(self, tolerance: float, model_name: str = None):
        if model_name:
            self._simulation_opts[model_name].set_option(
                "tolerance", tolerance
            )
        else:
            for model in self._simulation_opts:
                self._simulation_opts[model].set_option("tolerance", tolerance)

    def set_variable_filter(self, filter_str: str, model_name: str = None):
        if model_name:
            self._simulation_opts[model_name].set_option(
                "variableFilter", filter_str
            )
        else:
            for model in self._simulation_opts:
                self._simulation_opts[model].set_option(
                    "variableFilter", filter_str
                )

    def set_simulation_option(
        self, option_name: str, value: Any, model_name: str = None
    ):
        if model_name:
            self._simulation_opts[model_name].set_option(option_name, value)
        else:
            for model in self._simulation_opts:
                self._simulation_opts[model].set_option(option_name, value)

    def get_solutions(self) -> pandas.DataFrame:
        """Returns solutions to all simulated models as a dictionary of dataframes

        Outputs are written as Pandas dataframes the columns of which can be
        accessed by variable name.

        Returns
        -------
        Dict
            dictionary containing outputs to all simulated models as Pandas
            dataframes

        Raises
        ------
        pde.BinaryNotFoundError
            if no models have been compiled
        """
        if not self._binaries:
            raise pde.BinaryNotFoundError(
                "Cannot retrieve solutions, you need to compile and"
                " run one or more models first"
            )

        # The SolutionHandler class takes into account the case of multiple
        # output files, however with OM there is only ever a single file per
        # model so we only need to retrieve the first one

        return {
            model: self._solutions[model].get_solutions()[
                list(self._solutions[model].get_solutions().keys())[0]
            ]
            for model in self._solutions
        }
