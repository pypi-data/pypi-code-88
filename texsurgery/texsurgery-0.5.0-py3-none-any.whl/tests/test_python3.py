#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import logging

from texsurgery.texsurgery import TexSurgery


class TestPython3Surgery(unittest.TestCase):
    """ Tests TexSurgery.code_surgery for the python3 kernel"""

    def test_simple_addition(self):
        """ Tests a simple addition"""
        tex_source = r'\usepackage[python3]{texsurgery}2+2=\eval{2+2} '
        tex_out = r'2+2=4 '
        ts = TexSurgery(tex_source).code_surgery()
        self.assertEqual(ts.src, tex_out)
        del ts  # shutdown kernel

    def test_division(self):
        """ Tests a simple addition"""
        tex_source = r'\usepackage[python3]{texsurgery}1/2=\eval{1/2}'
        tex_out = r'1/2=0.5'
        ts = TexSurgery(tex_source).code_surgery()
        self.assertEqual(ts.src, tex_out)
        del ts  # shutdown kernel

    def test_nested_brackets(self):
        """ Tests an expression eval{ with {nested} brackets }"""
        tex_source = r"\usepackage[python3]{texsurgery}The first prime number is" \
                     r" \eval{sorted({7,3,5,2})[0]}"
        tex_out = r'The first prime number is 2'
        ts = TexSurgery(tex_source).code_surgery()
        self.assertEqual(ts.src, tex_out)
        del ts  # shutdown kernel

    def test_return_str(self):
        r"""\evalstr{'python string'} should not return the quotes"""
        tex_source = r"\usepackage[python3]{texsurgery}My favourite colour is \evalstr{'blue'} "
        tex_out = r'My favourite colour is blue '
        ts = TexSurgery(tex_source).code_surgery()
        self.assertEqual(ts.src, tex_out)
        del ts  # shutdown kernel

    def test_sif(self):
        r""" Tests \sif{}{}{}"""
        tex_source = r'\usepackage[python3]{texsurgery}'\
                     r'\begin{runsilent}a=3\end{runsilent}'\
                     r'\eval{a} is an \sif{a%2}{odd}{even} number'
        tex_out = r'3 is an odd number'
        ts = TexSurgery(tex_source).code_surgery()
        self.assertEqual(ts.src, tex_out)
        del ts  # shutdown kernel

        tex_source = r'\usepackage[python3]{texsurgery}'\
                     r'\begin{runsilent}a=4\end{runsilent}'\
                     r'\eval{a} is an \sif{a%2}{odd}{even} number'
        tex_out = r'4 is an even number'
        ts = TexSurgery(tex_source).code_surgery()
        self.assertEqual(ts.src, tex_out)
        del ts  # shutdown kernel

    def test_nested_sif(self):
        r""" Tests \sif{}{\eval{code}}{}"""
        tex_source = r'''\usepackage[python3]{texsurgery}\begin{runsilent}
a=3
def shift_letter(s):
    return ''.join(chr(ord(c)+ord('A')-ord('a')) for c in s)
\end{runsilent}
\eval{a} is an \sif{a%2}{\evalstr{shift_letter('odd')}}{\evalstr{shift_letter('even')}} number'''
        tex_out = '\n3 is an ODD number'
        ts = TexSurgery(tex_source).code_surgery()
        self.assertEqual(ts.src, tex_out)
        del ts  # shutdown kernel

        tex_source = r'''\usepackage[python3]{texsurgery}\begin{runsilent}
a=4
def shift_letter(s):
    return ''.join(chr(ord(c)+ord('A')-ord('a')) for c in s)
\end{runsilent}
\eval{a} is an \sif{a%2}{\evalstr{shift_letter('odd')}}{\evalstr{shift_letter('even')}} number'''
        tex_out = '\n4 is an EVEN number'
        ts = TexSurgery(tex_source).code_surgery()
        self.assertEqual(ts.src, tex_out)
        del ts  # shutdown kernel

    def test_sinput(self):
        r"""\sinput{file.py} should read that file and run it immediately"""
        tex_source = r"\usepackage[python3]{texsurgery}"\
                     r'\begin{runsilent}a=4\end{runsilent}'\
                     r'\sinput{tests/add_1_to_a.py}'\
                     r'a=\eval{a}'
        tex_out = r'a=5'
        ts = TexSurgery(tex_source).code_surgery()
        self.assertEqual(ts.src, tex_out)
        del ts  # shutdown kernel

    def test_comment(self):
        """simple comments remain"""
        tex_source = '\\usepackage[python3]{texsurgery}'\
        '\\begin{runsilent}a=4# some comment'\
        '\na+=1\\end{runsilent}'\
        'a=\\eval{a}%whatever\n'
        tex_out = 'a=5%whatever\n'
        ts = TexSurgery(tex_source).code_surgery()
        self.assertEqual(ts.src, tex_out)
        del ts  # shutdown kernel

    def test_comment_2(self):
        """Do not run code in \\eval{code} inside a LaTeX comment"""
        tex_source = '\\usepackage[python3]{texsurgery}'\
        '\\begin{runsilent}a=4# some comment'\
        '\na+=1\\end{runsilent}'\
        'a=\\eval{a}%\\eval{would be an error}\n'
        tex_out = 'a=5%\\eval{would be an error}\n'
        ts = TexSurgery(tex_source).code_surgery()
        self.assertEqual(ts.src, tex_out)
        del ts  # shutdown kernel

    def test_comment_3(self):
        """Allow % sign within \eval{...%...}: this is not a LaTeX comment"""
        tex_source = '\\usepackage[python3]{texsurgery}'\
        '\\begin{runsilent}a=4# some comment'\
        '\na+=1\\end{runsilent}'\
        'a=\\evalstr{"%.3f"%(1/3)}%\\eval{would be an error}\n'
        tex_out = 'a=0.333%\\eval{would be an error}\n'
        ts = TexSurgery(tex_source).code_surgery()
        self.assertEqual(ts.src, tex_out)
        del ts  # shutdown kernel

    def test_comment_4(self):
        """Allow % sign within \eval{...%...}: this is not a LaTeX comment"""
        tex_source = '\\usepackage[python3]{texsurgery}'\
        '\\begin{runsilent}a=4# some comment'\
        '\na+=1\\end{runsilent}'\
        'a=\\evalstr{"%.3f"%(1/3)}%\\eval{would be an% error}\n'
        tex_out = 'a=0.333%\\eval{would be an% error}\n'
        ts = TexSurgery(tex_source).code_surgery()
        self.assertEqual(ts.src, tex_out)
        del ts  # shutdown kernel
