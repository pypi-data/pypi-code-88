from datetime import datetime
from functools import lru_cache
from .conversor import Conversor

from jiraX import factories as factory
from sro_db.application import factories
from sro_db.model import factories as factories_model

class ConversorProject(Conversor):
    """
    Class responsible for create a SRO's Scum Atomic Project, Scrum Process, 
    Product Backlog Definition and Product Backlog from a Jira's Project
    """
    def __init__(self, organization, data):
        super().__init__(organization, data)

    def convert(self, jira_project: object, ontology_scrum_atomic_project: object = None, ontology_scrum_process: object  = None, ontology_product_backlog_definition: object  = None, ontology_product_backlog: object  = None):
        """Method responsible for converting

        Jira Issue -> SRO Scum Atomic Project, Scrum Process, Product Backlog Definition and Product Backlog

        Args:
            jira_project (object): Project from Jira
            ontology_scrum_atomic_project (object, optional): ScrumAtomicProject created by a sro_db's factory. Defaults to None.
            ontology_scrum_process (object, optional): ScrumProcess created by a sro_db's factory. Defaults to None.
            ontology_product_backlog_definition (object, optional): ProductBacklogDefinition created by a sro_db's factory. Defaults to None.
            ontology_product_backlog (object, optional): ProductBacklog created by a sro_db's factory. Defaults to None.

        Returns:
            tuple[object, object, object, object]: ScrumAtomicProject, ScrumProcess, ProductBacklogDefinition, ProductBacklog
        """
        print("--------- Conversor project -----------")

        # Scrum atomic project
        if ontology_scrum_atomic_project is None:
            ontology_scrum_atomic_project = factories_model.ScrumAtomicProjectFactory()
        ontology_scrum_atomic_project.organization_id = self.organization.id
        ontology_scrum_atomic_project.name = jira_project.name
        ontology_scrum_atomic_project.index = jira_project.key
        
        # Scrum process
        if ontology_scrum_process is None:
            ontology_scrum_process = factories_model.ScrumProcessFactory()
        ontology_scrum_process.organization = self.organization
        ontology_scrum_process.name = jira_project.name
        ontology_scrum_process.scrum_project = ontology_scrum_atomic_project

        # Product backlog definition
        if ontology_product_backlog_definition is None:
            ontology_product_backlog_definition = factories_model.ProductBacklogDefinitionFactory()
        ontology_product_backlog_definition.name = jira_project.name
        ontology_product_backlog_definition.scrum_process = ontology_scrum_process
        
        #Product backlog
        if ontology_product_backlog is None:
            ontology_product_backlog = factories_model.ProductBacklogFactory()
        ontology_product_backlog.name = jira_project.name
        # ontology_product_backlog.product_backlog_definition = ontology_product_backlog_definition.id

        print("--------- Conversor project End -----------")
        
        return ontology_scrum_atomic_project, ontology_scrum_process, ontology_product_backlog_definition, ontology_product_backlog