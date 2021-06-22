from pathlib import Path
import os

from google.oauth2 import service_account
from google.cloud import storage

from tqdm import tqdm

credentials = service_account.Credentials.from_service_account_file(os.environ['GCLOUD_CREDENTIALS'])
client = storage.Client(project=os.environ['GCLOUD_PROJECT'], credentials=credentials)


def list_blobs_with_prefix(bucket_name, prefix, delimiter=None, client=client):
    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = client.list_blobs(
        bucket_name, prefix=prefix, delimiter=delimiter
    )

    return list(blobs)


def download_blob(blob, dst, client=client):
    with open(dst, 'wb') as file_obj:
        client.download_blob_to_file(blob, file_obj)


def download_gs_folder(bucket, gs_path, dst_path, client=client):
    if not os.path.exists(dst_path):
        os.mkdir(dst_path)
    blobs = list_blobs_with_prefix(bucket, gs_path, client=client)
    blobs = list(blobs)
    print('Download starting - will print "DONE" when finished!')
    for blob in tqdm(blobs):
        fname = Path(blob.name).name
        dst = os.path.join(dst_path, fname)
        print(f'Downloading: {fname}')
        print(f'To: {dst}')
        download_blob(blob, dst, client=client)
    print("DONE")