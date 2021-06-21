from datetime import datetime
from elasticsearch_dsl import Document, Date, Keyword, connections, Integer, Text
import os
import requests

ROBOT_LOGS_PREFIX = 'robot-logs'
ROBOT_SUITE_PREFIX = 'robot-suite'


class KibanaUtils:

    def obter_simple_index_name(self, name: str, robot_name: str):
        index_suffix = ''

        environment = os.getenv('ENVIRONMENT', 'DEV').lower()
        return f'{name}-{environment}-{robot_name}{index_suffix}'


class KibanaService:

    BASE_URL = f'{os.getenv("ELASTIC_HOST")}/s/{os.getenv("ELASTIC_SPACE")}/api'
    headers = {
        'Authorization': f'ApiKey {os.getenv("ELASTIC_API_KEY")}',
        'kbn-xsrf': 'reporting'
    }

    def get_index_pattern_by_title(self, title: str):
        response = requests.get(
            f'{self.BASE_URL}/saved_objects/_find?type=index-pattern&search_fields=title&search={title}',
            headers=self.headers
        )
        response_json = response.json()
        if response_json.get('statusCode') is not None:
            raise Exception(response_json['message'])
        return response_json

    def create_index_pattern(self, title: str):
        response = requests.post(f'{self.BASE_URL}/index_patterns/index_pattern',
                                 headers=self.headers,
                                 json={
                                     'index_pattern': {
                                         'title': title
                                     }
                                 })
        response_json = response.json()
        if response_json.get('statusCode') is not None:
            raise Exception(response_json['message'])
        return response_json

    def _create_index_if_not_exist(self, name: str, robot_name: str):
        kibana_utils = KibanaUtils()
        simple_index_pattern = kibana_utils.obter_simple_index_name(
            name, robot_name)
        index_pattern_title = f'{simple_index_pattern}-*'

        response = self.get_index_pattern_by_title(index_pattern_title)
        if response['total'] == 0:
            self.create_index_pattern(index_pattern_title)

    def create_user_dashboard(self, robot_name):
        self._create_index_if_not_exist(ROBOT_LOGS_PREFIX, robot_name)
        self._create_index_if_not_exist(ROBOT_SUITE_PREFIX, robot_name)


class BaseDocument(Document):
    name: str
    timestamp = Date(default_timezone='Brazil/East')
    robot_name = Keyword()
    cliente_id: str

    def __init__(self, **kargs):
        super().__init__(**kargs)
        cliente_id = os.getenv('CLIENTE_ID')
        if cliente_id:
            self.cliente_id = cliente_id

    def obter_index_name(self):
        if not self.timestamp:
            self.timestamp = datetime.now()

        kibana_utils = KibanaUtils()
        index_name = kibana_utils.obter_simple_index_name(
            self.name, self.robot_name)
        return self.timestamp.strftime(f'{index_name}-%Y.%m')

    @ classmethod
    def connect(cls, host, user, pwd):
        connections.create_connection(
            hosts=[host], http_auth=f'{user}:{pwd}')

    def save(self, **kwargs):
        if not self.timestamp:
            self.timestamp = datetime.now()

        kwargs['index'] = self.obter_index_name()
        return super().save(**kwargs)


class RobotLog(BaseDocument):
    # Declare campos customizados
    name = ROBOT_LOGS_PREFIX
    message = Text(analyzer='brazilian')
    level = Keyword()

    class Index:
        name = ROBOT_LOGS_PREFIX
        settings = {
            "number_of_shards": 1
        }


class SuiteLog(BaseDocument):
    name = ROBOT_SUITE_PREFIX
    status = Keyword()
    duration = Integer()

    class Index:
        name = ROBOT_SUITE_PREFIX
        settings = {
            "number_of_shards": 1
        }
