# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Types of explanations."""


class ExplanationTypes:
    """Enum for types of explanations supported."""

    GLOBAL = 'global'
    LOCAL = 'local'

    ALL = [GLOBAL, LOCAL]
