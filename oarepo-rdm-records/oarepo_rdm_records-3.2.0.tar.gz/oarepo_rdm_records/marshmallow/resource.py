# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
# Copyright (C) 2020 Northwestern University.
#
# Invenio-RDM-Records is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""RDM record schemas."""
from marshmallow import Schema, ValidationError, fields, validates_schema
from oarepo_taxonomies.marshmallow import TaxonomyField

from oarepo_rdm_records.marshmallow.mixins import TitledMixin


class ResourceType(fields.Field):
    """Represents a Resource type as a field.

    This is needed to get a nice error message directly under the
    'resource_type' key. Otherwise the error message is under the "_schema"
    key.
    """

    class ResourceTypeSchema(Schema):
        """Resource type schema."""

        type = TaxonomyField(mixins=[TitledMixin], required=True)
        subtype = fields.Str()

        @validates_schema
        def validate_data(self, data, **kwargs):
            """Validate resource type."""
            pass

    def _deserialize(self, value, attr, data, **kwargs):
        try:
            return ResourceType.ResourceTypeSchema().load(value)
        except ValidationError as error:
            error_content = (
                    []
                    + error.messages.get("type", [])
                    + error.messages.get("subtype", [])
                    + error.messages.get("_schema", [])
            )

            raise ValidationError(error_content)
