# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Entry script that is invoked by the driver script from automl."""
import logging

from azureml.automl.dnn.nlp.classification.io.read import dataloader
from azureml.automl.dnn.nlp.classification.io.write.save_utils import save_model, save_score_script
from azureml.automl.dnn.nlp.classification.multilabel.bert_class import BERTClass
from azureml.automl.dnn.nlp.classification.multilabel.trainer import PytorchTrainer

from azureml.core.run import Run
from azureml.train.automl.runtime._entrypoints.utils.common import parse_settings

_logger = logging.getLogger(__name__)


def run(automl_settings):
    """Invoke training by passing settings and write the output model.
    :param automl_settings: dictionary with automl settings
    """
    run = Run.get_context()
    workspace = run.experiment.workspace

    automl_settings_obj = parse_settings(run, automl_settings)  # Parse settings internally initializes logger

    is_gpu = automl_settings_obj.is_gpu if hasattr(automl_settings_obj, "is_gpu") else True  # Expect gpu by default
    dataset_id = automl_settings_obj.dataset_id
    valid_dataset_id = automl_settings_obj.validation_dataset_id

    training_set, validation_set, num_label_cols = dataloader.dataset_loader(dataset_id, valid_dataset_id, workspace)

    trainer = PytorchTrainer(BERTClass, num_label_cols, is_gpu)
    model = trainer.train(training_set)
    accuracy, f1_score_micro, f1_score_macro = trainer.compute_metrics(validation_set)

    # Log metrics
    run.log('accuracy', accuracy)
    run.log('f1_score_micro', f1_score_micro)
    run.log('f1_score_macro', f1_score_macro)

    save_model(model)
    save_score_script()
