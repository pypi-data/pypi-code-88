# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools.translate import _


class sm_company(models.Model):
  _inherit = 'res.company'

  cs_already_active = fields.Many2one('mail.template',
    string=_("CS already active"))
  cs_already_requested_access = fields.Many2one('mail.template',
    string=_("CS access already requested"))
  cs_company_access_already_requested = fields.Many2one('mail.template',
    string=_("CS company access already requested"))
  cs_missing_data_email_template_id = fields.Many2one('mail.template',
    string=_("CS missing data email"))
  cs_complete_data_soci_not_found_email_template_id = fields.Many2one('mail.template',
    string=_("CS complete data soci not found"))
  cs_complete_data_successful_email_template_id = fields.Many2one('mail.template',
    string=_("CS complete data successful"))