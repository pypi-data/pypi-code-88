
from .ElasticLibrary import KibanaService
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
from .ElasticLibrary import RobotLog, SuiteLog, BaseDocument
import yaml
import os


class LoggerListener:

    ROBOT_LISTENER_API_VERSION = 2
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    kibana_service: KibanaService
    robot_name: str
    publish_to_elastic: bool

    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self
        self.bi = BuiltIn()
        self.kibana_service = KibanaService()
        self.publish_to_elastic = os.getenv(
            'PUBLISH_TO_ELASTIC', 'False') == 'True'
        try:
            with open("primerobot.yaml") as primerobotfile:
                content = primerobotfile.read()
                primerobot_content = yaml.load(content, Loader=yaml.FullLoader)
                self.robot_name = primerobot_content['metadata']['task_name']
        except Exception as e:
            print(e)

    def start_suite(self, name, attributes):
        try:
            if self.publish_to_elastic:
                logger.error(os.getenv('ELASTIC_HOST'))
                logger.error(os.getenv('ELASTIC_USER'))
                logger.error(os.getenv('ELASTIC_PWD'))
                BaseDocument.connect(
                    os.getenv('ELASTIC_HOST'),
                    os.getenv('ELASTIC_USER'),
                    os.getenv('ELASTIC_PWD')
                )
                RobotLog.init()
                SuiteLog.init()
            else:
                logger.warn(
                    "A execução foi configurada para não publicar os"
                    " resultados no Elasticsearch")
        except Exception as e:
            logger.error("seila")
            message = """
                Ocorreu um erro ao inicializar o Listerner do Elasticsearch.
                A publicação dos dados para o Elasticsearch foi desativada
                Erro: {error}
            """
            logger.error(message.format(error=e))
            self.publish_to_elastic = False

    def log_message(self, message):
        self._log_to_elastic(message['level'], message['message'])

    def end_suite(self, name, attributes):
        if not self.robot_name:
            self.robot_name = name.lower().replace(' ', '-')
        self._log_suite_to_elastic(
            attributes['status'],
            attributes['elapsedtime']
        )

    def end_test(self, name, attributes):
        if attributes['status'] == 'FAIL':
            self._log_to_elastic('CRITICAL', attributes['message'])

    # def close(self):
    #     self.kibana_service.create_user_dashboard(self.robot_name)

    def _log_to_elastic(self, level, message, cnpj=None):
        try:
            if self.publish_to_elastic:
                if not self.robot_name:
                    self.robot_name = \
                        self.bi.get_variable_value(
                            '${SUITE NAME}').lower().replace(' ', '-')
                log_level = 'INFO' if level == 'FAIL' else level
                robot_log = RobotLog(message=message,
                                     robot_name=self.robot_name,
                                     level=log_level,
                                     cnpj=cnpj)
                robot_log.save()
        except Exception as e:
            error_message = """
                Ocorreu um erro inesperado ao salvar o log no ElasticSearch.
                Log: {log}
                erro: {error}
            """
            logger.error(error_message.format(log=message, error=e))
            self.publish_to_elastic = False

    def _log_suite_to_elastic(self, status, duration):
        try:
            if self.publish_to_elastic:
                suite_log = SuiteLog(robot_name=self.robot_name,
                                     status=status, duration=duration)
                suite_log.save()
            else:
                logger.warn(
                    "A publicação da suite para o Elasticsearch estÃ¡ "
                    "desativada")
        except Exception as e:
            error_message = """
                Ocorreu um erro inesperado ao salvar o log de Suite.
                Status: {status}
                erro: {error}
            """
            logger.error(error_message.format(
                status=f'{status}-{duration}', error=e))
            self.publish_to_elastic = False
