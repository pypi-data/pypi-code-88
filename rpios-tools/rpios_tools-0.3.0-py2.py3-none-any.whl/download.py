import argparse
import os
import requests
import sys
import zipfile
import tempfile
from typing import List
from urllib.parse import urlparse
import shutil

from bs4 import BeautifulSoup

from rpios_tools.utils import printProgressBar

RASPIOS_DOWNLOAD_PAGE = 'https://downloads.raspberrypi.org/'
RASPIOS_PREFIX = 'raspios_'
IMAGE_DIRNAME = 'images'
RASPIOS_IMAGE_CACHE_DIR = os.path.join(os.environ.get('HOME'), '.local', 'share', 'rpi-os-tools', 'images')


def get_version_url(base_url: str, version_name: str) -> str:
    return os.path.join(base_url, version_name)


def get_download_url(version: str, release: str) -> str:
    release_url = os.path.join(RASPIOS_DOWNLOAD_PAGE, version,
        IMAGE_DIRNAME, release)
    return get_image_release_url(release_url)


def raspios_version_urls(image_downloads_url: str = RASPIOS_DOWNLOAD_PAGE) -> List[List[str]]:
    image_downloads_response = requests.get(image_downloads_url)
    downloads_html = image_downloads_response.text
    soup = BeautifulSoup(downloads_html, 'html.parser')
    links = soup.find_all('a')
    os_versions = []
    for l in links:
        text = l.text.replace('/', '')
        url = l.get('href')
        if text.startswith(RASPIOS_PREFIX):
            os_versions.append([text, os.path.join(image_downloads_url, url)])
    return os_versions


def list_releases(raspios_version: str, raspios_version_url: str) -> List[List[str]]:
    url = os.path.join(raspios_version_url, IMAGE_DIRNAME)
    images = requests.get(url).text
    images_soup = BeautifulSoup(images, 'html.parser')
    images_links = images_soup.find_all('a')
    raspios_release_urls = []
    for il in images_links:
        itext = il.text.replace('/', '')
        iurl = il.get('href')
        if itext.startswith(raspios_version):
            raspios_release_urls.append([itext, os.path.join(url, iurl)])
    return list(reversed(raspios_release_urls))


def get_image_release_url(release_url: str) -> str:
    release_dir = requests.get(release_url).text
    release_soup = BeautifulSoup(release_dir, 'html.parser')
    release_links = release_soup.find_all('a')
    for rl in release_links:
        rtext = rl.text
        rurl = rl.get('href')
        if rtext.endswith('.zip'):
            return os.path.join(release_url, rurl)


def download_raspios_image(url: str, destination_path: str, chunk_size: int = 8192, print_progress: bool = False):
    # NOTE the stream=True parameter below
    def pp(*args, **kwargs):
        if print_progress:
            printProgressBar(*args, **kwargs)
        else:
            pass


    with tempfile.TemporaryDirectory() as tmpdir:
        zip_download_dir = os.path.join(tmpdir, 'download')
        os.makedirs(zip_download_dir)
        zip_download_path = os.path.join(zip_download_dir, os.path.basename(destination_path))
        zip_extract_dir = os.path.join(tmpdir, 'extract')
        os.makedirs(zip_extract_dir)
        
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            num_chunks = int(r.headers.get("content-length")) / chunk_size
            print('Downloading image...')
            pp(0, num_chunks, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r")
            with open(zip_download_path, 'wb') as f:
                for i, chunk in enumerate(r.iter_content(chunk_size=chunk_size)):
                    # If you have chunk encoded response uncomment if
                    # and set chunk_size parameter to None.
                    #if chunk: 
                    f.write(chunk)
                    if print_progress:
                        pp(i, num_chunks, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r")
            pp(num_chunks, num_chunks, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r")
            print('Unzipping image...')
            with zipfile.ZipFile(zip_download_path, 'r') as zip_ref:
                zip_ref.extractall(zip_extract_dir)
            print(os.listdir(zip_extract_dir))
            print(f'Copying .img file to application storage {destination_path}...')
            shutil.copyfile(os.path.join(zip_extract_dir, os.path.basename(destination_path)), destination_path)

    return destination_path


def get_download_path(cache_dir: str, version: str, release: str):
    download_url = get_download_url(version, release)
    return os.path.join(cache_dir, os.path.basename(urlparse(download_url).path.replace('.zip', '.img')))


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--list-os-versions', action='store_true', help='List the available raspios versions available for download and exit')
    p.add_argument('--list-version-releases', action='store_true', help='')
    p.add_argument('--raspios-download-url', type=str, default=RASPIOS_DOWNLOAD_PAGE, help='URL to use as the base download page for the operating system')
    p.add_argument('--raspios-image-cache-dir', type=str, default=RASPIOS_IMAGE_CACHE_DIR, help='Directory to store the downloaded images in')
    p.add_argument('--force-download', action='store_true', help='by default download is skipped if file already exists on local machine')
    p.add_argument('--hide-progress', action='store_true', help='hide download progress bar')
    p.add_argument('--version', type=str, help='version of the operating system to download')
    p.add_argument('--release', type=str, help='which release of the operating system version to download')
    args = p.parse_args()

    if not os.path.exists(args.raspios_image_cache_dir):
        os.makedirs(args.raspios_image_cache_dir)


    available_versions = raspios_version_urls(args.raspios_download_url)
    version_names = [x[0] for x in available_versions]

    if args.list_os_versions:
        print('Listing raspios versions available:')
        print('\t' + '\n\t'.join(version_names))
        sys.exit(1)

    if args.version not in version_names:
        print(f'ERROR: version {args.version} not in {", ".join(version_names)}')
        sys.exit(1)


    available_releases = list_releases(args.version, get_version_url(args.raspios_download_url, args.version))
    release_names = [x[0] for x in available_releases]
    if args.list_version_releases:
        print('Listing {args.version} releases:')
        print('\t' + '\n\t'.join(release_names))
        sys.exit(1)

    if args.release not in release_names:
        print(f'ERROR: release {args.release} for version {args.version} not in {", ".join(release_names)}')
        sys.exit(1)

    if not args.release or not args.version:
        print(f'ERROR: version and release must be specified use -h to get commands to list the available ones')
        sys.exit(1)

    download_url = get_download_url(args.version, args.release)
    download_path = get_download_path(args.raspios_image_cache_dir, args.version, args.release)
    if args.force_download or not os.path.exists(download_path):
        print(f'Downloading raspios:\n\tversion: {args.version}\n\trelease: {args.release}\n\turl: {download_url}\n\tpath: {download_path}')
        download_raspios_image(download_url, download_path, print_progress=not args.hide_progress)
        print(f'Done!')
    else:
        print(f'Already downloaded!')


if __name__ == '__main__':
    main()
