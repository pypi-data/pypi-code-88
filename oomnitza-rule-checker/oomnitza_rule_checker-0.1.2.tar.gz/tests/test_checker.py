#!/usr/bin/env python
from oomnitza_rule_checker.checker import (
    _get_prop_from_field,
    _convert_string_to_timestamp,
    _is_numeric,
    _missed,
    check_rules,
    check_rule_by_op,
    Op,
)

import arrow
import pytest
from pytest_lazyfixture import lazy_fixture


@pytest.mark.parametrize(
    "given_field,given_object_type,expected_result",
    [
        ("ASSETS.serial_number", "ASSETS", "serial_number"),
        ("ASSETS.serial_number", "assets", "ASSETS.serial_number"),
        ("ASSETS.serial_number", "WHATEVER", "ASSETS.serial_number"),
        ("ASSETS.serial_number", "", "ASSETS.serial_number"),
        ("serial_number", "", "serial_number"),
        ("assigned_to.first_name", "", "assigned_to.first_name"),
     ],
)
def test_get_prop_from_field(given_field, given_object_type, expected_result):
    given_prop = _get_prop_from_field(given_field, given_object_type)
    assert given_prop == expected_result


class TestIsNumeric:
    def test_is_numeric_w_int(self):
        assert _is_numeric(42)

    def test_is_numeric_w_float(self):
        assert _is_numeric(42.0)

    def test_is_numeric_w_none(self):
        assert not _is_numeric(None)

    def test_is_numeric_w_text(self):
        assert not _is_numeric("hello")

    def test_is_numeric_w_int_string(self):
        assert _is_numeric("42")


class TestConvertStringToTimestamp:
    def test_ok(self):
        assert _convert_string_to_timestamp("2018/01/01") == 1514764800

    def test_invalid_date_string_not_ok(self):
        with pytest.raises(ValueError):
            _convert_string_to_timestamp("unknown")


