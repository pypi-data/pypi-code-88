from datetime import datetime
from functools import lru_cache
from .conversor import Conversor
from sro_db.model import factories as factories_model

class ConversorUser(Conversor):
    """
    Class responsible for create a SRO's Person from a Jira's User
    """
    def __init__(self, organization, data):
        self.organization = organization
    
    def convert(self, jira_user: object, ontology_user: object = None) -> object:
        """Method responsible for converting

        Jira User -> SRO Person

        Args:
            jira_user (object): User from Jira
            ontology_user (object, optional): Person created by a sro_db's factory. Defaults to None.

        Returns:
            object: Person created by a sro_db's factory
        """
        print("--------- Conversor User -----------")
    
        if ontology_user is None:
            ontology_user = factories_model.PersonFactory()
        
        ontology_user.organization_id = self.organization.id
        ontology_user.name = jira_user.displayName
        if jira_user.emailAddress != '':
            ontology_user.email = jira_user.emailAddress

        print("--------- Conversor User End -----------")

        return ontology_user