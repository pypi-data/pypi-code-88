import random
import requests

#%%
def dict_slice(contents, n):
    """Helper function to retrieve the first n elements in a dictionary"""
    return dict(list(contents.items())[:n])

#%%
def dict_random_samples(data, n):
    """Return a dictionary with n random entries from data"""
    keylist = list(data.keys())
    random.shuffle(keylist)
    samples = {}
    for key in keylist[:n]:
        samples[key] = data[key]

    return samples

#%%
def download_file(url, filepath=None, verbose=False):
    """Download file from url and save as filepath. If filepath is omitted
       check if http requests gives a filename, otherwise use url path
       filename and save at current work directory. This do not create the
       dir structure, that must be created beforehand.

    Input:
        url (str): Url to download
        filepath (str): Filepath to download to. If missing try to figure out.
        verbose (bool): Be verbose or not

    Outputs:
        local_filepath (str): Filepath to downloaded file
        filesize (int): Ammount of bytes downloaded

    TODO:
        (Igor): Add a download bar if verbose is true.
    """

    with requests.get(url, stream=True) as req:
        req.raise_for_status()

        # Check if filepath was given, otherwise find from request
        if filepath:
            # Name was given
            local_filepath = filepath
        else:
            # Name from http headers
            if 'content-disposition' in req.headers:
                disposition = req.headers['content-disposition']
                local_filepath = re.findall("local_filepath=(.+)", disposition)[0]
            # Name from url path
            if len(local_filepath) == 0:
                local_filepath = urlparse(url).path.split('/')[-1]

        # Check filesize (only works when stream=False)
        expected_filesize = 0
        if 'Content-Length' in req.headers:
            expected_filesize = int(req.headers['Content-Length'])

        if verbose:
            print (f'Downloading {url} to {local_filepath}', end='')
            if expected_filesize > 0:
                print(f' with {expected_filesize} bytes', end='')
            print()

        filesize = 0
        with open(local_filepath, 'wb') as f:
            for chunk in req.iter_content(chunk_size=None):
                if chunk:
                    filesize += len(chunk)
                    f.write(chunk)

    return local_filepath, filesize

