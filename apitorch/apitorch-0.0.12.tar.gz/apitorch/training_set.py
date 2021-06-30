from apitorch.api_client import Client
from apitorch.errors import ArgumentError
from apitorch.routes import training_set_images_route
from apitorch.utils import download_image
from pathlib import Path
from . import logger


def get_images_by_label(training_set_id):
    if not training_set_id:
        raise ArgumentError('training_set_id is a required argument')
    logger.info('Request: Get training set images')
    client = Client()
    url = training_set_images_route(training_set_id)
    response = client.get(url)
    return response.json()


def download_images(training_set_id, path, overwrite=False):
    if not path:
        raise ArgumentError('path is a required argument')
    parent_path = Path(path)
    if not parent_path.is_dir():
        raise ArgumentError(f'could not find directory at path: {path.name}')
    response = get_images_by_label(training_set_id)
    training_set_slug = str(response['training_set_slug'])
    destination = parent_path / training_set_slug
    destination.mkdir(exist_ok=True)
    num_labels = 0
    total_images = 0
    for label_data in response['data']:
        num_labels += 1
        total_images += len(label_data['images'])
    logger.info(
        f'Downloading {total_images} images from {num_labels} labels to {destination}...')

    # loop through labels
    for label_data in response['data']:
        label_name = label_data['label']
        image_dir = destination / str(label_name)
        image_dir.mkdir(exist_ok=True)
        num_images = len(label_data['images'])
        # download individual images
        for image in label_data['images']:
            filename = str(image['filename'])
            image_dest = image_dir / filename
            download_image(image['url'], image_dest, overwrite)
        logger.info(f' - Saved {num_images} images to {image_dir}')
