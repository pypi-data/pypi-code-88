from odoo import models

class carsharing_update_data(models.Model):
    _name = 'sm_partago_user.carsharing_update_data'
    _inherit = ["sm_partago_user.carsharing_update_data", "external.id.mixin"]