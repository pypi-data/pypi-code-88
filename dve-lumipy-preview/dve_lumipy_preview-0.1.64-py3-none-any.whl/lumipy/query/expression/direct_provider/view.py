from lumipy.common.ipython_utils import live_status_in_cell
from lumipy.query.expression.base_sql_expression import BaseSqlExpression
from lumipy.query.expression.sql_value_type import SqlValType
from lumipy.query.expression.table_op.base_table_op import BaseTableExpression
from IPython.core.display import clear_output
from pandas import DataFrame


class View(BaseSqlExpression):
    """Class representing a query passed to the `Sys.Admin.SetupView` provider.

    """

    def __init__(self, provider_name: str, query: BaseTableExpression):
        """__init__ method of the View class

        Args:
            provider_name (str): name of the provider that will be created/modified. Must be just alphanumerics and '.', '_'.
            query (BaseTableExpression): query that the view is built from.
        """
        if any(not c.isalnum() and c not in ['.', '_'] for c in provider_name) or len(provider_name) == 0:
            raise ValueError(
                "Input value for view provider_name must be non-empty string made up of alphanumeric characters and '.', '_'. "
                f"Was '{provider_name}'"
            )
        if not issubclass(type(query), BaseTableExpression):
            raise ValueError(
                f"Query input must be a table expression (e.g. select, where, limit). Was {type(query).__name__}."
            )

        self._client = query.get_client()

        def setup_view_sql(q):
            return '\n'.join([
                "@x = \nuse Sys.Admin.SetupView",
                f"--provider={provider_name}",
                "--------------",
                q.get_sql(),
                "\nenduse;",
                "\nselect * from @x;"
                ])

        super().__init__(
            "setup view",
            setup_view_sql,
            lambda *x: True,
            lambda *x: SqlValType.Unit,
            query
        )

    def go(self) -> DataFrame:
        """Send query off to Luminesce, monitor progress and then get the result back as a pandas dataframe.

        Returns:
            DataFrame: the result of the query as a pandas dataframe.
        """
        ex_id = 'N/A'
        try:
            ex_id = self._client.start_query(self.get_sql())
            live_status_in_cell(self._client, ex_id)
            df = self._client.get_result(ex_id)
            clear_output(wait=True)
            return df
        except KeyboardInterrupt as ki:
            print("Cancelling query... 💥")
            self._client.delete_query(ex_id)
            raise ki
        except Exception as e:
            raise e

    def print_sql(self):
        """Print the SQL that this expression resolves to.

        """
        print(self.get_sql())

    def go_async(self) -> str:
        """Just send the query to luminesce. Don't monitor progress or fetch result.

        Returns:
            str: the execution ID of the query.
        """
        ex_id = self._client.start_query(self.get_sql())
        print(f"Query running as {ex_id}")
        return ex_id
