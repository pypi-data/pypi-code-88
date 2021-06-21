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
class Priority(BaseEntity):
    """
	Class responsible for handle issue's priority from jira
	"""
    def do(self, data: dict) -> None:
        """Search on mongo for distinct priorities and save them on sro's database

        Args:
            data (dict): With user, key and server to connect with jira
        """
        try:
            logging.info("Priority")
			
            self.config(data)
            pprint ("Priority")
			#Buscando os dados salvos no banco do mongo
            mongo_collection_name = self.mongo_db.get_collection('issue')

            jira_priority = mongo_collection_name.distinct("fields.priority.name")
			
            priority_list = []
			
			#Processando os ontology_scrum_intended_development_task
            for jira_element in jira_priority:
				
                priority = factories_model.PriorityFactory()
                priority.name = jira_element.lower()
                priority_list.append (priority)
				
            	
            priority_application = factories.PriorityFactory()
            priority_application.create_bulk(priority_list)

            logging.info("Successfully done Priority ")

        except Exception as e:
            pprint(e)
            logging.error("Failed to do Task")

	