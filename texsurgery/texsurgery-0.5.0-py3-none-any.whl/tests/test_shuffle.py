#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
# import logging

from texsurgery.texsurgery import TexSurgery


class TestShuffle(unittest.TestCase):
    """ Tests TexSurgery.insertAfter"""

    def __init__(self, methodName='runTest'):
        super(TestShuffle, self).__init__(methodName=methodName)
        with open('tests/test_shuffle.tex', 'r') as f:
            self.sample_tex = f.read()

    def test_shuffle_basic_README(self):
        '''test basic example from README.md
        '''
        tex = r'''\begin{choices}
  \wrongchoice{$\sage{fd + a}$}
  \correctchoice{$\sage{fd}$}
  \wrongchoice{$\sage{fd*a}$}
\end{choices}
'''
        expectedtex = r'''\begin{choices}
  \correctchoice{$\sage{fd}$}
  \wrongchoice{$\sage{fd*a}$}
  \wrongchoice{$\sage{fd + a}$}
\end{choices}
'''
        ts = TexSurgery(tex)
        ts.shuffle('choices', r'\correctchoice{choice},\wrongchoice{choice}', randomseed=2)
        self.assertEqual(ts.src, expectedtex)

    def test_shuffle_one_choices(self):
        """shuffles wrongchoice and correctchoice inside only one choices environment
        """
        tex_source = self.sample_tex

        ts = TexSurgery(tex_source)
        ts.shuffle(
            'question[questionid=basic-multiplication]{questionid} choices',
            r'\correctchoice{choice},\wrongchoice{choice}',
            randomseed=1)

        # #uncomment to "reset" the test
        # with open('tests/test_shuffle_out_2.tex', 'w') as f:
        #     tex_out = f.write(ts.src)
        #     print(tex_out)
        with open('tests/test_shuffle_out_2.tex', 'r') as f:
            tex_out = f.read()
        self.maxDiff = None
        self.assertEqual(ts.src, tex_out)

    def test_shuffle_all_choices(self):
        """shuffles wrongchoice and correctchoice inside all choices environments
        """
        tex_source = self.sample_tex

        ts = TexSurgery(tex_source)
        ts.shuffle('choices', r'\correctchoice{choice},\wrongchoice{choice}', randomseed=1)

        # #uncomment to "reset" the test
        # with open('tests/test_shuffle_out_1.tex','w') as f:
        #     tex_out = f.write(ts.src)
        #     print(tex_out)
        with open('tests/test_shuffle_out_3.tex', 'r') as f:
            tex_out = f.read()
        self.maxDiff = None
        self.assertEqual(ts.src, tex_out)
