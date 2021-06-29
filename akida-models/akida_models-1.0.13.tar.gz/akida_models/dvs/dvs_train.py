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
Training script for DVS models.
"""

# System imports
import os
import argparse
import numpy as np

# Tensorflow imports
import tensorflow as tf
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import get_file

# Akida imports
from cnn2snn import load_quantized_model, convert

# Better LR Handling
from akida_models.cyclic_lr import CyclicLR

# Local utils
from .dvs_generator import DVS_DataGenerator


def prepare_dataset(dataset_name, train_set, test_set):
    """ Set dataset parameters for DVSDataGenerator from DVS pickles.

    Args:
        dataset_name (str): name of the dataset to use
        train_set (list): train data
        test_set (list): test data

    Returns:
        tuple: train data, test data, classes selected for training and number
         of times that every sample have to be repeated for training
    """
    if dataset_name == 'dvs_gesture':
        events_inversion = False
        allow_duplicate_events = False
        packets_fixed_by = 'dur'
        packets_per_sample = 3
        # packet_length is in milliseconds
        packet_length = 60
        downscale = 2
        camera_dims = (128, 128, 2)
        # class_list is used to define class that have to be learnt
        class_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        # sample_repeats define number of time that sample should be repeated
        sample_repeats = 5
    elif dataset_name == 'samsung_handy':
        events_inversion = False
        allow_duplicate_events = False
        packets_fixed_by = 'dur'
        packets_per_sample = 1
        packet_length = 20
        downscale = 4
        camera_dims = (480, 640, 2)
        class_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        sample_repeats = 30
    else:
        print('ERROR: Dataset "{}" not recognised'.format(dataset_name))

    # Generate DVS data from preprocessed NPY files with params defined above
    train_data = DVS_DataGenerator(
        inversion=events_inversion,
        dataset=train_set,
        subpacket_length=packet_length,
        subpackets_per_packet=packets_per_sample,
        camera_dims=camera_dims,
        packets_fixed_by=packets_fixed_by,
        include_polarity=True,
        allow_duplicate_events=allow_duplicate_events,
        downscale=downscale)

    test_data = DVS_DataGenerator(inversion=events_inversion,
                                  dataset=test_set,
                                  subpacket_length=packet_length,
                                  subpackets_per_packet=packets_per_sample,
                                  camera_dims=camera_dims,
                                  packets_fixed_by=packets_fixed_by,
                                  include_polarity=True,
                                  allow_duplicate_events=allow_duplicate_events,
                                  downscale=downscale)

    return train_data, test_data, class_list, sample_repeats


def compile_model(model, learning_rate=0.001):
    """ Compiles the model.

    Args:
        model (tf.Keras.Model): the model to compile
        learning_rate (float, optional): the learning rate. Defaults to 0.001.

    Returns:
        tf.Keras.Model: the compiled model
    """
    # Add ADAM optimizer and compile the model
    opt = Adam(lr=learning_rate)
    model.compile(loss='categorical_crossentropy',
                  metrics=['accuracy'],
                  optimizer=opt)
    return model


def train_model(model, train_set, test_set, class_list, sample_repeats,
                batch_size, max_learning_rate, epochs):
    """ Trains the model.

    Args:
        model (tf.Keras.Model): the model to train
        train_set (DVS_DataGenerator): train data generator
        test_set (DVS_DataGenerator): test data generator
        class_list (list): classes selected for training
        sample_repeats (int): number of times that every sample have to be
         repeated for training
        batch_size (int): the batch size
        max_learning_rate (float): learning rate maximum value
        epochs (int): the number of epochs
    """
    if epochs > 0:
        model = compile_model(model, max_learning_rate)

        min_lr = max_learning_rate * 0.01

        callbacks = []
        n_iterations = np.round(
            len(train_set.dataset) * sample_repeats / batch_size)

        lr_scheduler = CyclicLR(base_lr=min_lr,
                                max_lr=max_learning_rate,
                                step_size=4 * n_iterations,
                                mode='triangular2')
        callbacks.append(lr_scheduler)

        x_test_ev, y_test = test_set.get_random_samples(
            class_list=class_list, samples_per_trial=sample_repeats)
        x_test = test_set.samples_evs2images(x_test_ev)
        y_test = tf.keras.utils.to_categorical(y_test)

        for j in range(epochs):
            print('Epoch: ' + str(j))
            x_train_ev, y_train = train_set.get_random_samples(
                class_list=class_list, samples_per_trial=sample_repeats)
            y_train = tf.keras.utils.to_categorical(y_train)

            augmentation_repeats = 4
            for _ in range(augmentation_repeats):
                x_train_ev_aug = train_set.augment_data(x_train_ev,
                                                        polarity_flip=True,
                                                        rotation_range=30,
                                                        width_shift_range=1.5,
                                                        height_shift_range=1.5)

                x_train = train_set.samples_evs2images(x_train_ev_aug)
                model.fit(x_train,
                          y_train,
                          epochs=1,
                          batch_size=batch_size,
                          callbacks=callbacks,
                          validation_data=(x_test, y_test))

            del x_train_ev, x_train, y_train


def evaluate_model(model, test_set, sample_repeats, class_list):
    """ Evaluates model performances.

    Args:
        model (tf.Keras.Model): the model to train
        test_set (DVS_DataGenerator): test data generator
        sample_repeats (int): number of times that every sample have to be
         repeated for training
        class_list (list): classes selected for training
    """
    x_test_ev, y_test = test_set.get_random_samples(
        class_list=class_list, samples_per_trial=sample_repeats)
    x_test = test_set.samples_evs2images(x_test_ev)
    y_test = tf.keras.utils.to_categorical(y_test)

    model = compile_model(model)
    _, accuracy = model.evaluate(x_test, y_test, verbose=0)
    print('Test accuracy:', accuracy)


def main():
    """ Entry point for script and CLI usage.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-m",
                        "--model",
                        type=str,
                        required=True,
                        help="Model to load")
    parser.add_argument(
        "-s",
        "--savemodel",
        default=None,
        help="Save model with the specified name (if epochs > 0).")

    parser.add_argument("-d",
                        "--dataset",
                        type=str,
                        default='dvs_gesture',
                        choices=['dvs_gesture', 'samsung_handy'],
                        help="Dataset name (defaut=dvs_gesture")
    parser.add_argument("-e",
                        "--epochs",
                        type=int,
                        default=0,
                        help="The number of training epochs")
    parser.add_argument("-b",
                        "--batch_size",
                        type=int,
                        default=32,
                        help="The batch size.")

    sp = parser.add_subparsers(dest="action")
    sp.add_parser(
        "train",
        help="Train a Keras model (data augmentation, decreasing learning rate)"
    )
    sp.add_parser(
        "tune",
        help="Tune a pre-trained Keras model (low learning rate, early stop)")
    sp.add_parser(
        "fine_tune",
        help="Fine tune a pre-trained Keras model (very low learning rate)")
    sp.add_parser("convert",
                  help="Convert a quantized Keras model to an Akida model")
    sp.add_parser("eval", help="Evaluate performance on full test set")

    args = parser.parse_args()

    print("Instantiating convtiny_" + args.dataset + " model")

    # Load pre-processed dataset
    train_file = get_file(fname=args.dataset + '_preprocessed_train.npy',
                          origin=os.path.join(
                              'http://data.brainchip.com/dataset-mirror',
                              args.dataset,
                              args.dataset + '_preprocessed_train.npy'),
                          cache_subdir=os.path.join('datasets', args.dataset))

    test_file = get_file(fname=args.dataset + '_preprocessed_test.npy',
                         origin=os.path.join(
                             'http://data.brainchip.com/dataset-mirror',
                             args.dataset,
                             args.dataset + '_preprocessed_test.npy'),
                         cache_subdir=os.path.join('datasets', args.dataset))

    train_set = list(np.load(train_file, allow_pickle=True))
    test_set = list(np.load(test_file, allow_pickle=True))

    # prepare data with DVS_DataGenerator
    train_data, test_data, class_list, sample_repeats = prepare_dataset(
        dataset_name=args.dataset, train_set=train_set, test_set=test_set)

    # Load the source model
    model = load_quantized_model(args.model)

    if args.action == "convert":
        # Convert to Akida
        model_ak = convert(model, input_is_image=False)
        model_ak.save(args.savemodel)
    elif args.action == "eval":
        evaluate_model(model, test_data, sample_repeats, class_list)
    else:
        if args.action == 'train':
            learning_rate = 0.001
        elif args.action == 'tune':
            learning_rate = 0.0001
        elif args.action == 'fine_tune':
            learning_rate = 0.00001

        # Train model
        train_model(model=model,
                    train_set=train_data,
                    test_set=test_data,
                    class_list=class_list,
                    sample_repeats=sample_repeats,
                    batch_size=args.batch_size,
                    max_learning_rate=learning_rate,
                    epochs=args.epochs)

        if args.savemodel:
            # Save model in Keras format (h5)
            model.save(args.savemodel, include_optimizer=False)


if __name__ == "__main__":
    main()
