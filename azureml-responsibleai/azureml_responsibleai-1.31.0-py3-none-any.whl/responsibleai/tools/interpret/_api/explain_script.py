# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Script for remote explanations."""
import argparse
import pickle

from azureml.core import Dataset, Model, Run
from azureml.responsibleai.tools.interpret._api.explain import _explain_internal


def main(args):
    run = Run.get_context()
    workspace = run.experiment.workspace

    model = Model(workspace=workspace, id=args.model_id)

    dataset_init = Dataset.get_by_id(workspace=workspace, id=args.dataset_id_init)
    dataset_eval = Dataset.get_by_id(workspace=workspace, id=args.dataset_id_eval)

    with open(args.model_loader_filepath, 'rb') as f:
        model_loader = pickle.load(f)

    feature_maps = None
    if args.feature_maps_filepath is not None:
        with open(args.feature_maps_filepath, 'rb') as f:
            feature_maps = pickle.load(f)

    _explain_internal(workspace, run, model, dataset_init, dataset_eval, args.target_feature, model_loader,
                      feature_maps=feature_maps, comment=args.comment)


def parse_args():
    parser = argparse.ArgumentParser()

    # Required
    parser.add_argument('--dataset_id_init', type=str, required=True,
                        help="Initialization dataset ID.")
    parser.add_argument('--dataset_id_eval', type=str, required=True,
                        help="Evaluation dataset ID.")
    parser.add_argument('--target_feature', type=str, required=True,
                        help="Target feature name.")
    parser.add_argument('--model_id', type=str, required=True,
                        help="ID of registered AzureML model.")
    parser.add_argument('--model_loader_filepath', type=str, required=True,
                        help="Path to a serialized custom model loader.")

    # Optional
    parser.add_argument('--feature_maps_filepath', type=str, default=None,
                        help="Path to a serialized list of maps from engineered to raw features.")
    parser.add_argument('--comment', type=str, default=None,
                        help="Comment for the explanation.")

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(args)
