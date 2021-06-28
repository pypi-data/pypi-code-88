from lxml import etree
from .util import strip_comments


class XMLModule():
    def __init__(self, name, parser, logger, help=""):
        self.name = name
        self.logger = logger
        self.parser = parser.add_parser(name, help=help)
        self.parser.set_defaults(func=self.handle)

    def handle(self, params, local_ns=None):
        raise NotImplementedError()


class ParseModule(XMLModule):
    def __init__(self, parser, logger):
        super().__init__("parse", parser, logger, "Module for parsing trees from xml")
        self.parser.add_argument(
            "--label", "-l", help="Store parsed xml tree with this label")
        self.parser.add_argument(
            "--var", "-v", help="Store the result in a given variable"
        )
        self.parser.add_argument(
            "--from-var", "-f", help="Parse from variable"
        )

    def handle(self, params, local_ns=None):
        if params.from_var is not None:
            if params.from_var in local_ns:
                params.cell = local_ns[params.from_var]
            else:
                self.logger.print(f"Variable {params.from_var} not found.")
        if params.cell is None:
            self.logger.print("Cannot parse empty cell.")
            return
        try:
            tree = etree.ElementTree(etree.fromstring(params.cell))
            if params.label is not None:
                local_ns["xmltrees"][params.label] = tree
                local_ns["xmlsources"][params.label] = params.cell
            local_ns["xmltrees"]["last"] = tree
            local_ns["xmlsources"]["last"] = params.cell
            self.logger.print("Successfully parsed XML.")
            if params.var is not None:
                local_ns[params.var] = tree
        except Exception as e:
            self.logger.print("Could not parse XML. Error:\n"+str(e))
            if params.label is not None:
                local_ns["xmltrees"][params.label] = None
                local_ns["xmlsources"][params.label] = params.cell
            local_ns["xmltrees"]["last"] = None
            local_ns["xmlsources"]["last"] = params.cell


class XPathModule(XMLModule):
    def __init__(self, parser, logger):
        super().__init__("xpath", parser, logger, "Module for querying xml trees using XPath")
        self.parser.add_argument("target", help="Label of target graph")
        self.parser.add_argument(
            "--label", "-l", help="Store element resulting from XPath")
        self.parser.add_argument(
            "--show-result", "-s", help="Prints all resulting elements", action='store_true')
        self.parser.add_argument(
            "--var", "-v", help="Store the result in a given variable"
        )
        self.parser.add_argument(
            "--from-var", "-f", help="Parse from variable"
        )

    def handle(self, params, local_ns=None):
        if params.from_var is not None:
            if params.from_var in local_ns:
                params.cell = local_ns[params.from_var]
            else:
                self.logger.print(f"Variable {params.from_var} not found.")
        if params.cell is None:
            self.logger.print("Cannot parse empty cell.")
            return
        if params.target not in local_ns["xmltrees"]:
            self.logger.print(f"Target tree {params.target} not found.")
            return
        xpath = strip_comments(params.cell)
        xpath = xpath.replace('\n', '').replace('\r', '').strip()
        result = local_ns["xmltrees"][params.target].xpath(xpath)
        if params.label is not None:
            local_ns["xmlpaths"][params.label] = xpath
            local_ns["xmlpathresults"][params.label] = result
        local_ns["xmlpaths"]["last"] = xpath
        local_ns["xmlpathresults"]["last"] = result
        if params.var is not None:
            local_ns[params.var] = result
        if params.show_result:
            self.print_result(result)

    def print_result(self, result):
        for (i, element) in enumerate(result):
            if isinstance(element, etree._Element):
                self.logger.print(
                    f"{i}:" + etree.tostring(element, encoding="unicode"))
            else:
                self.logger.print(f"{i}:" + str(element))


class XMLSchemaModule(XMLModule):
    def __init__(self, parser, logger):
        super().__init__("xmlschema", parser, logger,
                         "Module for validating XML using XMLSchema")
        self.parser.add_argument("action", choices=[
                                 "parse", "validate"], help="Do you want to parse a schema or validate a tree")
        self.parser.add_argument(
            "--schema-label", "-l", help="Store or select a parsed xml schema")
        self.parser.add_argument(
            "--tree-label", "-t", help="Label of tree which you want to validate")
        self.parser.add_argument(
            "--var", "-v", help="Store the result in a given variable"
        )
        self.parser.add_argument(
            "--from-var", "-f", help="Parse from variable"
        )

    def handle(self, params, local_ns=None):
        if params.action == "parse":
            return self.parse(params, local_ns)
        elif params.action == "validate":
            return self.validate(params, local_ns)

    def parse(self, params, local_ns=None):
        if params.from_var is not None:
            if params.from_var in local_ns:
                params.cell = local_ns[params.from_var]
            else:
                self.logger.print(f"Variable {params.from_var} not found.")
        if params.cell is None:
            self.logger.print("Cannot parse empty cell.")
            return
        try:
            tree = etree.fromstring(params.cell)
            validator = etree.XMLSchema(tree)
            if params.schema_label is not None:
                local_ns["xmlschemas"][params.schema_label] = validator
                local_ns["xmlschematrees"][params.schema_label] = tree
                local_ns["xmlschemasources"][params.schema_label] = params.cell
            local_ns["xmlschemas"]["last"] = validator
            local_ns["xmlschematrees"]["last"] = tree
            local_ns["xmlschemasources"]["last"] = params.cell
            self.logger.print("Successfully parsed XMLSchema.")
            if params.var is not None:
                local_ns[params.var] = tree
        except Exception as e:
            self.logger.print("Could not parse XMLSchema. Error:\n"+str(e))
            if params.schema_label is not None:
                local_ns["xmlschemas"][params.schema_label] = None
                local_ns["xmlschematrees"][params.schema_label] = None
                local_ns["xmlschemasources"][params.schema_label] = params.cell
            local_ns["xmlschemas"]["last"] = None
            local_ns["xmlschemavalidators"]["last"] = None
            local_ns["xmlschemasources"]["last"] = params.cell

    def validate(self, params, local_ns=None):
        if params.tree_label not in local_ns["xmltrees"]:
            self.logger.print(f"Tree labelled {params.tree_label} not found.")
            return
        if params.schema_label not in local_ns["xmlschemas"]:
            self.logger.print(
                f"Schema labelled {params.schema_label} not found.")
            return
        if local_ns["xmlschemas"][params.schema_label].validate(local_ns["xmltrees"][params.tree_label]):
            self.logger.print("XML is valid!")
            if params.var is not None:
                local_ns[params.var] = True
            return True
        else:
            self.logger.print("XML is not valid. Reason:\n"+str(
                local_ns["xmlschemas"][params.schema_label].error_log.last_error))
            if params.var is not None:
                local_ns[params.var] = False
            return False
