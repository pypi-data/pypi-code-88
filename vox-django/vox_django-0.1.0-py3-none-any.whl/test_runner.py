from django.test.runner import DiscoverRunner
from django_sorcery.db import databases


class TestRunner(DiscoverRunner):
    def __init__(self, **kwargs):
        super(TestRunner, self).__init__(**kwargs)
        self.aliases = []

    def setup_databases(self, **kwargs):
        for alias in kwargs['aliases']:
            self.aliases.append(alias)
            databases.get(alias).create_all()

    def teardown_databases(self, old_config, **kwargs):
        for alias in self.aliases:
            databases.get(alias).drop_all()
