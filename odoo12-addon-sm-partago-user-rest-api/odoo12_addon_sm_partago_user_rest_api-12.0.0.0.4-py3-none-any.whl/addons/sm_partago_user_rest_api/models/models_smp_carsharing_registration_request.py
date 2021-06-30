from odoo import models

class carsharing_registration_request(models.Model):
    _name = 'sm_partago_user.carsharing_registration_request'
    _inherit = ["sm_partago_user.carsharing_registration_request", "external.id.mixin"]