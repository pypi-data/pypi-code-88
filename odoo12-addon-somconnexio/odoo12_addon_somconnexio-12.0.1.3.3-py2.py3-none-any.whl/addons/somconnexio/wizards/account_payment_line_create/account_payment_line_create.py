from odoo import models, fields, api


class AccountPaymentLineCreate(models.TransientModel):
    _inherit = 'account.payment.line.create'
    limit_enabled = fields.Boolean('Split in new payment orders?', default=True)
    limit = fields.Integer('Group maximum lines', default=1000)
    queue_enabled = fields.Boolean('Do it in background?', default=True)

    @api.multi
    def create_payment_lines(self):
        if self.limit_enabled and self.move_line_ids:
            move_line_pool = self.env['account.move.line']
            limit = self.limit
            num_groups = len(self.move_line_ids) // limit
            if len(self.move_line_ids) % limit:
                num_groups += 1
            g = self.move_line_ids[0:limit]
            if self.queue_enabled:
                move_line_pool.with_delay(
                    priority=50
                ).create_payment_line_from_move_line_queued(
                    g.ids, self.order_id.id
                )
            else:
                g.create_payment_line_from_move_line(
                    self.order_id
                )
            for g in [
                self.move_line_ids[n*limit:(n+1)*limit]
                for n in range(1, num_groups)
            ]:
                order_id = self.order_id.copy()
                if self.queue_enabled:
                    move_line_pool.with_delay(
                        priority=50
                    ).create_payment_line_from_move_line_queued(
                        g.ids, order_id.id
                    )
                else:
                    g.create_payment_line_from_move_line(order_id)
        else:
            super().create_payment_lines()
        return True
