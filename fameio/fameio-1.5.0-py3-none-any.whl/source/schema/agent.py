# -*- coding:utf-8 -*-

import logging as log
from typing import Dict

from fameio.source.schema.attribute import AttributeSpecs
from fameio.source.tools import keys_to_lower


class AgentType:
    """Schema definitions for an Agent type"""
    _NO_ATTRIBUTES = "Agent '{}' has no specified 'Attributes'."
    _NO_PRODUCTS = "Agent '{}' has no specified Products."

    _KEY_ATTRIBUTES = 'Attributes'.lower()
    _KEY_PRODUCTS = 'Products'.lower()

    def __init__(self, name: str, definition: dict):
        """Loads an agent's `definition` from the given input dict"""
        definition = keys_to_lower(definition)

        self.attributes = dict()
        if AgentType._KEY_ATTRIBUTES in definition:
            for attribute_name, attribute_details in definition[AgentType._KEY_ATTRIBUTES].items():
                full_name = name + "." + attribute_name
                self.attributes[attribute_name] = AttributeSpecs(full_name, attribute_details)
        else:
            log.info(AgentType._NO_ATTRIBUTES.format(name))

        self.products = list()
        if AgentType._KEY_PRODUCTS in definition:
            products_to_add = definition[AgentType._KEY_PRODUCTS]
            if isinstance(products_to_add, list):
                self.products.extend(products_to_add)
            else:
                self.products.append(products_to_add)
        else:
            log.info(AgentType._NO_PRODUCTS.format(name))

    def get_products(self) -> list:
        """Returns list of products or an empty list if no products are defined"""
        return self.products

    def get_attributes(self) -> Dict[str, AttributeSpecs]:
        """ Returns list of Attributes of this agent or an empty list if no attributes are defined"""
        return self.attributes
