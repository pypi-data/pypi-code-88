from json.decoder import JSONDecodeError
import requests
from biolib.biolib_errors import BioLibError
from biolib.biolib_logging import logger


class BiolibApiClient:
    api_client = None

    @staticmethod
    def initialize(biolib_host):
        BiolibApiClient.api_client = BiolibApiClient()
        BiolibApiClient.api_client.refresh_token = ''
        BiolibApiClient.api_client.access_token = ''
        BiolibApiClient.api_client.base_url = f'{biolib_host}/api'

    @staticmethod
    def get():
        api_client = BiolibApiClient.api_client
        if api_client is not None:
            return api_client
        else:
            raise BioLibError("Attempted to use uninitialized API client")

    def __init__(self):
        self.refresh_token = None
        self.access_token = None
        self.base_url = None

    def set_host(self, biolib_host):
        self.base_url = f'{biolib_host}/api'

    def login(self, api_token, exit_on_failure=False):
        if api_token is None:
            if exit_on_failure:
                raise BioLibError('Error: Attempted login, but BIOLIB_TOKEN was not set, exiting...')
            else:
                logger.debug('Attempted login, but BIOLIB_TOKEN was not set, so continuing without logging in')
                return

        response = requests.post(f'{self.base_url}/user/api_tokens/exchange/',
                                 json={'token': api_token})
        try:
            json_response = response.json()
        except JSONDecodeError as error:
            logger.error('Could not decode response from server as JSON:')
            raise BioLibError(response.text) from error
        if not response.ok:
            logger.error('Login with API token failed:')
            raise BioLibError(json_response['detail'])
        else:
            self.refresh_token = json_response['refresh_token']
            self.access_token = json_response['access_token']
            logger.info('Successfully authenticated')
