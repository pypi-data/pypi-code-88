#   Copyright  2020 Atos Spain SA. All rights reserved.
 
#   This file is part of EASIER AI.
 
#   EASIER AI is free software: you can redistribute it and/or modify it under the terms of Apache License, either version 2 of the License, or
#   (at your option) any later version.
 
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT ANY WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING 
#   BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT,
#   IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#   WHETHER IN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE 
#   OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#   See  LICENSE file for full license information  in the project root.

import sys
sys.path.append('..')
sys.path.append('.')

import time
import json
import numpy

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.integer):
            return int(obj)
        elif isinstance(obj, numpy.floating):
            return float(obj)
        elif isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

class TrainingMetadata():
    """Class to store the training's metadata information.
    """

    inference_mode = ''
    optimizer = ''
    loss = ''
    epochs = 100
    batch_size = 10
    metrics = []
    

    def __init__(self, f:dict=None):
        """Constructor for the Training Metadata Class.

        Args:
            f (dict, optional): Dictionary with the Training's metadata information.
        """
        if f is not None:
            if 'inference_mode' in f: self.inference_mode = f['inference_mode']
            if 'optimizer' in f: self.optimizer = f['optimizer']
            if 'loss' in f: self.loss = f['loss']
            if 'epochs' in f: self.epochs = f['epochs']
            if 'batch_size' in f: self.batch_size = f['batch_size']
            if 'metrics' in f: self.metrics = f['metrics']
        else:
            pass

    # def seria
    def pretty_print(self):
        """Print the training metadata information.
        """
        row_format ="{:<30}" * 2
        print(row_format.format(*['Inference Mode:', self.inference_mode]))
        print(row_format.format(*['Optimizer:', self.optimizer]))
        print(row_format.format(*['Loss function:', self.loss]))
        print(row_format.format(*['Epochs:', self.epochs]))
        print(row_format.format(*['Batch size:', str(self.batch_size)]))
        print(row_format.format(*['Metrics:', str(self.metrics)]))
        
    def dump_to_file(self, path:str):
        """Dump metadata information to a file.

        Args:
            path (str): Path to store the file with the metadata information.
        """
        with open(path+'/training_metadata.json', 'w') as f:
            f.write(json.dumps(self.__dict__, default=lambda o: str(o.value), 
                sort_keys=True, indent=4, cls=NumpyEncoder))

