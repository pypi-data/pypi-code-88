# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.tools.translate import _

class cs_car_service(models.Model):
  _name = 'fleet.vehicle.log.services'
  _inherit = 'fleet.vehicle.log.services'
  related_member_id = fields.Many2one('res.partner',string=_("Related Member"))
  related_invoice_id = fields.Many2one('account.invoice',string=_("Related Invoice"),domain=[('type', '=', 'in_invoice')])

  #One2one relation to a task
  related_task_id = fields.Many2one('project.task', string=_("Related task"))
  related_ticket_id = fields.Many2one('helpdesk.ticket', string=_("Related helpdesk ticket"))






