#!/usr/bin/env python
# ******************************************************************************
# Copyright 2020 Brainchip Holdings Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ******************************************************************************
"""
KWS model training script.
"""

# System imports
import os
import argparse
import pickle

# Keras imports
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical, get_file

# Akida
from cnn2snn import load_quantized_model, quantize_layer

# Better LR Handling
from akida_models.cyclic_lr import CyclicLR


def get_rescaled_dataset(a, b):
    """ Loads and rescales KWS dataset.

    Args:
        a (int): rescale factor
        b (int): rescale bias

    Returns:
        tuple: train data, train labels, validation data and validation labels
    """
    # Load pre-processed dataset
    fname = get_file(
        fname='kws_preprocessed_all_words_except_backward_follow_forward.pkl',
        origin=
        'http://data.brainchip.com/dataset-mirror/kws/kws_preprocessed_all_words_except_backward_follow_forward.pkl',
        cache_subdir=os.path.join('datasets', 'kws'))

    print('Loading pre-processed dataset...')
    with open(fname, 'rb') as f:
        [x_train_ak, y_train, x_val_ak, y_val, _, _, _, _] = pickle.load(f)

    # For cnn2snn Keras training, data must be scaled (usually to [0,1])
    x_train_keras = \
        (x_train_ak.astype('float32') - b) / a
    x_val_keras = \
        (x_val_ak.astype('float32') - b) / a

    return x_train_keras, y_train, x_val_keras, y_val


def compile_model(model, learning_rate=1e-4):
    """ Compiles the model.

    Args:
        model (tf.Keras.Model): the model to compile
        learning_rate (float): the learning rate

    Returns:
        tf.Keras.Model: the compiled model
    """
    # Initialize optimizer and compile model
    opt = Adam(lr=learning_rate)
    model.compile(loss='categorical_crossentropy',
                  optimizer=opt,
                  metrics=['accuracy'])
    return model


def train_model(model, x_train, y_train, x_val, y_val, batch_size, epochs):
    """ Trains the model.

    Args:
         model (tf.Keras.Model): the model to train
        x_train (numpy.ndarray): train data
        y_train (numpy.ndarray): train labels
        x_val (numpy.ndarray): validation data
        y_val (numpy.ndarray): validation labels
        batch_size (int): the batch size
        epochs (int): the number of epochs
    """
    # Warn user if number of epochs is not a multiple of 8
    if epochs % 8:
        print("WARNING: for better performance, the number of epochs "
              f" must be a multiple of 8; got 'epochs' = {epochs}")

    # Training parameters (cyclical learning rate)
    scaler = 4
    base_lr = 5e-6
    max_lr = 2e-3

    # Cyclical learning rate
    callbacks = []
    clr = CyclicLR(base_lr=base_lr,
                   max_lr=max_lr,
                   step_size=scaler * x_train.shape[0] / batch_size,
                   mode='triangular')
    callbacks.append(clr)

    # Compile model
    model = compile_model(model, max_lr)

    model.fit(x_train,
              to_categorical(y_train),
              batch_size=batch_size,
              epochs=epochs,
              verbose=1,
              validation_data=(x_val, to_categorical(y_val)),
              callbacks=callbacks)


def evaluate_model(model, x_val, y_val):
    """ Evaluates model performances.

    Args:
        model (tf.Keras.Model): the model to evaluate
        x_val (numpy.ndarray): evaluation data
        y_val (numpy.ndarray): evaluation labels
    """
    model = compile_model(model)
    _, accuracy = model.evaluate(x_val, to_categorical(y_val), verbose=0)
    print('Validation accuracy:', accuracy)


def main():
    """ Entry point for script and CLI usage.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-m",
                        "--model",
                        type=str,
                        required=True,
                        help="Model to load")
    parser.add_argument("-s",
                        "--save_model",
                        type=str,
                        default=None,
                        help="Save model with the specified name")
    parser.add_argument("-laq",
                        "--last_activ_quantization",
                        type=int,
                        default=None,
                        help="The last layer activation quantization")
    parser.add_argument("-e",
                        "--epochs",
                        type=int,
                        default=0,
                        help="The number of training epochs")
    parser.add_argument("-b",
                        "--batch_size",
                        type=int,
                        default=100,
                        help="The training batch size")

    sp = parser.add_subparsers(dest="action")
    sp.add_parser("train", help="Train a Keras model")
    sp.add_parser("eval", help="Evaluate a model")

    args = parser.parse_args()

    # Input scaling
    # Akida is configured to take 8-bit inputs without rescaling
    # but for the training, we use float weights between 0 and 1
    a = 255
    b = 0

    # Load the source model
    model = load_quantized_model(args.model)

    # If specified, change the last layer activation bitwidth
    if args.last_activ_quantization:
        model = quantize_layer(model, 'separable_6_relu',
                               args.last_activ_quantization)

    # Prepare the dataset
    x_train, y_train, x_val, y_val = get_rescaled_dataset(a, b)

    # Training parameters
    batch_size = args.batch_size
    epochs = args.epochs

    # Train model
    if epochs > 0 and args.action == "train":
        train_model(model, x_train, y_train, x_val, y_val, batch_size, epochs)

        # Save model in Keras format (h5)
        if args.save_model:
            model.save(args.save_model, include_optimizer=False)

    if args.action == "eval":
        # Evaluate model accuracy
        evaluate_model(model, x_val, y_val)


if __name__ == "__main__":
    main()
