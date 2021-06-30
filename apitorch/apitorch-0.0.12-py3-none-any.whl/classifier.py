from apitorch.api_client import Client
from apitorch.errors import ArgumentError
from apitorch.routes import classify_image_route
from . import logger

MAX_CLASSIFIERS_ALLOWED = 10
POST_ARGS_WHITELIST = ['classifiers', 'image_url']


def classify_image(**kwargs):
    if not 'image_url' in kwargs:
        raise ArgumentError('image_url is a required argument')
    if not 'classifiers' in kwargs:
        raise ArgumentError('At least one classifier must be specified')

    postdata = {key: kwargs[key] for key in POST_ARGS_WHITELIST}
    if isinstance(postdata['classifiers'], str):
        postdata['classifiers'] = [postdata['classifiers']]
    if not isinstance(postdata['classifiers'], list):
        raise ArgumentError('`classifiers` is not properly defined')
    num_classifiers = len(postdata['classifiers'])
    if num_classifiers < 1 or num_classifiers > MAX_CLASSIFIERS_ALLOWED:
        raise ArgumentError('Number of classifiers must be between 1 and 10')
    logger.debug(f'POST data: {postdata}')

    logger.info('Request: Classify image')
    client = Client()
    response = client.post(classify_image_route(), postdata)
    return response.json()
