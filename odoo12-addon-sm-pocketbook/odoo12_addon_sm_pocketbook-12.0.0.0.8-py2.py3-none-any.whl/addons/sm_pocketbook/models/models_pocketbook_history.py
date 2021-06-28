# -*- coding: utf-8 -*-

from odoo.tools.translate import _
from odoo import models, fields, api
from odoo.addons.sm_maintenance.models.models_sm_utils import sm_utils


class pocketbook_history(models.Model):
  _name = 'pocketbook.pocketbook_history'

  name = fields.Char(string=_("Name"), required=True)
  date = fields.Date(string=_("Date"))
  amount = fields.Float(string=_("Amount"))
  related_invoice_id = fields.Many2one('account.invoice', string=_("Related Invoice"))
  # is_rewards_active = fields.Boolean(string=_("Rewards active"), compute="check_is_rewards_active", store=False)
  # related_reward_id = fields.Many2one('sm_rewards.sm_reward', string=_("Related Reward"))
  is_partago_active = fields.Boolean(string=_("Partago active"), compute="check_is_partago_active", store=False)
  related_tariff_id = fields.Many2one('smp.sm_carsharing_tariff', string=_("Related Tariff"))
  # related_report_id = fields.Many2one('smp.sm_report_reservation_compute', string=_("Related Reservation Report"))
  # related_invoice_report_id = fields.Many2one('sm.invoice_report', string=_("Related Invoice Report"))
  obs = fields.Char(string=_("Observations"))
  related_member_id = fields.Many2one('res.partner', string=_("Related Member"))
  htype = fields.Selection(
    [('reward_in', 'Reward IN'),
     ('work_in', 'Work IN'),
     ('tariff_prepayment_in', 'Tariff prepayment IN'),
     ('report_reward_in', 'Reservations report reward IN'),
     ('monthly_fee_in', 'Monthly fee IN'),
     ('manual_in', 'Manual modify IN'),
     ('invoice_out', 'Invoice OUT'),
     ('invoice_report_out', 'Invoice Report OUT'),
     ('manual_out', 'Manual OUT')],
    _('Record type'))

  _order = "date desc"

  # @api.depends('htype')
  # def check_is_rewards_active(self):
  #   for record in self:
  #     if record.htype == 'reward_in':
  #       active = sm_utils.is_module_active(record, 'sm_rewards')
  #       if active:
  #         record.is_rewards_active = True
  #       else:
  #         record.is_rewards_active = False
  #     else:
  #       record.is_rewards_active = False

  @api.depends('htype')
  def check_is_partago_active(self):
    for record in self:
      if record.htype == 'tariff_prepayment_in':
        active = sm_utils.is_module_active(record, 'sm_partago_invoicing')
        if active:
          record.is_partago_active = True
        else:
          record.is_partago_active = False
      else:
        record.is_partago_active = False
