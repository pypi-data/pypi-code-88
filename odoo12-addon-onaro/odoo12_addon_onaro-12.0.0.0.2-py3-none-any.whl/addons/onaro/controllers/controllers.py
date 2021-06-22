from odoo.addons.base_rest.controllers import main


class CrmLeadController(main.RestController):
    _root_path = "/api/"
    _collection_name = "onaro.services"
    _default_auth = "api_key"
