# ******************************************************************************
#!/usr/bin/env python
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
Training script for YOLO models.
"""

import os
import argparse
import pickle

from tensorflow.keras import Model
from tensorflow.keras.layers import Reshape
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping

from cnn2snn import load_quantized_model

from .yolo_loss import YoloLoss
from .map_evaluation import MapEvaluation
from .batch_generator import BatchGenerator


def compile_model(model_path, anchors, tune, freeze, num_classes, batch_size):
    """ Loads and compiles the model.

    Args:
        model_path (str): path of the model to load and compile
        anchors (list): list of anchors
        tune (bool): True if tuning, False if training
        freeze (bool): enables freezing of the MobileNet base layers
        num_classes (int): the number of classes
        batch_size (int): the batch size

    Returns:
        tuple: the loaded model and the grid size parameter of the model
    """
    nb_box = len(anchors)

    # Load the source model
    base_model = load_quantized_model(model_path)

    # Create a final reshape layer for loss computation
    grid_size = base_model.output_shape[1:3]
    output = Reshape((grid_size[1], grid_size[0], nb_box, 4 + 1 + num_classes),
                     name="YOLO_output")(base_model.output)

    # Build the full model
    model = Model(base_model.input, output)

    # Create optimizer
    if tune:
        learning_rate = 1e-5
    else:
        learning_rate = 1e-4

    optimizer = Adam(lr=learning_rate,
                     beta_1=0.9,
                     beta_2=0.999,
                     epsilon=1e-08,
                     decay=0.0)

    # Create a loss object
    loss_yolo = YoloLoss(anchors, grid_size, batch_size)

    # Compile the model
    model.compile(loss=loss_yolo, optimizer=optimizer)

    # Freeze the model
    if freeze:
        model.trainable = False
        for layer in model.layers[-11:]:  # unfreeze top layers for YOLO
            layer.trainable = True

    return model, grid_size


def train(model_path, train_data, valid_data, anchors, labels, obj_threshold,
          nms_threshold, epochs, tune, freeze, batch_size):
    """ Trains the model.

    Args:
        model_path (str): path of the model to train
        train_data (dict): training data
        valid_data (dict): validation data
        anchors (list): list of anchors
        labels (list): list of labels
        obj_threshold (float): confidence threshold for a box
        nms_threshold (float): non-maximal supression threshold
        epochs (int): the number of epochs
        tune (bool): True if tuning, False if training
        freeze (bool): enables freezing of the MobileNet base layers
        batch_size (int): the batch size

    Returns:
        tf.Keras.Model: the trained model
    """
    TRAIN_TIMES = 10

    # Compile model
    model, grid_size = compile_model(model_path, anchors, tune, freeze,
                                     len(labels), batch_size)

    # Build batch generators
    input_shape = model.input.shape[1:]

    train_generator = BatchGenerator(input_shape=input_shape,
                                     data=train_data,
                                     grid_size=grid_size,
                                     labels=labels,
                                     anchors=anchors,
                                     batch_size=batch_size)

    valid_generator = BatchGenerator(input_shape=input_shape,
                                     data=valid_data,
                                     grid_size=grid_size,
                                     labels=labels,
                                     anchors=anchors,
                                     batch_size=batch_size,
                                     jitter=False)

    # Create callbacks
    early_stop_cb = EarlyStopping(monitor='val_loss',
                                  min_delta=0.001,
                                  patience=10,
                                  mode='min',
                                  verbose=1)

    map_evaluator_cb = MapEvaluation(model,
                                     valid_data,
                                     labels,
                                     anchors,
                                     period=4,
                                     obj_threshold=obj_threshold,
                                     nms_threshold=nms_threshold)

    callbacks = [early_stop_cb, map_evaluator_cb]

    # Start the training process
    model.fit(x=train_generator,
              steps_per_epoch=len(train_generator) * TRAIN_TIMES,
              epochs=epochs,
              validation_data=valid_generator,
              callbacks=callbacks,
              workers=12,
              max_queue_size=40)

    return model


def evaluate(model_path, valid_data, anchors, labels, obj_threshold,
             nms_threshold, batch_size):
    """ Evaluates model performances.

    Args:
        model_path (str): path of the model to evaluate
        valid_data (dict): evaluation data
        anchors (list): list of anchors
        labels (list): list of labels
        obj_threshold (float): confidence threshold for a box
        nms_threshold (float): non-maximal supression threshold
        batch_size (int): the batch size
    """
    # Compile model
    model, _ = compile_model(model_path, anchors, True, False, len(labels),
                             batch_size)

    # Create the mAP evaluator
    map_evaluator = MapEvaluation(model,
                                  valid_data,
                                  labels,
                                  anchors,
                                  obj_threshold=obj_threshold,
                                  nms_threshold=nms_threshold)

    # Compute mAP scores and display them
    mAP, average_precisions = map_evaluator.evaluate_map()
    for label, average_precision in average_precisions.items():
        print(labels[label], '{:.4f}'.format(average_precision))
    print('mAP: {:.4f}'.format(mAP))


def main():
    """ Entry point for script and CLI usage.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-d",
                        "--data",
                        default=None,
                        help="The pickle file generated by the preprocessing"
                        " step that contains data variables")
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
    parser.add_argument("-e",
                        "--epochs",
                        type=int,
                        default=15,
                        help="The number of training epochs")
    parser.add_argument("-b",
                        "--batch_size",
                        type=int,
                        default=128,
                        help="The batch size.")
    parser.add_argument("-ap",
                        "--anchors_path",
                        default=None,
                        help="Path to anchors boxes file.")
    parser.add_argument("-f",
                        "--freeze",
                        type=bool,
                        default=False,
                        help="Freeze the MobileNet layers.")
    parser.add_argument("-obj",
                        "--obj_thresh",
                        type=float,
                        default=0.5,
                        help="Confidence threshold for a box")
    parser.add_argument("-nms",
                        "--nms_thresh",
                        type=float,
                        default=0.5,
                        help="Non-Maximal Suppression threshold.")

    sp = parser.add_subparsers(dest="action")
    sp.add_parser("train", help="Train a YOLO model")
    sp.add_parser("tune", help="Tune a pre-trained YOLO model")
    sp.add_parser("eval", help="Evaluate a model.")

    args = parser.parse_args()
    data_path = args.data
    epochs = args.epochs
    anchors_path = args.anchors_path
    freeze = args.freeze
    tune = args.action == 'tune'

    if data_path is None or not os.path.exists(data_path):
        raise ValueError("--data argument is mandatory and must be a valid "
                         "pickle file path produced by the preprocessing step")

    if anchors_path is None or not os.path.exists(anchors_path):
        raise ValueError("--anchors_path is mandatory and must be a valid "
                         "pickle file path produced by the preprocessing step")

    with open(data_path, 'rb') as handle:
        train_data, valid_data, labels = pickle.load(handle)

    with open(anchors_path, 'rb') as handle:
        anchors = pickle.load(handle)

    if args.action != 'eval':
        # Train/tune the model
        model = train(args.model, train_data, valid_data, anchors, labels,
                      args.obj_thresh, args.nms_thresh, epochs, tune, freeze,
                      args.batch_size)
        if args.savemodel:
            # Remove the last reshape layer introduced for training
            model = Model(model.input, model.layers[-2].output)
            # Save the model
            model.save(args.savemodel, include_optimizer=False)
            print(f"Trained model saved as {args.savemodel}")
    else:
        # Evaluate the model
        evaluate(args.model, valid_data, anchors, labels, args.obj_thresh,
                 args.nms_thresh, args.batch_size)


if __name__ == "__main__":
    main()
