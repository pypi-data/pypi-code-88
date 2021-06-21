# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Worker script to compute RAI requests."""


from azureml.responsibleai.tools.model_analysis._compute_utilities import _compute_wrapper


if __name__ == '__main__':
    _compute_wrapper()
