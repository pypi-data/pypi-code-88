from django_sorcery.db import databases
from health_check.backends import BaseHealthCheckBackend
from health_check.exceptions import HealthCheckException

db = databases.get("default")


class DatabaseHealthCheck(BaseHealthCheckBackend):
    critical_service = True

    def check_status(self):
        try:
            return db.execute('SELECT 1 FROM DUAL')
        except Exception as e:
            raise HealthCheckException(str(e))

    def identifier(self):
        return 'Database'
