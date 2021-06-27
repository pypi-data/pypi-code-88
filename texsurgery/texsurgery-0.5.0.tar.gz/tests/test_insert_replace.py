#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
# import logging

from texsurgery.texsurgery import TexSurgery


class TestInsert(unittest.TestCase):
    """ Tests TexSurgery.insertAfter"""

    def __init__(self, methodName='runTest'):
        super(TestInsert, self).__init__(methodName=methodName)
        with open('tests/test_find.tex', 'r') as f:
            self.sample_tex = f.read()

    def test_add_choice(self):
        """finds a nested selector and inserts a new wrongchoice after it
        """
        tex_source = self.sample_tex
        expected_res = [
            ('choices', [
                (r'\wrongchoice', {'choice': r'$\sage{fd/a}$'}),
                (r'\wrongchoice', {'choice': r'$\sage{fd*a}$'}),
                (r'\wrongchoice', {'choice': r'$\sage{fd + a}$'})
                ]),
        ]
        ts = TexSurgery(tex_source)
        ts.insertAfter(r'choices \correctchoice{choice}', r'\wrongchoice{$\sage{fd/a}$}')
        res = ts.findall(r'choices \wrongchoice{choice}')
        self.assertEqual(repr(res), repr(expected_res))

        # part II, a different insertion point
        expected_res = [
            ('choices', [
                (r'\wrongchoice', {'choice': r'$\sage{fd*a}$'}),
                (r'\wrongchoice', {'choice': r'$\sage{fd/a}$'}),
                (r'\wrongchoice', {'choice': r'$\sage{fd + a}$'})
                ]),
        ]
        ts = TexSurgery(tex_source)
        ts.insertAfter(r'choices \wrongchoice{choice}', r'\wrongchoice{$\sage{fd/a}$}')
        res = ts.findall(r'choices \wrongchoice{choice}')
        self.assertEqual(repr(res), repr(expected_res))

    def test_add_choice_with_comma(self):
        """Similar to test_add_choice, but the selector is more complex
        """
        tex_source = self.sample_tex
        expected_res = [
            ('choices', [
                (r'\wrongchoice', {'choice': r'$\sage{fd*a}$'}),
                (r'\wrongchoice', {'choice': r'$\sage{fd/a}$'}),
                (r'\wrongchoice', {'choice': r'$\sage{fd + a}$'})
                ]),
        ]
        ts = TexSurgery(tex_source)
        ts.insertAfter(r'choices,itemize \wrongchoice{choice}', r'\wrongchoice{$\sage{fd/a}$}')
        res = ts.findall(r'choices \wrongchoice{choice}')
        self.assertEqual(repr(res), repr(expected_res))

    def test_replace_choice(self):
        r"""finds a nested selector for \correctchoice and replaces it with other text
        """
        tex_source = self.sample_tex
        expected_res = [
            ('choices', [
                (r'\correctchoice', {'choice': r'$\sage{f.derivative(x)}$'}),
                ]),
        ]
        ts = TexSurgery(tex_source)
        ts.replace(r'choices \correctchoice{choice}', r'\correctchoice{$\sage{f.derivative(x)}$}')
        res = ts.findall(r'choices \correctchoice{choice}')
        self.assertEqual(repr(res), repr(expected_res))

        # part II, a different insertion point
        expected_res = [
            ('choices', [
                (r'\wrongchoice', {'choice': r'$\sage{fd*a}$'}),
                (r'\wrongchoice', {'choice': r'$\sage{fd/a}$'}),
                (r'\wrongchoice', {'choice': r'$\sage{fd + a}$'})
                ]),
        ]
        ts = TexSurgery(tex_source)
        ts.insertAfter(r'choices \wrongchoice{choice}', r'\wrongchoice{$\sage{fd/a}$}')
        res = ts.findall(r'choices \wrongchoice{choice}')
        self.assertEqual(repr(res), repr(expected_res))
