# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.tools.translate import _
from odoo.addons.sm_maintenance.models.models_sm_utils import sm_utils

class cs_helpdesk_ticket_service_wizard(models.TransientModel):
  _name = 'sm_carsharing_structure.cs_ticket_service_wizard'

  service_car_id = fields.Many2one('fleet.vehicle', string=_("Car"))
  service_type_id = fields.Many2one('fleet.service.type', string=_("Service Type"))
  amount = fields.Float(string=_("Total cost"))
  related_member_id = fields.Many2one('res.partner',string=_("Related Member"))
  vendor_id = fields.Many2one('res.partner',string=_("Vendor"))
  related_invoice_id = fields.Many2one('account.invoice',string=_("Related Invoice"))
  date = fields.Date(string=_("Date"), default=sm_utils.get_today_date())

  related_ticket_id = fields.Many2one('helpdesk.ticket')

  def create_service(self):
    self.env['fleet.vehicle.log.services'].create({
      'vehicle_id': self.service_car_id.id,
      'cost_subtype_id': self.service_type_id.id,
      'amount': float(self.amount),
      'date': self.date,
      'related_member_id': self.related_member_id.id,
      'related_ticket_id': self.related_ticket_id.id,
      'vendor_id': self.vendor_id.id,
      'related_invoice_id': self.related_invoice_id.id
    })