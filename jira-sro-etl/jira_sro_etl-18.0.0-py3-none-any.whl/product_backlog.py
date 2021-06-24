import logging
logging.basicConfig(level=logging.INFO)

from jiraX import factories as factory
from pprint import pprint
from .base_entity import BaseEntity

from .conversor import factories as factories_conversor

""" Product backlog """
class product_backlog(BaseEntity):
	"""
	Class responsible for retrieve the backlog of a project from jira
	"""
	def do(self,data):
		"""Retrieve all story, task, sub-task and epic from the projects

		Args:
			data (dict): With user, key and server to connect with jira

		Returns:
			dict: Key is the project's key and value is a list with backlog of this project
		"""
		try:
			logging.info("Product Backlog")

			self.config(data)

			project_apl = factory.ProjectFactory(user=self.user,apikey=self.key,server=self.url)
			backlog_apl = factory.BacklogFactory(user=self.user,apikey=self.key,server=self.url)

			projects = project_apl.find_all()
			backlogs = {}
			for project in projects:
				backlogs[project.key] = backlog_apl.find_by_project(project.key)
			pprint(backlogs)
			return backlogs

		except Exception as e:
			pass

