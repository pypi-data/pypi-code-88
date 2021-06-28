# -*- coding: utf-8 -*-

from odoo.tools.translate import _
from odoo import models, fields, api
from odoo.addons.sm_maintenance.models.models_sm_utils import sm_utils


class pocketbook_record_history(models.Model):
  _name = 'pocketbook.pocketbook_record_history'

  name = fields.Char(string=_("Name"), required=True)
  date = fields.Date(string=_("Date"))
  amount = fields.Float(string=_("Amount"))
  related_invoice_line_id = fields.Many2one('account.invoice.line', string=_("Related Invoice Line"))
  obs = fields.Char(string=_("Observations"))
  related_pb_record_id = fields.Many2one('pocketbook.pocketbook_record', string=_("Related record"))

  _order = "date desc"