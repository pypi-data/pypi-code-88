#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys


class TestCommandLine(unittest.TestCase):
    """ Tests command_line.py -> the texsurgery shell command"""

    def test_simple_code_surgery(self):
        """ Tests a simple code surgery example"""
        tex_out = '2+2=4\n'
        sys.argv = ['texsurgery',
                    '-o',
                    'tests/test_command_line_out_tmpfile.tex',
                    'tests/test_command_line.tex']
        # import after modifying sys.argv
        from texsurgery.command_line import main
        main()
        with open('tests/test_command_line_out_tmpfile.tex', 'r') as f:
            tex_in_outfile = f.read()
        self.assertEqual(tex_in_outfile, tex_out)

    def test_find(self):
        """ Tests a texsurgery -find example"""
        tex_out = r"\AMCnumericChoices{\eval{8+a}}{digits=2,sign=false,scoreexact=3}"
        outfile = 'tests/test_command_line_find_out_tmpfile.tex'
        sys.argv = ['texsurgery',
                    '-find', r'questionmultx \AMCnumericChoices{solution}{options}',
                    '-o', outfile,
                    'tests/test_find.tex']
        # import after modifying sys.argv
        from texsurgery.command_line import main
        main()
        with open(outfile, 'r') as f:
            tex_in_outfile = f.read()
        self.assertEqual(tex_in_outfile, tex_out)

    def test_replace(self):
        """ Tests a texsurgery -replace example"""
        outfile = 'tests/test_command_line_replace_out_tmpfile.tex'
        expected_file = 'tests/test_command_line_replace_out.tex'
        sys.argv = ['texsurgery',
                    '-replace',
                    r'\correctchoice{choice}',
                    r'\correctchoice{$\sage{f.derivative(x)}$}',
                    '-o', outfile,
                    'tests/test_find.tex']
        # import after modifying sys.argv
        from texsurgery.command_line import main
        main()
        with open(outfile, 'r') as f:
            tex_in_outfile = f.read()
        with open(expected_file, 'r') as f:
            tex_expected = f.read()
        self.assertEqual(tex_in_outfile, tex_expected)

    def test_shuffle(self):
        """ Tests a texsurgery -shuffle example"""
        outfile = 'tests/test_command_line_shuffle_out_tmpfile.tex'
        expected_file = 'tests/test_shuffle_out_2.tex'
        sys.argv = ['texsurgery',
                    '-shuffle',
                    'question[questionid=basic-multiplication]{questionid} choices',
                    r'\correctchoice{choice},\wrongchoice{choice}',
                    '-randomseed',
                    '1',
                    '-o', outfile,
                    'tests/test_shuffle.tex']
        # import after modifying sys.argv
        from texsurgery.command_line import main
        main()
        with open(outfile, 'r') as f:
            tex_in_outfile = f.read()
        with open(expected_file, 'r') as f:
            tex_expected = f.read()
        self.assertEqual(tex_in_outfile, tex_expected)
