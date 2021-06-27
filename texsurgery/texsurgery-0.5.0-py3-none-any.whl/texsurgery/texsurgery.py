# -*- coding: utf-8 -*-
import os
from random import random, seed, shuffle
import base64
# shlex required later, a job that may be possible to do with pyparsing :-/
# but a solution with shlex works, and solutions with pyparsing seem more complicated
# https://codereview.stackexchange.com/questions/191391/splitting-a-string-by-spaces-without-space-splitting-elements-in-double-quotes
import shlex

from pyparsing import nestedExpr, Optional, Word, alphanums, alphas,\
                      originalTextFor, Literal, SkipTo, Empty, Or, ZeroOrMore, \
                      delimitedList  # ,restOfLine
from pyparsing import _MAX_INT as pyparsing_MAX_INT

from .simplekernel import SimpleKernel


def skipToMatching(opener, closer):
    """

    :param opener: opening token
    :param closer: closing token

    """
    # https://github.com/sagemath/sagetex/issues/6#issuecomment-734968972
    nest = nestedExpr(opener, closer)
    return originalTextFor(nest)


class TexElement(object):
    """
    :param src: ancestral tex document, to which istart and iend refer
    :param istart: opening index
    :param iend: closing index
    :param parent: TexElement inmmediately containing this
    """

    # iend = None since src[slice(0, None)] is the full src
    # curiousity: mystring[0:None] gives an error
    def __init__(self, src=None, istart=0, iend=None, parent=None, *args, **kwds):
        self.src = src
        self.istart = istart
        self.iend = iend
        self.parent = parent

    def __str__(self):
        return self.src[slice(self.istart, self.iend)]


