from gclang.guarded_exception import GuardedException
import click

from .deriving.reverse_visitor import ReverseVisitor as DerivingVisitor
from .executing.visitor import Visitor as ExecutingVisitor
from .translate.latex_visitor import LatexVisitor
from .translate.python_visitor import PythonVisitor
from .gen.GuardedLexer import GuardedLexer
from .gen.GuardedParser import GuardedParser
import sys

from click_repl import register_repl

from antlr4 import CommonTokenStream, FileStream, InputStream


@click.group(help='Guarded command language interpreter')
@click.version_option(prog_name='guarded')
@click.pass_context
def cli(ctx):
    pass

@cli.command(help='Run program and print final state')
@click.pass_context
@click.argument('file')
@click.option('--verbose', '-v', is_flag=True, help='Print result state')
def run(ctx, file, verbose):
    try:
        tree = GuardedParser(CommonTokenStream(GuardedLexer(FileStream(file)))).start()
        result = ExecutingVisitor().visit(tree)
        if verbose:
            print('Final state:')
            for k, v in result.items():
                print(f'{k} = {v}')
    except GuardedException as e:
        sys.stderr.write(str(e) + '\n')
        exit(1)


@cli.command(help='Derive initial state from specified final state')
@click.argument('file')
@click.pass_context
def derive(ctx, file):
    tree = GuardedParser(CommonTokenStream(GuardedLexer(FileStream(file)))).start()
    DerivingVisitor().visit(tree)


@cli.group(help='Translate guarded program to other language')
def translate():
    ...


@translate.command()
@click.pass_context
def latex(ctx):
    print(LatexVisitor().visit(ctx.obj))


@translate.command()
@click.pass_context
def python(ctx):
    PythonVisitor().visit(ctx.obj)

@cli.command(name='repl', help='REPL for guarded command language')
def repl():
    visitor = ExecutingVisitor()
    while True:
        line = input('> ')
        try:
            tree = GuardedParser(CommonTokenStream(GuardedLexer(InputStream(line)))).start()
            result = visitor.visit(tree)

            if 'ans' in result:
                print(result['ans'])
        except BaseException as e:
            print('Error: ' + str(e))

if __name__ == '__main__':
    cli()
