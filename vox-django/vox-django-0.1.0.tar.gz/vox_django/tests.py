from unittest import TestCase
from unittest.mock import patch, call, MagicMock

from django.conf import settings
from health_check.exceptions import HealthCheckException
from sqlalchemy_pagination import Page

from vox_django.criptografia import decrypt_aes, encrypt_aes

settings.configure(
    DEBUG=True,
    DATABASES={'default': {
        'ENGINE': 'sqlite'
    }},
    APP_NAME='foo',
    APP_VERSION='1.0',
    HEALTH_CHECK_PLUGINS=[
        'database',
    ],
    INSTALLED_APPS=[
        'vox_django',
    ],
    ORGANIZATION='riachuelo',
)


class TestCriptography(TestCase):
    def test_should_decrypt(self):
        PASS = 'j7ysUJr7buPaE7jNuNyI7g=='

        self.assertEqual(decrypt_aes(PASS), 'simula')

    def test_should_encrypt(self):
        PASS = 'simula'

        self.assertEqual(encrypt_aes(PASS), 'j7ysUJr7buPaE7jNuNyI7g==')


class TestHealthCheckBackends(TestCase):
    @patch('vox_django.healthcheck.backends.db')
    def test_should_healthcheck_database(self, db):
        from vox_django.healthcheck.backends import DatabaseHealthCheck

        DatabaseHealthCheck().check_status()
        db.execute.assert_called()

        db.execute.side_effect = Exception('error')

        with self.assertRaises(HealthCheckException):
            DatabaseHealthCheck().check_status()


class TestMiddleware(TestCase):
    @patch('vox_django.middleware.logging.getLogger')
    def test_should_log_error(self, getLogger):
        from vox_django.middleware import ExceptionMiddleware

        middlwware = ExceptionMiddleware()
        middlwware.process_exception(request={}, error='some error')

        getLogger().error.assert_called_with('some error', extra={"appName": settings.APP_NAME,
                                                                  "appVersion": "1.0.0"})


class TestModels(TestCase):
    @patch('vox_django.models.paginate')
    def test_should_paginate(self, paginate):
        paginate.side_effect = None
        paginate.return_value = Page(items=[], page=1, page_size=10, total=100)
        from vox_django.models import Paginator
        paginator = Paginator('select', 1)

        paginator.__next__()

        self.assertEqual([], paginator.items)
        self.assertEqual(1, paginator.current_page)

    @patch('vox_django.models.paginate')
    def test_should_iterate_pages(self, paginate):
        from vox_django.models import Paginator

        pages_stub = [
            Page(items=[{'test': 1}], page=1, page_size=1, total=2),
            Page(items=[{'test': 2}], page=2, page_size=1, total=2),
        ]

        paginate.side_effect = pages_stub

        pages = Paginator('select', 1)

        cur_page = 0
        for page in pages:
            cur_page += 1
            self.assertEqual(pages.page_number, cur_page)
            self.assertTrue(page in pages_stub)


class TestDjangoApp(TestCase):
    @patch('vox_django.apps.plugin_dir')
    def test_should_install_health_check_plugins(self, plugin_dir):
        from vox_django.apps import VoxDjangoConfig
        from vox_django.healthcheck.backends import DatabaseHealthCheck

        VoxDjangoConfig.path = 'vox_django'
        config = VoxDjangoConfig('foo', 'vox_django')
        config.ready()

        plugin_dir.register.assert_has_calls([
            call(DatabaseHealthCheck),
        ])
