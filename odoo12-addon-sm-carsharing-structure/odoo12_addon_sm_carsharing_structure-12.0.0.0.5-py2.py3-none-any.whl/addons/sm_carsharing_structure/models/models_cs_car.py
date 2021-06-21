# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.tools.translate import _

class cs_car(models.Model):
  _name = 'fleet.vehicle'
  _inherit = 'fleet.vehicle'

  db_car_id = fields.Many2one('smp.sm_car',string=_("DB APP: Car"))
  analytic_account_id = fields.Many2one('account.analytic.account', string=_("Related analytic account"))
  db_carconfigs_id = fields.One2many('smp.sm_car_config', string=_('DB APP: Carconfigs'), compute="_get_db_carconfigs_id",store=False)
  cs_carconfigs_id = fields.One2many('sm_carsharing_structure.cs_carconfig', string=_('CS Structure: Carconfigs'), compute="_get_cs_carconfigs_id",store=False)
  cs_production_units_id = fields.One2many('sm_carsharing_structure.cs_production_unit', string=_('CS Structure: Production Unit'), compute="_get_cs_production_units_id",store=False)
  cs_communities_id = fields.One2many('sm_carsharing_structure.cs_community', string=_('CS Structure: Community'), compute="_get_cs_communities_id",store=False)
  db_car_owner_group_index = fields.Char(string=_("DB APP: Owner Group"),compute="_get_db_car_owner_group_index",store=True)
  # Vehicle type should be Many2one? to which model?
  vehicle_type = fields.Selection([
    ('car', 'Car'),
    ('bike', 'Bike'),
    ('van', 'Van'),
    ('cargo-bike', 'Cargo Bike')
  ],default='car',required=True, string='Vehicle type')
  cs_task_ids = fields.One2many('project.task', 'cs_task_car_id', string=_("Related Tasks"))

  @api.depends('db_car_id')
  def _get_db_carconfigs_id(self):
    for record in self:
      if record.db_car_id:
        record.db_carconfigs_id = record.db_car_id.db_carconfigs_id

  @api.depends('db_car_id')
  def _get_db_car_owner_group_index(self):
    for record in self:
      if record.db_car_id:
        record.db_car_owner_group_index = record.db_car_id.owner_group_index

  @api.depends('db_carconfigs_id')
  def _get_cs_carconfigs_id(self):
    for record in self:
      cs_carconfigs = []
      if record.db_carconfigs_id:
        for db_carconfig in record.db_carconfigs_id:
          if db_carconfig.cs_carconfig_ids:
            for cs_carconfig in db_carconfig.cs_carconfig_ids:
              cs_carconfigs.append((4,cs_carconfig.id))
      record.cs_carconfigs_id = cs_carconfigs

  @api.depends('cs_carconfigs_id')
  def _get_cs_production_units_id(self):
    for record in self:
      cs_pus = []
      if record.cs_carconfigs_id:
        for cs_carconfig in record.cs_carconfigs_id:
          cs_pus.append((4,cs_carconfig.production_unit_id.id))
      record.cs_production_units_id = cs_pus

  @api.depends('cs_carconfigs_id')
  def _get_cs_communities_id(self):
    for record in self:
      cs_cs = []
      if record.cs_carconfigs_id:
        for cs_carconfig in record.cs_carconfigs_id:
          cs_cs.append((4,cs_carconfig.community_id.id))
      record.cs_communities_id = cs_cs






