from pydelica.exception import ResultRetrievalError
import pandas as pd
import os
import logging
import glob


class SolutionHandler:
    def __init__(self, session_directory: str):
        self._logger = logging.getLogger("PyDelica.Solutions")
        self._session_dir = session_directory
        self._solutions = {}

    def retrieve_session_solutions(self):
        _has_csv = glob.glob(os.path.join(self._session_dir, "*.csv"))

        if not _has_csv:
            raise ResultRetrievalError

        for out_file in _has_csv:
            if not "_res" in out_file:
                continue
            self._logger.debug(
                "Reading results from output file '%s'", out_file
            )
            _key = out_file.split("_res")[0]
            self._solutions[_key] = pd.read_csv(_has_csv[0])
        return self._solutions

    def get_solutions(self):
        return self._solutions
