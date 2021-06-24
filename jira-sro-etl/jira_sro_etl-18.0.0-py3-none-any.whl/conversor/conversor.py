from jiraX import factories as factory
from sro_db.application import factories
from sro_db.model import factories as factories_model
from datetime import datetime
from functools import lru_cache
from pprint import pprint

import abc

class Conversor(metaclass=abc.ABCMeta):
    """
    An abstract class for conversors
    """
    def __init__(self, organization, data):
        self.organization = organization
        self.data = data
        self.issue_apl = factory.IssueFactory(user=data['user'], apikey=data['key'], server=data['url'])
        self.board_apl = factory.BoardFactory(user=data['user'], apikey=data['key'], server=data['url'])

    def date_formater(self, date_string: str) -> datetime:
        """Receive date in YYYY-MM-DD T HH:MM:SS and return datetime

        Can receive date with more details like hour, minute and second, but all info
        after day is ignored

		Args:
			date_string (str/NoneType): string YYYY-MM-DD T HH:MM:SS or None

		Returns:
			datetime/NoneType: Formated date or None if param was None
		"""
        if date_string:
            return datetime.strptime(date_string.split('.')[0], '%Y-%m-%dT%H:%M:%S')
        return None

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

    def __find_on_changelog_list(self, ids_list: list, _list: list) -> list:
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

    def __find_on_changelog(self, issue: object, ids_list: list) -> list:
        """Find informations inside changelogs list.
        
        By first, try on changelogs that are already inside of issue object
        if still missing some data, get complete changelog from api and try with it

        Args:
            issue (object): Issue from Jira
            ids_list (list): List with status's ids (from a board)

        Returns:
            list: [(activated date, activated by), (resolved date, resolved by), (closed date, closed by)]
            with None on missing data
        """
        first_try = self.__find_on_changelog_list(ids_list, issue.raw['changelog']['histories'])
        if len([x for x,y in first_try if x is not None]) == len(ids_list):
            return first_try
        second_try = self.__find_on_changelog_list(ids_list, self.issue_apl.get_changelog(issue.key)['values'])
        return second_try

    def find_activated_resolved_closed(self, issue: object) -> list:
        """Given a issue, return the activated, resolved and closed infos

		Args:
			issue (object): Issue from Jira

		Returns:
			list: List of [activated, resolve, closed]
		"""
        try:
            board_id = issue.raw['fields']['customfield_10018'][-1]['boardId']
            status_ids = self.__find_status_from_boardId(board_id)
            actual_status_index = status_ids.index(issue.raw['fields']['status']['id'])
            len_status = len(status_ids)
            desired_ids = filter(lambda x: x <= actual_status_index, [1, len_status-2, len_status-1]) # Segundo, penúltimo e último
            result_list = self.__find_on_changelog(issue, [status_ids[i] for i in desired_ids])
            return result_list
        except Exception as e:
            # Caso não esteja em um board
            return [(None,None),(None,None),(None,None)]

    @abc.abstractmethod
    def convert(self):
        pass