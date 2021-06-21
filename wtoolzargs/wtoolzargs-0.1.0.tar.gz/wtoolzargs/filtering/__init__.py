from wtoolzargs.filtering import scanner
from wtoolzargs.filtering import parser
from wtoolzargs.filtering import interpreter


def filter_(model, source):
    """
    Returns sqlalchemy.sql.elements.XYExpression for given model using
    filter DSL.

    Paramaters
    ----------
    model: sqlalchemy model
      sqlalchemy model.
    source: str
      Filter DSL (see grammar in details).

    Returns
    -------
    _: sqlalchemy.sql.elements.XYExpression
      A thing that can be passed to query.filter.

    Raises
    ------
    _: wtoolzargs.wtoolzargsError

    Details
    -------

    Filter DSL grammar is:

    expression           -> conditional_not ;
    conditional_not      -> "not" conditional_or | conditional_or ;
    conditional_or       -> conditional_and ( "or" conditional_and )* ;
    conditional_and      -> comparison ( "and" comparison )* ;
    comparison           -> identifier
                            ( "ne" | "eq" | "gt" | "ge" | "lt" | "le" )
                            unary | "(" expression ")" ;
    unary                -> "not" unary | primary ;
    primary              -> NUMBER | STRING ;
    identifier           -> IDENTIFIER ;


    And some productions:

    a eq 10
    a eq 'a'
    a eq 'a' and b eq 'b'
    a eq not 'a'
    """

    tokens = scanner.Scanner(source).scan()
    expression = parser.Parser(tokens).parse()
    return interpreter.Interpreter(model, expression).interpret()
