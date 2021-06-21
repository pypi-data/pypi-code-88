# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from typing import List

from .explain_request import ExplainRequest


class RequestDTO:
    """Pickleable object for transmitting the requests to remote compute.

    Ideally we ought to be able to convert this to JSON as well."""

    def __init__(self,
                 *,
                 explanation_requests: List[ExplainRequest]):
        if explanation_requests is not None:
            self._explain_requests = explanation_requests
        else:
            self._explain_requests = []

    @property
    def explanation_requests(self) -> List[ExplainRequest]:
        return self._explain_requests
