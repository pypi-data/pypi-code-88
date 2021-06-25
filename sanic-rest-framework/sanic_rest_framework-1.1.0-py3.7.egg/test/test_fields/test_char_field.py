"""
@Author：WangYuXiang
@E-mile：Hill@3io.cc
@CreateTime：2021/1/28 16:16
@DependencyLibrary：无
@MainFunction：无
@FileDoc： 
    test_char_field.py
    字符字段单元测试
@ChangeHistory:
    datetime action why
    example:
    2021/1/28 16:16 change 'Fix bug'
        
"""
import asyncio
import unittest

from tortoise.contrib.test import initializer

from sanic_rest_framework.exceptions import ValidationError
from sanic_rest_framework.fields import CharField
from sanic_rest_framework.test.test_fields.test_base_field import TestBaseField

initializer(['sanic_rest_framework.test.models', ],
            # db_url="sqlite://./db.sqlite",
            loop=asyncio.get_event_loop())


class TestCharField(TestBaseField):
    def test_external_to_internal(self):
        data = ' Python'
        char1 = CharField()
        self.assertEqual(char1.external_to_internal(data), 'Python')

    async def test_internal_to_external(self):
        data1 = {'char1': 'Python'}
        data2 = {'char1': 66666}
        char1 = CharField()
        char1.bind('char1', char1)

        value = await char1.get_internal_value(data1)
        self.assertEqual(await char1.internal_to_external(value), 'Python')

        value = await char1.get_internal_value(data2)
        self.assertEqual(await char1.internal_to_external(value), '66666')

    def test_trim_whitespace(self):
        data = ' Python'
        char1 = CharField()
        char2 = CharField(trim_whitespace=True)
        char3 = CharField(trim_whitespace=False)
        c1_data = char1.external_to_internal(data)
        c2_data = char2.external_to_internal(data)
        c3_data = char3.external_to_internal(data)
        self.assertEqual(c1_data, 'Python')
        self.assertEqual(c2_data, 'Python')
        self.assertEqual(c3_data, ' Python')

    def test_max_length(self):
        data = 'Python'
        char1 = CharField()
        char2 = CharField(max_length=10)
        char3 = CharField(max_length=5)
        self.assertEqual(char1.run_validation(data), 'Python')
        self.assertEqual(char2.run_validation(data), 'Python')

        with self.assertRaises(ValidationError):
            char3.run_validation(data)

    def test_min_length(self):
        data = 'Python'
        char1 = CharField()
        char2 = CharField(min_length=5)
        char3 = CharField(min_length=10)
        self.assertEqual(char1.run_validation(data), 'Python')
        self.assertEqual(char2.run_validation(data), 'Python')

        with self.assertRaises(ValidationError):
            char3.run_validation(data)


if __name__ == '__main__':
    unittest.main()
