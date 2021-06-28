# -*- coding: utf-8 -*-
from odoo import fields, models, _

class ResConfigSettings(models.TransientModel):
  _inherit = 'res.config.settings'

  cs_reward_completed_email_template_id = fields.Many2one(
    related='company_id.cs_reward_completed_email_template_id',
    string=_("CS reward completed"),
    readonly=False)

  cs_reward_soci_not_found_email_template_id = fields.Many2one(
    related='company_id.cs_reward_soci_not_found_email_template_id',
    string=_("CS reward soci not found"),
    readonly=False)

  reward_account_id = fields.Many2one(
    related='company_id.reward_account_id',
    string=_("Coupon reward account"),
    readonly=False)

  reward_analytic_account_id = fields.Many2one(
    related='company_id.reward_analytic_account_id',
    string=_("Coupon reward analytic account"),
    readonly=False)
    