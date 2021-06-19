from apitorch.errors import ArgumentError
from apitorch.api_client import Client
from apitorch.routes import CLASSIFY_IMAGE
from . import logger

MAX_CLASSIFIERS_ALLOWED = 10
POST_ARGS_WHITELIST = ['image_url', 'classifiers']


def classify_image(**kwargs):
    if not 'image_url' in kwargs:
        raise ArgumentError('`image_url` must be specified')
    if not 'classifiers' in kwargs:
        raise ArgumentError('At least one classifier must be specified')

    data = {key: kwargs[key] for key in POST_ARGS_WHITELIST}
    classifiers = [data['classifiers']] if isinstance(
        data['classifiers'], str) else data['classifiers']
    if not isinstance(classifiers, list):
        raise ArgumentError('`classifiers` is not properly defined')
    if len(classifiers) < 1 or len(classifiers) > MAX_CLASSIFIERS_ALLOWED:
        raise ArgumentError('Number of `classifiers` must be between 1 and 10')

    client = Client()
    logger.debug('Classify image_url')
    response = client.post(CLASSIFY_IMAGE, *data)
    print(f'got response {response}')