class TestCheckRule:
    def test_rule_equal(self):
        assert check_rule_by_op(Op.EQUAL, "a", "a")
        assert not check_rule_by_op(Op.EQUAL, "a", "b")

    def test_rule_not_equal(self):
        assert check_rule_by_op(Op.NOT_EQUAL, "a", "b")
        assert not check_rule_by_op(Op.NOT_EQUAL, "a", "a")

    def test_rule_begins_with(self):
        assert check_rule_by_op(Op.BEGINS_WITH, "aaa", "a")
        assert not check_rule_by_op(Op.BEGINS_WITH, "aaa", "b")

    def test_rule_does_not_begin_with(self):
        assert not check_rule_by_op(Op.DOES_NOT_BEGIN_WITH, "aaa", "a")
        assert check_rule_by_op(Op.DOES_NOT_BEGIN_WITH, "aaa", "b")

    def test_rule_ends_with(self):
        assert check_rule_by_op(Op.ENDS_WITH, "aaa", "a")
        assert not check_rule_by_op(Op.ENDS_WITH, "aaa", "b")

    def test_rule_does_not_end_with(self):
        assert not check_rule_by_op(Op.DOES_NOT_END_WITH, "aaa", "a")
        assert check_rule_by_op(Op.DOES_NOT_END_WITH, "aaa", "b")

    def test_rule_contains(self):
        assert check_rule_by_op(Op.CONTAINS, "aaa", "a")
        assert not check_rule_by_op(Op.CONTAINS, "aaa", "b")

    def test_rule_does_not_contain(self):
        assert not check_rule_by_op(Op.DOES_NOT_CONTAIN, "aaa", "a")
        assert check_rule_by_op(Op.DOES_NOT_CONTAIN, "aaa", "b")

    def test_rule_lt(self):
        assert check_rule_by_op(Op.LESS_THEN, "1", "2")
        assert not check_rule_by_op(Op.LESS_THEN, "2", "1")

    def test_rule_le(self):
        assert check_rule_by_op(Op.LESS_OR_EQUAL, "1", "2")
        assert check_rule_by_op(Op.LESS_OR_EQUAL, "2", "2")

    def test_rule_gt(self):
        assert check_rule_by_op(Op.GREATER_THEN, "2", "1")
        assert not check_rule_by_op(Op.GREATER_THEN, "1", "2")

    def test_rule_ge(self):
        assert check_rule_by_op(Op.GREATER_OR_EQUAL, "2", "2")
        assert check_rule_by_op(Op.GREATER_OR_EQUAL, "3", "2")

    def test_rule_lt_0_value(self):
        assert check_rule_by_op(Op.LESS_THEN, "0", "2")
        assert not check_rule_by_op(Op.LESS_THEN, "2", "0")

    def test_rule_le_0_value(self):
        assert check_rule_by_op(Op.LESS_OR_EQUAL, "0.1", "2")
        assert check_rule_by_op(Op.LESS_OR_EQUAL, "0", "0")
        assert not check_rule_by_op(Op.LESS_OR_EQUAL, "0.2", "0.1")

    def test_rule_gt_0_value(self):
        assert check_rule_by_op(Op.GREATER_THEN, "2", "0")
        assert not check_rule_by_op(Op.GREATER_THEN, "0", "0.001")

    def test_rule_ge_0_value(self):
        assert check_rule_by_op(Op.GREATER_OR_EQUAL, "0.0000001", "0")
        assert check_rule_by_op(Op.GREATER_OR_EQUAL, "0", "0")
        assert not check_rule_by_op(Op.GREATER_OR_EQUAL, "0", "0.2")

    @pytest.mark.parametrize(
        "operator,left_value,right_value",
        [
            (Op.LESS_THEN, "invalid", "2"),
            (Op.LESS_THEN, "2", "0.1.0"),
            (Op.LESS_OR_EQUAL, "invalid", "2"),
            (Op.LESS_OR_EQUAL, "0", "0000.1.0000"),
            (Op.LESS_OR_EQUAL, "0.1.0", "@!#$"),
            (Op.GREATER_THEN, "2", "invalid"),
            (Op.GREATER_THEN, "0", "0.001*)"),
            (Op.GREATER_OR_EQUAL, "invalid", "invalid"),
            (Op.GREATER_OR_EQUAL, "0.0001", "0.0001*"),
        ],
    )
    def test_invalid_numeric_value(self, operator, left_value, right_value):
        assert not check_rule_by_op(operator, left_value, right_value)

    def test_rule_is_null(self):
        assert check_rule_by_op(Op.IS_NULL, None, None)
        assert check_rule_by_op(Op.IS_NULL, "", None)

    def test_rule_not_null(self):
        assert check_rule_by_op(Op.NOT_NULL, "1", None)

    @pytest.fixture
    def now(self):
        return arrow.utcnow()

    @pytest.fixture
    def now_unix(self, now):
        return now.timestamp

    @pytest.fixture
    def day_before_unix(self, now):
        return now.shift(days=-1).timestamp

    @pytest.fixture
    def day_before_at_13_30_unix(self, now):
        return now.shift(days=-1).replace(hour=13, minute=30).timestamp

    @pytest.fixture
    def day_before_at_8_20_unix(self, now):
        return now.shift(days=-1).replace(hour=8, minute=20).timestamp

    @pytest.fixture
    def day_before_at_23_59_unix(self, now):
        return now.shift(days=-1).replace(hour=23, minute=59).timestamp

    @pytest.fixture
    def day_after_unix(self, now):
        return now.shift(days=1).timestamp

    @pytest.fixture
    def day_after_at_13_30_unix(self, now):
        return now.shift(days=1).replace(hour=13, minute=30).timestamp

    @pytest.fixture
    def day_after_at_8_20_unix(self, now):
        return now.shift(days=1).replace(hour=8, minute=20).timestamp

    @pytest.fixture
    def day_after_at_23_59_unix(self, now):
        return now.shift(days=1).replace(hour=23, minute=59).timestamp

    @pytest.mark.parametrize(
        "current_value,target_value,expected_result",
        [
            (lazy_fixture("day_before_unix"), "1", True),
            (lazy_fixture("day_before_at_8_20_unix"), "1", True),
            (lazy_fixture("day_before_at_13_30_unix"), "1", True),
            (lazy_fixture("day_before_at_23_59_unix"), "1", True),
            (lazy_fixture("day_before_unix"), "2", False),
            (None, "2", False),
        ],
    )
    def test_rule_days_after_ok(self, current_value, target_value, expected_result):
        given_result = check_rule_by_op(Op.DAYS_AFTER, current_value, target_value)
        assert bool(given_result) is expected_result

    @pytest.mark.parametrize(
        "current_value,target_value,expected_result",
        [
            (lazy_fixture("day_after_unix"), "1", True),
            (lazy_fixture("day_after_at_8_20_unix"), "1", True),
            (lazy_fixture("day_after_at_13_30_unix"), "1", True),
            (lazy_fixture("day_after_at_23_59_unix"), "1", True),
            (lazy_fixture("day_after_unix"), "2", False),
            (None, "1", False),
            (None, "2", False),
        ],
    )
    def test_rule_days_before_ok(self, current_value, target_value, expected_result):
        given_result = check_rule_by_op(Op.DAYS_BEFORE, current_value, target_value)
        assert bool(given_result) is expected_result

    def test_rule_days_equal_ok(self, now_unix):
        assert check_rule_by_op(Op.DAYS_EQUAL, f"{now_unix}", None)
        assert not check_rule_by_op(Op.DAYS_EQUAL, None, None)

    def test_rule_has_been_changed_ok(self):
        assert check_rule_by_op(Op.HAS_BEEN_CHANGED, "before", "after")
        assert not check_rule_by_op(Op.HAS_BEEN_CHANGED, "dontcare", "dontcare")
        assert check_rule_by_op(Op.HAS_BEEN_CHANGED, _missed, "after")
        assert not check_rule_by_op(Op.HAS_BEEN_CHANGED, "before", _missed)
        assert not check_rule_by_op(Op.HAS_BEEN_CHANGED, _missed, _missed)

    def test_rule_between_ok(self, now_unix, day_before_unix, day_after_unix):
        assert not check_rule_by_op(
            Op.BETWEEN, f"{now_unix}", {"from": day_after_unix, "to": None},
        )
        assert not check_rule_by_op(
            Op.BETWEEN, f"{now_unix}", {"from": None, "to": day_before_unix},
        )
        assert check_rule_by_op(
            Op.BETWEEN, f"{now_unix}", {"from": day_before_unix, "to": day_after_unix},
        )
        assert check_rule_by_op(
            Op.BETWEEN, f"{now_unix}", {"from": day_before_unix, "to": None},
        )
        assert check_rule_by_op(
            Op.BETWEEN, f"{now_unix}", {"from": None, "to": day_after_unix},
        )

    def test_rule_unknown_action_not_ok(self):
        assert not check_rule_by_op("unknown_action", None, None)


