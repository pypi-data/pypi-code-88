import psycopg2
import os
from .base_handler import BaseHandler


class DataBaseHandler(BaseHandler):

    _max_id_length = 255
    _max_result_length = 255
    
    def __init__(self, table_name='results'):
        """
        :param table_name: (str) Optional string name of the table logs will be insert into (default is 'results')
        """

        self.connection_info = os.environ.get("ABCUNIT_DB_SETTINGS")
        if not self.connection_info:
            raise KeyError('Please create environment variable ABCUNIT_DB_SETTINGS'
                           'in for format of "dbname=<db_name> user=<user_name>'
                           'host=<host_name> password=<password>"')
        
        self._test_connection()
        self.table_name = table_name
        self._create_table()


    def _test_connection(self):
        try:
            conn = psycopg2.connect(self.connection_info)
        except psycopg2.Error as err:
            print(err)
            raise ValueError('ABCUNIT_DB_SETTINGS string is incorrect. Should be'
                             'in for format of "dbname=<db_name> user=<user_name>'
                             'host=<host_name> password=<password>"')

        conn.close()


    def _create_table(self):
        """
        Creates a table called <self.table_name> with primary key id varchar(255)
        and result varchar(255), if one does not already exist
        """

        with psycopg2.connect(self.connection_info) as conn:
            with conn.cursor() as cur:
                cur.execute(f'CREATE TABLE IF NOT EXISTS {self.table_name}'
                            f'(id varchar({self._max_id_length}) PRIMARY KEY, '
                            f'result varchar({self._max_result_length}) NOT NULL);')
                conn.commit()


    def _delete_table(self):
        """
        Drops the database table
        """

        with psycopg2.connect(self.connection_info) as conn:
            with conn.cursor() as cur:
                cur.execute(f"DROP TABLE {self.table_name};")
                conn.commit()


    def get_result(self, identifier):
        """
        Selects the result of the job with the identifier parsed
        and returns it

        :param identifier: (str) Identifier of the job result
        :return: (str) Result of job
        """

        query = f"SELECT result FROM {self.table_name} " \
                f"WHERE id='{identifier}';"
        
        with psycopg2.connect(self.connection_info) as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                if cur.rowcount > 0:
                    return cur.fetchone()[0]

        return None


    def get_all_results(self):
        """
        :return: (dict) Dictionary of all job identifiers mapped to their respective results
        """

        query = f"SELECT * FROM {self.table_name}"

        with psycopg2.connect(self.connection_info) as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                result_dict = {}
                for (name, result) in cur:
                    result_dict[name] = result

        return result_dict


    def get_successful_runs(self):
        """
        :return: (str list) Returns a list of the identifiers of all successful runs
        """

        query = f"SELECT id FROM {self.table_name} " \
                "WHERE result='success';"
        
        with psycopg2.connect(self.connection_info) as conn:
            with conn.cursor() as cur:
                cur.execute(query)

                return [name[0] for name in cur]


    def get_failed_runs(self):
        """
        :return: (dict) Dictionary of error types mapped to lists of job identifiers which result in them
        """

        query = f"SELECT id, result FROM {self.table_name} " \
                "WHERE result<>'success';"

        with psycopg2.connect(self.connection_info) as conn:
            with conn.cursor() as cur: 
                cur.execute(query)
                failures = {}
                for (name, result) in cur:
                    failures.setdefault(result, [])
                    failures[result].append(name)

        return failures


    def delete_result(self, identifier):
        """
        Deletes entry specified by the given identifier
        from the database

        :param identifier: (str) Identifier of the job
        """

        query = f"DELETE FROM {self.table_name} " \
                f"WHERE id='{identifier}';"

        with psycopg2.connect(self.connection_info) as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                conn.commit()


    def delete_all_results(self):
        """
        Deletes all entries from the table
        """

        with psycopg2.connect(self.connection_info) as conn:
            with conn.cursor() as cur:
                cur.execute(f"DELETE FROM {self.table_name};")
                conn.commit()


    def ran_successfully(self, identifier):
        """
        Returns true / false on whether the result with this
        identifier is successful

        :param identifier: (str) Identifier of the job result
        :return: (bool) Boolean on if job ran successfully
        """

        query = f"SELECT result FROM {self.table_name} " \
                f"WHERE id='{identifier}';"

        with psycopg2.connect(self.connection_info) as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                result = cur.fetchone()
                if result is not None:
                    return result[0] == 'success'

        return False


    def count_results(self):
        """
        :return: (int) Number of results in the table
        """

        with psycopg2.connect(self.connection_info) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT COUNT(*) FROM {self.table_name};")

                return cur.fetchone()[0]


    def count_successes(self):
        """
        :return: (int) Number of successfull results in the table
        """

        query = f"SELECT COUNT(*) FROM {self.table_name} " \
                "WHERE result='success';"

        with psycopg2.connect(self.connection_info) as conn:
            with conn.cursor() as cur:
                cur.execute(query)

                return cur.fetchone()[0]


    def count_failures(self):
        """
        :return: (int) Number of failed results in the table
        """

        query = f"SELECT COUNT(*) FROM {self.table_name} " \
                "WHERE result<>'success';"

        with psycopg2.connect(self.connection_info) as conn:
            with conn.cursor() as cur:
                cur.execute(query)

                return cur.fetchone()[0]


    def insert_success(self, identifier):
        """
        Inserts an entry into the table with a given identifier
        and the result 'success'

        :param identifier: (str) Identifier of the job
        """

        if self.get_result(identifier):
            self.delete_result(identifier)

        query = f"INSERT INTO {self.table_name} " \
                f"VALUES ('{identifier}', 'success');"

        with psycopg2.connect(self.connection_info) as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                conn.commit()


    def insert_failure(self, identifier, error_type='failure'):
        """
        Inserts an entry into the table with a given identifier
        and erroneous result

        :param identifier: (str) Identifier of the job
        :param error_type: (str) Result of the job
        """

        if self.get_result(identifier):
            self.delete_result(identifier)

        error_type = error_type[:self._max_result_length]
        
        query = f"INSERT INTO {self.table_name} " \
                f"VALUES ('{identifier}', '{error_type}');"

        with psycopg2.connect(self.connection_info) as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                conn.commit()

