# -*- coding: utf-8 -*-

from datetime import datetime

from odoo import models, fields, api
from odoo.tools.translate import _


class sm_member(models.Model):
  _inherit = 'res.partner'

  cs_pocketbook = fields.Float(string=_("Pocketbook"))
  pocketbook_record_ids = fields.One2many(comodel_name='pocketbook.pocketbook_record',
      inverse_name ='related_member_id',string=_("Pocketbook lines"))
  pocketbook_records_total = fields.Float(compute="_calculate_pb_records_total")
  pocketbook_records_total_taxed = fields.Float(compute="_calculate_pb_records_total_taxed")

  @api.depends('pocketbook_record_ids')
  def _calculate_pb_records_total(self):
    for record in self:
      for pb_record in record.pocketbook_record_ids:
        record.pocketbook_records_total += pb_record.amount

  @api.depends('pocketbook_record_ids')
  def _calculate_pb_records_total_taxed(self):
    for record in self:
      #TODO: this should be dynamic when create multiinstance
      record.pocketbook_records_total_taxed = record.pocketbook_records_total + 0.21*record.pocketbook_records_total

  @api.model
  def get_pocketbook_update_view(self):
    view_ref = self.env['ir.ui.view'].sudo().search([('name', '=', 'pocketbook.pocketbook_history_wizard.form')])
    return view_ref.id

  @api.model
  def update_member_pocketbook_from_action(self):
    if self.env.context:
      if 'active_ids' in self.env.context:
        members = self.env['res.partner'].browse(self.env.context['active_ids'])
        if members.exists():
          for member in members:
            data = {'current_member': member.id}
            return {
              'type': 'ir.actions.act_window',
              'name': "Update pocketbook",
              'res_model': 'pocketbook.pocketbook_history_wizard',
              'view_type': 'form',
              'view_mode': 'form',
              'res_id': self.env['pocketbook.pocketbook_history_wizard'].create(data).id,
              'view_id': self.get_pocketbook_update_view(),
              'target': 'new',
            }
