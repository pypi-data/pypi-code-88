# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.tools.translate import _

class cs_production_unit(models.Model):
  _name = 'sm_carsharing_structure.cs_production_unit'

  name = fields.Char(string=_("Name"))
  analytic_account_id = fields.Many2one('account.analytic.account',
    string=_("Related analytic account"))
  cs_carconfig_ids = fields.One2many(comodel_name='sm_carsharing_structure.cs_carconfig',
    inverse_name='production_unit_id',
    string=_("CS carconfigs"))
  community_id = fields.Many2one('sm_carsharing_structure.cs_community',
    string=_("Related community"))





