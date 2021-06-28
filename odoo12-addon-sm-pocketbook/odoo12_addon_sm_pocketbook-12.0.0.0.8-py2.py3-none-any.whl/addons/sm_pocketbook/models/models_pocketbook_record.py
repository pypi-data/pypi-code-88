# -*- coding: utf-8 -*-

from odoo.tools.translate import _
from odoo import models, fields, api
from odoo.addons.sm_maintenance.models.models_sm_utils import sm_utils


class pocketbook_record(models.Model):
  _name = 'pocketbook.pocketbook_record'

  name = fields.Char(string=_("Name"), required=True)
  date = fields.Date(string=_("Date"),compute="_get_pocketbook_record_date",store=True)
  amount = fields.Float(string=_("Amount"),compute="_calculate_amount", store=True)
  obs = fields.Char(string=_("Observations"))
  related_member_id = fields.Many2one('res.partner', string=_("Related Member"))
  related_account_id = fields.Many2one('account.account', string=_("Related account"))
  related_analytic_account_id = fields.Many2one('account.analytic.account', string=_("Related analytic account"))
  history_line_ids = fields.One2many(comodel_name='pocketbook.pocketbook_record_history', 
    inverse_name='related_pb_record_id', string=_("History lines"))

  _order = "date asc"

  @api.depends('history_line_ids')
  def _get_pocketbook_record_date(self):
    for record in self:
      if record.history_line_ids:
        record.date = record.history_line_ids[0].date

  @api.depends('history_line_ids')
  def _calculate_amount(self):
    for record in self:
      amount = 0
      for h_line in record.history_line_ids:
        record.amount += h_line.amount
