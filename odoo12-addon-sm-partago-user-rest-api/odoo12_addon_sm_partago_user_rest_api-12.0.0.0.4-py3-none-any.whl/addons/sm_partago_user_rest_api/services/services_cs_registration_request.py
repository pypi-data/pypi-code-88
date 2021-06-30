import logging

from werkzeug.exceptions import BadRequest, NotFound

from odoo import _
from odoo.fields import Date

from odoo.addons.base_rest.http import wrapJsonException
from odoo.addons.component.core import Component

from . import schemas
from odoo.addons.sm_maintenance.models.models_api_services_utils import api_services_utils

_logger = logging.getLogger(__name__)

class RegistrationRequestService(Component):
  _inherit = "emc.rest.service"
  _name = "sm_partago_user.carsharing_registration_request.services"
  _usage = "cs-registration-request"
  _description = """
    Carsharing Registration Request Services
  """

  def get(self, _id):
    registration = self.env["sm_partago_user.carsharing_registration_request"].search(
      [("id", "=", _id)]
    )
    if registration:
      return self._to_dict(registration)
    else:
      raise wrapJsonException(
        NotFound(_("No registration for id %s") % _id)
      )

  def create(self, **params):  # pylint: disable=method-required-super
    params = self._prepare_create(params)
    registration = self.env["sm_partago_user.carsharing_registration_request"].create(params)
    return self._to_dict(registration)

  def update(self, _id, **params):
    params = self._prepare_create(params)
    registration = self.env["sm_partago_user.carsharing_registration_request"].search(
      [("_api_external_id", "=", _id)]
    )
    if not registration:
      raise wrapJsonException(
        NotFound(_("No registration request for id %s") % _id)
      )
    registration.write(params)
    return self._to_dict(registration)

  def validate(self, _id, **params):
    registration = self.env["sm_partago_user.carsharing_registration_request"].search(
      [("_api_external_id", "=", _id)]
    )
    if not registration:
      raise wrapJsonException(
        NotFound(_("No registration for id %s") % _id)
      )
    return self._to_dict(registration)

  """Prepare a writable dictionary of values"""
  def _prepare_create(self, params):
    utils = api_services_utils.get_instance()
    attributes = {
      "force_registration",
      "group_index",
      "ba_behaviour",
      "ba_credits",
      "related_subscription_id",
      "related_member_id",
    }
    result = utils.generate_create_dictionary(params,attributes)
    return result


  def _to_dict(self, record):
    record.ensure_one()
    utils = api_services_utils.get_instance()
    attributes = {
      "force_registration",
      "group_index",
      "ba_behaviour",
      "ba_credits",
      "related_subscription_id",
      "related_member_id",
      "related_coupon_index",
      "completed",
      "completed_date",
      "completed_behaviour"
    }
    return utils.generate_get_dictionary(record,attributes)

  def _validator_get(self):
    return schemas.S_CS_REGISTRATION_REQUEST_GET

  def _validator_return_get(self):
    return schemas.S_CS_REGISTRATION_REQUEST_RETURN_GET

  def _validator_create(self):
    return schemas.S_CS_REGISTRATION_REQUEST_CREATE

  def _validator_return_create(self):
    return schemas.S_CS_REGISTRATION_REQUEST_RETURN_GET

  def _validator_update(self):
    return schemas.S_CS_REGISTRATION_REQUEST_UPDATE

  def _validator_return_update(self):
    return schemas.S_CS_REGISTRATION_REQUEST_RETURN_GET

  def _validator_validate(self):
    return schemas.S_CS_REGISTRATION_REQUEST_VALIDATE

  def _validator_return_validate(self):
    return schemas.S_CS_REGISTRATION_REQUEST_RETURN_GET