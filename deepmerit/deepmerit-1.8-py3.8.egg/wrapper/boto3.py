import boto3
import mimetypes
from six.moves.urllib.parse import urlencode
from io import BytesIO
import pandas as pd
from PIL import Image
import pickle
import json
import h5py
import s3fs
import numpy as np
import os

client = boto3.client('s3') #low-level functional API
s3_resource = boto3.resource('s3')

def s3_upload_file(bucketName, key, localFilePath, contentType=' ',tagging = ' '):
    """
    Arguments:
    ------------------------------------------------------------------------------------------------------------------------------------
    bucketName    : Type - string     | The Object's bucket_name identifier | **[REQUIRED]**  |
    key           : Type - string     | S3 The Object's key identifier      | **[REQUIRED]**  | Example., "example-folder/filename.csv" |
    localFilePath : Type - string     | File path in local directory        | **[REQUIRED]**  |
    contentType   : Type - string     | Media type of the given oobject     | Example., for .csv file contentType is 'text/csv'
    tagging       : Type - dictionary | Input Tags for the given object     | Example., {"key1":"value1","key2":"value2"}
    ------------------------------------------------------------------------------------------------------------------------------------
    Output        : Returns "Success" if upload has been done.
    """
    if key[0] == "/":
        return "Please Don't include '/' at the intial of key"
    if contentType == ' ':
        contentType = mimetypes.guess_type(localFilePath, strict=True)[0]
    if tagging == ' ':
        s3_resource.Object(bucketName, key).upload_file(Filename=localFilePath, ExtraArgs={'ContentType':contentType})
    else:
        s3_resource.Object(bucketName, key).upload_file(Filename=localFilePath, ExtraArgs={'ContentType':contentType,'Tagging': urlencode(tagging)})
    return "Success"


def s3_read_csv(bucketName, key):
    """
    Arguments:
    ---------------------------------------------------------------------------------------
    bucketName  : Type - string | The bucket name containing the object | **[REQUIRED]**  |
    key         : Type - string | Key of the object to get              | **[REQUIRED]**  |
    ---------------------------------------------------------------------------------------
    """
    client = boto3.client('s3') #low-level functional API
    obj = client.get_object(Bucket=bucketName, Key=key)
    return pd.read_csv(obj['Body'])

def s3_read_image(bucketName, key):
    """
    Arguments:
    ---------------------------------------------------------------------------------------
    bucketName  : Type - string | The bucket name containing the object | **[REQUIRED]**  |
    key         : Type - string | Key of the object to get              | **[REQUIRED]**  |
    ---------------------------------------------------------------------------------------
    """
    obj = client.get_object(Bucket=bucketName, Key=key)['Body'].read()
    return Image.open(BytesIO(obj))


def s3_read_pickle(bucketName, key):
    """
    Arguments:
    ---------------------------------------------------------------------------------------
    bucketName  : Type - string | The bucket name containing the object | **[REQUIRED]**  |
    key         : Type - string | Key of the object to get              | **[REQUIRED]**  |
    ---------------------------------------------------------------------------------------
    """
    return pickle.loads(s3_resource.Bucket(bucketName).Object(key).get()['Body'].read())


def s3_read_json(bucketName, key):
    """
    Arguments:
    ---------------------------------------------------------------------------------------
    bucketName  : Type - string | The bucket name containing the object | **[REQUIRED]**  |
    key         : Type - string | Key of the object to get              | **[REQUIRED]**  |
    ---------------------------------------------------------------------------------------
    """
    obj = client.get_object(Bucket=bucketName, Key=key)
    return json.loads(obj['Body'].read())

def s3_read_h5(s3FilePath):
    """
    Argument:
    --------------------------------------------------------------------------------
    s3FilePath  : Type - string | Object file path in s3         | **[REQUIRED]**  |
    --------------------------------------------------------------------------------
    """
    s3 = s3fs.S3FileSystem()
    return h5py.File(s3.open(s3FilePath))


def s3_create_empty_folder(bucket_name,folder_path):
    """
    Arguments:
    -------------------------------------------------------------------------------------------
    bucketName  : Type - string | The bucket name for containing the folder | **[REQUIRED]**  |
    folder_path : Type - string |  The Folder Path                          | **[REQUIRED]**  |
    -------------------------------------------------------------------------------------------
    """
    if folder_path[0] == "/":
        return "Please Don't include '/' at the intial of folder_path"
    if folder_path[-1] != "/":
        return "Please include '/' at the end of folder_path"
    client.put_object(Bucket=bucket_name, Key=folder_path)
    return "Success"

def s3_read_multiple_images(bucketName,key_path):
    """
    Arguments:
    -------------------------------------------------------------------------------------------
    bucketName    : Type - string     | The Object's bucket_name identifier | **[REQUIRED]**  |
    key           : Type - string     | S3 folder that contains objects     | **[REQUIRED]**  |
    -------------------------------------------------------------------------------------------
    Output        : Returns List which contains objects as array.
    """
    bucket = s3_resource.Bucket(bucketName)
    keys=[]
    for obj in bucket.objects.filter(Prefix=key_path):
        keys.append(obj.key)
    img_list = []
    for i in keys:
        if not i.endswith("/"):
            im1 = Image.open(bucket.Object(i).get()['Body'])
            img_list.append(np.array(im1))
    return img_list

def upload_folder_to_s3(bucketName, inputDir, s3Path,tagging=' '):
    """
    Arguments:
    ---------------------------------------------------------------------------------------------------------------------------------------------------
    bucketName    : Type - string     | The Object's bucket_name identifier         | **[REQUIRED]**  |
    inputDir      : Type - string     | Local Input directory path                  | **[REQUIRED]**  |
    s3Path        : Type - string     | S3 folder path to upload inputDir's objects | **[REQUIRED]**  | Example., "example-folder/example-subfolder/" |
    tagging       : Type - dictionary | Input Tags for the given object             | [Option]        | Example., {"key1":"value1","key2":"value2"}
    ---------------------------------------------------------------------------------------------------------------------------------------------------
    Output        : Returns "Success" if upload has been done.
    """

    try:
        s3bucket = s3_resource.Bucket(bucketName)

        if s3Path[0] == "/":
            return "Please Don't include '/' at the intial of s3Path"
        if s3Path[-1] != "/":
            return "Please include '/' at the end of s3Path"

        for path, subdirs, files in os.walk(inputDir):
            for file in files:
                dest_path = path.replace(inputDir,"")
                __s3file = os.path.normpath(s3Path + '/' + dest_path + '/' + file)
                __local_file = os.path.join(path, file)
                if tagging == ' ':
                    s3bucket.upload_file(__local_file, __s3file)
                else:
                    s3bucket.upload_file(__local_file, __s3file, ExtraArgs={'Tagging': urlencode(tagging)})
        return "Success"
    except Exception as e:
        print(" ... Failed!! Quitting Upload!!")
        print(e)
        raise e
