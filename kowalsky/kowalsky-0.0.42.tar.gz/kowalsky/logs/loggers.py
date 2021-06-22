import random
from datetime import datetime
import os
import sqlite3
from sqlite3 import Error


def _gen_id():
    return random.randint(0, 10_000_000)


def get_logger(logger, run_name, params):
    if logger == 'local':
        return LocalLogger(run_name, **params)
    elif logger == 'sqlite':
        return SqliteLogger(run_name, **params)
    else:
        return Logger(run_name, **params)


class Logger:

    def __init__(self, run_name, suppress_std=False, time_format="%m.%d.%Y_%H:%M:%S"):
        self.suppress_std = suppress_std
        self.time_format = time_format
        self.run_name = run_name

    def __call__(self, *args, **kwargs):
        self.log(' '.join([str(x) for x in args]))

    def log(self, message):
        tm = datetime.now().strftime(self.time_format)
        formatted_message = f'{tm}: \t{message}'
        self.std(formatted_message)
        return tm, message, formatted_message

    def std(self, message):
        if not self.suppress_std:
            print(message)

    def end_session(self):
        pass

    def _get_env_info(self):
        timestamp = datetime.now().strftime(self.time_format)
        cwd = os.getcwd()
        dir_path = f'{cwd}/logs' if self.run_name == '' else f'{cwd}/logs/{self.run_name}'
        return timestamp, dir_path


class LocalLogger(Logger):

    def __init__(self, run_name, suppress_std=False):
        super(LocalLogger, self).__init__(run_name, suppress_std)
        timestamp, dir_path = super(LocalLogger, self)._get_env_info()
        os.makedirs(dir_path, exist_ok=True)

        self.file_path = f'{dir_path}/{timestamp}.txt'
        self.file = open(self.file_path, 'a')

        self.std(f'Logs init. See {self.file_path}')

    def log(self, message):
        _, _, formatted_message = super(LocalLogger, self).log(message)
        if not self.file.closed:
            self.file.write(f'{formatted_message}\n')

    def end_session(self):
        if not self.file.closed:
            self.file.close()


class SqliteLogger(Logger):

    CREATE_RUN_TABLE = """
        create table if not exists run (
            id integer PRIMARY KEY, 
            name text,
            tm text not null
        )
        """

    CREATE_LOG_TABLE = """
        create table if not exists log (
            id integer PRIMARY KEY,
            run_id integer not null,
            message text,
            tm text not null,
            FOREIGN KEY (run_id) REFERENCES run (id) 
        )
        """

    ADD_RUN = """
        INSERT INTO run(id, name, tm)
                  VALUES(?,?,?)
        """

    ADD_LOG = """
        INSERT INTO log(id, run_id, message, tm)
                  VALUES(?,?,?,?)
        """

    def __init__(self, run_name, suppress_std=False):
        super(SqliteLogger, self).__init__(run_name, suppress_std)
        timestamp, dir_path = super(SqliteLogger, self)._get_env_info()
        os.makedirs(dir_path, exist_ok=True)
        self._init_db(f'{dir_path}/{run_name}.db')
        self._exec(self.CREATE_RUN_TABLE)
        self._exec(self.CREATE_LOG_TABLE)

        self.run_id = _gen_id()
        self._add_run(self.run_id, run_name, timestamp)

    def log(self, message):
        tm, message, _ = super(SqliteLogger, self).log(message)
        self._add_log(_gen_id(), self.run_id, message, tm)

    def end_session(self):
        if self.conn:
            self.conn.close()

    def _init_db(self, db_path):
        self.db_path = db_path
        self.conn = None
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.std(f'Database init. See {self.db_path}')
        except Error as e:
            self.std(e)

    def _add_run(self, id, name, tm):
        try:
            c = self.conn.cursor()
            c.execute(self.ADD_RUN, (id, name, tm))
            self.conn.commit()
        except Error as e:
            self.std(e)

    def _add_log(self, id, run_id, message, tm):
        try:
            c = self.conn.cursor()
            c.execute(self.ADD_LOG, (id, run_id, message, tm))
            self.conn.commit()
        except Error as e:
            self.std(e)

    def _exec(self, command):
        try:
            c = self.conn.cursor()
            c.execute(command)
            self.conn.commit()
        except Error as e:
            self.std(e)
