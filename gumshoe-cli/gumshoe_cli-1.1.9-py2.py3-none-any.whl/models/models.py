import logging
from datetime import datetime
import sqlite3
from sqlite3 import Error
import os


if os.path.exists(os.path.join(os.path.dirname(__file__), "../database/test_gumshoe.db")):
    database = os.path.join(os.path.dirname(__file__), "../database/test_gumshoe.db")
else:
    database = os.path.join(os.path.dirname(__file__), "../database/gumshoe.db")

logging.basicConfig(filename=os.path.join(os.path.dirname(__file__), "../logs/app.log"), filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class Database:

    def create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return conn

    def create_table(self, conn, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def setup(self):
        sql_create_habits_table = """ CREATE TABLE IF NOT EXISTS habits (
                                            id integer PRIMARY KEY AUTOINCREMENT,
                                            name text NOT NULL UNIQUE,
                                            quota integer NOT NULL,
                                            period text NOT NULL,
                                            created_at text NOT NULL
                                     ); """

        sql_create_activity_table = """CREATE TABLE IF NOT EXISTS activity (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        habit_id integer NOT NULL,
                                        created_at text NOT NULL,
                                        FOREIGN KEY (habit_id) REFERENCES habits (id)
                                    );"""

        # create a database connection
        conn = self.create_connection(database)

        # create tables
        if conn is not None:
            # create habits table
            self.create_table(conn, sql_create_habits_table)

            # create activities table
            self.create_table(conn, sql_create_activity_table)
        else:
            print("Error! cannot create the database connection.")

    def remove_test_db(self):
        if os.path.exists(os.path.join(os.path.dirname(__file__), "../database/test_gumshoe.db")):
            database = os.path.join(os.path.dirname(__file__), "../database/test_gumshoe.db")
            os.remove(database)
            print("Test Database remove successfully!")
        else:
            print("No Test Database found.")


class HabitModel(Database):

    def show_habit(self,period):
        # create a database connection
        conn = self.create_connection(database)
        c = conn.cursor()
        if period == "all":
            my_cursor = c.execute("SELECT * FROM habits")
        else:
            my_cursor = c.execute("SELECT * FROM habits WHERE period = ?",(period,))
        return my_cursor.fetchall()

    def check_habit_exists(self, habit):
        try:
            conn = self.create_connection(database)
            c = conn.cursor()
            my_cursor = c.execute("SELECT * FROM habits WHERE name = ?", (habit.name,))
            result = my_cursor.fetchall()
            if not result:
                return ()
            else:
                return result[0]
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)
            return ()

    def create_habit(self, habit):
        try:
            d = datetime.now()
            conn = self.create_connection(database)
            c = conn.cursor()
            c.execute("INSERT INTO habits (name, quota, period, created_at) VALUES (?, ?, ?, ?)",
                      (habit.name, habit.quota, habit.period, d.strftime("%Y-%m-%d %H:%M")))
            conn.commit()
            return True
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)
            return False

    def remove_habit(self, id):
        try:
            conn = self.create_connection(database)
            c = conn.cursor()
            c.execute("DELETE FROM habits WHERE id=?", (id,))
            c.execute("DELETE FROM activity WHERE habit_id=?", (id,))
            conn.commit()
            return True
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)
            return False


class ActivityModel(Database):

    def get_activities(self,habit_id):
        try:
            conn = self.create_connection(database)
            c = conn.cursor()
            my_cursor = c.execute("SELECT * FROM activity WHERE habit_id = ?", (habit_id,))
            result = my_cursor.fetchall()
            if not result:
                return ()
            else:
                return result
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)
            return ()

    def complete_activity(self,habit_id):
        try:
            d = datetime.now()
            conn = self.create_connection(database)
            c = conn.cursor()
            c.execute("INSERT INTO activity (habit_id, created_at) VALUES (?, ?)",
                      (habit_id, d.strftime("%Y-%m-%d %H:%M")))
            conn.commit()
            return True
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)
            return False
