""" This module implement data entities functionality  """
import pandas as pd

from superwise.controller.base import BaseController
from superwise.controller.summary.entities_validator import EntitiesValidator
from superwise.controller.summary.feature_importance import FeatureImportance
from superwise.controller.summary.summary import Summary
from superwise.models.data_entity import DataEntity
from superwise.models.data_entity import DataEntitySummary
from superwise.resources.supwewise_enums import CategoricalSecondaryType
from superwise.resources.supwewise_enums import FeatureType


class DataEntityController(BaseController):
    """ controller for Data entities  """

    def __init__(self, client, sw):
        """
        constructer for DataEntityController class

        :param client:

        """
        super().__init__(client, sw)
        self.path = "model/v1/data_entities"
        self.model_name = "DataEntity"
        self._entities_df = None
        self.data = None

    def create(self, name=None, type=None, is_dimension=None, role=None, feature_importance=None):
        """
        create data entity
        """

        params = locals()
        return self._dict_to_model(params)

    def update_summary(self, data_entity_id, summary):
        """
        update summary implementation
        """
        self.model = DataEntitySummary(data_entity_id, summary)
        self.model_name = "DataEntitySummary"
        self.create(self.model)

    def generate_summary(self, data_entities, task, data, base_version=None, is_return_model=True, **kwargs):
        """
        :param model: model of version
        :return: model of version
        """
        task_id = task.id

        # if base_version supplied -> use it: save only new entities
        if base_version:
            r = self.client.get(self.build_url("model/v1/versions/{}/data_entities".format(base_version.id)))

            previus_entities = self.parse_response(r, is_return_model=False)
            previus_entities = [e["data_entity"] for e in previus_entities]
            previus_entities_dict = {}
            if previus_entities:
                for data_entity in previus_entities:
                    previus_entities_dict[data_entity["name"]] = data_entity["id"]
            for de in data_entities:
                if de.name in previus_entities_dict:
                    de.id = previus_entities_dict[de.name]
                else:
                    de.id = None
        entities_df = DataEntity.list_to_df(data_entities)
        self.data = data
        self._entities_df = entities_df
        validator = EntitiesValidator(task, entities_df)
        validator.prepare(data)
        fi = FeatureImportance(self._entities_df)
        self._entities_df = fi.compute(data)
        entities_df_summary = Summary(self._entities_df, self.data).generate()
        data_entities = DataEntity.df_to_list(entities_df_summary)
        return data_entities
