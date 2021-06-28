# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
# Copyright (C) 2020 Northwestern University.
#
# Invenio-RDM-Records is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""RDM record schemas."""

from marshmallow_utils.fields import SanitizedUnicode
from marshmallow_utils.schemas import IdentifierSchema


class ReferenceSchema(IdentifierSchema):
    """Reference schema."""

    SCHEMES = [
        "isni",
        "grid",
        "crossreffunderid",
        "other"
    ]

    def __init__(self, **kwargs):
        """Refer schema constructor."""
        super().__init__(allowed_schemes=self.SCHEMES,
                         identifier_required=False, **kwargs)

    reference = SanitizedUnicode(required=True)
