from elasticsearch import Elasticsearch
from robot.api import logger
from datetime import datetime
import pytz
import os

PUBLISH_TO_ELASTIC = os.environ.get("PUBLISH_TO_ELASTIC", True)
ELASTICSEARCH_HOST = os.environ.get(
    "ELASTICSEARCH_HOST", "https:localhost:9200/")
ENVIRONMENT = os.environ.get("ENVIRONMENT", "dev")
CLIENT = os.environ.get("CLIENT", "xyz")
ROBOT_NAME = os.environ.get("ROBOT_NAME", "Google")


# TODO Exemplo de classe para conexão com o Elastic
class Elastic:
    tz = pytz.timezone("America/Sao_Paulo")

    def __init__(self) -> None:
        self.es = Elasticsearch(
            hosts=ELASTICSEARCH_HOST
        )
        self.index = datetime.today().strftime(
            f"robot-logs-{ENVIRONMENT}-{CLIENT}-{ROBOT_NAME}-%Y.%m")

    def publish(self, message, **fields):
        timestamp = datetime.now(self.tz)
        doc = {
            "message": message,
            "timestamp": timestamp
        }
        try:
            for key, value in fields.items():
                doc.update({key: value})
            resultado = self.es.index(
                index=self.index, body=doc)
            return resultado
        except Exception as e:
            logger.error(
                f"Erro ao tentar logar no ElasticSearch. Detalhes: {e}",
                html=True)
