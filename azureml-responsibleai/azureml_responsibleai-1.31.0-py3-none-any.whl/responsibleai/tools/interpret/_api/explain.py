# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""APIs for remote and local explanations."""
import numpy as np
import pickle
import scipy
import shutil
import tempfile
import uuid

from pathlib import Path
from typing import List, Optional, Union

from interpret.ext.glassbox import LGBMExplainableModel

from azureml._base_sdk_common._docstring_wrapper import experimental
from azureml._common._error_definition import AzureMLError
from azureml.data import TabularDataset
from azureml.core import (
    Dataset, Experiment, Model, Run,
    RunConfiguration, ScriptRunConfig, Workspace)
from azureml.exceptions import UserErrorException
from azureml.interpret import ExplanationClient
from azureml.interpret.mimic_wrapper import MimicWrapper

from azureml.responsibleai.common._errors.error_definitions import (
    InvalidDatasetTypeError, InvalidExperimentTypeError, InvalidModelTypeError)
from azureml.responsibleai.common.model_loader import ModelLoader
from azureml.responsibleai.tools.interpret._api.explanation_types import ExplanationTypes
from azureml.responsibleai.tools.interpret._api.surrogate_types import SurrogateTypes
from azureml.responsibleai.tools.interpret._api.config_validation import inject_dependencies


# Remote script constants
SCRIPT_NAME = 'explain_script.py'
SCRIPT_INIT_PATH = Path(__file__).parent / SCRIPT_NAME

REMOTE_UPLOAD_DIR = Path(tempfile.gettempdir()) / 'remote_upload'

MODEL_LOADER_FILENAME = 'model_loader.pkl'
FEATURE_MAPS_FILENAME = 'feature_maps.pkl'

# Local explanation constants
MODEL_DOWNLOAD_DIR = Path(tempfile.gettempdir()) / 'azureml-model-cache'


@experimental
def submit_explanation_run(
    workspace: Workspace,
    experiment: Union[Experiment, str],
    run_config: RunConfiguration,
    model: Union[Model, str],
    dataset_init: Union[Dataset, str],
    dataset_eval: Union[Dataset, str],
    target_feature: str,
    model_loader: ModelLoader,
    feature_maps: Optional[List[Union[np.ndarray, scipy.sparse.csr_matrix]]] = None,
    comment: Optional[str] = None,
) -> Run:
    """
    Submit a run to explain a model.

    :param workspace: Workspace where the AzureML model to explain is registered.
    :type workspace: azureml.core.Workspace
    :param experiment: Experiment in which to create the remote run (or experiment name).
    :type experiment: azureml.core.Experiment
    :param run_config: RunConfiguration to configure the remote or local run.
    :type run_config: azureml.core.RunConfiguration
    :param model: The registered AzureML model to explain (or model ID).
    :type model: azureml.core.Model
    :param dataset_init: Initialization dataset (or dataset ID).
    :type dataset_init: azureml.core.Dataset
    :param dataset_eval: Evaluation dataset (or dataset ID).
    :type dataset_eval: azureml.core.Dataset
    :param target_feature: Dataset target feature name.
    :type target_feature: str
    :param model_loader: Model loader to use when deserializing the model.
    :type model_loader: azureml.responsibleai.common.model_loader.ModelLoader
    :param feature_maps: A mapping from raw to engineered features.
    :type feature_maps: list[Union[numpy.array, scipy.sparse.csr_matrix]]
    :param comment: Optional comment for the explanation.
    :type comment: str
    :return: The AzureML run that was launched to create the new explanation.
    """
    experiment = _get_experiment(workspace, experiment)
    dataset_init = _get_dataset(workspace, dataset_init, 'dataset_init')
    dataset_eval = _get_dataset(workspace, dataset_eval, 'dataset_eval')
    model = _get_model(workspace, model)

    surrogate_type = SurrogateTypes.LIGHTGBM
    inject_dependencies(run_config, surrogate_type)

    remote_dir = REMOTE_UPLOAD_DIR / str(uuid.uuid4())
    remote_dir.mkdir(parents=True)

    shutil.copy(SCRIPT_INIT_PATH, remote_dir)

    script_arguments = [
        '--model_id', model.id,
        '--dataset_id_init', dataset_init.id,
        '--dataset_id_eval', dataset_eval.id,
        '--target_feature', target_feature,
    ]

    with open(remote_dir / MODEL_LOADER_FILENAME, 'wb') as f:
        pickle.dump(model_loader, f)
    script_arguments.extend(['--model_loader_filepath', MODEL_LOADER_FILENAME])

    if feature_maps is not None:
        with open(remote_dir / FEATURE_MAPS_FILENAME, 'wb') as f:
            pickle.dump(feature_maps, f)
        script_arguments.extend(['--feature_maps_filepath', FEATURE_MAPS_FILENAME])

    if comment is not None:
        script_arguments.extend(['--comment', comment])

    script_run_config = ScriptRunConfig(source_directory=remote_dir,
                                        script=SCRIPT_NAME,
                                        run_config=run_config,
                                        arguments=script_arguments)

    return experiment.submit(script_run_config)


