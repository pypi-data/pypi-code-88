import os
import sys
from typing import TypedDict
from yucebio_uploader.base import BaseUploader
import oss2
import click
import logging

class S3Config(TypedDict):
    access_key_id: str
    access_key_secret: str
    region: str
    bucket: str

class Uploader(BaseUploader):
    PLATFROM = 'aws'

    def __init__(self) -> None:
        super().__init__()
        self._auth = None
        self._bucket = None

    @property
    def config(self):
        return self._config('oss', {})

    def configure(self):
        access_id = click.prompt("Please Input ACCESS KEY ID")
        access_secrect = click.prompt("Please Input ACCESS KEY SECRECT")
        region = click.prompt("Please Input Region", default='cn-shenzhen')
        bucket = click.prompt("Please Input Bucket name", default='yucebio')

        self._config['oss'] = {
            "access_key_id": access_id,
            "access_key_secret": access_secrect,
            "region": region,
            "bucket": bucket
        }
        self._config.reload()

    @property
    def s3_config(self) -> S3Config:
        if not self.config:
            self.configure()
        return self.config

    @property
    def endpoint(self) -> str:
        return f"https://oss-{self.s3_config['region']}.aliyuncs.com"

    @property
    def auth(self) -> oss2.Auth:
        if not self._auth:
            self._auth = oss2.Auth(self.s3_config["access_key_id"], self.s3_config['access_key_secret'])
        return self._auth

    @property
    def bucket(self) -> oss2.Bucket:
        if not self._bucket:
            self._bucket = oss2.Bucket(self.auth, self.endpoint, self.s3_config['bucket'])
        return self._bucket

    def upload(self, local: str, remote: str, recursive: bool = False) -> str:
        if not os.path.exists(local):
            raise FileNotFoundError(local)

        def percentage(byte_size, total_bytes):
            if total_bytes:
                rate = int(100 * (float(byte_size) / float(total_bytes)))
                print(click.style(f'\rUploaded {rate}%:', fg='yellow') + click.style('#' * rate, fg='green'), end="")
                sys.stdout.flush()

        click.secho(f"开始上传文件{local} ==> {remote}", fg='green')

        # 检查文件是否存在
        logging.info(f"start upload file: {local} ==> {remote}")
        key = '/'.join(os.sep.split(remote))
        if self.bucket.object_exists(key):
            meta: oss2.models.GetObjectMetaResult = self.bucket.get_object_meta(key)
            if meta.etag.lower() == self.md5(local):
                logging.info(f"remote file [{remote}][md5: {meta.etag}] exists!! ")
                return f"oss://{self.bucket.bucket_name}/{key}"

        self.bucket.put_object_from_file(key, local, progress_callback=percentage)
        logging.info(f"oss://{self.bucket.bucket_name}/{key} file upload success.")

        return f"oss://{self.bucket.bucket_name}/{key}"
