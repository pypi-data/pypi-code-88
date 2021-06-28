# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools.translate import _

class sm_company(models.Model):
  _inherit = 'res.company'

  cs_reward_completed_email_template_id = fields.Many2one('mail.template',
    string=_("CS reward completed"))
  cs_reward_soci_not_found_email_template_id = fields.Many2one('mail.template',
    string=_("CS reward soci not found"))
  reward_account_id = fields.Many2one('account.account', string=_("Reward account"))
  reward_analytic_account_id = fields.Many2one('account.analytic.account',
    string=_("Reward analytic account"))