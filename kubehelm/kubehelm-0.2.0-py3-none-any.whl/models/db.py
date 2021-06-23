from re import search as regular_expression_search
from mysql.connector import connect as mysql_connect
from mysql.connector.errors import DatabaseError


class MySql:
    """
    CREATE USER 'myuser5'@'%' IDENTIFIED VIA mysql_native_password USING '***';

    GRANT USAGE ON *.* TO 'myuser5'@'%' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;

    GRANT ALL PRIVILEGES ON `myuser5\_%`.* TO 'myuser5'@'%';
    GRANT ALL PRIVILEGES ON `mydb3`.* TO 'myuser5'@'%';
    """

    def clean(self, name):
        assert name
        return name

    def validate_ingress_name(self, value):
        if not value or regular_expression_search('^[0-9\-]|[^a-z0-9\-]|\-$', value):
            return False
        return True

    def get_mysql_connect(self):
        return mysql_connect(
            host="localhost",
            port="8000",
            user="root",
            password="root")

    def add_database(self, database, user):
        try:
            mysql_database = self.get_mysql_connect()
            cursor = mysql_database.cursor()
            cursor.execute(f"CREATE DATABASE {self.clean(database)};")
            cursor.close()
            self.grant_privileges(database, user)
        except DatabaseError:
            cursor.close()
            raise

    def add_user(self, user, password):
        command = f"CREATE USER '{self.clean(user)}'@'%' IDENTIFIED BY '{self.clean(password)}';"
        try:
            mysql_database = self.get_mysql_connect()
            cursor = mysql_database.cursor()
            cursor.execute(command)
            cursor.execute("FLUSH PRIVILEGES;")
            cursor.close()
            self.set_user_quotas(user)
        except DatabaseError:
            cursor.close()
            raise

    def grant_privileges(self, database, user):
        command = f"GRANT ALL PRIVILEGES ON `{self.clean(database)}`.* TO '{self.clean(user)}'@'%';"
        try:
            mysql_database = self.get_mysql_connect()
            cursor = mysql_database.cursor()
            cursor.execute(command)
            cursor.execute("FLUSH PRIVILEGES;")
            cursor.close()
        except DatabaseError:
            cursor.close()
            raise

    def set_user_quotas(self, user):
        command = f"GRANT USAGE ON *.* TO '{self.clean(user)}'@'%' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;"
        try:
            mysql_database = self.get_mysql_connect()
            cursor = mysql_database.cursor()
            cursor.execute(command)
            cursor.execute("FLUSH PRIVILEGES;")
            cursor.close()
        except DatabaseError:
            cursor.close()
            raise
