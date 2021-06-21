from odoo.tests.common import SavepointCase


class TestPaymentReturn(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super(TestPaymentReturn, cls).setUpClass()
        cls.journal = cls.env['account.journal'].create({
            'name': 'Test Sales Journal',
            'code': 'tVEN',
            'type': 'sale',
            'update_posted': True,
        })
        cls.account_type = cls.env['account.account.type'].create({
            'name': 'Test',
            'type': 'receivable',
        })
        cls.account = cls.env['account.account'].create({
            'name': 'Test account',
            'code': 'TEST',
            'user_type_id': cls.account_type.id,
            'reconcile': True,
        })
        cls.partner_expense = cls.env['res.partner'].create({'name': 'PE'})
        cls.bank_journal = cls.env['account.journal'].create({
            'name': 'Test Bank Journal',
            'code': 'BANK',
            'type': 'bank',
            'update_posted': True,
            'default_expense_account_id': cls.account.id,
            'default_expense_partner_id': cls.partner_expense.id,
        })
        cls.bank_journal_2 = cls.env['account.journal'].create({
            'name': 'Test Bank Journal 2',
            'code': 'BANK2',
            'type': 'bank',
            'update_posted': True,
            'default_expense_account_id': cls.account.id,
            'default_expense_partner_id': cls.partner_expense.id,
        })

        cls.account_income = cls.env['account.account'].create({
            'name': 'Test income account',
            'code': 'INCOME',
            'user_type_id': cls.env['account.account.type'].create(
                {'name': 'Test income'}).id,
        })
        cls.partner = cls.env['res.partner'].create({'name': 'Test'})
        cls.partner_1 = cls.env['res.partner'].create({'name': 'Test 1'})
        cls.invoice = cls.env['account.invoice'].create({
            'journal_id': cls.journal.id,
            'account_id': cls.account.id,
            'company_id': cls.env.user.company_id.id,
            'currency_id': cls.env.user.company_id.currency_id.id,
            'partner_id': cls.partner.id,
            'invoice_line_ids': [(0, 0, {
                'account_id': cls.account_income.id,
                'name': 'Test line',
                'price_unit': 50,
                'quantity': 10,
            })]
        })
        cls.reason = cls.env['payment.return.reason'].create({
            'code': 'RTEST',
            'name': 'Reason Test'
        })
        cls.invoice.action_invoice_open()
        cls.receivable_line = cls.invoice.move_id.line_ids.filtered(
            lambda x: x.account_id.internal_type == 'receivable')
        # Invert the move to simulate the payment
        cls.payment_move = cls.invoice.move_id.copy({
            'journal_id': cls.bank_journal.id
        })
        for move_line in cls.payment_move.line_ids:
            move_line.with_context(check_move_validity=False).write({
                'debit': move_line.credit, 'credit': move_line.debit})
        cls.payment_line = cls.payment_move.line_ids.filtered(
            lambda x: x.account_id.internal_type == 'receivable')
        # Reconcile both
        (cls.receivable_line | cls.payment_line).reconcile()
        # Create payment return
        cls.payment_return = cls.env['payment.return'].create(
            {'journal_id': cls.bank_journal.id,
             'line_ids': [
                 (0, 0, {'partner_id': cls.partner.id,
                         'move_line_ids': [(6, 0, cls.payment_line.ids)],
                         'amount': cls.payment_line.credit,
                         'expense_account': cls.account.id,
                         'expense_amount': 10.0,
                         'expense_partner_id': cls.partner.id})]})

    def test_find_match_invoice(self):
        self.payment_return.journal_id = self.bank_journal
        self.payment_return.line_ids.write({
            'partner_id': False,
            'move_line_ids': [(6, 0, [])],
            'amount': 0.0,
            'reference': self.invoice.number,
        })
        self.payment_return.button_match()
        self.assertEquals(
            self.payment_return.line_ids[0].move_line_ids,
            self.payment_line
        )

    def test_find_match_move(self):
        self.payment_return.journal_id = self.bank_journal
        self.payment_line.name = 'test match move line 001'
        self.payment_line.write({
            'name': 'YYY',
            'ref': 'YYY'
        })
        self.payment_return.line_ids.write({
            'partner_id': False,
            'move_line_ids': [(6, 0, [])],
            'amount': 0.0,
            'reference': self.payment_line.move_id.name,
        })
        self.invoice.number = 'XXX'
        self.payment_return.button_match()
        self.assertEquals(
            self.payment_return.line_ids[0].move_line_ids,
            self.payment_line
        )

    def test_find_match_invoice_diff_journal(self):
        self.payment_return.journal_id = self.bank_journal_2
        self.payment_return.line_ids.write({
            'partner_id': False,
            'move_line_ids': [(6, 0, [])],
            'amount': 0.0,
            'reference': self.invoice.number,
        })
        self.payment_return.button_match()
        self.assertFalse(self.payment_return.line_ids[0].move_line_ids)

    def test_find_match_move_diff_journal(self):
        self.payment_return.journal_id = self.bank_journal_2
        self.payment_line.name = 'test match move line 001'
        self.payment_line.write({
            'name': 'YYY',
            'ref': 'YYY'
        })
        self.payment_return.line_ids.write({
            'partner_id': False,
            'move_line_ids': [(6, 0, [])],
            'amount': 0.0,
            'reference': self.payment_line.move_id.name,
        })
        self.invoice.number = 'XXX'
        self.payment_return.button_match()
        self.assertFalse(self.payment_return.line_ids[0].move_line_ids)

    def test_find_match_move_line(self):
        self.payment_return.journal_id = self.bank_journal
        self.payment_line.name = 'test match move line 001'
        self.payment_return.line_ids.write({
            'partner_id': False,
            'move_line_ids': [(6, 0, [])],
            'amount': 0.0,
            'reference': self.payment_line.name,
        })
        self.payment_return.button_match()
        self.assertEquals(
            self.payment_return.line_ids[0].move_line_ids,
            self.payment_line
        )

    def test_find_match_move_line_diff_journal(self):
        self.payment_return.journal_id = self.bank_journal_2
        self.payment_line.name = 'test match move line 001'
        self.payment_return.line_ids.write({
            'partner_id': False,
            'move_line_ids': [(6, 0, [])],
            'amount': 0.0,
            'reference': self.payment_line.name,
        })
        self.payment_return.button_match()
        self.assertFalse(self.payment_return.line_ids[0].move_line_ids)
