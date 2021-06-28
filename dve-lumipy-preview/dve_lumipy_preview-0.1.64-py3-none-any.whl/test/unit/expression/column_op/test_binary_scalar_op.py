import unittest

from lumipy.query.expression.column.source_column import SourceColumn
from lumipy.query.expression.sql_value_type import SqlValType, numerics
from test.test_utils import make_test_atlas


class TestColumnBinaryScalarOp(unittest.TestCase):

    def setUp(self) -> None:
        self.atlas = make_test_atlas()
        self.appreq = self.atlas.lusid_logs_apprequest()
        self.rtrace = self.atlas.lusid_logs_requesttrace()
        self.test_text_col = self.appreq.request_id
        self.test_double_col = self.appreq.duration
        self.test_int_col = self.appreq.error_code.cast(int)

    def test_is_in_variants(self):

        other = self.appreq.select(self.appreq.request_id).where(
            self.appreq.duration > 1000
        ).to_table_var('other')

        is_in_sql = self.appreq.request_id.is_in(other.select(other.request_id)).get_sql()

        test_sql = self.appreq.select('^').where(
            self.appreq.request_id.is_in(
                other.select(other.request_id)
            )
        ).get_sql()
        pass

    def test_new_scalar_op_base(self):

        duration = self.appreq.duration
        test = (duration + 1) + 100
        test_sql = test.get_sql()

        self.assertEqual(test_sql, '([Duration] + 1) + 100')

    def test_is_in_with_list(self):

        is_in_sql = self.appreq.application.is_in(['shrine', 'lusid']).get_sql()
        self.assertEqual(is_in_sql, "[Application] in ('shrine', 'lusid')")

    def test_membership_container(self):

        from lumipy.query.expression.column.collection import CollectionExpression

        container1 = CollectionExpression(self.appreq.select(self.appreq.duration))
        container1_sql = container1.get_sql()
        self.assertEqual(container1_sql, "(select [Duration] from Lusid.Logs.AppRequest)")

        container2 = CollectionExpression(*["a", "b", "c"])
        container2_sql = container2.get_sql()

        self.assertEqual(container2_sql, "('a', 'b', 'c')")

    def test_is_in_prefixing_reconstruction(self):

        appreq_alias = self.appreq.with_alias('test')
        rtrace_alias = self.rtrace.with_alias('RT')

        is_in = self.appreq.application.is_in(['shrine', 'lusid'])
        prfx_is_in = appreq_alias.apply_prefix(is_in)

        sql_prfx_is_in = prfx_is_in.get_sql()
        self.assertEqual(sql_prfx_is_in, "test.[Application] in ('shrine', 'lusid')")

        rids = self.appreq.select('*').where(self.appreq.duration > 10000).to_table_var('rids').with_alias('RIDS')

        cndn = self.rtrace.request_id.is_in(rids.select(rids.request_id))
        prfx_cndn = rids.apply_prefix(rtrace_alias.apply_prefix(cndn))

        prfx_cndn_sql = prfx_cndn.get_sql()
        self.assertEqual(prfx_cndn_sql, 'RT.[RequestId] in (select RIDS.[RequestId] from @rids as RIDS)')

    # noinspection SpellCheckingInspection
    def test_numeric_binary_op_source_and_literal_cols(self):

        const = 2.0
        test_ops = {
            'mul': lambda x: x * const,
            'div': lambda x: x / const,
            'add': lambda x: x + const,
            'sub': lambda x: x - const,
            'mod': lambda x: x % const,
        }

        for p_description in self.atlas.list_providers():

            p_hash = hash(p_description)

            for c_description in p_description.list_columns():

                if c_description.data_type in numerics:
                    for name, op in test_ops.items():
                        col = SourceColumn(c_description, p_hash)
                        expr = op(col)

                        self.assertTrue(name in expr.get_name())
                        self.assertEqual(expr.source_table_hash(), col.source_table_hash())
                        self.assertEqual(len(expr.get_lineage()), 2)

                if c_description.data_type == SqlValType.Text:
                    col = SourceColumn(c_description, p_hash)
                    expr = col.concat('_ABCD')

                    self.assertTrue('_conc_' in expr.get_name())
                    self.assertEqual(expr.source_table_hash(), col.source_table_hash())
                    self.assertEqual(len(expr.get_lineage()), 2)

    def test_numeric_binary_op_two_source_cols(self):

        test_ops = {
            'mul': lambda x, y: x * y,
            'div': lambda x, y: x / y,
            'add': lambda x, y: x + y,
            'sub': lambda x, y: x - y,
            'mod': lambda x, y: x % y,
        }

        for p_description in self.atlas.list_providers():
            p_hash = hash(p_description)
            numeric_fields = [SourceColumn(c, p_hash) for c in p_description.list_columns() if c.data_type in numerics]
            for col1 in numeric_fields:
                for col2 in numeric_fields:
                    for name, op in test_ops.items():
                        expr = op(col1, col2)
                        self.assertTrue(name in expr.get_name())
                        self.assertEqual(expr.source_table_hash(), col1.source_table_hash())
                        self.assertEqual(len(expr.get_lineage()), 2)

    def test_degenerate_expression_args_bug(self):

        provider1 = self.atlas.lusid_logs_apprequest()
        provider2 = self.atlas.lusid_logs_apprequest()
        v1 = provider1.duration / 2
        v2 = provider2.duration / 2

        v3 = v1 + v2
        self.assertEqual(v3.get_sql(), f"({v1.get_sql()}) + ({v2.get_sql()})")

    def test_regexp_binary_op_sql(self):

        pattern = '^.*?$'
        self.assertEqual(self.test_text_col.regexp(pattern).get_sql(),
                         f"{self.test_text_col.get_sql()} regexp '{pattern}'")
        self.assertEqual(self.test_text_col.not_regexp(pattern).get_sql(),
                         f"{self.test_text_col.get_sql()} not regexp '{pattern}'")
        self.assertRaises(TypeError, lambda p: self.test_double_col.regexp(p), pattern)
        self.assertRaises(TypeError, lambda p: self.test_double_col.not_regexp(p), pattern)

    def test_power_expressions(self):

        # Test expressions raised to a power
        for n in range(5):
            int_pow = self.test_int_col**n
            self.assertEqual(int_pow.get_sql(), f'power(({self.test_int_col.get_sql()}), {n})')
            self.assertEqual(int_pow.get_type(), SqlValType.Int)

            dbl_pow = self.test_double_col ** n
            self.assertEqual(dbl_pow.get_sql(), f'power({self.test_double_col.get_sql()}, {n})')
            self.assertEqual(dbl_pow.get_type(), SqlValType.Double)

        # Test literals raised to the power of an expression
        two_to_dbl = 2**self.test_double_col
        self.assertEqual(two_to_dbl.get_sql(), f'power(2, {self.test_double_col.get_sql()})')
        self.assertEqual(two_to_dbl.get_type(), SqlValType.Double)

        two_to_int = 2**self.test_int_col
        self.assertEqual(two_to_int.get_sql(), f'power(2, ({self.test_int_col.get_sql()}))')
        self.assertEqual(two_to_int.get_type(), SqlValType.Int)

    def test_round_expression(self):

        # No number of places specified evals to zero places
        round_none1 = self.test_double_col.round()
        round_none2 = round(self.test_double_col)
        self.assertEqual(round_none2.get_sql(), round_none1.get_sql())
        self.assertEqual(round_none1.get_type(), SqlValType.Double)
        self.assertEqual(round_none1.get_sql(), f"round({self.test_double_col.get_sql()}, 0)")

        for n in range(3):
            rounded = round(self.test_double_col, n)
            self.assertEqual(rounded.get_sql(), f'round({self.test_double_col.get_sql()}, {n})')

    def test_cast_in_prefix_insertion(self):

        table = self.appreq.with_alias('test')

        trunc_sec = (self.appreq.duration*0.001).cast(int)
        prefixed = table.apply_prefix(trunc_sec)
        sql = prefixed.get_sql()
        self.assertEqual(sql, 'cast(test.[Duration] * 0.001 as INT)')

    def test_round_in_prefix_insertion(self):

        table = self.appreq.with_alias('test')

        nearest_sec = round(self.appreq.duration*0.001)
        prefixed = table.apply_prefix(nearest_sec)
        sql = prefixed.get_sql()
        self.assertEqual(sql, 'round((test.[Duration] * 0.001), 0)')

    def test_power_in_prefix_insertion(self):

        table = self.appreq.with_alias('test')

        cube_sec = self.appreq.duration ** 3
        prefixed = table.apply_prefix(cube_sec)
        sql = prefixed.get_sql()
        self.assertEqual(sql, 'power(test.[Duration], 3)')
