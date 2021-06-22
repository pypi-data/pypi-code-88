import os
import logging
import re
import jaydebeapi
import jpype
import pandas as pd

import asyncio
import aiohttp
from pydtc.utils import exec_time, async_retry

## dict of database software name to jdbc driver class name
driver_class = {
               'db2': 'com.ibm.db2.jcc.DB2Driver',
               'teradata': 'com.teradata.jdbc.TeraDriver',
               'sqlserver': 'com.microsoft.sqlserver.jdbc.SQLServerDriver',
               'oracle': 'oracle.jdbc.driver.OracleDriver',
               'mysql': 'com.mysql.cj.jdbc.Driver',
               'hive2': 'org.apache.hive.jdbc.HiveDriver'
               }

class DBClient():
    '''
    Class wrapping the connection to database via jdbc with batch/fast
    load capability.

    The jdbc driver jar file(s) to be supplied by the user which can be easily
    accquired and to be placed into folder jdbc_driver under the user's home
    directory.
    '''

    def __init__(self, db, host, user, password, java_props={}, classname=None, lib_path=None, runtime_path=None):
        '''
        Instance of DBCon class.

        param:
            db: str; db2|teradata|mssql|mysql etc.
            host: str; url of db server.
            user: str
            password: str
            java_props: dict; the java property that to be set system-wide, optional
            classname: str, the forclass name for the jdbc driver
            lib_path: str, default to jdbc_driver under user's home directory
            runtime_path: str; location of the jvm lib, optional       
        '''

        self.logger = logging.getLogger(__name__)

        if runtime_path:
            jvm = runtime_path
        else:
            jvm = jpype.getDefaultJVMPath()

        self._db = db
        self._host = host
        self._user = user
        self._pass = password

        self._conn = None
        self._cur = None
        self._col_prop = {}

        try:
            self._driver = driver_class[db]
        except KeyError:
            if classname:
                self._driver = classname
            else:
                raise Exception('unknown driver class name. specify like: ' +
                                'classname = "com.mysql.jdbc.Driver"')

        if lib_path:
            _lib_path = lib_path
        else:
            _lib_path = os.path.join(os.path.expanduser('~'), 'jdbc_driver')
            if not os.path.exists(_lib_path):
                os.makedirs(_lib_path)

        classes = [c for c in os.listdir(_lib_path) if c.endswith('.jar')]

        if len(classes) == 0:
            raise Exception('no jar file(s) provided in folder {}.'.format(_lib_path))

        if os.name == 'nt':
            _path = ';'.join([os.path.join(_lib_path, c) for c in classes])
        else:
            _path = ':'.join([os.path.join(_lib_path, c) for c in classes])

        args = '-Djava.class.path={}'.format(_path)
        if jpype.isJVMStarted():
            pass
        else:
            jpype.startJVM(jvm, args)
            if java_props:
                system = jpype.JClass("java.lang.System")
                for k, v in java_props.items():
                    system.setProperty(str(k), str(v))


    def connect(self):
        if self._db == 'oracle':
            connectionstring = 'jdbc:{db}:thin:@{host}'.format(db=self._db, host=self._host)
        else:
            connectionstring = 'jdbc:{db}://{host}'.format(db=self._db, host=self._host)

        try:
            self._conn = jaydebeapi.connect(self._driver, connectionstring,
                                            [self._user, self._pass],
                                            None,)

            self._conn.jconn.setAutoCommit(False)
            self._cur = self._conn.cursor()

            self.logger.warning('Connected: %s', self._db.title())

        except jpype.JavaException as err:
            self.logger.error(err)
            raise

    @exec_time()
    def update_sql(self, sqlstr, errmsg = 'Update Failed'):
        '''
        param:
            sqlstr: str; sql statement, e.g. create temporary table temp (id int); delete from tbl
        '''

        try:
            stmt = self._conn.jconn.createStatement()
            if sqlstr.lower().startswith('delete'):
                stmt.execute(sqlstr)
            else:
                stmt.executeUpdate(sqlstr)
            self._conn.commit()

            stmt.close()
        except Exception:
            self.logger.exception(errmsg)
            raise

    @exec_time()
    def create_temp(self, sqlstr):
        self.update_sql(sqlstr, errmsg='Temporary table creation failed.')

    @exec_time()
    def load_batch(self, sqlstr, indata, chunksize=10000, errmsg='Batch load failed.'):
        '''
        param:
            sqlstr: str; sql statement
            indata: DataFrame; data to be inserted into the table, support int and string data type
            chunksize: int; default to 10000
        sample:
            sqlstr: insert into Demo (col1, col2) values (?,?)
        '''

        if isinstance(indata, pd.DataFrame):
            try:
                pstmt = self._conn.jconn.prepareStatement(sqlstr)

                _schema = [str(indata[c].dtype) for c in indata.columns]
                for i in range(0, len(indata), chunksize):
                    _data = indata.iloc[i: i+chunksize]
                    for j in zip(*_data.T.values.tolist()):
                        for k in range(len(j)):
                            if _schema[k].find('int') == 0:
                                pstmt.setInt(k+1, j[k])
                            elif _schema[k].find('obj') == 0:
                                pstmt.setString(k+1, j[k])

                        pstmt.addBatch()

                    pstmt.executeBatch()

                self._conn.commit()
                pstmt.close()
            except Exception:
                self.logger.exception(errmsg)
                raise
        else:
            raise Exception('Input takes dataframe only.')


    @exec_time()
    def load_temp(self, sqlstr, indata, chunksize=10000):
        self.load_batch(sqlstr, indata, chunksize=10000, errmsg='Temporary table insertion failed.')


    @exec_time()
    def read_sql(self, sqlstr, custom_converters=None):
        '''
        param:
            sqlstr: str; sql statement
            custom_converters: default to use builtin.
        '''
        if custom_converters == None:
            converters = jaydebeapi._converters
        elif isinstance(custom_converters, dict):
            converters = {**jaydebeapi._converters, **custom_converters}
        else:
            raise Exception('Dictionary of column type and custom function to be provide.')


        stmt = self._conn.jconn.createStatement()
        try:
            stmt.execute(sqlstr)

            result = stmt.getResultSet()
            meta = result.getMetaData()
            column_count = meta.getColumnCount()

            rows, columns, converter_func = [], [], []

            for col in range(1, column_count+1):
                _coltyp = meta.getColumnType(col)
                _colnm = meta.getColumnName(col)
                self._col_prop[_colnm] = _coltyp
                converter = converters.get(_coltyp, jaydebeapi._unknownSqlTypeConverter)
                converter_func.append(converter)
                columns.append(_colnm)
                
            while result.next():
                row = []
                for i in range(column_count):
                    row.append(converter_func[i](result, i+1))
                rows.append(row)

            self._conn.commit()

            if rows:
                return pd.DataFrame(rows, columns=columns)
            else:
                return pd.DataFrame(columns=columns, dtype=object)
        except Exception as e:
            self.logger.error(str(e))
            raise
        finally:
            stmt.close()


    def close(self):
        try:
            self._cur.close()
            self._conn.close()
        except Exception as e:
            self.logger.warning(e)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()


