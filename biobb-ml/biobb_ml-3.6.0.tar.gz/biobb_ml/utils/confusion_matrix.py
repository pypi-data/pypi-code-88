#!/usr/bin/env python3

"""Module containing the ConfusionMatrix class and the command line interface."""
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn import linear_model
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import ensemble
from sklearn import svm
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_common.command_wrapper import cmd_wrapper
from biobb_ml.utils.common import *


class ConfusionMatrix():
    """Generates a confusion matrix from a given model.

    Args:
        input_model_path (str): Path to the input model. File type: input. `Sample file <>`_. Accepted formats: pkl.
        output_plot_path (str): Path to the confusion matrix plot. File type: output. `Sample file <>`_. Accepted formats: png.
        properties (dic):
            * **normalize_cm** (*bool*) - (False) Whether or not to normalize the confusion matrix.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
    """

    def __init__(self, input_model_path,
                 output_plot_path, properties=None, **kwargs) -> None:
        properties = properties or {}

        # Input/Output files
        self.io_dict = { 
            "in": { "input_model_path": input_model_path }, 
            "out": { "output_plot_path": output_plot_path } 
        }

        # Properties specific for BB
        self.normalize_cm = properties.get('normalize_cm', False)
        self.properties = properties

        # Properties common in all BB
        self.can_write_console_log = properties.get('can_write_console_log', True)
        self.global_log = properties.get('global_log', None)
        self.prefix = properties.get('prefix', None)
        self.step = properties.get('step', None)
        self.path = properties.get('path', '')
        self.remove_tmp = properties.get('remove_tmp', True)
        self.restart = properties.get('restart', False)

    def check_data_params(self, out_log, err_log):
        """ Checks all the input/output paths and parameters """
        self.io_dict["in"]["input_model_path"] = check_input_path(self.io_dict["in"]["input_model_path"], "input_model_path", out_log, self.__class__.__name__)
        self.io_dict["out"]["output_plot_path"] = check_output_path(self.io_dict["out"]["output_plot_path"],"output_plot_path", False, out_log, self.__class__.__name__)

    @launchlogger
    def launch(self) -> int:
        """Launches the execution of the ConfusionMatrix module."""

        # Get local loggers from launchlogger decorator
        out_log = getattr(self, 'out_log', None)
        err_log = getattr(self, 'err_log', None)

        # check input/output paths and parameters
        self.check_data_params(out_log, err_log)

        # Check the properties
        fu.check_properties(self, self.properties)

        if self.restart:
            output_file_list = [self.io_dict["out"]["output_plot_path"]]
            if fu.check_complete_files(output_file_list):
                fu.log('Restart is enabled, this step: %s will the skipped' % self.step, out_log, self.global_log)
                return 0

        fu.log('Getting model from %s' % self.io_dict["in"]["input_model_path"], out_log, self.global_log)

        with open(self.io_dict["in"]["input_model_path"], "rb") as f:
            while True:
                try:
                    m = joblib.load(f)
                    if (isinstance(m, linear_model.LogisticRegression)
                        or isinstance(m, KNeighborsClassifier)
                        or isinstance(m, DecisionTreeClassifier)
                        or isinstance(m, ensemble.RandomForestClassifier)
                        or isinstance(m, svm.SVC)):
                        new_model = m
                    if isinstance(m, StandardScaler):
                        scaler = m
                    if isinstance(m, dict):
                        variables = m
                except EOFError:
                    break

        """new_data = scaler.transform(new_data_table)
        p = new_model.predict_proba(new_data)"""

        print(new_model)
        print(scaler)
        print(variables)

        # load dataset
        """fu.log('Getting dataset from %s' % self.io_dict["in"]["input_dataset_path"], out_log, self.global_log)
        data = pd.read_csv(self.io_dict["in"]["input_dataset_path"])

        if self.features: data = data.filter(self.features)

        fu.log('Generating dendrogram', out_log, self.global_log)

        sns.clustermap(data, cmap='Blues')

        plt.savefig(self.io_dict["out"]["output_plot_path"], dpi=150)
        fu.log('Saving ConfusionMatrix Plot to %s' % self.io_dict["out"]["output_plot_path"], out_log, self.global_log)"""

        return 0

def main():
    parser = argparse.ArgumentParser(description="Generates a dendrogram from a given dataset", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')

    # Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_model_path', required=True, help='Path to the input model. Accepted formats: pkl.')
    required_args.add_argument('--output_plot_path', required=True, help='Path to the dendrogram plot. Accepted formats: png.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config).get_prop_dic()

    # Specific call of each building block
    ConfusionMatrix(input_model_path=args.input_model_path,
                   output_plot_path=args.output_plot_path,
                   properties=properties).launch()

if __name__ == '__main__':
    main()

