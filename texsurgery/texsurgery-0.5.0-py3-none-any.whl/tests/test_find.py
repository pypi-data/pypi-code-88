#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
# import logging

from texsurgery.texsurgery import TexSurgery


class TestFind(unittest.TestCase):
    """ Tests TexSurgery.find and  TexSurgery.findall"""

    def __init__(self, methodName='runTest'):
        super(TestFind, self).__init__(methodName=methodName)
        with open('tests/test_find.tex', 'r') as f:
            self.sample_tex = f.read()

    def test_find_one_environment(self):
        """use find for a non nested environment
        """
        tex_source = self.sample_tex
        expected_res = ('run', "\nprint('The random seed is ', seed)\n")
        res = TexSurgery(tex_source).find('run')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_unexisting(self):
        """use find for an environment that is not in the document
        """
        tex_source = self.sample_tex
        expected_res = None
        res = TexSurgery(tex_source).find('runmeplease')
        self.assertEqual(repr(res), repr(expected_res))

    def test_findall_one_environment(self):
        """finds all apperances of one non nested environment
        that appears only once.
        """
        tex_source = self.sample_tex
        expected_res = [('run', "\nprint('The random seed is ', seed)\n")]
        res = TexSurgery(tex_source).findall('run')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_all(self):
        """finds all apperances of a non nested environment
        that appears a few times.
        """
        tex_source = self.sample_tex
        expected_res = [
            ('runsilent', """\nseed = 1\nset_random_seed(seed)\n"""),
            ('runsilent', """\na = randint(1,10)\n"""),
            ('runsilent', """\na = randint(2,10)\n"""),
            ('runsilent', """\na = randint(2,10)\nf = sin(a*x)\nfd = f.derivative(x)\n"""),
        ]
        res = TexSurgery(tex_source).findall('runsilent')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_nested(self):
        """finds all apperances of a command nested inside
        an environment that appears once.
        """
        tex_source = self.sample_tex
        expected_res = [
            ('choices', [r'\correctchoice']),
        ]
        res = TexSurgery(tex_source).findall(r'choices \correctchoice')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_nested_with_code(self):
        """finds all apperances of a command nested inside
        an environment that appears once.
        """
        tex_source = self.sample_tex
        expected_res = [
            ('choices', [(r'\correctchoice',  {'code': '$\\sage{fd}$'})]),
        ]
        res = TexSurgery(tex_source).findall(r'choices \correctchoice{code}')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_nested_2(self):
        """finds all apperances of a command nested inside
        an environment which is nested inside
        another environment that appears once.
        """
        tex_source = self.sample_tex
        expected_res = [
            ('question', [('choices', [r'\correctchoice'])])
        ]
        res = TexSurgery(tex_source).findall(r'question choices \correctchoice')
        self.assertEqual(repr(res), repr(expected_res))

        expected_res = [
          ('question',
           [('choices', [r'\wrongchoice', r'\wrongchoice'])])
        ]
        res = TexSurgery(tex_source).findall(r'question choices \wrongchoice')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_nested_2_with_code(self):
        """finds all apperances of a command nested inside
        an environment which is nested inside
        another environment that appears once.
        """
        tex_source = self.sample_tex
        expected_res = [
            ('question', [
               ('choices', [(r'\correctchoice', {'code': '$\\sage{fd}$'})])
               ]),
        ]
        res = TexSurgery(tex_source).findall(r'question choices \correctchoice{code}')
        self.assertEqual(repr(res), repr(expected_res))

        expected_res = [
          ('question',
           [('choices', [
             (r'\wrongchoice', {'code': '$\\sage{fd*a}$'}),
             (r'\wrongchoice', {'code': '$\\sage{fd + a}$'})])])
        ]
        res = TexSurgery(tex_source).findall(r'question choices \wrongchoice{code}')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_nested_commands(self):
        """use find for a command nested inside an command
        """
        tex_source = self.sample_tex
        expected_res = (r'\AMCnumericChoices', r'\eval')
        res = TexSurgery(tex_source).find(r'\AMCnumericChoices \eval')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_nested_commands_with_code(self):
        """use find for a command nested inside an command
        """
        tex_source = self.sample_tex
        expected_res = (r'\AMCnumericChoices', (r'\eval', {'code': '8+a'}))
        res = TexSurgery(tex_source).find(r'\AMCnumericChoices \eval{code}')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_comma_nested(self):
        """use find for a command nested inside an environment
        """
        tex_source = self.sample_tex
        expected_res = ('choices', r'\correctchoice')
        res = TexSurgery(tex_source).find(r'run,choices \correctchoice')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_comma_nested_2(self):
        """finds all apperances of a command nested inside an environment
        nested inside another environment which can be of two different types.
        """
        tex_source = self.sample_tex
        expected_res = [
            ('question', [
               ('choices', [r'\correctchoice'])
               ]),
        ]
        res = TexSurgery(tex_source).findall(r'question,questionmultx choices \correctchoice')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_nested_comma_nested_mult(self):
        """finds all apperances of a command nested inside an environment
        which is nested inside another environment which can be of two different types.
        It matches the tex twice.
        """
        tex_source = self.sample_tex
        expected_res = [
            ('questionmultx', [('runsilent', '\na = randint(1,10)\n')]),
            ('questionmultx', [('runsilent', '\na = randint(2,10)\n')]),
            ('question',
             [('runsilent', '\na = randint(2,10)\nf = sin(a*x)\nfd = f.derivative(x)\n')])
        ]
        res = TexSurgery(tex_source).findall('question,questionmultx runsilent')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_comma_alternatives(self):
        """tests a selector consisting of two selectors separated by a comma.
        """
        tex_source = self.sample_tex
        expected_res = ('question', 'choices', r'\correctchoice')
        res = TexSurgery(tex_source).find(
            r'question choices \correctchoice, questionmultx \AMCnumericChoices')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_comma_alternatives_with_code(self):
        """tests a selector consisting of two selectors separated by a comma.
        """
        tex_source = self.sample_tex
        expected_res = (
            'question', 'choices', (r'\correctchoice', {'content': r'$\sage{fd}$'})
        )
        res = TexSurgery(tex_source).find(
            r'question choices \correctchoice{content}, '
            r'questionmultx \AMCnumericChoices{content}'
        )
        self.assertEqual(repr(res), repr(expected_res))

    def test_findall_comma_alternatives(self):
        """tests a selector consisting of two selectors separated by a comma.
        """
        tex_source = self.sample_tex
        expected_res = [
            ('question', [('choices', [r'\correctchoice'])]),
            ('questionmultx', [r'\AMCnumericChoices']),
            ('questionmultx', [r'\AMCnumericChoices'])
        ]
        res = TexSurgery(tex_source).findall(
            r'question choices \correctchoice, questionmultx \AMCnumericChoices')
        self.assertEqual(repr(res), repr(expected_res))

    def test_findall_comma_alternatives_with_code(self):
        """tests a selector consisting of two selectors separated by a comma.
        """
        tex_source = self.sample_tex
        expected_res = [
            ('question', [('choices', [(r'\correctchoice', {'content': r'$\sage{fd}$'})])]),
            ('questionmultx', [(r'\AMCnumericChoices', {'content': r'\eval{8+a}'})]),
            ('questionmultx', [(r'\AMCnumericChoices', {'content': r'\eval{8*a}'})])
        ]
        res = TexSurgery(tex_source).findall(
            r'question choices \correctchoice{content},'
            + r' questionmultx \AMCnumericChoices{content}'
        )
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_command_with_two_arguments(self):
        """tests a selector consisting of a command with two mandatory arguments in braces {}.
        """
        tex_source = self.sample_tex
        expected_res = [
            ('questionmultx',
             [('\\AMCnumericChoices',
               {'arg0': '\\eval{8+a}',
                'arg1': 'digits=2,sign=false,scoreexact=3'})]),
            ('questionmultx',
             [('\\AMCnumericChoices',
               {'arg0': '\\eval{8*a}',
                'arg1': 'digits=2,sign=false,scoreexact=3'})])
        ]
        res = TexSurgery(tex_source).findall(r'questionmultx \AMCnumericChoices[_nargs=2]')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_command_with_a_named_argument(self):
        """tests a selector consisting of a command with a named argument in braces {}.
        """
        tex_source = self.sample_tex
        expected_res = [
            ('questionmultx',
             [('\\AMCnumericChoices',
               {'solution': '\\eval{8+a}',
                'options': 'digits=2,sign=false,scoreexact=3'})]),
            ('questionmultx',
             [('\\AMCnumericChoices',
               {'solution': '\\eval{8*a}',
                'options': 'digits=2,sign=false,scoreexact=3'})])
        ]
        res = TexSurgery(tex_source).findall(
            r'questionmultx \AMCnumericChoices{solution}{options}'
        )
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_command_with_a_named_argument_and_nargs(self):
        """tests a selector consisting of a command with a named argument in braces {}.
        """
        tex_source = self.sample_tex
        expected_res = [
            ('questionmultx',
             [('\\AMCnumericChoices',
               {'solution': '\\eval{8+a}',
                'arg0': 'digits=2,sign=false,scoreexact=3'})]),
            ('questionmultx',
             [('\\AMCnumericChoices',
               {'solution': '\\eval{8*a}',
                'arg0': 'digits=2,sign=false,scoreexact=3'})])
        ]
        res = TexSurgery(tex_source).findall(
            r'questionmultx \AMCnumericChoices[_nargs=1]{solution}'
        )
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_mixed(self):
        """tests a mixed selector combining commas at two different levels
        """
        tex_source = self.sample_tex
        expected_res = ('questionmultx', '\\AMCnumericChoices')
        res = TexSurgery(tex_source).find(
            r'questionmultx,question \correctchoice,\AMCnumericChoices')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_mixed_with_code(self):
        """tests a mixed selector combining commas at two different levels
        """
        tex_source = self.sample_tex
        expected_res = ('questionmultx', ('\\AMCnumericChoices', {'code': '\\eval{8+a}'}))
        res = TexSurgery(tex_source).find(
            r'questionmultx,question \correctchoice{code},\AMCnumericChoices{code}')
        self.assertEqual(repr(res), repr(expected_res))

    def test_findall_mixed(self):
        """tests a mixed selector combining commas at two different levels
        """
        tex_source = self.sample_tex
        expected_res = [
            ('questionmultx', ['\\AMCnumericChoices']),
            ('questionmultx', ['\\AMCnumericChoices']),
            ('question', ['\\correctchoice'])
        ]
        res = TexSurgery(tex_source).findall(
            r'questionmultx,question \correctchoice,\AMCnumericChoices')
        self.assertEqual(repr(res), repr(expected_res))

    def test_findall_mixed_with_code(self):
        """tests a mixed selector combining commas at two different levels
        """
        tex_source = self.sample_tex
        expected_res = [
            ('questionmultx', [('\\AMCnumericChoices', {'code': '\\eval{8+a}'})]),
            ('questionmultx', [('\\AMCnumericChoices', {'code': '\\eval{8*a}'})]),
            ('question', [('\\correctchoice', {'code': '$\\sage{fd}$'})])
        ]
        res = TexSurgery(tex_source).findall(
            r'questionmultx,question \correctchoice{code},\AMCnumericChoices{code}')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_environment_with_argument(self):
        """finds all appearances of one environment with a named argument.
        """
        tex_source = self.sample_tex
        expected_res = [('question',
                         {'questionid': 'derivativesin'},
                        r'''\scoring{e=-0.5,b=1,m=-.25,p=-0.5}
\begin{runsilent}
a = randint(2,10)
f = sin(a*x)
fd = f.derivative(x)
\end{runsilent}
  What is the first derivative of $\sage{f}$?
  \begin{choices}
    \correctchoice{$\sage{fd}$}
    \wrongchoice{$\sage{fd*a}$}
    \wrongchoice{$\sage{fd + a}$}
  \end{choices}
''')]
        res = TexSurgery(tex_source).findall('question{questionid}')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_exact_argument(self):
        """finds an environment with an exact text for a specific argument
        """
        tex_source = self.sample_tex
        expected_res = (
            'questionmultx',
            {'questionid': 'basic-multiplication'},
            r'''
\begin{runsilent}
a = randint(2,10)
\end{runsilent}
What is $8*\eval{a}$?
\AMCnumericChoices{\eval{8*a}}{digits=2,sign=false,scoreexact=3}
'''
        )
        res = TexSurgery(tex_source).find(
            r'questionmultx[questionid=basic-multiplication]{questionid}')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_exact_argument_short(self):
        """questionmultx{@basic-multiplication}

        finds an environment with an exact text for a specific argument using
        the short @arg syntax
        """
        tex_source = self.sample_tex
        expected_res = (
            'questionmultx',
            {'@basic-multiplication': 'basic-multiplication'},
            r'''
\begin{runsilent}
a = randint(2,10)
\end{runsilent}
What is $8*\eval{a}$?
\AMCnumericChoices{\eval{8*a}}{digits=2,sign=false,scoreexact=3}
'''
        )
        res = TexSurgery(tex_source).find(
            r'questionmultx{@basic-multiplication}')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_command_exact_argument_short(self):
        r"""\label{@seed}

        finds a command with an exact text for a specific argument using
        the short @arg syntax
        """
        tex_source = self.sample_tex
        expected_res = (r'\label', {'@seed': 'seed'})
        res = TexSurgery(tex_source).find(r'\label{@seed}')
        self.assertEqual(repr(res), repr(expected_res))

    def test_findall_command_exact_argument_and_other_argument_short(self):
        r"""\copygroup{@cat1}{group}

        finds a command with an exact text for a specific argument using
        the short @arg syntax, and captures also the next argument
        """
        tex_source = self.sample_tex
        expected_res = [(r'\copygroup', {'@cat1': 'cat1', 'group': 'BigGroupe'})]
        res = TexSurgery(tex_source).findall(r'\copygroup{@cat1}{group}')
        self.assertEqual(repr(res), repr(expected_res))

    def test_findall_command_exact_argument_and_other_argument_short_2(self):
        r"""\copygroup{category}{@BigGroupe}

        finds a command with an exact text for a specific argument using
        the short @arg syntax, and captures also the next argument
        """
        tex_source = self.sample_tex
        expected_res = [
            (r'\copygroup', {'category': 'cat1', '@BigGroupe': 'BigGroupe'}),
            (r'\copygroup', {'category': 'cat2', '@BigGroupe': 'BigGroupe'})
        ]
        res = TexSurgery(tex_source).findall(r'\copygroup{category}{@BigGroupe}')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_command_with_square_and_curly_brackets(self):
        """finds a command with both mandatory and optional arguments
        """
        tex_source = self.sample_tex
        expected_res = (
            '\\documentclass',
            {'dtype': 'article'}
        )
        res = TexSurgery(tex_source).find(r'\documentclass{dtype}')
        self.assertEqual(repr(res), repr(expected_res))

    # 21-06-16: issue #4
    def test_find_one_section_with_label(self):
        r"""use find for a non nested \section with a label
        """
        tex_source = self.sample_tex
        expected_res = ('\\section', {'sectiontext': 'Intro'})
        res = TexSurgery(tex_source).find('\\section{sectiontext}#intro')
        self.assertEqual(repr(res), repr(expected_res))

        expected_res = ('\\section', {'sectiontext': 'Exercises'})
        res = TexSurgery(tex_source).find('\\section{sectiontext}#exercises')
        self.assertEqual(repr(res), repr(expected_res))

        expected_res = None
        res = TexSurgery(tex_source).find('\\section#notpresent')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_one_section_with_label_and_pseudo_next(self):
        r"""use find for a non nested \section{sectionname}#intro:next
        """
        tex_source = self.sample_tex
        expected_res = (
            ('\\section', {'sectiontext': 'Intro'}),
            '\\subsection{Exam id...answers are ticked')
        res = TexSurgery(tex_source).find(r'\section{sectiontext}#intro:next')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_one_section_with_label_and_pseudo_next_2(self):
        r"""use find for a non nested \section{sectionname}#intro:next
        """
        tex_source = self.sample_tex
        expected_res = None
        res = TexSurgery(tex_source).find(r'\section#notpresent:next')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_one_section_with_label_and_pseudo_next_3(self):
        r"""use find for a non nested \section{sectionname}#intro:next
        """
        tex_source = self.sample_tex
        expected_res = (
            ('\\section', {'sectiontext': 'Exercises'}),
            r'\subsection{Exercis...upe{BigGroupe}}')
        res = TexSurgery(tex_source).find('\\section{sectiontext}#exercises:next')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_one_subsection_with_label_and_pseudo_next(self):
        r"""use find for a non nested \subsection{sectionname}#intro:next

        should stop at the next \section or \subsection or \end{document}
        """
        tex_source = self.sample_tex
        expected_res = (
            ('\\subsection', {'title': 'Exam identification'}),
            '\\begin{examdata} ...ate\\end{examdata}')
        res = TexSurgery(tex_source).find('\\subsection{title}#examdata:next')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_one_subsection_with_label_and_pseudo_next_2(self):
        r"""use find for a non nested \subsection{sectionname}#intro:next

        should stop at the next \section or \subsection or \end{document}
        """
        tex_source = self.sample_tex
        expected_res = None
        res = TexSurgery(tex_source).find('\\subsection#notpresent:next')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_one_subsection_with_label_and_pseudo_next_3(self):
        r"""use find for a non nested \subsection{sectionname}#intro:next

        should stop at the next \section or \subsection or \end{document}
        """
        tex_source = self.sample_tex
        expected_res = (
            ('\\subsection', {'title': 'Seed'}),
            '\\begin{runsilent}...answers are ticked')
        res = TexSurgery(tex_source).find('\\subsection{title}#seed:next')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_one_subsection_with_label_and_pseudo_next_4(self):
        r"""use find for a non nested \subsection{sectionname}#intro:next

        should stop at the next \section or \subsection or \end{document}
        """
        tex_source = self.sample_tex
        expected_res = (
            ('\\subsection', {'title': 'Exercise 3'}),
            '\\element{cat2}{\\be...upe{BigGroupe}}')
        res = TexSurgery(tex_source).find('\\subsection{title}#ex3:next')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_one_subsection_with_label_and_pseudo_next_long(self):
        r"""use find for a non nested \subsection[label="student id"]{title}:next

        should stop at the next \subsection
        """
        tex_source = self.sample_tex
        expected_res = (
            ('\\subsection', {'title': 'Student identification'}),
            r'\begin{studentid}...e}\end{studentid}')
        res = TexSurgery(tex_source).find('\\subsection[label="student id"]{title}:next')
        self.assertEqual(repr(res), repr(expected_res))
        # and single quotes
        res = TexSurgery(tex_source).find("\\subsection[label='student id']{title}:next")
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_section_pseudo_next_nested(self):
        r"""use find for a nested \section{sectionname}#intro:next run
        """
        tex_source = self.sample_tex
        expected_res = ('\\section', ('run', '\nprint(\'The random seed is \', seed)\n'))
        res = TexSurgery(tex_source).find('\\section{sectiontext}#intro:next run')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_section_pseudo_next_nested_2(self):
        r"""use find for a nested \section{sectionname}#intro:next run
        """
        tex_source = self.sample_tex
        expected_res = ('\\section', ('\\correctchoice', {'choice': r'$\sage{fd}$'}))
        res = TexSurgery(tex_source).find(
            r'\section{sectiontext}#exercises:next \correctchoice{choice}')
        self.assertEqual(repr(res), repr(expected_res))

    def test_find_section_pseudo_next_nested_3(self):
        r"""use find for a nested \subsection{sectionname}#seed:next run
        """
        tex_source = self.sample_tex
        expected_res = ('\\subsection', ('run', '\nprint(\'The random seed is \', seed)\n'))
        res = TexSurgery(tex_source).find('\\subsection{sectiontext}#seed:next run')
        self.assertEqual(repr(res), repr(expected_res))
