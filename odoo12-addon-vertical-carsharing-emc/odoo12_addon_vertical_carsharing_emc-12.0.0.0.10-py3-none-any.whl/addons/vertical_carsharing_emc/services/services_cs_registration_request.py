from odoo.addons.component.core import Component

class RegistrationRequestService(Component):
  _inherit = "sm_partago_user.carsharing_registration_request.services"

  def _prepare_create(self, params):
    create_schema = super()._prepare_create(params)
    subscription = self.env["subscription.request"].search(
      [("_api_external_id", "=", create_schema['related_subscription_id'])])
    if subscription:
      create_schema['related_subscription_id'] = subscription.id
    return create_schema