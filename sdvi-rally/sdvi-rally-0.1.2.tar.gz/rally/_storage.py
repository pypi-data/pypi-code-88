import functools
from urllib.parse import urlparse

from ._session import _getSession
from . import exceptions


@functools.lru_cache()
def _getStorageLocationFromUrl(name):
    """ Get the a Storage Location from a URL """

    # The V2 API doesn't give us great tools here, force the usage of RSL:// syntax so
    # we can easily convert back and forth from URIs and StorageLocations
    parsed = urlparse(name)
    if parsed.scheme:
        assert parsed.scheme == 'rsl', f'scheme must be rsl, not {parsed.scheme}'
        name = parsed.netloc

    s = _getSession()
    params = {'filter': 'name=' + name}  # todo requests cannot handle marshalling our nested dict, do it by hand

    resp = s.get(f'v2/storageLocations', params=params)

    results = resp.json()['data']

    if len(results) == 0:
        raise ValueError(f'No StorageLocation named {name}')

    if len(results) > 1:
        raise ValueError(f'Ambiguous StorageLocation name {name}')

    return results[0]


@functools.lru_cache()
def _getStoragePartsFromUrl(url):
    """ Returns a tuple containing a storage location and key (object) name given a supported url
    Schema currently supported: RSL, S3, AC, AZ, and GS

    :param url: the URI to parse
    :type url: str
    """

    parsed = urlparse(url)
    if parsed.scheme not in ('rsl', 's3', 'az', 'gs', 'ac'):
        raise ValueError('not a supported url')

    # BUG having more than one Location referencing a bucket is complicated, perhaps even stupid
    #  a location is a combination of bucket + prefix, which each pair can have its own Rally permissions against...
    #  but many operations in Rally + S3 will happy accept a filename with with "/" in the name which is considered a
    #  prefix so if Rally maps Bucket=Foo + prefix='aaa' as Location "Alpha" and Bucket=Foo + prefix='aaa/bbb' as
    #  Location "Beta" it is possible to select Location "Alpha" and write to "Beta" using filenames with
    #  'bbb/name.txt'.  This lets you bypass more restrictive permissions in "Beta" if present.  Because Rally mixes
    #  the use of URL and StorageLocation names as identifiers it isn't hard to imagine this being exploited not to
    #  mention confusing

    storage = {
        'rsl': {'route': 'storageLocations', 'filter': 'name'},
        's3': {'route': 's3StorageLocations', 'filter': 'bucketName'},
        'az': {'route': 'azureStorageLocations', 'filter': 'bucketName'},
        'gs': {'route': 'googleStorageLocations', 'filter': 'bucketName'},
        'ac': {'route': 'alibabaStorageLocations', 'filter': 'bucketName'}
    }

    route = storage[parsed.scheme]['route']
    filterParam = storage[parsed.scheme]['filter']
    objectName = parsed.path

    results = _getAllLocations(route, filterParam, parsed.netloc)

    if not len(results):
        raise exceptions.NotFound(f'Storage Location {parsed.netloc}')
    if parsed.scheme == 'rsl' and len(results) > 1:
        raise ValueError(f'Ambiguous StorageLocation name {parsed.netloc}')

    location = results[0]
    if not int(location['id']) or parsed.scheme == 'rsl':
        location['id'] = 'PlatformBucket' if not location['id'] else location['id']
        return location, objectName[1:]

    return _findCorrectBucketAndObject(objectName, results)


def _findCorrectBucketAndObject(objectName, locations):
    bucketsByPrefix = {b['attributes']['prefix'] or '/': b for b in locations}

    prefixMatches = {}
    for prefix in bucketsByPrefix:
        _, _, substring = objectName.partition(prefix)
        if substring:
            prefixMatches[substring] = prefix

    # the shortest substring has the longest prefix match, and is the one we want
    keyName = sorted(prefixMatches, key=len)[0]
    location = bucketsByPrefix[prefixMatches[keyName]]

    return location, keyName


def _getAllLocations(url, param, netloc):
    results = []
    marker = None

    while True:
        if marker:
            path = marker
            params = None
        else:
            path = f'v2/{url}'
            params = {'filter': f'{param}={netloc}', 'page': '1p100'}
        page = _getSession().get(path, params=params).json()
        marker = page['links']['next']
        results = results + (page['data'])

        if not marker:
            return results
