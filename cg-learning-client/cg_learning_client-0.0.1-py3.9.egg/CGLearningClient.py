from cg_learning_client.utils.HttpUtil import get_request
from cg_learning_client.utils.HttpUtil import get_or_exception
from cg_learning_client.utils.HttpUtil import post_request
from cg_learning_client.DataSet import CGXAPIData
import requests
import json


class CGLearningClient:
    def __init__(self, endpoint, username: str = None, password: str = None):
        self.endpoint = endpoint
        self.username = username
        self.password = password

    def query_activity_by_name(self, name: str, exact: bool = False):
        response = get_request(self.endpoint, '/CG/xAPI/activities', params={
            'name': name,
            'exact': exact
        })
        if requests.codes.ok == response.status_code:
            return response.json()

    def query_statements(self, statement_id: str = None, agent: dict = None,
                         verb: str = None, activity: str = None, registration: str = None,
                         related_activities: bool = False, related_agents: bool = False,
                         related_statements: bool = False, since=None, until=None,
                         page=0, limit=20, need_format=None, attachments: bool = False,
                         ascending: bool = False):
        params = {
            'relatedActivities': related_activities,
            'relatedAgents': related_agents,
            'relatedStatements': related_statements,
            'page': page,
            'limit': limit,
            'attachments': attachments,
            'ascending': ascending
        }
        if statement_id is not None:
            params['statementId'] = statement_id
        if agent is not None:
            params['agent'] = json.dumps(agent)
        if verb is not None:
            params['verb'] = verb
        if activity is not None:
            params['activity'] = activity
        if registration is not None:
            params['registration'] = registration
        if since is not None:
            params['since'] = since
        if until is not None:
            params['until'] = until
        if need_format is not None:
            params['format'] = need_format
        response = get_or_exception(self.endpoint, '/xAPI/statements', params=params)
        data = CGXAPIData(self, params)
        data.data = response['statements']
        data.params = params
        return data

    def generate_operator(self, op_type: str, params: dict, source: list = None):
        operator = {
            'type': op_type,
            'params': params
        }
        if source is not None:
            operator['source'] = source
        response = post_request(self.endpoint, '/CG/xAPI/operator', params=None,
                                content_data=operator)
        if requests.codes.ok == response.status_code:
            return response.json()
        raise Exception("generate operator error")

    def query_operator_output(self, op_id: str, page=0, limit=20):
        response = post_request(self.endpoint, '/CG/xAPI/operator/output',
                            params={
                                'operatorId': op_id,
                                'page': page,
                                'limit': limit
                            })
        if requests.codes.ok == response.status_code:
            return response.json()
        raise Exception("query operator output error")
