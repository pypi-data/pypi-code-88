from dataclasses import dataclass

@dataclass
class ConfigSql:
    """ Represents config model for SQL connection strings. """
    server: str
    database: str
    uid: str
    pwd: str


    def to_sql_connection_string(self):
        """ Build SQL connection string from SQL properties. """

        # Reference: https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/step-3-proof-of-concept-connecting-to-sql-using-pyodbc?view=sql-server-ver15
        return (
            "DRIVER={SQL Server Native Client 11.0};"
            + f"SERVER={self.server};"
            + f"DATABASE={self.database};"
            + f"UID={self.uid};"
            + f"PWD={self.pwd}"
        )