class APIClient():
    '''
    Class wrapping connection to RESTful api utilizing aiohttp package for concurrent requests.
    '''

    def __init__(self, auth=None, loop=None, **kwargs):
        '''
        param:
            auth: requests authentication; default: None
            loop: EventLoop; default: None
        '''

        self._session = aiohttp.ClientSession(auth=auth, loop=loop, **kwargs)


    @async_retry(Exception, logger = logging.getLogger('retry'))
    async def fetch(self, url):
        async with self._session.get(url) as response:
            status = response.status
            if status == 200:
                return await response.json()
            else:
                if response.text:
                    raise Exception('Status Code: {}; Message: {}'.format(status, await response.json()))
                else:
                    raise Exception('GET Failed: {}'.format(status))


    async def fetch_all(self, urls):
        results = await asyncio.gather(
            *[self.fetch(url) for url in urls],
            return_exceptions=True
        )

        return results


    @async_retry(Exception, logger=logging.getLogger('retry'))
    async def update(self, url, data=None, method='put'):
        _requests = {'post' : self._session.post,
                     'put' : self._session.put,
                     'patch' : self._session.patch,
                     'delete' : self._session.delete
        }

        if method not in _requests:
            raise Exception('unknown action.')

        async with _requests[method](url, json=data) as response:
            status = response.status
            if status == 200:
                return await response.json()
            else:
                if response.text:
                    raise Exception('Status Code: {}; Message: {}'.format(status, await response.json()))
                else:
                    raise Exception('UPDATE Failed: {}'.format(status))


    async def close(self):
        await self._session.close()
    

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()