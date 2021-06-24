from functools import lru_cache
import logging

logging.basicConfig(level=logging.INFO)

from jiraX import factories as factory
from pprint import pprint
from .base_entity import BaseEntity
from tqdm import tqdm

from .conversor import factories as factories_conversor

import concurrent.futures

""" Scrum performed development task """
class scrum_development_task_history(BaseEntity):
	"""
	Class responsible for retrieve tasks from jira and save them on database
	"""
	def create(self, data, jira_issue = None, jira_project = None):
		pass

	def update(self, data, is_a_task = False):
		pass

	def delete(self, data):
		pass

	def get_board_id_status(self, issue: object, board_apl: object) -> list:
		"""Get a list of all status's ids from a board

		Args:
			issue (object): An issue from Jira
			board_apl (object): Object created by a jiraX's factory

		Returns:
			list: List containing ids of all board's status
		"""
		try:
			board_id = issue.raw['fields']['customfield_10018'][-1]['boardId']
			return self.__find_status_from_boardId(board_id, board_apl)
		except Exception:
			return None

	def get_issue_status_id(self, issue: object) -> str:
		"""Get issue's status id

		Args:
			issue (object): An issue from Jira

		Returns:
			str: Issue's status id
		"""
		try:
			return issue.raw['fields']['status']['id']
		except Exception:
			return None

	def extract_changelog(self, project: object) -> list:
		"""Get the changelog of all issues of a given project and save useful
		informations on changelog's collection on mongo

		Args:
			project (object): A project from Jira

		Returns:
			list: List with the changelog of all issues
		"""
		issue_apl = factory.IssueFactory(user=self.user,apikey=self.key,server=self.url)
		board_apl = factory.BoardFactory(user=self.user,apikey=self.key,server=self.url)
		
		issues = issue_apl.find_by_project(project.key)
		changelog_list = []
		pprint ("Changelog do projeto: "+project.name)
		for issue in issues:	
			try:
				changelog = issue_apl.get_changelog(issue.key)
				changelog['issue_id'] = issue.id
				changelog['board_id_status'] = self.get_board_id_status(issue, board_apl)
				changelog['issue_status'] = self.get_issue_status_id(issue)
				changelog_list.append(changelog)
			except Exception as e:
				pprint(e)

		pprint("Fim Changelog do projeto:"+project.name)
		return changelog_list

	def extract(self, data: dict) -> None:
		"""Retrieve changelog from all projects and save them on database

		Args:
			data (dict): Dict to configure the BaseEntity
		"""
		try:
			logging.info("Scrum Development Task")

			self.config(data)
			self.delete_data_collection("changelog")

			project_apl = factory.ProjectFactory(user=self.user,apikey=self.key,server=self.url)
			projects = project_apl.find_all()
			
			with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
				result_futures = list(map(lambda project: executor.submit(self.extract_changelog, project), projects))
				for future in concurrent.futures.as_completed(result_futures):
					try:
						self.insert_many_on_mongo_db(future.result(),"changelog") 						
						print('resutl save' + str(len(future.result())))
					except Exception as e:
						print('e is', e, type(e))

			logging.info("Successfully done history ")
		
		except Exception as e:
			pprint(e)
			logging.error("Failed to do Scrum Development Task")

	@lru_cache(maxsize=20)
	def __find_status_from_boardId(self, board_id: str, board_apl: object) -> list:
		"""Get all possible status id from a board (sorted: init -> end)

		Args:
			board_id (str): Jira's board id
			board_apl (object): Object created by a jiraX's factory

		Returns:
			list: List with desired ids to search on changelog
		"""
		raw = board_apl.get_config(board_id)
		columns_list = raw['columnConfig']['columns']
		status_ids_list = [_dict['statuses'][0]['id'] for _dict in columns_list] 
		return status_ids_list

	def __find_on_changelog_list(self, ids_list: list, _list: list)-> list:
		"""Find date and responsible user for activated, resolved and closed

		Args:
			ids_list (list): List of desired status's ids from a specific board
			_list (list): Changelogs

		Returns:
			list: [(activated date, activated by), (resolved date, resolved by), (closed date, closed by)]
		"""
		result = [(None,None),(None,None),(None,None)]
		try:
			for changelog in _list:
				for item in changelog['items']:
					try:
						if(item['field'] == 'status' and item['to'] in ids_list):
							result[ids_list.index(item['to'])] = (self.date_formater(changelog['created']), changelog['author']['accountId'])
					except Exception as e:
						pass
		except Exception as e:
			pass
		return result

	def find_activated_resolved_closed(self, changelogs: list) -> list:
		"""Given a changelogs list, return the activated, resolved and closed
		infos for each changelog on a list

		Args:
			changelogs (list): List of changelogs

		Returns:
			list: List of (issue id, [activated, resolve, closed])
		"""
		out = []
		for changelog in changelogs:
			try:
				status_ids = changelog['board_id_status']
				actual_status_index = status_ids.index(changelog['issue_status'])
				len_status = len(status_ids)
				desired_ids = filter(lambda x: x <= actual_status_index, [1, len_status-2, len_status-1])
				result_list = self.__find_on_changelog_list([status_ids[i] for i in desired_ids], changelog['values'])
				out.append( (changelog['issue_id'], result_list) )
			except Exception as e:
				out.append( (changelog['issue_id'], [(None,None),(None,None),(None,None)]) )
		return out

	def do(self, data: dict) -> None:
		"""Update activated, resolve, and closed info for all issues on mongo

		Args:
			data (dict): With user, key and server to connect with jira
		"""
		logging.info("Changelog")
		self.config(data)
		pprint ("Changelog Started")
		mongo_collection_name = self.mongo_db.get_collection('changelog')
		mongo_collection_issue = self.mongo_db.get_collection('issue')

		changelogs = mongo_collection_name.find({},{ "issue_id": 1, "values": 1, "board_id_status": 1, "issue_status": 1 })

		result = self.find_activated_resolved_closed(changelogs)

		bulk = mongo_collection_issue.initialize_ordered_bulk_op()
		for issue_id, data in result:
			(activated_date, activated_id), (resolved_date, resolved_id), (closed_date, closed_id) = data
			bulk.find({ 'id': issue_id }).update(
				{'$set':
					{'activated_date': activated_date,
					'activated_id': activated_id,
					'resolved_date': resolved_date,
					'resolved_id': resolved_id,
					'closed_date': closed_date,
					'closed_id': closed_id}
				}
			)
		bulk.execute()
		pprint ("Changelog Done")



