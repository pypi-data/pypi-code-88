from etl_bq_tools.utils import constants as cons
from etl_bq_tools.utils.memory import get_reduce_memory


def gs_bucket_list_patterns(project_id, bucket_name,
                            prefix_start=None, prefix_end=None,
                            logging=None, key_path=None):
    """
    :param project_id: String
    :param bucket_name: String
    :param prefix_start: String
    :param prefix_end: String
    :param logging: Object
    :param key_path: file.json
    :return: list_blobs
    """
    from color_tools import cprint
    from google.cloud import storage

    if not project_id:
        raise Exception('require var project_id:{project_id} ')
    if not bucket_name:
        raise Exception('require var bucket_name:{bucket_name} ')

    client = storage.Client(project=project_id)
    if project_id and key_path:
        client = storage.Client.from_service_account_json(key_path)

    try:
        bucket = client.get_bucket(bucket_name)
        blobs = bucket.list_blobs()

        filenames = list()
        if prefix_start:
            filenames = list(sorted([str(blob.name) for blob in blobs
                                     if str(blob.name).startswith(prefix_start)]))

        elif prefix_end:
            filenames = list(sorted([str(blob.name) for blob in blobs
                                     if str(blob.name).endswith(prefix_end)]))

        elif prefix_start and prefix_start:
            filenames = list(sorted([str(blob.name) for blob in blobs
                                     if str(blob.name).startswith(prefix_start) and
                                     str(blob.name).endswith(prefix_end)]))

        elif not prefix_start and not prefix_start:
            filenames = list(sorted([str(blob.name) for blob in blobs]))

        if logging:
            logging.info(cons.txt_gs_bucket_list_patterns_success.format(bucket_name))
            cprint(cons.txt_gs_bucket_list_patterns_success.format(bucket_name), 'yellow')
        else:
            cprint(cons.txt_gs_bucket_list_patterns_success.format(bucket_name), 'yellow')
        return filenames
    except Exception as e:
        if logging:
            logging.info(cons.txt_gs_bucket_list_patterns_errors.format(bucket_name))
            cprint(cons.txt_gs_bucket_list_patterns_errors.format(bucket_name), 'yellow')
        else:
            cprint(cons.txt_gs_bucket_list_patterns_errors.format(bucket_name), 'yellow')


def gs_bucket_list_to_df(project_id, bucket_name,
                         filename=None, filename_col=None,
                         logging=None, key_path=None):
    import pandas as pd
    import gc
    from color_tools import cprint
    import gcsfs

    if not project_id:
        raise Exception('require var project_id:{project_id} ')
    if not bucket_name:
        raise Exception('require var bucket_name:{bucket_name} ')
    if not filename:
        raise Exception('require var filename:{filename} ')
    if not filename_col:
        raise Exception('require var filename_col:{filename_col} ')

    try:
        fs = gcsfs.GCSFileSystem(project=project_id,
                                 token=key_path)

        with fs.open(f"gs://{bucket_name}/{filename}") as f:
            frame = pd.read_csv(f)
            frame[f'{filename_col}'] = filename
            df_columns = frame.columns
            frame[df_columns] = frame[df_columns].astype(str)
            df2 = get_reduce_memory(frame, False)
            f.close()
        del frame
        gc.collect()

        if logging:
            logging.info(cons.txt_gs_bucket_list_to_df_success.format(bucket_name, filename))
            cprint(cons.txt_gs_bucket_list_to_df_success.format(bucket_name, filename), 'yellow')
        else:
            cprint(cons.txt_gs_bucket_list_to_df_success.format(bucket_name, filename), 'yellow')

        return df2
    except Exception as e:
        if logging:
            logging.info(cons.txt_gs_bucket_list_to_df_errors.format(bucket_name))
            cprint(cons.txt_gs_bucket_list_to_df_errors.format(bucket_name), 'yellow')
        else:
            cprint(cons.txt_gs_bucket_list_to_df_errors.format(bucket_name), 'yellow')


def storage_download_file(project_id, url=None,
                          logging=None, key_path=None):
    """
     :param project_id: String
     :param url: String
     :param logging: Object
     :param key_path: file.json
     :return: download_blobs
    """

    import os
    from urllib.parse import urlparse
    from color_tools import cprint
    from google.cloud import storage

    if not project_id:
        raise Exception('require var project_id:{project_id} ')
    if not url:
        raise Exception('require var url:{url} ')

    storage_client = storage.Client(project=project_id)
    if project_id and key_path:
        storage_client = storage.Client.from_service_account_json(key_path)

    def decode_gcs_url(url):
        p = urlparse(url)
        path = p.path[1:].split('/', 1)
        bucket, file_path = str(path[0]), path[1]
        return bucket, file_path

    bucket, file_path = decode_gcs_url(url)
    try:
        bucket = storage_client.bucket(bucket)
        blob = bucket.blob(file_path)
        blob.download_to_filename(os.path.basename(file_path))

        if logging:
            logging.info(cons.txt_bucket_download_file_success.format(os.path.basename(file_path)))
            cprint(cons.txt_bucket_download_file_success.format(os.path.basename(file_path)), 'yellow')
        else:
            cprint(cons.txt_bucket_download_file_success.format(os.path.basename(file_path)), 'yellow')

    except Exception as e:
        if logging:
            logging.info(cons.txt_bucket_download_file_errors.format(os.path.basename(file_path)))
            cprint(cons.txt_bucket_download_file_errors.format(os.path.basename(file_path)), 'yellow')
        else:
            cprint(cons.txt_bucket_download_file_errors.format(os.path.basename(file_path)), 'yellow')


