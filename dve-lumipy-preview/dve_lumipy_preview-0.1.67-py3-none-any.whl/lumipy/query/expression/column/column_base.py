from abc import abstractmethod
from typing import Callable, Union

from lumipy.navigation.field_metadata import FieldMetadata
from lumipy.query.expression.base_sql_expression import BaseSqlExpression
from lumipy.query.expression.sql_value_type import SqlValType


class BaseColumnExpression(BaseSqlExpression):
    """Base class for all of the column classes. Contains the overloads that allow constructon of
    column expressions out of base column class inheritors and python operators.

    Each inheritor of BaseColumnExpression should represent a SQL operation on a column. They are combined together to
    form a directed acyclic graph of expressions that describes the operations that are combined to make a SQL query.
    """

    @abstractmethod
    def __init__(
            self,
            name: str,
            is_main: bool,
            source_table_hash: int,
            sql_str_fn: Callable,
            type_check_fn: Callable,
            data_type_fn: Callable,
            op_name: str,
            *values: Union['BaseColumnExpression', FieldMetadata]
    ):
        """__init__ method for the base column expression class.

        Args:
            name (str): valid python var name for the column (the name to use when it's a member of a table class).
            is_main (bool): whether this is a main field that shows up in 'select ^ from ...'
            source_table_hash (int): hash of the source table this column originated from.
            sql_str_fn (Callable): function that turns the parent values into a SQL piece string.
            type_check_fn (Callable): function that checks the sql value types of the parents.
            return_type_fn (Callable): function that determines the output sql value type of this expression.
            op_name (Callable): name of the operation this class represents.
            *values Union[BaseColumnExpression, FieldDescription]: parent values of the expression.
        """
        if any((not c.isalnum() and c != '_') for c in name) or name[0].isnumeric():
            raise ValueError(f"Column type has an invalid python attribute name: {name}.")

        self._name = name
        self._is_main = is_main
        self._source_table_hash = source_table_hash

        super().__init__(
            op_name,
            sql_str_fn,
            type_check_fn,
            data_type_fn,
            *values
        )

    def get_name(self) -> str:
        """Get the python variable name of this column.

        Returns:
            str: the pythonic name.
        """
        return self._name

    def is_main(self) -> bool:
        """Get whether this is a main column (is selected by 'select ^ ...').

        Returns:
            bool: true if is main column else false.
        """
        return self._is_main

    def source_table_hash(self) -> int:
        """Get the __hash__ value of the column's source table.

        Returns:
            int: the source table hash value.
        """
        return self._source_table_hash

    # noinspection PyUnresolvedReferences
    # import for use in type check will cause circ ref
    def sum(self) -> 'Sum':
        """Apply a sum expression (sql = 'total()') to the column expression.

        This resolves to a 'total' op rather than 'sum' op so the that the behaviour when summing a column of nulls
        matches the pandas dataframe behaviour (sum of a column of nulls is equal to zero).

        This will only work for expressions that resolve to numeric SQL value types.

        Returns:
            Sum: sum aggregate expression object of this column expression.
        """
        from lumipy.query.expression.column_op.aggregation_op import Sum
        return Sum(self)

    # noinspection PyUnresolvedReferences
    # import for use in type check will cause circ ref
    def count(self) -> 'Count':
        """Apply a count expression (sql = 'count([col])') to the column expression.

        The 'count' op will count the number of elements in a column.

        Returns:
            Count: count aggregate expression object of this column expression.
        """
        from lumipy.query.expression.column_op.aggregation_op import Count
        return Count(self)

    # noinspection PyUnresolvedReferences
    # import for use in type check will cause circ ref
    def avg(self) -> 'Average':
        """Apply an avg (equivalent to a mean, sql = 'avg([col])') expression to the column expression

        This will only work for expressions that resolve to numeric SQL value types.

        Returns:
            Average: avg aggregate expression object of this column expression.
        """
        from lumipy.query.expression.column_op.aggregation_op import Average
        return Average(self)

    # noinspection PyUnresolvedReferences
    # import for use in type check will cause circ ref
    def mean(self) -> 'Average':
        """Equivalent to the avg method. Applies an expression that represents computing the mean of a column.

        This will only work for expressions that resolve to numeric SQL value types.

        Returns:
            Average: avg aggregate expression object of this column expression.

        """
        return self.avg()

    # noinspection PyUnresolvedReferences
    # import for use in type check will cause circ ref
    def min(self) -> 'Min':
        """Apply a min expression to this column expression (sql = 'min([col])').

        This will only work for expressions that resolve to numeric SQL value types.

        Returns:
            Min: min expression object applied to this column expression.
        """
        from lumipy.query.expression.column_op.aggregation_op import Min
        return Min(self)

    # noinspection PyUnresolvedReferences
    # import for use in type check will cause circ ref
    def max(self) -> 'Max':
        """Apply a max expression to this column expression (sql = 'max([col])').

        This will only work for expressions that resolve to numeric SQL value types.

        Returns:
            Max: max expression object applied to this column expression.
        """
        from lumipy.query.expression.column_op.aggregation_op import Max
        return Max(self)

    # noinspection PyUnresolvedReferences
    # import for use in type check will cause circ ref
    def median(self) -> 'Median':
        """Apply a median aggregate expression to this column expression (sql = 'median([col])').

        This will only work for expressions that resolve to numeric SQL value types.

        The 'median' op computes the median value of the input. The median is the 'middle value' that separates the top
        half of an ordered set of values from the lower half.
        This input can be a column or an expression made out of columns: e.g. stdev(col1*col2).

        Returns:
            Median: median expression object applied to this column expression.
        """
        from lumipy.query.expression.column_op.aggregation_op import Median
        return Median(self)

    # noinspection PyUnresolvedReferences
    # import for use in type check will cause circ ref
    def stdev(self) -> 'Stdev':
        """Apply a standard deviation aggregate expression to this column expression (sql = 'stdev([col])')

        The 'stdev' op computes the standard deviation of the input. This input can be a column or an expression made
        out of columns: e.g. stdev(col1*col2).

        This will only work for expressions that resolve to numeric SQL value types.

        Returns:
            Stdev: stdev expression object applied to this column expression.
        """
        from lumipy.query.expression.column_op.aggregation_op import Stdev
        return Stdev(self)

    # noinspection PyUnresolvedReferences
    # import for use in type check will cause circ ref
    def quantile(self, value: float) -> 'Quantile':
        """Apply a quantile aggregate expression to this column expression (sql = 'quantile([col], value)')

        Computes the value of a given quantile of the input (the value that bounds this fraction of the data). For
        example a quantile of 0.9 will be the value that 90% of the data is below.

        Args:
            value: the value of the quantile to evaluate.

        Returns:
            Quantile: quantile expression object applied to this oclumn expression.
        """
        if value < 0 or value > 1:
            raise ValueError("Quantiles are only defined between 0 and 1.")

        from lumipy.query.expression.column_op.aggregation_op import Quantile
        return Quantile(self, value)

    # noinspection PyUnresolvedReferences
    # import for use in type check will cause circ ref
    def ascending(self) -> 'AscendingOrder':
        """Apply an ascending order expression to the column expression (sql = '[col] asc').

        Returns:
            AscendingOrder: ascending order expression built from this column expression.
        """
        from .column_ordering import AscendingOrder
        return AscendingOrder(self)

    # noinspection PyUnresolvedReferences
    # import for use in type check will cause circ ref
    def descending(self) -> 'DescendingOrder':
        """Apply a descending order expression to the column expression (sql = '[col] asc').

        Returns:
            DescendingOrder: descending order expression built from this column expression.
        """
        from .column_ordering import DescendingOrder
        return DescendingOrder(self)

    # noinspection PyUnresolvedReferences
    # import for use in type check will cause circ ref
    def with_alias(self, alias: str) -> 'AliasedColumn':
        """Apply an alias expression to the column expression (sql = '[col] as my_alias')

        Args:
            alias (str): alias to apply to the column

        Returns:
            AliasedColumn: aliased column expression build from the column expression.

        """
        from lumipy.query.expression.column.column_alias import AliasedColumn
        return AliasedColumn(self, alias)

    def __hash__(self):
        return hash(self.source_table_hash() + super().__hash__())

    def __add__(self, other):
        from ..column_op.binary_op import Add
        return Add(self, other)

    def __sub__(self, other):
        from ..column_op.binary_op import Sub
        return Sub(self, other)

    def __mul__(self, other):
        from ..column_op.binary_op import Mul
        return Mul(self, other)

    def __mod__(self, other):
        from ..column_op.binary_op import Mod
        return Mod(self, other)

    def __floordiv__(self, other):
        from ..column_op.binary_op import Div
        return Div(self, other)

    def __truediv__(self, other):
        from ..column_op.binary_op import Div
        return Div(self, other)

    def __radd__(self, other):
        from ..column_op.binary_op import Add
        return Add(self, other)

    def __rsub__(self, other):
        from ..column_op.binary_op import Sub
        return Sub(self, other)

    def __rmul__(self, other):
        from ..column_op.binary_op import Mul
        return Mul(self, other)

    def __rmod__(self, other):
        from ..column_op.binary_op import Mod
        return Mod(self, other)

    def __rtruediv__(self, other):
        from ..column_op.binary_op import Div
        return Div(self, other)

    def __rfloordiv__(self, other):
        from ..column_op.binary_op import Div
        return Div(self, other)

    def __and__(self, other):
        from ..column_op.binary_op import And
        return And(self, other)

    def __or__(self, other):
        from ..column_op.binary_op import Or
        return Or(self, other)

    def __xor__(self, other):
        from ..column_op.binary_op import BitwiseXor
        return BitwiseXor(self, other)

    def __invert__(self):
        from ..column_op.unary_op import Not
        return Not(self)

    def __eq__(self, other):
        from ..column_op.binary_op import Equals
        return Equals(self, other)

    def __ne__(self, other):
        from ..column_op.binary_op import NotEquals
        return NotEquals(self, other)

    def __gt__(self, other):
        from ..column_op.binary_op import GreaterThan
        return GreaterThan(self, other)

    def __lt__(self, other):
        from ..column_op.binary_op import LessThan
        return LessThan(self, other)

    def __ge__(self, other):
        from ..column_op.binary_op import GreaterThanOrEqual
        return GreaterThanOrEqual(self, other)

    def __neg__(self):
        from ..column_op.unary_op import Negative
        return Negative(self)

    def __le__(self, other):
        from ..column_op.binary_op import LessThanOrEqual
        return LessThanOrEqual(self, other)

    def __rand__(self, other):
        from ..column_op.binary_op import And
        return And(self, other)

    def __ror__(self, other):
        from ..column_op.binary_op import Or
        return Or(self, other)

    def __rxor__(self, other):
        from ..column_op.binary_op import BitwiseXor
        return BitwiseXor(self, other)

    def __pow__(self, power, modulo=None):
        from ..column_op.binary_op import Power
        return Power(self, power)

    def __rpow__(self, other):
        from ..column_op.binary_op import Power
        return Power(other, self)

    def __ceil__(self):
        from ..column_op.unary_op import Ceil
        return Ceil(self)

    def __floor__(self):
        from ..column_op.unary_op import Floor
        return Floor(self)

    def __abs__(self):
        from ..column_op.unary_op import Abs
        return Abs(self)

    def __round__(self, n=None):
        from ..column_op.binary_op import Round
        if n is not None and n < 0:
            raise ValueError("Number of places to round a value to must be non-negative!")
        return Round(self, n if n is not None else 0)

    def cast(self, val_type: type):

        from ..column_op.binary_op import CastTo

        if val_type == int:
            return CastTo(self, SqlValType.Int.name)
        elif val_type == bool:
            return CastTo(self, SqlValType.Boolean.name)
        elif val_type == str:
            return CastTo(self, SqlValType.Text.name)
        elif val_type == float:
            return CastTo(self, SqlValType.Double.name)
        else:
            valid_types = [int, bool, str, float]
            raise TypeError(
                f"Invalid input to cast: {val_type}. "
                f"Supported inputs are the types {', '.join(t.__name__ for t in valid_types)}."
            )

    def exp(self):
        from ..column_op.unary_op import Exp
        return Exp(self)

    def log(self):
        from ..column_op.unary_op import LogE
        return LogE(self)

    def log10(self):
        from ..column_op.unary_op import Log10
        return Log10(self)

    def len(self):
        from ..column_op.unary_op import Len
        return Len(self)

    def sqrt(self):
        return self**0.5

    def square(self):
        return self**2

    def ceil(self):
        return self.__ceil__()

    def floor(self):
        return self.__floor__()

    def abs(self):
        return self.__abs__()

    def round(self, n_places=None):
        return self.__round__(n_places)

    def sign(self):
        from ..column_op.unary_op import Sign
        return Sign(self)

    def trim(self, trim_str=None, trim_type='both'):
        from ..column_op.binary_op import Trim

        trim_text = trim_str if trim_str is not None else ''

        if trim_type.lower() == 'both':
            return Trim(self, trim_text, '')
        elif trim_type.lower() == 'left':
            return Trim(self, trim_text, 'l')
        elif trim_type.lower() == 'right':
            return Trim(self, trim_text, 'r')
        else:
            raise ValueError(
                f"Invalid trim type '{trim_type}'. Must be one of 'right', 'left' or 'both'. Defaults to 'both'."
            )

    # noinspection PyUnresolvedReferences
    # import for use in type check will cause circ ref
    def like(self, other: str) -> 'Like':
        """Apply a 'like' condition expression to this expression (sql = '[col] like '%example%')

        The like operation is for case-insensitive pattern matching in strings where you're looking for a value located
        somewhere in the string. There are two wildcards: '%' which matches and sequence of characters and '_' which
        matches any single character.

        This expression and the argument to like must both resolve to Text SQL value types.

        Args:
            other (Union[str, BaseColumnExpression]): string literal or a column expression that resolves to Text SQL
            value type.

        Returns:
            Like: the Like expression object that represents this operation.
        """
        from ..column_op.binary_op import Like
        return Like(self, other)

    # noinspection PyUnresolvedReferences
    # import for use in type check will cause circ ref
    def not_like(self, other: str) -> 'NotLike':
        """Apply a 'not like' condition expression to this expression (sql = '[col] not like '%example%').

        The not like operation is the negation of case-insensitive pattern matching in strings where you're looking for
        a value located somewhere in the string. There are two wildcards: '%' which matches and sequence of characters
        and '_' which matches any single character.

        This expression and the argument to not like must both resolve to Text SQL value types.

        Args:
            other (Union[str, BaseColumnExpression]): string literal or a column expression that resolves to Text SQL
            value type.

        Returns:
            NotLike: the NotLike expression object that represents this operation.

        """
        from ..column_op.binary_op import NotLike
        return NotLike(self, other)

    # noinspection PyUnresolvedReferences
    # import for use in type check will cause circ ref
    def glob(self, other: str) -> 'Glob':
        """Apply a 'glob' condition expression to this expression (sql = '[col] glob '*example*').

        The glob operation does unix-style string pattern matching. It is case sensitive and there are two wildcards:
        '*' will match any sequence of characters '?' matches a single character.

        This expression and the argument to glob must both resolve to Text SQL value types.

        Args:
            other (Union[str, BaseColumnExpression]): string literal or a column expression that resolves to Text SQL
            value type.

        Returns:
            Glob: the Glob expression object that represents this operation.

        """
        from ..column_op.binary_op import Glob
        return Glob(self, other)

    # noinspection PyUnresolvedReferences
    # import for use in type check will cause circ ref
    def not_glob(self, other: str) -> 'NotGlob':
        """Apply a 'not glob' condition expression to this expression (sql = '[col] not glob '*example*').

        Negation of the glob operation that does unix-style string pattern matching. It is case sensitive and there are
        two wildcards '*' will match any sequence of characters '?' matches a single character.

        This expression and the argument to not glob must both resolve to Text SQL value types.

        Args:
            other (Union[str, BaseColumnExpression]): string literal or a column expression that resolves to Text SQL
            value type.

        Returns:
            NotGlob: the NotGlob expression object that represents this operation.

        """
        from ..column_op.binary_op import NotGlob
        return NotGlob(self, other)

    # noinspection PyUnresolvedReferences
    # import for use in type check will cause circ ref
    def regexp(self, other) -> 'Regexp':
        """Apply a 'regexp' condition expression to this expression (sql = '[col] regexp 'example[0-9A-Za-z]*$').

        The regexp operation checks whether a regular expression finds a match in the input string. It is case sensitive.

        This expression and the argument to regexp must both resolve to Text SQL value types.

        Args:
            other (Union[str, BaseColumnExpression]): string literal or a column expression that resolves to Text SQL
            value type.

        Returns:
            Regexp : the Regexp expression object that represents this operation.

        """
        from ..column_op.binary_op import Regexp
        return Regexp(self, other)

    # noinspection PyUnresolvedReferences
    # import for use in type check will cause circ ref
    def not_regexp(self, other) -> 'NotRegexp':
        """Apply a 'not regexp' condition expression to this expression (sql = '[col] not regexp 'example[0-9A-Za-z]*$').

        Negation of the regexp operation that checks whether a regular expression finds a match in the input string. It is case sensitive.

        This expression and the argument to not regexp must both resolve to Text SQL value types.

        Args:
            other (Union[str, BaseColumnExpression]): string literal or a column expression that resolves to Text SQL
            value type.

        Returns:
            NotRegexp : the NotRegexp expression object that represents this operation.

        """
        from ..column_op.binary_op import NotRegexp
        return NotRegexp(self, other)

    # noinspection PyUnresolvedReferences
    # import for use in type check will cause circ ref
    def is_null(self) -> 'IsNull':
        """Apply an 'is null' condition expresson to this expression (sql = '[col] is null').

        Conditional operation that evaluates whether a value is null.

        Returns:
            IsNull: the IsNull instance that represents 'is null' applied to this expression.
        """
        from ..column_op.unary_op import IsNull
        return IsNull(self)

    # noinspection PyUnresolvedReferences
    # import for use in type check will cause circ ref
    def is_not_null(self) -> 'NotIsNull':
        """Apply an 'is not null' condition expresson to this expression (sql = '[col] is not null').

        Conditional operation that evaluates whether a value is not null.

        Returns:
            NotIsNull: the NotIsNull instance that represents 'is not null' applied to this expression.
        """
        from ..column_op.unary_op import IsNotNull
        return IsNotNull(self)

    # noinspection PyUnresolvedReferences
    # import for use in type check will cause circ ref
    def is_in(self, *others) -> 'IsIn':
        """Apply 'in' expression to this expression given a list of values (sql = '[col] in ('A', 'B', 'C')'.

        The 'in' op is a conditional that evaluates whether a column value is a member of an array.

        Args:
            others:

        Returns:
            IsIn: the IsIn instance that represents the 'in' condition applied to this expression and argument.
        """
        from ..column_op.binary_op import IsIn
        from lumipy.query.expression.column.collection import CollectionExpression
        from collections.abc import Sequence

        if len(others) == 0:
            raise ValueError("Empty arg for IN.")
        elif len(others) == 1 and isinstance(others[0], Sequence):
            collection = CollectionExpression(*others[0])
            return IsIn(self, collection)
        else:
            collection = CollectionExpression(*others)
            return IsIn(self, collection)

    # noinspection PyUnresolvedReferences
    # import for use in type check will cause circ ref
    def not_in(self, *others) -> 'NotIn':
        """Apply 'not in' expression to this expression given a list of values (sql = '[col] not in ('A', 'B', 'C')'.

        The 'not in' op is a conditional that evaluates whether a column value is not a member of an array.

        Args:
            other List[Union[str, int, float]]: list of python primitives to check non-membership of.

        Returns:
            NotIn: the NotIn instance that represents the 'not in' op applied to this expression and argument.
        """
        from ..column_op.binary_op import NotIn
        from lumipy.query.expression.column.collection import CollectionExpression
        from collections.abc import Sequence

        if len(others) == 0:
            raise ValueError("Empty arg for NOT IN.")
        elif len(others) == 1 and isinstance(others[0], Sequence):
            collection = CollectionExpression(*others[0])
            return NotIn(self, collection)
        else:
            collection = CollectionExpression(*others)
            return NotIn(self, collection)

    # noinspection PyUnresolvedReferences
    # import for use in type check will cause circ ref
    def between(self, other1, other2) -> 'Between':
        """Apply 'between' expression to this expression given two values that define an interval
        (sql = '[col] between 1 and 2').

        The 'between' op is a conditional that evaluates whether a column value is between two values.
        The SQL value types of this expression and the arguments must resolve to either numerics, date or datetime; or
        be int, float, date, datetime python objects.

        Args:
            other1 Union[int, float, datetime, BaseColumnExpression]: lower limit of the interval.
            other2 Union[int, float, datetime, BaseColumnExpression]: upper limit of the interval.

        Returns:
            Between: the Between instance that represents the 'between' op applied to this expression.
        """
        from ..column_op.ternary_op import Between
        return Between(self, other1, other2)

    # noinspection PyUnresolvedReferences
    # import for use in type check will cause circ ref
    def not_between(self, other1, other2) -> 'NotBetween':
        """Apply 'not between' expression to this expression given two values that define an interval
        (sql = '[col] not between 1 and 2').

        The 'not between' op is a conditional that evaluates whether a column value is not between two values.
        The SQL value types of this expression and the arguments must resolve to either numerics, date or datetime; or
        be int, float, date, datetime python objects.

        Args:
            other1 Union[int, float, datetime, BaseColumnExpression]: lower limit of the interval.
            other2 Union[int, float, datetime, BaseColumnExpression]: upper limit of the interval.

        Returns:
            NotBetween: the NotBetween instance that represents the 'not between' op applied to this expression.
        """
        from ..column_op.ternary_op import NotBetween
        return NotBetween(self, other1, other2)

    # noinspection PyUnresolvedReferences
    # import for use in type check will cause circ ref
    def concat(self, other: 'BaseColumnExpression', where: str = 'end') -> 'StringConcat':
        """Concatenate this column expression with another (sql = 'x | y'). Only valid for expressions
        that resolve to Text SQL value type.

        Args:
            other BaseSqlExpression: other expression that resolves to a column of SQL Text values.
            where str: where to concatente the str: "start" or "end" (defaults to "end").
        Returns:
            StringConcat: expression that represents the string concat of this column and other.
        """
        from ..column_op.binary_op import StringConcat
        if where.lower() == 'end':
            return StringConcat(self, other)
        elif where.lower() == 'start':
            return StringConcat(other, self)
        else:
            raise ValueError(f"Invalid input for the where arg: {where}. Must be 'start' or 'end'.")

    def replace(self, target: str, substitute: str):
        from ..column_op.ternary_op import StrReplace
        return StrReplace(self, target, substitute)

    def lower(self):
        from ..column_op.unary_op import LowerCase
        return LowerCase(self)

    def upper(self):
        from ..column_op.unary_op import UpperCase
        return UpperCase(self)

    def soundex(self):
        from ..column_op.unary_op import Soundex
        return Soundex(self)

    def substr(self, start_ind: int, length: int = 1):
        if start_ind == 0:
            raise ValueError(
                f'Invalid input for start_ind: 0. '
                f'SQL substring index must be a positive non-zero int (indexing from string start) or negative '
                f'(indexing backward from string end).'
            )

        from ..column_op.ternary_op import Substr
        return Substr(self, start_ind, length)

    def unicode(self):
        from ..column_op.unary_op import Unicode
        return Unicode(self)

    def replicate(self, times: int):
        from ..column_op.binary_op import Replicate
        return Replicate(self, times)

    def reverse(self):
        from ..column_op.unary_op import Reverse
        return Reverse(self)

    def left_str(self, n_char: int):
        from ..column_op.binary_op import LeftStr
        if n_char < 1:
            raise ValueError("n_char must be positive and non-zero.")
        return LeftStr(self, n_char)

    def right_str(self, n_char: int):
        from ..column_op.binary_op import RightStr
        if n_char < 1:
            raise ValueError("n_char must be positive and non-zero.")
        return RightStr(self, n_char)

    def pad_str(self, length: int, pad_type: str):
        from ..column_op.binary_op import Pad
        if pad_type.lower() == 'right':
            return Pad(self, length, 'r')
        elif pad_type.lower() == 'left':
            return Pad(self, length, 'l')
        elif pad_type.lower() == 'center':
            return Pad(self, length, 'c')
        elif pad_type.lower() == 'centre':
            return Pad(self, length, 'c')
        else:
            raise ValueError(f'Unrecognised pad type: {pad_type}')

    def str_filter(self, filter_str: str):
        from ..column_op.binary_op import StrFilter
        return StrFilter(self, filter_str)

    def char_index(self, chars: str, occurrence: int = 0):
        from lumipy.query.expression.column_op.ternary_op import CharIndex
        return CharIndex(self, chars, occurrence)

    def proper(self):
        from ..column_op.unary_op import Proper
        return Proper(self)

    def capitalize(self):
        return self.proper()

    def contains(self, sub_str: str, case_sensitive: bool = False):
        if case_sensitive:
            return self.glob(f"*{sub_str}*")
        else:
            return self.like(f"%{sub_str}%")

    def starts_with(self, sub_str: str, case_sensitive: bool = False):
        if case_sensitive:
            return self.glob(f"{sub_str}*")
        else:
            return self.like(f"{sub_str}%")

    def ends_with(self, sub_str: str, case_sensitive: bool = False):
        if case_sensitive:
            return self.glob(f"*{sub_str}")
        else:
            return self.like(f"%{sub_str}")
