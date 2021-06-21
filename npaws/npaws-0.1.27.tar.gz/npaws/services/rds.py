import pymysql

from ..config import (
    DB_HOST,
    DB_USER,
    DB_PASSWORD
)


CURSOR_TYPE = pymysql.cursors.DictCursor
DB_CHARSET = "utf8mb4"


class RDSClient():
    """
    """
    
    def __init__(self):
        """
        """
        self._database = pymysql.connect(host=DB_HOST,
                                         db='ebdb',
                                         charset=DB_CHARSET,
                                         user=DB_USER,
                                         password=DB_PASSWORD,
                                         autocommit=True,
                                         cursorclass=CURSOR_TYPE)
        self._cursor = self._database.cursor()
        
    def select_query(self,
                     query: str,
                     fetchone: bool = False) -> object:
        """
        Executes a SELECT query. Returns one or all rows selected.
        :param query: the select query to execute.
        :param fetchone: if set to True, only returns the firt selected row.
                            If set to False, returns all rows.
        """
        print(f'select_query : INFO : Executing query {query}')
        try:
            self._cursor.execute(query)
            if fetchone:
                return self._cursor.fetchone()
            return self._cursor.fetchall()
        except Exception as e:
            print(f'select_query : ERROR : {e}')
    
    
    def update_query(self,
                     query: str) -> bool:
        """
        Executes an UPDATE query. Returns True if query is executed succesfully.
        :param query: the update query to execute. 
        """
        print(f'update_query : INFO : Executing query {query}')
        try:
            self._cursor.execute(query)
            self._database.commit()
            return True
        except Exception as e:
            print(f'select_query : ERROR : {e}')
            return False
        
        
    def delete_query(self,
                     query: str) -> bool:
        """
        Executes a DELETE query. Returns True if query is executed succesfully.
        :param query: the delete query to execute.
        """
        print(f'delete_query : INFO : Executing query {query}')
        try:
            self._cursor.execute(query)
            self._database.commit()
            return True
        except Exception as e:
            print(f'select_query : ERROR : {e}')
            return False


    def insert_query(self,
                     query: str) -> object:
        """
        Executes an INSERT query. Returns the primary key of the inserted row.
        :param query: the insert query to execute.
        """
        print(f'insert_query : INFO : Executing query {query}')
        try:
            self._cursor.execute(query)
            self._database.commit()
            return self._cursor.lastrowid
        except Exception as e:
            print(f'select_query : ERROR : {e}')
            return False
        
    def get_project_version_documents(self,
                                      project_id: int,
                                      version_id: int) -> list:
        """
        """
        query = f"SELECT d.id, d.uri FROM neuralplatform_document d, neuralplatform_dataset dat, neuralplatform_version v WHERE (d.tagged = 1 AND d.dataset_id = dat.id AND dat.project_id = {project_id} AND v.id = {version_id} AND (d.uploadDate BETWEEN v.startDate AND v.endDate));"
        return self.select_query(query, fetchone=False)

    def get_project(self,
                    project_id: int) -> dict:
        """
        """
        query = f"SELECT * FROM neuralplatform_project p WHERE p.id = {project_id};"
        return self.select_query(query, fetchone=True)
    
    def get_project_bucket(self,
                           project_id: int) -> str:
        """
        """
        query = f"SELECT s3Bucket FROM neuralplatform_account a, neuralplatform_project p WHERE p.id = {project_id} AND p.account_id = a.id"
        return self.select_query(query, fetchone=True).s3Bucket
    
    def update_version_status(self,
                              version_id: int,
                              status: str) -> bool:
        """
        """
        query = f"UPDATE neuralplatform_version v SET status = '{status}' WHERE v.id = {version_id};"
        return self.update_query(query)

    def get_project_bucket(self,
                    project_id: int) -> str:
        """
        """
        query = f"SELECT s3Bucket FROM neuralplatform_account a, neuralplatform_project p WHERE p.id = {project_id} AND p.account_id = a.id;"
        return self.select_query(query)
        

    def get_document_name_and_uri(self,
                    document_id: int) -> tuple:
        """
        """
        query = f"SELECT name, uri FROM neuralplatform_document WHERE id = {document_id};"
        return self.select_query(query)
            
            
    def insert_page(self,
                    img_uri: str,
                    document_id: int) -> int:
        """
        """
        query = f'INSERT INTO neuralplatform_page(imgUri, ocrUri, document_id) VALUES ("{img_uri}", "", {document_id});'
        return self.insert_query(query)