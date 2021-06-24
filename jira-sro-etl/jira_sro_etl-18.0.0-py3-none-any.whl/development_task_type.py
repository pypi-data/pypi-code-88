import logging
logging.basicConfig(level=logging.INFO)

from pprint import pprint
from .base_entity import BaseEntity
from tqdm import tqdm
from pprint import pprint

from sro_db.application import factories
from sro_db.model import factories as factories_model
from .conversor import factories as factories_conversor

""" An Development Task Type """
class DevelopmentTaskType(BaseEntity):
    """
	Class responsible for save Development Task Types on database
	"""
    def do(self, data: dict) -> None:
        """Search for all distincts development task types on mongo (looking in all issues) and save an instance for them on the  sro's database

        Args:
            data (dict): With user, key and server to connect with jira
        """
        try:
            logging.info("Development Task Type")
			
            self.config(data)
            pprint ("Application Type")
			#Buscando os dados salvos no banco do mongo
            mongo_collection_name = self.mongo_db.get_collection('issue')

            jira_development_task_type = mongo_collection_name.distinct("fields.labels")
			
            development_task_type_list = []
			
			#Processando os ontology_scrum_intended_development_task
            for jira_element in jira_development_task_type:
                development_task_type = factories_model.DevelopmentTaskTypeFactory()
                development_task_type.name = jira_element.lower()
                development_task_type_list.append (development_task_type)

            development_task_type_application = factories.DevelopmentTaskTypeFactory()
            development_task_type_application.create_bulk(development_task_type_list)

            logging.info("Successfully done Development Task Type ")

        except Exception as e:
            pprint(e)
            logging.error("Failed to do Task")

	