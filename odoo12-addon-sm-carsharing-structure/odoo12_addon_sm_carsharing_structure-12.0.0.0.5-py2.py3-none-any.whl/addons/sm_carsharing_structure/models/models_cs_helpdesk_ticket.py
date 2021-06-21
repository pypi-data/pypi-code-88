# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.tools.translate import _

class cs_helpdesk_ticket(models.Model):
  _name = 'helpdesk.ticket'
  _inherit = 'helpdesk.ticket'

  cs_ticket_type = fields.Selection(selection=[
    ('none', 'None'),
    ('car', 'Car'), 
    ('carconfig', 'CarConfig'), 
    ('pu', 'Production unit'), 
    ('community', 'Community')
    ], default='none', string=_("CS Ticket Type"))

  cs_car_id = fields.Many2one('fleet.vehicle', string=_("CS Car"))
  cs_carconfig_id = fields.Many2one('sm_carsharing_structure.cs_carconfig', string=_("CS Structure: Carconfigs"))
  cs_pu_id = fields.Many2one('sm_carsharing_structure.cs_production_unit', string=_("CS Structure: Production Unit'"))
  cs_community_id = fields.Many2one('sm_carsharing_structure.cs_community', string=_("CS Community"))


  def get_create_wizard_view(self):
    view_ref = self.env['ir.ui.view'].search(
      [('name', '=', 'sm_carsharing_structure.ticket_service_wizard.form')])
    return view_ref.id

  @api.multi
  def ticket_service_wizard(self):
    if self.env.context:
      wizard_id = self.env['sm_carsharing_structure.cs_ticket_service_wizard'].create({
        "service_car_id": self.cs_car_id.id,
        "related_ticket_id": self.id})
      return {
        'type': 'ir.actions.act_window',
        'name': "Create Service",
        'res_model': 'sm_carsharing_structure.cs_ticket_service_wizard',
        'view_type': 'form',
        'view_mode': 'form',
        'res_id': wizard_id.id,
        'view_id': self.get_create_wizard_view(),
        'target': 'new',
        'context': self.env.context
      }


  related_service_ids = fields.One2many('fleet.vehicle.log.services', 'related_ticket_id')
