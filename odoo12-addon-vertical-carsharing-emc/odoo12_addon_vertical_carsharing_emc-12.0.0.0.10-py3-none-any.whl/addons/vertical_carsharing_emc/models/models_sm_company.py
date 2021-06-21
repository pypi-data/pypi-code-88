# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools.translate import _


class sm_company(models.Model):
  _inherit = 'res.company'

  subscription_invoice_payment_mode_id = fields.Many2one('account.payment.mode',
    string=_("Payment Mode default for subscription invoices"))