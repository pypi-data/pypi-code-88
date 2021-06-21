import logging
logging.basicConfig(level=logging.INFO)

from jiraX import factories as factory
from .base_entity import BaseEntity
from pprint import pprint
from tqdm import tqdm

from sro_db.application import factories
from sro_db.model import factories as factories_model
from .conversor import factories as factories_conversor

from .scrum_project_team import scrum_project_team as etl_scrum_project_team

""" Scrum development team """
class scrum_development_team(BaseEntity):
	"""
	Class responsible for retrieve teams from jira
	"""
	
	def create(self, data: dict, jira_project: object = None) -> object:
		"""Create a development team and save it on database.

		Args:
			data (dict): Dict with jira project information (project_id = data['content']['all']['project']['id'])
			jira_project (object, optional): Project from Jira

		Returns:
			object: DevelopmentTeam created by a sro_db's factory
		"""
		try:
			logging.info("Creating Scrum Development Team")

			if jira_project is None:
				project_id = data['content']['all']['project']['id']
				project_apl = factory.ProjectFactory(user=self.user,apikey=self.key,server=self.url)
				jira_project = project_apl.find_by_id(project_id)

			self.conversor = factories_conversor.ConversorDevelopmentTeamFactory(organization = self.organization, data = self.data)
			scrum_development_team = self.conversor.convert(
				etl_scrum_project_team,
				jira_project)

			scrum_development_team_application = factories.DevelopmentTeamFactory()
			scrum_development_team = scrum_development_team_application.create(scrum_development_team)
			self.create_application_reference('project', scrum_development_team, jira_project.id)

			logging.info("Scrum Development Team created")

			return scrum_development_team
 
		except Exception as e:
			pprint(e)
			logging.error("Failed to create Scrum Development Team")

	def update(self, data):
		pass

	def delete(self, data: dict) -> None:
		"""Delete a development team on database.

		Args:
			data (dict): [description]
		"""
		try:
			logging.info("Deleting Scrum Development Team")

			scrum_development_team_application = factories.DevelopmentTeamFactory()

			content = data['content']
			project = content['all']['project']

			scrum_development_team = scrum_development_team_application.retrive_by_external_uuid(project['id'])
			scrum_development_team_application.delete(scrum_development_team)

			logging.info("Scrum Development Team deleted")

		except Exception as e:
			pprint(e)
			logging.error("Failed to delete Scrum Development Team")

	def do (self, data: dict) -> list:
		"""With data saved on mongo, create and save all development teams on sro db

		Args:
			data (dict): With user, key and server to connect with jira

		Returns:
			list: List of all development teams
		"""
		try:
			logging.info("Scrum Development Team")

			self.config(data)

			mongo_collection_name = self.mongo_db.get_collection('project')

			projects = mongo_collection_name.find({},{ "id": 1,  "name": 1, "key": 1, 'self': 1, 'sro_db_scrum_team_id':1  })

			scrum_development_team_application = factories.DevelopmentTeamFactory()

			scrum_development_team_list = []

			for jira_element in tqdm(projects, desc='Scrum Development Team'):
				scrum_development_team = factories_model.DevelopmentTeamFactory()
				scrum_development_team.organization_id = self.organization.id
				scrum_development_team.name = jira_element['name']+"__scrum_development_team"
				scrum_development_team.scrum_team_id = jira_element['sro_db_scrum_team_id']
				scrum_development_team.jira_element = jira_element
				scrum_development_team.jira_project_id = jira_element['id']
				scrum_development_team_list.append(scrum_development_team)
		
			scrum_development_team_list = scrum_development_team_application.create_bulk(scrum_development_team_list)
			self.create_application_reference_bulk(scrum_development_team_list,'project','id','self')
			
			for scrum_development_team in scrum_development_team_list:
				index_value = scrum_development_team.jira_project_id
				field_value = scrum_development_team.id
				self.update_one_query("issue", "project_id", str(index_value), "sro_db_development_team_id",field_value)

			logging.info("Successfully done (Scrum Development Team)")
			return scrum_development_team_list

		except Exception as e:
			pprint (e)
