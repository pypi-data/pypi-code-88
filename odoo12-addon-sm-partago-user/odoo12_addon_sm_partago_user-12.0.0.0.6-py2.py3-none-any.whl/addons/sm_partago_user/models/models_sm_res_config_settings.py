# -*- coding: utf-8 -*-
from odoo import fields, models, _

class ResConfigSettings(models.TransientModel):
  _inherit = 'res.config.settings'

  cs_already_active = fields.Many2one(
    related='company_id.cs_already_active',
    string=_("CS user already active"),
    readonly=False)

  cs_already_requested_access = fields.Many2one(
    related='company_id.cs_already_requested_access',
    string=_("CS access already requested"),
    readonly=False)

  cs_company_access_already_requested = fields.Many2one(
    related='company_id.cs_company_access_already_requested',
    string=_("CS company access already requested"),
    readonly=False)

  cs_missing_data_email_template_id = fields.Many2one(
    related='company_id.cs_missing_data_email_template_id',
    string=_("CS missing data email"),
    readonly=False)

  cs_complete_data_soci_not_found_email_template_id = fields.Many2one(
    related='company_id.cs_complete_data_soci_not_found_email_template_id',
    string=_("CS complete data soci not found"),
    readonly=False)

  cs_complete_data_successful_email_template_id = fields.Many2one(
    related='company_id.cs_complete_data_successful_email_template_id',
    string=_("CS complete data successful"),
    readonly=False)
