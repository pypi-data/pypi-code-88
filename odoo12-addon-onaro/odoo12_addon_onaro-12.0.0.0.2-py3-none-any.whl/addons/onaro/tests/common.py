import requests

import odoo

from odoo.addons.base_rest.tests.common import BaseRestCase

HOST = "127.0.0.1"
PORT = odoo.tools.config["http_port"]


class BaseEMCRestCase(BaseRestCase):
    @classmethod
    def setUpClass(cls, *args, **kwargs):
        super().setUpClass(*args, **kwargs)
        cls.AuthApiKey = cls.env["auth.api.key"]
        cls.api_key_test = cls.env.ref("onaro.auth_api_key_manager_emc_demo")

    def setUp(self):
        super().setUp()
        self.session = requests.Session()

    def _add_api_key(self, headers):
        key_dict = {"API-KEY": self.api_key_test.key}
        if headers:
            headers.update(key_dict)
        else:
            headers = key_dict
        return headers
