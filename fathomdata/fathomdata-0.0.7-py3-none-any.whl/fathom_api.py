import requests
import pandas as pd


from .document import Document

__fathom_state = {
    'environment': 'demo',
    'api_key': None,
    'important_document_columns': [
        'DocumentId',
        'ReceivedTime',
        'Source',
        'ContentType',
        # 'Filename',
        'UploadedByUserId',
        'IsValidated'
    ],
    'document_cache': {}
}


def set_api_key(api_key):
    __fathom_state['api_key'] = api_key


def _set_environment(environment):
    __fathom_state['environment'] = environment


def get_documents_df(document_type='batch'):

    if document_type == 'batch':

        url = __get_access_url()
        headers = __get_request_headers()

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        dataframe = pd.DataFrame.from_dict(response.json())
        dataframe = dataframe[__fathom_state['important_document_columns']]

        return dataframe

    return None


def get_document(document_id, document_type='processed'):

    if not document_id in __fathom_state['document_cache']:
        __fathom_state['document_cache'][document_id] = {}

    if not document_type in __fathom_state['document_cache'][document_id]:

        url = f"{__get_access_url()}/{document_id}/{document_type}"
        headers = __get_request_headers()

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        __fathom_state['document_cache'][document_id][document_type] = response.json()

    document_data = __fathom_state['document_cache'][document_id][document_type]
    return Document(document_data)


def ingest_document(path, document_category=None):

    upload_url = __get_ingest_url()
    headers = __get_request_headers()
    filename = path.split('/')[-1]
    query_parameters = {
        'filename': filename,
        'documentCategory': document_category
    }

    fathom_response = requests.get(upload_url, headers=headers, params=query_parameters)
    fathom_response.raise_for_status()

    fathom_response_data = fathom_response.json()
    s3_fields_data = fathom_response_data['fields']
    new_document_key = fathom_response_data['fields']['key']
    presigned_link_url = fathom_response_data['url']
    files = {'file': open(path, 'rb')}

    s3_response = requests.post(presigned_link_url, data=s3_fields_data, files=files)
    s3_response.raise_for_status()

    return new_document_key


def __get_access_url():

    url = __get_api_base_url()
    url = url.replace('<api_path>', 'access')
    url = url.replace('<sandbox_subdomain>', 'n3b7m86hzi')
    url += '/record'

    return url


def __get_ingest_url():

    url = __get_api_base_url()
    url = url.replace('<api_path>', 'ingest')
    url = url.replace('<sandbox_subdomain>', 'o836upnv30')
    url += '/upload'

    return url


def __get_api_base_url():

    if __fathom_state['environment'] in ['demo', 'staging']:
        return f"https://{__fathom_state['environment']}.api.fathom.one/<api_path>"

    elif __fathom_state['environment'] == 'sandbox':
        return "https://<sandbox_subdomain>.execute-api.us-east-1.amazonaws.com/dev"

    else:
        raise Exception("Environment is misconfigured.")


def __get_request_headers():

    return {
        'x-api-key': __fathom_state['api_key']
    }
