#!/usr/bin/env python3

"""Module containing the ProteinDnaBinding class and the command line interface."""
import argparse
import pandas as pd
import numpy as np
from itertools import product
from sklearn.preprocessing import MinMaxScaler
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_common.command_wrapper import cmd_wrapper
from biobb_ml.utils.common import *

class ProteinDnaBinding():
    """Generates a ProteinDnaBinding from a given dataset.

    Args:
        input_dataset_path (str): Path to the input dataset. File type: input. `Sample file <>`_. Accepted formats: csv.
        input_avg_path (str): Path to the input avg tetramer. File type: input. `Sample file <>`_. Accepted formats: dat.
        input_fce_path (str): Path to the input fce tetramer. File type: input. `Sample file <>`_. Accepted formats: dat.
        input_mgw_path (str): Path to the input mgw rohs. File type: input. `Sample file <>`_. Accepted formats: txt.
        output_dataset_path (str): Path to the output dataset. File type: output. `Sample file <>`_. Accepted formats: csv.
        properties (dic):
            * **model_target** (*str*) - ("tetramers") TODO.
            * **randomize_fce** (*bool*) - (False) TODO.
            * **features_list** (*list*) - (None) List with all features to extract from the input dataset. Values: presence_tetramer, avg, diagonal_fce, mgw, full_fce, onehot_1mer, integer.
            * **score** (*str*) - ("Median_intensity") TODO.
            * **selected_tetramers** (*list*) - (None) TODO.
            * **pbm** (*int*) - (10) TODO. ??????
            * **predict** (*bool*) - (False) Whether or not the output dataset is for predicting or training.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
    """

    def __init__(self, input_dataset_path, input_avg_path, input_fce_path, input_mgw_path,
                 output_dataset_path, properties=None, **kwargs) -> None:
        properties = properties or {}

        # Input/Output files
        self.io_dict = { 
            "in": { "input_dataset_path": input_dataset_path, "input_avg_path": input_avg_path, "input_fce_path": input_fce_path, "input_mgw_path": input_mgw_path }, 
            "out": { "output_dataset_path": output_dataset_path } 
        }

        # Properties specific for BB
        self.model_target = properties.get('model_target', 'tetramers')
        self.randomize_fce = properties.get('randomize_fce', False)
        self.features_list = properties.get('features_list', [])
        self.score = properties.get('score', 'Median_intensity')
        self.selected_tetramers = properties.get('selected_tetramers', [])
        self.pbm = properties.get('pbm', 10)
        self.predict = properties.get('predict', False)
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
        self.io_dict["in"]["input_dataset_path"] = check_input_path(self.io_dict["in"]["input_dataset_path"], "input_dataset_path", out_log, self.__class__.__name__)
        # TODO: CHECK OTHERS INPUTS
        self.io_dict["out"]["output_dataset_path"] = check_output_path(self.io_dict["out"]["output_dataset_path"],"output_dataset_path", False, out_log, self.__class__.__name__)

    @staticmethod
    def onehot_encoding(sequence):
        # define encoding input values
        nucleotides = 'ACGT'
        # define mapping of chars to integers and viceversa
        char_to_int = dict((c, i) for i, c in enumerate(nucleotides))
        # integer encode input data
        integer_encoded = [char_to_int[char] for char in sequence]
        # one hot encode
        onehot_encoded = list()
        for value in integer_encoded:
            letter = [0 for _ in range(len(nucleotides))]
            letter[value] = 1
            onehot_encoded.extend(letter)
        return(np.array(onehot_encoded))

    @staticmethod
    def presence(sequence, k):
        kmers = np.zeros(4**k)
        positions = {''.join(x): n for n, x in enumerate(list(product('ACTG',repeat=k)))}
        for i in range(len(sequence)-k+1):
            kmers[positions[sequence[i:i+k]]] = 1
