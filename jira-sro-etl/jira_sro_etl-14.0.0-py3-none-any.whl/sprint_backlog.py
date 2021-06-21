import logging
import time
import threading
logging.basicConfig(level=logging.INFO)

from jiraX import factories as factory
from pprint import pprint
from .base_entity import BaseEntity

from .conversor import factories as factories_conversor

global sprint_backlogs
global tempo_max

sprint_backlogs = {}
tempo_max = False



""" Sprint backlog """
class sprint_backlog(BaseEntity):
	"""
	Class responsible for retrieve the sprints backlog from jira
	"""
	
	def do (self, data: dict) -> dict:
		"""Retrive backlog of all sprints

		Args:
			data (dict): With user, key and server to connect with jira

		Returns:
			dict: Key is the project's key and sprint's id, the value is a list with backlog of this sprint
		"""
		try:
			logging.info("Sprint Backlog")

			self.config(data)

			project_apl = factory.ProjectFactory(user=self.user,apikey=self.key,server=self.url)
			sprint_backlog_apl = factory.SprintBacklogFactory(user=self.user,apikey=self.key,server=self.url)
			board_apl = factory.BoardFactory(user=self.user,apikey=self.key,server=self.url)
			sprint_apl = factory.SprintFactory(user=self.user,apikey=self.key,server=self.url)
			
			# Pegaria todas as histórias/epic do sprint e coloca no sprint_backlog
			# Relaciona as tarefas(sub-task) às histórias/epic(parent)
			# 

			projects = project_apl.find_all()
			for project in projects:
				# logging.info("")
				boards = board_apl.find_by_project(project.key)
				get_board_thread = threading.Thread(target=self.get_board, args=[boards,project.key, sprint_apl, sprint_backlog_apl, sprint_backlogs])
				get_board_thread.start()
				
			return sprint_backlogs

		except Exception as e:
			pass
		
	def get_board(self, boards: list, project_key: str, sprint_apl: object, sprint_backlog_apl: object, sprint_backlogs: dict) -> None:
		"""Save board info for all boards of all sprints of all projects on mongo db

		Args:
			boards (list): List with board (object)
			project_key (str): Project key
			sprint_apl (object): Object created by a jiraX's factory
			sprint_backlog_apl (object): [description]
			sprint_backlogs (dict): [description]
		"""
		try:
			logging.info("entrando")
			logging.info(project_key)
			for board in boards:
				sprints = sprint_apl.find_by_board(board.id)
				for sprint in sprints:
					sprint_backlogs[f'{project_key}({sprint.id})'] = sprint_backlog_apl.find_by_sprint(sprint.id)	
		except Exception as e:
			logging.info("====================ERROR================")
		logging.info(project_key)
		logging.info("saindo")
