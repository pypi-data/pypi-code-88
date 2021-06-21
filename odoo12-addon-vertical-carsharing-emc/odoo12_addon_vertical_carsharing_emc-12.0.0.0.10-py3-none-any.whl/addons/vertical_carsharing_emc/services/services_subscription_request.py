import logging
from odoo.addons.component.core import Component
from . import schemas
from werkzeug.exceptions import BadRequest
from odoo.addons.base_rest.http import wrapJsonException

from odoo.addons.sm_maintenance.models.models_api_services_utils import api_services_utils

_logger = logging.getLogger(__name__)


class SubscriptionRequestService(Component):
  _inherit = "subscription.request.services"

  def _prepare_create(self, params):
    utils = api_services_utils.get_instance()
    attributes = self._get_attributes_list()
    sr_create_values = utils.generate_create_dictionary(params,attributes)

    address = params["address"]
    country = self._get_country(address["country"])
    state_id = self._get_state(address["state"], country.id)
    sr_create_values_address = {
      "address": address["street"],
      "zip_code": address["zip_code"],
      "city": address["city"],
      "country_id": country.id,
      "state_id": state_id,
      "share_product_id": params["share_product"]
    }
    try:
      birthdate = "{} 00:00:00".format(params["birthdate"])
      sr_create_values_address["birthdate"] = birthdate
    except:
      print("company registration - no birthdate")

    return {**sr_create_values, **sr_create_values_address}

  def _validator_create(self):
    create_schema = super()._validator_create()
    create_schema.update(schemas.S_SUBSCRIPTION_REQUEST_CREATE_SC_FIELDS)
    return create_schema

  def _get_state(self, state, country_id):
    state_id = self.env['res.country.state'].search([
      ('code', '=', state),
      ('country_id', '=', country_id),
    ]).id
    if not state_id:
      raise wrapJsonException(
        BadRequest(
          'State %s not found' % (state)
        ),
        include_description=True,
      )
    return state_id
  
  def _get_attributes_list(self):
   return [
    "name",
    "firstname",
    "lastname",
    "email",
    "phone",
    "lang",
    "iban",
    "ordered_parts",
    "vat",
    "gender",
    "phone",
    "firstname",
    "lastname",
    "is_company",
    "company_name",
    "company_email",
    "mobile",
    "must_register_in_cs",
    "driving_license_expiration_date",
    "image_dni",
    "image_driving_license",
    "external_obj_id",
    "representative_vat"
   ]