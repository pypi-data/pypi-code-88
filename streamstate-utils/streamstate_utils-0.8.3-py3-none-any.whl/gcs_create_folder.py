from google.cloud import storage
from streamstate_utils.utils import get_folder_location
from streamstate_utils.structs import InputStruct
from typing import List, Optional
import google.auth
from google.oauth2 import service_account


def create_gcs_folders(
    bucket_name: str,
    app_name: str,
    inputs: List[InputStruct],
    path_to_json_key: Optional[str] = None,  # if not passed, use workload identity
):
    if path_to_json_key:
        credentials = service_account.Credentials.from_service_account_file(
            path_to_json_key
        )
    else:
        credentials, project = google.auth.default()
    gcs_client = storage.Client(credentials=credentials)
    bucket = gcs_client.get_bucket(bucket_name)
    for input in inputs:
        folder_name = get_folder_location(app_name, input.topic)
        folder_name_with_delimiter = f"{folder_name}/"
        result = 0
        for blob in gcs_client.list_blobs(
            bucket_name, prefix=folder_name, delimiter="/"
        ):
            result = 1

        if result == 0:
            blob = bucket.blob(folder_name_with_delimiter)
            blob.upload_from_string(
                "", content_type="application/x-www-form-urlencoded;charset=UTF-8"
            )
            print("Folder does not exist, creating")
        else:
            print("Folder already exists, skipping")
