from odoo import _, models, fields, api
from odoo.exceptions import ValidationError, UserError
from odoo.addons.sm_maintenance.models.models_sm_utils import sm_utils

import logging
_logger = logging.getLogger(__name__)
try:
  from stdnum.es.nie import is_valid as valid_nie
except (ImportError, IOError) as err:
  _logger.debug(err)


class SubscriptionRequest(models.Model):
  _inherit = ['subscription.request', 'mail.thread']
  _name = "subscription.request"

  # iban = fields.Char(required=True)

  state_id = fields.Many2one('res.country.state', string=_("State"))
  mobile = fields.Char(string=_("Mobile"))
  must_register_in_cs = fields.Boolean(string=_("Must register in carsharing"))
  driving_license_expiration_date = fields.Char(string=_("Driving license expiration date"))
  image_dni = fields.Char(string=_("DNI image"))
  image_driving_license = fields.Char(string=_("Driving license image"))
  external_obj_id = fields.Integer(string=_("External obj id"))
  related_registration_ids = fields.One2many(comodel_name='sm_partago_user.carsharing_registration_request',
    inverse_name='related_subscription_id', string=_("Related Registrations"))
  representative_vat = fields.Char(string=_("Representative VAT"))
  validation_cron_executed = fields.Boolean(string=_("Validate cron executed"))

  def get_partner_company_vals(self):
    values = super().get_partner_company_vals()
    values["state_id"] = self.state_id.id
    values["mobile"] = self.mobile
    values["driving_license_expiration_date"] = self.driving_license_expiration_date
    values["image_dni"] = self.image_dni
    values["image_driving_license"] = self.image_driving_license
    return values

  def get_partner_vals(self):
    values = super().get_partner_vals()
    values["state_id"] = self.state_id.id
    values["mobile"] = self.mobile
    values["driving_license_expiration_date"] = self.driving_license_expiration_date
    values["image_dni"] = self.image_dni
    values["image_driving_license"] = self.image_driving_license
    return values

  # TODO: Might be useful if invoice not defined as expected
  def get_invoice_vals(self, partner):
      invoice_vals = super().get_invoice_vals(partner)
      #if self.payment_type == 'split':
      #    invoice_vals['payment_term_id'] = self.env.ref(
      #        'somconnexio.account_payment_term_10months'
      #    ).id
      company = self.env.user.company_id
      if company.subscription_invoice_payment_mode_id:
        invoice_vals[
          'payment_mode_id'
          ] = company.subscription_invoice_payment_mode_id.id
      return invoice_vals
  @api.model
  def name_search(self, name, args=None, operator='ilike', limit=100):
    if name:
      records = self.env['subscription.request'].search([
        '|', '|', '|', '|',
        ('vat', operator, name),
        ('email', operator, name),
        ('firstname', operator, name),
        ('lastname', operator, name),
        ('name', operator, name),
        ],
        limit=limit
      )
      return models.lazy_name_get(records)
    else:
      return super().name_search(name, args=args, operator=operator, limit=limit)
    return []

  # TODO: not working bank validation
  @api.multi
  def validate_subscription_request(self):
    self.ensure_one()
    if not sm_utils.validate_iban(self,self.iban) and not self.skip_control_ng:
      raise ValidationError(_("Invalid bank."))
    if self.ordered_parts > 0:
      return self._validate_member_subscription_request()
    elif self.ordered_parts <= 0 and not self.skip_control_ng:
      raise UserError(_("Number of share must be greater than 0."))

  def _validate_member_subscription_request(self):
    self.ensure_one()
    # todo rename to validate (careful with iwp dependencies)

    self.partner = self.get_create_partner()

    self.write({"state": "done"})

    # Create invoice for shares
    invoice = self.create_invoice(self.partner)

    return invoice

  def get_create_partner(self):
    if self.partner_id:
      partner = self.partner_id
    else:
      partner = None
      if self.already_cooperator:
        raise UserError(
          _(
            "The checkbox already cooperator is"
            " checked please select a cooperator."
          )
        )
      elif self.vat:
        domain = [("vat", "ilike", self.vat)]
        partner = self.env["res.partner"].search(domain)

      if not partner:
        partner = self.create_coop_partner()
        if not partner.vat and self.vat:
          partner.vat = self.vat
        self.partner_id = partner
        if self.related_registration_ids:
          self.related_registration_ids[0].related_member_id = partner.id
      else:
        raise UserError(
          _(
            "A partner with VAT %s already exists in our system"
          ) % self.vat
        )
      partner.cooperator = True

    if self.is_company and not partner.has_representative():
      contact = False
      contact_vals = self.get_representative_vals()
      if self.representative_vat:
        contact_vals['vat'] = self.representative_vat
      contact = self.env["res.partner"].create(contact_vals)
      if not contact:
        raise UserError("Could not create representative partner")
    
    # Assign representative_vat here instead? For existing and new partners
    return partner

  @api.model
  def cron_validate_subscriptions_request(self):
    subscriptions = self.env['subscription.request'].search([('state', '=', 'draft'),('type','=','new'),('validation_cron_executed','=',False)])
    for subscription in subscriptions:
      try:
        subscription.validate_subscription_request()
      except Exception as err:
        sm_utils.create_system_task(self,"Subscription Validation error", str(err) + " on Subscription ID: " + str(subscription.id))
      subscription.write({'validation_cron_executed':True})