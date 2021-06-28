# -*- coding: utf-8 -*-


# from odoo.addons.sm_rest_api.models.models import validate_request
from odoo.addons.base_rest.controllers import main
from odoo.http import Controller, ControllerType, Response, request, route


class PartnerRestPublicApiController(main.RestController):
  _root_path = '/sm-api/public/'
  _collection_name = 'partago_partner.rest.public.services'
  _default_auth = 'public'
