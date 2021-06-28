from IPython.core.magic import (
    Magics, magics_class, line_cell_magic, needs_local_scope)
from shlex import split
from .util import MagicParser
from .xml_modules import ParseModule, XPathModule, XMLSchemaModule
from .log import JupyterLogger

@magics_class
class JupyterXML(Magics):

    def __init__(self, shell):
        super(JupyterXML, self).__init__(shell)
        self.parser = MagicParser("%xml")
        self.parser.set_defaults(func=lambda _: (
            self.logger.log("missingmodule")))
        self.parser.add_argument(
            "--verbose", "-v", help="Enable verbose output", action="store_true")
        subparsers = self.parser.add_subparsers(help="Jupyter XML module")

        self.logger = JupyterLogger()
        ParseModule(subparsers, self.logger)
        XPathModule(subparsers, self.logger)
        XMLSchemaModule(subparsers, self.logger)


    @needs_local_scope
    @line_cell_magic
    def xml(self, line, cell=None, local_ns=None):
        try:
            args = self.parser.parse_args(split(line))
            self.logger.set_verbose(args.verbose)
            args.cell = cell
            return args.func(args, local_ns)
        except TypeError as e:
            print(e)