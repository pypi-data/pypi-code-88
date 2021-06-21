# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Base model settings class to be used by object detection and classification"""

from abc import ABC, abstractmethod


class BaseModelSettings(ABC):
    """Base class defining interface for model settings to be used by object detection and classification"""

    @abstractmethod
    def __init__(self, settings: dict):
        """Initialize model settings from run settings dictionary.

        :param settings: Settings passed into runner.
        :type settings: dict
        """
        pass

    @abstractmethod
    def model_init_kwargs(self):
        """Get kwargs to be used for model initialization.

        :return: kwargs used for initialization
        :rtype: dict
        """
        pass

    @abstractmethod
    def get_settings_dict(self):
        """Get settings dict from which model settings object can be re-initialized.

        :return: Settings dictionary
        :rtype: dict
        """
        pass