class TexSource(TexElement):
    r"""
    Some bulk tex code, as opposed to environments or commands.
    The whole document or the content of an environment are examples.
    """

    def __init__(self, *args, **kwds):
        super(TexSource, self).__init__(*args, **kwds)
        self.len_repr = kwds.get('length', 40)

    def __repr__(self):
        iend = self.iend or (len(self.src) - 1)
        if iend - self.istart < self.len_repr:
            return self.long_repr()
        return repr((self.src[slice(self.istart, self.istart + self.len_repr//2)]
                     + '...'
                     + self.src[slice(iend - self.len_repr//2, self.iend)]
                     ).replace('\n', ''))

    def long_repr(self):
        return repr(self.src[slice(self.istart, self.iend)])


class Arguments(object):
    r"""
    docstring for Arguments.
    """

    def __init__(self, *args, **kwds):
        self.args = args + tuple(kwds.keys())
        self.named_args = {}
        for k, v in kwds.items():
            self.named_args[k] = v

    def __getitem__(self, k):
        return self.args[k]

    def __getattr__(self, attr):
        if (attr == 'named_args') or attr not in self.named_args:
            return super(Arguments, self).__getattr__(attr)
        return self.named_args[attr]


class EnvOrCommand(TexElement):
    r"""
    :param name: name of the Environment or Command
    :param optional_args: a list of TexElement
    """

    def __init__(self, name='', options=None, arguments=None, *args, **kwds):
        ''''''
        super(EnvOrCommand, self).__init__(*args, **kwds)
        self.name = name
        self.options = options or Arguments()
        self.arguments = arguments or Arguments()

    def __repr__(self):
        return repr(self.name)

    @staticmethod
    def newEnvOrCommand(name, *args, **kwds):
        if name[0] == '\\':
            return Command(name, *args, **kwds)
        return Environment(name, *args, **kwds)


class EnvOrCommandNext(TexElement):
    r"""a TexElement that consists of a Command or Environment followed by a TexElement

    Main use (as of 21-06-17): \section{sectiontitle}#sectionid:next"""

    def __init__(self, commandOrEnv, next, *args, **kwds):
        super(EnvOrCommandNext, self).__init__(*args, **kwds)
        self.commandOrEnv = commandOrEnv
        self.next = next
        self.icontent = next.istart

    def __repr__(self):
        return repr(self.commandOrEnv.name)

    def long_repr(self):
        return '(%s, %s)' % (self.commandOrEnv.long_repr(), repr(self.next))


class Command(EnvOrCommand):
    r"""
    docstring for Command.
    """

    def __init__(self, *args, **kwds):
        super(Command, self).__init__(*args, **kwds)
        # When it comes to searching nested commands (which is what icontent is about),
        # a command starts with '\commandname{...' (length is 2+lname)
        # finishes with '...}'
        # and 'content' is everything in between
        lname = len(self.name)
        self.icontent = self.istart + 2 + lname

    def __repr__(self):
        return "'" + '\\' + self.name + "'"

    def long_repr(self):
        if self.arguments.named_args:
            return repr((self.name, self.arguments.named_args))
        elif self.arguments.args:
            return repr((self.name, self.arguments.args))
        else:
            return repr(self.name)


class Environment(EnvOrCommand):
    r"""
    docstring for Environment.
    """

    def __init__(self, *args, **kwds):
        super(Environment, self).__init__(*args, **kwds)
        lname = len(self.name)
        # The environment starts with \begin{envname} (length is 8+lname)
        # finishes with \end{envname}  (length is 6+lname)
        # content is everything in between
        self.icontent = self.istart + 8 + lname
        self.content = kwds.get('content', '')
        if not self.content and self.iend is not None:
            # TODO: lazy property ?
            self.content = self.src[slice(self.icontent, self.iend - (6 + lname))]

    def long_repr(self):
        if self.arguments.named_args:
            return repr((self.name, self.arguments.named_args, self.content))
        return repr((self.name, self.content))


class Match(tuple):
    r"""
    A call to `findall()` return a ResultSet of Matches

    :param parent: TexElement
        first element of the selector
    :param children: ResultSet of Match
        matches for the rest of the selector that are nested within parent

    displays as a tuple, if possible compatible with current unit tests
    """
    def __new__(cls, parent, children=None):
        return super(Match, cls).__new__(cls, (parent, children))

    def __init__(self, parent, children=None):
        self.parent = parent
        self.children = children

    def flatten(self):
        r'''
        return a FlatMatch, keeping only the first child, and also recursively
        '''
        elements = self._recursive_first_child()
        return FlatMatch(elements)

    def _recursive_first_child(self):
        return (self.parent,) + (self.children[0]._recursive_first_child()
                                 if self.children else ())

    def __repr__(self):
        if self.children:
            return super(Match, self).__repr__()
#            return repr((self.parent, self.children))
        elif isinstance(self.parent, EnvOrCommand):
            return self.parent.long_repr()
        else:
            return repr(self.parent)


class FlatMatch(tuple):
    r"""
    A call to `find()`  returns a FlatMatch, which contains the elements that correspond
    to each part of the selector.

    parent : TexElement
        first element of the selector
    child: FlatMatch
        match for the rest of the selector that is nested within parent
    """
    def __new__(cls, elements):
        return super(FlatMatch, cls).__new__(cls, elements)

    def __repr__(self):
        if len(self) > 1:
            return ('('
                    + ', '.join(repr(o) for o in self[:len(self)-1])
                    + ', '
                    + self[-1].long_repr()
                    + ')')
        else:
            return self[0].long_repr()


class ResultSet(list):
    r"""
    A ResultSet is just a list that keeps track of the TexSurgery
    that created it.
    """
    # Borrowed from BeautifulSoup
    # http://www.crummy.com/software/BeautifulSoup/

    def __init__(self, ts, contentlist):
        super(ResultSet, self).__init__(contentlist)
        self.ts = ts

    def __getattr__(self, key):
        """Raise a helpful exception to explain a common code fix."""
        raise AttributeError(
            "ResultSet object has no attribute '%s'. You're probably treating a list of elements "
            "like a single element. Did you call findall() when you meant to call find()?" % key
        )


class TexSurgery(TexElement):
    r"""
    TexSurgery allows to make some replacements in LaTeX code
    """

    # TODO: logging level
    def __init__(self, tex_source, path='.', verbose=True):
        super(TexSurgery, self).__init__(tex_source)
        self.original_src = tex_source
        self.src = tex_source
        self.path = path
        # self.kernel is a lazy property
        self._kernels = dict()
        self.kernel_names = []
        self._auxfiles = 0
        # A random number to distinguish different concurrent jobs
        self._id = str(random())[2:]
        # self.codeparser is a lazy property
        self._codeparser = None
        self.verbose = verbose

    def __del__(self):
        r"""
        Destructor. Shuts down kernel safely.
        """
        self.shutdown()

    def shutdown(self):
        if self._kernels:
            for kernel in self._kernels.values():
                kernel.kernel_manager.shutdown_kernel()
            self._kernels = dict()

    @property
    def kernels(self):
        if not self._kernels:
            self._kernels = {
                kernelname:SimpleKernel(kernelname, verbose=self.verbose)
                for kernelname in self.kernel_names}
        return self._kernels

    @property
    def codeparser(self):
        if not self._codeparser:
            self._build_codeparser()
        return self._codeparser

    def _add_import_action(self, packagename, options):
        def action(l, s, t):
            return '\\documentclass' + t.restofline + '\n\\usepackage%s{%s}' % (
                '[%s]' % options if options else '',
                packagename
            )
        return action

    def add_import(self, packagename, options=''):
        documentclass = (
            '\\documentclass' + SkipTo('\n')('restofline')
        )
        documentclass.setParseAction(
            self._add_import_action(packagename, options)
        )
        self.src = documentclass.transformString(self.src)
        return self

    def data_surgery(self, replacements):
        # TODO: use pyparsing instead of regex, for the sake of uniformity
        src = self.src
        import re
        revars = re.compile('|'.join(r'\\'+key for key in replacements))
        pos, pieces = 0, []
        m = revars.search(src)
        while m:
            start, end = m.span()
            pieces.append(src[pos:start])
            # start+1, since the backslash \ is not part of the key
            name = src[start+1:end]
            pieces.append(replacements[name])
            pos = end
            m = revars.search(src, pos=pos)
        pieces.append(src[pos:])
        self.src = ''.join(map(str, pieces))
        return self

    def _latexify(self, results):
        # TODO do something special with 'text/html'?
        # TODO error -> texttt
        result = ''
        for r in results:
            hasimage = r.get('image/png')
            if hasimage:
                images_folder = 'images'
                images_path = os.path.join(self.path, images_folder)
                filename = 'texsurgery_image_{}_{}.png'.format(
                    self._id, self._auxfiles
                )
                fullpath = os.path.join(images_path, filename)
                if not os.path.exists(images_path):
                    os.mkdir(images_path)
                with open(fullpath, 'wb') as fd:
                    fd.write(base64.b64decode(hasimage))
                result += '\n\\includegraphics{%s}\n' % os.path.join(images_folder, filename)
                self._auxfiles += 1
            else:
                if r.get('text/latex'):
                    result += r.get('text/latex')[1:-1]
                else:
                    result += r.get('text/plain') or r.get('text/html') or r.get('error')
        return result

    def _select_kernel(self, t):
        if 'options' in t:
            kernel = self.kernels[t['options']]
        else:
            kernel = self.kernels[self.kernel_names[0]]
        return kernel

    def _runsilent(self, l, s, t):
        self._select_kernel(t).executesilent(t.content)
        return ''

    def _run(self, l, s, t):
        return self._latexify(self._select_kernel(t).execute(t.content, allow_errors=True))

    def _eval(self, l, s, t):
        # TODO: optional format code here
        code = t.code[1:-1]
        return self._latexify(self._select_kernel(t).execute(code))

    def _srepl(self, l, s, t):
        r"""
        Use for a block of code that should reflect what happens in an interactive sage session
        (both input and output)
        """
        code = t.content.strip()
        lines = code.split('\n')+['']
        if not lines:
            return ''
        result = '\\begin{verbatim}\n'
        partialblock = lines.pop(0) + '\n'
        result += 'sage: ' + partialblock
        while lines:
            line = lines.pop(0)
            if line and line[0] in [' ', '\t']:
                partialblock += line + '\n'
                result += '....: ' + line + '\n'
            else:
                answer = self._latexify(self.kernels['sagemath'].execute(partialblock))
                if len(answer)>0:
                    result += answer + '\n'
                partialblock = line + '\n'
                if line:
                    result += 'sage: ' + line + '\n'
        return result + '\\end{verbatim}'

    def _comments(self, l, s, t):
        return

    def _latex_escape(self, text):
        """
            :param text: a plain text message
            :return: the message escaped to appear correctly in LaTeX
        """
        # TODO: use pyparsing, not regex
        import re
        conv = {
            '&': r'\&',
            '%': r'\%',
            '$': r'\$',
            '#': r'\#',
            '_': r'\_',
            '{': r'\{',
            '}': r'\}',
            '~': r'\textasciitilde{}',
            '^': r'\^{}',
            '\\': r'\textbackslash{}',
            '<': r'\textless{}',
            '>': r'\textgreater{}',
        }
        regex = re.compile('|'.join(
            re.escape(key)
            for key in sorted(conv.keys(), key=lambda item: - len(item))))
        text_wo_latex_special = regex.sub(lambda match: conv[match.group()], text)
        return text_wo_latex_special.replace('\xc2\xa0', '').replace('€', '\\geneuro')

    def _escape_string(self, s):
        if isinstance(s, str) and (s[0] == s[-1] == "'" or s[0] == s[-1] == '"'):
            return s[1:-1].replace(r'\\', '\\').replace('\\n', '\n')
        return s

    def _evalstr(self, l, s, t):
        return self._latex_escape(self._evaltex(l, s, t))

    def _evaltex(self, l, s, t):
        code = t.code[1:-1]
        kernel = self.kernels[self.kernel_names[0]]
        results = kernel.execute(code)
        return '\n'.join(
            r.get('text/tex') or
            self._escape_string(r.get('text/plain')) or
            r.get('text/html') or
            r.get('error') or ''
            for r in results
        )

    def _sage(self, l, s, t):
        code = t.code[1:-1]
        return self._latexify(self.kernels['sagemath'].execute('latex(%s)'%code))

    def _sinput(self, l, s, t):
        filename = t.filename[1:-1]
        with open(filename, 'r') as codefile:
            code = codefile.read()
        return self._latexify(self._select_kernel(t).execute(code))

    def _truish(self, s):
        r'''
        Return True if the string correspond to the True value
        in the current kernel.
        '''
        if self.kernel_names[0] in ('python2', 'python3', 'sagemath'):
            # TODO: non exhaustive (but just a helper for the user!)
            return s not in ('False', '', '[]', '0', '0.0')
        else:
            return s in ('true', 'True')

    def _sif(self, l, s, t):
        r"""
        `\sif{condition}{texif}{texelse}`
        Uses only the first kernel.
        The strings texif and texelse are not code to be executed, but tex strings,
        but those strings may contain \eval{code}.
        """
        kernel = self.kernels[self.kernel_names[0]]
        code = t.condition[1:-1]
        results = kernel.execute(code)
        if (len(results) == 1 and self._truish(results[0].get('text/plain'))):
            return self.codeparser.transformString(t.texif[1:-1])
        else:
            return self.codeparser.transformString(t.texelse[1:-1])

    def _build_codeparser(self):
        # Look for usepackage[kernel]{surgery} markup to choose sage, python, R, julia
        #  or whatever interactive command line application
        # Use pyparsing as in student_surgery to go through sage|sagestr|sagesilent|sif|schoose|etc
        # in order
        # Use SimpleKernel to comunicate with the kernel

        usepackage = ('\\usepackage' +
                      Optional('[' + delimitedList(Word(alphanums))('kernels') + ']') +
                      '{texsurgery}')
        self.kernel_names = list(usepackage.searchString(self.src, maxMatches=1)[0]['kernels'])
        usepackage.setParseAction(lambda l, s, t: '')
        run = self._parserFor('run')
        run.setParseAction(self._run)
        runsilent = self._parserFor('runsilent')
        runsilent.setParseAction(self._runsilent)
        eval = self._parserFor('\\eval{code}', options=False)
        eval.setParseAction(self._eval)
        evalstr = self._parserFor('\\evalstr{code}', options=False)
        evalstr.setParseAction(self._evalstr)
        evaltex = self._parserFor('\\evaltex{code}', options=False)
        evaltex.setParseAction(self._evaltex)
        sage = self._parserFor('\\sage{code}', options=False)
        sage.setParseAction(self._sage)
        sinput = self._parserFor('\\sinput{filename}', options=False)
        sinput.setParseAction(self._sinput)
        sif = self._parserFor(
            '\\sif{condition}{texif}{texelse}', options=False
        )
        sif.setParseAction(self._sif)
        srepl = self._parserFor('srepl')
        srepl.setParseAction(self._srepl)
        comments = '%' + SkipTo('\n').leaveWhitespace()
        comments.setParseAction(self._comments)
        self._codeparser = (usepackage | run | runsilent | eval | evalstr |
                            evaltex | sage | sif | sinput | srepl | comments)
        # Do not ignore latex comments, because % is a useful python operator
        # Although there is an uncommon situation where this causes trouble:
        # if a comment contains an \eval{...some code...} and evaluation of the code
        # gives a result with a line break, compilation of the tex file will probably fail
#        self._codeparser.ignore('%' + restOfLine)

    def code_surgery(self):
        self.src = self.codeparser.transformString(self.src)
        return self

    def _opts_parser(self, str_opts):
        r'''
        parse a string of the form "key1=val1,key2=val2..."
        '''
        return dict(map((lambda s: s.strip()), str_pair.strip().split('='))
                    for str_pair in str_opts.split(','))

    hierarchy_commands = [
        '\\part', '\\chapter', '\\section', '\\subsection', '\\subsubsection',
        '\\paragraph', '\\subparagraph'
    ]

    def _parserFor(self, selector, options=True):
        parts, args, restrictions, label, pseudo = self._parse_selector(selector)
        name = parts.name
        if args:
            args_parser = sum(
                (Literal('{%s}' % restrictions[arg])(arg) if (arg in restrictions)
                 else Literal('{%s}' % arg[1:])(arg) if (arg[0] == '@')
                 else skipToMatching('{', '}')(arg)
                 for arg in args),
                Empty()
            )
        # Drop this, since a command may have no arguments
#        elif name[0]=='\\':
#            args_parser = skipToMatching('{','}')('content')
        else:
            args_parser = Empty()
        if options:
            args_parser = Optional('[' + Word(alphanums)('options') + ']') + args_parser
        if label:
            label_parser = Literal('\\label{%s}' % label)
        else:
            label_parser = Empty()
        if pseudo and pseudo == ':next':
            try:
                ihierarchy = self.hierarchy_commands.index(name)
                end_alternatives = Or(
                    ['\\end{document}']
                    + [sectioning_command
                       for sectioning_command in self.hierarchy_commands[:ihierarchy+1]])
            except ValueError:
                end_alternatives = '\\end{document}'
            pseudo_parser = SkipTo(end_alternatives)('next')
        else:
            pseudo_parser = Empty()
        if name[0] == '\\':
            return (Literal(name)('name')
                    + args_parser
                    + label_parser
                    + pseudo_parser).leaveWhitespace()
        else:
            return ('\\begin{' + Literal(name)('name') + '}'
                    + args_parser
                    + label_parser
                    + SkipTo('\\end{'+name+'}')('content')
                    + '\\end{' + name + '}'
                    + pseudo_parser).leaveWhitespace()

    def _wholeEnvParserFor(self, env):
        return originalTextFor(
                ('\\begin{' + Literal(env) + '}')
                + SkipTo('\\end{' + env + '}')
                + ('\\end{' + env + '}')
            )('all')

    _command_parser = (
        originalTextFor(Optional('\\') + Word(alphas))('name')
        + originalTextFor(Optional(nestedExpr('[', ']')))('options')
        + (ZeroOrMore(nestedExpr('{', '}')))('namedargs')
        + (originalTextFor(Optional(Literal('#',) + Word(alphanums)))('label')
           & originalTextFor(Optional(Literal(':') + Word(alphas)))('pseudo'))
    )

    def _parse_selector(self, selector):
        parts = self._command_parser.searchString(selector)[0]
        args = []
        if parts.namedargs:
            args += [m[0] for m in parts.namedargs]
        if parts.options:
            options = self._opts_parser(parts.options[1:-1])
            if '_nargs' in options:
                nargs = int(options['_nargs'])
                args += ['arg%d' % k for k in range(nargs)]
                del options['_nargs']
            restrictions = options
        else:
            restrictions = {}
        if parts.label:
            # Remove the # character if label appeared in short format \command#mylabel
            label = parts.label[1:]
        elif 'label' in restrictions:
            # Remove the quotes if label appeared as an option \command[label="a b c"]
            label = restrictions['label'][1:-1]
        else:
            label = None
        return parts, args, restrictions, label, parts.pseudo

    def insertAfter(self, selector, text):
        match = self.find(selector)
        iend = match[-1].iend
        self.src = self.src[:iend] + text + self.src[iend:]
        return self

    def replace(self, selector, text):
        match = self.find(selector)
        if match:
            istart = match[-1].istart
            iend = match[-1].iend
            self.src = self.src[:istart] + text + self.src[iend:]
        return self

    def find(self, selector):
        # quick solution for issue #7
        # TODO: more efficient solution (see last proposal)
        # res = self.findall(selector, maxMatches=1)
        res = self.findall(selector)
        return res[0].flatten() if res else None

    def findall(self, selector, tex=None, maxMatches=pyparsing_MAX_INT, ibegin=0):
        r"""
        Finds all occurrences of a given selector

        currently it is not possible to look for commands nested inside commands,
        the parent can only be an environment.

        :param str selector: a string with the CSS-style selector
        :param str tex: string to search, usually None except for recursive calls
        :param int maxMatches: maximum number of matches, usually either 1 or a very big number

        :returns: ResultSet of Match

        >>> from texsurgery.texsurgery import TexSurgery
        >>> tex = open('../tests/test_find.tex').read()
        >>> TexSurgery(tex).findall('question,questionmultx runsilent')
        [('questionmultx', [('runsilent', '\na = randint(1,10)\n')]), ('questionmultx', [('runsilent', '\na = randint(2,10)\n')]), ('question', [('runsilent', '\na = randint(2,10)\nf = sin(a*x)\nfd = f.derivative(x)\n')])]
        >>> TexSurgery(tex).findall(r'question,questionmultx choices \correctchoice{choice}')
        [('question', [('choices', [('\\correctchoice', {'choice': '$\\sage{fd}$'})])])]
        >>> TexSurgery(tex).findall(r'questionmultx \AMCnumericChoices[_nargs=2]')
        [('questionmultx', [('\\AMCnumericChoices', {'arg0': '\\eval{8+a}', 'arg1': 'digits=2,sign=false,scoreexact=3'})]), ('questionmultx', [('\\AMCnumericChoices', {'arg0': '\\eval{8*a}', 'arg1': 'digits=2,sign=false,scoreexact=3'})])]
        """
        if tex == '':
            return ResultSet(self, [])
        elif tex is None:
            tex = self.src
        # First, if there is a ", " at the top level, we split there
        selector_parts = shlex.split(selector.replace('\\', '\\\\' ))
        if len(selector_parts) > 1 and any((part[-1] == ',') for part in selector_parts):
            partials = []
            partial_selector = ''
            for j, part in enumerate(selector_parts):
                if part[-1] == ',':
                    partial_selector += part[:-1]
                    partials.extend(self.findall(partial_selector))
                    partial_selector = ''
                elif j == len(selector_parts) - 1:
                    partial_selector += part
                    partials.extend(self.findall(partial_selector))
                    partial_selector = ''
                else:
                    partial_selector += part + ' '
            return ResultSet(self, partials)
        parent, *rest = selector_parts
        if rest:
            # If parent is a command, we want to capture its first argument
            # to look for the rest of the selector inside
            alternatives = [env_or_command+'{content}' if env_or_command[0] == '\\'
                            else env_or_command
                            for env_or_command in parent.split(',')]
            names = Or([self._parserFor(env_or_command)
                        for env_or_command in alternatives])
            # if rest, then parent has no attributes :-/
            # issue #7: find calls findall with optional argument maxMatches=1
            #  => find does not find some nested commands that findall finds
            # if self.findall(rest[0], match.content) is None, the only match is discarded
            pyparsing_results = (
                (EnvOrCommand.newEnvOrCommand(
                        name=match.name,
                        src=self.src,
                        istart=ibegin + istart, iend=ibegin + iend - len(match.next)),
                 match, istart, iend)
                for match, istart, iend in names.scanString(tex, maxMatches=maxMatches)
            )
            elements = (
                (EnvOrCommandNext(
                    commandOrEnv=env_or_command,
                    next=TexSource(src=self.src, istart=iend-len(match.next), iend=iend))
                 if match.next else env_or_command,
                 match)
                for env_or_command, match, istart, iend in pyparsing_results)
            nested_matches = (
                (element, self.findall(' '.join(rest), match.next or match.content, ibegin=element.icontent))
                for (element, match) in elements
            )
            return ResultSet(
                self,
                [Match(element, nest) for (element, nest) in nested_matches if nest]
            )

        names = Or([self._parserFor(env_or_command)
                    for env_or_command in selector.split(',')])
        # The tail part of the selector may have named arguments and restrictions
        _, args, _, _, _ = self._parse_selector(selector)
        pyparsing_results = [
            (EnvOrCommand.newEnvOrCommand(
                    name=match.name,
                    src=self.src, istart=ibegin + istart, iend=ibegin + iend - len(match.next),
                    options=match.options,
                    arguments=(Arguments(**{arg: match[arg][1:-1] for arg in args})),
                    content=match.content
                    ),
             match, istart, iend)
            for match, istart, iend in names.scanString(tex, maxMatches=maxMatches)
        ]
        return ResultSet(
            self,
            [Match(EnvOrCommandNext(
                    commandOrEnv=env_or_command,
                    next=TexSource(src=self.src, istart=iend-len(match.next), iend=iend),
                    istart=istart, iend=iend)
                   if match.next else env_or_command)
             for env_or_command, match, istart, iend in pyparsing_results]
        )

    def shuffle(self, parentselector, childrenselector, randomseed=None):
        r'''
        shuffles all matches of childrenselector within each parentselector

        :param parentselector: the selector should match those TexElements that
            host the TexElements to be shuffled. The parents themselves are not shuffled
        :param childrenselector: the TexElements that are shuffled, but each child may be shuffled
            only with its siblings with the same parent, never with a "cousin"
        :param seed: for testing purposes

        Setting the seed should not affect the randomness of the tex treatment.
        In a typical pyexams use, user wants to generate several runs of the file, same code
        but different seed, set globally once at the begginning of the document.
        But that seed is set in the jupyter kernel session, while this seed is set in a
        different environment.
        '''
        if randomseed:
            seed(randomseed)
        src = self.src
        parents = self.findall(parentselector)
        if not parents:
            return self
        nparents = len(parents)
        parts = [src[:parents[0].parent.istart]]
        for i, match in enumerate(parents):
            parent = match.parent
            parentsrc = src[parent.istart:parent.iend]
            children = self.findall(childrenselector, tex=parentsrc)
            nchildren = len(children)
            shuffled = list(range(nchildren))
            shuffle(shuffled)
            # From start of parent to first children
            parts.append(parentsrc[:children[0].parent.istart])
            for j in range(nchildren):
                child_new_order = children[shuffled[j]].parent
                parts.append(parentsrc[child_new_order.istart:child_new_order.iend])
                if j < nchildren-1:
                    # tex between old_order children[j] and old_order children[j+1]
                    intermediate = parentsrc[children[j].parent.iend:children[j+1].parent.istart]
                    parts.append(intermediate)
            # From last children to end of parent
            parts.append(parentsrc[children[-1].parent.iend:])
            if i < nparents-1:
                # tex between parent[i] (which is `parent`) and parent[i+1]
                intermediate = src[parent.iend:parents[i+1].parent.istart]
                parts.append(intermediate)
        parts.append(src[parents[-1].parent.iend:])
        self.src = ''.join(parts)
        return self