class TestCheckRules:
    @pytest.fixture
    def rules_w_data(self):
        return [
            {"op": "cn", "data": "CC1UH", "field": "ASSETS.serial_number",},
            {
                "op": "eq",
                "data": "2e84e8e99431411a84f2339bd02cacb0",
                "field": "ASSETS.assigned_to",
            },
            {
                "op": "eq",
                "data": "ad2c2ab54adb481c8436d6238838813a",
                "field": "ASSETS.equipment_id",
            },
        ]

    @pytest.fixture
    def group_w_andop(self, rules_w_data):
        some_rule, *rest = rules_w_data
        return {
            "rules": [],
            "groupOp": "and",
            "groups": [
                {"groupOp": "and", "rules": [some_rule,], "groups": [],},
                {"groupOp": "and", "rules": [*rest], "groups": [],},
            ],
        }

    @pytest.fixture
    def group_w_orop(self, rules_w_data):
        some_rule, *rest = rules_w_data
        return {
            "rules": [],
            "groupOp": "or",
            "groups": [
                {"groupOp": "and", "rules": [some_rule,], "groups": [],},
                {"groupOp": "and", "rules": [*rest], "groups": [],},
            ],
        }

    @pytest.fixture
    def document(self):
        return {
            "equipment_id": "ad2c2ab54adb481c8436d6238838813a",
            "assigned_to": "2e84e8e99431411a84f2339bd02cacb0",
            "serial_number": "C02CC1UHMD6T1",
            "model": "MacBookPro16,1",
        }

    @pytest.fixture
    def document_w_partial_match(self, document):
        return {
            "equipment_id": "9cd3ed7e80a0467f89bbc715ef4d8609",
            "assigned_to": "5ae18391b46344ca9d88dd857dc2f21f",
            "serial_number": "C02CC1UHMD6T2",
            "model": "MacBookPro16,1",
        }

    @pytest.mark.parametrize(
        "given_rules,given_document,expected_result",
        [
            (lazy_fixture("group_w_andop"), lazy_fixture("document"), True),
            (
                lazy_fixture("group_w_andop"),
                lazy_fixture("document_w_partial_match"),
                False,
            ),
            (lazy_fixture("group_w_andop"), {}, False),
            (lazy_fixture("group_w_orop"), lazy_fixture("document"), True),
            (
                lazy_fixture("group_w_orop"),
                lazy_fixture("document_w_partial_match"),
                True,
            ),
            (lazy_fixture("group_w_orop"), {}, False),
        ],
    )
    def test_ok(self, given_rules, given_document, expected_result):
        given_result = check_rules(
            given_rules,
            document=given_document,
            changed_values=None,
            object_type="ASSETS",
        )
        assert given_result is expected_result