def storage_upload_file(project_id, bucket_name=None,
                        destination_blob_name=None,
                        source_file_name=None,
                        is_public=False,
                        logging=None,
                        key_path=None):
    """
     :param project_id: String
     :param bucket_name: String
     :param destination_blob_name: String
     :param source_file_name: String
     :param logging: Object
     :param key_path: file.json
     :return: uploads_blobs
    """
    import os
    from color_tools import cprint
    from google.cloud import storage

    if not project_id:
        raise Exception('require var project_id:{project_id} ')
    if not bucket_name:
        raise Exception('require var bucket_name')
    if not destination_blob_name:
        raise Exception('require var destination_blob_name')
    if not source_file_name:
        raise Exception('require var source_file_name')

    storage_client = storage.Client(project=project_id)
    if project_id and key_path:
        storage_client = storage.Client.from_service_account_json(key_path)

    try:
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)
        if is_public:
            blob.make_public()

        if logging:
            logging.info(cons.txt_bucket_upload_file_success.format(os.path.basename(source_file_name)))
            cprint(cons.txt_bucket_upload_file_success.format(os.path.basename(source_file_name)), 'yellow')
        else:
            cprint(cons.txt_bucket_upload_file_success.format(os.path.basename(source_file_name)), 'yellow')

    except Exception as e:
        if logging:
            logging.info(cons.txt_bucket_upload_file_errors.format(os.path.basename(source_file_name)))
            cprint(cons.txt_bucket_upload_file_errors.format(os.path.basename(source_file_name)), 'yellow')
        else:
            cprint(cons.txt_bucket_upload_file_errors.format(os.path.basename(source_file_name)), 'yellow')


def storage_delete_file(project_id,
                        bucket_name,
                        source_file_name=None,
                        logging=None,
                        key_path=None):
    """
     :param project_id: String
     :param bucket_name: String
     :param source_file_name: String
     :param logging: Object
     :param key_path: file.json
     :return: uploads_blobs
    """
    import os
    from color_tools import cprint
    from google.cloud import storage

    if not project_id:
        raise Exception('require var project_id:{project_id} ')
    if not bucket_name:
        raise Exception('require var bucket_name')
    if not source_file_name:
        raise Exception('require var source_file_name')

    storage_client = storage.Client(project=project_id)
    if project_id and key_path:
        storage_client = storage.Client.from_service_account_json(key_path)

    try:
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(source_file_name)
        blob.delete()

        if logging:
            logging.info(cons.txt_storage_delete_file_success.format(os.path.basename(source_file_name)))
            cprint(cons.txt_storage_delete_file_success.format(os.path.basename(source_file_name)), 'yellow')
        else:
            cprint(cons.txt_storage_delete_file_success.format(os.path.basename(source_file_name)), 'yellow')

    except Exception as e:
        if logging:
            logging.info(cons.txt_storage_delete_file_errors.format(os.path.basename(source_file_name)))
            cprint(cons.txt_storage_delete_file_errors.format(os.path.basename(source_file_name)), 'yellow')
        else:
            cprint(cons.txt_storage_delete_file_errors.format(os.path.basename(source_file_name)), 'yellow')


def storage_delete_folder(project_id=None,
                          bucket_name=None,
                          path_folder=None,
                          logging=None,
                          key_path=None):
    """
     :param bucket_name: The bucket name in which the file is to be placed
     :param path_folder: Folder name to be deleted
     :param logging: Object
     :param key_path: file.json
    :return: returns nothing
    """
    import os
    from color_tools import cprint
    from google.cloud import storage

    if not project_id:
        raise Exception('require var project_id:{project_id} ')
    if not bucket_name:
        raise Exception('require var bucket_name')
    if not path_folder:
        raise Exception('require var path_folder')

    storage_client = storage.Client(project=project_id)
    if project_id and key_path:
        storage_client = storage.Client.from_service_account_json(key_path)

    bucket = storage_client.bucket(bucket_name)
    try:
        bucket.delete_blobs(blobs=list(bucket.list_blobs(prefix=path_folder)))

        if logging:
            logging.info(cons.txt_storage_delete_folder_success.format(os.path.basename(path_folder)))
            cprint(cons.txt_storage_delete_folder_success.format(os.path.basename(path_folder)), 'yellow')
        else:
            cprint(cons.txt_storage_delete_folder_success.format(os.path.basename(path_folder)), 'yellow')

    except Exception as e:
        if logging:
            logging.info(cons.txt_storage_delete_folder_errors.format(os.path.basename(path_folder)))
            cprint(cons.txt_storage_delete_folder_errors.format(os.path.basename(path_folder)), 'yellow')
        else:
            cprint(cons.txt_storage_delete_folder_errors.format(os.path.basename(path_folder)), 'yellow')
