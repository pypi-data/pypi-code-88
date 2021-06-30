import logging

from werkzeug.exceptions import BadRequest, NotFound

from odoo import _
from odoo.fields import Date

from odoo.addons.base_rest.http import wrapJsonException
from odoo.addons.component.core import Component

from . import schemas
from odoo.addons.sm_maintenance.models.models_api_services_utils import api_services_utils

_logger = logging.getLogger(__name__)

class CSUpdateDataService(Component):
  _inherit = "emc.rest.service"
  _name = "sm_partago_user.carsharing_update_data.services"
  _usage = "cs-update-data"
  _description = """
    Carsharing Data Update / Registration Service
  """

  def get(self, _id):
    record = self.env["sm_partago_user.carsharing_update_data"].search(
      [("id", "=", _id)]
    )
    if record:
      return self._to_dict(record)
    else:
      raise wrapJsonException(
        NotFound(_("No update data record for id %s") % _id)
      )

  def create(self, **params):  # pylint: disable=method-required-super
    params = self._prepare_create(params)
    record = self.env["sm_partago_user.carsharing_update_data"].create(params)
    return self._to_dict(record)

  def update(self, _id, **params):
    params = self._prepare_create(params)
    record = self.env["sm_partago_user.carsharing_update_data"].search(
      [("_api_external_id", "=", _id)]
    )
    if not record:
      raise wrapJsonException(
        NotFound(_("No update data record for id %s") % _id)
      )
    record.write(params)
    return self._to_dict(record)

  def validate(self, _id, **params):
    record = self.env["sm_partago_user.carsharing_update_data"].search(
      [("_api_external_id", "=", _id)]
    )
    if not record:
      raise wrapJsonException(
        NotFound(_("No record for id %s") % _id)
      )
    return self._to_dict(record)

  """Prepare a writable dictionary of values"""
  def _prepare_create(self, params):
    utils = api_services_utils.get_instance()
    attributes = {
      "form_id",
      "cs_update_type",
      "cs_update_dni",
      "cs_update_name",
      "cs_update_first_surname",
      "cs_update_second_surname",
      "cs_update_dni_image",
      "cs_update_image_driving_license",
      "cs_update_email",
      "cs_update_mobile",
      "cs_update_birthday",
      "cs_update_driving_license_expiration_date",
      "cs_update_cif",
      "cs_update_group",
      "cs_update_group_secondary",
      "cs_update_comments"
    }
    return utils.generate_create_dictionary(params, attributes)

  def _to_dict(self, record):
    record.ensure_one()
    utils = api_services_utils.get_instance()
    attributes = {
      "form_id",
      "cs_update_type",
      "cs_update_dni",
      "cs_update_name",
      "cs_update_first_surname",
      "cs_update_second_surname",
      "cs_update_dni_image",
      "cs_update_image_driving_license",
      "cs_update_email",
      "cs_update_mobile",
      "cs_update_birthday",
      "cs_update_driving_license_expiration_date",
      "cs_update_cif",
      "cs_update_group",
      "cs_update_group_secondary",
      "cs_update_comments",
      "final_state"
    }
    return utils.generate_get_dictionary(record, attributes)

  def _validator_get(self):
    return schemas.S_CS_UPDATE_DATA_GET

  def _validator_return_get(self):
    return schemas.S_CS_UPDATE_DATA_RETURN_GET

  def _validator_create(self):
    return schemas.S_CS_UPDATE_DATA_CREATE

  def _validator_return_create(self):
    return schemas.S_CS_UPDATE_DATA_RETURN_GET

  def _validator_update(self):
    return schemas.S_CS_UPDATE_DATA_UPDATE

  def _validator_return_update(self):
    return schemas.S_CS_UPDATE_DATA_RETURN_GET

  def _validator_validate(self):
    return schemas.S_CS_UPDATE_DATA_VALIDATE

  def _validator_return_validate(self):
    return schemas.S_CS_UPDATE_DATA_RETURN_GET