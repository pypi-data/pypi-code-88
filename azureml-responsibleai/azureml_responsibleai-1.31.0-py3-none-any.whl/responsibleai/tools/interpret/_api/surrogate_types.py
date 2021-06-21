# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Surrogate model types for explanations."""
from interpret.ext.glassbox import LGBMExplainableModel

from azureml._common._error_definition import AzureMLError
from azureml.exceptions import AzureMLException

from azureml.responsibleai.common._errors.error_definitions import InvalidEnumElementError
from azureml.responsibleai.common._constants import PackageNames


class SurrogateTypes:
    """Enum for types of surrogate models supported by MimicExplainer."""

    LIGHTGBM = 'lightgbm'

    @classmethod
    def get_class(cls, surrogate_type: str):
        """
        Get the surrogate class given a surrogate type string.

        :param surrogate_type: The name of the surrogate model to use when explaining.
        :type surrogate_type: str
        """
        if surrogate_type == cls.LIGHTGBM:
            return LGBMExplainableModel
        else:
            raise AzureMLException._with_error(
                AzureMLError.create(
                    InvalidEnumElementError, value=surrogate_type, enum_name='SurrogateTypes',
                    target="surrogate_type"))

    @classmethod
    def get_dependencies(cls, surrogate_type: str):
        """
        Get the dependencies required to use the specified surrogate model.

        :param surrogate_type: The name of the surrogate model to use when explaining.
        :type surrogate_type: str
        """
        if surrogate_type == cls.LIGHTGBM:
            return [PackageNames.LIGHTGBM]
        else:
            raise AzureMLException._with_error(
                AzureMLError.create(
                    InvalidEnumElementError, value=surrogate_type, enum_name='SurrogateTypes',
                    target="surrogate_type"))
