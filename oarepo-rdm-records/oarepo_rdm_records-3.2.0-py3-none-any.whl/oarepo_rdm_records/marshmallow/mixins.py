# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
# Copyright (C) 2020 Northwestern University.
#
# Invenio-RDM-Records is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""RDM record schemas."""
from invenio_records_rest.schemas import StrictKeysMixin
from marshmallow.fields import URL, Nested
from oarepo_multilingual.marshmallow import MultilingualStringV2


class TitledMixin:
    """Mixin that adds a multilingual title field to Schema."""

    title = MultilingualStringV2()


class RightsMixin:
    """License rights mixin."""

    def __init__(self, **kwargs):
        """Rights schema constructor."""
        super().__init__(
            fail_on_unknown=False, identifier_required=False, **kwargs)

    class RightsRelated(StrictKeysMixin):
        """Related rights URI."""

        uri = URL()

    icon = URL()
    related = Nested(RightsRelated)
