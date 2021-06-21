from wtoolzargs.ordering import scanner
from wtoolzargs.ordering import parser
from wtoolzargs.ordering import interpreter


def order(model, source):
    """
    Returns [sqlalchemy.sql.elements.XYExpression] for given model using
    order DSL.

    Paramaters
    ----------
    model: sqlalchemy model
      sqlalchemy model.
    source: str
      Order DSL (see grammar in details).

    Returns
    -------
    _: [sqlalchemy.sql.elements.XYExpression]
      A thing that can be *passed to query.order_by.

    Raises
    ------
    _: wtoolzargs.wtoolzargsError

    Details
    -------

    Order DSL grammar is:

    expression  -> orderings ;
    orderings   -> order ("," order )* ;
    order       -> identifier ("asc" | "desc")? ;
    identifier  -> IDENTIFIER ;

    And some productions:

    a asc
    a desc
    a desc, b desc
    """

    tokens = scanner.Scanner(source).scan()
    expression = parser.Parser(tokens).parse()
    return interpreter.Interpreter(model, expression).interpret()
