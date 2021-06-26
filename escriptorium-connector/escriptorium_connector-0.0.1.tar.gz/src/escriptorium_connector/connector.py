import requests
import logging
import backoff

logger = logging.getLogger(__name__)

class EscriptoriumConnector:
    def __init__(self, base_url: str, api_url: str, token: str, project: str = None):
        # Make sure the urls terminates with a front slash
        self.api_url = api_url if api_url[-1] == '/' else api_url + '/'
        self.base_url = base_url if base_url[-1] == '/' else base_url + '/'

        self.headers = {'Accept': 'application/json', 'Authorization': f'Token {token}'}
        self.project = project

    @backoff.on_exception(backoff.expo, requests.exceptions.HTTPError, max_time=60)
    def __get_url(self, url: str):
        r = requests.get(url, headers=self.headers)
        r.raise_for_status()
        return r

    @backoff.on_exception(backoff.expo, requests.exceptions.HTTPError, max_time=60)
    def __post_url(self, url: str, payload: object, files: object = None) -> object:
        r = requests.post(url, data=payload, files=files, headers=self.headers) if files is not None else requests.post(url, data=payload, headers=self.headers)
        r.raise_for_status()
        return r

    @backoff.on_exception(backoff.expo, requests.exceptions.HTTPError, max_time=60)
    def __put_url(self, url: str, payload: object, files: object = None) -> object:
        r = requests.put(url, data=payload, files=files, headers=self.headers) if files is not None else requests.put(url, data=payload, headers=self.headers)
        r.raise_for_status()
        return r
    
    @backoff.on_exception(backoff.expo, requests.exceptions.HTTPError, max_time=60)
    def __delete_url(self, url: str) -> object:
        r = requests.delete(url, headers=self.headers)
        r.raise_for_status()
        return r

    def get_documents(self):
        r = self.__get_url(f'{self.api_url}documents')
        info = r.json()
        documents = info['results']
        while info['next'] is not None:
            r = self.__get_url(info['next'])
            info = r.json()
            documents = documents + info['results']

        return documents

    def get_document(self, pk: int):
        r = self.__get_url(f'{self.api_url}documents/{pk}')
        return r.json()
    
    def get_document_part(self, doc_pk: int, part_pk: int):
        r = self.__get_url(f'{self.api_url}documents/{doc_pk}/parts/{part_pk}')
        return r.json()
    
    def get_document_part_line(self, doc_pk: int, part_pk: int, line_pk: int):
        r = self.__get_url(f'{self.api_url}documents/{doc_pk}/parts/{part_pk}/lines/{line_pk}')
        return r.json()

    def get_document_part_region(self, doc_pk: int, part_pk: int, region_pk: int):
        regions = self.get_document_part_regions(self, doc_pk, part_pk)
        region = [x for x in regions if x['pk'] == region_pk]
        return region[0] if region else None

    def get_document_part_line_transcription(self, doc_pk: int, part_pk: int, line_pk: int, transcription_pk: int):
        transcriptions = self.get_document_part_line_transcriptions(self, doc_pk, part_pk, line_pk)
        transcription = [x for x in transcriptions if x['pk'] == transcription_pk]
        return transcription[0] if transcription else None

    def get_document_part_line_transcriptions(self, doc_pk: int, part_pk: int, line_pk: int):
        line = self.get_document_part_line(self, doc_pk, part_pk, line_pk)
        return line['transcriptions']

    def get_document_part_regions(self, doc_pk: int, part_pk: int):
        r = self.__get_url(f'{self.api_url}documents/{doc_pk}/parts/{part_pk}')
        part = r.json()
        return part['regions']

    def get_document_transcription(self, doc_pk: int, transcription_pk: int):
        r = self.__get_url(f'{self.api_url}documents/{doc_pk}/transcriptions/{transcription_pk}')
        return r.json()

    def get_document_transcriptions(self, doc_pk: int):
        r = self.__get_url(f'{self.api_url}documents/{doc_pk}/transcriptions')
        return r.json()

    def get_document_part_lines(self, doc_pk: int, part_pk: int):
        r = self.__get_url(f'{self.api_url}documents/{doc_pk}/parts/{part_pk}/lines')
        return r.json()

    def get_document_images(self, document_pk: str):
        r = self.__get_url(f'{self.api_url}documents/{document_pk}/parts')
        image_info = r.json()
        image_names = image_info['results']
        while image_info['next'] is not None:
            r = self.__get_url(image_info['next'])
            image_info = r.json()
            image_names = image_names + image_info['results']

        return image_names

    def delete_document_parts(self, document_pk: str, start: int, end: int):
        parts = self.get_document_images(document_pk)
        for part in parts[start:end]:
            r = self.__delete_url(f'{self.api_url}documents/{document_pk}/parts/{part["pk"]}')

    def get_image(self, img_url: str):
        r = self.__get_url(f'{self.base_url}{img_url}')
        return r.content

    def create_document(self, doc_data: object):
        if self.project:
            doc_data['project'] = self.project
        return self.__post_url(f'{self.api_url}documents/', doc_data)

    def create_image(self, document_pk: str, image_data_info: object, image_data: bytes):
        return self.__post_url(f'{self.api_url}documents/{document_pk}/parts/', image_data_info,
                               {'image': (image_data_info['filename'], image_data)})


if __name__ == '__main__':
    source_url = 'https://www.escriptorium.fr/'
    source_api = f'{source_url}api/'
    source_token = ''
    source = EscriptoriumConnector(source_url, source_api, source_token)
    print(source.get_documents())