@experimental
def _explain_internal(
    workspace: Workspace,
    run: Run,
    model: Model,
    dataset_init: Dataset,
    dataset_eval: Dataset,
    target_feature: str,
    model_loader: ModelLoader,
    feature_maps: Optional[List[Union[np.ndarray, scipy.sparse.csr_matrix]]] = None,
    comment: Optional[str] = None,
):
    """
    Explain a model on local compute.

    :param workspace: Workspace where the AzureML model to explain is registered.
    :param run: An AzureML run where the explanation will be uploaded.
    :param model: The registered AzureML model to explain.
    :param dataset_init: Initialization dataset.
    :param dataset_eval: Evaluation dataset.
    :param target_feature: Dataset target feature name.
    :param model_loader: Model loader to use when deserializing the model.
    :param feature_maps: A mapping from raw to engineered features.
    :param comment: Optional comment for the explanation.
    :return: The new explanation object.
    """
    model_dir = MODEL_DOWNLOAD_DIR / str(uuid.uuid4())

    if model_dir.exists():
        shutil.rmtree(model_dir)

    model.download(target_dir=model_dir)

    loaded_model = model_loader.load(model_dir)

    X_init = dataset_init.drop_columns([target_feature]).to_pandas_dataframe()
    X_eval = dataset_eval.drop_columns([target_feature]).to_pandas_dataframe()

    surrogate_class = LGBMExplainableModel
    # TODO: Pass transformations
    explainer = MimicWrapper(workspace, loaded_model, surrogate_class,
                             init_dataset=X_init, feature_maps=feature_maps)

    # TODO: Pass true_ys
    explanation = explainer.explain(ExplanationTypes.ALL, eval_dataset=X_eval, upload=False)

    client = ExplanationClient.from_run(run)
    client.upload_model_explanation(explanation, comment=comment)

    return explanation


def _get_dataset(workspace: Workspace, dataset: Union[Dataset, str], arg_name: str) -> Dataset:
    """
    Get a reference to an AzureML Dataset object.

    If the `dataset` argument passed is a Dataset already then return it, otherwise convert the
    Dataset ID to a Dataset object by fetching it from the provided Workspace.

    :param workspace: Workspace where the AzureML Dataset is registered.
    :param dataset: Dataset object or Dataset ID string.
    :param arg_name: Name of the dataset being fetched, used only on fetch failures.
    :return: The Dataset object.
    """
    if isinstance(dataset, str):
        return Dataset(workspace, id=dataset)
    elif isinstance(dataset, (Dataset, TabularDataset)):
        return dataset
    else:
        raise UserErrorException._with_error(
            AzureMLError.create(
                InvalidDatasetTypeError,
                actual_type=type(dataset),
                arg_name=arg_name,
                type_list="Dataset, str",
                target='explain'))


def _get_experiment(workspace: Workspace, experiment: Union[Experiment, str]):
    """
    Get a reference to an AzureML Exeriment object.

    If the `experiment` argument passed is an Exeriment already then return it,
    otherwise convert the Exeriment ID to an Exeriment object by fetching it
    from the provided Workspace.

    :param workspace: Workspace where the AzureML Exeriment is registered.
    :param experiment: Exeriment object or Exeriment ID string.
    :return: The Experiment object.
    """
    if isinstance(experiment, str):
        return Experiment(workspace, name=experiment)
    elif isinstance(experiment, Experiment):
        return experiment
    else:
        raise UserErrorException._with_error(
            AzureMLError.create(
                InvalidExperimentTypeError,
                actual_type=type(experiment),
                arg_name='experiment',
                type_list="Experiment, str",
                target='explain'))


def _get_model(workspace: Workspace, model: Union[Model, str]):
    """
    Get a reference to an AzureML Model object.

    If the `model` argument passed is a Model already then return it,
    otherwise convert the Model ID to a Model object by fetching it
    from the provided Workspace.

    :param workspace: Workspace where the AzureML Model is registered.
    :param model: Model object or Model ID string.
    :return: The Model object.
    """
    if isinstance(model, str):
        return Model(workspace, id=model)
    elif isinstance(model, Model):
        return model
    else:
        raise UserErrorException._with_error(
            AzureMLError.create(
                InvalidModelTypeError,
                actual_type=type(model),
                arg_name='model',
                type_list="Model, str",
                target='explain'))
