from abc import ABC
import json
from datetime import datetime, date
from urllib.parse import urljoin
from typing import Union
import requests
from requests import HTTPError
from requests.auth import HTTPBasicAuth, AuthBase
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry, )
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


class DatabaseAlreadyExistError(Exception):
    pass


class CollectionAlreadyExistError(Exception):
    pass


class DocumentDotExist(Exception):
    pass


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, (datetime, date)):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)


class TokenAuth(AuthBase):
    def __init__(self, token):
        self._token = token

    def __call__(self, r):
        r.headers['Authorization'] = f'Token {self._token}'
        return r


class Collection(ABC):
    pass


class Database(ABC):
    def collection(self, col_name) -> Collection:
        pass


class FreedbClient:
    def __init__(self, baseurl, token: Union[str, tuple]):
        self._baseurl = baseurl
        session = requests_retry_session()
        if isinstance(token, str):
            session.auth = TokenAuth(token)
        else:
            session.auth = token
        self.session = session

    def _urljoin(self, path):
        return urljoin(self._baseurl, path) 

    def create_database(self, db_name):
        session = self.session
        try:
            response = session.post(self._urljoin('/api/databases'), data={'name': db_name})
            response.raise_for_status()
            return self.database(db_name)
        except requests.exceptions.HTTPError as ex:
            if ex.response.status_code == 409:
                raise DatabaseAlreadyExistError() from ex
            raise

    def create_collection(self, db_name, col_name):
        session = self.session
        try:
            response = session.post(self._urljoin(f'/api/databases/{db_name}/collections'), data={'name': col_name})
            response.raise_for_status()
        except requests.exceptions.HTTPError as ex:
            if ex.response.status_code == 409:
                raise CollectionAlreadyExistError() from ex
            raise

    def save_document(self, db_name, col_name, doc):
        response = self.session.post(self._urljoin(f'/api/databases/{db_name}/collections/{col_name}/documents'), 
            data=json.dumps(doc, cls=DateTimeEncoder), 
            headers={'Content-Type': 'application/json'}, 
            timeout=30)
        response.raise_for_status()
        return response.json()

    def query(self, db_name, col_name, query=None, skip=None):
        params = {}
        if query:
            params['query'] = json.dumps(query)
        if skip:
            params['skip'] = skip
        response = self.session.get(self._urljoin(f'/api/databases/{db_name}/collections/{col_name}'), params=params)
        response.raise_for_status()
        return response.json()

    def get_collection(self, db_name, col_name):
        response = self.session.get(self._urljoin(f'/api/databases/{db_name}/collections/{col_name}'))
        response.raise_for_status()
        return response.json()

    def get_document(self, db_name, col_name, doc_id):
        response = self.session.get(self._urljoin(f'/api/databases/{db_name}/collections/{col_name}/documents/{doc_id}'), 
                                    timeout=30)
        try:
            response.raise_for_status()
        except HTTPError as ex:
            if ex.response.status_code == 404:
                raise DocumentDotExist()
            raise
        return response.json()

    def database(self, database_name) -> Database:
        return FreedbDatabase(self, database_name)

    def list_databases(self):
        response = self.session.get(self._urljoin(f'/api/databases'))
        response.raise_for_status()
        return response.json()


class FreedbDatabase(Database):
    def __init__(self, client:FreedbClient, name):
        self._client = client
        self._name = name

    @property
    def name(self):
        return self._name

    def list_collections(self):
        response = self._client.session.get(self._client._urljoin(f'/api/databases/{self._name}/collections'))
        response.raise_for_status()
        return response.json()

    def create_collection(self, col_name):
        post_data = {'name': col_name}
        response = self._client.session.post(
            self._client._urljoin(f'/api/databases/{self._name}/collections'), 
            data=post_data)
        
        # response.raise_for_status()
        return response.json()

    def collection(self, col_name) -> Collection:
        return FreedbCollection(self, col_name)


class FreedbCollection:
    def __init__(self, database, col_name):
        self._database = database
        self._col_name = col_name

    @property
    def name(self):
        return self._col_name

    def doc(self, doc_id):
        client = self._database._client
        response = client.session.get(client._urljoin(f'/api/databases/{self._database.name}/collections/{self._col_name}/documents/{doc_id}'))
        try:
            response.raise_for_status()
        except requests.HTTPError as ex:
            if ex.response.status_code == 404:
                raise DocumentDotExist()
            raise
        return response.json()

    def put_doc(self, doc_id, doc):
        client = self._database._client
        response = client.session.put(client._urljoin(f'/api/databases/{self._database.name}/collections/{self._col_name}/documents/{doc_id}'), json=doc)
        try:
            response.raise_for_status()
        except requests.HTTPError as ex:
            if ex.response.status_code == 404:
                raise DocumentDotExist()
            raise
        return response.json()

    def merge_doc(self, doc_id, doc):
        client = self._database._client
        response = client.session.patch(client._urljoin(f'/api/databases/{self._database.name}/collections/{self._col_name}/documents/{doc_id}'), json=doc)
        try:
            response.raise_for_status()
        except requests.HTTPError as ex:
            if ex.response.status_code == 404:
                raise DocumentDotExist()
            raise
        return response.json()

    def post(self, doc):
        client = self._database._client
        response = client.session.post(client._urljoin(f'/api/databases/{self._database.name}/collections/{self._col_name}/documents'), json=doc)
        try:
            response.raise_for_status()
        except requests.HTTPError as ex:
            if ex.response.status_code == 404:
                raise DocumentDotExist()
            raise
        return response.json()

    def query(self, query=None, skip=0):
        client = self._database._client
        url = client._urljoin(f'/api/databases/{self._database.name}/collections/{self._col_name}/documents')
        params = {}
        if query:
            params['query'] = json.dumps(query)
        if skip:
            params['skip'] = skip
        
        response = client.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def delete_doc(self, doc_id):
        client = self._database._client
        response = client.session.delete(client._urljoin(f'/api/databases/{self._database.name}/collections/{self._col_name}/documents/{doc_id}'))
        try:
            response.raise_for_status()
        except requests.HTTPError as ex:
            if ex.response.status_code == 404:
                raise DocumentDotExist()
            raise
        return response.json()

    def iter(self, query=None, skip=0):
        return QueryIterator(self, query, skip=skip)


class QueryIterator:
    def __init__(self, collection:Collection, query=None, skip=None):
        self._query=query
        self._doc = []
        self._total = 0
        self._skip = 0
        if skip:
            self._skip = skip
        self._limit = 20
        self._collection = collection
        self._iter = None
        self._do_query()

    def _do_query(self):
        res_data = self._collection.query(self._query, skip=self._skip)
        self._docs = res_data['data']
        self._iter = iter(self._docs)
        self._total = res_data['paging']['total']

    def __next__(self):
        try:
            return next(self._iter)
        except StopIteration:
            if self._skip + self._limit < self._total:
                self._skip += self._limit
                self._do_query()
            return next(self._iter)

    def __iter__(self):
        return self