#             kmers[positions[sequence[i:i+k]]] += 1
        return kmers

    @property
    def scores(self):
        keyw = "VALUE" if self.score == 'Median_intensity' else "Z-score"
        if self.model_target == "octamers":
            vals = self.pbm35[keyw].values
            return MinMaxScaler().fit_transform(vals.reshape(-1,1))
        elif self.model_target == "tetramers":
            mean_scores = self.mean_score()
            vals = np.array([[mean_scores[i][otmer[i:i+4]] for i in self.selected_tetramers] for otmer in self.sequences])
            return MinMaxScaler().fit_transform(vals)

    @staticmethod
    def inv_seq(seq):
        complementary = {"A": "T", "T": "A", "C": "G", "G": "C"}
        return ''.join([complementary[x] for x in seq[::-1]])

    @property
    def features(self):
        avail = {'avg': 'tetra_avg', 'full_fce': 'tetra_fce', 'diagonal_fce': 'tetra_fce_reduced', 'onehot_1mer': 'onehot_1mer', \
                 'integer': 'integer', 'presence_tetramer': 'presence_tetra', 'mgw': 'mgw'}
        return np.hstack([self.__getattribute__(avail[feat]) for feat in self.features_list])

    def mean_score(self):
        """
        generates a list of dictionaries, each containing the position-wise
        score per tetramer
        """
        keyw = "VALUE" if self.score == 'Median_intensity' else "Z-score"
        if self.model_target == "tetramers":
            expt_scores = self.pbm35[keyw].values
            from collections import defaultdict
            position_scores = [defaultdict(lambda: 0) for _ in range(self.p - 3)]
            position_counts = [defaultdict(lambda: 0) for _ in range(self.p - 3)]
            for seq, score in zip(self.sequences, expt_scores):
                for i in range(self.p - 3):
                    position_scores[i][seq[i:i+4]] += score
                    position_counts[i][seq[i:i+4]] += 1
        return [{ttmer: position_scores[i][ttmer]/position_counts[i][ttmer] for ttmer in position_scores[i].keys()} for i in range(self.p - 3)]

    def featurize(self):
        if 'avg' in self.features_list:
            tetra_avg = {line.split()[0] : np.array([float(x) for x in line.split()[1:]])  for line in open(self.io_dict["in"]["input_avg_path"]) if 'SHIFT' not in line}
            self.tetra_avg = np.array([np.concatenate([tetra_avg[otmer[i:i+4]] for i in self.selected_tetramers]) for otmer in self.sequences])
        if 'full_fce' in self.features_list or 'diagonal_fce' in self.features_list:
            tetra_fce = {line.split()[0] : np.array([float(x) for x in line.split()[1:]])  for line in open(self.io_dict["in"]["input_fce_path"]) if 'SHIFT' not in line}
            if self.randomize_fce:
                keys = list(tetra_fce.keys())
                permut_keys = np.random.permutation(keys)
                tetra_fce = {key: tetra_fce[val] for key, val in zip(keys, permut_keys)}
            self.tetra_fce = np.array([np.concatenate([tetra_fce[otmer[i:i+4]] for i in self.selected_tetramers]) for otmer in self.sequences])
        # We might want to scramble the matchings to do 'negative control', i.e., remove all physical information from the dataset
        # Let's also keep track of the reduced matrix
        if 'diagonal_fce' in self.features_list:
            tetra_fce_reduced = {tt: tetra_fce[tt][list(range(0,36,7))] for tt in tetra_fce.keys()}
            self.tetra_fce_reduced = np.array([np.concatenate([tetra_fce_reduced[otmer[i:i+4]] for i in self.selected_tetramers]) for otmer in self.sequences])
        if 'onehot_1mer' in self.features_list:
            #self.onehot_1mer = np.array([self.onehot_encoding(otmer) for otmer in self.sequences]).astype(np.int8)
            self.onehot_1mer = np.array([self.onehot_encoding(otmer) for otmer in self.sequences])
        if 'integer' in self.features_list:
            # define encoding input values
            nucleotides = product('ACGT', repeat=4)
            char_to_int = dict((''.join(c), i) for i, c in enumerate(nucleotides))
            self.integer = np.array([[char_to_int[otmer[i:i+4]] for i in self.selected_tetramers] for otmer in self.sequences]).astype(int)
        if 'presence_tetramer' in self.features_list:
            self.presence_tetra = np.array([self.presence(otmer, 4) for otmer in self.sequences]).astype(np.int8)
        #####
        if 'mgw' in self.features_list:
            self.mgw = {line.split()[0] : [float(x) for x in line.split()[1:]]  for line in open(self.io_dict["in"]["input_mgw_path"]) if 'SHIFT' not in line}
            self.mgw = np.array([np.concatenate([self.mgw[otmer[i:i+4]] for i in self.selected_tetramers]) for otmer in self.sequences])

    @launchlogger
    def launch(self) -> int:
        """Launches the execution of the ProteinDnaBinding module."""

        # Get local loggers from launchlogger decorator
        out_log = getattr(self, 'out_log', None)
        err_log = getattr(self, 'err_log', None)

        # check input/output paths and parameters
        self.check_data_params(out_log, err_log)

        # Check the properties
        fu.check_properties(self, self.properties)

        if self.restart:
            output_file_list = [self.io_dict["out"]["output_dataset_path"]]
            if fu.check_complete_files(output_file_list):
                fu.log('Restart is enabled, this step: %s will the skipped' % self.step, out_log, self.global_log)
                return 0

        # load dataset
        fu.log('Getting dataset from %s' % self.io_dict["in"]["input_dataset_path"], out_log, self.global_log)
        self.pbm35 = pd.read_csv(self.io_dict["in"]["input_dataset_path"], sep="\s+|;|:|,|\t", engine="python")
        
        self.pbm35 = self.pbm35[["ID_REF","VALUE", 'WEIGHT']]
        self.pbm35.columns = ["ID_REF", "VALUE", 'WEIGHT']
        self.pbm35 = self.pbm35.dropna()
        
        inv_seq_data = self.pbm35.copy()
        inv_seq_data["ID_REF"] = inv_seq_data["ID_REF"].apply(self.inv_seq)
        self.pbm35 = pd.concat([self.pbm35, inv_seq_data])
        self.pbm35.reset_index(inplace = True)
        
        #Get list of all kmers for indices purposes
        self.sequences = list(self.pbm35["ID_REF"])
        self.p = len(self.sequences[0])

        #Get list of all tetramers per each octamer in order to get features
        fu.log('Featurizing dataset', out_log, self.global_log)
        self.featurize()

        if self.predict:
            all_cols = self.features
        else: 
            all_cols = np.column_stack((self.features, self.scores, self.pbm35['WEIGHT']))
        
        fu.log('Saving output dataset to %s' % self.io_dict["out"]["output_dataset_path"], out_log, self.global_log)
        np.savetxt(self.io_dict["out"]["output_dataset_path"], all_cols, delimiter=",")

        return 0

def main():
    parser = argparse.ArgumentParser(description="Generates a ProteinDnaBinding from a given dataset", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')

    # Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_dataset_path', required=True, help='Path to the input dataset. Accepted formats: csv.')
    required_args.add_argument('--input_avg_path', required=True, help=' Path to the input avg tetramer. Accepted formats: dat.')
    required_args.add_argument('--input_fce_path', required=True, help='Path to the input fce tetramer. Accepted formats: dat.')
    required_args.add_argument('--input_mgw_path', required=True, help='Path to the input mgw rohs. Accepted formats: txt.')
    required_args.add_argument('--output_dataset_path', required=True, help='Path to the output dataset. Accepted formats: csv.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config).get_prop_dic()

    # Specific call of each building block
    ProteinDnaBinding(input_dataset_path=args.input_dataset_path, input_avg_path=args.input_avg_path, input_fce_path=args.input_fce_path, input_mgw_path=args.input_mgw_path,
                   output_dataset_path=args.output_dataset_path,
                   properties=properties).launch()

if __name__ == '__main__':
    main()

