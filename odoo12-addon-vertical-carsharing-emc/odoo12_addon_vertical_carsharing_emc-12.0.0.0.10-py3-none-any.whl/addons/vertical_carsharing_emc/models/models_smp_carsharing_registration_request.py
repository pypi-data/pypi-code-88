# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.tools.translate import _

class carsharing_registration_request(models.Model):
  _name = 'sm_partago_user.carsharing_registration_request'
  _inherit = 'sm_partago_user.carsharing_registration_request'
  related_subscription_id = fields.Many2one('subscription.request', string=_("Related Subscription Request"))